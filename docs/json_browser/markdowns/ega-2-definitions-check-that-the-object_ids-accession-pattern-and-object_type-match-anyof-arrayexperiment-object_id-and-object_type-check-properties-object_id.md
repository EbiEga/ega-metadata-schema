# Untitled undefined type in EGA common metadata definitions v0.0.1 Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/11/properties/object_id
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## object_id Type

unknown

# object_id Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                  |
| :------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA common metadata definitions v0.0.1](ega-2-definitions-pattern-of-an-ega-arrayexperiments-id-egae.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/11/properties/object_id/properties/ega_accession") |

## ega_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA ArrayExperiment's ID (EGAE...)](ega-2-definitions-pattern-of-an-ega-arrayexperiments-id-egae.md))

*   cannot be null

*   defined in: [EGA common metadata definitions v0.0.1](ega-2-definitions-pattern-of-an-ega-arrayexperiments-id-egae.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/11/properties/object_id/properties/ega_accession")

### ega_accession Type

`string` ([Pattern of an EGA ArrayExperiment's ID (EGAE...)](ega-2-definitions-pattern-of-an-ega-arrayexperiments-id-egae.md))

### ega_accession Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^EGAE[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAE%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega_accession Examples

```json
"EGAE00001004508"
```
