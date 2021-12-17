# Experimental condition \[XCO:0000000] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/minimal_public_attributes/properties/experimental_condition
```

A state of being, an external or environmental factor or a treatment observed or administered prior to or concurrent with an investigative procedure such as an assessment of a morphological or physiological state or property in a single individual or sample or in a group of individuals or samples, especially a state, factor or treatment which has the potential to influence the outcome of such an assessment. We highly recommend the usage of ontologies to describe experimental conditions (search at '<https://www.ebi.ac.uk/ols/ontologies/efo>').

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json*](../out/EGA.sample.json "open original schema") |

## experimental_condition Type

`object` ([Experimental condition \[XCO:0000000\]](ega-2-definitions-experimental-condition-xco0000000.md))

# experimental_condition Properties

| Property                                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                |
| :------------------------------------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [experimental_condition_term](#experimental_condition_term)               | `string` | Required | cannot be null | [EGA common metadata definitions v0.0.1](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-term.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_term")               |
| [experimental_condition_curie](#experimental_condition_curie)             | `string` | Optional | cannot be null | [EGA common metadata definitions v0.0.1](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_curie")             |
| [experimental_condition_description](#experimental_condition_description) | `string` | Optional | cannot be null | [EGA common metadata definitions v0.0.1](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_description") |

## experimental_condition_term

Human-readable term that specifies the experimental condition (e.g. 'fibroadenoma').

`experimental_condition_term`

*   is required

*   Type: `string` ([Experimental condition term](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-term.md))

*   cannot be null

*   defined in: [EGA common metadata definitions v0.0.1](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-term.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_term")

### experimental_condition_term Type

`string` ([Experimental condition term](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-term.md))

### experimental_condition_term Examples

```json
"control"
```

```json
"fibroadenoma"
```

```json
"osteonecrosis"
```

## experimental_condition_curie

Curie (i.e. ontologised term - e.g. 'EFO:0001461') of the experimental condition.

`experimental_condition_curie`

*   is optional

*   Type: `string` ([Experimental condition curie](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions v0.0.1](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_curie")

### experimental_condition_curie Type

`string` ([Experimental condition curie](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-curie.md))

### experimental_condition_curie Examples

```json
"EFO:0001461"
```

```json
"EFO:1000254"
```

```json
"EFO:0004259"
```

## experimental_condition_description

Broad description of the experimental condition, providing further details and context over the ontologised term.

`experimental_condition_description`

*   is optional

*   Type: `string` ([Experimental condition description](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions v0.0.1](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_description")

### experimental_condition_description Type

`string` ([Experimental condition description](ega-2-definitions-experimental-condition-xco0000000-properties-experimental-condition-description.md))

### experimental_condition_description Examples

```json
"A control role is borne by a material in a process in which results obtained from an experimental sample and a control sample are compared."
```

```json
"A benign tumor of the breast characterized by the presence of stromal and epithelial elements."
```

```json
"A none disease characterized by death of bone tissue due to a lack of blood supply."
```
