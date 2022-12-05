# Repeatable arrayLabel node Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/arrayExperiment/properties/arrayLabels/items
```

Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation. This node corresponds to the basic description of one single label, and thus should be repeated as an array where inherited if multiple labels are intended to be described. Its basic structure is a label ID and its optional CURIE.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## items Type

`object` ([Repeatable arrayLabel node](ega-12-definitions-repeatable-arraylabel-node.md))

# items Properties

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                   |
| :------------------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [arrayLabelId](#arraylabelid)         | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelId")              |
| [arrayLabelCurie](#arraylabelcurie)   | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---curie.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelCurie")        |
| [labelDescription](#labeldescription) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/labelDescription") |

## arrayLabelId

ID/name (e.g. 'Cy3 dye' or 'Biotin') of the Array label used for the experiment.

`arrayLabelId`

*   is required

*   Type: `string` ([Array label of the array experiment - ID](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelId")

### arrayLabelId Type

`string` ([Array label of the array experiment - ID](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---id.md))

### arrayLabelId Examples

```json
"Cy3 dye"
```

## arrayLabelCurie

CURIE (i.e. ontologized term - e.g. 'CHEBI:37987' or 'CHEBI:15956') of the Array label used for the experiment. Search for the ontologized term at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index).

`arrayLabelCurie`

*   is optional

*   Type: `string` ([Array label of the array experiment - CURIE](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---curie.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelCurie")

### arrayLabelCurie Type

`string` ([Array label of the array experiment - CURIE](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---curie.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

### arrayLabelCurie Examples

```json
"CHEBI:37987"
```

## labelDescription

Additional description of the used label, indicating further details: context, purpose of the label, description of the label in the absence of an ontologized term, etc.

`labelDescription`

*   is optional

*   Type: `string` ([Array label of the array experiment - Description](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/labelDescription")

### labelDescription Type

`string` ([Array label of the array experiment - Description](ega-12-definitions-repeatable-arraylabel-node-properties-array-label-of-the-array-experiment---description.md))

### labelDescription Examples

```json
"This label was use to dye the control samples"
```

```json
"This newly discovered label (yet to be added to an ontology) consists in a compound of type X..."
```

```json
"The label ID is unknown because we were given the RNA already dyed..."
```
