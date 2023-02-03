# Case vs control Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/caseVsControl
```

Property that specifies whether the sample is subject to the (usually altered) condition under study (i.e. case), or part of reference group (i.e. control). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## caseVsControl Type

`string` ([Case vs control](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-case-vs-control.md))

## caseVsControl Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation                                                                                                                        |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `"case"`           | \[PATO:0000460]: Abnormal - A quality inhering in a bearer by virtue of the bearer's deviation from normal or average.             |
| `"control"`        | \[PATO:0000461]: Normal - A quality inhering in a bearer by virtue of the bearer's exhibiting no deviation from normal or average. |
| `"not applicable"` | \[NCIT:C48660]: Determination of a case or control is not relevant for this condition under study.                                 |
