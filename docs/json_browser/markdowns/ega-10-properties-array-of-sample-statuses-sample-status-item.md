# Sample status item Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items
```

One individual sample status of the array.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## items Type

`object` ([Sample status item](ega-10-properties-array-of-sample-statuses-sample-status-item.md))

# items Properties

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                           |
| :------------------------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [caseVsControl](#casevscontrol)             | `string` | Required | cannot be null | [EGA sample metadata schema](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-case-vs-control.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/caseVsControl")        |
| [conditionUnderStudy](#conditionunderstudy) | Merged   | Required | cannot be null | [EGA sample metadata schema](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy") |

## caseVsControl

Property that specifies whether the sample is subject to the (usually altered) condition under study (i.e. case), or part of reference group (i.e. control). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`caseVsControl`

*   is required

*   Type: `string` ([Case vs control](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-case-vs-control.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-case-vs-control.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/caseVsControl")

### caseVsControl Type

`string` ([Case vs control](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-case-vs-control.md))

### caseVsControl Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation                                                                                                                        |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `"case"`           | \[PATO:0000460]: Abnormal - A quality inhering in a bearer by virtue of the bearer's deviation from normal or average.             |
| `"control"`        | \[PATO:0000461]: Normal - A quality inhering in a bearer by virtue of the bearer's exhibiting no deviation from normal or average. |
| `"not applicable"` | \[NCIT:C48660]: Determination of a case or control is not relevant for this condition under study.                                 |

## conditionUnderStudy

One of the primary conditions under study (CUS). For example: treated with cisplatin, sample taken from a fibroadenoma, osteonecrosis, differences in sequencing workflows, etcetera. Notice that the sample may or may not be affected by this condition under study, belonging to the case or control groups respectively (defined by 'caseVsControl' for each CUS).

`conditionUnderStudy`

*   is required

*   Type: `object` ([Sample condition](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy")

### conditionUnderStudy Type

`object` ([Sample condition](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")
