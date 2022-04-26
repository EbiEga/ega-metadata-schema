# Check that policy EGA ID (EGAP) is correct Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.policy.json#/properties/object_id/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.policy.json\*](../../../schemas/EGA.policy.json "open original schema") |

## 1 Type

unknown ([Check that policy EGA ID (EGAP) is correct](ega-16-properties-objects-ids-block-allof-check-that-policy-ega-id-egap-is-correct.md))

# 1 Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                     |
| :------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega\_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA policy metadata schema](ega-12-definitions-pattern-of-an-ega-policys-id-egap.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.policy.json#/properties/object_id/allOf/1/properties/ega_accession") |

## ega\_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA policy's ID (EGAP...)](ega-12-definitions-pattern-of-an-ega-policys-id-egap.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-12-definitions-pattern-of-an-ega-policys-id-egap.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.policy.json#/properties/object_id/allOf/1/properties/ega_accession")

### ega\_accession Type

`string` ([Pattern of an EGA policy's ID (EGAP...)](ega-12-definitions-pattern-of-an-ega-policys-id-egap.md))

### ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAP[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAP%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega\_accession Examples

```json
"EGAP00001001831"
```
