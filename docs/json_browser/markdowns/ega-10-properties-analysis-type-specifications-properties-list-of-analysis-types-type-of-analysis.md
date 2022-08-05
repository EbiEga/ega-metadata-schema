# Type of analysis Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysis_type_specifications/properties/analysis_types/items
```

Overall type of the analysis. Term chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## items Type

`string` ([Type of analysis](ega-10-properties-analysis-type-specifications-properties-list-of-analysis-types-type-of-analysis.md))

## items Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                          | Explanation |
| :----------------------------- | :---------- |
| `"sequence variation"`         |             |
| `"sequence alignment"`         |             |
| `"phenotype characterization"` |             |
| `"sequence annotation"`        |             |
| `"sequence assembly"`          |             |
| `"gene expression"`            |             |
