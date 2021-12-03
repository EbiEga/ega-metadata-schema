# Type of the relationship's object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type
```

Type of the relationship's object, chosen from a list of CV (e.g. arrayExperiment, dataset, external_URL...). Both the source or target types can be: (1) the object tag of one of EGA’s object (e.g. file, sample…); (2) an 'external_accession'; (3) or an 'external_URL'.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## object_type Type

`string` ([Type of the relationship's object](ega-2-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

## object_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation |
| :--------------------- | :---------- |
| `"experiment"`         |             |
| `"study"`              |             |
| `"sample"`             |             |
| `"submission"`         |             |
| `"run"`                |             |
| `"dataset"`            |             |
| `"analysis"`           |             |
| `"policy"`             |             |
| `"DAC"`                |             |
| `"ArrayExperiment"`    |             |
| `"ArrayAssay"`         |             |
| `"external_accession"` |             |
| `"external_URL"`       |             |

## object_type Examples

```json
"sample"
```
