# Experimental design of the ArrayExperiment - ID Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/experimental_design/properties/experimental_design_id
```

The human readable ID (e.g. RNA stability design), chosen from a list of CVs, of the experimental design defining the ArrayExperiment.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## experimental_design_id Type

`string` ([Experimental design of the ArrayExperiment - ID](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426-properties-experimental-design-of-the-arrayexperiment---id.md))

## experimental_design_id Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                     | Explanation |
| :---------------------------------------- | :---------- |
| `"RNA stability design"`                  |             |
| `"binding site identification design"`    |             |
| `"case control design"`                   |             |
| `"cell component comparison design"`      |             |
| `"cell cycle design"`                     |             |
| `"cell type comparison design"`           |             |
| `"cellular modification design"`          |             |
| `"clinical history design"`               |             |
| `"compound treatment design"`             |             |
| `"cross sectional design"`                |             |
| `"development or differentiation design"` |             |
| `"disease state design"`                  |             |
| `"dose response design"`                  |             |
| `"twin design"`                           |             |
| `"genetic modification design"`           |             |
| `"genotype design"`                       |             |
| `"growth condition design"`               |             |
| `"imprinting design"`                     |             |
| `"injury design"`                         |             |
| `"innate behavior design"`                |             |
| `"organism part comparison design"`       |             |
| `"organism status design"`                |             |
| `"pathogenicity design"`                  |             |
| `"population based design"`               |             |
| `"sex design"`                            |             |
| `"species design"`                        |             |
| `"stimulus or stress design"`             |             |
| `"strain or line design"`                 |             |
| `"time series design"`                    |             |

## experimental_design_id Examples

```json
"RNA stability design"
```
