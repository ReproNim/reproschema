# How can I use reproschema to create my own questionnaire?

Broadly speaking, there are two ways to create new assessments (`actitivies`) or combinations
of assessments (`protocols`). IF you only have very few items to put in new activity or you simply want to create a protocol that reuses activities that already exist, you can do that manually by editing the files directly. But if you have to create complex activities or protocols, we suggest that for your own sanity and to avoid wasting time in the long run, you look into scripting the creation of your new tools.

## Manual schema generation

Here we will show a step by step approach to create a new protocol that includes activities that already exist and how to create a brand new activity.

## Requirements

For this tutorial you will be using some other tools to put your work online. Here is what you will need to install or set up.

- [Git](https://git-scm.com/downloads)
- a [Github account](https://github.com/)
- a "decent" text editor like [atom](https://atom.io/) or [visual studio code](https://code.visualstudio.com/) and we do recommend that you look for extensions or packages that help you deal with json files.

We don't assume that you have in-depth knowledge of git and github for this tutorial so we will try to provide with commands you need to type when it is required. Similarly, we will provide some of the commands to create directories and files though you could do many of those actions "by hand" with a couple of mouse clicks.

For Windows users: 

Most of the commands we will provide should work in the command line interface that will come on your computer when you isntall Git. But you could also look into using one the linux sub-system that provide you with Unix command line and that can be easily installed from the app-store on your computer.

## Context

To make this a bit less abstract, we will imagine we want to create a new protocol for a new neuroimaging study we are starting to investigate some aspects of linguistic processing is affected in patients with depression. 

So we would want to have a set of questionnaires:
- to assess the severity of the depression of our participants,
- check which participants can go in an MRI scanner,
- estimate the handedness of the participants (because of the language lateralization organization of the brain).

## Setting the stage

We first need to create some folders to host the schema that will represent all our questionnaires.

```bash
# FYI: this is comment and it will not be executed 
#  if you copy paste it in the command line

# Creating the directory for the depression neuroimaging study
mkdir depression_nimg_schema

# Move into the directory 
cd depression_nimg_schema
```

Now let's create the `protocol` folder, a protocol file named after our study.

```bash
mkdir protocol
touch protocol/depression_nimg_schema.jsonld
```

Ok so now we are ready to start putting some content into those files.

Open the `depression_nimg_schema.jsonld` with a text editor and add the following content into it.

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    "@type": "reproschema:Protocol",
    "@id": "depression_nimg_schema",
    "prefLabel": "depression neuroimaging study",
    "description": "a study on linguistic processing in depression",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1"
}
```

To explain a bit what all of this means:

- `@context` gives the URL where we can find the "definitions" of terms used in the reproschema. It is itself a json file that you [can view directly](https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic).
- `@type` just says what type of entity this jsonld file describes. In this case it is a `protocol` entity as defined by the reproschema.
- `@id` is the identity of this entity, its unique identifier.

You can then use the preferred label field and the description to give more human readable ways to describe this entity.

You must also specify the version of the schema you are using.

### Landing page

Let's now take care of adding a landing page to the list of assessments our participants will have to fill in.

Let's create a markdown readme file in the `protocol` folder.

```bash
touch protocol/README.md
```

Add some content to it just to get things started, like for example

```markdown
# README

Hello world
```

Now we want to add this file to our protocol and make it the landing page for the english version of this study. So the content of your protocol file should now read like this.

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
    "@type": "reproschema:Protocol",
    "@id": "depression_nimg_schema",
    "prefLabel": "depression neuroimaging study",
    "description": "a study on linguistic processing in depression",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1",
    "landingPage": { 
        "@id": "README.md",
        "@language": "en"
    }
}
```

## Add a first assessment

OK now we want to add a questionnaire to assess the severity of the depression of our participants.

The first thing to do is to browse through the [library of assessments](https://github.com/ReproNim/reproschema-library/tree/master/activities) that already exist on the [dedicated repronim repositor](https://github.com/ReproNim/reproschema-library).

It seems that we can use the [PHQ-9](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1495268/) that self describes as a "Brief Depression Severity Measure".

The schema that describe the PHQ-9 activity can be found [here](https://github.com/ReproNim/reproschema-library/blob/master/activities/PHQ-9/PHQ9_schema).

If you want to visualize this activity on its own, you can use the [reproschema-ui](https://www.repronim.org/reproschema-ui/#/). To do that you can point the UI to the **raw** content of this activity.

To get access to the raw content of that activity you must click on the `Raw` button on github once you have opened its [page](https://github.com/ReproNim/reproschema-library/blob/master/activities/PHQ-9/PHQ9_schema). This will open this URL: [https://raw.githubusercontent.com/ReproNim/reproschema-library/master/activities/PHQ-9/PHQ9_schema](https://raw.githubusercontent.com/ReproNim/reproschema-library/master/activities/PHQ-9/PHQ9_schema).

You can then pass the the URL of raw content to the UI using the following template:

```
https://www.repronim.org/reproschema-ui/#/activities/0?url=url-to-activity-schema
```

So in the case of the PHQ-9, it would give this URL that we copy-paste in a browser to view the activity on its own.

```
https://www.repronim.org/reproschema-ui/#/activities/0?url=https://raw.githubusercontent.com/ReproNim/reproschema-library/master/activities/PHQ-9/PHQ9_schema
```

You should now be able to see something like this and browse directly through the content of the activity.

<img
src="../img/phq-9_ui.png"
alt="phq-9_ui.png"
style="width: 700px; height: auto; display: block; margin-left: auto;  margin-right: auto;"/>


OK now that we know what we need to add to our protocol, let's add it our schema.

To do this, the content of your `depression_nimg_schema.jsonld` should now look like this.

```json
{
    "@context": [ "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0-rc1/contexts/generic",
        {
            "rl": "https://raw.githubusercontent.com/ReproNim/reproschema-library/master/activities/"
        }
    ],
    "@type": "reproschema:Protocol",
    "@id": "depression_nimg_schema",
    "prefLabel": "depression neuroimaging study",
    "description": "a study on linguistic processing in depression",
    "schemaVersion": "1.0.0-rc1",
    "version": "0.0.1",
    "landingPage": { 
        "@id": "README.md",
        "@language": "en"
    },
    "ui": {
    "addProperties": [
        {"isAbout": "rl:PHQ-9/PHQ9_schema",
        "variableName": "PHQ9_schema",
        "prefLabel": {"en": "Depression"}
        }
    ],
    "order": [
        "rl:PHQ-9/PHQ9_schema"
    ]
    }
}
```

Let's just highlight the things that have changed.

We have added a `ui` and an `order` fields.

`ui` contains `addProperties` where we will be listing all the assessments that we add to our protocol.

Each assessment is represented by an activity that is given a `variableName` and a `prefLabel`. The latter will be used in this case as the name to display on the UI in english.

The field `isAbout` is the URL to point to the schema of that activity. You might notice that `rl:PHQ-9/PHQ9_schema` does not look like a typical URL and clearly does not match the one we fed the UI earlier (https://raw.githubusercontent.com/ReproNim/reproschema-library/master/activities/PHQ-9/PHQ9_schema). Well this is because we have defined, in the `@context` part of our jsonld, that the `rl` from `rl:PHQ-9/PHQ9_schema` will actually stand for `https://raw.githubusercontent.com/ReproNim/reproschema-library/master/activities/`. This shorthand makes it faster for us to write URL but the UI will know how to `expand` this into an actual URL.

The field `order` is there to indicate which activity should be presented first, second...

### Starting to put things online to see how they look

So now we want to put things online and see how things look.

To do that we will use Git and Github.

Let's first initialize a repository in the folder where we have have been working.

```bash
git init . # the dot signifies the directory where you currently are
```

Now we tell git to make a snapshot of the current state of your folder.

```bash
git add --all # tell git to include all the new changes into the next snapshot

git commit -m 'add protocol and README' # make a first snapshot of your protocol
```

Now to move things to a github repository, you need to go and create an empty repository to host the folder and files you have created.

The repository should have an URL that resembles this one where `your_user_name` is your actual Github username:

```
https://github.com/your_user_name/depression_nimg_schema.git
```

You "push" the content of the `depression_nimg_schema` onto the empty "remote" repository you have just created.

```bash
# tell git about the existence of this new online repository you have just created
git remote add origin https://github.com/your_user_name/depression_nimg_schema.git

# Transfer the content there
git push -u origin master
```

If everything worked normally, you should be able to use the reproschema-ui to visualize your protocol using the following template:

```
https://www.repronim.org/reproschema-ui/#/?url=url-to-protocol-schema
```

So once again grab the URL of the **raw** content of your protocol and point the UI to it:

```
https://www.repronim.org/reproschema-ui/#/?url=https://raw.githubusercontent.com/your_user_name/depression_nimg_schema/master/protocol/depression_nimg_schema.jsonld
```

## In you own time: add the thank-you activity

For practice you can now add another activity to your protocol: one to thank people for their participation.

You can find it here in the reproschema library.

https://github.com/ReproNim/reproschema-library/tree/master/activities/ThankYou

Once you have changed the `depression_nimg_schema.jsonld`, you can update the oneline content with the following git commands.

```bash
git add --all
git commit -m 'add a thank you activity'
git push
```


<!-- 
## Create a new activity

Activity directory structure:

-   `/items` (directory) : contains the `jsonld` files for individual items of the activity schema
    -   `item_1`
    -   `item_2`
    -   …
-   `activityName_schema` : schema to define the activity
-   `activityName_context` : context to define keys used specific to the activity schema

Creating `activityName_schema` – use the keys defined in [`schemas/Activity`](./schemas/Activity).
If any other keys are used, then define them in `activityName_context`

Mandatory keys:

-  `@context` - [Array] Include the ReproNim generic context JSON-LD file along with the activity context.
-   `@type`- describes type of the schema.
-   `@id` - unique id for the schema. should be same as the filename.
-   `skos:prefLabel` - display name for the schema
-   `ui.addProperties` - defines the various properties of each item.
-   `variablename` - variable name used in `ui.order` for the items
-   `isAbout` - file name of the corresponding variable name
-   `ui.order` - [Array] defines the order in which the items appear in the activity

### Create items

To create `item_x` in the items folder:

-   Use keys defined in [`schemas/Field`](./schemas/Field)
-   `@type`=`"https://raw.githubusercontent.com/ReproNim/reproschema/master/schemas/Field"`
-   `responseOptions` – can be embedded or can point to a remote JSON-LD object.

## Programmatic schema generation

Tool to convert redcap CSVs to our schema format. But it cannot be used to convert every
redcap-formatted table as some are customized redcap tables (for example the 100s that are in ABCD)
but does cover most cases. A template of the CSV and how to use the tool can be found
[here](https://github.com/sanuann/reproschema-builder) -->