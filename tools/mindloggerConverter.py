from nested_lookup import nested_lookup, get_all_keys
import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

schemaMap = {
	"_id": "@id",
	"_modelType": "@type",
	"description": "schema:description",
	"meta.abbreviation": "skos:altLabel",
	"meta.description": "skos:prefLabel",
	# "meta['notification']": "ui.nitification",
	# "meta['screens']": "ui.order",
	# "name": "Physical Health",
	# "parentCollection": "folder",
	# "parentId": "5bd88558336da80de9145b75",
	# "public": true,
	# "publicFlags": [],
	# "size": 0,
	# "updated": "2018-11-16T16:07:47.309000+00:00"

}


mindloggerapiUrl = 'https://api.mindlogger.info/api/v1'
url = 'https://api.mindlogger.info/api/v1/folder/5bd88558336da80de9145b76'

form_schema = requests.get(url).json()
#pp.pprint(form_schema.keys())
items = form_schema['meta']['screens']

form_dict = {}
for key, value in form_schema.items():
	if key in schemaMap:
		mapped_key = schemaMap[key]
		form_dict[mapped_key] = value
	# elif type(value) is dict:
	# 	for k, v in value.items():
	# 		if k in schemaMap:
	# 			form_dict[schemaMap[k]] = v

meta_form_info = nested_lookup(
	key='meta',
	document=form_schema
)

for key, value in meta_form_info[0].items():
	if ('meta.'+key) in schemaMap:
		mapped_key = schemaMap['meta.'+key]
		form_dict[mapped_key] = value

pp.pprint(form_dict)


for item in items:
	# pp.pprint(item['@id'])
	itemUrl = mindloggerapiUrl + '/' + item['@id']
	# print(itemUrl)
	i = requests.get(itemUrl).json()
# pp.pprint(i)

