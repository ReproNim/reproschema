# ReproSchema Documentation Reorganization Proposal

## Problem Statement

The current documentation has:
- **Duplication**: "create-new-protocol" exists in both tutorials/ and user-guide/
- **Unclear distinctions**: What's the difference between tutorials and user-guide?
- **Mixed content types**: Conceptual explanations mixed with step-by-step guides
- **Navigation issues**: Users don't know where to find what they need

## Proposed Solution: Diátaxis Framework

Reorganize documentation into four clear categories:

### 1. **Tutorials** (Learning-Oriented)
*"I want to learn ReproSchema step-by-step"*
- Complete walkthroughs from start to finish
- Build understanding progressively
- End with a working example

### 2. **How-To Guides** (Task-Oriented)
*"I need to accomplish a specific task"*
- Direct solutions to specific problems
- Assume basic knowledge
- Focus on getting things done

### 3. **Explanation** (Understanding-Oriented)
*"I want to understand the concepts"*
- Why things work the way they do
- Background and context
- Design decisions and trade-offs

### 4. **Reference** (Information-Oriented)
*"I need to look up specific details"*
- Complete technical specifications
- API documentation
- Comprehensive field/property listings

## New Structure

```
docs/
├── tutorials/               # Complete learning exercises
│   ├── getting-started      # First steps & setup
│   ├── first-protocol       # Build a complete protocol
│   ├── first-activity       # Create an activity from scratch
│   └── protocol-with-library # Use existing assessments
│
├── how-to/                  # Quick task solutions
│   ├── create-protocol      # Quick protocol creation
│   ├── validate-schema      # Run validation
│   ├── translate-content    # Add translations
│   ├── visualize-ui         # Preview in UI
│   └── deploy-protocol      # Deploy to production
│
├── explanation/             # Conceptual understanding
│   ├── core-concepts        # Protocols, Activities, Items
│   ├── json-ld-basics       # Why JSON-LD?
│   ├── schema-structure     # Architecture overview
│   └── best-practices       # Design patterns
│
└── reference/               # Technical specifications
    ├── schema-spec          # Complete schema reference
    ├── api-reference        # Python API docs
    ├── cli-reference        # Command-line tools
    └── field-types          # All fields & properties
```

## Key Benefits

1. **Clear Purpose**: Each section has a distinct goal
2. **No Duplication**: One canonical location for each topic
3. **Better Navigation**: Users know where to look
4. **Progressive Learning**: Clear path from beginner to advanced
5. **Maintainable**: Easier to keep updated

## Migration Plan

### Phase 1: Structure & Navigation
- Create new directory structure
- Add index pages for each section
- Set up navigation in mkdocs.yml

### Phase 2: Content Migration
- Move existing content to appropriate sections
- Eliminate duplication
- Update cross-references

### Phase 3: Fill Gaps
- Write missing how-to guides
- Add conceptual explanations
- Complete reference documentation

### Phase 4: Polish
- Add examples and diagrams
- Improve search and navigation
- Test user journeys

## Example User Journeys

**New User:**
1. Read Introduction
2. Follow Tutorial: Getting Started
3. Complete Tutorial: First Protocol
4. Use How-To guides for specific tasks

**Experienced Developer:**
1. Jump to How-To for specific task
2. Check Reference for field details
3. Read Explanation for advanced concepts

**Evaluating ReproSchema:**
1. Read Introduction
2. Review Explanation: Core Concepts
3. Try Tutorial: Getting Started

## Next Steps

1. Review and approve this proposal
2. Create new directory structure
3. Begin content migration
4. Write new content to fill gaps

This reorganization will make ReproSchema documentation more accessible, reduce confusion, and provide clear paths for all user types.