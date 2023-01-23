# EGA object-set metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate an object-set. A set or group of objects is defined as an array of individual objects (e.g. 'sample' or 'experiment'). The minimum length of the array is 1 (i.e. it has to contain at least one object). These objects can be of different nature, and are validated against their corresponding schemas based on the 'schemaDescriptor' node within each individual object, which specifies the schema against the individual object needs to be validated. Notice how this schema is missing the basic 'objectId' of other objects, since an object-set is not an object per se, it is just a compilation of objects. To put it simply, this object-set schema exists to avoid the need of 1 single file per each object: for a submission of 1000 samples we would require 1000 JSON files, each of them corresponding to one of the objects; whereas using an object-set allows us to fit all those objects together in a single file. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.object-set.json](../../../schemas/EGA.object-set.json "open original schema") |

## EGA object-set metadata schema Type

`object` ([EGA object-set metadata schema](ega-15.md))

# EGA object-set metadata schema Properties

| Property                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                         |
| :-------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectTitle](#objecttitle)             | `string` | Optional | cannot be null | [EGA object-set metadata schema](ega-15-properties-title-of-the-object-set.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/objectTitle")             |
| [objectDescription](#objectdescription) | `string` | Optional | cannot be null | [EGA object-set metadata schema](ega-15-properties-description-of-the-object-set.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/objectDescription") |
| [schemaDescriptor](#schemadescriptor)   | `object` | Optional | cannot be null | [EGA object-set metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/schemaDescriptor")             |
| [objectArray](#objectarray)             | `array`  | Required | cannot be null | [EGA object-set metadata schema](ega-15-properties-array-containing-metadata-objects.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/objectArray")   |

## objectTitle

Free-form title of the object-set. Used as a convenient way to identify different object-sets.

`objectTitle`

*   is optional

*   Type: `string` ([Title of the object-set](ega-15-properties-title-of-the-object-set.md))

*   cannot be null

*   defined in: [EGA object-set metadata schema](ega-15-properties-title-of-the-object-set.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/objectTitle")

### objectTitle Type

`string` ([Title of the object-set](ega-15-properties-title-of-the-object-set.md))

### objectTitle Examples

```json
"Example of Single Cell Sequencing"
```

```json
"myObjectSet_2"
```

## objectDescription

More extensive free-form description of the object-set. Used to provide context on why the items (i.e. individual objects) of the array are grouped together.

`objectDescription`

*   is optional

*   Type: `string` ([Description of the object-set](ega-15-properties-description-of-the-object-set.md))

*   cannot be null

*   defined in: [EGA object-set metadata schema](ega-15-properties-description-of-the-object-set.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/objectDescription")

### objectDescription Type

`string` ([Description of the object-set](ega-15-properties-description-of-the-object-set.md))

### objectDescription Examples

```json
"This object-set corresponds to a whole example of a Single Cell Sequencing submission, being grouped together and submitted together."
```

```json
"When submitting the previous object set, 4 samples were wrong and need to be re-submitted, and that's the purpose of this object-set."
```

## schemaDescriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schemaDescriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA object-set metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/schemaDescriptor")

### schemaDescriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## objectArray

The array per se containing the list of metadata objects to be validated. For each type of metadata object (e.g. 'sample') its corresponding schema (e.g. '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#>') is applied conditionally based on the value of schemaDescriptor\[objectType] within each object. This way this array can contain any combination of metadata objects and each will be validated individually against the correct schemas. Notice how the 'schemaDescriptor' is a required node for the object-set to be used.

`objectArray`

*   is required

*   Type: an array of merged types ([Schemas being conditionally applied based on value of 'objectType' from 'schemaDescriptor' in each object.](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-objecttype-from-schemadescriptor-in-each-object.md))

*   cannot be null

*   defined in: [EGA object-set metadata schema](ega-15-properties-array-containing-metadata-objects.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/objectArray")

### objectArray Type

an array of merged types ([Schemas being conditionally applied based on value of 'objectType' from 'schemaDescriptor' in each object.](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-objecttype-from-schemadescriptor-in-each-object.md))

### objectArray Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
