# Properties of Field schema
|             Property              |                                       Description                                       |      Domain       |                     Range                     |
|-----------------------------------|-----------------------------------------------------------------------------------------|-------------------|-----------------------------------------------|
| skos:prefLabel                    | Indicates the label of the Field.                                                       | reproschema:Field | schema:Text                                   |
| schema:description                | A description of the item.                                                              | reproschema:Field | schema:Text                                   |
| schema:schemaVersion              | Indicates (by URL or string) a particular version of the reproschema.                   | reproschema:Field | ['schema:Text', 'schema:URL']                 |
| schema:version                    | Indicates (by URL or string) a particular version of the item.                          | reproschema:Field | ['schema:Text', 'schema:URL']                 |
| reproterms:preamble               | The preamble for the Field item.                                                        | reproschema:Field | schema:Text                                   |
| schema:question                   | The text displayed for the item.                                                        | reproschema:Field | schema:Text                                   |
| reproterms:inputType              | An element to describe the input type of the Field item.                                | reproschema:Field | schema:text                                   |
| reproterms:readOnly               | An element( by Boolean) to indicate a readOnly Field.                                   | reproschema:Field | schema:Boolean                                |
| schema:isPartOf                   | Indicates an item that this item is part of.                                            | reproterms:Field  | ['reproschema:Activity', 'schema:URL']        |
| reproterms:responseOptions        | An element (object or by URL)to describe the properties of response of the Field item.  | reproschema:Field | ['reproschema:ResponseOptions', 'schema:URL'] |
| http://schema.org/associatedMedia | A media object that encodes this CreativeWork. This property is a synonym for encoding. | reproschema:Field | schema:MediaObject                            |
