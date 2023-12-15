# Finalizing the Protocol

After setting up individual activities, we return to the main protocol schema to organize everything cohesively. This step involves structuring the 'DemoProtocol_schema' to include all the activities we have developed, defining their sequence and presentation within the overall research protocol. In the 'DemoProtocol_schema', located in the 'DemoProtocol' folder, we integrate each activity schema using the following approach:
1. Context and protocol definition

    The '@context', '@type', '@id', and descriptive fields ('prefLabel', 'description', etc.) provide the foundational information about the protocol.

2. Inclusion of activities
   
    The ui section's addProperties array is crucial. Here, each activity schema we've created is referenced under 'isAbout', with its respective 'variableName' and 'prefLabel'. For example, the consent activity is linked as 
    ```javascript
    {
        "isAbout": "../activities/0_consent/consent_schema", 
        "variableName": "consent_schema", 
        "prefLabel": {"en": "Sign Consent"}
    }
    ```
    This structure is repeated for each activity, including audio check, demographics, psychological questions, clinical questions, speech task, and feedback.

2. Order of presentation
    
    The order array within ui specifies the sequence in which these activities will appear in the protocol. It's arranged to flow logically from consent, through various assessments, to the final feedback, ensuring a structured participant experience. For instance, the order starts with `../activities/0_audio/audio_check_schema` and progresses through to `../activities/5_feedback/feedback_schema`.

3. Additional UI settings:
    - 'shuffle' is set to false to maintain the specified order.
    - 'allow' includes functionalities such as 'reproschema:AllowExport' for data exporting options.
	
Upon finalizing our protocol with the integrated activities, the end result is a fully interactive research tool hosted on our GitHub repository. For data collection, this tool can be linked to a backend server, or participants can be given the option to export their data directly.
