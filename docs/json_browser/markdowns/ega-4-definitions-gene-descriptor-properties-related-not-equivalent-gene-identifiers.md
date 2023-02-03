# Related (not equivalent) gene identifiers Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/relatedGeneIdentifiers
```

Array of related identifiers (e.g. termIds 'VGNC:97422', 'MGI:2385071', 'RGD:1305712' for gene ETF1). This field can be used to provide identifiers to resources representing related, but not equivalent gene identifiers. For example: paralog, analog or ortholog identifiers.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## relatedGeneIdentifiers Type

`object[]` ([Related gene identifier item](ega-4-definitions-gene-descriptor-properties-related-not-equivalent-gene-identifiers-related-gene-identifier-item.md))

## relatedGeneIdentifiers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
