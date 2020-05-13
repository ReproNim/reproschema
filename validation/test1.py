from pyld import jsonld
from urllib.request import urlopen
from pyshacl import validate
import json
import os

url = 'https://raw.githubusercontent.com/ReproNim/reproschema/master/activities/PHQ-9/PHQ9_schema'
data = json.loads(urlopen(url).read().decode("utf-8"))

for root, dirs, files in os.walk('./activities/PHQ-9'):
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
                    normalized = jsonld.normalize(
                        data, {'algorithm': 'URDNA2015', 'format':
                            'application/n-quads'})
                    r = validate(normalized, shacl_graph='validation/ActivityShape.ttl')
                    conforms, results_graph, results_text = r
                    # read_json_files.append(files)
                except ValueError as e:
                    print ("File '%s' has JSON validation errors. %s" %(full_file_name, e))
                    raise

# exp = jsonld.expand(doc)
normalized = jsonld.normalize(
    data, {'algorithm': 'URDNA2015', 'format':
        'application/n-quads'})

#print(normalized)
