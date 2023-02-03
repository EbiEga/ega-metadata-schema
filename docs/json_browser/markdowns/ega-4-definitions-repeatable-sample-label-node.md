# Repeatable Sample-label node Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation
```

The base node of a label-sample association. One form of basic identification of the sample (inherited from objectCoreId - e.g. either the center name and alias or the accession) is required, as well as the label per se.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## sampleLabelAssociation Type

`object` ([Repeatable Sample-label node](ega-4-definitions-repeatable-sample-label-node.md))

# sampleLabelAssociation Properties

| Property                  | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                        |
| :------------------------ | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [arrayLabel](#arraylabel) | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/arrayLabel")                              |
| [objectId](#objectid)     | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/objectId") |

## arrayLabel

Chemical conjugated to nucleic acid/proteins to label them before microarray hybridisation. This node defines one single label, and thus should be repeated as an array where inherited if multiple labels are intended to be described.

`arrayLabel`

*   is required

*   Type: `object` ([Repeatable arrayLabel node](ega-4-definitions-repeatable-arraylabel-node.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/arrayLabel")

### arrayLabel Type

`object` ([Repeatable arrayLabel node](ega-4-definitions-repeatable-arraylabel-node.md))

any of

*   [Untitled undefined type in EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-anyof-0.md "check type definition")

*   [Untitled undefined type in EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-anyof-1.md "check type definition")

## objectId



`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that sample EGA ID (EGAN) pattern is correct](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block-allof-check-that-sample-ega-id-egan-pattern-is-correct.md "check type definition")
