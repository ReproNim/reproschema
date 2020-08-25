# Create a new activity

Now you would like to add a small questionaire 




Activity directory structure:

- `/items` (directory) : contains the `jsonld` files for individual items of the activity schema
  - `item_1`
  - `item_2`
  - …
- `activityName_schema` : schema to define the activity
- `activityName_context` : context to define keys used specific to the activity schema

Creating `activityName_schema` – use the keys defined in [`schemas/Activity`](./schemas/Activity).
If any other keys are used, then define them in `activityName_context`

Mandatory keys:

- `@context` - [Array] Include the ReproNim generic context JSON-LD file along with the activity context.
- `@type`- describes type of the schema.
- `@id` - unique id for the schema. should be same as the filename.
- `skos:prefLabel` - display name for the schema
- `ui.addProperties` - defines the various properties of each item.
- `variablename` - variable name used in `ui.order` for the items
- `isAbout` - file name of the corresponding variable name
- `ui.order` - [Array] defines the order in which the items appear in the activity

### Create items

To create `item_x` in the items folder:

- Use keys defined in [`schemas/Field`](./schemas/Field)
- `@type`=`"https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/Field"`
- `responseOptions` – can be embedded or can point to a remote JSON-LD object.

## Programmatic schema generation

Tool to convert redcap CSVs to our schema format. But it cannot be used to convert every
redcap-formatted table as some are customized redcap tables (for example the 100s that are in ABCD)
but does cover most cases. A template of the CSV and how to use the tool can be found
[here](https://github.com/sanuann/reproschema-builder)
