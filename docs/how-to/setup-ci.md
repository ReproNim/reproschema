# Set Up Continuous Integration

Automate validation and testing of your ReproSchema schemas.

## Goal

Ensure your schemas are valid and consistent through automated checks.

## Prerequisites

- GitHub repository with ReproSchema schemas
- Basic knowledge of Git workflows

## Steps

### 1. Enable GitHub Actions

GitHub Actions is already configured in the reproschema repository. You can customize it for your fork.

### 2. Pre-commit Configuration

#### Install pre-commit
```bash
pip install pre-commit
```

#### Install hooks
```bash
cd your-reproschema-repo
pre-commit install
```

### 3. Create .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-added-large-files
        args: ['--maxkb=1000']

  - repo: local
    hooks:
      - id: reproschema-validate
        name: Validate ReproSchema schemas
        entry: reproschema validate
        language: system
        files: \.(jsonld|json)$
        pass_filenames: true
```

### 4. GitHub Actions Workflow

Create `.github/workflows/validate.yml`:

```yaml
name: Validate Schemas

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  validate:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install ReproSchema
      run: |
        pip install reproschema

    - name: Validate all schemas
      run: |
        reproschema validate protocols/*/*.jsonld
        reproschema validate activities/*/*.jsonld
        reproschema validate items/*/*.jsonld

    - name: Check for syntax errors
      run: |
        find . -name "*.jsonld" -exec python -m json.tool {} \; > /dev/null
```

### 5. Linting Configuration

#### JSON Schema Linting
```yaml
# .github/workflows/lint.yml
name: Lint Schemas

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Validate JSON syntax
      run: |
        find . -name "*.jsonld" -exec python -m json.tool {} \; > /dev/null

    - name: Check for duplicate IDs
      run: |
        python scripts/check_duplicates.py
```

#### Create check_duplicates.py
```python
#!/usr/bin/env python3
import json
import glob
from collections import defaultdict

ids = defaultdict(list)

for file in glob.glob('**/*.jsonld', recursive=True):
    with open(file) as f:
        data = json.load(f)
        schema_id = data.get('@id', '')
        if schema_id:
            ids[schema_id].append(file)

# Report duplicates
for schema_id, files in ids.items():
    if len(files) > 1:
        print(f"Duplicate ID {schema_id} found in:")
        for file in files:
            print(f"  - {file}")
```

### 6. Automated Testing

#### Unit Tests
```python
# tests/test_schemas.py
import json
import glob

def test_all_schemas_have_id():
    """All schemas must have @id field"""
    for file in glob.glob('**/*.jsonld', recursive=True):
        with open(file) as f:
            data = json.load(f)
            assert '@id' in data, f"{file} missing @id"

def test_all_schemas_have_type():
    """All schemas must have @type field"""
    for file in glob.glob('**/*.jsonld', recursive=True):
        with open(file) as f:
            data = json.load(f)
            assert '@type' in data, f"{file} missing @type"

def test_activity_items_exist():
    """Activity references must point to existing items"""
    # Implement checks for item references
    pass
```

#### Test Workflow
```yaml
# .github/workflows/test.yml
name: Test Schemas

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        pip install pytest

    - name: Run tests
      run: |
        pytest tests/
```

### 7. Pre-commit with pre-commit.ci

Enable automatic pre-commit.ci for PRs:

1. Visit https://pre-commit.ci/
2. Authorize your repository
3. Add `.pre-commit-config.yaml` to your repo
4. Pre-commit.ci will run automatically on PRs

### 8. Branch Protection Rules

Set up in GitHub repository settings:

```yaml
Required checks:
  - Validate Schemas
  - Lint Schemas
  - Test Schemas

Require branches to be up to date before merging
Require status checks to pass before merging
Require pull request reviews before merging
```

### 9. Release Workflow

Automate release validation:

```yaml
# .github/workflows/release.yml
name: Release

on:
  release:
    types: [published]

jobs:
  validate-release:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install ReproSchema
      run: pip install reproschema

    - name: Validate release
      run: |
        reproschema validate protocols/*/*.jsonld
        reproschema validate activities/*/*.jsonld
        reproschema validate items/*/*.jsonld

    - name: Create release assets
      run: |
        tar -czf schemas.tar.gz protocols/ activities/ items/
        gh release upload ${{ github.event.release.tag_name }} schemas.tar.gz
```

## Troubleshooting

### Pre-commit not working
```bash
# Clear cache
pre-commit clean

# Reinstall hooks
pre-commit uninstall
pre-commit install
```

### CI failing locally but passing remotely
- Check Python version
- Verify dependencies
- Review environment variables

### Slow CI pipeline
- Cache dependencies
- Use matrix strategy sparingly
- Parallelize independent jobs

## Best Practices

1. **Fast feedback**: Keep CI pipeline quick
2. **Clear error messages**: Help contributors fix issues
3. **Comprehensive checks**: Validate schemas, lint code, run tests
4. **Automate releases**: Use release workflows
5. **Document requirements**: Keep README updated

## Next Steps

- [Create your first schema](create-protocol.md)
- [Validate schemas manually](validation.md)
- [Set up deployment](deploy-protocol.md)
