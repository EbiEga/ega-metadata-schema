# Array label identifier Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelIdentifier
```

The chosen term (e.g. 'Cy3 dye' \[CHEBI:37987]) needs to be a Chemical Entity from the CHEBI ontology, look for yours at: <https://www.ebi.ac.uk/ols/search?q=&ontology=chebi>

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## arrayLabelIdentifier Type

`object` ([Array label identifier](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# arrayLabelIdentifier Properties

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                      |
| :---------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelIdentifier/properties/termId") |

## termId



`termId`

*   is optional

*   Type: unknown ([Ontology constraints for this specific termId](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelIdentifier/properties/termId")

### termId Type

unknown ([Ontology constraints for this specific termId](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier-properties-ontology-constraints-for-this-specific-termid.md))

### termId Examples

```json
"CHEBI:37987"
```

```json
"CHEBI:15956"
```
