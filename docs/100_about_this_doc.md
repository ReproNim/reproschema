# About this documentation

This documentation is a work in progress and we wellcome any input: if something is missing or unclear, let us know by [opening an issue on our repository] (???).

## Serving the doc locally

This project uses [MkDocs](https://www.mkdocs.org/) tool with [Material theme](https://squidfunk.github.io/mkdocs-material/) 
and extra plugins to generate the website.

To test locally, you will need to install the Python dependencies. To do that, type the following commands:

```
git clone https://github.com/ReproNim/reproschema.git
cd reproschema
pip install -r requirements.txt
```

If you are working on your *fork*, simply replace `https://github.com/ReproNim/reproschema.git`
by `git clone git@github.com/<username>/reproschema.git` where `<username>` is your GitHub username

Once done, you need to run MkDocs. Simply type:

```
mkdocs serve
```

Finally, open up [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) in your browser, and you
should see the default home page of the being displayed.
