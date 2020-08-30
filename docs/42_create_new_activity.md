# Create a new activity

Now you would like to add a small questionnaire to estimate the handedness of each participant. We can use the Edinburgh handedness inventory for this. 

This tool is not part of the set of questionnaires included in the repronim library so we are going to have to create it ourselves.

There are 2 version for this questionnaire a long and a short version.

- Oldfield, R.C. (1971). The assessment and analysis of handedness: The Edinburgh inventory. Neuropsychologia, 9, 97-113. DOI: https://doi.org/10.1016/0028-3932(71)90067-4
- Veale, J.F. (2014). Edinburgh Handedness Inventory - Short Form: A revised version based on confirmatory factor analysis. Laterality, 19, 164-177. DOI: https://doi.org/10.1080/1357650X.2013.783045

The participant is given one question and a set of activities:

```
Please indicate your preferences in the use of hands in the following activities or objects:

1) Writing (*)
2) Drawing
3) Throwing (*)
4) Using Scissors
5) Using a Toothbrush (*)
6) Using a Knife (without a fork)
7) Using a Spoon (*)
8) Using a broom (upper hand)
9) Striking a Match (holds the match)
10) Opening a Box (holding the lid)

i) Which foot do you prefer to kick with ?
ii) Which eye do you use when using only one?
```

The asterisks denote the subset of items that belong to the short form of the questionnaire.

The scoring for each item follows the following scheme: 

- Always right = 100
- Usually right = 50
- Both equally = 0
- Usually left = -50
- Always left = -100

The Laterality Quotient is given by the mean score over items. And the final classification according to the Laterality Quotient score goes as follow:

- Left handers: -100 to -61
- Mixed handers: -60 to 60
- Right handers: 61 to 100

<!-- ---

Note that there is also a longer with extra items that are not on the standard inventory.

- Holding a Computer Mouse
- Using a Key to Unlock a Door
- Holding a Hammer
- Holding a Brush or Comb
- Holding a Cup while Drinking

Source: http://www.brainmapping.org/shared/Edinburgh.php -->

## Preparing the JSON for the activity

Now let's create the `activities` folder, an activity file for the new assessment tool we want to create. For this tutorial we will be using the short form of the Edinburgh handedness inventory.

```bash
# Type this in a terminal window
mkdir activities
touch activities/EHI/edinburgh_handedness_inventory_short.jsonld
```

Now let's start by adding the following content in the activity file we have just created.

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    "@type": "reproschema:Activity",
    "@id": "edinburgh_handedness_inventory_short.jsonld",
    "prefLabel": "Edinburgh handedness inventory - short form",
    "description": "Short version of the Edinburgh handedness inventory",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1",
}
```

The content is for now very similar to the jsonld that defines our protocol. The main difference is for the `@type` field that mentions that we are now describing an activity as defined in the Reproschema.

Two other things we can add right away are: 
- the references for this questionnaire,
- the "preamble" that is common to all items in this questionnaire.

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    "@type": "reproschema:Activity",
    "@id": "edinburgh_handedness_inventory_short.jsonld",
    "prefLabel": "Edinburgh handedness inventory - short form",
    "description": "Short version of the Edinburgh handedness inventory",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1",
    "citation": "10.1080/1357650X.2013.783045",
    "preamble": "Please indicate your preferences in the use of hands in the following activities or objects:"
}
```

## Creating items

Now that we have a basic structure for this new activity, let us start adding some items.

Let's first start with the item for `writing`

```bash
# Type this in a terminal window
mkdir activities/EHI/items
touch activities/EHI/items/writing.jsonld
```

The content for items starts like the ones we have seen so far but `"reproschema:Field"` for the `@type` field.

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    "@type": "reproschema:Field",
    "@id": "writing.jsonld",
    "prefLabel": "writing",
    "description": "writing item of the EHI",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1"
}
```

We can now add:

-  the question for this item
-  the response options
-  and the `inputType` for for the user interface that will decide how this item will displayed to the user.

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    "@type": "reproschema:Field",
    "@id": "writing",
    "prefLabel": "writing",
    "description": "writing item of the EHI",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1",
    "question": "Writing",
    "ui": {"inputType": "radio"},
    "responseOptions": {
        "valueType": "xsd:integer",
        "minValue": -100,
        "maxValue": 100,
        "multipleChoice": false,
        "choices": [
            {
                "name": "Always right",
                "value": 100
            },
            {
                "name": "Usually right",
                "value": 50
            },
            {
                "name": "Both equally",
                "value": 0
            },
            {
                "name": "Usually left",
                "value": -50
            },
            {
                "name": "Always left",
                "value": -100
            }
        ]
    }
}
```

### What did we add ?

```json
"question": "Writing",
```

```json
"ui": {"inputType": "radio"},
```

```json
"responseOptions": {
    "valueType": "xsd:integer",
    "minValue": -100,
    "maxValue": 100,
    "multipleChoice": false,
    "choices": [
        {
            "name": "Always right",
            "value": 100
        },
        {
            "name": "Usually right",
            "value": 50
        },
        {
            "name": "Both equally",
            "value": 0
        },
        {
            "name": "Usually left",
            "value": -50
        },
        {
            "name": "Always left",
            "value": -100
        }
    ]
}
```

<!-- TODO
- describe the different input types or at least point the doc of the UI that describes them -->


## In your own time: create a second item

For next step you can create on your own the `throwing` item of the questionnaire.

## Add the items to the activity

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    "@type": "reproschema:Activity",
    "@id": "edinburgh_handedness_inventory_short.jsonld",
    "prefLabel": "Edinburgh handedness inventory - short form",
    "description": "Short version of the Edinburgh handedness inventory",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1",
    "citation": "10.1080/1357650X.2013.783045",
    "preamble": "Please indicate your preferences in the use of hands in the following activities or objects:",
    "ui": {
        "order": [
            "items/writing.jsonld",
            "items/throwing.jsonld"
        ],
        "shuffle": false,
        "addProperties": [
            {
                "variableName": "writing",
                "isAbout": "items/writing.jsonld",
                "isVis": true
            },
            {
                "variableName": "throwing",
                "isAbout": "items/throwing.jsonld",
                "isVis": true
            }
        ]
    }
}
```

### What did we add ?

```json
"ui": {
    "order": [
        "items/writing.jsonld",
        "items/throwing.jsonld"
    ],
    "shuffle": false,
    "addProperties": [
        {
            "variableName": "writing",
            "isAbout": "items/writing.jsonld",
            "isVis": true
        },
        {
            "variableName": "throwing",
            "isAbout": "items/throwing.jsonld",
            "isVis": true
        }
    ]
}
```

## Viewing the activity

Push the content you have created on your repository on github

```bash
# Type this in a terminal window
git add --all
git commit -m 'adding the EHI activity'
git push
```

Use the UI to visualize just the activity.

```
https://www.repronim.org/reproschema-ui/#/activities/0?url=url-to-activity-schema
```

```
https://www.repronim.org/reproschema-ui/#/activities/0?url=https://raw.githubusercontent.com/your_user_name/depression_nimg_schema/activities/edinburgh_handedness_inventory_short.jsonld
```
<!-- https://www.repronim.org/reproschema-ui/#/activities/0?url=https://raw.githubusercontent.com/Remi-Gau/depression_nimg_schema/master/activities/edinburgh_handedness_inventory_short.jsonld -->

<!-- https://www.repronim.org/reproschema-ui/#/activities/0?url=https://raw.githubusercontent.com/ReproNim/reproschema-library/master/activities/PHQ-9/PHQ9_schema -->



## Viewing the results


### Creating an item for the results

```bash
# Type this in a terminal window
mkdir activities/items
touch activities/items/EHI_results.jsonld
```

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    "@type": "reproschema:Field",
    "@id": "EHI_results.jsonld",
    "prefLabel": "EHI results",
    "description": "Edinburgh handedness inventory",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1",
    "ui": {
        "inputType": "number",
        "readonlyValue": true
    },
    "responseOptions": {
        "valueType": "xsd:integer",
        "minValue": -100,
        "maxValue": 100
    }
}
```


```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    "@type": "reproschema:Activity",
    "@id": "edinburgh_handedness_inventory_short.jsonld",
    "prefLabel": "Edinburgh handedness inventory - short form",
    "description": "Short version of the Edinburgh handedness inventory",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1",
    "citation": "10.1080/1357650X.2013.783045",
    "preamble": "Please indicate your preferences in the use of hands in the following activities or objects:",
    "ui": {
        "order": [
            "items/writing.jsonld",
            "items/throwing.jsonld",
            "items/EHI_results.jsonld"
        ],
        "shuffle": false,
        "addProperties": [
            {
                "variableName": "writing",
                "isAbout": "items/writing.jsonld",
                "valueRequired": true,
                "isVis": true
            },
            {
                "variableName": "throwing",
                "isAbout": "items/throwing.jsonld",
                "valueRequired": true,
                "isVis": true
            },
            {
                "isAbout": "items/EHI_results.jsonld",
                "variableName": "EHI_results",
                "isVis": true
            }
        ]
    },
    "compute": [
        {
            "variableName": "EHI_results",
            "jsExpression": "( writing + throwing ) / 2"
        }
    ]
}
```

### What did we add ?

```json
    "ui": {
        "order": [
            ...
            "items/EHI_results.jsonld"
        ],
        "addProperties": [
            ...
            {
                "isAbout": "items/EHI_results.jsonld",
                "variableName": "EHI_results",
                "isVis": true
            }
        ]
    }
```

```json
"compute": [
    {
        "variableName": "EHI_results",
        "jsExpression": "( writing + throwing ) / 2"
    }
]
```

## Adding the activity to the protocol


```json
{
  "@context": [
    "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    {
      "rl": "https://raw.githubusercontent.com/ReproNim/reproschema-library/master/activities/"
    }
  ],
  "@type": "reproschema:Protocol",
  "@id": "depression_nimg_schema.jsonld",
  "prefLabel": "depression neuroimaging study",
  "description": "a study on linguistic processing in depression",
  "schemaVersion": "1.0.0-rc1",
  "version": "0.0.1",
  "landingPage": {EHI
    "@id": "README.md",
    "@language": "en"
  },
  "ui": {
    "addProperties": [
      {
        "isAbout": "rl:PHQ-9/PHQ9_schema",
        "variableName": "PHQ9_schema",
        "prefLabel": { "en": "Depression" }
      },
        {
        "isAbout": "../activities/EHI/edinburgh_handedness_inventory_short.jsonld",
        "variableName": "EHI_short_schema",
        "prefLabel": { "en": "EHI" }
      }
    ],
    "order": [
        "rl:PHQ-9/PHQ9_schema",
        "EHI_short_schema"
        ]
  }
}
```

### What did we add ?

```json
"ui": {
"addProperties": [
    ...
    {
    "isAbout": "../activities/edinburgh_handedness_inventory_short.jsonld",
    "variableName": "EHI_short_schema",
    "prefLabel": { "en": "EHI" }
    }
],
"order": [
    ...
    "EHI_short_schema"
    ]
}
```