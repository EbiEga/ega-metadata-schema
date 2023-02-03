# Array label description Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelDescription
```

Additional description of the used array label, indicating further details: context, purpose of the label, description of the label in the absence of an ontologized term, etcetera.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## arrayLabelDescription Type

`string` ([Array label description](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-description.md))

## arrayLabelDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## arrayLabelDescription Examples

```json
"This label was used to dye the control samples"
```

```json
"This newly discovered label (yet to be added to an ontology) consists of a compound of type X..."
```

```json
"The label ID is unknown because we were given an already dyed kit..."
```
