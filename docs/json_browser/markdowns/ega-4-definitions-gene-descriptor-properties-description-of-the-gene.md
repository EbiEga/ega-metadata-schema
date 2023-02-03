# Description of the gene Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneDescription
```

Free-text description of the gene, only to be used to provide additional context that would otherwise be impossible to add encoded in the schema. In other words, kindly refrain from providing alternative gene identifiers in the description, when they could be added at 'alternateGeneIdentifiers'.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## geneDescription Type

`string` ([Description of the gene](ega-4-definitions-gene-descriptor-properties-description-of-the-gene.md))

## geneDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## geneDescription Examples

```json
"In the mutated cells, the only difference with the reference gene is that at locus ... position +23 was modified: thymine was transitioned to cytosine (T-C)..."
```
