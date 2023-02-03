# Loci of the targeted genomic feature Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/targetedLoci
```

Array of items that unambiguously define the loci of targeted genomic features in the analysis. For example, if the aim of the analysis was to detect variants in the human gene TAF1 and TP53, their identifiers will be expected in two items of this array.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## targetedLoci Type

`object[]` ([Locus identifier](ega-4-definitions-locus-identifier.md))

## targetedLoci Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
