![Python package](https://github.com/ReproNim/reproschema/workflows/Python%20package/badge.svg)

# Schema Standardization

This documentation describes and explains the ReproNim schema specification.

## 0.0: Contents

- [1.0: Introduction](#10-introduction)
- [2.0: Need for Standardizing assessments](#20-need-for-standardizing-assessments)
- [3.0: Advantages of current representation](#30-advantages-of-current-representation)
- [4.0: Schema](#40-schema)
- [5.0: Contribute - how to create activity, protocol?](#50-how-can-i-create-a-new-activity-and-protocol)
- [6.0: Test schema and collect data](#60-view-schema-and-collect-data)
- [7.0: Why linked data?]()
- [8.0: How these activities are licensed?]()
- [9.0: Which tools will/are supporting this standard?]()

## 1.0: Introduction
Cognitive and clinical assessments are used throughout neuroscience, but little consistency exists in assessment data acquisition or response representation across studies. Harmonizing data after acquisition is resource intensive. Currently, the NIMH Data Archive (NDA) enforces harmonization during data submission. This approach can create a mismatch between collected and submitted data. Reverse engineering NDA data dictionaries to their original assessments using a tool like Brainverse can be tedious. To enforce consistency at the data acquisition stage, we created a standard schema and a set of reusable common assessments. The schema extends and modifies the CEDAR metadata representation. Using JSON-LD, we represent Items (elements of individual assessments) or Scores, Activities (individual assessments), and Protocols (collections of activities performed by a participant). An implementation of the schema  can specify scoring logic, branching logic, and user interface rendering options. The schema allows internationalization (multiple languages), is implementation agnostic, and tracks variations in assessments (e.g., PHQ-9, PHQ-8). This open and accessible schema library with appropriate conversion (e.g., to RedCap) and data collection tools (e.g., [MindLogger](https://mindlogger.org/), LORIS, RedCap) enables more consistent acquisition across projects, with results being harmonized by design.

## 2.0: Need for Standardizing assessments
- Cognitive and Clinical assessments are used throughout neuroimaging to perform deep phenotyping
- Despite many efforts (Cog Atlas, Cognitive Paradigm Ontology, OOve) no consistency in data representation across projects
- Each project uses own schema, format, data collection tool (paper, form)
- Need for harmonization across projects
  - NIMH Data Archive enforces harmonization during submission
    - Significant effort
    - Creates mismatch between experiment and stored data
  - Harmonize large projects
    - ABCD
    - CONP
- Collaborations: ABCD, Healthy Brain Network, LORIS/CONP
- We used CEDAR templates as a starting point

## 3.0: Advantages of current representation
- Rich contexts with JSON-LD
  - Redcap uses CSVs to represent forms
- Single source of curated assessments from [ReproNim](https://github.com/ReproNim)
- Each Item, Activity, and Protocol provide unique and persistent identifiers
- Variations can be tracked (e.g., PHQ-9, PHQ-8)
- Allows, supports, and tracks internationalization (ABCD requires Spanish and English forms)
- Implementation agnostic – schema can be used by several software
- Still a linked data graph and can be validated using [SHACL](https://www.w3.org/TR/shacl/)

## 4.0: Schema
We have developed cleaner JSON-LD representation to represent:
  - __Protocols__: Collections of activities performed by a participant
  - __Activity__: Individual assessments
  - __Field__: Elements of individual assessments

Properties of each of the above schema are described below:
- [Properties of a Protocol](docs/pages/protocol_props.md)
- [Properties of an Activity](docs/pages/activity_props.md)
- [Properties of Field](docs/pages/field_props.md)

## 5.0: How can I create a new activity and protocol

### 5.1: Programmatic schema generation: 
- Tool to convert redcap CSVs to our schema format. But it cannot be used to convert every redcap-formatted table as some are customized redcap tables (for example the 100s that are in ABCD) but does cover most cases. A template of the CSV and how to use the tool can be found [here](https://github.com/sanuann/reproschema-builder)
- Python package to generate JSON-LDs in our schema format. [repo](https://github.com/akeshavan/mindlogger-build-applet)

### 5.2: Manual schema generation: 
Fork the project and manually create the jsonld files according to the above directory structure. (This process will be tedious for large
 questionnaires).

- To create an activity:
  - Under the [`activities`](./activities) directory, create directory with name of activity in the CamelCase naming convention.
  - activity directory structure:
    - `/items` (directory) : contains the `jsonld` files for individual items of the activity schema
      - `item_1`
      - …
    - `activityName_schema` : schema to define the activity
    - `activityName_context` : context to define keys used specific to the activity schema

  - Creating `activityName_schema` – use the keys defined in [`schemas/Activity`](./schemas/Activity). If any other keys are used, then define them in `activityName_context`
  
  For example,
  ```
    {
    "@context": [ "https://raw.githubusercontent.com/ReproNim/reproschema/master/contexts/generic",
        "https://raw.githubusercontent.com/ReproNim/reproschema/master/activities/Wellbeing/Wellbeing_context"
    ],
    "@type": "reproschema:Activity",
    "@id": "Wellbeing_schema",
    "skos:prefLabel": "Wellbeing",
    "schema:description": " Wellbeing Voice tasks",
    "schema:schemaVersion": "0.0.1",
    "schema:version": "0.0.1",
    "preamble": {
        "en": "For each task, you should hit the record button before speaking and then stop once you are done speaking. You may hit play to hear what was recorded.",
        "es": "Para cada pregunta, debería hacer click sobre el botón antes de hablar y luego hacerlo de nuevo para parar de grabar. Luego puede tocar play para escuchar su respuesta."
    },
    "ui": {
        "addProperties": [
            {"isAbout": "share_data",
            "variableName": "share_data",
            "prefLabel": {"en": "Share Data"},
            "isVis": true,
            "allow": ["skipped", "dontknow"],
            ...
            },
            {"isAbout": "email",
            "variableName": "email",
            "isVis": "share_data === 1"
            },
            {"isAbout": "multipart_audio_check",
            "variableName": "multipart_audio_check",
            "isVis": true
            },
            {"isAbout": "free_speech_general_mood",
            "variableName": "share_data",
            "isVis": true
            },
            {"isAbout": "say_ah",
            "variableName": "say_ah",
            "isVis": true
            }
        ],
        "order": [
            "multipart_audio_check",
            "share_data",
            "email",
            "free_speech_general_mood",
            "say_ah"
        ],
        "shuffle": false
    }
  }
  ```
  
  - Mandatory keys:
    - `@context` - [Array] Include the ReproNim generic context JSON-LD file along with the activity context.
    - `@type`- describes type of the schema.
    - `@id` - unique id for the schema. should be same as the filename.
    - `skos:prefLabel` - display name for the schema
    - `ui.addProperties` - defines the various properties of each item.
    - `variablename` - variable name used in `ui.order` for the items
    - `isAbout` - file name of the corresponding variable name
    - `ui.order` - [Array] defines the order in which the items appear in the activity

  - To create `item_x` in the items folder:
    - Use keys defined in [`schemas/Field`](./schemas/Field)
    - `@type`=`"https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/Field"`
    - `responseOptions` – can be embedded or can point to a remote JSON-LD object.

- To create a protocol:
  - Under the [`protocols`](./protocols) directory, create directory with name of protocol in the CamelCase naming convention.
  - protocol directory structure:
    - `protocolName_schema` : schema to define the protocol
    - `protocolName_context` : context to define keys used specific to the protocol schema

  - Creating `protocolName_schema` – use the keys defined in [`schemas/Protocol`](./schemas/Protocol). If any other keys are used, then define them in `protocolName_context`

  - Description of some other keys:
    - `@context` – Array. Include the ReproNim generic context JSON-LD file along with the protocol context.

      For example,
      ```json
      {
        "@context": [
          "https://raw.githubusercontent.com/ReproNim/reproschema/master/contexts/generic",
          "https://raw.githubusercontent.com/ReproNim/reproschema/master/protocols/example/nda-phq_context"
        ]
      }
      ```
    - `@type`=`"https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/Protocol"`

## 6.0: Test schema and collect data

First, make sure your syntax is in correct jsonld format. Test all files with ```@content``` from command line:
```
npm install -g jsonlint
grep -r --exclude-dir=node_modules --exclude-dir=ui --exclude-dir=.github "@context" . | cut -d: -f1 | xargs -I fname jsonlint -q fname
```

Or test individual files here: ```https://jsonlint.com/```

Then you can view your schema here:

`http://schema.repronim.org/ui/#/?url=path_to_protocol_schema`

For example: 

`
https://schema.repronim.org/ui/#/?url=https://raw.githubusercontent.com/sensein/covid19/master/protocol/Covid19_schema
`



## 7.0: Why linked data?

## 8.0: How these activities are licensed?

## 9.0: Which tools will/are supporting this standard?
