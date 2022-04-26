# Check that individual EGA ID (EGAI) is correct Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/object_id/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## 1 Type

unknown ([Check that individual EGA ID (EGAI) is correct](ega-14-properties-objects-ids-block-allof-check-that-individual-ega-id-egai-is-correct.md))

# 1 Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                 |
| :------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega\_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA individual metadata schema](ega-12-definitions-pattern-of-an-ega-individuals-id-egai.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/object_id/allOf/1/properties/ega_accession") |

## ega\_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA Individual's ID (EGAI...)](ega-12-definitions-pattern-of-an-ega-individuals-id-egai.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-12-definitions-pattern-of-an-ega-individuals-id-egai.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/object_id/allOf/1/properties/ega_accession")

### ega\_accession Type

`string` ([Pattern of an EGA Individual's ID (EGAI...)](ega-12-definitions-pattern-of-an-ega-individuals-id-egai.md))

### ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAI[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAI%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega\_accession Examples

```json
"EGAI00001159712"
```
