# Loci of the targeted genomic feature Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/targeted_loci
```

Array of items that unambiguously define the loci of targeted genomic features in the experiment. For example, if the experiment aim was to detect variants in the human gene TAF1 and TP53, their identifiers will be expected in two items of this array.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## targeted\_loci Type

`object[]` ([Locus identifier](ega-12-definitions-locus-identifier.md))

## targeted\_loci Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
