# Enumeration of design keywords Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyDesigns/items
```

An object containing the enumeration of multiple study-design keywords, to be inherited at their respective nodes. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.study.json\*](../../../schemas/EGA.study.json "open original schema") |

## items Type

`string` ([Enumeration of design keywords](ega-4-definitions-enumeration-of-design-keywords.md))

## items Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                              | Explanation    |
| :------------------------------------------------- | :------------- |
| `"RNA stability design"`                           | \[EFO:0001783] |
| `"binding site identification design"`             | \[EFO:0004664] |
| `"case control design"`                            | \[EFO:0001427] |
| `"cell component comparison design"`               | \[EFO:0001743] |
| `"cell cycle design"`                              | \[EFO:0001744] |
| `"cell type comparison design"`                    | \[EFO:0001745] |
| `"cellular modification design"`                   | \[EFO:0004666] |
| `"clinical history design"`                        | \[EFO:0001780] |
| `"compound treatment design"`                      | \[EFO:0001755] |
| `"cross sectional design"`                         | \[EFO:0001428] |
| `"development or differentiation design"`          | \[EFO:0001746] |
| `"disease state design"`                           | \[EFO:0001756] |
| `"dose response design"`                           | \[EFO:0001757] |
| `"twin design"`                                    | \[EFO:0001431] |
| `"genetic modification design"`                    | \[EFO:0001758] |
| `"genotype design"`                                | \[EFO:0001748] |
| `"growth condition design"`                        | \[EFO:0001759] |
| `"imprinting design"`                              | \[EFO:0001747] |
| `"injury design"`                                  | \[EFO:0001760] |
| `"innate behavior design"`                         | \[EFO:0001749] |
| `"organism part comparison design"`                | \[EFO:0001750] |
| `"organism status design"`                         | \[EFO:0001751] |
| `"pathogenicity design"`                           | \[EFO:0001761] |
| `"population based design"`                        | \[EFO:0001430] |
| `"sex design"`                                     | \[EFO:0001752] |
| `"species design"`                                 | \[EFO:0001753] |
| `"stimulus or stress design"`                      | \[EFO:0001762] |
| `"strain or line design"`                          | \[EFO:0001754] |
| `"time series design"`                             | \[EFO:0001779] |
| `"family based design"`                            | \[EFO:0001429] |
| `"genotyping design"`                              | \[EFO:0001784] |
| `"mobile element identification design"`           | \[EFO:0005693] |
| `"operon identification design"`                   | \[EFO:0001785] |
| `"secreted protein identification design"`         | \[EFO:0001786] |
| `"translational bias design"`                      | \[EFO:0001787] |
| `"transposable element identification design"`     | \[EFO:0005692] |
| `"hardware variation design"`                      | \[EFO:0001767] |
| `"normalization testing design"`                   | \[EFO:0001771] |
| `"operator variation design"`                      | \[EFO:0001772] |
| `"optimization design"`                            | \[EFO:0001773] |
| `"quality control testing design"`                 | \[EFO:0001774] |
| `"reference design"`                               | \[EFO:0001775] |
| `"replicate design"`                               | \[EFO:0001776] |
| `"software variation design"`                      | \[EFO:0001778] |
| `"validation by real time PCR design"`             | \[OBI:0001166] |
| `"validation by reverse transcription PCR design"` | \[OBI:0001162] |

## items Examples

```json
"RNA stability design"
```
