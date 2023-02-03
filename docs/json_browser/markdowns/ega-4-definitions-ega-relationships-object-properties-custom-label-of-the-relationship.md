# Custom label of the relationship Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rLabel
```

Custom free-form label of the relationship, used to add extra details of the relationship if needed.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## rLabel Type

`string` ([Custom label of the relationship](ega-4-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md))

## rLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## rLabel Examples

```json
"Source individual is the third child of the target individual"
```

```json
"Grouped samples by colour of the medium"
```

```json
"Both samples are the same because of an error in the submission at..."
```
