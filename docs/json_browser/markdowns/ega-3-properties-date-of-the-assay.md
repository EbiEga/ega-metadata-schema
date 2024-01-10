# Date of the assay Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayDate
```

Date when the sequencing assay took place (e.g. '2021-05-15'). If the protocols are too long, the date shall be the day the assay concluded.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## assayDate Type

`string` ([Date of the assay](ega-3-properties-date-of-the-assay.md))

## assayDate Constraints

**date**: the string must be a date string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## assayDate Examples

```json
"2021-04-30"
```

```json
"2020-12-29"
```
