![Python package](https://github.com/ReproNim/reproschema/workflows/Python%20package/badge.svg)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4064940.svg)](https://doi.org/10.5281/zenodo.4064940)

<img src="docs/img/reproschema_logo.png" width="100px" />

# ReproSchema: Enhancing Research Reproducibility through Standardized Survey Data Collection

## Table of Contents

- [Introduction](#introduction)
- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
  - [Creating a Simple Item](#creating-a-simple-item)
  - [Creating an Activity](#creating-an-activity)
  - [Creating a Protocol](#creating-a-protocol)
  - [Validating Schemas](#validating-schemas)
- [Schema Structure](#schema-structure)
  - [File Formats](#file-formats)
  - [Schema Components](#schema-components)
- [ReproSchema Ecosystem](#reproschema-ecosystem)
- [Repository Structure](#repository-structure)
- [Development](#development)
  - [Updating the Schema](#updating-the-schema)
  - [Style Guidelines](#style-guidelines)
  - [Release Process](#release-process)
- [Resources and Links](#resources-and-links)
- [Licenses](#licenses)
- [Contributors](#contributors)

## Introduction

ReproSchema is a standardized framework for creating, sharing, and reusing cognitive and clinical assessments. It addresses the lack of consistency in assessment data acquisition across studies by providing a common schema that captures relationships between questionnaire elements from the start.

**Key Benefits:**
- 📊 **Rich Context**: JSON-LD format provides semantic relationships rather than flat CSV files
- 🔄 **Version Control**: Track different versions of questionnaires (e.g., PHQ-9, PHQ-8)
- 🌍 **Internationalization**: Built-in support for multiple languages
- 🔗 **Persistent Identifiers**: Unique IDs for items, activities, and protocols
- ✅ **Validation**: Schema validation using SHACL ensures data quality
- 🚀 **Implementation Agnostic**: Use with any software platform

## Quick Start

Get started with ReproSchema in minutes:

```bash
# Install the ReproSchema Python package
pip install reproschema

# Validate an example schema
reproschema validate examples/protocols/protocol1.jsonld

# Create a new protocol from template (requires cookiecutter)
pip install cookiecutter
cookiecutter https://github.com/ReproNim/reproschema-protocol-cookiecutter
```

## Prerequisites

Before using ReproSchema, ensure you have:

- **Python 3.8+**: Required for the reproschema-py tools
- **Git**: For version control and cloning repositories
- **Text Editor**: Preferably with JSON/JSON-LD support (e.g., VS Code)
- **Basic JSON Knowledge**: Understanding of JSON syntax

Optional but recommended:
- **GitHub Account**: For hosting and sharing your schemas
- **Node.js**: If using the reproschema-ui interface

## Installation

### Installing the Python Package

The easiest way to work with ReproSchema is through the Python package:

```bash
# Using pip
pip install reproschema

# Using pip with specific version
pip install reproschema==1.0.0

# For development (with latest changes)
pip install git+https://github.com/ReproNim/reproschema-py.git
```

### Cloning the Repository

To access examples and contribute to the schema:

```bash
git clone https://github.com/ReproNim/reproschema.git
cd reproschema
```

## Usage Examples

### Creating a Simple Item

An item represents a single question in a questionnaire. Here's a basic example:

```json
{
  "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
  "@type": "reproschema:Field",
  "@id": "age_item",
  "prefLabel": "Age",
  "description": "Participant's age in years",
  "schemaVersion": "1.0.0",
  "version": "1.0.0",
  "ui": {
    "inputType": "number"
  },
  "responseOptions": {
    "valueType": "xsd:integer",
    "minValue": 0,
    "maxValue": 120,
    "unitCode": "years"
  }
}
```

### Creating an Activity

An activity groups related items (like a complete questionnaire):

```json
{
  "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
  "@type": "reproschema:Activity",
  "@id": "demographics_activity",
  "prefLabel": "Demographics",
  "description": "Basic demographic information",
  "schemaVersion": "1.0.0",
  "version": "1.0.0",
  "ui": {
    "order": ["age_item", "gender_item"],
    "shuffle": false,
    "addProperties": [
      {
        "variableName": "age",
        "isAbout": "age_item",
        "isVis": true
      },
      {
        "variableName": "gender",
        "isAbout": "gender_item",
        "isVis": true
      }
    ]
  }
}
```

### Creating a Protocol

A protocol combines multiple activities for a complete study:

```json
{
  "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
  "@type": "reproschema:Protocol",
  "@id": "my_study_protocol",
  "prefLabel": "My Research Study",
  "description": "Protocol for my research study",
  "schemaVersion": "1.0.0",
  "version": "1.0.0",
  "ui": {
    "order": ["demographics_activity", "phq9_activity"],
    "shuffle": false,
    "addProperties": [
      {
        "variableName": "demographics",
        "isAbout": "demographics_activity",
        "prefLabel": "Demographics",
        "isVis": true
      },
      {
        "variableName": "phq9",
        "isAbout": "phq9_activity",
        "prefLabel": "PHQ-9 Depression Scale",
        "isVis": true
      }
    ]
  }
}
```

### Validating Schemas

Always validate your schemas to ensure they're correctly formatted:

```bash
# Validate a single file
reproschema validate my_protocol.jsonld

# Validate all files in a directory
reproschema validate protocols/

# Validate with detailed output
reproschema --log-level DEBUG validate my_schema.jsonld
```

## Schema Structure

### File Formats

ReproSchema uses several file formats:

- **JSON-LD (.jsonld)**: Primary format combining JSON with Linked Data
- **Turtle (.ttl)**: RDF serialization format
- **N-Triples (.nt)**: Line-based RDF format
- **YAML**: Used for LinkML schema definitions

### Schema Components

The ReproSchema consists of three hierarchical levels:

1. **Items (Fields)**: Individual questions or data points
   - Question text and descriptions
   - Input types (text, number, select, etc.)
   - Response options and constraints
   - Visibility conditions

2. **Activities**: Collections of related items
   - Groups items into logical assessments
   - Defines item order and display logic
   - Can include scoring computations
   - Supports branching logic

3. **Protocols**: Complete study designs
   - Combines multiple activities
   - Defines activity order and scheduling
   - Manages participant flow
   - Includes study-level metadata

## ReproSchema Ecosystem

The ReproSchema project integrates five key components designed to standardize research protocols and enhance consistency across various stages of data collection:

### 1. Foundational Schema ([reproschema](https://github.com/ReproNim/reproschema))
This core schema delineates the content and relationships of protocols, assessments, and items to ensure consistency and facilitate data harmonization across studies.

### 2. Assessment Library ([reproschema-library](https://github.com/ReproNim/reproschema-library))
A comprehensive collection of standardized questionnaires, supporting the application of uniform assessments across time and different studies.

### 3. Python CLI Tool ([reproschema-py](https://github.com/ReproNim/reproschema-py))
Command-line interface tool that facilitates schema development and validation, aiding researchers in efficiently creating and refining data collection frameworks.

### 4. User Interface ([reproschema-ui](https://github.com/ReproNim/reproschema-ui))
An intuitive web interface that simplifies the visualization and interaction with data, enhancing the manageability of the data collection process for researchers.

### 5. Protocol Template ([reproschema-protocol-cookiecutter](https://github.com/ReproNim/reproschema-protocol-cookiecutter))
A customizable template that supports the design and implementation of research protocols tailored to specific study requirements.

## Repository Structure

This repository contains:

```
reproschema/
├── terms/              # ReproSchema vocabulary terms
├── contexts/           # JSON-LD context files
├── examples/           # Example protocols, activities, and items
│   ├── activities/     # Sample activities
│   ├── protocols/      # Sample protocols
│   └── responses/      # Sample response data
├── linkml-schema/      # LinkML schema definitions
├── releases/           # Official release versions
├── docs/               # Documentation
│   ├── tutorials/      # Step-by-step guides
│   ├── how-to/         # Task-specific instructions
│   └── user-guide/     # Comprehensive user documentation
└── scripts/            # Utility scripts
```

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

## Citation

If you use ReproSchema in your research, please cite our paper:

Chen Y, Jarecka D, Abraham S, Gau R, Ng E, Low D, Bevers I, Johnson A, Keshavan A, Klein A, Clucas J, Rosli Z, Hodge S, Linkersdörfer J, Bartsch H, Das S, Fair D, Kennedy D, Ghosh S. **Standardizing Survey Data Collection to Enhance Reproducibility: Development and Comparative Evaluation of the ReproSchema Ecosystem**. J Med Internet Res 2025;27:e63343. DOI: [10.2196/63343](https://doi.org/10.2196/63343)

## Contributors

https://github.com/ReproNim/reproschema/graphs/contributors
