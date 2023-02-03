# Repeatable arrayLabel node Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/arrayExperiment/properties/arrayLabels/items
```

Chemical conjugated to nucleic acid/proteins to label them before microarray hybridisation. This node defines one single label, and thus should be repeated as an array where inherited if multiple labels are intended to be described.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## items Type

`object` ([Repeatable arrayLabel node](ega-4-definitions-repeatable-arraylabel-node.md))

any of

*   [Untitled undefined type in EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-anyof-0.md "check type definition")

*   [Untitled undefined type in EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-anyof-1.md "check type definition")

# items Properties

| Property                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                             |
| :---------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [arrayLabelIdentifier](#arraylabelidentifier)   | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelIdentifier")   |
| [arrayLabelDescription](#arraylabeldescription) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelDescription") |

## arrayLabelIdentifier

The chosen term (e.g. 'Cy3 dye' \[CHEBI:37987]) needs to be a Chemical Entity from the CHEBI ontology, look for yours at: <https://www.ebi.ac.uk/ols/search?q=&ontology=chebi>

`arrayLabelIdentifier`

*   is optional

*   Type: `object` ([Array label identifier](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelIdentifier")

### arrayLabelIdentifier Type

`object` ([Array label identifier](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

## arrayLabelDescription

Additional description of the used array label, indicating further details: context, purpose of the label, description of the label in the absence of an ontologized term, etcetera.

`arrayLabelDescription`

*   is optional

*   Type: `string` ([Array label description](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelDescription")

### arrayLabelDescription Type

`string` ([Array label description](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-description.md))

### arrayLabelDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### arrayLabelDescription Examples

```json
"This label was used to dye the control samples"
```

```json
"This newly discovered label (yet to be added to an ontology) consists of a compound of type X..."
```

```json
"The label ID is unknown because we were given an already dyed kit..."
```
