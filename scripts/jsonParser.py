import json
import os

schema_dirs = ["contexts", "schemas", "terms"]
tested = 0
for root, _, files in os.walk(".", topdown=True):
    if os.path.basename(root) in schema_dirs:
        for name in files:
            with open(os.path.join(root, name)) as fp:
                print(f" trying parsing {root}/{name} as json")
                try:
                    tested += 1
                    json.load(fp)
                except json.decoder.JSONDecodeError:
                    print(f"{root}/{name} could not be loaded")
                    raise
if tested == 0:
    raise ValueError("Zero files tested")
