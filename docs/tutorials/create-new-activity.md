# Create a new activity

Now you would like to add a small questionnaire to estimate the handedness of
each participant. We can use the Edinburgh handedness inventory for this.

This tool is not part of the set of questionnaires included in the repronim
library so we are going to have to create it ourselves.

There are 2 version for this questionnaire a long and a short version.

-   Oldfield, R.C. (1971). The assessment and analysis of handedness: The
    Edinburgh inventory. Neuropsychologia, 9, 97-113.
    doi:[10.1016/0028-3932(71)90067-4](https://doi.org/10.1016/0028-3932(71)90067-4)

-   Veale, J.F. (2014). Edinburgh Handedness Inventory - Short Form: A revised
    version based on confirmatory factor analysis. Laterality, 19, 164-177.
    doi:[10.1080/1357650X.2013.783045](https://doi.org/10.1080/1357650X.2013.783045)

The participant is given one question and a set of activities:

```text
Please indicate your preferences in the use of hands in the following activities or objects:

1) Writing (*)
2) Drawing
3) Throwing (*)
4) Using Scissors
5) Using a Toothbrush (*)
6) Using a Knife (without a fork)
7) Using a Spoon (*)
8) Using a broom (upper hand)
9) Striking a Match (holds the match)
10) Opening a Box (holding the lid)

i) Which foot do you prefer to kick with ?
ii) Which eye do you use when using only one?
```

The asterisks denote the subset of items that belong to the short form of the questionnaire.

The scoring for each item follows the following scheme:

-   Always right = 100
-   Usually right = 50
-   Both equally = 0
-   Usually left = -50
-   Always left = -100

The Laterality Quotient is given by the mean score over items. And the final
classification according to the Laterality Quotient score goes as follow:

-   Left handers: -100 to -61
-   Mixed handers: -60 to 60
-   Right handers: 61 to 100

<!-- ---
Note that there is also a longer with extra items that are not on the standard inventory.

- Holding a Computer Mouse
- Using a Key to Unlock a Door
- Holding a Hammer
- Holding a Brush or Comb
- Holding a Cup while Drinking

Source: http://www.brainmapping.org/shared/Edinburgh.php
-->

## Preparing the JSON for the activity

Now let's create the `activities` folder, an activity file for the new assessment tool we want to create.
For this tutorial we will be using the short form of the Edinburgh handedness inventory.

```bash
# Type this in a terminal window
mkdir activities
touch activities/EHI/edinburgh_handedness_inventory_short.jsonld
```

Now let's start by adding the following content in the activity file we have just created.

```json linenums="1"
{
  "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
  "@type": "reproschema:Activity",
  "@id": "edinburgh_handedness_inventory_short.jsonld",
  "prefLabel": "Edinburgh handedness inventory - short form",
  "description": "Short version of the Edinburgh handedness inventory",
  "schemaVersion": "1.0.0-rc1",
  "version": "0.0.1"
}
```

The content is for now very similar to the JSON-LD that defines our protocol.
The main difference is for the `@type` field that mentions
that we are now describing an activity as defined in the Reproschema.

Two other things we can add right away are:

-   the references for this questionnaire,
-   the `"preamble"` that is common to all items in this questionnaire.

```json linenums="1" hl_lines="9-10"
{
  "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
  "@type": "reproschema:Activity",
  "@id": "edinburgh_handedness_inventory_short.jsonld",
  "prefLabel": "Edinburgh handedness inventory - short form",
  "description": "Short version of the Edinburgh handedness inventory",
  "schemaVersion": "1.0.0-rc1",
  "version": "0.0.1",
  "citation": "10.1080/1357650X.2013.783045",
  "preamble": "Please indicate your preferences in the use of hands in the following activities or objects:"
}
```
