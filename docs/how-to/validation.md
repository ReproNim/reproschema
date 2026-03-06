# Validate Your Schemas

Ensure your ReproSchema files are correctly formatted and compliant.

## Goal

Validate schema files to catch errors before deployment.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

Install the reproschema validation tools:

```bash
pip install reproschema
```

## Basic Validation

### Validate a Single File

```bash
reproschema validate path/to/schema.jsonld
```

### Validate a Directory

```bash
reproschema validate protocols/
```

This validates all `.jsonld` files in the directory and subdirectories.

### Verbose Output

For detailed validation information:

```bash
reproschema --log-level DEBUG validate protocols/
```

## Common Validation Errors

### 1. Missing Required Fields

**Error:**
```
ValidationError: '@context' is a required property
```

**Solution:** Add the required `@context`:
```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    ...
}
```

### 2. Invalid @type

**Error:**
```
ValidationError: 'Activity' is not valid under any of the given schemas
```

**Solution:** Use the correct type with prefix:
```json
"@type": "reproschema:Activity"
```

### 3. Invalid References

**Error:**
```
ValidationError: Could not resolve '../activities/missing_activity'
```

**Solution:** Check that:
- The file path is correct
- The referenced file exists
- Use forward slashes (/) not backslashes

### 4. JSON Syntax Errors

**Error:**
```
JSONDecodeError: Expecting ',' delimiter
```

**Solution:** 
- Check for missing commas between properties
- Ensure quotes are properly closed
- Validate JSON syntax first using a JSON validator

## Advanced Validation

### Validate Specific Schema Version

```bash
reproschema validate --schema-version 1.0.0 protocols/
```

### Validate with Custom Context

```bash
reproschema validate --context https://your-context-url protocols/
```

### Validate Multiple Paths

```bash
reproschema validate protocols/ activities/ items/
```

## Validation Best Practices

1. **Validate Early and Often**
   - Run validation after each change
   - Don't wait until deployment

2. **Use Debug Mode for Development**
   ```bash
   reproschema --log-level DEBUG validate .
   ```

3. **Validate Before Commits**
   Add to your git pre-commit hook:
   ```bash
   #!/bin/sh
   reproschema validate protocols/ activities/
   ```

4. **Check References**
   Ensure all referenced files exist before validation

## Understanding Validation Output

### Success Output
```
✓ protocols/my_protocol_schema.jsonld
✓ activities/phq9/phq9_schema.jsonld
All schemas are valid!
```

### Error Output
```
✗ protocols/my_protocol_schema.jsonld
  - Line 15: Missing required field 'prefLabel'
  - Line 23: Invalid reference to '../activities/missing'
1 schema(s) failed validation
```

## Troubleshooting

### Installation Issues

If `pip install reproschema` fails:

1. Upgrade pip:
   ```bash
   python -m pip install --upgrade pip
   ```

2. Try installing in a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install reproschema
   ```

### Validation Hangs

If validation seems stuck:
- Check for circular references in schemas
- Use `--timeout 30` to set a timeout
- Validate files individually to isolate the issue

### Context Loading Errors

If you see "Could not load context":
- Ensure you have internet connectivity
- Check if context URLs are accessible
- Try using a local context file

## Next Steps

- [Set up CI/CD validation](setup-ci.md)
- [Visualize validated schemas](visualize.md)
- [Deploy validated protocols](deploy-protocol.md)

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
