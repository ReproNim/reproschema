from glob import glob
from pyld import jsonld
from urllib.request import urlopen
from pyshacl import validate
import json
import os

import os
import threading
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler


def simple_http_server(host='localhost', port=4001, path='.'):
    """
    From: https://stackoverflow.com/a/38943044
    """

    server = HTTPServer((host, port), SimpleHTTPRequestHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.deamon = True

    cwd = os.getcwd()

    def start():
        os.chdir(path)
        thread.start()
        print('starting server on port {}'.format(server.server_port))

    def stop():
        os.chdir(cwd)
        server.shutdown()
        server.socket.close()
        print('stopping server on port {}'.format(server.server_port))

    return start, stop

data_file_format = 'nquads'
shape_file_format = 'turtle'


def validate_data(data, root, shape_file_path):
    base_url = f"http://localhost:8000/{root}/"
    normalized = jsonld.normalize(data,
                                  {'algorithm': 'URDNA2015',
                                   'base': base_url,
                                   'format': 'application/n-quads'})
    conforms, v_graph, v_text = validate(normalized,
                                         shacl_graph=shape_file_path,
                                         data_graph_format=data_file_format,
                                         shacl_graph_format=shape_file_format,
                                         inference='rdfs', debug=False,
                                         serialize_report_graph=True)
    print(base_url + name, 'Conforms:', conforms)
    if not conforms:
        raise ValueError(v_text)

start, stop = simple_http_server(port=8000, path=os.getcwd())

start()
for root, dirs, files in os.walk('examples'):
    for name in files:
        full_file_name = os.path.join(root, name)
        with open(full_file_name) as json_file:
            try:
                data = json.load(json_file)
                if '@type' not in data:
                    raise ValueError(f"{full_file_name} missing @type")
                if data['@type'] == 'reproschema:Protocol':
                    shape_file_path = 'validation/ProtocolShape.ttl'
                elif data['@type'] == 'reproschema:Activity':
                    shape_file_path = 'validation/ActivityShape.ttl'
                elif data['@type'] == 'reproschema:Field':
                    shape_file_path = 'validation/FieldShape.ttl'
                validate_data(data, root, shape_file_path)
            except ValueError as e:
                print ("File '%s' has validation errors: \n %s" %(full_file_name, e))
                stop()
                raise
stop()