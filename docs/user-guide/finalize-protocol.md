# Finalizing the Protocol

After setting up individual activities, we return to the main [protocol schema](https://github.com/ReproNim/reproschema-demo-protocol/blob/main/reproschema_demo_protocol/reproschema_demo_protocol_schema) to organize everything cohesively.
This step involves structuring the 'DemoProtocol_schema' to include all the activities we have developed, defining their sequence and presentation within the overall research protocol.
In the 'DemoProtocol_schema', located in the 'DemoProtocol' folder, we integrate each activity schema using the following approach:

1.  Context and protocol definition

    The `@context`, `@type`, `@id`, and descriptive fields (`prefLabel`, `description`, etc.) provide the foundational information about the protocol.

1.  Inclusion of activities

    The ui section's addProperties array is crucial. Here, each activity schema we've created is referenced under `isAbout`, with its respective `variableName` and `prefLabel`. For example, the `audio` activity is linked as

```json
{
    "isAbout": "../activities/0_audio/audio_check_schema",
    "variableName": "audio_check_schema",
    "prefLabel": {"en": "Audio Check"}
}
```

This structure is repeated for each activity, including audio check, demographics, psychological questions, clinical questions, speech task, and feedback.

1.  [Order of presentation](https://github.com/ReproNim/reproschema-demo-protocol/blob/454ea9b65ef563c70cd496de7c8f22fbbc18ba5a/reproschema_demo_protocol/reproschema_demo_protocol_schema#L50)

    The order array within ui specifies the sequence in which these activities will appear in the protocol.
    It's arranged to flow logically from consent, through various assessments, to the final feedback, ensuring a structured participant experience. For instance, the order starts with `../activities/0_audio/audio_check_schema` and progresses through to `../activities/5_feedback/feedback_schema`.

1.  [Additional UI settings](https://github.com/ReproNim/reproschema-demo-protocol/blob/454ea9b65ef563c70cd496de7c8f22fbbc18ba5a/reproschema_demo_protocol/reproschema_demo_protocol_schema#L23)
    -   `"shuffle"` is set to false to maintain the specified order.
    -   `"allow"` includes functionalities such as `"reproschema:AllowExport"` for data exporting options.

1.  Update [README.md](https://github.com/ReproNim/reproschema-demo-protocol/blob/main/reproschema_demo_protocol/README.md)

    Give clear and concise instructions on what this protocol is about and how participants should use it.

Upon finalizing our protocol with the integrated activities, the end result is a fully interactive research tool hosted on our GitHub repository. For data collection, this tool can be linked to a backend server, or participants can be given the option to export their data directly.
