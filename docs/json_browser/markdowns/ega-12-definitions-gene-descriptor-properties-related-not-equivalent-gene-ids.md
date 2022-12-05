# Related (not equivalent) gene IDs Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneExternalReferences
```

Array of related identifiers. This field can be used to provide identifiers to alternative resources representing related, but not equivalent concepts, for example gene paralog, analog or ortholog IDs.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## geneExternalReferences Type

`string[]` ([Related gene ID](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids-related-gene-id.md))

## geneExternalReferences Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
