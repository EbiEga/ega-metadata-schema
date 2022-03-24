# Enumeration of design keywords Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_designs/items
```

An object containing the enumeration of multiple study-design keywords, to be inherited at their respective nodes. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.study.json*](../out/EGA.study.json "open original schema") |

## items Type

`string` ([Enumeration of design keywords](ega-12-definitions-enumeration-of-design-keywords.md))

## items Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                              | Explanation |
| :------------------------------------------------- | :---------- |
| `"RNA stability design"`                           |             |
| `"binding site identification design"`             |             |
| `"case control design"`                            |             |
| `"cell component comparison design"`               |             |
| `"cell cycle design"`                              |             |
| `"cell type comparison design"`                    |             |
| `"cellular modification design"`                   |             |
| `"clinical history design"`                        |             |
| `"compound treatment design"`                      |             |
| `"cross sectional design"`                         |             |
| `"development or differentiation design"`          |             |
| `"disease state design"`                           |             |
| `"dose response design"`                           |             |
| `"twin design"`                                    |             |
| `"genetic modification design"`                    |             |
| `"genotype design"`                                |             |
| `"growth condition design"`                        |             |
| `"imprinting design"`                              |             |
| `"injury design"`                                  |             |
| `"innate behavior design"`                         |             |
| `"organism part comparison design"`                |             |
| `"organism status design"`                         |             |
| `"pathogenicity design"`                           |             |
| `"population based design"`                        |             |
| `"sex design"`                                     |             |
| `"species design"`                                 |             |
| `"stimulus or stress design"`                      |             |
| `"strain or line design"`                          |             |
| `"time series design"`                             |             |
| `"family based design"`                            |             |
| `"genotyping design"`                              |             |
| `"mobile element identification design"`           |             |
| `"operon identification design"`                   |             |
| `"secreted protein identification design"`         |             |
| `"translational bias design"`                      |             |
| `"transposable element identification design"`     |             |
| `"hardware variation design"`                      |             |
| `"normalization testing design"`                   |             |
| `"operator variation design"`                      |             |
| `"optimization design"`                            |             |
| `"quality control testing design"`                 |             |
| `"reference design"`                               |             |
| `"replicate design"`                               |             |
| `"software variation design"`                      |             |
| `"validation by real time PCR design"`             |             |
| `"validation by reverse transcription PCR design"` |             |

## items Examples

```json
"RNA stability design"
```
