import os
import json
from pyld import jsonld
import rdflib as rl
from reproschema.jsonldutils import to_newformat


def create_release(version):
    # read all the terms
    terms = []
    for root, dirs, files in os.walk("terms"):
        for name in files:
            terms.extend(json.loads(to_newformat(os.path.join(root, name),
                                                 "jsonld")))

    kwargs = {"algorithm": "URDNA2015", "format": "application/n-quads"}
    data = jsonld.normalize(terms, kwargs)

    with open("contexts/base") as fp:
        base_context = json.load(fp)

    g = rl.Graph()
    for key, val in base_context["@context"].items():
        if not key.startswith("@"):
            g.namespace_manager.bind(key, val)
    g.parse(data=data, format="nt")

    # write n-triples and turtle files
    os.makedirs(f"releases/{version}", exist_ok=True)
    with open(f"releases/{version}/reproschema.nt", "w") as fp:
        fp.write(data) #g.serialize(format="nt").decode())
    with open(f"releases/{version}/reproschema.ttl", "w") as fp:
        fp.write(g.serialize(format="turtle").decode())
    return g


if __name__ == "__main__":
    version = "1.0-rc1"
    create_release(version)
