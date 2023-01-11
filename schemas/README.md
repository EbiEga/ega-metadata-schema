# EGA Metadata Schemas
## Overview
In this directory you will find EGA's **metadata standards** or **_schemas_**: a coding system to catalogue information in structured descriptive records. These basically stablish **data elements** (_e.g._ what is ``Phenotype`` within a Sample) and the **rules** (_e.g._ if such ``Phenotype`` field can contain ``strings`` and ``integers`` or not) governing their usage to describe instances. There
is one schema file (_e.g._ ``EGA.experiment.json``) for every metadata object (_e.g._ ``experiment``), in addition to:
* The **common definitions** (``EGA.common-definitions.json``) contain shared nodes that other schemas can inherit. For instance, the node ``schemaDescriptor`` is uniformly used by all other schemas. In order to avoid creating redundant and repeated code in each of them, we create a common "definition" of ``schemaDescriptor`` within ``EGA.common-definitions.json`` that other schemas can
reference.
* An **object-set** (``EGA.object-set.json``) is, simply put, an array of EGA metadata objects. In other words, a compilation of individual metadata objects (e.g. 20 ``samples``, 2 ``assays`` and 1 ``experiment`` - any combination is valid) that are validated individually. The purpose of an object-set is to avoid the need of one file per each of the metadata objects (e.g. 100 sample JSON documents
 if we were to validate 100 sample objects), being able to group them all in a single file.

The current schemas are written in JavaScript Object Notation (**JSON**), providing both human- and machine-readable documentation. For further details regarding JSON-schemas visit [JSON-schema](https://json-schema.org/) and [Getting started](https://json-schema.org/learn/getting-started-step-by-step) (for an overview), or
[Understanding JSON schema](https://json-schema.org/understanding-json-schema/) (for a detailed explanation).

## JSON Schema Validation
In the folder [``json_validation_tests/``](../examples/json_validation_tests/) there are several ``json`` files which serve as **examples that are supposed to pass validation** (their name contains ``valid``). The current approach taken to validate JSON documents against their schemas is through EBI's tool [**Biovalidator**](https://github.com/elixir-europe/biovalidator)(``main`` branch). This tool is, in summary, AJV validation with extra custom keywords. This GitHub repository contains GH actions that perform validations onto the JSON test files. Check the actions [folder](../.github/workflows/) and [diagrams](../docs/gh_workflows/) for details on how local and remote validation is performed.

## Contributing to the schemas
**Your contributions are welcomed**! If you have any ideas on how our metadata standards should improve (e.g. new fields, terms, structure...) please go to our [**contribution documentation**](../docs/contributing.md).

## Planning to modify the schemas?
In case these schemas need to be modified, in this section you will find listed some details about the current approach that may ease the process:
* **Naming conventions**. Properties within the JSON schemas follow SWIFT naming conventions: they are named in ``lowerCammelCase`` format. For example, ``md5ChecksumPattern`` versus ``md5_checksum_pattern``.
* **Shared definitions**. All schemas share some fields (_e.g._ ``alias``) or patterns (_e.g._ checksum patterns) which can lead to duplicated code. In order to avoid it, we created an additional schema that corresponds to none of the EGA objects: ``EGA.common-definitions.json``. Within this file those repeated objects are specified for other schemas or objects to inherit. Based on the
**source and target** (being the same file or another) **of the reference**, we can differentiate: (1) same-file shared definitions; (2) different-file shared definitions.
    1. **Same-file shared definitions**. Objects within a JSON schema can be reused indefinitely. In order to do so, we stored them in the **``definitions`` anchor** (at the first level of the common schema), and then referenced them elsewhere using their relative JSON pointer (its path - _e.g._ ``"#/definitions/md5ChecksumPattern"``).
    See [Definitions](https://json-schema.org/understanding-json-schema/structuring.html#definitions) section for further details.
    As an **example**, take a look at how we defined ``md5ChecksumPattern`` within ``definitions`` of the ``EGA.common-definitions.json``:
    ````
    # Simplified common schema:
    {
        "$id": "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json",
        "definitions": {
            "md5ChecksumPattern": {
                "type": "string",
                "pattern": "^[0-9a-z](?:-?[0-9a-z]){31}$"
            }
        }
    }
   
    # When referencing the pattern:
    { "$ref": "#/definitions/md5ChecksumPattern" }
    ````

    2. **Different-file shared definitions**. The way these cross-file references are achieved is by using the IDs of the schemas (``$id`` within its first layer) and object's anchors (_e.g._ ``"EGASampleIdPattern``), which point to the objects within the files, turning them into references (``$ref`` wherever they are needed). References are resolved against the absolute URL identifiers of the 
    schemas. In other words, a relative reference ($ref; e.g. ``./EGA.common-definitions.json#...``) is resolved against the absolute identifier (``$id``; e.g. ``https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json``) of the referencing schema (in this example ``EGA.analysis.json``), transforming the relative reference into an absolute one (e.g. 
    ``https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#...``). See 
    [Structuring a complex schema](https://json-schema.org/understanding-json-schema/structuring.html) for further details. As an **example**, take a look at how we defined ``objectCoreId`` within ``definitions`` of the ``EGA.common-definitions.json`` and then referenced it within the ``EGA.experiment.json`` (notice how this time the JSON 
    pointer contains the whole ``$id`` instead of being relative):
    ````
    # Simplified common schema
    {
        "$id": "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json",
        "definitions": {
            "objectCoreId": {
                ...
            }
    }

    # Simplified experiment schema with a reference to the objectCoreId:
    {
        "$id": "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json",
        "properties": {
            "objectId": {
                "type": "object",
                "allOf": [
                    {
                        "$ref": "./EGA.common-definitions.json#/definitions/objectCoreId"
                    }
                ]
            }
        }
    }
    ````
