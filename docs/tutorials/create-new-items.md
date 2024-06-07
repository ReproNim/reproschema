## Creating items

Now that we have a basic structure for this new activity, let us start adding some items.

Let's first start with the item for `writing`

```bash
# Type this in a terminal window
mkdir activities/EHI/items
touch activities/EHI/items/writing.jsonld
```

The content for items starts like the ones we have seen so far but
`"reproschema:Field"` for the `@type` field.

```json linenums="1"
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

-   the question for this item
-   the `inputType` for for the user interface that will decide how this item will displayed to the user.
-   the response options

```json linenums="1" hl_lines="9 10 11-38"
--8<-- "examples/activities/EHI/items/writing.jsonld"
```

<!-- TODO
- describe the different input types or at least point the doc of the UI that describes them
-->

## In your own time: create a second item

For next step you can create on your own the `throwing` item of the questionnaire.

## Add the items to the activity

```json linenums="1"  hl_lines="11-26"
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
    "order": ["items/writing.jsonld", "items/throwing.jsonld"],
    "shuffle": false,
    "addProperties": [
      {
        "variableName": "writing",jsonld
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

## Viewing the results

### Creating an item for the results

```bash
# Type this in a terminal window
touch activities/EHI/items/EHI_results.jsonld
```

Add the following content to it.

```json linenums="1"
--8<-- "examples/activities/EHI/items/EHI_results.jsonld"
```

Add it to the activity.

```json linenums="1" hl_lines="15 31-35 38-42"
--8<-- "examples/activities/EHI/edinburgh_handedness_inventory_short.jsonld"
```

## Using presets response options

If you have to create several items that always have the same set of response options,
then it might be easier to create a separate file with those response options and point each item to that file instead.
This way, if you need to change the characteristics of one response,
you only have to change things in one file rather than in many.

For example, you could create response set file to constrains the possible answers
on the questions of the Edinburgh Handedness Inventory we have been working on by organizing things this way.

```text
activities
├── edinburgh_handedness_inventory_short.jsonld
├── leftRightValueConstraints.jsonld
└── items
    ├── writing.jsonld
    ├ ...
    ...
```

The content of the `leftRightValueConstraints.jsonld` file would look like this:

```json linenums="1"
--8<-- "examples/activities/EHI/leftRightValueConstraints.jsonld"
```

And you can point each item to it by referring to the local file in the `responseOptions` field.

```json linenums="1" hl_lines="11"
{
  "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
  "@type": "reproschema:Field",
  "@id": "writing",
  "prefLabel": "writing",
  "description": "writing item of the EHI",
  "schemaVersion": "1.0.0-rc1",
  "version": "0.0.1",
  "question": "Writing",
  "ui": { "inputType": "radio" },
  "responseOptions": "../leftRightValueConstraints.jsonld"
}
```

<!-- ## Programmatic schema generation
Tool to convert redcap CSVs to our schema format. But it cannot be used to convert every
redcap-formatted table as some are customized redcap tables (for example the 100s that are in ABCD)
but does cover most cases. A template of the CSV and how to use the tool can be found
[here](https://github.com/sanuann/reproschema-builder)
-->
