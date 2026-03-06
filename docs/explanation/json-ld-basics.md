# JSON-LD in ReproSchema

Understanding why ReproSchema uses JSON-LD and how it enhances data interoperability.

## What is JSON-LD?

JSON-LD (JSON for Linked Data) is JSON with superpowers. It looks like regular JSON but includes semantic meaning that machines can understand.

### Regular JSON vs JSON-LD

**Regular JSON:**
```json
{
    "name": "PHQ-9",
    "type": "questionnaire",
    "questions": 9
}
```

**JSON-LD:**
```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    "@type": "reproschema:Activity",
    "@id": "PHQ-9_schema",
    "prefLabel": "PHQ-9",
    "description": "Patient Health Questionnaire - 9 items"
}
```

## Why JSON-LD?

### 1. Semantic Clarity

The `@context` tells machines exactly what each term means:
- `prefLabel` isn't just a random property name
- It maps to a standardized definition
- Different systems can understand it consistently

### 2. Interoperability

JSON-LD enables:
- Integration with other semantic web standards
- Automatic conversion between formats
- Linking to external vocabularies (schema.org, NIDM)

### 3. Self-Documenting

Each schema carries its own semantic information:
- No need for external documentation to understand structure
- Properties have standardized meanings
- Relationships are explicit

## Key JSON-LD Features in ReproSchema

### @context

Defines the vocabulary and term mappings:

```json
"@context": [
    "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    {
        "rl": "https://raw.githubusercontent.com/ReproNim/reproschema-library/master/activities/"
    }
]
```

This allows:
- Using ReproSchema vocabulary
- Creating shortcuts (like `rl:` for library references)
- Mixing vocabularies

### @type

Specifies what kind of thing this is:

```json
"@type": "reproschema:Protocol"  // This is a Protocol
"@type": "reproschema:Activity"  // This is an Activity
"@type": "reproschema:Field"     // This is an Item/Field
```

### @id

Provides a unique identifier:

```json
"@id": "depression_study_schema"
```

This enables:
- Referencing from other schemas
- Creating persistent links
- Version tracking

## Practical Benefits

### 1. Automatic Validation

Because terms have defined meanings, we can:
- Validate structure automatically
- Catch errors early
- Ensure consistency

### 2. Enhanced Tooling

JSON-LD enables tools to:
- Generate documentation automatically
- Convert between formats
- Create visualizations
- Build user interfaces

### 3. Future-Proofing

As standards evolve:
- New properties can be added without breaking existing schemas
- Vocabularies can be extended
- Backwards compatibility is maintained

## Working with JSON-LD

### Context Shortcuts

Create readable shortcuts:

```json
"@context": {
    "nidm": "http://purl.org/nidash/nidm#",
    "schema": "http://schema.org/"
}
```

Then use them:
```json
"nidm:hasAge": 25,
"schema:author": "Researcher Name"
```

### Referencing Other Schemas

Link to activities or items:

```json
"ui": {
    "order": [
        "../activities/phq9/phq9_schema",
        "rl:GAD-7/GAD7_schema"
    ]
}
```

### Language Support

Specify multiple languages:

```json
"prefLabel": {
    "en": "Depression Questionnaire",
    "es": "Cuestionario de Depresión",
    "fr": "Questionnaire de Dépression"
}
```

## Common Patterns

### 1. Activity References

```json
"isAbout": "../activities/demographics/demographics_schema"
```

### 2. Conditional Display

```json
"isVis": "age > 18"
```

### 3. Response Bindings

```json
"valueRequired": true
```

## Best Practices

1. **Always include @context** - It's required for JSON-LD
2. **Use standard properties** - Don't create custom properties when standard ones exist
3. **Reference, don't duplicate** - Link to existing schemas
4. **Version your contexts** - Include version numbers in context URLs

## Debugging Tips

When schemas don't work as expected:

1. **Validate the JSON-LD** - Use online validators
2. **Check context URLs** - Ensure they're accessible
3. **Verify @type values** - Must match vocabulary definitions
4. **Test references** - Ensure all paths resolve correctly

Understanding JSON-LD is key to leveraging ReproSchema's full power for creating interoperable, semantic research instruments.