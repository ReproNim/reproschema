# Welcome to the Reproschema documentation

<img
src="./img/reproschema_logo.png"
alt="reposchema_logo"
style="width: 350px; height: auto; display: block; margin-left: auto;  margin-right: auto;"/>

## How to use this documentation

- [1.0: Introduction](#10-introduction)

## 1.0: Introduction
Cognitive and clinical assessments are used throughout neuroscience, but little consistency exists in assessment data acquisition or response representation across studies. Harmonizing data after acquisition is resource intensive. Currently, the NIMH Data Archive (NDA) enforces harmonization during data submission. This approach can create a mismatch between collected and submitted data. Reverse engineering NDA data dictionaries to their original assessments using a tool like Brainverse can be tedious. To enforce consistency at the data acquisition stage, we created a standard schema and a set of reusable common assessments. The schema extends and modifies the CEDAR metadata representation. Using JSON-LD, we represent Items (elements of individual assessments) or Scores, Activities (individual assessments), and Protocols (collections of activities performed by a participant). An implementation of the schema  can specify scoring logic, branching logic, and user interface rendering options. The schema allows internationalization (multiple languages), is implementation agnostic, and tracks variations in assessments (e.g., PHQ-9, PHQ-8). This open and accessible schema library with appropriate conversion (e.g., to RedCap) and data collection tools (e.g., [MindLogger](https://mindlogger.org/), LORIS, RedCap) enables more consistent acquisition across projects, with results being harmonized by design.

## 2.0: Need for Standardizing assessments

## 3.0: Advantages of current representation

## 4.0: Schema

Schema overall structure:

## Licence

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Contributing and feedback

We are looking for people to give us feedback on this documentation if anything is unclear by [opening an issue on our repository](???).

You can also get in touch on [our channel on the mattermost Brainhack](???).

If you want to get started right away and contribut directly to this documentation,you can find references and how-to in the [about section](./100_about_this_doc.md).
