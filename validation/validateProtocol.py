from pyld import jsonld
from urllib.request import urlopen
from pyshacl import validate
import json
import os

data_file_format = 'nquads'
shapes_file_format = 'turtle'

for root, dirs, files in os.walk('./protocols'):
    for name in files:
        # files without extension or with .jsonld extn
        # print(18, '--- ', name)
        full_file_name = os.path.join(root, name)
        if name != '.DS_Store' and (not os.path.splitext(full_file_name)[1]):
            with open(full_file_name) as json_file:
                try:
                    data_file = json.load(json_file)
                    if '@type' in data_file:
                        base_path = root.split('protocols/')[1]
                        base_url = 'https://raw.githubusercontent.com/ReproNim/reproschema/master/protocols/' + base_path + '/'

                        if data_file['@type'] == 'reproschema:Protocol':
                            shape_file_path = 'validation/ProtocolShape.ttl'

                        elif data_file['@type'] == 'reproschema:Field':
                            shape_file_path = 'validation/FieldShape.ttl'

                        normalized = jsonld.normalize(data_file, {'algorithm': 'URDNA2015', 'base': base_url, 'format': 'application/n-quads'})
                        conforms, v_graph, v_text = validate(normalized, shacl_graph=shape_file_path,
                                                             data_graph_format=data_file_format,
                                                             shacl_graph_format=shapes_file_format,
                                                             inference='rdfs', debug=False,
                                                             serialize_report_graph=True)
                        print(base_url+name, 'Conforms:', conforms)
                        if not conforms:
                            raise ValueError(v_text)
                except ValueError as e:
                    print ("File '%s' has validation errors: \n %s" %(full_file_name, e))
                    raise

