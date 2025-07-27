# API Reference

Python API documentation for working with ReproSchema programmatically.

## Installation

```bash
pip install reproschema
```

## Basic Usage

### Import the Module

```python
import reproschema as rs
from reproschema import validate, convert
```

## Validation API

### validate()

Validate ReproSchema files.

```python
def validate(path, schema_version=None, context_url=None):
    """
    Validate ReproSchema files.
    
    Args:
        path (str): Path to file or directory to validate
        schema_version (str, optional): Schema version to validate against
        context_url (str, optional): Custom context URL
        
    Returns:
        bool: True if validation passes, False otherwise
        
    Raises:
        ValidationError: If validation fails
        FileNotFoundError: If path doesn't exist
    """
```

#### Examples

**Validate a single file:**
```python
from reproschema import validate

# Validate a protocol
is_valid = validate("protocols/my_protocol_schema.jsonld")
print(f"Protocol is valid: {is_valid}")

# Validate with specific version
is_valid = validate("protocols/my_protocol_schema.jsonld", schema_version="1.0.0")
```

**Validate a directory:**
```python
# Validate all schemas in directory
is_valid = validate("protocols/")

# Validate multiple directories
for directory in ["protocols/", "activities/", "items/"]:
    is_valid = validate(directory)
    print(f"{directory} is valid: {is_valid}")
```

**Handle validation errors:**
```python
from reproschema import validate, ValidationError

try:
    validate("invalid_schema.jsonld")
except ValidationError as e:
    print(f"Validation failed: {e}")
    print(f"Errors: {e.errors}")
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

## Conversion API

### redcap2reproschema()

Convert REDCap data dictionary to ReproSchema.

```python
def redcap2reproschema(csv_file, yaml_file=None, output_dir="output"):
    """
    Convert REDCap CSV to ReproSchema.
    
    Args:
        csv_file (str): Path to REDCap CSV file
        yaml_file (str, optional): Path to conversion configuration
        output_dir (str): Output directory for generated schemas
        
    Returns:
        dict: Conversion results and statistics
    """
```

#### Examples

**Basic conversion:**
```python
from reproschema import redcap2reproschema

# Convert REDCap CSV
result = redcap2reproschema("redcap_export.csv", output_dir="my_protocol")
print(f"Converted {result['activities_created']} activities")
```

**With configuration:**
```python
# Use YAML configuration for custom mapping
result = redcap2reproschema(
    csv_file="redcap_export.csv",
    yaml_file="conversion_config.yaml",
    output_dir="my_protocol"
)
```

### reproschema2redcap()

Convert ReproSchema to REDCap format.

```python
def reproschema2redcap(protocol_path, output_file="redcap_dictionary.csv"):
    """
    Convert ReproSchema protocol to REDCap CSV.
    
    Args:
        protocol_path (str): Path to protocol schema
        output_file (str): Output CSV file path
        
    Returns:
        str: Path to generated CSV file
    """
```

#### Examples

```python
from reproschema import reproschema2redcap

# Convert protocol to REDCap
csv_path = reproschema2redcap("protocols/my_protocol_schema.jsonld")
print(f"REDCap dictionary saved to: {csv_path}")
```

## Schema Loading API

### load_schema()

Load and parse ReproSchema files.

```python
def load_schema(path):
    """
    Load ReproSchema from file.
    
    Args:
        path (str): Path to schema file
        
    Returns:
        dict: Parsed schema data
    """
```

#### Examples

```python
from reproschema import load_schema

# Load protocol
protocol = load_schema("protocols/my_protocol_schema.jsonld")
print(f"Protocol name: {protocol['prefLabel']}")

# Load activity
activity = load_schema("activities/phq9/phq9_schema.jsonld")
print(f"Activity type: {activity['@type']}")
```

### resolve_references()

Resolve schema references and expand contexts.

```python
def resolve_references(schema, base_path="."):
    """
    Resolve all references in a schema.
    
    Args:
        schema (dict): Schema with references
        base_path (str): Base path for resolving relative references
        
    Returns:
        dict: Schema with resolved references
    """
```

## Schema Creation API

### create_protocol()

Create a new protocol schema.

```python
def create_protocol(name, description, activities=None):
    """
    Create a new protocol schema.
    
    Args:
        name (str): Protocol name
        description (str): Protocol description
        activities (list, optional): List of activity references
        
    Returns:
        dict: New protocol schema
    """
```

#### Examples

```python
from reproschema import create_protocol, save_schema

# Create new protocol
protocol = create_protocol(
    name="Depression Study",
    description="A study measuring depression and anxiety",
    activities=[
        "../activities/phq9/phq9_schema",
        "../activities/gad7/gad7_schema"
    ]
)

# Save to file
save_schema(protocol, "protocols/depression_study_schema.jsonld")
```

### create_activity()

Create a new activity schema.

```python
def create_activity(name, description, items=None):
    """
    Create a new activity schema.
    
    Args:
        name (str): Activity name
        description (str): Activity description
        items (list, optional): List of item references
        
    Returns:
        dict: New activity schema
    """
```

### create_item()

Create a new item schema.

```python
def create_item(question, input_type, response_options=None):
    """
    Create a new item schema.
    
    Args:
        question (str): Item question text
        input_type (str): Input type (radio, text, etc.)
        response_options (dict, optional): Response configuration
        
    Returns:
        dict: New item schema
    """
```

#### Examples

```python
from reproschema import create_item

# Create text item
text_item = create_item(
    question="What is your name?",
    input_type="text",
    response_options={
        "valueType": "xsd:string",
        "maxLength": 100
    }
)

# Create radio item
radio_item = create_item(
    question="How are you feeling?",
    input_type="radio",
    response_options={
        "valueType": "xsd:integer",
        "choices": [
            {"value": 1, "name": "Very bad"},
            {"value": 2, "name": "Bad"},
            {"value": 3, "name": "Okay"},
            {"value": 4, "name": "Good"},
            {"value": 5, "name": "Very good"}
        ]
    }
)
```

## Utility Functions

### save_schema()

Save schema to file.

```python
def save_schema(schema, file_path):
    """
    Save schema to JSON-LD file.
    
    Args:
        schema (dict): Schema to save
        file_path (str): Output file path
    """
```

### get_schema_version()

Get current schema version.

```python
def get_schema_version():
    """
    Get the current ReproSchema version.
    
    Returns:
        str: Version string
    """
```

### list_field_types()

Get available field types.

```python
def list_field_types():
    """
    List all available input types.
    
    Returns:
        list: Available input types
    """
```

## Error Handling

### ValidationError

Raised when schema validation fails.

```python
class ValidationError(Exception):
    def __init__(self, message, errors=None):
        self.message = message
        self.errors = errors or []
        super().__init__(self.message)
```

### ConversionError

Raised when format conversion fails.

```python
class ConversionError(Exception):
    def __init__(self, message, source_format=None, target_format=None):
        self.message = message
        self.source_format = source_format
        self.target_format = target_format
        super().__init__(self.message)
```

## Configuration

### Set Default Context

```python
from reproschema import set_default_context

set_default_context("https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema")
```

### Set Validation Options

```python
from reproschema import set_validation_options

set_validation_options({
    "strict_mode": True,
    "check_references": True,
    "validate_context": True
})
```

## Examples

### Complete Workflow

```python
from reproschema import (
    redcap2reproschema, 
    validate, 
    load_schema,
    reproschema2redcap
)

# 1. Convert from REDCap
result = redcap2reproschema("study.csv", output_dir="my_study")

# 2. Validate generated schemas
is_valid = validate("my_study/")
if not is_valid:
    print("Validation failed!")
    exit(1)

# 3. Load and inspect protocol
protocol = load_schema("my_study/protocols/my_study_schema.jsonld")
print(f"Protocol: {protocol['prefLabel']}")

# 4. Convert back to REDCap for sharing
redcap_file = reproschema2redcap("my_study/protocols/my_study_schema.jsonld")
print(f"REDCap dictionary: {redcap_file}")
```

### Batch Processing

```python
import os
from reproschema import validate

# Validate all protocols in multiple directories
study_dirs = ["study1/", "study2/", "study3/"]

for study_dir in study_dirs:
    if os.path.exists(f"{study_dir}/protocols/"):
        is_valid = validate(f"{study_dir}/protocols/")
        print(f"{study_dir}: {'✓ Valid' if is_valid else '✗ Invalid'}")
```

## See Also

- [Field Types Reference](field-types.md)
- [Validation How-To](../how-to/validation.md)
- [Conversion How-To](../how-to/convert-from-redcap.md)