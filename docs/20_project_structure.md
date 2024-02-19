# Project structure

The ReproSchema project is organized around several github repositories. The
main ones are the following.

- [reproschema](https://github.com/ReproNim/reproschema)
- [reproschema-library](https://github.com/ReproNim/reproschema-library)
- [reproschema-py](https://github.com/ReproNim/reproschema-py)
- [reproschema-ui](https://github.com/ReproNim/reproschema-ui)
- [reproschema-protocol-cookiecutter](https://github.com/ReproNim/reproschema-protocol-cookiecutter)

A brief description of how they all interact could be along the following lines:

> If you're gearing up to launch a research project that requires standardized questionnaires, starting with **reproschema-protocol-cookiecutter** is your best first step. This tool sets you up with a custom protocol for your study, integrating handy features for a smooth setup right from the get-go. You'll have two main paths for adding questionnaires, or activities, to your study:

> Option 1: Dive into **reproschema-library** where we've got a stash of ready-made questionnaires. Pick what fits your study, and you're good to go.

> Option 2: Feeling creative? Craft your own activities with **reproschema-py**. This tool not only lets you design new activities but also checks that they meet all the ReproSchema standards.

> Once your protocol is packed with all the activities you need, **reproschema-ui** automatically steps in. This part of the toolkit lets you see your study in action before you even start, making sure everything's set up just right for gathering data.

## [reproschema](https://github.com/ReproNim/reproschema)

The ReproSchema is like a blueprint for research projects, ensuring everyone collects data in a consistent way, which makes it easier to compare results from different studies. Here’s a simpler breakdown of what’s inside:

- **Key Terms:** These are the building blocks, like common types of answers and data formats, that help everyone understand and use data the same way.
- **How Data is Organized:** ReproSchema sorts information into three main layers to keep things neat:
- - **Item Level:** This is where individual questions or parts of a survey are detailed, allowing for close examination of each element.
- - **Activity Level:** At this stage, an entire survey or tool, made up of many items, is grouped together as an "Activity." It gives a complete overview of what the survey involves.
- - **Protocols Level:** The highest level, a "Protocol," bundles together all the activities a participant will do in a study, providing a comprehensive plan.
- **[Validation](https://github.com/ReproNim/reproschema/tree/master/validation):** The schema uses special standards (like SHACL files) to make sure the data and forms are up to standard and consistent.
- **Context Files:** These files ([`contexts`](https://github.com/ReproNim/reproschema/tree/master/contexts)and [`terms`](https://github.com/ReproNim/reproschema/tree/master/terms)) specify user-interface details and enhance schema flexibility. They define elements like input types, visibility conditions, and response options, supporting a tailored user experience. Additionally, they enable internationalization and multiple language support for broad applicability.

There is also an [`example`](https://github.com/ReproNim/reproschema/tree/master/examples)
schema that can help give you a quick overview of what the protocol and activity
for a study might look like. For more details see the [schema section](../docs/30_schema.md).

## [reproschema-library](https://github.com/ReproNim/reproschema-library)

This [repository](https://github.com/ReproNim/reproschema-library) hosts all the
community curated assessments and questionnaires that support the ReproSchema
standard.

Imagine this as curated library of reusable assessments and questionnaires, from
where you can easily pull a copy from rather than having to photocopy a new
questionnaire for your next participant or patient. Also you can mix and match
items from this library, knowing that the information is tracked in your protocol.

All assessments are listed in [the `activity` folder](https://github.com/ReproNim/reproschema-library/tree/master/activities)
and are served [here](https://schema.repronim.org/rl/) if you want to visualize
them.

- **Standard Alignment:** Each element in the library aligns with the ReproSchema framework, ensuring uniformity in terms and structure and upholding validation protocols for consistency across the ecosystem.
- **Research Protocol Integration:** Researchers can utilize these assessments in various combinations to align with specific protocol needs, customizing their application per study objectives. This process can be integrated using the reproschema-protocol-cookiecutter for constructing user interfaces.
- **Collaborative Expansion:** The library supports expansion through researcher contributions, allowing adding new, relevant assessments. These contributions are automatically validated using reproschema-py, maintaining the library’s standardization and relevance to evolving research demands.

## [reproschema-py](https://github.com/ReproNim/reproschema-py)

This is the ReproSchema python library. This is a python Command Line Interface (CLI)
that allows you to help create and validate the schemas of new assessments.

- **Schema Development and Validation:** This tool streamlines the creation and validation of new assessment schemas, verifying their alignment with ReproSchema's standards. It rigorously tests protocols, activities, and items to meet predefined specifications.
- **Consistency Assurance:** Integrated with the ReproSchema-library and ReproSchema-Protocol-Cookiecutter, reproschema-py validates library assessments for quality and uniformity. It also automatically ensures the consistency of research protocols generated through the ReproSchema-Protocol-Cookiecutter.
- **Interoperability with REDCap:** Its capability to convert between REDCap and ReproSchema formats exemplifies its role in harmonizing diverse data collection methods in complex, multi-faceted research environments.

## [reproschema-ui](https://github.com/ReproNim/reproschema-ui)

This repository contains the code for the user-interface for the ReproSchema to
visualize questionnaires and collect data.

You can see it in action [here](https://www.repronim.org/reproschema-ui/)

## [reproschema-protocol-cookiecutter](https://github.com/ReproNim/reproschema-protocol-cookiecutter)

The reproschema-protocol-cookiecutter is a straightforward tool that helps you quickly set up a research study. It offers a ready-to-use template for organizing your study's structure and surveys, ensuring everything meets standard guidelines. Think of it as a quick-start guide to get your research project up and running smoothly. A step-by-step guide see [here](../docs/41_create_new_protocol.md).

## Other repositories

### [Demo-protocol](https://github.com/ReproNim/demo-protocol)

This repository contain a full fledge protocol that can be used as demonstration.

### [Reprolib-server](https://github.com/ReproNim/reprolib-server)

This contains some additional information on how the activities are served on
[https://schema.repronim.org/rl/](https://schema.repronim.org/rl/).
