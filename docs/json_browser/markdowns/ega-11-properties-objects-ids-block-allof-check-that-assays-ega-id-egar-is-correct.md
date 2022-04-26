# Check that assay's EGA ID (EGAR) is correct Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/object_id/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## 1 Type

unknown ([Check that assay's EGA ID (EGAR) is correct](ega-11-properties-objects-ids-block-allof-check-that-assays-ega-id-egar-is-correct.md))

# 1 Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                             |
| :------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega\_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-objects-ids-block-allof-check-that-assays-ega-id-egar-is-correct-properties-pattern-of-an-ega-assays-id-egar.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/object_id/allOf/1/properties/ega_accession") |

## ega\_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA assay's ID (EGAR...)](ega-11-properties-objects-ids-block-allof-check-that-assays-ega-id-egar-is-correct-properties-pattern-of-an-ega-assays-id-egar.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-objects-ids-block-allof-check-that-assays-ega-id-egar-is-correct-properties-pattern-of-an-ega-assays-id-egar.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/object_id/allOf/1/properties/ega_accession")

### ega\_accession Type

`string` ([Pattern of an EGA assay's ID (EGAR...)](ega-11-properties-objects-ids-block-allof-check-that-assays-ega-id-egar-is-correct-properties-pattern-of-an-ega-assays-id-egar.md))

### ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAR[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAR%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega\_accession Examples

```json
"EGAR00001314547"
```
