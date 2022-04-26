# Pattern of an EGA assay's ID (EGAR...) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/object_id/allOf/1/properties/ega_accession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## ega\_accession Type

`string` ([Pattern of an EGA assay's ID (EGAR...)](ega-11-properties-objects-ids-block-allof-check-that-assays-ega-id-egar-is-correct-properties-pattern-of-an-ega-assays-id-egar.md))

## ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAR[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAR%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## ega\_accession Examples

```json
"EGAR00001314547"
```
