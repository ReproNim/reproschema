# Schema Standardization

This documentation describes and explains the ReproNim schema specification.

## 0.0: Contents

- [1.0: Introduction](#10-introduction)
- [2.0: Need for Standardizing assessments](#20-need-for-standardizing-assessments)
- [3.0: Advantages of current representation](#30-advantages-of-current-representation)
- [4.0: Schema](#40-schema)
- [5.0: Contribute - how to create activity, activity-sets?](#50-how-can-i-create-a-new-activity-and-activity-set)
- [6.0: Test the schema](#60-view-schema-and-collect-data)
- [7.0: Why linked data?]()
- [8.0: How these activities are licensed?]()
- [9.0: Which tools will/are supporting this standard?]()

## 1.0: Introduction
Cognitive and clinical assessments are used throughout neuroscience, but little consistency exists in assessment data acquisition or response representation across studies. Harmonizing data after acquisition is resource intensive. Currently, the NIMH Data Archive (NDA) enforces harmonization during data submission. This approach can create a mismatch between collected and submitted data. Reverse engineering NDA data dictionaries to their original assessments using a tool like Brainverse can be tedious. To enforce consistency at the data acquisition stage, we created a standard schema and a set of reusable common assessments. The schema extends and modifies the CEDAR metadata representation. Using JSON-LD, we represent Items (elements of individual assessments) or Scores, Activities (individual assessments), and Activity sets (collections of activities performed by a participant). An implementation of the schema  can specify scoring logic, branching logic, and user interface rendering options. The schema allows internationalization (multiple languages), is implementation agnostic, and tracks variations in assessments (e.g., PHQ-9, PHQ-8). This open and accessible schema library with appropriate conversion (e.g., to RedCap) and data collection tools (e.g., [MindLogger](https://mindlogger.info/), LORIS, RedCap) enables more consistent acquisition across projects, with results being harmonized by design.

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
- [ActivitySet](https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/ActivitySet)
- [Activity](https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/Activity)
- [Item](https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/Field)

Schema overall structure:

- activity-set directory structure: name the directory in the CamelCase naming convention. It contains the following:
  - activity_set_name_schema : schema to define the activity-set
  - activity_name_context : context to define keys used specific to the activity-set schema
- activity directory structure: name the directory with name of activity in the CamelCase naming convention. It contains the following:
  - items (directory) : contains the individual items/questions in the activity schema
    - item_1
    - ...
  - activity_name_schema : schema to define the activity
  - activity_name_context : context to define keys used specific to the activity schema
  - sub-activity jsonld schemas (if any)

The generic keys are defined in the generic context file (contexts/generic)


## 5.0: How can I create a new activity and activity-set

### 5.1: Programmatic schema generation: 
- Tool to convert redcap CSVs to our schema format. But it cannot be used to convert every redcap-formatted table as some are customized redcap tables (for example the 100s that are in ABCD) but does cover most cases. A template of the CSV and how to use the tool can be found [here](https://github.com/sanuann/reproschema-builder)
- Python package to generate JSON-LDs in our schema format. [repo](https://github.com/akeshavan/mindlogger-build-applet)

### 5.2: Manual schema generation: 
Fork the project and manually create the jsonld files according to the above directory structure. this process will be tedious for large questionnaires.

- To create an activity:
  - Under the [`activities`](./activities) directory, create directory with name of activity in the CamelCase naming convention.
  - activity directory structure:
    - `items` (directory) : contains the individual items/questions in the activity schema
      - `Item_1`
      - …
    - `activityName_schema` : schema to define the activity
    - `activityName_context` : context to define keys used specific to the activity schema

  - Creating `activityName_schema` – use the keys defined in [`schemas/Activity`](./schemas/Activity). If any other keys are used, then define them in `activityName_context`

  - Description of some other keys:
    - `@context` - Array. Include the ReproNim generic context JSON-LD file along with the activity context.

      For example,
      ```json
      {
        "@context": [
          "https://raw.githubusercontent.com/ReproNim/reproschema/master/contexts/generic",
          "https://raw.githubusercontent.com/ReproNim/reproschema/master/activities/PHQ-9/phq9_context"
        ]
      }
      ```
    - `@type`=`"https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/Activity"`

  - To create `item_x` in the items folder:
    - Use keys defined in [`schemas/Field`](./schemas/Field)
    - `@type`=`"https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/Field"`
    - `responseOptions` – can be embedded or can point to a remote JSON-LD object.

- To create an activity-set:
  - Under the [`activity-sets`](./activity-sets) directory, create directory with name of activity-set in the CamelCase naming convention.
  - activity-set directory structure:
    - `activitySetName_schema` : schema to define the activity-set
    - `activitySetName_context` : context to define keys used specific to the activity-set schema

  - Creating `activitySetName_schema` – use the keys defined in [`schemas/ActivitySet`](./schemas/ActivitySet). If any other keys are used, then define them in `activitySetName_context`

  - Description of some other keys:
    - `@context` – Array. Include the ReproNim generic context JSON-LD file along with the activity-set context.

      For example,
      ```json
      {
        "@context": [
          "https://raw.githubusercontent.com/ReproNim/reproschema/master/contexts/generic",
          "https://raw.githubusercontent.com/sanuann/reproschema/master/activity-sets/example/nda-phq_context"
        ]
      }
      ```
    - `@type`=`"https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/ActivitySet"`

## 6.0: View schema and collect data

`http://schema.repronimg.org/ui/#/?url=path_to_activity_set_schema`

## 7.0: Why linked data?

## 8.0: How these activities are licensed?

## 9.0: Which tools will/are supporting this standard?
