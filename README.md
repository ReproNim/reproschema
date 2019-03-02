## Schema Standardization - An effort to work towards a set of reusable schemas for common assessments across projects

We are building out the standard by extending and modifying the Center for Expanded Data Annotation and Retrieval ([CEDAR](https://github.com/metadatacenter)) metadata representation. CEDAR uses JSON-LD to represent their templates, which we are continuing to use. For instruments and assessments, we are adding the ability to specify scoring logic and branching logic. This will be one of the richest repositories of form information publicly available.

### Highlights:
* Cleaner JSON-LD representation to represent:
  * __Activity Sets__: Collections of activities performed by a participant
  * __Activity__: Individual assessments
  * __Items__: Elements of individual assessments
* Advantages of current representation
  * Rich contexts with JSON-LD
  * Single source of curated assessments from [ReproNim](https://github.com/ReproNim)
  * Each Item, Activity, and Activity Set provide unique and persistent identifiers
  * Variations can be tracked (e.g., PHQ-9, PHQ-8)
  * Allows, supports, and tracks internationalization
  * Implementation agnostic - schema can be used by several software
  * Still a linked data graph and can be validated using [SHACL](https://www.w3.org/TR/shacl/)

