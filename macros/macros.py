from pathlib import Path

import ruamel.yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)

ROOT = Path(__file__).parents[1]

TEMPLATES_DIR = ROOT / "templates"

SCHEMA_DIR = ROOT / "linkml-schema"

def return_jinja_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(),
        lstrip_blocks=True,
        trim_blocks=True,
    )


def schema_table() -> str:

    target_classes = [
        "Protocol",
        "Activity",
        "Item",
        "AdditionalProperty",
        "OverrideProperty",
        "UnitOption",
        "ResponseOption",
        "Choice",
        "ComputeSpecification",
        "MessageSpecification",
        "AdditionalNoteObj",
        "ResponseActivity",
        "Response",
        "Participant",
        "SoftwareAgent",
    ]

    input_file = SCHEMA_DIR / "reproschema.yaml"

    reproschema = yaml.load(input_file)

    env = return_jinja_env()
    template = env.get_template("table.jinja")

    content = []
    for this_class in target_classes:

        class_dict = reproschema["classes"][this_class]
        class_dict["uri"] = class_dict["class_uri"].replace(
            "reproschema:", reproschema["id"]
        )

        slots = []
        for this_slot in class_dict["slots"]:

            slot_dict = reproschema["slots"][this_slot]

            slot_dict["name"] = this_slot

            if "title" not in slot_dict:
                slot_dict["title"] = "**TODO**"
            if "description" not in slot_dict:
                slot_dict["description"] = "**TODO**"

            prefix = slot_dict["slot_uri"].split(":")[0]
            value = reproschema["id"]
            if prefix in reproschema["prefixes"]:
                value = reproschema["prefixes"][prefix]

            slot_dict["uri"] = slot_dict["slot_uri"].replace(f"{prefix}:", value)

            slots.append(slot_dict)

        class_dict["slots"] = slots

        content.append(template.render(this_class=class_dict))

    return "\n".join(content)


def main():
    print(schema_table())


if __name__ == "__main__":
    main()
