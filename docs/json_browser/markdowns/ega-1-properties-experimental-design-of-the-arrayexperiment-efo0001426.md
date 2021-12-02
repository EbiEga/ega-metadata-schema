# Experimental design of the ArrayExperiment \[EFO:0001426] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/experimental_design
```

Experimental factor describing the method of investigating particular types of research questions or solving particular types of problems. It contains both the human readable ID (e.g. RNA stability design) and CURIE (e.g. EFO:0001783) of the experimental design.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## experimental_design Type

`object` ([Experimental design of the ArrayExperiment \[EFO:0001426\]](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426.md))

# experimental_design Properties

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [experimental_design_id](#experimental_design_id)       | `string` | Required | cannot be null | [EGA ArrayExperiment metadata schema](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426-properties-experimental-design-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/experimental_design/properties/experimental_design_id")       |
| [experimental_design_curie](#experimental_design_curie) | `string` | Optional | cannot be null | [EGA ArrayExperiment metadata schema](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426-properties-experimental-design-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/experimental_design/properties/experimental_design_curie") |

## experimental_design_id

The human readable ID (e.g. RNA stability design), chosen from a list of CVs, of the experimental design defining the ArrayExperiment.

`experimental_design_id`

*   is required

*   Type: `string` ([Experimental design of the ArrayExperiment - ID](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426-properties-experimental-design-of-the-arrayexperiment---id.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426-properties-experimental-design-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/experimental_design/properties/experimental_design_id")

### experimental_design_id Type

`string` ([Experimental design of the ArrayExperiment - ID](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426-properties-experimental-design-of-the-arrayexperiment---id.md))

### experimental_design_id Constraints

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

### experimental_design_id Examples

```json
"RNA stability design"
```

## experimental_design_curie

The CURIE (i.e. ontologized term - e.g. EFO:0001783), chosen from a list of CVs, of the experimental design defining the ArrayExperiment

`experimental_design_curie`

*   is optional

*   Type: `string` ([Experimental design of the ArrayExperiment - CURIE](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426-properties-experimental-design-of-the-arrayexperiment---curie.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426-properties-experimental-design-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/experimental_design/properties/experimental_design_curie")

### experimental_design_curie Type

`string` ([Experimental design of the ArrayExperiment - CURIE](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426-properties-experimental-design-of-the-arrayexperiment---curie.md))

### experimental_design_curie Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"EFO:0001783"` |             |
| `"EFO:0004664"` |             |
| `"EFO:0001427"` |             |
| `"EFO:0001743"` |             |
| `"EFO:0001744"` |             |
| `"EFO:0001745"` |             |
| `"EFO:0004666"` |             |
| `"EFO:0001780"` |             |
| `"EFO:0001755"` |             |
| `"EFO:0001428"` |             |
| `"EFO:0001746"` |             |
| `"EFO:0001756"` |             |
| `"EFO:0001757"` |             |
| `"EFO:0001431"` |             |
| `"EFO:0001758"` |             |
| `"EFO:0001748"` |             |
| `"EFO:0001759"` |             |
| `"EFO:0001747"` |             |
| `"EFO:0001760"` |             |
| `"EFO:0001749"` |             |
| `"EFO:0001750"` |             |
| `"EFO:0001751"` |             |
| `"EFO:0001761"` |             |
| `"EFO:0001430"` |             |
| `"EFO:0001752"` |             |
| `"EFO:0001753"` |             |
| `"EFO:0001762"` |             |
| `"EFO:0001754"` |             |
| `"EFO:0001779"` |             |

### experimental_design_curie Examples

```json
"EFO:0001783"
```
