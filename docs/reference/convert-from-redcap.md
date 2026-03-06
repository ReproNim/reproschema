# Convert from REDCap

Migrate REDCap instruments to ReproSchema format.

## Goal

Convert existing REDCap data collection instruments to ReproSchema schemas.

## Prerequisites

- REDCap project with exported instruments
- Python 3.8+
- Basic understanding of REDCap structure

## Methods

### Method 1: Using hbcd-redcap2rs (Recommended)

For HBCD projects, use the specialized converter:

```bash
# Clone the converter
git clone https://github.com/ReproNim/hbcd-redcap2rs.git
cd hbcd-redcap2rs

# Install dependencies
pip install -r requirements.txt

# Convert REDCap data dictionary
python redcap_to_reproschema.py \
  --input data_dictionary.csv \
  --output output_dir \
  --protocol-name "My Protocol"
```

### Method 2: Using reproschema-py

```python
from reproschema import Activity, Item, Protocol
import pandas as pd

# Load REDCap data dictionary
df = pd.read_csv('data_dictionary.csv')

# Create protocol
protocol = Protocol(
    prefLabel="My Protocol",
    description="Converted from REDCap"
)

# Iterate through REDCap fields
for _, row in df.iterrows():
    field_name = row['field_name']
    field_label = row['field_label']
    field_type = row['field_type']
    choices = row.get('select_choices_or_calculations', '')

    # Create item
    item = Item(
        prefLabel=field_label,
        question=field_label,
        variableName=field_name
    )

    # Map REDCap field types to ReproSchema
    if field_type == 'dropdown':
        # Parse choices
        choice_list = parse_redcap_choices(choices)
        item.responseOptions = {
            'choices': choice_list,
            'valueType': 'xsd:integer'
        }
    elif field_type == 'text':
        item.responseOptions = {
            'valueType': 'xsd:string',
            'maxLength': row.get('text_validation_max', '')
        }
    elif field_type == 'yesno':
        item.responseOptions = {
            'choices': [
                {'name': 'Yes', 'value': 1},
                {'name': 'No', 'value': 0}
            ],
            'valueType': 'xsd:integer'
        }

    # Add to activity (group related fields)
    activity.add_item(item)

# Save schemas
protocol.write('protocol.jsonld')
```

### Method 3: Manual Conversion

#### REDCap Field Type Mapping

| REDCap Type | ReproSchema Type | Example |
|-------------|------------------|---------|
| text | string | `"valueType": "xsd:string"` |
| dropdown | choices | `"choices": [...]` |
| radio | choices | `"choices": [...]` |
| checkbox | choices (multiple) | `"multipleChoice": true` |
| yesno | binary choices | `"choices": [{"name": "Yes", "value": 1}, {"name": "No", "value": 0}]` |
| truefalse | boolean | `"valueType": "xsd:boolean"` |
| number | integer/float | `"valueType": "xsd:integer"` |
| date | date | `"valueType": "xsd:date"` |
| datetime | datetime | `"valueType": "xsd:dateTime"` |
| notes | long string | `"valueType": "xsd:string", "maxLength": 5000` |
| file | file | `"valueType": "xsd:anyURI"` |

#### Example Conversion

**REDCap Data Dictionary:**
```csv
field_name,field_label,field_type,select_choices_or_calculations
phq9_1,PHQ-9 Question 1,radio,1, Little interest|2, Not at all
phq9_2,PHQ-9 Question 2,radio,1, Feeling down|2, Not at all
```

**ReproSchema Item:**
```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    "@type": "reproschema:Item",
    "@id": "phq9_1",
    "prefLabel": "PHQ-9 Question 1",
    "question": "Little interest or pleasure in doing things?",
    "responseOptions": {
        "choices": [
            {
                "name": "Not at all",
                "value": 0
            },
            {
                "name": "Several days",
                "value": 1
            },
            {
                "name": "More than half the days",
                "value": 2
            },
            {
                "name": "Nearly every day",
                "value": 3
            }
        ],
        "valueType": "xsd:integer",
        "minValue": 0,
        "maxValue": 3
    }
}
```

## Advanced Conversion

### Handling REDCap Logic

#### Branching Logic
```python
# REDCap branching logic: [q1] = 1
# ReproSchema equivalent:
item = Item(
    prefLabel="Follow-up Question",
    question="If yes, provide details",
    visibility="q1 == 1"
)
```

#### Calculated Fields
```python
# REDCap calculation: ([q1] + [q2]) / 2
# ReproSchema equivalent (post-processing):
# Calculate after data collection
```

### Validation Rules

```python
# REDCap validation: date_YYYY-MM-DD
item.responseOptions = {
    "valueType": "xsd:date",
    "validation": {
        "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    }
}
```

### Skip Patterns

```python
# REDCap: Show field Q2 only if Q1 = 1
item2 = Item(
    prefLabel="Q2",
    visibility="Q1 == 1"
)
```

## Data Migration

### Export REDCap Data

```python
import pandas as pd

# Export from REDCap API or UI
df = pd.read_csv('redcap_export.csv')

# Convert to ReproSchema format
reproschema_data = []

for _, row in df.iterrows():
    response = {
        "participant_id": row['record_id'],
        "item_id": row['field_name'],
        "response": row.get('value'),
        "timestamp": row.get('redcap_event_name')
    }
    reproschema_data.append(response)

# Save as JSON
import json
with open('responses.json', 'w') as f:
    json.dump(reproschema_data, f, indent=2)
```

## Quality Assurance

### Validation Checklist

- [ ] All fields converted
- [ ] Choice values mapped correctly
- [ ] Branching logic preserved
- [ ] Validation rules implemented
- [ ] Labels and descriptions match
- [ ] Data types appropriate
- [ ] Required fields marked

### Testing

```bash
# Validate converted schemas
reproschema validate protocol.jsonld
reproschema validate activities/*/*.jsonld

# Test with sample data
reproschema test protocol.jsonld --data sample_responses.json
```

## Best Practices

1. **Backup REDCap data**: Export before conversion
2. **Test incrementally**: Convert one form at a time
3. **Validate thoroughly**: Check each conversion step
4. **Document mappings**: Keep a log of field mappings
5. **Preserve metadata**: Include original REDCap IDs

## Troubleshooting

### Choice parsing issues
- Check REDCap choice format
- Verify separator (| vs comma)
- Test with sample data

### Branching logic not working
- Check field references
- Verify syntax
- Test with test data

### Data type mismatches
- Review REDCap field types
- Map to appropriate ReproSchema type
- Validate sample data

## Resources

- [hbcd-redcap2rs](https://github.com/ReproNim/hbcd-redcap2rs)
- [REDCap API Documentation](https://projectredcap.org/api/)
- [REDCap Data Dictionary](https://projectredcap.org/)

## Next Steps

- [Validate converted schemas](../how-to/validation.md)
- [Test with sample data](../how-to/visualize.md)
- [Deploy converted protocol](../how-to/deploy-protocol.md)
