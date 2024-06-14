## Viewing the activity

Push the content you have created on your repository on github

```bash
# Type this in a terminal window
git add --all
git commit -m 'adding the EHI activity'
git push
```

Use the UI to visualize just the activity.

```text
https://www.repronim.org/reproschema-ui/#/activities/0?url=url-to-activity-schema
```

```text
https://www.repronim.org/reproschema-ui/#/activities/0?url=https://raw.githubusercontent.com/<YOUR_USERNAME>/depression_nimg_schema/activities/edinburgh_handedness_inventory_short.jsonld
```

## Adding the activity to the protocol

```json linenums="1" hl_lines="25-29 33"
--8<-- "examples/protocols/depression_nimg_schema.jsonld"
```
