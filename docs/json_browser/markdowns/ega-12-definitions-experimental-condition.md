# Experimental condition Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimentalConditionDescriptor
```

A state of being, an external or environmental factor or a treatment observed or administered prior to or concurrent with an investigative procedure such as an assessment of a morphological or physiological state or property in a single individual or sample or in a group of individuals or samples, especially a state, factor or treatment which has the potential to influence the outcome of such an assessment. We highly recommend the usage of ontologies to describe experimental conditions (search at '<https://www.ebi.ac.uk/ols/ontologies/efo>').

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## experimentalConditionDescriptor Type

`object` ([Experimental condition](ega-12-definitions-experimental-condition.md))

# experimentalConditionDescriptor Properties

| Property                                                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                     |
| :-------------------------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [experimentalConditionTerm](#experimentalconditionterm)               | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimentalConditionDescriptor/properties/experimentalConditionTerm")               |
| [experimentalConditionCurie](#experimentalconditioncurie)             | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimentalConditionDescriptor/properties/experimentalConditionCurie")             |
| [experimentalConditionDescription](#experimentalconditiondescription) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimentalConditionDescriptor/properties/experimentalConditionDescription") |

## experimentalConditionTerm

Term that specifies the experimental condition (e.g. 'fibroadenoma').

`experimentalConditionTerm`

*   is required

*   Type: `string` ([Experimental condition term](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimentalConditionDescriptor/properties/experimentalConditionTerm")

### experimentalConditionTerm Type

`string` ([Experimental condition term](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md))

### experimentalConditionTerm Examples

```json
"control"
```

```json
"fibroadenoma"
```

```json
"osteonecrosis"
```

## experimentalConditionCurie

Curie (i.e. ontologised term - e.g. 'EFO:0001461') of the experimental condition. Search for the ontologized term at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index).

`experimentalConditionCurie`

*   is optional

*   Type: `string` ([Experimental condition curie](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimentalConditionDescriptor/properties/experimentalConditionCurie")

### experimentalConditionCurie Type

`string` ([Experimental condition curie](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-experimental-condition-properties-experimental-condition-curie-allof-compact-uri-curie-pattern.md "check type definition")

### experimentalConditionCurie Examples

```json
"EFO:0001461"
```

```json
"EFO:1000254"
```

```json
"EFO:0004259"
```

## experimentalConditionDescription

Broad description of the experimental condition, providing further details and context over the ontologised term.

`experimentalConditionDescription`

*   is optional

*   Type: `string` ([Experimental condition description](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimentalConditionDescriptor/properties/experimentalConditionDescription")

### experimentalConditionDescription Type

`string` ([Experimental condition description](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md))

### experimentalConditionDescription Examples

```json
"A control role is borne by a material in a process in which results obtained from an experimental sample and a control sample are compared."
```

```json
"A benign tumor of the breast characterized by the presence of stromal and epithelial elements."
```

```json
"A none disease characterized by death of bone tissue due to a lack of blood supply."
```
