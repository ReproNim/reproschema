# Validation

### Validating your schema

If you want to validate a schema you have created:

- install the reproschema python tools

```bash
pip install reproschema
```

- run its `validate` command

```bash
reproschema --log-level DEBUG validate PATH_TO_VALIDATE
```

!!! note

    You can validate a single file or all the files in a folder and its subfolder.

### Automating validation

If you are hosting your schema on a github repository,
you can automate its validation with a with GitHub CI workflow.

For example if your repository is structured like this:

```text
├── protocols
│    └── protocol-1.jsonld
├── activities
│    ├── items
│    │   └── item-1.jsonld
│    └── activity-1.jsonld
└── README.md
```

create a `.github/workflows/validate.yml` file in this repository.

```text hl_lines="1-3"
├── .github # hidden github folder
│    └── workflows
│        └── validate.yml # file the actions used to validate your schema
├── protocols
│    └── protocol-1.jsonld
├── activities
│    ├── items
│    │   └── item-1.jsonld
│    └── activity-1.jsonld
└── README.md
```

Content of `validate.yml`:

```yaml
name: validation

on:
  push:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: 3.12
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip setuptools
        pip install reproschema-py
    - name: validate
      run: |
        reproschema validate protocols
        reproschema validate activities
```

!!! note

    Note that if you have created your schema
    using the [reproschema cookie cutter](../user-guide/create-new-protocol.md)
    then a validation workflow should already be included in your repository.
