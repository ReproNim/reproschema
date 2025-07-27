# Core Concepts

Understanding the fundamental building blocks of ReproSchema.

## The ReproSchema Hierarchy

ReproSchema follows a three-level hierarchy that mirrors how research studies are organized:

```
Protocol
└── Activity
    └── Item
```

### Protocol

A **Protocol** represents your entire research study or assessment battery. It's the top-level container that:
- Defines the study's metadata (title, description, version)
- Lists all activities (questionnaires, tasks) in the study
- Controls the order and flow of activities
- Manages study-wide settings and permissions

Think of it as your study's blueprint.

### Activity

An **Activity** is a logical grouping of related questions or tasks. Common examples:
- A standardized questionnaire (PHQ-9, GAD-7)
- A demographic information form
- A cognitive task
- A custom assessment

Activities:
- Contain multiple items (questions)
- Can be reused across different protocols
- Have their own display logic and branching
- Can be imported from the reproschema-library

### Item

An **Item** is an individual question or data collection point. It defines:
- The question text and help text
- The response type (text, multiple choice, slider, etc.)
- Validation rules
- Scoring information

Items are the atomic units where actual data is collected.

## How They Work Together

1. **Composition**: A Protocol contains Activities, which contain Items
2. **Reusability**: Activities and Items can be shared across protocols
3. **Modularity**: Each level can be modified independently
4. **Flexibility**: Mix custom and library components at any level

## Schema Structure

Each level is defined by a JSON-LD schema file that specifies:

### Common Properties
- `@context`: Links to vocabulary definitions
- `@type`: The schema type (Protocol, Activity, or Item)
- `@id`: Unique identifier
- `prefLabel`: Display name
- `description`: Detailed description

### Level-Specific Properties

**Protocol**:
- `landingPage`: Welcome content
- `ui.order`: Activity sequence
- `ui.addProperties`: Activity configurations

**Activity**:
- `preamble`: Instructions
- `ui.order`: Item sequence
- `ui.addProperties`: Item configurations

**Item**:
- `question`: Question text
- `ui.inputType`: Response widget type
- `responseOptions`: Valid responses

## Design Philosophy

ReproSchema embraces several key principles:

1. **Semantic Clarity**: Every element has explicit meaning
2. **Reusability**: Build once, use many times
3. **Interoperability**: Works with other standards
4. **Version Control**: Track changes over time
5. **Validation**: Ensure data quality from the start

## Why This Structure?

This hierarchical approach provides:
- **Organization**: Natural grouping of related content
- **Flexibility**: Mix and match components
- **Standardization**: Consistent structure across studies
- **Efficiency**: Reuse existing validated instruments
- **Clarity**: Clear relationships between elements

Understanding these concepts is essential for effectively using ReproSchema to create robust, reusable research instruments.