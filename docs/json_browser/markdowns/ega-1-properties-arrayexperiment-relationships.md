# ArrayExperiment relationships Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_experiment_relationships
```

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. an ArrayExperiment being linked to a Sample) the EGA. #! Using an empty item list but defining the relationship as possible additionalItems we create the correct constraint: anything but a relationship object is rejected, but EGA can add as many as required.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## array_experiment_relationships Type

`object[]` ([EGA Relationships object](ega-2-definitions-ega-relationships-object.md))

## array_experiment_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
