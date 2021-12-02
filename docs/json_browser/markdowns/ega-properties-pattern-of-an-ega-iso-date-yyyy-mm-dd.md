# Pattern of an EGA ISO date (YYYY-MM-DD) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_date
```

ISO date (format YYYY-MM-DD - e.g. '2021-05-15') when the ArrayAssay took place. If the protocols are long enough, the date shall be the day the ArrayAssay concluded.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.ArrayAssay.json*](../out/EGA.ArrayAssay.json "open original schema") |

## array_assay_date Type

`string` ([Pattern of an EGA ISO date (YYYY-MM-DD)](ega-properties-pattern-of-an-ega-iso-date-yyyy-mm-dd.md))

## array_assay_date Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(19|20)[0-9]{2}-(0[0-9]|1[0-2])-([012][0-9]|3[01])$
```

[try pattern](https://regexr.com/?expression=%5E\(19%7C20\)%5B0-9%5D%7B2%7D-\(0%5B0-9%5D%7C1%5B0-2%5D\)-\(%5B012%5D%5B0-9%5D%7C3%5B01%5D\)%24 "try regular expression with regexr.com")

## array_assay_date Examples

```json
"2021-04-30"
```
