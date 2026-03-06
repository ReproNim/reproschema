# Add Items to an Activity

Add individual questions to your ReproSchema activity.

## Goal

Create custom questions with appropriate response options for your assessment.

## Prerequisites

- Existing activity structure
- Read [Create an Activity](create-activity.md)

## Steps

### 1. Create Item Directory

```bash
cd activities/my_activity
mkdir -p items/my_new_item
cd items/my_new_item
```

### 2. Create Item Schema

Create `my_new_item_schema.jsonld`:

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    "@type": "reproschema:Item",
    "@id": "my_new_item",
    "prefLabel": "Question Label",
    "description": "Detailed description if needed",
    "question": "What is your answer?",
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
            },
            {
                "name": "Option 3",
                "value": 3
            }
        ],
        "minValue": 1,
        "maxValue": 3
    }
}
```

### 3. Response Option Types

#### Multiple Choice
```json
"responseOptions": {
    "valueType": "xsd:integer",
    "choices": [
        {"name": "Yes", "value": 1},
        {"name": "No", "value": 0}
    ],
    "minValue": 0,
    "maxValue": 1
}
```

#### Numeric Input
```json
"responseOptions": {
    "valueType": "xsd:integer",
    "minValue": 0,
    "maxValue": 10
}
```

#### Text Input
```json
"responseOptions": {
    "valueType": "xsd:string",
    "maxLength": 500
}
```

#### Date Input
```json
"responseOptions": {
    "valueType": "xsd:date"
}
```

### 4. Add to Activity Order

Update your activity's `ui.order`:

```json
"ui": {
    "order": [
        "../items/item1/item1_schema",
        "../items/my_new_item/my_new_item_schema",
        "../items/item3/item3_schema"
    ]
}
```

### 5. Add to Activity Properties

Update `ui.addProperties` in your activity:

```json
"addProperties": [
    {
        "isAbout": "../items/my_new_item/my_new_item_schema",
        "variableName": "my_new_item",
        "prefLabel": "My New Question",
        "isVis": true,
        "requiredValue": true
    }
]
```

## Advanced Options

### Conditional Logic
```json
"pilot": {
    "question": "If yes, describe:",
    "visibility": "parent_item1 == 1"
}
```

### Custom Validation
```json
"validate": {
    "pattern": "^\\d{3}-\\d{2}-\\d{4}$"
}
```

### Branching
```json
"branching": {
    "item1": {
        "1": "activity2",
        "2": "activity3"
    }
}
```

## Best Practices

- Use clear, concise questions
- Keep response options balanced
- Test validation rules thoroughly
- Use descriptive variable names
- Consider accessibility and localization

## Next Steps

- [Visualize your items](visualize.md)
- [Validate your schema](validation.md)
