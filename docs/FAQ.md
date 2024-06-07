# FAQ

## Reproschema
<!--
### Why should I use ReproSchema?

**🛠 Work in progress 🛠**

### Who is ReproSchema for?

**🛠 Work in progress 🛠**

### How can I know if a certain property is supported by ReproSchema?

**🛠 Work in progress 🛠**

### How can I add a property to my schema?

**🛠 Work in progress 🛠**

### How are these assessments licensed?

**🛠 Work in progress 🛠**

### How can I contribute to the project?

**🛠 Work in progress 🛠**

### An assessment tool I regularly use is not supported by ReproSchema: how can I add it?

**🛠 Work in progress 🛠**
-->

### How can I visualize the schema for a `protocol` or an `activity`?

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

## Linked data and semantic web

## What is the semantic web?

When you request access to a certain document by clicking on a hyperlink,
the computer will give a visual rendering of the html code of this document.
But computer used to do that in pretty "silly" fashion:
it would give you a human-readable version of the content,
but the computer would not make the distinction if a certain element in the webpage
(for example a paragraph) was referring to a person or a place or a song.

What the semantic wed allows is to "inject" additional information into a webpage
so that a machine can know what certain elements are about (e.g "*this image is about a cat.*")
or how they are linked to other elements (on the same page or somewhere else on the web).
The tagged content of a webpage thus acquires "meaning" from the point of view of the computer,
making the semantic content of the code machine-readable.

#### More info

-   [wikipedia article on the semantic web](https://en.wikipedia.org/wiki/Semantic_Web)
-   A short video intro to the semantic web by Manu Sporny:

<iframe width="560" height="315" src="https://www.youtube.com/embed/OGg8A2zfWKg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### What is linked data?

#### The theory

The same way that an element in webpage could be given "meaning"
by tagging with extra information about the nature of this element, the same can be done with data.
Hence a given row on a spreadsheet stored somewhere on the web can be tagged
and linked to another piece of data on another website.

"*Linked data is a way to create a network of standards-based machine interpretable data across different documents and Web sites. It allows an application to start at one piece of Linked Data, and follow embedded links to other pieces of Linked Data that are hosted on different sites across the Web.*" [[source](https://w3c.github.io/json-ld-bp/#terminology)]

Linked data has some basic principles behind it ([adapted from wikipedia](https://en.wikipedia.org/wiki/Linked_data)):

-   Use Unique Resources identifiers (URI) to name (identify) things.
-   Use HTTP URIs so that these things can be looked up.
-   Provide useful information about what a name identifies when it's looked up.
-   Refer to other things using their HTTP URI-based names when publishing data on the Web.

#### A more concrete example

As things might be be quite abstract, here is a simple example of linked data to help make things more concrete:

```json
{
  "@context": "http://schema.org",
  "name": "Barack Obama",
  "givenName": "Barack",
  "familyName": "Obama",
  "jobTitle": "44th President of the United States"
}
```

You can see that the file is organised in pairs of `"key": "value"`.
The `@context` gives you the base URL of the website where you can find more information
about the different properties of this piece of data.

What follows (`name`, `givenNAme`, `familyName`, ...) are the actual properties about this data
and in front of it the values that this data takes for each property (in this case: "Barack Obama", "Barack", "Obama").

Now go and look up what is hiding behind one of those property
by going to the URL made of the **base URL + the property name**, for example [https://schema.org/familyName](https://schema.org/familyName).
This is the HTTP URI of `familyName` and this gives you a description of the `familyName` property.

Well "*So what?*" you might say.
Well it also tells you which type of data this property it can be applied to: in this case, the `Person` type (see its description [here](https://schema.org/Person)).
So even though, we never wrote anywhere explicitly that this data describes a person,
a computer able to parse that piece of linked data above would "know" this.

#### More info

-   Here is [a TED talk](https://www.ted.com/talks/tim_berners_lee_the_next_web) by Tim Berners-Lee on linked data.
-   A short video intro to linked data by Manu Sporny:

<iframe width="560" height="315" src="https://www.youtube.com/embed/4x_xzT5eF5Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### What is JSON-LD?

#### What is JSON?

OK before we go for JSON-LD, let's start with JSON. JSON stands for JavaScript Object Notation
and is just a specific format for a text file.
This type of text file is very often used by website when they need to transmit information to one another.

If you want to see an example of how this works, here is [dummy example](http://dummy.restapiexample.com/api/v1/employees) of the response to a request made by one website to another about a list of employees.
By default the output of this dummy example is presented in a way that is more pleasing to the human eye,
but if you click on `Raw Data`, you will see the raw unformatted JSON file that was returned by the website.
Copy-paste in a text editor, it should like the big ugly and scary one-liner below that we, mere mortals,
have no idea what to do with, but that a computer has no problem making sense of.

<!-- **Insert image ???** -->

```json

{"status":"success","data":[{"id":"1","employee_name":"Tiger Nixon","employee_salary":"320800","employee_age":"61","profile_image":""},{"id":"2","employee_name":"Garrett Winters","employee_salary":"170750","employee_age":"63","profile_image":""},{"id":"3","employee_name":"Ashton Cox","employee_salary":"86000","employee_age":"66","profile_image":""},{"id":"4","employee_name":"Cedric Kelly","employee_salary":"433060","employee_age":"22","profile_image":""},{"id":"5","employee_name":"Airi Satou","employee_salary":"162700","employee_age":"33","profile_image":""},{"id":"6","employee_name":"Brielle Williamson","employee_salary":"372000","employee_age":"61","profile_image":""},{"id":"7","employee_name":"Herrod Chandler","employee_salary":"137500","employee_age":"59","profile_image":""},{"id":"8","employee_name":"Rhona Davidson","employee_salary":"327900","employee_age":"55","profile_image":""},{"id":"9","employee_name":"Colleen Hurst","employee_salary":"205500","employee_age":"39","profile_image":""},{"id":"10","employee_name":"Sonya Frost","employee_salary":"103600","employee_age":"23","profile_image":""},{"id":"11","employee_name":"Jena Gaines","employee_salary":"90560","employee_age":"30","profile_image":""},{"id":"12","employee_name":"Quinn Flynn","employee_salary":"342000","employee_age":"22","profile_image":""},{"id":"13","employee_name":"Charde Marshall","employee_salary":"470600","employee_age":"36","profile_image":""},{"id":"14","employee_name":"Haley Kennedy","employee_salary":"313500","employee_age":"43","profile_image":""},{"id":"15","employee_name":"Tatyana Fitzpatrick","employee_salary":"385750","employee_age":"19","profile_image":""},{"id":"16","employee_name":"Michael Silva","employee_salary":"198500","employee_age":"66","profile_image":""},{"id":"17","employee_name":"Paul Byrd","employee_salary":"725000","employee_age":"64","profile_image":""},{"id":"18","employee_name":"Gloria Little","employee_salary":"237500","employee_age":"59","profile_image":""},{"id":"19","employee_name":"Bradley Greer","employee_salary":"132000","employee_age":"41","profile_image":""},{"id":"20","employee_name":"Dai Rios","employee_salary":"217500","employee_age":"35","profile_image":""},{"id":"21","employee_name":"Jenette Caldwell","employee_salary":"345000","employee_age":"30","profile_image":""},{"id":"22","employee_name":"Yuri Berry","employee_salary":"675000","employee_age":"40","profile_image":""},{"id":"23","employee_name":"Caesar Vance","employee_salary":"106450","employee_age":"21","profile_image":""},{"id":"24","employee_name":"Doris Wilder","employee_salary":"85600","employee_age":"23","profile_image":""}]}

```

By the way, if you ever come across such monstrosity and you want to turn into something you as a human being can understand (or least read), you can copy-paste it in a validator-formatter like [jsonformatter](https://jsonformatter.curiousconcept.com/) or [jsonlint](https://jsonlint.com/). This will quickly tell you
1.  whether this is a valid JSON format (eaning if it respects the rules of how a JSON file should be formatted) and
1.  it will highlight and help you navigate the nested and hierarchical nature of the JSON file.

<!-- **Insert image ???** -->

OK but let's start with a much simpler example of a JSON file,
like the one below which could be the content of JSON file returned by a website when asked about a certain person.

```json
{
  "name": "Barack Obama",
  "givenName": "Barack",
  "familyName": "Obama",
  "jobTitle": "44th President of the United States"
}
```

Looks familiar? It is very close to the one we had at the end of the previous FAQ section.

#### From JSON to JSON-LD

Now say you would like to use this JSON file to represent a piece of linked-data.
The only thing you would need to do in this specific case is to provide the `@context`
line we saw before that will give a precise and unambiguous meaning to the following lines.

```json
{
  "@context": "http://schema.org",
  "name": "Barack Obama",
  "givenName": "Barack",
  "familyName": "Obama",
  "jobTitle": "44th President of the United States"
}
```

🎉 **Congratulations!** 🎉

You now have a valid JSON-LD. If you want to make sure it is valid, you can copy-paste that into the [JSON-LD playground](https://json-ld.org/playground/).
If you to to visualize the "linked" aspect of that data, you can click on the `Visualized` tab
and this will give you a graph where that connects the different nodes (piece of information to one another).

If you want to visualize a more complex graph, we can try that with one of the JSON-LD file that describe one of the `protocols` of the reproschema like the one [here](https://github.com/ReproNim/reproschema/blob/741e295d998037629c213ef41cffaaf177f4d014/examples/protocols/protocol1.jsonld).
Actually if you want to test get the raw content of the file you should click on `Raw`.
You can then either use the raw content of the file or the URL of this raw file which should be something like:

```text
https://raw.githubusercontent.com/ReproNim/reproschema/741e295d998037629c213ef41cffaaf177f4d014/examples/protocols/protocol1.jsonld
```

directly into the [JSON-LD playground](https://json-ld.org/playground/) to see whether it is a valid JSON-LD and how the different elements are connected.

#### More info

-   It would be a stretch to say that the [JSON-LD specifications](https://www.w3.org/TR/json-ld11/) make for a fascinating read that will keep you up at night (although they might but mostly out of frustration)
but it is good to know that it is out there in case you eventually need to look something up
-   Two short videos by Manu Sporny about JSON-LD and core mark up features JSON-LD:

<iframe width="560" height="315"
src="https://www.youtube.com/embed/vioCbTo3C-4" frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>

<iframe width="560" height="315"
src="https://www.youtube.com/embed/UmvWk_TQ30A" frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>

### Why is linked data important for the ReproSchema ?

### Which assessments tools will/are supporting this standard?

At the moment, all the assessments that support this standard are listed in [this folder](https://github.com/ReproNim/reproschema-library/tree/master/activities) or the [reproschema-library repository](https://github.com/ReproNim/reproschema-library).

If you want to see those different tools in action using our user interface,
you can explore them on [schema.repronim.org/](https://schema.repronim.org/rl/).

The ReproSchema is also used to develop a checklist to [improve methods and results reporting in neuroimaging](https://github.com/ohbm/cobidas).
