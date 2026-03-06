# Create a Protocol from Scratch

Create a ReproSchema protocol manually for full control over the structure.

## Goal

Create a custom protocol with your specific requirements without using templates.

## Prerequisites

- Text editor
- Basic understanding of JSON
- Terminal/command line access

## Steps

### 1. Create Directory Structure

```bash
# Create main directory
mkdir my_protocol
cd my_protocol

# Create subdirectories
mkdir protocols
mkdir activities
```

### 2. Create Protocol Schema

Create `protocols/my_protocol_schema.jsonld`:

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    "@type": "reproschema:Protocol",
    "@id": "my_protocol_schema",
    "prefLabel": "My Research Protocol",
    "description": "Description of your research protocol",
    "landingPage": {
        "@id": "README.md",
        "@language": "en"
    },
    "ui": {
        "order": [
            "../activities/activity1/activity1_schema"
        ],
        "shuffle": false,
        "addProperties": [
            {
                "isAbout": "../activities/activity1/activity1_schema",
                "variableName": "activity1",
                "prefLabel": "First Activity"
            }
        ]
    }
}
```

### 3. Add Activities

For each activity in your protocol:
1. Create a directory: `mkdir activities/activity_name`
2. Create the activity schema file
3. Add it to the protocol's `ui.order` and `ui.addProperties`

### 4. Validate Your Protocol

```bash
reproschema -l DEBUG validate protocols/my_protocol_schema.jsonld
```

## Troubleshooting

- **Validation errors**: Check JSON syntax and required fields
- **Activities not showing**: Verify paths in `ui.order`
- **Wrong display order**: Check the sequence in `ui.order` array

## Next Steps

- [Add activities to your protocol](create-activity.md)
- [Visualize your protocol](visualize.md)
- [Deploy your protocol](deploy-protocol.md)