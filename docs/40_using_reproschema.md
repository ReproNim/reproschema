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

We don't assume that you have in-depth knowledge of Git and Github for this tutorial so we will try to provide with the commands you need to type when it is required. Similarly, we will provide some of the commands to create directories and files though you could do many of those actions "by hand" with a couple of mouse clicks.

??? "For Windows users"
    Most of the commands we will provide should work in the command line interface that will come on your computer when you isntall Git. But you could also look into using one the linux sub-system that provide you with Unix command line and that can be easily installed from the app-store on your computer.

## Context

To make this a bit less abstract, we will imagine we want to create a new protocol for a new neuroimaging study we are starting to investigate some aspects of linguistic processing is affected in patients with depression.

So we would want to have a set of questionnaires:

- to assess the severity of the depression of our participants,
- check which participants can go in an MRI scanner,
- estimate the handedness of the participants (because of the language lateralization organization of the brain).
