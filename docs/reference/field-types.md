# Field Types Reference

Complete reference for all ReproSchema field types and their properties.

## Input Types

### Text Input

#### `text`
Single-line text input field.

```json
{
    "ui": {
        "inputType": "text"
    },
    "responseOptions": {
        "valueType": "xsd:string",
        "maxLength": 255
    }
}
```

#### `multitext`
Multi-line text input (textarea).

```json
{
    "ui": {
        "inputType": "multitext"
    },
    "responseOptions": {
        "valueType": "xsd:string",
        "maxLength": 5000,
        "rows": 5
    }
}
```

#### `email`
Email input with validation.

```json
{
    "ui": {
        "inputType": "email"
    },
    "responseOptions": {
        "valueType": "xsd:string",
        "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    }
}
```

### Numeric Input

#### `number`
Numeric input field.

```json
{
    "ui": {
        "inputType": "number"
    },
    "responseOptions": {
        "valueType": "xsd:integer",
        "minValue": 0,
        "maxValue": 100
    }
}
```

#### `float`
Decimal number input.

```json
{
    "ui": {
        "inputType": "float"
    },
    "responseOptions": {
        "valueType": "xsd:decimal",
        "minValue": 0.0,
        "maxValue": 100.0,
        "precision": 2
    }
}
```

### Selection Input

#### `radio`
Radio button selection (single choice).

```json
{
    "ui": {
        "inputType": "radio"
    },
    "responseOptions": {
        "valueType": "xsd:integer",
        "minValue": 0,
        "maxValue": 4,
        "multipleChoice": false,
        "choices": [
            {
                "value": 0,
                "name": "Never"
            },
            {
                "value": 1,
                "name": "Rarely"
            },
            {
                "value": 2,
                "name": "Sometimes"
            },
            {
                "value": 3,
                "name": "Often"
            },
            {
                "value": 4,
                "name": "Always"
            }
        ]
    }
}
```

#### `select`
Dropdown selection.

```json
{
    "ui": {
        "inputType": "select"
    },
    "responseOptions": {
        "valueType": "xsd:string",
        "multipleChoice": false,
        "choices": [
            {
                "value": "usa",
                "name": "United States"
            },
            {
                "value": "canada",
                "name": "Canada"
            },
            {
                "value": "other",
                "name": "Other"
            }
        ]
    }
}
```

#### `selectMultiple`
Multiple selection dropdown.

```json
{
    "ui": {
        "inputType": "select"
    },
    "responseOptions": {
        "valueType": "xsd:string",
        "multipleChoice": true,
        "choices": [
            {
                "value": "reading",
                "name": "Reading"
            },
            {
                "value": "sports",
                "name": "Sports"
            },
            {
                "value": "music",
                "name": "Music"
            }
        ]
    }
}
```

### Range Input

#### `slider`
Slider for numeric ranges.

```json
{
    "ui": {
        "inputType": "slider"
    },
    "responseOptions": {
        "valueType": "xsd:integer",
        "minValue": 0,
        "maxValue": 10,
        "step": 1,
        "minLabel": "No pain",
        "maxLabel": "Worst pain"
    }
}
```

### Date/Time Input

#### `date`
Date picker.

```json
{
    "ui": {
        "inputType": "date"
    },
    "responseOptions": {
        "valueType": "xsd:date",
        "minValue": "1900-01-01",
        "maxValue": "2024-12-31"
    }
}
```

#### `time`
Time picker.

```json
{
    "ui": {
        "inputType": "time"
    },
    "responseOptions": {
        "valueType": "xsd:time"
    }
}
```

#### `datetime`
Date and time picker.

```json
{
    "ui": {
        "inputType": "datetime"
    },
    "responseOptions": {
        "valueType": "xsd:dateTime"
    }
}
```

### Media Input

#### `audioRecord`
Audio recording input.

```json
{
    "ui": {
        "inputType": "audioRecord"
    },
    "responseOptions": {
        "valueType": "schema:AudioObject",
        "maxDuration": 300,
        "mediaType": "audio/wav"
    }
}
```

#### `audioPassage`
Audio playback with passage recording.

```json
{
    "ui": {
        "inputType": "audioPassage"
    },
    "responseOptions": {
        "valueType": "schema:AudioObject",
        "passages": [
            {
                "id": "rainbow_passage",
                "text": "When the sunlight strikes raindrops in the air...",
                "audio": "https://example.com/rainbow.mp3"
            }
        ]
    }
}
```

#### `image`
Image upload.

```json
{
    "ui": {
        "inputType": "image"
    },
    "responseOptions": {
        "valueType": "schema:ImageObject",
        "maxSize": 5242880,
        "acceptedFormats": ["image/jpeg", "image/png"]
    }
}
```

#### `video`
Video recording or upload.

```json
{
    "ui": {
        "inputType": "video"
    },
    "responseOptions": {
        "valueType": "schema:VideoObject",
        "maxDuration": 120,
        "maxSize": 104857600
    }
}
```

### Special Input Types

#### `static`
Display-only content (no user input).

```json
{
    "ui": {
        "inputType": "static"
    },
    "question": "Please read the following instructions carefully..."
}
```

#### `consent`
Consent checkbox with terms.

```json
{
    "ui": {
        "inputType": "consent"
    },
    "responseOptions": {
        "valueType": "xsd:boolean",
        "requiredValue": true
    }
}
```

#### `location`
Geographic location input.

```json
{
    "ui": {
        "inputType": "location"
    },
    "responseOptions": {
        "valueType": "schema:GeoCoordinates",
        "enableHighAccuracy": true
    }
}
```

## Response Options Properties

### Common Properties

| Property | Type | Description |
|----------|------|-------------|
| `valueType` | string | Data type of the response (xsd:string, xsd:integer, etc.) |
| `multipleChoice` | boolean | Allow multiple selections |
| `requiredValue` | boolean | Whether a response is required |
| `minValue` | varies | Minimum allowed value |
| `maxValue` | varies | Maximum allowed value |

### Text Properties

| Property | Type | Description |
|----------|------|-------------|
| `maxLength` | integer | Maximum character length |
| `pattern` | string | Regular expression for validation |
| `placeholder` | string | Placeholder text |

### Numeric Properties

| Property | Type | Description |
|----------|------|-------------|
| `step` | number | Increment step for numeric inputs |
| `precision` | integer | Decimal places for float values |
| `unitCode` | string | Unit of measurement (kg, cm, etc.) |

### Choice Properties

| Property | Type | Description |
|----------|------|-------------|
| `choices` | array | Array of choice objects |
| `choice.value` | varies | Stored value |
| `choice.name` | string/object | Display label (can be multilingual) |
| `choice.image` | string | URL to choice image |

### Media Properties

| Property | Type | Description |
|----------|------|-------------|
| `maxDuration` | integer | Maximum duration in seconds |
| `maxSize` | integer | Maximum file size in bytes |
| `mediaType` | string | MIME type |
| `acceptedFormats` | array | Array of accepted MIME types |

## Validation Rules

### Required Fields

```json
{
    "responseOptions": {
        "requiredValue": true
    }
}
```

### Conditional Requirements

```json
{
    "responseOptions": {
        "requiredValue": "age >= 18"
    }
}
```

### Custom Validation

```json
{
    "responseOptions": {
        "valueType": "xsd:string",
        "pattern": "^[A-Z]{2}\\d{6}$",
        "invalidMessage": "Please enter a valid ID (e.g., AB123456)"
    }
}
```

## Multilingual Support

### Multilingual Labels

```json
{
    "choices": [
        {
            "value": 1,
            "name": {
                "en": "Yes",
                "es": "Sí",
                "fr": "Oui"
            }
        },
        {
            "value": 0,
            "name": {
                "en": "No",
                "es": "No",
                "fr": "Non"
            }
        }
    ]
}
```

## Advanced Features

### Dynamic Value Constraints

```json
{
    "responseOptions": {
        "valueType": "xsd:integer",
        "minValue": 0,
        "maxValue": "age_at_enrollment"
    }
}
```

### Computed Values

```json
{
    "ui": {
        "inputType": "number",
        "readOnly": true
    },
    "compute": [
        {
            "variableName": "bmi",
            "jsExpression": "weight / (height * height)"
        }
    ]
}
```

## Best Practices

1. **Choose Appropriate Types**: Use the most specific input type for better UX
2. **Set Constraints**: Always define min/max values for numeric inputs
3. **Provide Help Text**: Use `description` field for instructions
4. **Consider Mobile**: Some input types work better on mobile devices
5. **Validate Early**: Use appropriate validation patterns
6. **Internationalize**: Provide translations for all user-facing text

## See Also

- [Schema Specification](schema-spec.md)
- [Create Items Tutorial](../tutorials/create-new-items.md)
- [Validation Guide](../how-to/validation.md)