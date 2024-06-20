# Visualize

If you want to visualize the graph represented by the JSON-LD file,
we explain how to do this in [From JSON to JSON-LD](../FAQ.md#from-json-to-json-ld).

If you want to visualize the protocol or the activity you have created as a web form,
you can use the [reproschema-ui](https://github.com/ReproNim/reproschema-ui) to preview it.
To do so you can pass the URL to your protocol or activity as a query
to the [reproschema-ui app](https://www.repronim.org/reproschema-ui/)

```https://www.repronim.org/reproschema-ui/#/?url=url-to-your-schema```

If you are hosting a schema on github, make sure that you are passing the URL of the **raw** content of the schema.
For example, our demo protocol can be accessed at this URL:

[https://github.com/ReproNim/reproschema-demo-protocol/blob/7ed1ae49279f75acdd57380fff1f8aaff2c7b511/reproschema_demo_protocol/reproschema_demo_protocol_schema](https://github.com/ReproNim/reproschema-demo-protocol/blob/7ed1ae49279f75acdd57380fff1f8aaff2c7b511/reproschema_demo_protocol/reproschema_demo_protocol_schema)

But to get access to the raw content of that file you must click on the `Raw` button
once you have opened that page on github that will open this URL:

[https://raw.githubusercontent.com/ReproNim/reproschema-demo-protocol/7ed1ae49279f75acdd57380fff1f8aaff2c7b511/reproschema_demo_protocol/reproschema_demo_protocol_schema](https://raw.githubusercontent.com/ReproNim/reproschema-demo-protocol/7ed1ae49279f75acdd57380fff1f8aaff2c7b511/reproschema_demo_protocol/reproschema_demo_protocol_schema).

So in the end the URL to preview this protocol as a web form would be:

[https://www.repronim.org/reproschema-ui/#/?url=https://raw.githubusercontent.com/ReproNim/reproschema-demo-protocol/7ed1ae49279f75acdd57380fff1f8aaff2c7b511/reproschema_demo_protocol/reproschema_demo_protocol_schema](
https://www.repronim.org/reproschema-ui/#/?url=https://raw.githubusercontent.com/ReproNim/reproschema-demo-protocol/7ed1ae49279f75acdd57380fff1f8aaff2c7b511/reproschema_demo_protocol/reproschema_demo_protocol_schema)
