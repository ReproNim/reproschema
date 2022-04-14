# Introduction

??? example "Tl;DR - Advantages of the current schema representation"
    - Rich contexts for a questionnaire with JSON-LD rather than a "flat" csv file.
    - A single source of curated assessments from [ReproSchema Library](https://github.com/reproschema-library)
    - Each `item` (i.e question), `activity` (i.e questionnaire), and `protocol`
    (i.e set of questionnaires) provides unique and persistent identifiers.
    - Versions of a given questionnaire can be tracked (e.g., PHQ-9, PHQ-8).
    - Allows, supports, and tracks internationalization (e.g. ABCD requires Spanish
    and English forms).
    - Implementation agnostic – the schema can be used by several software
    - Uses a linked data graph that can be validated using [SHACL](https://www.w3.org/TR/shacl/).

## The problem

Cognitive and clinical questionnaires and assessments are used throughout
neuroscience. There is little consistency in assessment data acquisition or response
representation across studies or laboratories. Each project tends to use its own
format and data collection tool (e.g., paper, survey tools, RedCap, LORIS). In the
long run, this can be a source of a lot inefficiencies not only in terms data
curation but also by diminishing the value of the data less interoperable and
reusable. Imagine for example a researcher wanting to run a meta or mega-analysis
across several studies. To do this each one would not only need to know which
specific assessments were collected, but also how to relate different column names in
data spreadsheets to these assessments and across projects.

Several efforts have focused on linking the assessments themselves
through consistent terminologies and relationships that map to human cognition
(e.g., [Cognitive Atlas](https://www.cognitiveatlas.org/),
[Cognitive Paradigm Ontology](http://www.cogpo.org/)). Other efforts such as the
National Institute for Mental Health (NIMH) Data Archive (NDA) and the National
Library of Medicine (NLM) [Common Data Elements](https://www.nlm.nih.gov/cde/index.html)
have curated data elements corresponding to the items and calculated scores from
these questionnaires. However, these resources are often used to make data
consistent and reusable after, rather than during data collection. However,
harmonizing data after acquisition is resource intensive and this approach can
create a mismatch between collected and submitted data due to human error during
the harmonization process. To faciliate tedious harmonization efforts, several
projects, over the last two decades, have developed technologies to automatically
or interactively align and harmonize data elements (e.g., BIRN mediator, OpenRefine).

Given the dynamic and evolving nature of scientific investigation, many
questionnaires are altered when used to suit the requirements of a particular
study (e.g., different language, selective and new questions). This information
linking the specific information used when asking a question is often decoupled
from the data element representing the response to the question. When questions
are changed, researchers often shoehorn the response into an existing data
element, thus creating additional noise. Another drawback to these data elements
is that there is often no way to find out which version of a questionnaire was
used or how exactly it was scored.

## Our solution

Our simpler solution is to enforce consistency directly at the data acquisition
stage by relying on a common `schema` that encodes how the different elements of
the data and / or the metadata relate to one another. This way, all this relational
information between these elements is captured from the very start as it is already
embedded in the formal description of the assessment. This solution was inspired
by the work of [CEDAR Metadata Model](https://more.metadatacenter.org/tools-training/outreach/cedar-template-model).

In this project we provide a comprehensive set of tools to create and use the
schemas, while tracking the source of the schema, and changes to it over time.
The Reproschema project covers:

1. a schema that can be found [in the present repository](https://github.com/ReproNim/reproschema)
that describes the content and relations of the different elements of a
questionnaire or set of assessment tools,
2. an [associated curated library of reusable common assessments and questionnaires](https://github.com/ReproNim/reproschema-library),
3. a [python package](https://github.com/ReproNim/reproschema-py) to help create
and validate the schemas of new assessments,
4. a [user interface](https://github.com/ReproNim/reproschema-ui) to visualize
questionnaire and collect data locally,
5. a [backend server](https://github.com/sensein/voice-backend) to capture the
data remotely.

In brief, Reproschema offers a way to standardize the underlying representation
of assessment tools. It comes with an open and accessible library of questionnaires
with appropriate conversion (e.g., from/to [RedCap](https://www.project-redcap.org/))
and data collection tools (e.g., [MindLogger](https://mindlogger.org/),
[RedCap](https://www.project-redcap.org/), [LORIS - future work](https://loris.ca))
to enable a more consistent acquisition across projects, with data being
harmonized by design.

## General description

With this schema we can represent:

- at the `item` level, the elements of an individual assessment, like the questions
in a questionnaire
- at the `activity` level, an individual assessment that contains a set of `items`,
like for example a whole questionnaire with a several questions.
- at the `protocols` level, a collection of `activities` performed by a participant,
 e.g a set of questionnaires used in a study.

All those elements are specified text files in a `JSON-LD` format (JavaScript
Object Notation for Linked Data) and each `item`, `activity`, and `protocol` provides
unique and persistent identifiers.

Below we show an example of one of the possible ways a questionnaire with 3 questions
for a study could be organized with a `protocol` for that study, one `activity`
and 3 `items`.

```json
├── activities
│   └── activity1
│       ├── activity1_schema.jsonld
│       └── items
│           ├── item1.jsonld
│           ├── item2.jsonld
│           └── item3.jsonld
└── protocol
    └── protocol1_schema.jsonld
```

The Reproschema can also easily and flexibly specify details how the schema
for an assessment should be used. Independently of what solution is chosen in the
end by a researcher, a lab, or an institute to display the assessment to their
participants or patients (for example whether using an Web-app written in javascript
or a mobile app written in React-native), the schema can already specify:

- the `input type` to choose among several user-interface rendering options e.g.,
 a Likert scale, a dropdown menu, a multiple choice...
- the `visibility` to decide whether a given `item` or `activity` should be
displayed to the user and under which conditions,
- the `compute logic` of how the total score to the responses on a questionnaire
should be computed

The Reproschema also allows for internationalization and multiple languages support
by making it very easy to keep everything the same 
except the language displayed by the user interface.

Finally Reproschema allows tracking of variations and version of different assessments
tools (e.g., PHQ-9, PHQ-8).
