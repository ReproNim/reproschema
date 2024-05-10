# Translating a questionnaire

Imagine that a colleague of yours has heard that you have created this online tool
based on the Edinburgh handedness inventory and she wants to use it for her own work.
But she would need a French version of the questionnaire.

Well there is an easy way to reuse the work we have already done to have the tool support several languages.

First here is the list of the questions of the EHI in French.

```text
Quelle main utilisez vous de préférence pour:

1) Écrire (*)
2) Dessiner
3) Lancer (*)
4) Utiliser une paire de ciseaux
5) Utiliser une brosse à dents (*)
6) Tenir un couteau (sans fourchette)
7) Tenir une cuillère (*)
8) Utiliser un balai (main supérieure)
9) Tenir une allumette pour l'allumer
10) Ouvrir une boîte (prendre le couvercle)

i) Quel est le pied avec lequel vous préférez shooter?
ii) Quel oeil utiliser-vous pour viser?
```

## Updating the items

```json linenums="1" hl_lines="5-8 12-15"
{
  "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
  "@type": "reproschema:Field",
  "@id": "writing",
  "prefLabel": {
    "en": "writing",
    "fr": "écrire"
  },
  "description": "writing item of the EHI",
  "schemaVersion": "1.0.0-rc1",
  "version": "0.0.1",
  "question": {
    "en": "Writing",
    "fr": "Écrire"
  },
  "ui": { "inputType": "radio" },
  "responseOptions": "../leftRightValueConstraintsMultiLang.jsonld"
}
```

## Updating the response options

```json linenums="1" hl_lines="10-14 17-21 24-28 31-35 38-42"
--8<-- "example_ehi/activities/EHI/leftRightValueConstraintsMultiLang.jsonld"
```

## Updating the activity

We need to update the `edinburgh_handedness_inventory_short.jsonld` so that the preamble question has both languages:

```json linenums="1" hl_lines="5-8 13-16"
--8<-- "example_ehi/activities/EHI/edinburgh_handedness_inventory_short_multi_lang.jsonld"
```
