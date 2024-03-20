# Adopting Assessments from the reproschema-library

This part focuses on how to select and integrate assessments from the reproschema-library into your research protocol, an essential step in crafting a comprehensive study. The chosen assessments are to be placed in the `activities` folder within your repository. This folder serves as the central hub for various assessments or activities that collectively form your research protocol.

Each activity or assessment within this `activities` folder is typically structured around a file named with a suffix `_schema`. This file defines the overall framework of the assessment. Accompanying this, if an assessment comprises specific questions, these are organized in a subfolder titled `items` within the respective activity's directory. It's important to note that if an assessment is directly taken from the ReproSchema-library without any customization, the creation of an `items` subfolder is not necessary, as the itemized questions are predefined in the library.

To illustrate this process, we will use two specific types of assessments from [reproschema-library](https://github.com/ReproNim/reproschema-library): `demographics` and `psychological questions`. The latter represents a composite assessment created from multiple pre-existing assessments within the library. This example demonstrates how to combine different elements from the library to construct a bespoke assessment tailored to the unique demands of your research protocol.

## Step 1: Understand the structure of a *_schema file through this [exemplar file](https://github.com/ReproNim/reproschema-protocol-cookiecutter/blob/main/%7B%7Bcookiecutter.protocol_name%7D%7D/activities/Activity1/activity1_schema)

1. **Context (@context)**: This field provides references to the context definitions. In this schema, it links to the generic context of ReproSchema and the specific context for the items in the repository, defined by the URL with the "rl" key. This context helps to interpret the terms used within the schema.
2. **Type (@type)**: Defined as "reproschema:Activity," this indicates the nature of the document, specifying that it is an activity within the ReproSchema framework.
3. **Identifier (@id)**: The unique identifier for this specific schema is "activity1_schema." This ID uniquely distinguishes this activity from others in the repository.
4. **PrefLabel**: This is the human-readable name of the activity, here given as "Screening." It serves as a clear and concise title for the activity.
5. **Description**: Provides a brief overview of the activity, in this case, "example of an activity."
6. **SchemaVersion and Version**: These fields indicate the versions of the ReproSchema being used ("1.0.0-rc2" means “1.0.0 Release Candidate 2”) and the version of this particular activity schema ("0.0.1"), respectively.
7. **UI Configuration**: This section specifies how the activity will be presented to users. It includes:
    - **addProperties**: Lists the variables and corresponding items collected in the activity. For example, the variable `document_upload_item` is about the item `items/document_upload_item` and is always visible (`isVis: true`). It allows for the item to be skipped (`reproschema:Skipped`).
    - **order**: Dictates the sequence in which items will appear in the UI. Here, it specifies that "items/document_upload_item" will be the first (and only) item.
    - **shuffle**: Indicates whether the order of items should be randomized. In this example, it is set to `false`, meaning the order is fixed.
    - **allow**: Defines additional UI functionalities. Here, it includes `reproschema:AutoAdvance` for automatic progression and `reproschema:AllowExport` to enable data export.

## Step 2: Customizing the schema file for demographics using existing assessments from reproschema-library

This step involves precise modifications, particularly in the `@context` and `addProperties` sections, to ensure the schema accurately reflects the demographic data you aim to collect.

1. **Adjusting the `@context` for Demographics**:

    In addition to the standard ReproSchema context, we've added a specific link in the "@context" section for demographics:

    ```
    "demo": "https://raw.githubusercontent.com/ReproNim/reproschema-library/[commitID]/demographics_and_background_information_v1/items/"
    ```

    Labeling this link as "demo" directs the schema to the location in the ReproSchema-library where items for demographics and background information are defined. We use the link with a specific commit ID to ensure the consistency of the assessment version. This contextual link allows the schema to access the detailed structures and definitions needed for each demographic item.

2. **Customizing "addProperties" for Demographic Variables**:

    In the "addProperties" section, we define each variable that corresponds to a demographic question. For example:

    ```
    {
    "variableName": "year_of_birth",
    "isAbout": "demo:year_of_birth"
    }
    ```

    The `"variableName": "year_of_birth"` is where you specify the variable as the participant's year of birth.
    The `"isAbout": "demo:year_of_birth"` part establishes a link to the detailed structure of this item in the ReproSchema-library. The "demo:" prefix references the additional context you've added, guiding the schema to the correct location for the structure and details of the "year_of_birth" item.

    See the outcome file [here](https://github.com/ReproNim/reproschema-demo-protocol/blob/main/activities/1_demographics/demographics_schema)

## Step 3: Integrating multiple assessments

Different from `demograpgics`, `psychological_questionnaire_schema` combines assessments, such as [PHQ-9](https://github.com/ReproNim/reproschema-library/tree/master/activities/PHQ-9), [GAD7](https://github.com/ReproNim/reproschema-library/tree/master/activities/GAD7), [PC-PTSD-5](https://github.com/ReproNim/reproschema-library/tree/master/activities/PC-PTSD-5), and [demographics](https://github.com/ReproNim/reproschema-library/tree/master/activities/demographics_and_background_information_v1/items) from [reproschema-library](https://github.com/ReproNim/reproschema-library).

1. **Contextual setup (@context)**:

    The @context section is expanded to include not only the generic ReproSchema context but also specific links to the ReproSchema-library. This enables the schema to access a broader range of predefined items and assessments. For the psychological questionnaire, two context links are established:

    ```
    "@context": [
    "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc4/contexts/generic",
            {
                "activities": "https://raw.githubusercontent.com/ReproNim/reproschema-library/[commitID]/activities/",
                "demo": "https://raw.githubusercontent.com/ReproNim/reproschema-library/[commitID]/activities/demographics_and_background_information_v1/items/"
            }
        ]
    ```

    A link to the activities in the reproschema-library (`activities`: ) and a link for demographics items (`demo`: ), both are commit-specific. This indicates that we will combine different assessments from those two parts.

2. **Defining the activity (@type, @id, prefLabel, etc.)**:

    The standard fields like @type, @id, prefLabel, description, preamble, schemaVersion, and version define the nature and purpose of the psychological questionnaire.

3. **UI configuration and integration of multiple assessments (ui)**:

    ```
    "ui": {
        "addProperties": [
            {
                "variableName": "phq-9",
                "isAbout": "activities:PHQ-9/PHQ9_schema"
            },
            {
                "variableName": "gad-7",
                "isAbout": "activities:GAD7/GAD7_schema"
            },
            {
                "variableName": "pc-ptsd-5",
                "isAbout": "activities:PC-PTSD-5/PC-PTSD-5_schema"
            },
            {
                "variableName": "clinical_history_psychiatry",
                "isAbout": "demo:clinical_history_psychiatry"
            },
            {
                "variableName": "clinical_history_psychiatry_other",
                "isAbout": "demo:clinical_history_psychiatry_other"
            },
            {
                "variableName": "clinical_history_psychiatry_current",
                "isAbout": "demo:clinical_history_psychiatry_current"
            },
            {
                "variableName": "clinical_history_psychiatry_current_only_some",
                "isAbout": "demo:clinical_history_psychiatry_current_only_some"
            },
            {
                "variableName": "clinical_history_psychiatry_current_only_some_other",
                "isAbout": "demo:clinical_history_psychiatry_current_only_some_other"
            }
            ],
        "order": [
            "activities:PHQ-9/PHQ9_schema",
            "activities:GAD7/GAD7_schema",
            "activities:PC-PTSD-5/PC-PTSD-5_schema",
            "demo:clinical_history_psychiatry",
            "demo:clinical_history_psychiatry_other",
            "demo:clinical_history_psychiatry_current",
            "demo:clinical_history_psychiatry_current_only_some",
            "demo:clinical_history_psychiatry_current_only_some_other"
            ],
        "shuffle": false,
        "allow": [
            "reproschema:AutoAdvance",
            "reproschema:AllowExport"
            ]
    }
    ```

    In the addProperties section, we define each variable that corresponds to a specific assessment. For instance:
    - `"variableName": "phq-9"` is linked to `"isAbout": "activities:PHQ-9/PHQ9_schema"`. This implies that the PHQ-9 schema (an assessment for depressive symptoms) from the reproschema-library is used in the current psychological questionnaire schema.
    - Similarly, other assessments like `GAD-7` and `PC-PTSD-5` are included using their respective variable names and links to their schemas in the activities context.
    - Additional variables related to clinical history in psychiatry are linked using the demo context, pointing to specific items within the demographics and background information section of the reproschema-library.

        ```
        {
            "variableName": "clinical_history_psychiatry",
            "isAbout": "demo:clinical_history_psychiatry"
        }
        ```

    - The `order` array specifies the sequence in which these assessments will appear in the questionnaire, ensuring a logical flow for participants.
    - The `shuffle` setting is `false`, maintaining the defined order, and allow includes functionalities like auto-advance between assessments and data export.

See the outcome [here](https://github.com/ReproNim/reproschema-demo-protocol/blob/main/activities/2_psychological/psychological_questionnaire_schema)
