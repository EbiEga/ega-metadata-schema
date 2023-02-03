# Assayed biological macromolecule Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayedBiologicalMacromolecule
```

Node containing information about the assayed biological macromolecule: the material entity (e.g. 'nuclear RNA') that was assayed to generate the data. We recommend that you choose the most specific term that applies to your case: for example, if the assayed molecule is 'long non polyA RNA', choose the specific term 'long non polyA RNA' \[EFO:0005018], instead of the generic term 'ribonucleic acid' \[CHEBI:33697].

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## assayedBiologicalMacromolecule Type

`object` ([Assayed biological macromolecule](ega-1-properties-assayed-biological-macromolecule.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# assayedBiologicalMacromolecule Properties

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                   |
| :---------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Not specified | Optional | cannot be null | [EGA Experiment metadata schema](ega-1-properties-assayed-biological-macromolecule-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayedBiologicalMacromolecule/properties/termId") |

## termId



`termId`

*   is optional

*   Type: unknown ([Ontology constraints for this specific termId](ega-1-properties-assayed-biological-macromolecule-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-assayed-biological-macromolecule-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayedBiologicalMacromolecule/properties/termId")

### termId Type

unknown ([Ontology constraints for this specific termId](ega-1-properties-assayed-biological-macromolecule-properties-ontology-constraints-for-this-specific-termid.md))

### termId Examples

```json
"EFO:0005018"
```

```json
"CHEBI:33697"
```

```json
"EFO:0005019"
```
