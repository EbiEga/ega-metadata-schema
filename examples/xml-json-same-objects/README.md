## XML and JSON documents for the same objects
___
In this folder you will find **examples of XML and JSON documents that correspond to the same objects**. Each format is validated against their respective schemas: [XSDs](https://github.com/enasequence/schema/tree/master/src/main/resources/uk/ac/ebi/ena/sra/schema) in the case of XMLs and [JSON Schemas](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas) in the case of JSONs. The aim 
of this folder is exclusively for you to see how XMLs and JSONs can be used to describe similar sets of data. For example, you will find files [``sample.json``](sample/sample.json) and [``sample.xml``](sample/sample.xml) that both contain the exact same information, but differently formatted. 

These documents are not representations of _good practice_ metadata standards. The metadata they contain is a modified version of XML files once submitted to EGA.

### Table of examples

| Object type* | JSON file | XML file |
|--------|--------|--------|
| policy | [``policy.json``](policy/policy.json) | [``policy.xml``](policy/policy.xml) |
| assay | [``sequencing_assay.json``](assay/sequencing_assay.json) | [``sequencing_run.xml``](assay/sequencing_run.xml) |
| sample |  [``sample.json``](sample/sample.json) | [``sample.xml``](sample/sample.xml) |

_\*Object types corresponding to the new metadata model._

### How to validate documents
Both JSON and XMLs validate against their own schemas, but you can see for yourself.
#### Validating XML files
There are two main ways to validate XMLs against ENA's standards: either through Webin validation or by direct validation with XSDs schemas.

1. **Webin validation**. You will need a Webin submission account to validate against ENA's system. If you do have one, you can use ``curl`` to send the validation request as follows (in this example validating the [``policy.xml``](policy/policy.xml) file). Use your account credentials for username and password.
```` bash
curl -u <username>:<password> -F "ACTION=VALIDATE" -F "POLICY=@policy/policy.xml" "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"
````
2. **XSD validation**. The easiest is to use star2xml's [validateXML.py](https://github.com/EGA-archive/star2xml#validatexmlpy) script. All information on how to validate the XML files is within its README. 

#### Validating JSON files
Within this same GH repository there are [instructions](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas#validation) on how to validate JSON documents against the new EGA's JSON schemas.

For example, to validate the [``policy.json``](policy/policy.json) file, one could execute the following command:
````bash
schema_name="policy"; json_doc="$schema_name.json"; ajv --strict=false --spec=draft2019 -s ../../schemas/EGA.$schema_name.json -d $schema_name/$json_doc -r "../../schemas/EGA.!($schema_name).json" -r "../../schemas/controlled_vocabulary_schemas/*"
````