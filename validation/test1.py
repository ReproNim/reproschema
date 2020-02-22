# from rdflib import Graph, plugin
# from rdflib.serializer import Serializer
#
# testrdf = '''
# @prefix dc: <http://purl.org/dc/terms/> .
# <http://example.org/about>
# dc:title "Someone's Homepage"@en .
# '''
#
# testjson = '''{
#     "@context": {
#         "@language": "en",
#         "@vocab": "http://purl.org/dc/terms/"
#     },
#     "@id": "http://example.org/about",
#     "title": "Someone's Homepage"
# }'''
# g = Graph().parse(data=testjson, format='json-ld')
#
# print(g.serialize(format='n3'))


from pyld import jsonld
import json

# read file
# with open('../activities/PHQ-9/phq9_schema', 'r') as myfile:
#     data=myfile.read()

from urllib.request import urlopen
import json

url = 'https://raw.githubusercontent.com/sanuann/reproschema/master/activities/PHQ-9/phq9_schema'
data = json.loads(urlopen(url).read().decode("utf-8"))

doc2 = {
    "@context": {
        "day" : {
          "@id" : "test:day"
        },
        "month" : {
          "@id" : "test:month"
        },
        "myList" : {
          "@id" : "test:myList"
        },
        "year" : {
          "@id" : "test:year"
        },
        "schema" : "http://schema.org/",
        "rdf" : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "xsd" : "http://www.w3.org/2001/XMLSchema#",
        "test" : "http://www.test.com/ns#",
        "reproterms": "https://raw.githubusercontent.com/ReproNim/reproschema/master/terms/>",
        "isAbout": {
            "@id": "reproterms:isAbout",
            "@type": "@vocab"
        },
      },

    "@id": "test:MyNode",
    "@type": "test:MyTargetClass",
    "myList": [
      {
        "year": "2019",
        "month": "October",
        "day": "29"
      },
      {
        "year": "2018",
        "month": "January",
        "day": "17"
      }
    ]
}

doc = {
    "@context": [
    "https://raw.githubusercontent.com/ReproNim/reproschema/master/contexts/generic",
    "https://raw.githubusercontent.com/ReproNim/reproschema/master/activities/PHQ-9/phq9_context"
    ],
    "@type": "reproschema:Activity",
    "@id": "https://raw.githubusercontent.com/ReproNim/reproschema/master/activities/PHQ-9/phq9_schema",
    "variableMap": [
        {
        "variableName": "phq9_1",
        "isAbout": "phq9_1"
        }
    ]
}

# exp = jsonld.expand(doc)
normalized = jsonld.normalize(
    data, {'algorithm': 'URDNA2015', 'format':
        'application/n-quads'})

print(normalized)
