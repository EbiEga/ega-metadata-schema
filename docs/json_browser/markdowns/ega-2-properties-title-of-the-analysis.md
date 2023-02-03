# Title of the analysis Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectTitle
```

An informative analysis title that should serve as an overview of the analysis, including: performed analysis, samples, purpose... (e.g. 'Variant calling analysis of tumor repressed cells'). This short text can be used to call out analyses records in searches or in displays.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## objectTitle Type

`string` ([Title of the analysis](ega-2-properties-title-of-the-analysis.md))

## objectTitle Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## objectTitle Examples

```json
"Variant calling analysis of tumor repressed cells"
```
