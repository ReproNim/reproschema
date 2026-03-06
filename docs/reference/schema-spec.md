# ReproSchema Schema Specification

Complete technical specification of the ReproSchema data model.

## Overview

ReproSchema is a Linked Data model for representing protocols, activities, and items in a structured, machine-readable format. It uses JSON-LD (JSON for Linked Data) with a well-defined context.

## JSON-LD Context

### Base Context

```json
{
    "@context": {
        "@vocab": "http://schema.repronim.org/",
        "reproschema": "http://schema.repronim.org/",
        "schema": "http://schema.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "prov": "http://www.w3.org/ns/prov#",
        "obo": "http://purl.obolibrary.org/obo/"
    }
}
```

### Full Context URL

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema"
}
```

## Core Classes

### Protocol

The top-level container for a study or assessment.

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    "@type": "reproschema:Protocol",
    "@id": "my_protocol",
    "prefLabel": "My Study Protocol",
    "description": "Description of the protocol",
    "landingPage": {
        "@id": "README.md",
        "@language": "en"
    },
    "ui": {
        "order": [
            "../activities/activity1/activity1_schema"
        ],
        "shuffle": false,
        "addProperties": [...]
    }
}
```

**Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@id` | string | Yes | Unique identifier |
| `@type` | string | Yes | Must be "reproschema:Protocol" |
| `prefLabel` | string | Yes | Human-readable name |
| `description` | string | No | Detailed description |
| `landingPage` | object | No | Reference to landing page |
| `ui` | object | Yes | UI configuration |
| `about` | array | No | What the protocol is about |
| `preamble` | string | No | Instructions for participants |
| `compute` | object | No | Computed fields |

### Activity

A group of related items/questions.

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    "@type": "reproschema:Activity",
    "@id": "my_activity",
    "prefLabel": "My Activity",
    "description": "Description of activity",
    "ui": {
        "order": [
            "../items/item1/item1_schema"
        ],
        "shuffle": false,
        "addProperties": [...]
    }
}
```

**Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@id` | string | Yes | Unique identifier |
| `@type` | string | Yes | Must be "reproschema:Activity" |
| `prefLabel` | string | Yes | Human-readable name |
| `description` | string | No | Detailed description |
| `ui` | object | Yes | UI configuration |
| `about` | array | No | What the activity is about |
| `isAbout` | string | No | Reference to ontology term |
| `preamble` | string | No | Activity instructions |
| `compute` | object | No | Computed fields |

### Field (Item)

An individual question or data field.

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    "@type": "reproschema:Item",
    "@id": "my_item",
    "prefLabel": "My Question",
    "question": "What is your answer?",
    "description": "Additional context",
    "responseOptions": {
        "valueType": "xsd:integer",
        "choices": [...],
        "minValue": 0,
        "maxValue": 10
    },
    "ui": {
        "inputType": "radio"
    }
}
```

**Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@id` | string | Yes | Unique identifier |
| `@type` | string | Yes | Must be "reproschema:Item" |
| `prefLabel` | string | Yes | Human-readable label |
| `question` | string | No | The question text |
| `description` | string | No | Additional context |
| `responseOptions` | object | Yes | Response specification |
| `isAbout` | string | No | Ontology reference |
| `ui` | object | No | UI configuration |
| `validate` | object | No | Validation rules |

## Response Options

### Data Types

```json
{
    "valueType": "xsd:string"
}
```

Supported types:
- `xsd:string` - Text input
- `xsd:integer` - Whole numbers
- `xsd:float` - Decimal numbers
- `xsd:boolean` - True/false
- `xsd:date` - Date (YYYY-MM-DD)
- `xsd:dateTime` - Date and time
- `xsd:time` - Time
- `xsd:anyURI` - URL or file reference

### Choice Options

```json
{
    "responseOptions": {
        "valueType": "xsd:integer",
        "choices": [
            {
                "name": "Option 1",
                "value": 1
            },
            {
                "name": "Option 2",
                "value": 2
            }
        ],
        "minValue": 1,
        "maxValue": 2
    }
}
```

### Numeric Range

```json
{
    "responseOptions": {
        "valueType": "xsd:integer",
        "minValue": 0,
        "maxValue": 10
    }
}
```

### String Constraints

```json
{
    "responseOptions": {
        "valueType": "xsd:string",
        "maxLength": 500
    }
}
```

## UI Configuration

### Order

```json
"ui": {
    "order": [
        "../items/item1/item1_schema",
        "../items/item2/item2_schema"
    ]
}
```

### Shuffle

```json
"ui": {
    "shuffle": true
}
```

### Add Properties

```json
"ui": {
    "addProperties": [
        {
            "isAbout": "../items/item1/item1_schema",
            "variableName": "item1",
            "prefLabel": "Item 1",
            "isVis": true,
            "requiredValue": true
        }
    ]
}
```

**Property Types:**

| Property | Type | Description |
|----------|------|-------------|
| `isAbout` | string | Reference to item schema |
| `variableName` | string | Variable name for export |
| `prefLabel` | string | Display label |
| `isVis` | boolean | Visibility |
| `requiredValue` | boolean | Is required |
| `defaultValue` | any | Default value |

## Conditional Logic

### Visibility

```json
{
    "ui": {
        "visibility": "parent_item == 1"
    }
}
```

### Branching

```json
{
    "ui": {
        "branching": {
            "item1": {
                "1": "activity2",
                "2": "activity3"
            }
        }
    }
}
```

## Validation Rules

### Pattern Matching

```json
{
    "validate": {
        "pattern": "^\\d{3}-\\d{2}-\\d{4}$"
    }
}
```

### Range Validation

```json
{
    "validate": {
        "minValue": 0,
        "maxValue": 100
    }
}
```

### Custom Validation

```json
{
    "validate": {
        "custom": "function(value) { return value.length > 5; }"
    }
}
```

## Computed Fields

```json
{
    "compute": {
        "total_score": {
            "valueType": "xsd:integer",
            "computeExpression": "sum([item1, item2, item3])"
        }
    }
}
```

## Ontology References

### isAbout

```json
{
    "isAbout": "http://purl.obolibrary.org/obo/PATO_0000461"
}
```

### About

```json
{
    "about": [
        {
            "@id": "http://purl.obolibrary.org/obo/PATO_0000461",
            "prefLabel": "Normal"
        }
    ]
}
```

## Provenance

### Created

```json
{
    "prov:wasGeneratedBy": {
        "@id": "my_activity_creation",
        "@type": "prov:Activity",
        "prov:startedAtTime": "2026-03-06T12:00:00Z",
        "prov:endedAtTime": "2026-03-06T13:00:00Z"
    }
}
```

### Derived From

```json
{
    "prov:wasDerivedFrom": {
        "@id": "original_activity_schema",
        "@type": "reproschema:Activity"
    }
}
```

## Validation

### Schema Validation

Schemas must validate against the ReproSchema LinkML model:

```bash
reproschema validate schema.jsonld
```

### Required Fields

Every schema must include:
- `@context`
- `@id`
- `@type`
- `prefLabel`

### URI Format

IDs should follow URI conventions:

```
protocol_id: "my_protocol"
activity_id: "activity1"
item_id: "item1"
```

## Best Practices

1. **Use descriptive IDs**: Make IDs self-documenting
2. **Include descriptions**: Provide context for each element
3. **Use ontologies**: Reference standard vocabularies where possible
4. **Validate frequently**: Check schemas during development
5. **Version control**: Track schema changes in git

## Resources

- [LinkML Schema](https://github.com/ReproNim/reproschema/blob/main/linkml-schema/reproschema.yaml)
- [JSON-LD Documentation](https://json-ld.org/)
- [Schema.org](https://schema.org/)
- [NIDM](https://nidm.nidash.org/)

## Next Steps

- [See field types reference](field-types.md)
- [Create your first protocol](../how-to/create-protocol.md)
- [Validate schemas](../how-to/validation.md)
