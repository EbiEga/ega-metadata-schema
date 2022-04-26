# Title of the assay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/object_title
```

An informative assay title that should serve as an overview of the assay and differentiate it from others. This short text can be used to call out assay records in searches or in displays.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## object\_title Type

`string` ([Title of the assay](ega-11-properties-title-of-the-assay.md))

## object\_title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## object\_title Examples

```json
"Ilumina sequencing assay 3409 - Cancer genomics"
```
