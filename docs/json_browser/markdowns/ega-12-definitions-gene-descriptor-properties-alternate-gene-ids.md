# Alternate gene IDs Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/alternate_gene_ids
```

Array of alternate identifiers for this gene. For example, Ensemble identifiers for genes and its transcripts.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## alternate\_gene\_ids Type

`string[]` ([Alternate gene ID](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids-alternate-gene-id.md))

## alternate\_gene\_ids Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
