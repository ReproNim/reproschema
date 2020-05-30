from pyld import jsonld
from urllib.request import urlopen
from pyshacl import validate
import json
import os

url = 'https://raw.githubusercontent.com/ReproNim/reproschema/master/activities/PHQ-9/items/phq9_1'
data = json.loads(urlopen(url).read().decode("utf-8"))

for root, dirs, files in os.walk('./activities/PHQ-9/items'):
    for name in files:
        full_file_name = os.path.join(root, name)
        if not os.path.splitext(full_file_name)[1]:
            with open(full_file_name) as json_file:
                try:
                    data = json.load(json_file)
                    # normalized = jsonld.normalize(
                    #     data, {'algorithm': 'URDNA2015', 'format':
                    #         'application/n-quads'})
                    # r = validate(normalized, shacl_graph='validation/ActivityShape.ttl')
                    # conforms, results_graph, results_text = r
                    # read_json_files.append(files)
                    # print(27, data['@type'], data['@id'])
                    # with open("test1.ttl", "w+") as fp:
                    #     fp.write(normalized)
                except ValueError as e:
                    print ("File '%s' has JSON validation errors. %s" %(full_file_name, e))
                    raise

# exp = jsonld.expand(doc)
normalized = jsonld.normalize(
    data, {'algorithm': 'URDNA2015', 'format':
        'application/n-quads'})

print(normalized)
