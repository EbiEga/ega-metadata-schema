# Check that protocol EGA ID (EGAO) is correct Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/object_id/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## 1 Type

unknown ([Check that protocol EGA ID (EGAO) is correct](ega-17-properties-objects-ids-block-allof-check-that-protocol-ega-id-egao-is-correct.md))

# 1 Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                     |
| :------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega\_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA protocol metadata schema](ega-12-definitions-pattern-of-an-ega-protocols-id-egao.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/object_id/allOf/1/properties/ega_accession") |

## ega\_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA protocol's ID (EGAO...)](ega-12-definitions-pattern-of-an-ega-protocols-id-egao.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-12-definitions-pattern-of-an-ega-protocols-id-egao.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/object_id/allOf/1/properties/ega_accession")

### ega\_accession Type

`string` ([Pattern of an EGA protocol's ID (EGAO...)](ega-12-definitions-pattern-of-an-ega-protocols-id-egao.md))

### ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAO[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAO%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega\_accession Examples

```json
"EGAO00001159483"
```