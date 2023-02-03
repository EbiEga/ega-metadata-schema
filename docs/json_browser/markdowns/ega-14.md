# EGA individual metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its individual metadata object. This object is intended to contain metadata about the individual, also known as the sample donor or subject of study. An individual is defined as a person that participates in an experiment or from which a material sample was derived. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.individual.json](../../../schemas/EGA.individual.json "open original schema") |

## EGA individual metadata schema Type

`object` ([EGA individual metadata schema](ega-14.md))

# EGA individual metadata schema Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                    |
| :-------------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)                               | Merged   | Required | cannot be null | [EGA individual metadata schema](ega-14-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/objectId")                                                 |
| [schemaDescriptor](#schemadescriptor)               | `object` | Optional | cannot be null | [EGA individual metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/schemaDescriptor")                                        |
| [organismDescriptor](#organismdescriptor)           | `object` | Required | cannot be null | [EGA individual metadata schema](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/organismDescriptor")                   |
| [minimalPublicAttributes](#minimalpublicattributes) | Merged   | Required | cannot be null | [EGA individual metadata schema](ega-14-properties-minimal-public-attributes-describing-an-individual.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes") |
| [individualRelationships](#individualrelationships) | `array`  | Optional | cannot be null | [EGA individual metadata schema](ega-14-properties-individual-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/individualRelationships")                           |
| [individualAttributes](#individualattributes)       | `array`  | Optional | cannot be null | [EGA individual metadata schema](ega-14-properties-individual-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/individualAttributes")                          |

## objectId

Node containing the main identifiers of the object (e.g. alias, centerName...), inherited from the common definitions. #! We extend the core object (objectCoreId) by adding a pattern check based on this schema's nature: a individual (by using EGAIndividualIdPattern)

`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-14-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-14-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-14-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that individual EGA ID (EGAI) is correct](ega-14-properties-objects-ids-block-allof-check-that-individual-ega-id-egai-is-correct.md "check type definition")

## schemaDescriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schemaDescriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/schemaDescriptor")

### schemaDescriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## organismDescriptor

This property describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or, like humans, made up of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance.

`organismDescriptor`

*   is required

*   Type: `object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/organismDescriptor")

### organismDescriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

## minimalPublicAttributes

Among all attributes describing an individual, some may contain identifiable metadata and thus must be private. Nevertheless, there are three/four required attributes (even if they are unknown): subject id, biological sex, phenotypicAbnormalities and/or diseases. These shall be displayed and queryable on our portal. In the case of a healthy individual (with no phenotypic abnormalities nor diseases), the 'phenotypicAbnormalities' and 'diseases' arrays will contain a reference to 'Unaffected' \[NCIT:C94232]. Do take into account the 'excluded' property of each 'disease' or 'phenotypicAbnormality' in order to evaluate it correctly, since logic negation can be provided using that property.

`minimalPublicAttributes`

*   is required

*   Type: `object` ([Minimal public attributes describing an individual](ega-14-properties-minimal-public-attributes-describing-an-individual.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-14-properties-minimal-public-attributes-describing-an-individual.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes")

### minimalPublicAttributes Type

`object` ([Minimal public attributes describing an individual](ega-14-properties-minimal-public-attributes-describing-an-individual.md))

any of

*   [Either the phenotypicAbnormalities array is given](ega-14-properties-minimal-public-attributes-describing-an-individual-anyof-either-the-phenotypicabnormalities-array-is-given.md "check type definition")

*   [Or the diseases array is given](ega-14-properties-minimal-public-attributes-describing-an-individual-anyof-or-the-diseases-array-is-given.md "check type definition")

## individualRelationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. a viral sample from BioSamples being linked to a blood sample within the EGA) and within (e.g. a sample being linked to an individual) the EGA.

`individualRelationships`

*   is optional

*   Type: an array of merged types ([Details](ega-14-properties-individual-relationships-items.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-14-properties-individual-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/individualRelationships")

### individualRelationships Type

an array of merged types ([Details](ega-14-properties-individual-relationships-items.md))

### individualRelationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## individualAttributes

Custom attributes of an individual: reusable attributes to encode tag-value pairs (e.g. Tag being 'age' and its Value '30') with optional units (e.g. 'years'). Its properties are inherited from the common-definitions.json schema.

`individualAttributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-14-properties-individual-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/individualAttributes")

### individualAttributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### individualAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
