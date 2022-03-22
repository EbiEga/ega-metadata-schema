# Study-types array Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_types
```

List of study types. Contains specific keywords (e.g. 'COVID-19') as items that can be associated to the study, providing an overall view of its purpose.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.study.json*](../out/EGA.study.json "open original schema") |

## study_types Type

`string[]` ([Study type](ega-18-properties-study-types-array-study-type.md))

## study_types Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
