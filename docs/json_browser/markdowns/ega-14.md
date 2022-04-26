# EGA individual metadata schema Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its individual metadata object. This object is intended to contain metadata about the individual, also known as the sample donor or subject of study. An individual is defined as a person that participates in an experiment or from which a material sample was derived. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.individual.json](../../../schemas/EGA.individual.json "open original schema") |

## EGA individual metadata schema Type

`object` ([EGA individual metadata schema](ega-14.md))

# EGA individual metadata schema Properties

| Property                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                            |
| :-------------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [object\_id](#object_id)                                  | Merged   | Required | cannot be null | [EGA individual metadata schema](ega-14-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/object_id")                                                  |
| [schema\_descriptor](#schema_descriptor)                  | `object` | Optional | cannot be null | [EGA individual metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/schema_descriptor")                                         |
| [organism\_descriptor](#organism_descriptor)              | `object` | Required | cannot be null | [EGA individual metadata schema](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/organism_descriptor")                    |
| [minimal\_public\_attributes](#minimal_public_attributes) | `object` | Required | cannot be null | [EGA individual metadata schema](ega-14-properties-minimal-public-attributes-describing-an-individual.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes") |
| [individual\_relationships](#individual_relationships)    | `array`  | Optional | cannot be null | [EGA individual metadata schema](ega-14-properties-individual-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/individual_relationships")                            |
| [individual\_attributes](#individual_attributes)          | `array`  | Optional | cannot be null | [EGA individual metadata schema](ega-14-properties-individual-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/individual_attributes")                           |

## object\_id

Node containing the main identifiers of the object (e.g. alias, center\_name...), inherited from the common definitions. #! We extend the core object (object\_core\_id) by adding a pattern check based on this schema's nature: a individual (by using EGA-individual-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-14-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-14-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/object_id")

### object\_id Type

`object` ([Object's IDs block](ega-14-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that individual EGA ID (EGAI) is correct](ega-14-properties-objects-ids-block-allof-check-that-individual-ega-id-egai-is-correct.md "check type definition")

## schema\_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/schema_descriptor")

### schema\_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## organism\_descriptor

This node describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or made up, like humans, of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance by default.

`organism_descriptor`

*   is required

*   Type: `object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/organism_descriptor")

### organism\_descriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

## minimal\_public\_attributes

Among all attributes describing an individual, some may contain identifiable metadata and thus must be private. Nevertheless, there are three required attributes (even if they are unknown): subject id, biological sex and phenotype. These shall be displayed and queryable.

`minimal_public_attributes`

*   is required

*   Type: `object` ([Minimal public attributes describing an individual](ega-14-properties-minimal-public-attributes-describing-an-individual.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-14-properties-minimal-public-attributes-describing-an-individual.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes")

### minimal\_public\_attributes Type

`object` ([Minimal public attributes describing an individual](ega-14-properties-minimal-public-attributes-describing-an-individual.md))

## individual\_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. a viral sample from BioSamples being linked to a blood sample within the EGA) and within (e.g. a sample being linked to an individual) the EGA.

`individual_relationships`

*   is optional

*   Type: an array of merged types ([Details](ega-14-properties-individual-relationships-items.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-14-properties-individual-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/individual_relationships")

### individual\_relationships Type

an array of merged types ([Details](ega-14-properties-individual-relationships-items.md))

### individual\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## individual\_attributes

Custom attributes of an individual: reusable attributes to encode tag-value pairs (e.g. Tag being 'age' and its Value '30') with optional units (e.g. 'years'). Its properties are inherited from the common-definitions.json schema.

`individual_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-14-properties-individual-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/individual_attributes")

### individual\_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### individual\_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
