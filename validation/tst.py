from pyshacl import validate


shapes_file = '''
@prefix dash: <http://datashapes.org/dash#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <http://schema.org/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix dash: <http://datashapes.org/dash#> .
@prefix reproterms: <https://raw.githubusercontent.com/ReproNim/reproschema/master/terms/> .
@prefix reproschema: <https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .


reproschema:ActivityShape
    a sh:NodeShape ;
    sh:closed true ;
    sh:ignoredProperties ( rdf:type ) ;
    sh:targetClass reproschema:Activity ;
    sh:property [
        sh:path schema:description;
        sh:datatype rdf:langString ;
    ] ;
    sh:property [
        sh:path schema:schemaVersion;
        sh:datatype rdf:langString ;
    ] ;
    sh:property [
        sh:path schema:version ;
        sh:datatype rdf:langString ;
    ] ;
    sh:property [
        sh:path schema:citation ;
        sh:datatype rdf:langString ;
    ] ;
    sh:property [
        sh:path skos:prefLabel ;
        sh:datatype rdf:langString ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path reproterms:preamble;
        sh:datatype rdf:langString ;
    ] ;
    sh:property [
        sh:path reproterms:scoringLogic ;
        sh:node reproterms:ScoringShape ;
    ] ;
    sh:property [
        sh:path reproterms:order ;
        sh:node dash:ListShape ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:property [
            sh:path ( [ sh:zeroOrMorePath rdf:rest ] rdf:first ) ;
            sh:nodeKind sh:IRI ;
            sh:minCount 1 ;
        ]
    ] ;
    sh:property [
        sh:path reproterms:addProperties ;
        sh:node reproterms:AddPropertiesShape ;
    ] ;
    sh:property [
        sh:path reproterms:inputType ;
        sh:datatype xsd:string ;
    ] ;
    sh:property [
        sh:path reproterms:shuffle ;
        sh:datatype schema:Boolean ;
    ] ;
    sh:property [
        sh:path reproterms:allow ;
        sh:node dash:ListShape ;
        sh:maxCount 1 ;
        sh:property [
            sh:path ( [ sh:zeroOrMorePath rdf:rest ] rdf:first ) ;
            sh:nodeKind sh:IRI ;
            sh:minCount 1 ;
        ]
    ] .

reproterms:AddPropertiesShape
    a sh:NodeShape ;
    sh:closed true ;
    sh:ignoredProperties ( rdf:type ) ;
    sh:property [
        sh:path reproterms:variableName ;
        sh:datatype rdf:langString ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path reproterms:isAbout ;
        sh:nodeKind sh:IRI ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path reproterms:isVis ;
        sh:or ( [ sh:datatype rdf:langString ] [ sh:datatype xsd:boolean ] [
        sh:node reproterms:IsVisShape ]) ;
    ] ;
    sh:property [
        sh:path skos:prefLabel ;
        sh:datatype rdf:langString ;
    ] .

reproterms:ScoringShape
    a sh:NodeShape ;
    sh:closed true ;
    sh:property [
        sh:path reproterms:variableName ;
        sh:datatype rdf:langString ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;
    sh:property [
        sh:path reproterms:jsExpression ;
        sh:datatype rdf:langString ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] .

reproterms:IsVisShape
    a sh:NodeShape ;
    sh:closed true ;
    sh:ignoredProperties ( rdf:type ) ;
    sh:property [
        sh:path schema:method ;
        sh:datatype rdf:langString ;
    ] ;
    sh:property [
        sh:path schema:url ;
        sh:datatype rdf:langString ;
    ] ;
    sh:property [
        sh:path reproterms:payload ;
        sh:datatype rdf:langString ;
    ] .
'''
shapes_file_format = 'turtle'

data_file = '''
{
    "@context": [ "https://raw.githubusercontent.com/ReproNim/reproschema/master/contexts/generic",
        "https://raw.githubusercontent.com/ReproNim/reproschema/master/activities/PHQ-9/PHQ9_context",

        {
            "@base": "https://raw.githubusercontent.com/ReproNim/reproschema/master/activities/PHQ-9/"
        }
    ],
    "@type": "reproschema:Activity",
    "@id": "PHQ9_schema",
    "skos:prefLabel": "PHQ-9 Assessment",
    "schema:description": "PHQ-9 assessment schema",
    "schema:schemaVersion": "0.0.1",
    "schema:version": "0.0.1",
    "schema:citation": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1495268/",
    "preamble": {
        "en": "Over the last 2 weeks, how often have you been bothered by any of the following problems?",
        "es": "Durante las últimas 2 semanas, ¿con qué frecuencia le han molestado los siguintes problemas?"

    },
    "scoringLogic": [
        {"variableName": "phq9_total_score", "jsExpression": "phq9_1 + phq9_2 + phq9_3 + phq9_4 + phq9_5 + phq9_6 + phq9_7 + phq9_8 + phq9_9"}
    ],
    "ui": {
        "addProperties": [
			{"isAbout": "phq9_1",
			"variableName": "phq9_1",
			"isVis": true
			},
			{"isAbout": "phq9_2",
			"variableName": "phq9_2",
			"isVis": true
			},
			{"isAbout": "phq9_3",
			"variableName": "phq9_3",
			"isVis": true
			},
			{"isAbout": "phq9_4",
			"variableName": "phq9_4",
			"isVis": true
			},
			{"isAbout": "phq9_5",
			"variableName": "phq9_5",
			"isVis": true
			},
			{"isAbout": "phq9_6",
			"variableName": "phq9_6",
			"isVis": true
			},
			{"isAbout": "phq9_7",
			"variableName": "phq9_7",
			"isVis": true
			},
			{"isAbout": "phq9_8",
			"variableName": "phq9_8",
			"isVis": true
			},
			{"isAbout": "phq9_9",
			"variableName": "phq9_9",
			"isVis": true
			},
			{"isAbout": "phq9_10",
			"variableName": "phq9_10",
			"isVis": "phq9_1 > 0 ||  phq9_2 > 0 || phq9_3 > 0 || phq9_4 > 0 || phq9_5 > 0 || phq9_6 > 0 || phq9_7 > 0 || phq9_8 > 0 || phq9_9 > 0"
			},
			{"isAbout": "phq9_total_score",
			"variableName": "phq9_total_score",
			"isVis": false
			}
		],
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
        "shuffle": false
    }
}
'''
data_file_format = 'json-ld'

conforms, v_graph, v_text = validate(data_file, shacl_graph=shapes_file,
                                     data_graph_format=data_file_format,
                                     shacl_graph_format=shapes_file_format,
                                     inference='rdfs', debug=True,
                                     serialize_report_graph=True)
# print(conforms)
# print(v_graph)
print(v_text)