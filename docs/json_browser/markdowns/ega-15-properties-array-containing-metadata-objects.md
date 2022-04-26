# Array containing metadata objects Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.object-set.json#/properties/object_array
```

The array per se containing the list of metadata objects to be validated. For each type of metadata object (e.g. 'sample') its corresponding schema (e.g. '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#>') is applied conditionally based on the value of schema\_descriptor\[object\_type] within each object. This way this array can contain any combination of metadata objects and each will be validated individually against the correct schemas. Notice how the 'schema\_descriptor' is a required node for the object-set to be used.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.object-set.json\*](../../../schemas/EGA.object-set.json "open original schema") |

## object\_array Type

an array of merged types ([Schemas being conditionally applied based on value of 'object\_type' from 'schema\_descriptor' in each object.](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object.md))

## object\_array Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
