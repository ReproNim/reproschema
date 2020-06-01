shapes_file = '''
@prefix dash: <http://datashapes.org/dash#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <http://schema.org/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix dash: <http://datashapes.org/dash#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix reproterms: <https://raw.githubusercontent.com/ReproNim/reproschema/master/terms/> .
@prefix reproschema: <https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/> .
reproschema:FieldShape
    a sh:NodeShape ;
    sh:closed true ;
    sh:ignoredProperties ( rdf:type ) ;
    sh:targetClass reproschema:Field ;
    sh:property [
        sh:path skos:prefLabel;
        sh:datatype rdf:langString ;
        
    ] ;
    sh:property [
        sh:path schema:description ;
        sh:datatype rdf:langString ;
        sh:maxCount 1 ;
    ] ;
    sh:property [
        sh:path schema:schemaVersion ;
        sh:datatype rdf:langString ;
        sh:maxCount 1 ;
    ] ;
    sh:property [
        sh:path schema:version ;
        sh:datatype rdf:langString ;
        sh:maxCount 1 ;
    ] ;
    sh:property [
        sh:path schema:question ;
        sh:datatype rdf:langString ;
    ] ;
    sh:property [
        sh:path reproterms:preamble;
        sh:datatype rdf:langString ;
        sh:maxCount 1 ;
    ] ;
    sh:property [
        sh:path reproterms:inputType ;
        sh:datatype xsd:string ;
        sh:maxCount 1 ;
    ] ;
   sh:property [
        sh:path reproterms:responseOptions ;
        sh:node reproterms:ResponseOptionsShape ;
   ] .

reproterms:ResponseOptionsShape
    a sh:NodeShape ;
    sh:closed true ;
    sh:ignoredProperties ( rdf:type ) ;
    sh:property [
        sh:path reproterms:multipleChoice ;
        sh:datatype schema:Boolean ;
    ] ;
    sh:property [
        sh:path reproterms:requiredValue ;
        sh:datatype schema:Boolean ;
    ] ;
    sh:property [
        sh:path schema:minValue ;
        sh:datatype schema:Number ;
    ] ;
    sh:property [
        sh:path schema:maxValue ;
        sh:datatype xsd:integer ;
    ] ;
    sh:property [
        sh:path reproterms:valueType ;
        sh:datatype xsd:integer ;
    ] ;
    sh:property [
        sh:path schema:itemListElement ;
        sh:node schema:ChoicesShape ;
    ] .

schema:ChoicesShape
    a sh:NodeShape ;
    sh:closed true ;
    sh:ignoredProperties ( rdf:type ) ;
    sh:property [
        sh:path schema:name ;
        sh:datatype rdf:langString ;
    ] ;
    sh:property [
        sh:path schema:value ;
        sh:datatype xsd:integer ;
    ] ;
    sh:property [
        sh:path schema:image ;
        sh:datatype xsd:string ;
    ] ;
    sh:property [
        sh:path reproterms:dontKnow ;
        sh:nodeKind sh:IRI ;
    ] ;
    sh:property [
        sh:path reproterms:skipped ;
        sh:nodeKind sh:IRI ;
    ] .
'''
data_file = '''
{
    "@context": [ "https://raw.githubusercontent.com/ReproNim/reproschema/master/contexts/generic"
     ],
    "@type": "reproschema:Field",
    "@id": "phq9_8",
    "prefLabel": "PHQ9-8",
    "schema:description": "schema for Q8 of the PHQ-9 Assessment",
    "schema:schemaVersion": "0.0.1",
    "schema:version": "0.0.1",
    "question": {
        "en": "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual?",
        "es": "¿Se ha movido o hablado tan lento que otras personas podrían haberlo notado? o lo contrario – muy inquieto(a) o agitado(a) que ha estado moviéndose mucho más de lo normal?"
    },
    "ui": {
        "inputType": "radio"
    },
    "responseOptions": "https://raw.githubusercontent.com/ReproNim/reproschema/master/activities/PHQ-9/valueConstraints"
}
'''
import pyld
import json, os
from pyshacl import validate
shapes_file_format = 'turtle'

data = json.loads(data_file)
normalized = pyld.jsonld.normalize(
    data, {'algorithm': 'URDNA2015',
           'base': 'https://raw.githubusercontent.com/ReproNim/reproschema/master/activities/PHQ-9/items/',
           'format': 'application/n-quads'})
# print(136, normalized)
conforms, v_graph, v_text = validate(normalized, shacl_graph=shapes_file,
                                     data_graph_format='nquads',
                                     shacl_graph_format=shapes_file_format,
                                     inference='rdfs', debug=True,
                                     serialize_report_graph=True)

print(conforms)
# print(str(v_graph))


# for root, dirs, files in os.walk('./activities/PHQ-9/items'):
#     for name in files:
#         file_path = os.path.join(root, name)
#         if not os.path.splitext(file_path)[1]:  # files without extension
#             # print('\n', 192, name)
#             with open(file_path) as fp:
#                 data = json.load(fp)
#                 normalized = pyld.jsonld.normalize(
#                     data, {'algorithm': 'URDNA2015',
#                            'base': 'https://raw.githubusercontent.com/ReproNim/reproschema/master/activities/PHQ-9/items/',
#                            'format': 'application/n-quads'})
#                 # print(normalized)
#                 conforms, v_graph, v_text = validate(normalized, shacl_graph=shapes_file,
#                                                      data_graph_format='nquads',
#                                                      shacl_graph_format=shapes_file_format,
#                                                      inference='rdfs', debug=True,
#                                                      serialize_report_graph=True)
#                 print('------', name, conforms)
#                 # print(str(v_graph))
#
#             fp.close()
