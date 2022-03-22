# Loci of the targeted genomic feature Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/targeted_loci
```

Array of items that unambiguously define the loci of targeted genomic features in the analysis. For example, if the aim of the analysis was to detect variants in the human gene TAF1 and TP53, their identifiers will be expected in two items of this array.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.analysis.json*](../out/EGA.analysis.json "open original schema") |

## targeted_loci Type

`object[]` ([Locus identifier](ega-12-definitions-locus-identifier.md))

## targeted_loci Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
