import json
from pytablewriter import MarkdownTableWriter

a_writer = MarkdownTableWriter()
a_writer.table_name = "Properties of Activity schema"
a_writer.headers = ["Property", "Description", "Domain", "Range"]

p_writer = MarkdownTableWriter()
p_writer.table_name = "Properties of Protocol schema"
p_writer.headers = ["Property", "Description", "Domain", "Range"]

writer = MarkdownTableWriter()
writer.table_name = "Properties of Field schema"
writer.headers = ["Property", "Description", "Domain", "Range"]

protocol_properties = []
activity_properties = []
field_properties = []

# Opening JSON-ld file
protocol_file = open('./schemas/Protocol')
activity_file = open('./schemas/Activity')
field_file = open('./schemas/Field')

# returns JSON object as
# a dictionary
protocol_data = json.load(protocol_file)
act_data = json.load(activity_file)
field_data = json.load(field_file)

for i in protocol_data['@graph']:
    if i['@type'] == 'rdf:Property':
        each_property = [i['@id'], i['rdfs:comment']]
        if isinstance(i['schema:domainIncludes'], list):
            domain = [x['@id'] for x in i['schema:domainIncludes']]
            each_property.append(domain)
        else:
            each_property.append(i['schema:domainIncludes']['@id'])

        if isinstance(i['schema:rangeIncludes'], list):
            range = [x['@id'] for x in i['schema:rangeIncludes']]
            each_property.append(range)
        else:
            each_property.append(i['schema:rangeIncludes']['@id'])
        protocol_properties.append(each_property)

for i in act_data['@graph']:
    if i['@type'] == 'rdf:Property':
        each_property = [i['@id'], i['rdfs:comment']]
        if isinstance(i['schema:domainIncludes'], list):
            domain = [x['@id'] for x in i['schema:domainIncludes']]
            each_property.append(domain)
            # property_object['domain'] = [x['@id'] for x in i['schema:domainIncludes']]
        else:
            each_property.append(i['schema:domainIncludes']['@id'])
            # property_object['domain'] = i['schema:domainIncludes']['@id']

        if isinstance(i['schema:rangeIncludes'], list):
            range = [x['@id'] for x in i['schema:rangeIncludes']]
            each_property.append(range)
            # property_object['range'] = [x['@id'] for x in i['schema:rangeIncludes']]
        else:
            each_property.append(i['schema:rangeIncludes']['@id'])
            # property_object['range'] = i['schema:rangeIncludes']['@id']
        activity_properties.append(each_property)

for i in field_data['@graph']:
    if i['@type'] == 'rdf:Property':
        each_property = [i['@id'], i['rdfs:comment']]
        if isinstance(i['schema:domainIncludes'], list):
            domain = [x['@id'] for x in i['schema:domainIncludes']]
            each_property.append(domain)
        else:
            each_property.append(i['schema:domainIncludes']['@id'])

        if isinstance(i['schema:rangeIncludes'], list):
            range = [x['@id'] for x in i['schema:rangeIncludes']]
            each_property.append(range)
        else:
            each_property.append(i['schema:rangeIncludes']['@id'])
            # property_object['range'] = i['schema:rangeIncludes']['@id']
        field_properties.append(each_property)

p_writer.value_matrix = protocol_properties
p_writer.margin = 1
p_writer.write_table()

a_writer.value_matrix = activity_properties
a_writer.margin = 1
a_writer.write_table()

writer.value_matrix = field_properties
writer.margin = 1  # add a whitespace for both sides of each cell
writer.write_table()

# Closing file
protocol_file.close()
activity_file.close()
field_file.close()





