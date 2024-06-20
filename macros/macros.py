from pathlib import Path
import json

import ruamel.yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)

ROOT = Path(__file__).parents[1]

TEMPLATES_DIR = ROOT / "templates"

LIBRARY_DIR = ROOT / "library"

SCHEMA_DIR = ROOT / "linkml-schema"


def return_jinja_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(),
        lstrip_blocks=True,
        trim_blocks=True,
    )


def library_table() -> str:

    LIBRARY_URL = "https://github.com/ReproNim/reproschema-library"

    activities = []

    for activity_path in (LIBRARY_DIR / "activities").iterdir():

        if not activity_path:
            continue

        for file in activity_path.glob("*"):

            if file.is_dir() or file is None or "valueConstraints" in file.stem:
                continue

            with open(file) as f:
                content = json.load(f)

            activities.append(
                {
                    "name": content["@id"],
                    "description": (
                        content["description"] 
                        if "description" in content 
                        else ""
                    ),
                    "uri": f"{LIBRARY_URL}/tree/master/activities/{activity_path.stem}/{file.stem}{file.suffix}",
                }
            )

    env = return_jinja_env()
    template = env.get_template("library_table.jinja")

    return template.render(activities=activities)


def main():
    print(library_table())


if __name__ == "__main__":
    main()
