# Check that ArrayAssay EGA ID (EGAA) is correct Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/object_id/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.ArrayAssay.json*](../out/EGA.ArrayAssay.json "open original schema") |

## 1 Type

unknown ([Check that ArrayAssay EGA ID (EGAA) is correct](ega-properties-objects-ids-block-allof-check-that-arrayassay-ega-id-egaa-is-correct.md))

# 1 Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                             |
| :------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA ArrayAssay metadata schema](ega-properties-objects-ids-block-allof-check-that-arrayassay-ega-id-egaa-is-correct-properties-pattern-of-an-ega-arrayassays-id-egaa.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/object_id/allOf/1/properties/ega_accession") |

## ega_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA ArrayAssay's ID (EGAA...)](ega-properties-objects-ids-block-allof-check-that-arrayassay-ega-id-egaa-is-correct-properties-pattern-of-an-ega-arrayassays-id-egaa.md))

*   cannot be null

*   defined in: [EGA ArrayAssay metadata schema](ega-properties-objects-ids-block-allof-check-that-arrayassay-ega-id-egaa-is-correct-properties-pattern-of-an-ega-arrayassays-id-egaa.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/object_id/allOf/1/properties/ega_accession")

### ega_accession Type

`string` ([Pattern of an EGA ArrayAssay's ID (EGAA...)](ega-properties-objects-ids-block-allof-check-that-arrayassay-ega-id-egaa-is-correct-properties-pattern-of-an-ega-arrayassays-id-egaa.md))

### ega_accession Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^EGAA[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAA%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega_accession Examples

```json
"EGAA00002189113"
```
