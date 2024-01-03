# Adding a customized feedback section

To conclude our protocol, we integrate a customized feedback activity. This choice of ending with participant feedback is just one of many possibilities, demonstrating the adaptability of ReproSchema to diverse research needs.

```javascript
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc4/contexts/generic",
    "@type": "reproschema:Field",
    "@id": "feedback",
    "prefLabel": "Feedback",
    "description": "schema to record text response of overall feedback of the protocol",
    "schemaVersion": "1.0.0-rc4",
    "version": "0.0.1",
    "question": {
        "en": "Please leave any comments or suggestions on the study so we can improve it (or skip):",
        "es": "Deje cualquier comentario o sugerencia sobre el estudio para que podamos mejorarlo (u omitir):"
    },
    "ui": {
        "inputType": "textarea"
    },
    "responseOptions": {
        "valueType": "xsd:string"
    }
}
```

The `feedback` item in this activity ([`5_feedback`](https://github.com/ReproNim/reproschema-demo-protocol/blob/main/activities/5_feedback/items/feedback)) is specifically designed to gather open-ended responses, allowing participants to share their thoughts and suggestions:

- Item Structure: The item `feedback` is set up with an identification and purpose, indicated by its '@id' and descriptive fields.
- Question Prompt: The `question` is presented in both English and Spanish, encouraging participants to provide comments on their study experience. It’s formatted to be inclusive, giving participants the option to skip if they choose.
- UI Configuration for Open Responses: The choice of `textarea` as the `inputType` in the ui configuration facilitates extended text input, enabling participants to express detailed feedback comfortably. Accordingly, `valueType` in the `responseOptions` has been set as `"xsd:string"`.
