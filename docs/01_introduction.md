# Introduction

??? example "Tl;DR - Advantages of the current schema representation" 
    - Rich contexts for a questionnaire with JSON-LD rather than a "flat" csv file. 
    - A single source of curated assessments from [ReproNim](https://github.com/ReproNim) 
    - Each `item` (i.e question), `activity` (i.e questionnaire), and `protocol`
    (i.e set of questionnaires) provides unique and persistent identifiers. 
    - Versions of a given questionnaire can be tracked (e.g., PHQ-9, PHQ-8). 
    - Allows, supports, and tracks internationalization (e.g. ABCD requires Spanish
    and English forms). 
    - Implementation agnostic – the schema can be used by several software 
    - Still a linked data graph that can be validated using [SHACL](https://www.w3.org/TR/shacl/).

## The problem

Cognitive and clinical questionnaires and assessments are used throughout neuroscience. Despite many efforts
([Cognitive Atlas](https://www.cognitiveatlas.org/), [Cognitive Paradigm Ontology](http://www.cogpo.org/), [OOve](???)...)
there is little consistency in assessment data acquisition or response representation across studies or laboratories. Each
project tends to use its own format and data collection tool (paper, form, ...). In the long run, this can the source of a
lot inefficiencies not only in terms data curation but also by diminishing the value of the data less inter-operable and reusable.
Imagine for example a researcher wanting to run a meta or mega-analysis across several studies, but having no way to find out
which version of a questionnaire was used or how exactly it was scored.

This highlights the need for harmonization across projects. For example, the National institute for mental health (NIMH)
Data Archive (NDA) enforces harmonization during data submission. However, harmonizing data after acquisition is resource
intensive and this approach can create a mismatch between collected and submitted data due to human error during the
harmonization process. Another possibility would be to reverse engineer the data dictionaries to their original assessments:
this would mean figuring out the information describing the content, format, and structure of the questionnaire from the
data contained in the questionnaires themselves. This approach is potentially feasible using a tool like [Brainverse](???), but
it can be very tedious.

## Goals and general description

A simpler solution is to enforce consistency directly at the data acquisition stage by relying on a `schema` that encodes 
how the different elements of the data and / or the metadata relate to one another. This way, all this relational 
information between these elements is captured from the very start as it is already embedded in the formal description 
of the assessment.

This is the goal of the Reproschema project that covers:

1. a schema that can be found [in the present repository](???) that describes the content and relations of the different 
2. elements of a questionnaire or set of assessment tools,
3. an [associated curated library of reusable common assessments and questionnaires](???),
4. a [python package](???) to help create and validate the schemas of new assessments,
5. a [user interface](???) to visualize questionnaire and collect data.

In brief, Reproschema offers a way to standardize the underlying representation of assessment tools. It comes with an open 
and accessible library of questionnaire with appropriate conversion (e.g., to RedCap) and data collection 
tools (e.g., [MindLogger](https://mindlogger.org/), LORIS, RedCap) to enable a more consistent acquisition across projects, 
with results being harmonized by design.

## General description

With this schema we can represent:

- at the `item` level, the elements of an individual assessment, like the questions in a questionnaire
- at the `activity` level, an individual assessment that contains a set of `items`, like for example a whole questionnaire
  with a several questions.
- at the `protocols` level, a collection of `activities` performed by a participant, e.g a set of questionnaires used in 
  a study.

All those elements are specified text files in a `JSON-LD` format (JavaScript Object Notation for Linked Data) and each 
`item`, `activity`, and `protocol` provides unique and persistent identifiers.

Below we show an example of how the questionnaire with 3 question for a study could be organized with a `protocol` for 
that study, one `activity` and 3 `items`.

```json
├── activities
│   ├── activity1.jsonld
│   └── items
│       ├── item1.jsonld
│       ├── item2.jsonld
│       └── item3.jsonld
└── protocols
    └── protocol1.jsonld
```

The Reproschema can also easily and flexibly specify details about how the schema for an assessment should be implemented. 
Independently of what solution is chosen in the end by a researcher, a lab, or an institute to display the assessment to 
their participants or patients (for example whether using an web-app written in javascript or a mobile app written in 
python), the schema can already specify:

- the `input type` to choose among several user-interface rendering options e.g if an item should be displayed as a 
  Likert scale, a dropdown menu, a multiple choice...
- the `visibility` to decide whether a given `item` or `activity` should be displayed to the user and under which conditions,
- the `scoring logic` of how the total score to the responses on a questionnaire should be computed

The Reproschema also allows for internationalization and multiple languages support by making it very easy to keep everything 
the same about a questionnaire and only specify which language should be displayed by the user interface.

Finally Reproschema allows tracking of variations and version of different assessments tools (e.g., PHQ-9, PHQ-8).