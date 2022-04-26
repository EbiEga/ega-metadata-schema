# Experimental condition Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/minimal_public_attributes/properties/experimental_condition
```

A state of being, an external or environmental factor or a treatment observed or administered prior to or concurrent with an investigative procedure such as an assessment of a morphological or physiological state or property in a single individual or sample or in a group of individuals or samples, especially a state, factor or treatment which has the potential to influence the outcome of such an assessment. We highly recommend the usage of ontologies to describe experimental conditions (search at '<https://www.ebi.ac.uk/ols/ontologies/efo>').

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## experimental\_condition Type

`object` ([Experimental condition](ega-12-definitions-experimental-condition.md))

# experimental\_condition Properties

| Property                                                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                               |
| :-------------------------------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [experimental\_condition\_term](#experimental_condition_term)               | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_term")               |
| [experimental\_condition\_curie](#experimental_condition_curie)             | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_curie")             |
| [experimental\_condition\_description](#experimental_condition_description) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_description") |

## experimental\_condition\_term

Term that specifies the experimental condition (e.g. 'fibroadenoma').

`experimental_condition_term`

*   is required

*   Type: `string` ([Experimental condition term](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_term")

### experimental\_condition\_term Type

`string` ([Experimental condition term](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md))

### experimental\_condition\_term Examples

```json
"control"
```

```json
"fibroadenoma"
```

```json
"osteonecrosis"
```

## experimental\_condition\_curie

Curie (i.e. ontologised term - e.g. 'EFO:0001461') of the experimental condition. Search for the ontologized term at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index).

`experimental_condition_curie`

*   is optional

*   Type: `string` ([Experimental condition curie](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_curie")

### experimental\_condition\_curie Type

`string` ([Experimental condition curie](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

### experimental\_condition\_curie Examples

```json
"EFO:0001461"
```

```json
"EFO:1000254"
```

```json
"EFO:0004259"
```

## experimental\_condition\_description

Broad description of the experimental condition, providing further details and context over the ontologised term.

`experimental_condition_description`

*   is optional

*   Type: `string` ([Experimental condition description](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_description")

### experimental\_condition\_description Type

`string` ([Experimental condition description](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md))

### experimental\_condition\_description Examples

```json
"A control role is borne by a material in a process in which results obtained from an experimental sample and a control sample are compared."
```

```json
"A benign tumor of the breast characterized by the presence of stromal and epithelial elements."
```

```json
"A none disease characterized by death of bone tissue due to a lack of blood supply."
```
