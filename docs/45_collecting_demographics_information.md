# Collecting information about your participant

Before you go and start creating new activities and items to collect the names, surnames and other demographics of your participants make sure you have had a look at these items on the reproschema library: 

See the [demographics_and_background_information_v1](https://github.com/ReproNim/reproschema-library/tree/master/activities/demographics_and_background_information_v1/items) folder:

```
demographics_and_background_information_v1/
└── items
    ├── age_months
    ├── age_years
    ├── ann_fam_income
    ├── child_out_psych_cur
    ├── child_out_psych_ever
    ├── countryOfBirth
    ├── demo_init
    ├── demo_rpt_date
    ├── document
    ├── doe
    ├── education_level
    ├── email
    ├── ethnic_category
    ├── ethnic_category_informant
    ├── fluentLanguages
    ├── fullName
    ├── handedness
    ├── healthCondition
    ├── inpatient_psych
    ├── inpatient_treat_age
    ├── inpatient_treat_dur
    ├── inpatient_treatments
    ├── interviewed_who
    ├── interview_type
    ├── knownLanguages
    ├── last_period
    ├── medication
    ├── menarche_start
    ├── meneses
    ├── mentalHealth
    ├── nativeLanguage
    ├── other_persons_instructions
    ├── outpatient_treat_age
    ├── outpatient_treatments
    ├── outpatient_treat_weeks
    ├── parent_relationship
    ├── parent_relationship_1
    ├── parent_relationship_2
    ├── participant_education
    ├── participant_id
    ├── particpant_grade_level
    ├── person1_education
    ├── person1_id
    ├── person1_occ_lvl
    ├── person1_other_id
    ├── person2_education
    ├── person2_exist
    ├── person2_id
    ├── person2_occ_lvl
    ├── person2_other_id
    ├── race_category
    ├── race_category_informant
    ├── raceEthnicity
    ├── record_id
    ├── religious_category
    ├── sex
    ├── share_data
    ├── stateOfBirth
    ├── stateOfResidence
    └── verification_id
```

```json
{
    "@context": [ "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
        {
            "demo": "https://github.com/ReproNim/reproschema-library/tree/master/activities/demographics_and_background_information_v1/items"
        }
    ],
    "@type": "reproschema:Activity",
    "@id": "demographics.jsonld",
    "prefLabel": "demographics",
    "description": "information about the participant",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1",
    "ui": {
        "order": [
            "demo:writing.jsonld",
            "demo:throwing.jsonld",
            "demo:EHI_results.jsonld"
        ],
        "shuffle": false,
        "addProperties": [
            {
                "variableName": "participant_id",
                "isAbout": "demo:participant_id",
            },
            {
                "variableName": "fullName",
                "isAbout": "demo:fullName",
            },
            {
                "variableName": "sex",
                "isAbout": "demo:sex",
            },
            {
                "variableName": "age_years",
                "isAbout": "demo:age_years",
            },
            {
                "isAbout": "demo:email",
                "variableName": "email",
            },
            {
                "isAbout": "demo:participant_education",
                "variableName": "participant_education",
            },
            {
                "isAbout": "demo:nativeLanguage",
                "variableName": "nativeLanguage",
            },
            {
                "isAbout": "demo:healthCondition",
                "variableName": "healthCondition",
            },
            {
                "isAbout": "demo:mentalHealth",
                "variableName": "mentalHealth",
            },
            {
                "isAbout": "demo:share_data",
                "variableName": "share_data",
            },
            {
                "isAbout": "demo:medication",
                "variableName": "medication",
            }
        ]
    }
}
```
