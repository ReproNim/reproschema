from pyld import jsonld
from urllib.request import urlopen
import json
import os

url = 'https://raw.githubusercontent.com/sanuann/reproschema/master/activities/PHQ-9/phq9_schema'
data = json.loads(urlopen(url).read().decode("utf-8"))

# for root, dirs, files in os.walk('./activities/PHQ-9', topdown=True):
#     for name in files:
#         if name.endswith('_schema'):
#             file_path = os.path.join(root, name)
#             with open(file_path) as json_file:
#                 try:
#                     print(11, json.loads(file_path))
#                 except ValueError as e:
#                     print ("File '%s' has JSON validation errors. %s" %(file_path, e))
#                     raise

for root, dirs, files in os.walk('./activities/PHQ-9', topdown=True):
    for name in files:
        # files without extension or with .jsonld extn
        if name.endswith('_schema'):
            # print(18, '--- ', name)
            full_file_name = os.path.join(root, name)
            with open(full_file_name) as json_file:
                try:
                    #print(25, json_file.read())
                    #d = json.dumps(json_file)
                    data = json.load(json_file)
                    # read_json_files.append(files)
                except ValueError as e:
                    print ("File '%s' has JSON validation errors. %s" %(full_file_name, e))
                    raise

# exp = jsonld.expand(doc)
normalized = jsonld.normalize(
    data, {'algorithm': 'URDNA2015', 'format':
        'application/n-quads'})

print(normalized)
