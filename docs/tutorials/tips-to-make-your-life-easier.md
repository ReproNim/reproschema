# Tips to make your life easier

## Validating your JSON files

First, make sure your syntax is in correct JSON-LD format.
Test all files with `@context` from command line:

```bash
npm install -g jsonlint
grep -r "@context" . | cut -d: -f1 | xargs -I fname jsonlint -q fname
```

Or test individual files on the [json linter website](https://jsonlint.com/).

## Validating your schema

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

To set those up you simply need to create a `.github/workflows` folder inside the repository where you are working.
This will contain all the workflows (a set of "actions") that Github has to run on this repository.
Each workflow is described by a `yml` file.

For example you could create a `validate.yml` file in this repository.

```text
├── .git # hidden git folder
├── .github # hidden github folder
│    └── workflows
│        └── validate.yml # file the actions used to validate your schema
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
--8<-- ".github/workflows/validate.yml"
```
