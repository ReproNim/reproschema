![Python package](https://github.com/ReproNim/reproschema/workflows/Python%20package/badge.svg)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4064940.svg)](https://doi.org/10.5281/zenodo.4064940)

<img src="docs/img/reproschema_logo.png" width="100px" />

# Schema Standardization

To see the documentation concerning the ReproNim schema specification [click here](https://www.repronim.org/reproschema/).

This repository contains:

-   the [different terms of the Reproschema](./terms)
-   the [corresponding context files](./contexts)
-   a example of [a protocol based on the reproschema](./examples)
-   the [validation SHACL files](./validation)
-   the [documentation](./docs)


## Licenses

### Code

The content of this repository is distributed under the [Apache 2.0 license](./LICENSE).

### Documentation

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />The corresponding documentation is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Contributors

https://github.com/ReproNim/reproschema/graphs/contributors

### Developer notes
To run the Python scripts in the scripts directory, you will need to install the
following libraries via pip

- reproschema (makeRelease.py)
- pytablewriter (editProperties.py)

To make a new release:

```
python scripts/makeRelease.py <version>
python scripts/editProperties.py <version>
```

In addition, this repo uses pre-commit to check styling.

Install: `pip install pre-commit`
Use: run `pre-commit install` in the root directory of the repo.
