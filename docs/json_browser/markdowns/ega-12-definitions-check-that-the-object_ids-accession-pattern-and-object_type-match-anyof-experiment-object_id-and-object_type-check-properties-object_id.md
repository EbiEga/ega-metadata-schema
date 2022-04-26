# Untitled undefined type in EGA common metadata definitions Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/2/properties/object_id
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## object\_id Type

unknown

# object\_id Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                      |
| :------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega\_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-pattern-of-an-ega-experiments-id-egax.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/2/properties/object_id/properties/ega_accession") |

## ega\_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA experiment's ID (EGAX...)](ega-12-definitions-pattern-of-an-ega-experiments-id-egax.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-pattern-of-an-ega-experiments-id-egax.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/2/properties/object_id/properties/ega_accession")

### ega\_accession Type

`string` ([Pattern of an EGA experiment's ID (EGAX...)](ega-12-definitions-pattern-of-an-ega-experiments-id-egax.md))

### ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAX[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAX%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega\_accession Examples

```json
"EGAX00002189113"
```
