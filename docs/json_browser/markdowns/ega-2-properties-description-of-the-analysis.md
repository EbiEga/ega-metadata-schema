# Description of the analysis Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectDescription
```

An in-depth description of the biological relevance and intent of the analysis, including its workflow.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## objectDescription Type

`string` ([Description of the analysis](ega-2-properties-description-of-the-analysis.md))

## objectDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## objectDescription Examples

```json
"The analysis was conducted with the objective of... ...and for that purpose we compared untreated controls against..."
```
