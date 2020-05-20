from pyld import jsonld
from pyshacl import validate

data = {
    "@context": { "@vocab": "http://schema.org/" },
    "@id": "http://example.org/ns#Bob",
    "@type": "Person",
    "givenName": "Robert",
    "familyName": "Junior",
    "birthDate": "1961-07-07",
    "deathDate": "1968-09-10",
    "address": {
        "@id": "http://example.org/ns#BobsAddress",
        "streetAddress": "1600 Amphitheatre Pkway",
        "postalCode": 94040
    }
}


normalized = jsonld.normalize(
    data, {'algorithm': 'URDNA2015', 'format':
        'application/n-quads'})
r = validate(normalized, shacl_graph='validation/addressShape.ttl', meta_shacl=True, debug=True)
conforms, results_graph, results_text = r
print(conforms)