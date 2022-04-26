# Check that DAC EGA ID (EGAC) is correct Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.DAC.json#/properties/object_id/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.DAC.json\*](../../../schemas/EGA.DAC.json "open original schema") |

## 1 Type

unknown ([Check that DAC EGA ID (EGAC) is correct](ega-8-properties-objects-ids-block-allof-check-that-dac-ega-id-egac-is-correct.md))

# 1 Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                   |
| :------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega\_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA DAC metadata schema](ega-8-properties-objects-ids-block-allof-check-that-dac-ega-id-egac-is-correct-properties-pattern-of-an-ega-dacs-id-egac.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.DAC.json#/properties/object_id/allOf/1/properties/ega_accession") |

## ega\_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA DAC's ID (EGAC...)](ega-8-properties-objects-ids-block-allof-check-that-dac-ega-id-egac-is-correct-properties-pattern-of-an-ega-dacs-id-egac.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-8-properties-objects-ids-block-allof-check-that-dac-ega-id-egac-is-correct-properties-pattern-of-an-ega-dacs-id-egac.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.DAC.json#/properties/object_id/allOf/1/properties/ega_accession")

### ega\_accession Type

`string` ([Pattern of an EGA DAC's ID (EGAC...)](ega-8-properties-objects-ids-block-allof-check-that-dac-ega-id-egac-is-correct-properties-pattern-of-an-ega-dacs-id-egac.md))

### ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAC[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAC%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega\_accession Examples

```json
"EGAC00001000908"
```
