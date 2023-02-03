# Pattern of EGA ISO 8601 date Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/sampleCollectionDate/allOf/0
```

Regular expression to check the syntax of a date following 'ISO 8601 date' format. Notice that the Time (denoted by 'T...') is optional. So is the time zone, specified at the end of the string (e.g. 'Z', '+01:00'...). See more detail at '<https://regexpattern.com/iso-8601-dates-times/>'.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## 0 Type

`string` ([Pattern of EGA ISO 8601 date](ega-4-definitions-pattern-of-ega-iso-8601-date.md))

## 0 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])(T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?)?$
```

[try pattern](https://regexr.com/?expression=%5E\(-%3F\(%3F%3A%5B1-9%5D%5B0-9%5D*\)%3F%5B0-9%5D%7B4%7D\)-\(1%5B0-2%5D%7C0%5B1-9%5D\)-\(3%5B01%5D%7C0%5B1-9%5D%7C%5B12%5D%5B0-9%5D\)\(T\(2%5B0-3%5D%7C%5B01%5D%5B0-9%5D\)%3A\(%5B0-5%5D%5B0-9%5D\)%3A\(%5B0-5%5D%5B0-9%5D\)\(%5C.%5B0-9%5D%2B\)%3F\(Z%7C%5B%2B-%5D\(%3F%3A2%5B0-3%5D%7C%5B01%5D%5B0-9%5D\)%3A%5B0-5%5D%5B0-9%5D\)%3F\)%3F%24 "try regular expression with regexr.com")

## 0 Examples

```json
"2021-04-30"
```

```json
"2020-12-29T19:30:45.123Z"
```

```json
"2020-12-29"
```

```json
"2020-12-29T19:30:45"
```

```json
"2021-10-13T04:13:00+01:00"
```

```json
"2021-10-13T12:13:00-08:00"
```

```json
"2021-10-13T12:13:00"
```
