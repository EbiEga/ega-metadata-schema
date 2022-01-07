# EGA Metadata Schemas
## Overview
In this directory you will find EGA's **metadata standards** or **_schemas_**: a coding system to catalogue information in structured descriptive records. These basically stablish **data elements** (_e.g._ what is ``Phenotype`` within a Sample) and the **rules** (_e.g._ if such ``Phenotype`` field can contain ``strings`` and ``integers`` or not) governing their usage to describe instances. There is one schema file (_e.g._ ``EGA.ArrayExperiment.json``) for every metadata object (_e.g._ ``ArrayExperiment``), in addition to the common definitions (``EGA.common-definitions.json``) and object-set (``EGA.object-set.json``) schemas:
* The **common definitions** contain shared nodes that other schemas can inherit. For instance, the node ``schema_descriptor`` is uniformly used by all other schemas. In order to avoid creating redundant and repeated code in each of them, we create a common "definition" of ``schema_descriptor`` within ``EGA.common-definitions.json`` that other schemas can refer to. 
* An **object-set** is, simply put, an array of EGA metadata objects. In other words, a compilation of individual metadata objects (e.g. 20 ``samples``, 2 ``ArrayAssays`` and 1 ``ArrayExperiments`` - any combination is valid) that are validated individually. The purpose of an object-set is to avoid the need of one file per each of the metadata objects (e.g. 100 sample JSON documents if we were to validate 100 sample objects), being able to group them all in a single file.

The current schemas are written in JavaScript Object Notation (**JSON**), providing both human- and machine-readable documentation. For further details regarding JSON-schemas visit [JSON-schema](https://json-schema.org/) and [Getting started](https://json-schema.org/learn/getting-started-step-by-step) (for an overview), or [Understanding JSON schema](https://json-schema.org/understanding-json-schema/) (for a detailed explanation). 

## Validation
There is an additional folder, ``validation_tests``, in which there are several ``json`` files which serve as **examples that are supposed to pass validation** (if their name contains ``valid``) or **throw validation errors**. The current approach taken to validate JSON documents against their schemas is through **AJV command line interface** version ([AJV CLI](https://github.com/ajv-validator/ajv-cli#ajv-cli)). An validation example through the CLI is the following:

````bash
schema_name="object-set"
json_doc="object-set-valid-1.json"
ajv --strict=false --spec=draft2019 -s schemas/EGA.$schema_name.json -d schemas/validation_tests/$json_doc -r "schemas/EGA.!($schema_name).json"
````
Things to notice:
* Given how we use custom keywords (e.g. ``meta:version``) we switch off the **strict mode** of AJV. One needs to be careful when editing the schemas to use another type of linter, to avoid malformed keywords not being considered during validation.
* The **draft** we use for our schemas currently is the [**2019-09**](https://json-schema.org/draft/2019-09/release-notes.html).
* While the basic JSON document is validated against a single schema, in the example ``schemas/EGA.object-set.json`` (defined by ``-s``), there are references within said schema to other files (e.g. ``schema_descriptor`` from the common definitions). For this references to be resolved AJV requires the file paths of all other schemas that may be used as references (defined by [``-r``](https://github.com/ajv-validator/ajv-cli#-r---referenced-schemas)). To give all other schemas, except the one being given as the main schema, we use [glob patterns](https://github.com/isaacs/node-glob#glob-primer): ``"schemas/EGA.!($schema_name).json"`` translates into anything but the schema containing ``$schema_name``. 

## Planning to modify the schemas?
In case these schemas need to be modified, in this section you will find listed some details about the current approach that may ease the process:
* **Shared definitions**. All schemas share some fields (_e.g._ ``alias``) or patterns (_e.g._ checksum patterns) which can lead to duplicated code. In order to avoid it, we created an additional schema that corresponds to none of the EGA objects: ``EGA.common-definitions.json``. Within this file those repeated objects are specified for other schemas or objects to inherit. Based on the **source and target** (being the same file or another) **of the reference**, we can differentiate: (1) same-file shared definitions; (2) different-file shared definitions. 
    1. **Same-file shared definitions**. Objects within a JSON schema can be reused indefinitely. In order to do so, we stored them in the **``definitions`` anchor** (at the first level of the common schema), and then referenced them elsewhere using their relative JSON pointer (its path - _e.g._ ``"#/definitions/md5-checksum-pattern"``) . See [Definitions](https://json-schema.org/understanding-json-schema/structuring.html#definitions) section for further details. 
    As an **example**, take a look at how we defined ``md5-checksum-pattern`` within ``definitions`` of the ``EGA.common-definitions.json``:
    ````
    # Simplified common schema:
    {
        "$id": "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json",
        "definitions": {
            "md5-checksum-pattern": {
                "type": "string",
                "pattern": "^[0-9a-z](?:-?[0-9a-z]){31}$"
            }
        }
    }
    
    # When referencing the pattern:
    { "$ref": "#/definitions/md5-checksum-pattern" }
    ````

    2. **Different-file shared definitions**. The way these cross-file references are achieved is by using the IDs of the schemas (``$id`` within its first layer) and object's anchors (_e.g._ ``"EGA-sample-id-pattern``), which point to the objects within the files, turning them into references (``$ref`` wherever they are needed). See [Structuring a complex schema](https://json-schema.org/understanding-json-schema/structuring.html) for further details. As an **example**, take a look at how we defined ``object_coreIDs`` within ``definitions`` of the ``EGA.common-definitions.json`` and then referenced it within the ``ArrayExperiment.json`` (notice how this time the JSON pointer contains the whole ``$id`` instead of being relative):
    ````
    # Simplified common schema
    {
        "$id": "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json",
        "definitions": {
            "object_coreIDs": {
                ...
            }
    }

    # Simplified ArrayExperiment schema with a reference to the object_coreIDs:
    {
        "$id": "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json",
        "properties": {
            "object_ids": {
                "type": "object",
                "allOf": [
                    {
                        "$ref": "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_coreIDs"
                    }
                ]
            }
        }
    }
    ````
