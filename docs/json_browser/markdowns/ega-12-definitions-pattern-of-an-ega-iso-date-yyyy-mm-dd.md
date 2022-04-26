# Pattern of an EGA ISO date (YYYY-MM-DD) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sample_collection_date
```

ISO date (format YYYY-MM-DD - e.g. '2021-05-15') when the sample was collected. If the protocols are long enough, the date shall be the day the collection concluded.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sample\_collection\_date Type

`string` ([Pattern of an EGA ISO date (YYYY-MM-DD)](ega-12-definitions-pattern-of-an-ega-iso-date-yyyy-mm-dd.md))

## sample\_collection\_date Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-(0[0-9]|1[0-2])-([012][0-9]|3[01])$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-\(0%5B0-9%5D%7C1%5B0-2%5D\)-\(%5B012%5D%5B0-9%5D%7C3%5B01%5D\)%24 "try regular expression with regexr.com")

## sample\_collection\_date Examples

```json
"2021-04-30"
```
