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
with open('../activities/PHQ-9/phq9_schema', 'r') as myfile:
    data=myfile.read()
doc = {
#     "@context": {
#         "@version": 1.1,
#     "reproterms": "https://raw.githubusercontent.com/sanuann/schema-standardization/master/terms/",
#      "reproschema": "https://raw.githubusercontent.com/sanuann/schema-standardization/master/schemas/",
# "xsd": "http://www.w3.org/2001/XMLSchema#",
#     "ui" : "@nest",
#     "preamble": {
#         "@id": "reproterms:preamble",
#         "@container": "@language"
#     },
#     "shuffle": {
#             "@id": "reproterms:shuffle",
#             "@type": "xsd:boolean",
#             "@nest": "ui"
#     },
#     "@base": "https://raw.githubusercontent.com/sanuann/schema-standardization/master/activities/PHQ-9/"
#     },
    "@context": [
        {
            "@version": 1.1,
            "reproterms": "https://raw.githubusercontent.com/sanuann/schema-standardization/master/terms/",
            "reproschema": "https://raw.githubusercontent.com/sanuann/schema-standardization/master/schemas/",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "ui": "@nest",
            "preamble": {
                "@id": "reproterms:preamble",
                "@container": "@language"
            },
            "shuffle": {
                    "@id": "reproterms:shuffle",
                    "@type": "xsd:boolean",
                    "@nest": "ui"
            }
        },
        {
            "@base": "https://raw.githubusercontent.com/sanuann/schema-standardization/master/activities/PHQ-9/"
        }
    ],
    "@id": "phq9_schema",
    "@type": "reproschema:Activity",
    "preamble": 123,
    "ui": {
        "reproterms:inputType": "section",
        "reproterms:shuffle": False,
    }
}

doc1 = {
    # "@context": {
    #     "@version": 1.1,
    #     "pav": "http://purl.org/pav/",
    #     "xsd": "http://www.w3.org/2001/XMLSchema#",
    #     "skos": "http://www.w3.org/2004/02/skos/core#",
    #     "reproterms": "https://raw.githubusercontent.com/sanuann/schema-standardization/master/terms/",
    #     "reproschema": "https://raw.githubusercontent.com/sanuann/schema-standardization/master/schemas/",
    #     "schema": "http://schema.org/",
    #     "@language": "en",
    #     "description": {
    #         "@id": "schema:description",
    #         "@container": "@language"
    #     },
    #     "name": {
    #         "@id": "schema:name",
    #         "@container": "@language"
    #     },
    #     "value": {
    #         "@id": "schema:value",
    #         "@type": "xsd:integer"
    #     },
    #     "schema:citation": {
    #         "@container": "@language"
    #     },
    #     "version": {
    #         "@id": "schema:version",
    #         "@type": "xsd:string"
    #     },
    #     "schemaVersion": {
    #         "@id": "schema:schemaVersion",
    #         "@type": "xsd:string"
    #     },
    #     "prefLabel": {
    #         "@id": "skos:prefLabel",
    #         "@container": "@language"
    #     },
    #     "altLabel": {
    #         "@id": "skos:altLabel",
    #         "@container": "@language"
    #     },
    #     "preamble": {
    #         "@id": "reproterms:preamble",
    #         "@container": "@language"
    #     },
    #     "question": {
    #         "@id": "schema:question",
    #         "@container": "@language"
    #     },
    #     "choices": {
    #         "@id": "schema:itemListElement",
    #         "@container": "@list"
    #     },
    #     "choiceUrl": {
    #         "@id": "schema:DigitalDocument",
    #         "@type": "@id"
    #     },
    #     "requiredValue": {
    #         "@id": "reproterms:requiredValue",
    #         "@type": "schema:Boolean"
    #     },
    #     "multipleChoice": {
    #         "@id": "reproterms:multipleChoice",
    #         "@type": "schema:Boolean"
    #     },
    #     "responseOptions": {
    #         "@id": "reproterms:valueconstraints",
    #         "@type": "@vocab"
    #     },
    #     "dataType": {
    #         "@id": "schema:DataType",
    #         "@type": "@id"
    #     },
    #     "minValue": {
    #         "@id": "schema:minValue",
    #         "@type": "schema:Number"
    #     },
    #     "maxValue": {
    #         "@id": "schema:maxValue",
    #         "@type": "schema:Number"
    #     },
    #     "ui" : "@nest",
    #     "order": {
    #         "@id": "reproterms:order",
    #         "@container": "@list",
    #         "@type": "@vocab",
    #         "@nest": "ui"
    #     },
    #     "shuffle": {
    #         "@id": "reproterms:shuffle",
    #         "@type": "xsd:boolean",
    #         "@nest": "ui"
    #     },
    #     "activity_display_name": {
    #         "@id": "reproterms:activity_display_name",
    #         "@type": "schema:alternateName",
    #         "@nest": "ui"
    #     },
    #     "inputOptions": {
    #         "@id": "reproterms:inputs",
    #         "@container": "@index",
    #         "@nest": "ui"
    #     },
    #     "inputType": {
    #         "@id": "reproterms:inputType",
    #         "@type": "xsd:string",
    #         "@nest": "ui"
    #     },
    #     "readOnly": {
    #         "@id": "reproterms:readOnly",
    #         "@type": "xsd:boolean",
    #         "@nest": "ui"
    #     },
    #     "headerLevel": {
    #         "@id": "reproterms:headerLevel",
    #         "@type": "xsd:int",
    #         "@nest": "ui"
    #     },
    #     "headers": {
    #         "@id": "reproterms:tableheaders",
    #         "@container": "@list",
    #         "@nest": "ui"
    #     },
    #     "rows": {
    #         "@id": "reproterms:tablerows",
    #         "@container": "@list",
    #         "@type": "@vocab",
    #         "@nest": "ui"
    #     },
    #     "branchLogic": {
    #         "@id": "reproterms:branchLogic",
    #         "@container": "@index"
    #     },
    #     "scoringLogic": {
    #         "@id": "reproterms:scoringLogic",
    #         "@container": "@index"
    #     },
    #     "visibility": {
    #         "@id": "reproterms:visibility",
    #         "@container": "@index",
    #         "@nest": "ui"
    #     },
    #     "required": {
    #         "@id": "reproterms:required",
    #         "@container": "@index",
    #         "@nest": "ui"
    #     },
    #     "variableMap": {
    #         "@id": "reproterms:variableMap",
    #         "@container": "@list"
    #     },
    #     "variableName": "reproterms:variableName",
    #     "isAbout": {
    #         "@id": "reproterms:isAbout",
    #         "@type": "@vocab"
    #     },
    #     "allow": {
    #         "@id": "reproterms:allow",
    #         "@container": "@list",
    #         "@type": "@vocab",
    #         "@nest": "ui"
    #     },
    #     "addAllow": {
    #         "@id": "reproterms:addAllow",
    #         "@container": "@index",
    #         "@nest": "ui"
    #     },
    #     "skipped": "reproterms:refused_to_answer",
    #     "dontKnow": "reproterms:dont_know_answer",
    #     "timedOut": "reproterms:timed_out",
    #     "fullScreen": "reproterms:full_screen",
    #     "autoAdvance": "reproterms:auto_advance",
    #     "disableBack": "reproterms:disable_back",
    #     "allowExport": "reproterms:allow_export",
    #     "media": "reproterms:media",
    #     "timer": {
    #         "@id": "reproterms:timer",
    #         "@type": "@id",
    #         "@nest": "ui"
    #     },
    #     "delay": {
    #         "@id": "reproterms:delay",
    #         "@type": "@id",
    #         "@nest": "ui"
    #     },
    #     "method": "schema:httpMethod",
    #     "url": "schema:url",
    #     "payload": "reproterms:payload",
    #     "importedFrom": {
    #         "@id": "pav:importedFrom",
    #         "@type": "@id"
    #     },
    #     "importedBy": {
    #         "@id": "pav:importedBy",
    #         "@type": "@id"
    #     },
    #     "createdWith": {
    #         "@id": "pav:createdWith",
    #         "@type": "@id"
    #     },
    #     "createdBy": {
    #         "@id": "pav:createdBy",
    #         "@type": "@id"
    #     },
    #     "createdOn": {
    #         "@id": "pav:createdOn",
    #         "@type": "@id"
    #     },
    #     "previousVersion": {
    #         "@id": "pav:previousVersion",
    #         "@type": "@id"
    #     },
    #     "lastUpdateOn": {
    #         "@id": "pav:lastUpdateOn",
    #         "@type": "@id"
    #     },
    #     "derivedFrom": {
    #         "@id": "pav:derivedFrom",
    #         "@type": "@id"
    #     },
    #     "phq9": "https://raw.githubusercontent.com/sanuann/schema-standardization/master/activities/PHQ-9/items/",
    #     "phq9_1": {
    #         "@id": "phq9:phq9_1",
    #         "@type": "@id"
    #     },
    #     "phq9_2": {
    #         "@id": "phq9:phq9_2",
    #         "@type": "@id"
    #     },
    #     "phq9_3": {
    #         "@id": "phq9:phq9_3",
    #         "@type": "@id"
    #     },
    #     "phq9_4": {
    #         "@id": "phq9:phq9_4",
    #         "@type": "@id"
    #     },
    #     "phq9_5": {
    #         "@id": "phq9:phq9_5",
    #         "@type": "@id"
    #     },
    #     "phq9_6": {
    #         "@id": "phq9:phq9_6",
    #         "@type": "@id"
    #     },
    #     "phq9_7": {
    #         "@id": "phq9:phq9_7",
    #         "@type": "@id"
    #     },
    #     "phq9_8": {
    #         "@id": "phq9:phq9_8",
    #         "@type": "@id"
    #     },
    #     "phq9_9": {
    #         "@id": "phq9:phq9_9",
    #         "@type": "@id"
    #     },
    #     "phq9_10": {
    #         "@id": "phq9:phq9_10",
    #         "@type": "@id"
    #     },
    #     "phq9_total_score": {
    #         "@id": "phq9:phq9_total_score",
    #         "@type": "@id"
    #     },
    #     "phq9_category": {
    #         "@id": "phq9:phq9_category",
    #         "@type": "@id"
    #     }
    # },

    "@context": [
        "https://raw.githubusercontent.com/ReproNim/reproschema/master/contexts/generic",
        "https://raw.githubusercontent.com/ReproNim/reproschema/master/activities"
        "/PHQ-9/phq9_context",
    {
        "@base": "https://raw.githubusercontent.com/sanuann/schema-standardization/master/activities/PHQ-9/"
    }],
    "@type": "reproschema:Activity",
    "@id": "phq9_schema",
    "skos:prefLabel": "PHQ-9 Assessment",
    "skos:altLabel": "phq9_schema",
    "schema:description": 23,
    "schema:schemaVersion": "0.0.1",
    "schema:version": "0.0.1",
    "schema:citation": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1495268/",
    "preamble": "Over the last 2 weeks, how often have you been bothered by any of the following problems?",
    "scoringLogic": {
        "phq9_total_score": "phq9_1 + phq9_2 + phq9_3 + phq9_4 + phq9_5 + phq9_6 + phq9_7 + phq9_8 + phq9_9"
    },
    "variableMap": [
        {"variableName": "phq9_1", "isAbout": "phq9_1"},
        {"variableName": "phq9_2", "isAbout": "phq9_2"},
        {"variableName": "phq9_3", "isAbout": "phq9_3"},
        {"variableName": "phq9_4", "isAbout": "phq9_4"},
        {"variableName": "phq9_5", "isAbout": "phq9_5"},
        {"variableName": "phq9_6", "isAbout": "phq9_6"},
        {"variableName": "phq9_7", "isAbout": "phq9_7"},
        {"variableName": "phq9_8", "isAbout": "phq9_8"},
        {"variableName": "phq9_9", "isAbout": "phq9_9"},
        {"variableName": "phq9_10", "isAbout": "phq9_10"},
        {"variableName": "phq9_total_score", "isAbout": "phq9_total_score"}
    ],
    "ui": {
        "order": [
            "phq9_1",
            "phq9_2",
            "phq9_3",
            "phq9_4",
            "phq9_5",
            "phq9_6",
            "phq9_7",
            "phq9_8",
            "phq9_9",
            "phq9_10"
        ],
        "inputType": "section",
        "shuffle": False
    }

}
doc2 = {
    "@context": [ "https://raw.githubusercontent.com/ReproNim/reproschema/master/contexts/generic",
        "https://raw.githubusercontent.com/ReproNim/reproschema/master/activities"
        "/PHQ-9/phq9_context",
    {
        "@base": "https://raw.githubusercontent.com/sanuann/schema-standardization/master/activities/PHQ-9/"
    }],
    "@type": "reproschema:Activity",
    "@id": "phq9_schema",
    "skos:prefLabel": "PHQ-9 Assessment",
    "skos:altLabel": "phq9_schema",
    "schema:description": "PHQ-9 assessment schema",
    "schema:schemaVersion": "0.0.1",
    "schema:version": "0.0.1",
    "schema:citation": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1495268/",
    "preamble": "Over the last 2 weeks, how often have you been bothered by any of the following problems?"
}
exp = jsonld.expand(doc)
normalized = jsonld.normalize(
    exp, {'algorithm': 'URDNA2015', 'format':
        'application/n-quads'})


print(normalized)