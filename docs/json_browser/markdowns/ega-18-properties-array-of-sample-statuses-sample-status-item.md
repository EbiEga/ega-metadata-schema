# Sample status item Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_status/items
```

One individual sample status of the array.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## items Type

`object` ([Sample status item](ega-18-properties-array-of-sample-statuses-sample-status-item.md))

# items Properties

| Property                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                              |
| :------------------------------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [case\_vs\_control](#case_vs_control)             | `string` | Required | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-case-vs-control.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_status/items/properties/case_vs_control")        |
| [condition\_under\_study](#condition_under_study) | `object` | Required | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_status/items/properties/condition_under_study") |

## case\_vs\_control

Property that specifies whether the sample is subject to the (usually altered) condition under study (i.e. case), or part of reference group (i.e. control). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`case_vs_control`

*   is required

*   Type: `string` ([Case vs control](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-case-vs-control.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-case-vs-control.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_status/items/properties/case_vs_control")

### case\_vs\_control Type

`string` ([Case vs control](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-case-vs-control.md))

### case\_vs\_control Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation                                                                                                                        |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `"case"`    | \[PATO:0000460]: Abnormal - A quality inhering in a bearer by virtue of the bearer's deviation from normal or average.             |
| `"control"` | \[PATO:0000461]: Normal - A quality inhering in a bearer by virtue of the bearer's exhibiting no deviation from normal or average. |

## condition\_under\_study

One of the primary conditions under study (CUS). Notice that the sample may or may not be affected by this condition under study, belonging to the case or control groups respectively.

`condition_under_study`

*   is required

*   Type: `object` ([Sample condition](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_status/items/properties/condition_under_study")

### condition\_under\_study Type

`object` ([Sample condition](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md))
