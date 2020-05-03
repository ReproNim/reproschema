import os
import json

# invalid_json_files = []
# read_json_files = []


for root, dirs, files in os.walk('./activities', topdown=True):
    for name in files:
        # files without extension or with .jsonld extn
        if not os.path.splitext(name)[1] or os.path.splitext(name)[1] == '.jsonld':
            # print(18, '--- ', name)
            full_file_name = os.path.join(root, name)
            with open(full_file_name) as json_file:
                try:
                    #print(25, json_file.read())
                    #d = json.dumps(json_file)
                    json.load(json_file)
                    # read_json_files.append(files)
                except ValueError as e:
                    print ("File '%s' has JSON validation errors. %s" %(full_file_name, e))
                    raise
                    # invalid_json_files.append(files)

# print(invalid_json_files, len(read_json_files))
