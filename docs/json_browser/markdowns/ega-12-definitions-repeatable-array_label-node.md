# Repeatable array\_label node Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment/properties/array_labels/items
```

Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation. This node corresponds to the basic description of one single label, and thus should be repeated as an array where inherited if multiple labels are intended to be described. Its basic structure is a label ID and its optional CURIE.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## items Type

`object` ([Repeatable array\_label node](ega-12-definitions-repeatable-array_label-node.md))

# items Properties

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                            |
| :---------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [array\_label\_id](#array_label_id)       | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_id")             |
| [array\_label\_curie](#array_label_curie) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_curie")       |
| [label\_description](#label_description)  | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/label_description") |

## array\_label\_id

ID/name (e.g. 'Cy3 dye' or 'Biotin') of the Array label used for the experiment.

`array_label_id`

*   is required

*   Type: `string` ([Array label of the array experiment - ID](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_id")

### array\_label\_id Type

`string` ([Array label of the array experiment - ID](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md))

### array\_label\_id Examples

```json
"Cy3 dye"
```

## array\_label\_curie

CURIE (i.e. ontologized term - e.g. 'CHEBI:37987' or 'CHEBI:15956') of the Array label used for the experiment. Search for the ontologized term at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index).

`array_label_curie`

*   is optional

*   Type: `string` ([Array label of the array experiment - CURIE](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_curie")

### array\_label\_curie Type

`string` ([Array label of the array experiment - CURIE](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

### array\_label\_curie Examples

```json
"CHEBI:37987"
```

## label\_description

Additional description of the used label, indicating further details: context, purpose of the label, description of the label in the absence of an ontologized term, etc.

`label_description`

*   is optional

*   Type: `string` ([Array label of the array experiment - Description](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/label_description")

### label\_description Type

`string` ([Array label of the array experiment - Description](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md))

### label\_description Examples

```json
"This label was use to dye the control samples"
```

```json
"This newly discovered label (yet to be added to an ontology) consists in a compound of type X..."
```

```json
"The label ID is unknown because we were given the RNA already dyed..."
```
