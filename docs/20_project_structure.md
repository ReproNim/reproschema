# Project structure

The Reproschema project is organized around several github repositories. The
main ones are the following.

- [Reproschema](https://github.com/ReproNim/reproschema)
- [Reproschema-library](https://github.com/ReproNim/reproschema-library)
- [Reproschema-ui](https://github.com/ReproNim/reproschema-ui)
- [Reproschema-py](https://github.com/ReproNim/reproschema-py)

A brief description of how they all interact could be along the following lines:

>If you are about to start a new study that needs you to use some standardized assessments, you can create new **Reproschema** `protocol` either by reusing some of the ones that we have already created and are listed in the `activities` of the **Reproschema-library**, or by using the tools of **Reproschema-py** to create the `activities` describing new questionnaires you might want to use. You can also use the **Reproschema-py** to make sure that the these `activities` conform to the specifications described in the **Reproschema**. Once you have added all the `activities` to your study `protocol`, you can use the **Reproschema-ui** to visualize the `protocol` and collect data.

## [Reproschema](https://github.com/ReproNim/reproschema)

This repository contains the actual Reproschema with the [`contexts`](https://github.com/ReproNim/reproschema/tree/master/contexts)
of the schema and the [`terms`](https://github.com/ReproNim/reproschema/tree/master/terms)
that define its different elements and how they relate to each other and to other
external entities.

This repository also contains SHACL-based validation information in [`validation`](https://github.com/ReproNim/reproschema/tree/master/validation),
which allows you to ensure that any new `protocol`, `activity` or `item` you create
conforms to the specifications of the schema.

There is also an [`example`](https://github.com/ReproNim/reproschema/tree/master/examples)
schema that can help give you a quick overview of what the protocol and activity
for a study might look like. For more details see the [schema section](../30_schema).

## [Reproschema-library](https://github.com/ReproNim/reproschema-library)

This [repository](https://github.com/ReproNim/reproschema-library) hosts all the
community curated assessments and questionnaires that support the Reproschema
standard.

Imagine this as curated library of reusable assessments and questionnaires, from
where you can easily pull a copy from rather than having to photocopy a new
questionnaire for your next participant or patient. Also you can mix and match
items from this library, knowing that the information is tracked in your protocol.

All assessments are listed in [the `activity` folder](https://github.com/ReproNim/reproschema-library/tree/master/activities)
and are served [here](https://schema.repronim.org/rl/) if you want to visualize
them.

## [Reproschema-ui](https://github.com/ReproNim/reproschema-ui)

This repository contains the code for the user-interface for the ReproSchema to
visualize questionnaires and collect data.

You can see it in action [here](https://www.repronim.org/reproschema-ui/)

## [Reproschema-py](https://github.com/ReproNim/reproschema-py)

This is the Reproschema python library. This is a python Command Line Interface (CLI)
that allows you to help create and validate the schemas of new assessments.

- test that a schema for a `protocol`, `activity` or `item` is valid and matches
the specification of the Reproschema
- convert a csv file of a questionnaire into its equivalent Reproschema

## Other repositories

### [Demo-protocol](https://github.com/ReproNim/demo-protocol)

This repository contain a full fledge protocol that can be used as demonstration.

### [Reprolib-server](https://github.com/ReproNim/reprolib-server)

This contains some additional information on how the activities are served on
[https://schema.repronim.org/rl/](https://schema.repronim.org/rl/).

### [Reproschema-builder](https://github.com/ReproNim/reproschema-builder)

This repository contains a javascript conversion tool that have been used to
create some of our activities, and can be used to convert RedCap data
dictionaries to Reproschema.
