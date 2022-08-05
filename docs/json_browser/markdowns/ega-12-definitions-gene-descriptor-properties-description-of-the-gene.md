# Description of the gene Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_description
```

Free-text description of the gene, only to be used to provide additional context that would otherwise be impossible to add encoded in the schema. In other words, kindly refrain from providing alternative gene symbols in the description if they are not added likewise in the 'alternate\_gene\_symbols' property.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## gene\_description Type

`string` ([Description of the gene](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md))

## gene\_description Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## gene\_description Examples

```json
"In the used cells, locus of gene ... was modified at positions +23, where thymine was transitioned to cytosine (T-C)..."
```
