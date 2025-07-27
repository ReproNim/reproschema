# Use Assessments from the Library

Integrate pre-built assessments from the reproschema-library into your protocol.

## Goal

Add standardized questionnaires (PHQ-9, GAD-7, etc.) to your protocol without recreating them.

## Prerequisites

- Existing protocol structure
- Access to [reproschema-library](https://github.com/ReproNim/reproschema-library)

## Steps

### 1. Browse Available Assessments

View available assessments at: https://github.com/ReproNim/reproschema-library/tree/master/activities

Common assessments include:
- PHQ-9 (Depression)
- GAD-7 (Anxiety)
- Demographics
- BADS (Behavioral Activation)

### 2. Add Library Context

In your activity schema, add the library context:

```json
{
    "@context": [
        "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
        {
            "rl": "https://raw.githubusercontent.com/ReproNim/reproschema-library/master/activities/"
        }
    ]
}
```

### 3. Reference Library Items

In your activity's `addProperties`, reference library items:

```json
"addProperties": [
    {
        "isAbout": "rl:PHQ-9/items/phq9_1",
        "variableName": "phq9_1", 
        "prefLabel": "Little interest or pleasure",
        "isVis": true
    }
]
```

### 4. Add to UI Order

```json
"order": [
    "rl:PHQ-9/items/phq9_1",
    "rl:PHQ-9/items/phq9_2"
]
```

## Example: Complete PHQ-9 Integration

```json
{
    "@context": [
        "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
        {
            "rl": "https://raw.githubusercontent.com/ReproNim/reproschema-library/master/activities/"
        }
    ],
    "@type": "reproschema:Activity",
    "@id": "depression_assessment",
    "prefLabel": "Depression Assessment",
    "ui": {
        "order": [
            "rl:PHQ-9/PHQ9_schema"
        ],
        "addProperties": [
            {
                "isAbout": "rl:PHQ-9/PHQ9_schema",
                "variableName": "phq9",
                "prefLabel": "PHQ-9 Depression Scale"
            }
        ]
    }
}
```

## Tips

- Use complete assessments by referencing the activity schema
- Mix library items with custom items
- Override labels and descriptions as needed

## Next Steps

- [Create custom items](add-items.md)
- [Combine multiple assessments](create-activity.md)