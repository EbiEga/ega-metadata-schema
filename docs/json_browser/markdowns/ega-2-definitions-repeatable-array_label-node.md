# Repeatable array_label node Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/label
```

Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation. This node corresponds to the basic description of one single label, and thus should be repeated as an array where inherited if multiple labels are intended to be described. Its basic structure is a label ID and its optional CURIE.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## label Type

`object` ([Repeatable array_label node](ega-2-definitions-repeatable-array_label-node.md))

# label Properties

| Property                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                    |
| :-------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [array_label_id](#array_label_id)       | `string` | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_id")       |
| [array_label_curie](#array_label_curie) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_curie") |

## array_label_id

Human readable ID/name (e.g. 'Cy3 dye' or 'Biotin') of the Array label used for the experiment.

`array_label_id`

*   is required

*   Type: `string` ([Array label of the ArrayExperiment - ID](ega-2-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_id")

### array_label_id Type

`string` ([Array label of the ArrayExperiment - ID](ega-2-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---id.md))

### array_label_id Examples

```json
"Cy3 dye"
```

## array_label_curie

CURIE (i.e. ontologized term - e.g. 'CHEBI:37987' or 'CHEBI:15956') of the Array label used for the experiment.

`array_label_curie`

*   is required

*   Type: `string` ([Array label of the ArrayExperiment - CURIE](ega-2-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_curie")

### array_label_curie Type

`string` ([Array label of the ArrayExperiment - CURIE](ega-2-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---curie.md))

### array_label_curie Examples

```json
"CHEBI:37987"
```
