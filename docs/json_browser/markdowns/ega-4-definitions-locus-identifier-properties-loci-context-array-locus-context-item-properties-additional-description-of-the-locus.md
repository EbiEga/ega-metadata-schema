# Additional description of the locus Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor/items/properties/locusAdditionalDescription
```

Optional free-text description of the locus to add any additional context.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## locusAdditionalDescription Type

`string` ([Additional description of the locus](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item-properties-additional-description-of-the-locus.md))

## locusAdditionalDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## locusAdditionalDescription Examples

```json
"Targeted locus number 1 out of 3 possible loci that our experimental procedure aimed at."
```

```json
"The locus corresponds to a variant version of the defined gene, only existing in patients with X disease."
```
