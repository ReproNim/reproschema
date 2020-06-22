import os
import json

schema_dirs = ["contexts", "schemas", "terms"]

for root, dirs, files in os.walk('.', topdown=True):
    if os.path.basename(root) in schema_dirs:
        for name in files:
            with open(os.path.join(root, name)) as fp:
                try:
                    json.load(fp)
                except json.decoder.JSONDecodeError:
                    print(f"{root}/{name} could not be loaded")
                    raise

