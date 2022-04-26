# EGA object-set metadata schema Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.object-set.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate an object set. A set or group of objects is defined as an array of individual objects (e.g. 'sample' or 'experiment'). The minimum length of the array is 1 (i.e. it has to contain at least one object). These objects can be of different nature, and are validated against their corresponding schemas based on the 'schema\_descriptor' node within each individual object, which specifies the schema against the individual object needs to be validated. To put it simply, this object-set schema exists to avoid the need of 1 single file per each object: for a submission of 1000 samples we would require 1000 JSON files, each of them corresponding to one of the objects; whereas using an object-set allows us to fit all those objects together in a single file. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.object-set.json](../../../schemas/EGA.object-set.json "open original schema") |

## EGA object-set metadata schema Type

`object` ([EGA object-set metadata schema](ega-15.md))

# EGA object-set metadata schema Properties

| Property                                 | Type     | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :--------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [schema\_descriptor](#schema_descriptor) | `object` | Optional | cannot be null | [EGA object-set metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.object-set.json#/properties/schema_descriptor")           |
| [object\_array](#object_array)           | `array`  | Required | cannot be null | [EGA object-set metadata schema](ega-15-properties-array-containing-metadata-objects.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.object-set.json#/properties/object_array") |

## schema\_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA object-set metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.object-set.json#/properties/schema_descriptor")

### schema\_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## object\_array

The array per se containing the list of metadata objects to be validated. For each type of metadata object (e.g. 'sample') its corresponding schema (e.g. '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#>') is applied conditionally based on the value of schema\_descriptor\[object\_type] within each object. This way this array can contain any combination of metadata objects and each will be validated individually against the correct schemas. Notice how the 'schema\_descriptor' is a required node for the object-set to be used.

`object_array`

*   is required

*   Type: an array of merged types ([Schemas being conditionally applied based on value of 'object\_type' from 'schema\_descriptor' in each object.](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object.md))

*   cannot be null

*   defined in: [EGA object-set metadata schema](ega-15-properties-array-containing-metadata-objects.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.object-set.json#/properties/object_array")

### object\_array Type

an array of merged types ([Schemas being conditionally applied based on value of 'object\_type' from 'schema\_descriptor' in each object.](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object.md))

### object\_array Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
