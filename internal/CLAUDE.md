# reproschema - Documentation

## Inherits From
→ Parent: ../../internal/CLAUDE.md (all shared practices apply)

## Repository Purpose
Core ReproSchema specifications, contexts, and schema definitions

## Local Overrides
- **Versioning**: Strict semver (parent: flexible) - Breaking changes affect all downstream
- **Review**: 2 maintainers required (parent: 1) - Core schemas need extra scrutiny
- **Docs**: Must update specs (parent: optional) - Reference implementation

## Tech Stack
- Format: JSON-LD schemas
- Validation: JSON Schema
- Tools: reproschema-py for validation
- Docs: Markdown + Diátaxis framework

## Key Commands
```bash
# Validate schemas
reproschema -l DEBUG validate <path>

# Check all schemas
find . -name "*.jsonld" -exec reproschema validate {} \;
```

## Dependencies
- **Depends on**: None (root of ecosystem)
- **Used by**: All reproschema-* repositories
- **External**: JSON-LD, JSON Schema specs

## Current Focus
- Active: Documentation reorganization (Diátaxis)
- Next: Schema v2.0 planning
- Blocked: None

## Recent Changes (Last 5)
- 2025-01-29: Doc reorganization plan → ./changes/2025-01-doc-reorg.md
- 2025-01-28: Added new context → ./changes/2025-01-context.md

## Local Patterns
- Schema design → ./patterns/schema-design.md
- Context management → ./patterns/context-usage.md
- Version migration → ./patterns/version-migration.md

## Quick Links
- Specs: /docs/specifications/
- Examples: /examples/
- Contexts: /contexts/
- Terms: /terms/

---
*Line count: ~55 (target: < 100)*