# Date of the sample collection Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/sampleCollectionDate
```

Date when the sample was collected (e.g. '2021-05-15'). If the protocols are too long, the date shall be the day the collection concluded.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sampleCollectionDate Type

`string` ([Date of the sample collection](ega-10-properties-sample-collection-descriptor-properties-date-of-the-sample-collection.md))

## sampleCollectionDate Constraints

**date**: the string must be a date string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## sampleCollectionDate Examples

```json
"2021-04-30"
```

```json
"2020-12-29"
```
