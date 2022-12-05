# Repeatable Sample-label node Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation
```

The base node of a label-sample association. One form of basic identification of the sample (inherited from objectCoreId - e.g. either the center name and alias or the accession) is required, as well as the label per se.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## sampleLabelAssociation Type

`object` ([Repeatable Sample-label node](ega-12-definitions-repeatable-sample-label-node.md))

# sampleLabelAssociation Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                         |
| :-------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [label](#label)       | `object` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-arraylabel-node.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/label")                                   |
| [objectId](#objectid) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/objectId") |

## label

Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation. This node corresponds to the basic description of one single label, and thus should be repeated as an array where inherited if multiple labels are intended to be described. Its basic structure is a label ID and its optional CURIE.

`label`

*   is required

*   Type: `object` ([Repeatable arrayLabel node](ega-12-definitions-repeatable-arraylabel-node.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-arraylabel-node.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/label")

### label Type

`object` ([Repeatable arrayLabel node](ega-12-definitions-repeatable-arraylabel-node.md))

## objectId



`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that sample EGA ID (EGAN) pattern is correct](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block-allof-check-that-sample-ega-id-egan-pattern-is-correct.md "check type definition")
