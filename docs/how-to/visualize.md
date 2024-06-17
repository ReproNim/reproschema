# Visualize

If you want to visualize the protocol or the activity you have created,
you can use the [reproschema-ui](https://github.com/ReproNim/reproschema-ui) to preview it.

If you want to see what the assessment that are already supported by the ReproSchema would look like using our ReproSchema user-interface, you can visualize them directly on [schema.repronim.org](https://schema.repronim.org/rl).

If you just want to view a protocol or activity you are developing using the `reproschema-ui`,
you can pass the URL of the schema to the `url` query parameter like this:

```https://schema.repronim.org/ui/#/?url=url-to-your-schema```

If you are hosting a schema on github, make sure that you are passing the URL of the **raw** content of the schema.
For example, our demo protocol can be accessed at this URL:

[https://github.com/ReproNim/reproschema-demo-protocol/blob/7ed1ae49279f75acdd57380fff1f8aaff2c7b511/reproschema_demo_protocol/reproschema_demo_protocol_schema](https://github.com/ReproNim/reproschema-demo-protocol/blob/7ed1ae49279f75acdd57380fff1f8aaff2c7b511/reproschema_demo_protocol/reproschema_demo_protocol_schema)

But to get access to the raw content of that file you must click on the `Raw` button
once you have opened that page on github that will open this URL:

[https://raw.githubusercontent.com/ReproNim/reproschema-demo-protocol/7ed1ae49279f75acdd57380fff1f8aaff2c7b511/reproschema_demo_protocol/reproschema_demo_protocol_schema](https://raw.githubusercontent.com/ReproNim/reproschema-demo-protocol/7ed1ae49279f75acdd57380fff1f8aaff2c7b511/reproschema_demo_protocol/reproschema_demo_protocol_schema).

If you want to visualize the graph represented by the JSON-LD file,
we explain how to do this in [From JSON to JSON-LD](#from-json-to-json-ld).
