# Study relationships Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_relationships
```

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. an ArrayExperiment being linked to a study) the EGA.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.study.json\*](../../../schemas/EGA.study.json "open original schema") |

## study\_relationships Type

an array of merged types ([Details](ega-18-properties-study-relationships-items.md))

## study\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
