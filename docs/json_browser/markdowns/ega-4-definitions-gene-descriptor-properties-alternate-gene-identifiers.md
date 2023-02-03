# Alternate gene identifiers Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneIdentifiers
```

Array of alternate identifiers for this gene. This array can be used to provide any other alternate gene identifiers that refer to a gene, including previously approved gene symbols, Ensembl identifiers, gene transcripts (e.g. 'ensembl:ENST00000423759'), etcetera.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## alternateGeneIdentifiers Type

`object[]` ([Alternate gene identifier item](ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers-alternate-gene-identifier-item.md))

## alternateGeneIdentifiers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
