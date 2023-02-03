# Array containing metadata objects Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/objectArray
```

The array per se containing the list of metadata objects to be validated. For each type of metadata object (e.g. 'sample') its corresponding schema (e.g. '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#>') is applied conditionally based on the value of schemaDescriptor\[objectType] within each object. This way this array can contain any combination of metadata objects and each will be validated individually against the correct schemas. Notice how the 'schemaDescriptor' is a required node for the object-set to be used.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.object-set.json\*](../../../schemas/EGA.object-set.json "open original schema") |

## objectArray Type

an array of merged types ([Schemas being conditionally applied based on value of 'objectType' from 'schemaDescriptor' in each object.](ega-7-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-objecttype-from-schemadescriptor-in-each-object.md))

## objectArray Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
