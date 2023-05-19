import os
import sys
import json
from pyld import jsonld
import rdflib as rl
from shutil import copyfile
from reproschema.jsonldutils import to_newformat


def create_release(version):
    # read all the terms
    terms = []
    for root, dirs, files in os.walk("terms"):
        for name in files:
            terms.extend(json.loads(to_newformat(os.path.join(root, name), "jsonld")))

    kwargs = {"algorithm": "URDNA2015", "format": "application/n-quads"}
    data = jsonld.normalize(terms, kwargs)

    os.makedirs(f"releases/{version}", exist_ok=True)
    copyfile("contexts/base", f"releases/{version}/base")
    copyfile("contexts/generic", f"releases/{version}/generic")
    with open(f"releases/{version}/base") as fp:
        base_context = json.load(fp)
    compacted = jsonld.compact(terms, ctx=base_context)

    g = rl.Graph()
    for key, val in base_context["@context"].items():
        if not key.startswith("@"):
            g.namespace_manager.bind(key, val)
    g.parse(data=data, format="nt")

    # write n-triples and turtle files
    with open(f"releases/{version}/reproschema.jsonld", "w") as fp:
        json.dump(compacted, fp, indent=2)
    with open(f"releases/{version}/reproschema.nt", "w") as fp:
        fp.write(data)
    with open(f"releases/{version}/reproschema.ttl", "w") as fp:
        fp.write(g.serialize(format="turtle"))

    g1 = rl.Graph()
    g1.parse("validation/reproschema-shacl.ttl", format="turtle")
    with open(f"releases/{version}/reproschema-shacl.ttl", "w") as fp:
        fp.write(g1.serialize(format="turtle"))

    return g


if __name__ == "__main__":
    if len(sys.argv) < 2:
        version = "master"
    else:
        version = sys.argv[1]
    print(f"Generating release for version: {version}")
    create_release(version)
