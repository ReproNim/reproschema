![Python package](https://github.com/ReproNim/reproschema/workflows/Python%20package/badge.svg)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4064940.svg)](https://doi.org/10.5281/zenodo.4064940)

<img src="docs/img/reproschema_logo.png" width="100px" />

# ReproSchema: Enhancing Research Reproducibility through Standardized Survey Data Collection

The ReproSchema project integrates five key components designed to standardize research protocols and enhance consistency across various stages of data collection.
- Foundational Schema ([reproschema](https://github.com/ReproNim/reproschema)): This core schema delineates the content and relationships of protocols, assessments, and items to ensure consistency and facilitate data harmonization across studies.
- Assessment Library ([reproschema-library](https://github.com/ReproNim/reproschema-library)): This library provides a comprehensive collection of standardized questionnaires, supporting the application of uniform assessments across time and different studies.
- Python-based CLI Tool ([reproschema-py](https://github.com/ReproNim/reproschema-py)): This command-line interface tool facilitates schema development and validation, aiding researchers in efficiently creating and refining data collection frameworks.
- User Interface ([reproschema-ui](https://github.com/ReproNim/reproschema-ui)): This intuitive user interface simplifies the visualization and interaction with data, enhancing the manageability of the data collection process for researchers.
- Protocol Template ([reproschema-protocol-cookiecutter](https://github.com/ReproNim/reproschema-protocol-cookiecutter)): This customizable template supports the design and implementation of research protocols tailored to specific study requirements.

This repository contains:

- the [different terms of the ReproSchema](./terms)
- the [corresponding context files](./contexts)
- a example of [a protocol based on the reproschema](./examples)
- the [documentation](./docs)

## Developing ReproSchema

### Updating the schema

As of release 1.0.0, a linked data modeling language, [LinkML](https://linkml.io/linkml/), is used to create
a [YAML file](linkml-schema/reproschema.yaml) with the schema.

The [context file](contexts/reproschema) was automatically generated using LinkML,
and then manually curated in order to support all the reproschema feature.

#### Style

This repo uses pre-commit to check styling.
- Install pre-commit with pip: `pip install pre-commit`
- In order to use it with the repository, you have to run `run pre-commit install` in the root directory the first time you use it.


### Release
Upon release, there are additional formats, `jsonsld`, `turtle`, `n-triples`
and `pydantic` that are created using `LinkML` tools, `reproschema-py`,
and [reproschema-specific script](./scripts/fix_pydantic.py) to "fix" the `pydantic` format.
The entire process is automated in the GitHub Action Workflow:
[Validate and Release](.github/workflows/validate_and_release.yml).
This workflow must be manually triggered by the core developers once a new release is ready.
All the releases can be found in [releases directory](./releases).

### Updating model in reproschema-py
Another GitHub Action Workflow: [ Create Pull Request to reproschema-py](.github/workflows/push_reproschema_py.yml)
is responsible for creating pull request to the `reproschema-py` Python library with
the new version of pydantic model and context.
The workflow is currently also triggered manually by the core developers.


## Licenses

### Code

The content of this repository is distributed under the [Apache 2.0 license](./LICENSE).

### Documentation

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />The corresponding documentation is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Contributors

https://github.com/ReproNim/reproschema/graphs/contributors
