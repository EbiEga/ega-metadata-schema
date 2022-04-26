# Check that sample EGA ID (EGAN) pattern is correct Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 1 Type

unknown ([Check that sample EGA ID (EGAN) pattern is correct](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block-allof-check-that-sample-ega-id-egan-pattern-is-correct.md))

# 1 Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                           |
| :------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega\_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-pattern-of-an-ega-samples-id-egan.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id/allOf/1/properties/ega_accession") |

## ega\_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA sample's ID (EGAN...)](ega-12-definitions-pattern-of-an-ega-samples-id-egan.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-pattern-of-an-ega-samples-id-egan.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id/allOf/1/properties/ega_accession")

### ega\_accession Type

`string` ([Pattern of an EGA sample's ID (EGAN...)](ega-12-definitions-pattern-of-an-ega-samples-id-egan.md))

### ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAN[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAN%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega\_accession Examples

```json
"EGAN00003245489"
```
