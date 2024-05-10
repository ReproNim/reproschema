# Creating New Assessments for Unique Research Needs

This section provides the customized new assessments tailored to specific research needs. Our focus is on creating three distinct types of activities that are not readily available in the reproschema-library. These include: (1) clinical questions to gather clinical background information, (2) a speech task designed to collect audio data, and (3) an audio check to facilitate the speech task.

For each of these new assessments, the folder structure within the repository will differ slightly from those directly adopted from the reproschema-library. Specifically, each activity has its own dedicated folder within the `activities` directory. For instance, the speech task resides in [`activities/4_speech`](https://github.com/ReproNim/reproschema-demo-protocol/tree/main/activities/4_speech). Within this folder, besides the primary schema file (e.g., `speech_schema`), there is an additional subfolder named `items`. This `items` folder contains individual questions or tasks pertaining to that specific activity.

In the case of the speech task, the `items` folder might include a single task designed to prompt the participant to provide a speech sample. Similarly, for the clinical questions, their respective folders will contain `items` subfolders with corresponding questions tailored to elicit the required information.

The structure of an item within the `items` folder of a ReproSchema activity is similar to the schema template, but with key differences that cater to the specifics of individual data collection elements. Here's an explanation of the provided template for a `country item`:

1. **Context and type (@context, @type)**: The `@context` remains the same, pointing to the generic context of ReproSchema. The `@type` is now "reproschema:Field" instead of "reproschema:Activity". This change signifies that this template defines a single data collection field or question within an activity, as opposed to the overall structure of an activity.
2. **Identifier and descriptive fields (@id, prefLabel, description, etc.)**: `@id` serves as a unique identifier for the item, here named "country_item". prefLabel and description provide a human-readable name and a brief description of the item, similar to their use in the schema template.
3. **Question field (question)**: This field contains the actual question or prompt that will be presented to the participant. In this template, it reads: "This is an item where the user can select a country."
4. **UI configuration (ui)**: The ui section in the item template differs from the schema template. It specifies how the question will be presented to the user. The inputType is set to "selectCountry", indicating that the user interface will provide a country selection method.
5. **Response options (responseOptions)**: This section defines the nature and structure of the responses allowed for the item. In this example, it specifies the valueType as "xsd:string" and a maxLength of 50 characters. It also provides a URL to a list of choices, in this case, a JSON file containing country names. This link allows the questionnaire to dynamically fetch and display a list of countries as response options.

```javascript
"responseOptions": {
    "valueType": "xsd:string",
    "maxLength": 50,
    "choices": "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-name.json"
}
```

## Step 1: Specifying `inputType` and `responseOption` to gather precise data

We have crafted ten items in the 'items' folder for the clinical questions assessment. Each item, such as `alcohol_consumption`, `height`, `weight`, etc., has its `ui` inputType and `responseOptions` specifically defined to suit the nature of the question.

Take 'alcohol_consumption' as an example. The UI configuration and response options for this question are tailored to capture a straightforward piece of information:

```javascript
"question": {
    "en": "Have you drunk alcohol today?",
    "es": "¿Has bebido alcohol hoy?"
    },
"ui": {
    "inputType": "radio"
    },
"responseOptions": {
    "valueType": "xsd:string",
    "multipleChoice": false,
    "choices": [
        {
            "name": {
                "en": "Yes",
                "es": "Sí"
                },
            "value": 1
         },
         {
            "name": {
                "en": "No",
                 "es": "No"
                 },
            "value": 2
        }
    ]
}
```

- The ui section sets the `inputType` to `"radio"`. This choice indicates that the question will be presented to the participant as a radio button selection, providing a simple and clear interface for response selection.
- In the responseOptions, the `valueType` is defined as `"xsd:string"`, signifying that the expected type of response is a string. The multipleChoice field is set to false, indicating that participants can only select one of the provided options.
- The `choices` array lists the possible responses. In this case, there are two: "Yes" and "No", each with a corresponding value (1 for Yes, 2 for No) and translations provided for English ("en") and Spanish ("es").

- For the speech task in our demo project, the configuration of ui `inputType` and `responseOptions` is distinctively tailored to facilitate audio data collection:

```javascript
"ui": {
    "inputType": "audioPassageRecord"
},
"responseOptions": {
    "valueType": "schema:AudioObject",
    "minValue": 0,
    "maxValue": 60000
}
```

- In the ui section, the `inputType` is set to `"audioPassageRecord"`. This specific input type is designed to enable participants to record an audio passage directly within the questionnaire interface.
- The `responseOptions` are configured to accommodate the nature of audio data.
- The `valueType` is specified as "schema:AudioObject", indicating that the response will be an audio file.
- The fields `minValue` and `maxValue` define the allowable duration of the audio recording in milliseconds. In this case, the maximum duration is set to 60,000 milliseconds (or 1 minute).

## Step 2: Integrating additional components for activity-specific needs

We can integrate additional components tailored to the unique requirements of specific activities. For instance, considering the unique needs of our speech task, we add an 'audio check' component to confirm the functionality of the audio recording feature.

1. Setting up an audio check for the speech task

    To ensure the effectiveness of our speech task, we create an activity for audio verification within the `activities` folder, naming it [`0_audio`](https://github.com/ReproNim/reproschema-demo-protocol/blob/main/activities/0_audio/).
    This folder contains the [`audio_check_schema`](https://github.com/ReproNim/reproschema-demo-protocol/blob/main/activities/0_audio/audio_check_schema), a schema specifically designed to test and confirm that the audio recording system is operational and effective for participants.

2. Contextual and properties configuration for audio check

```javascript
    "@context": [
    "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc4/contexts/generic",
    {
        "voice": "https://raw.githubusercontent.com/ReproNim/reproschema-library/43e7afab312596708c0ad4dfd45b69c8904088ae/activities/VoiceTask/items/"
    }
]
```

    The @context section includes a specific context link under "voice", pointing to the repository with items relevant to voice and audio tasks: "<https://raw.githubusercontent.com/ReproNim/reproschema-library/.../VoiceTask/items/>" This targeted link ensures that the audio check activity aligns with the specific requirements of voice-related tasks.

    The ui's `addProperties` array is tailored for the audio check. We define a property `"variableName": "audio_check"` linked to `"isAbout": "voice:audio_check"`.
