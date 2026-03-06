# Create an Activity

Create an activity to group related items together.

## Goal

Organize related questions into a cohesive activity within your protocol.

## Prerequisites

- Basic understanding of JSON
- Read [Create a Protocol](create-protocol.md)

## Steps

### 1. Create Activity Directory

```bash
mkdir -p activities/my_activity
cd activities/my_activity
```

### 2. Create Activity Schema

Create `my_activity_schema.jsonld`:

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    "@type": "reproschema:Activity",
    "@id": "my_activity",
    "prefLabel": "My Activity",
    "description": "Description of this activity",
    "ui": {
        "order": [
            "../items/my_item1/my_item1_schema"
        ],
        "shuffle": false
    }
}
```

### 3. Add Items

Create individual item schemas in the `items/` subdirectory:

```bash
mkdir -p items/my_item1
```

Create `items/my_item1/my_item1_schema.jsonld`:

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    "@type": "reproschema:Item",
    "@id": "my_item1",
    "prefLabel": "Question 1",
    "description": "Description of this question",
    "question": "What is your answer?",
    "responseOptions": {
        "choices": [
            {
                "name": "yes",
                "value": 1
            },
            {
                "name": "no",
                "value": 0
            }
        ],
        "minValue": 0,
        "maxValue": 1
    }
}
```

### 4. Add More Items

Repeat step 3 for each question in your activity.

### 5. Link to Protocol

Update your protocol schema to include the activity:

```json
"ui": {
    "order": [
        "../activities/my_activity/my_activity_schema"
    ]
}
```

## Best Practices

- Group related questions logically
- Keep activities focused on one topic
- Use descriptive names for activities
- Test validation after each step

## Next Steps

- [Visualize your activity](visualize.md)
- [Add library assessments](use-library-assessments.md)
