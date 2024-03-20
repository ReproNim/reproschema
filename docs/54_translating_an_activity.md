# Translating a questionnaire

Imagine that a colleague of yours has heard that you have created this online tool based on the Edinburgh handedness inventory and she wants to use it for her own work. But she would need a French version of the questionnaire.

Well there is an easy way to reuse the work we have already done to have the tool support several languages.

First here is the list of the questions of the EHI in French.

```
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

<!-- ---

Signer un document
Lire le braille
Lancer
Utiliser une paire de ciseaux
Utiliser une brosse à dents
Tenir un couteau (sans fourchette)
Tenir une cuillère
Utiliser un balai (main supérieure)
Allumer un briquet
Ouvrir une boîte (prendre le couvercle)

Quel est le pied avec lequel vous préférez shooter?
Quel main utilisez vous pour tenir votre canne (ou chien guide si pas de canne)? -->

## Updating the items

```json
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
        "fr": "Écrire",
    },
    "ui": {"inputType": "radio"},
    "responseOptions": "../leftRightValueConstraints.jsonld"
}
```

### What did we change ?

```json
"prefLabel": {
    "en": "writing",
    "fr": "écrire"
}
```

```json
"question": {
    "en": "Writing",
    "fr": "Écrire"
}
```

## Updating the response options

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    "@id": "leftRightValueConstraints.jsonld",
    "@type": "reproschema:ResponseOption",
    "valueType": "xsd:integer",
    "minValue": -100,
    "maxValue": 100,
    "multipleChoice": false,
    "choices": [
        {
            "name": {
            "en": "Always right",
            "fr": "Toujours la main droite"
        },
            "value": 100
        },
        {
            "name": {
            "en": "Usually right",
            "fr": "En général la main droite"
        },
            "value": 50
        },
        {
            "name": {
            "en": "Both equally",
            "fr": "Les deux"
        },
            "value": 0
        },
        {
            "name": {
            "en": "Usually left",
            "fr": "En général la main gauche"
        },
            "value": -50
        },
        {
            "name": {
            "en": "Always left",
            "fr": "Toujours la main gauche"
        },
            "value": -100
        }
    ]
}
```

### What did we change ?

```json

```

## Updating the activity

We need to update the `edinburgh_handedness_inventory_short.jsonld` so that the preamble question has both languages:

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    "@type": "reproschema:Activity",
    "@id": "edinburgh_handedness_inventory_short.jsonld",
    "prefLabel": {
        "en": "Edinburgh handedness inventory - short form",
        "fr": "Version abrégée du test Edinburgh",
    },
    "description": "Short version of the Edinburgh handedness inventory",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1",
    "citation": "10.1080/1357650X.2013.783045",
    "preamble": {
        "en": "Please indicate your preferences in the use of hands in the following activities or objects:",
        "fr": "Quelle main utilisez-vous de préférence pour :"
    },
    "ui": {
        "order": [
            "items/writing.jsonld",
            "items/throwing.jsonld",
            "items/EHI_results.jsonld"
        ],
        "shuffle": false,
        "addProperties": [
            {
                "variableName": "writing",
                "isAbout": "items/writing.jsonld",
                "valueRequired": true,
                "isVis": true
            },
            {
                "variableName": "throwing",
                "isAbout": "items/throwing.jsonld",
                "valueRequired": true,
                "isVis": true
            },
            {
                "isAbout": "items/EHI_results.jsonld",
                "variableName": "EHI_results",
                "isVis": true
            }
        ]
    },
    "compute": [
        {
            "variableName": "EHI_results",
            "jsExpression": "( writing + throwing ) / 2"
        }
    ]
}
```

### What did we change ?

```json
"prefLabel": {
    "en": "Edinburgh handedness inventory - short form",
    "fr": "Version abrégée du test Edinburgh",
}
```

```json
"preamble": {
    "en": "Please indicate your preferences in the use of hands in the following activities or objects:",
    "fr": "Quelle main utilisez vous de préférence pour :"
}
```


