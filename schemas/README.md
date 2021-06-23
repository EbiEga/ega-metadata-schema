# EGA Metadata Schemas
## Overview
In this directory you will find EGA's **metadata standards** or **_schemas_**: a coding system to catalogue information in structured descriptive records. These basically stablish **data elements** (_e.g._ what is ``Phenotype`` within a Sample) and the **rules** (_e.g._ if such ``Phenotype`` field can contain ``strings`` and ``integers`` or not) governing their usage to describe instances. There is one schema file (_e.g._ ``EGA.ArrayExperiment.json``) for every metadata object (_e.g._ ``ArrayExperiment``), in addition to the common schema (``EGA.common-definitions.json``). 

The current schemas are written in JavaScript Object Notation (**JSON**), providing both human- and machine-readable documentation. For further details regarding JSON-schemas visit [JSON-schema](https://json-schema.org/) and [Getting started](https://json-schema.org/learn/getting-started-step-by-step) (for an overview), or [Understanding JSON schema](https://json-schema.org/understanding-json-schema/) (for a detailed explanation). 

Furthermore, there is an additional folder, ``validation_tests``, in which there are several ``json`` files which serve as **examples that are supposed to pass validation** (if their name contains ``valid``) or **throw validation errors**. Besides, in that same directory there is a **jupyter notebook** that contains a small code block ready for you to use it to validate these example ``json`` files. 

## Planning to modify the schemas?
In case these schemas need to be modified, in this section you will find listed some details about the current approach that may ease the process:
* **Shared definitions**. All schemas share some fields (_e.g._ ``alias``) or patterns (_e.g._ checksum patterns) which can lead to duplicated code. In order to avoid it, we created an additional schema that corresponds to none of the EGA objects: ``EGA.common-definitions.json``. Within this file those repeated objects are specified for other schemas or objects to inherit. Based on the **source and target** (being the same file or another) **of the reference**, we can differenciate: (1) same-file shared definitions; (2) different-file shared definitions. 
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
