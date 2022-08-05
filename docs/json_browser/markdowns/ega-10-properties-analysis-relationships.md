# Analysis relationships Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysis_relationships
```

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. an analysis being linked to a Sample) the EGA.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## analysis\_relationships Type

an array of merged types ([Details](ega-10-properties-analysis-relationships-items.md))

## analysis\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
