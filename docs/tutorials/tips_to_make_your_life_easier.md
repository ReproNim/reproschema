# Tips to make your life easier

## Validating your json files

<!-- TODO
- mention that it needs node.js and add a pointer on how to install it
-->

First, make sure your syntax is in correct jsonld format. Test all files with
`@context` from command line:

```bash
npm install -g jsonlint
grep -r "@context" . | cut -d: -f1 | xargs -I fname jsonlint -q fname
```

Or test individual files on the [json linter website](https://jsonlint.com/).

## Validating your schema

<!-- TODO
- add more details
- mention that it needs python and add a pointer to reproschema-py
-->

```bash
pip install reproschema requests_cache
reproschema -l DEBUG validate activities
```

## Automating those checks

It can be quickly become cumbersome to type some of the commands described above
to always make sure the files you have created are valid.

Thankfully though there are ways to automate those checks and integrate them
into your workflow. They rely on using some of the features of Github or Git.

### Github actions

The first one is using Github actions to let Github perform those checks for you
every time there some new content is added on a repository.

To set those up you simply need to create a `.github/workflows` folder inside
the repository where you are working. This will contain all the workflows (a set
of "actions") that Github has to run on this repository. Each workflow is
described by a `yml` file.

<!-- TODO
- add link to the turing-way section on yml files.
-->

For example you could create a `validate.yml` file in this repository.

```
├── .git # hidden git folder
├── .github # hidden github folder
│    └── workflows
│        └── validate.xml # file the actions used to validate your schema
├── protocols
│    ├── README-en.md
│    └── protocol-1.jsonld
├── activities
│    ├── items
│    │   └── item-1.jsonld
│    └── activity-1.jsonld
└── README.md
```

The content of `validate.yml` file would look like this.

```yaml
name: validate protocol and activities

# describes when this workfllow is triggered
on:
  push: # when pushing to a branch
    branches: [master] # on which branch
  pull_request: # when opening a new pull request
    branches: "*" # * refers to all branches

jobs:
  build:
    # describes the operating system that will #be used
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks executed as part of the job
    steps:
      - name: Setup Node # installing Node.js for all the javascript part
        uses: actions/setup-node@v1
        with:
          node-version: "12.x"

      # Checks-out your repository under $GITHUB_WORKSPACE,
      #  so your job can access it
      - uses: actions/checkout@v2

      # Checks that our JSON are valid
      # Installing `jsonlint` to validate the JSON files
      # Looking recursively through the directories `protocol`
      # and `activities` for any file with "@context" in them
      # (that makes them jsonld files) and validate their content
      # with jsonlint
      - name: Check for syntax errors
        run: |
          npm install -g jsonlint
          grep -r  "@context" activities | cut -d: -f1 | xargs -I fname jsonlint -q fname
          grep -r  "@context" protocols | cut -d: -f1 | xargs -I fname jsonlint -q fname

      # Checks that the schemas are valid
      # Using python and the installing the reproschema tools
      # from the reproschema-py repository to then validate
      # the content of the `activities` and `protocols` folders.
      - name: Set up Python 3.8
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip setuptools
          pip install reproschema requests_cache

      - name: Test with pyshacl
        run: |
          reproschema -l DEBUG validate activities
          reproschema -l DEBUG validate protocols
```

### Using git hooks and pre-commit

## Using a template for a new protocol

If you are starting a new study from scratch and already familiar with some of
the basics of reproschema, we recommend you use our template repository that
already has some basic set-up to to validate your files...

<!-- TODO
- Actually create a template repo
-->

## Using presets response options

If you have to create several items that always have the same set of response
options, then it might be easier to create a separate file with those response
options and point each item to that file instead. This way, if you need to
change the characteristics of one response, you only have to change things in
one file rather than in many.

For example, you could create response set file to constrains the possible
answers on the questions of the Edinburgh Handedness Inventory we have been
working on by organizing things this way.

```
activities
├── edinburgh_handedness_inventory_short.jsonld
├── leftRightValueConstraints.jsonld
└── items
    ├── writing.jsonld
    ├ ...
    ...
```

The content of the `leftRightValueConstraints.jsonld` file would look like this:

```json
{
  "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
  "@id": "leftRightValueConstraints.jsonld",
  "@type": "reproschema:ResponseOption",
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

And you can point each item to it by referring to the local file in the
`responseOptions` field.

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
  "ui": { "inputType": "radio" },
  "responseOptions": "../leftRightValueConstraints.jsonld"
}
```

<!-- ## Programmatic schema generation

Tool to convert redcap CSVs to our schema format. But it cannot be used to convert every
redcap-formatted table as some are customized redcap tables (for example the 100s that are in ABCD)
but does cover most cases. A template of the CSV and how to use the tool can be found
[here](https://github.com/sanuann/reproschema-builder) -->
