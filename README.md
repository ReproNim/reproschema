# Schema Standardization

This documentation describes and explains the ReproNim schema specification.

## 0.0: Contents

- [1.0: Introduction](#10-introduction)
- [2.0: Need for Standardizing assessments](#20-need-for-standardizing-assessments)
- [3.0: Advantages of current representation](#30-advantages-of-current-representation)
- [4.0: Schema](#40-schema)
- [5.0: Contribute - how to create activity, activity-sets?](#50-how-can-i-create-a-new-activity-and-activity-set)
- [6.0: Why linked data?]()
- [7.0: How these activities are licensed?]()
- [8.0: Which tools will/are supporting this standard?]()

## 1.0: Introduction
Creating NIMH Data Archive (NDA) forms using Brainverse turned out to be immensely time consuming for the average user, as a lot of details for data collection were missing in the current NDA schemas, which are primarily intended for data ingestion. We have been working with our collaborators, the Adolescent Brain Cognitive Development Study (ABCD) Study, the Canadian Open Neuroscience Platform (CONP) and the [MindLogger](https://mindlogger.org) team, to create a set of reusable schemas for common assessments across projects. We are building the assessment standard by extending and modifying the Center for Expanded Data Annotation and Retrieval (CEDAR) metadata representation. CEDAR uses JSON-LD to represent their templates, which we are continuing to use. For instruments and assessments, we are adding the ability to specify scoring logic and branching logic, but also clarifying how graph nodes are linked across JSON-LD documents. This will be one of the richest repositories of form-based assessment information publicly available.

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
- Developed cleaner JSON-LD representation to represent:
  - __Activity Sets__: Collections of activities performed by a participant
  - __Activity__: Individual assessments
  - __Items__: Elements of individual assessments

## 3.0: Advantages of current representation
- Rich contexts with JSON-LD
  - Redcap uses CSVs to represent forms
- Single source of curated assessments from [ReproNim](https://github.com/ReproNim)
- Each Item, Activity, and Activity Set provide unique and persistent identifiers
- Variations can be tracked (e.g., PHQ-9, PHQ-8)
- Allows, supports, and tracks internationalization (ABCD requires Spanish and English forms)
- Implementation agnostic – schema can be used by several software
- Still a linked data graph and can be validated using [SHACL](https://www.w3.org/TR/shacl/)

## 4.0: Schema
We have defined 3 different types of schema –
- [ActivitySet](https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/ActivitySet.jsonld)
- [Activity](https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Activity.jsonld)
- [Item](https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Field.jsonld)

## 5.0: How can I create a new activity and activity-set
- Fork the project
- To create an activity:
  - Under the [`activities`](./activities) directory, create directory with name of activity in the CamelCase naming convention.
  - activity directory structure:
    - `items` (directory) : contains the individual items/questions in the activity schema
      - `Item_1.jsonld`
      - …
    - `activityName_schema.jsonld` : schema to define the activity
    - `activityName_context.jsonld` : context to define keys used specific to the activity schema

  - Creating `activityName_schema.jsonld` – use the keys defined in [`schema/Activity.jsonld`](./schema/Activity.json). If any other keys are used, then define them in `activityName_context.jsonld`

  - Description of some other keys:
    - `@context` - Array. Include the ReproNim generic context JSON-LD file along with the activity context.

      For example,
      ```json
      {
        "@context": [
          "https://raw.githubusercontent.com/ReproNim/schema-standardization/master/contexts/generic.jsonld",
          "https://raw.githubusercontent.com/ReproNim/schema-standardization/master/activities/PHQ-9/phq9_context.jsonld"
        ]
      }
      ```
    - `@type`=`"https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Activity.jsonld"`

  - To create `item_x.jsonld` in the items folder:
    - Use keys defined in [`schema/Field.jsonld`](./schema/Field.jsonld)
    - `@type`=`"https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Field.jsonld"`
    - `responseOptions` – can be embedded or can point to a remote JSON-LD object.

- To create an activity-set:
  - Under the [`activity-sets`](./activity-sets) directory, create directory with name of activity-set in the CamelCase naming convention.
  - activity-set directory structure:
    - `activitySetName_schema.jsonld` : schema to define the activity-set
    - `activitySetName_context.jsonld` : context to define keys used specific to the activity-set schema

  - Creating `activitySetName_schema.jsonld` – use the keys defined in [`schema/ActivitySet.jsonld`](./schema/ActivitySet.jsonld). If any other keys are used, then define them in `activitySetName_context.jsonld`

  - Description of some other keys:
    - `@context` – Array. Include the ReproNim generic context JSON-LD file along with the activity-set context.

      For example,
      ```json
      {
        "@context": [
          "https://raw.githubusercontent.com/ReproNim/schema-standardization/master/contexts/generic.jsonld",
          "https://raw.githubusercontent.com/sanuann/schema-standardization/master/activity-sets/example/nda-phq_context.jsonld"
        ]
      }
      ```
    - `@type`=`"https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/ActivitySet.jsonld"`

## 6.0: Why linked data?

## 7.0: How these activities are licensed?

## 8.0: Which tools will/are supporting this standard?
