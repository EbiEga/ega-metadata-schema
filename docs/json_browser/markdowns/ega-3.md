# EGA individual metadata schema v0.0.1 Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its individual metadata object. This object is intended to contain metadata about the individual, also known as the sample donor or subject of study. An individual is defined as a person that participates in an experiment or from which a material sample was derived. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                               |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.individual.json](../out/EGA.individual.json "open original schema") |

## EGA individual metadata schema v0.0.1 Type

`object` ([EGA individual metadata schema v0.0.1](ega-3.md))

# EGA individual metadata schema v0.0.1 Properties

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                  |
| :------------------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [object_id](#object_id)                                 | Merged   | Required | cannot be null | [EGA individual metadata schema v0.0.1](ega-3-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/object_id")                                                  |
| [minimal_public_attributes](#minimal_public_attributes) | `object` | Required | cannot be null | [EGA individual metadata schema v0.0.1](ega-3-properties-minimal-public-attributes-describing-an-individual.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes") |
| [individual_relationships](#individual_relationships)   | `array`  | Optional | cannot be null | [EGA individual metadata schema v0.0.1](ega-3-properties-individual-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/individual_relationships")                            |
| [individual_attributes](#individual_attributes)         | `array`  | Optional | cannot be null | [EGA individual metadata schema v0.0.1](ega-3-properties-individual-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/individual_attributes")                           |

## object_id

Node containing the main identifiers of the object (e.g. alias, center_name...), inherited from the common definitions. #! We extend the core object (object_core_id) by adding a pattern check based on this schema's nature: a individual (by using EGA-individual-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-3-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA individual metadata schema v0.0.1](ega-3-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/object_id")

### object_id Type

`object` ([Object's IDs block](ega-3-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that individual EGA ID (EGAN) is correct](ega-3-properties-objects-ids-block-allof-check-that-individual-ega-id-egan-is-correct.md "check type definition")

## minimal_public_attributes

Among all fields describing an individual, some may contain identifiable metadata and thus be private. Nevertheless, there are three basic attributes that every individual should contain (even if they are unknown): subject id, biological sex and phenotype. These shall be displayed and queryable.

`minimal_public_attributes`

*   is required

*   Type: `object` ([Minimal public attributes describing an individual](ega-3-properties-minimal-public-attributes-describing-an-individual.md))

*   cannot be null

*   defined in: [EGA individual metadata schema v0.0.1](ega-3-properties-minimal-public-attributes-describing-an-individual.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes")

### minimal_public_attributes Type

`object` ([Minimal public attributes describing an individual](ega-3-properties-minimal-public-attributes-describing-an-individual.md))

## individual_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. a viral sample from BioSamples being linked to a blood sample within the EGA) and within (e.g. a sample being linked to an individual) the EGA.

`individual_relationships`

*   is optional

*   Type: `object[]` ([EGA Relationships object](ega-2-definitions-ega-relationships-object.md))

*   cannot be null

*   defined in: [EGA individual metadata schema v0.0.1](ega-3-properties-individual-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/individual_relationships")

### individual_relationships Type

`object[]` ([EGA Relationships object](ega-2-definitions-ega-relationships-object.md))

### individual_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## individual_attributes

Custom attributes of an individual: reusable attributes to encode tag-value pairs (e.g. Tag being 'age' and its Value '30') with optional units (e.g. 'years'). Its properties are inherited from the common-definitions.json schema.

`individual_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-2-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA individual metadata schema v0.0.1](ega-3-properties-individual-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/individual_attributes")

### individual_attributes Type

`object[]` ([Custom attribute of an object](ega-2-definitions-custom-attribute-of-an-object.md))

### individual_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
