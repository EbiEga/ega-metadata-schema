# EGA Experiment metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its experiment metadata object. An experiment is considered a planned and intentionally designed process performed as part of a study. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json](../../../schemas/EGA.experiment.json "open original schema") |

## EGA Experiment metadata schema Type

`object` ([EGA Experiment metadata schema](ega-1.md))

one (and only one) of

*   [If the assay technology is a sequencer, the experiment type has to match](ega-1-oneof-if-the-assay-technology-is-a-sequencer-the-experiment-type-has-to-match.md "check type definition")

*   [If the assay technology is an array, the experiment type has to match](ega-1-oneof-if-the-assay-technology-is-an-array-the-experiment-type-has-to-match.md "check type definition")

# EGA Experiment metadata schema Properties

| Property                                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                        |
| :---------------------------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)                                             | Merged   | Required | cannot be null | [EGA Experiment metadata schema](ega-1-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/objectId")                                      |
| [schemaDescriptor](#schemadescriptor)                             | `object` | Optional | cannot be null | [EGA Experiment metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/schemaDescriptor")                             |
| [objectTitle](#objecttitle)                                       | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-1-properties-title-of-the-experiment.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/objectTitle")                             |
| [objectDescription](#objectdescription)                           | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-1-properties-description-of-the-experiment.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/objectDescription")                 |
| [targetedLoci](#targetedloci)                                     | `array`  | Optional | cannot be null | [EGA Experiment metadata schema](ega-1-properties-loci-of-the-targeted-genomic-feature.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/targetedLoci")               |
| [assayTechnology](#assaytechnology)                               | `object` | Required | cannot be null | [EGA Experiment metadata schema](ega-4-definitions-assay-technology.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayTechnology")                               |
| [assayType](#assaytype)                                           | Merged   | Required | cannot be null | [EGA Experiment metadata schema](ega-1-properties-type-of-used-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayType")                                    |
| [assayedBiologicalMacromolecule](#assayedbiologicalmacromolecule) | Merged   | Required | cannot be null | [EGA Experiment metadata schema](ega-1-properties-assayed-biological-macromolecule.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayedBiologicalMacromolecule") |
| [typesOfOutputData](#typesofoutputdata)                           | `array`  | Optional | cannot be null | [EGA Experiment metadata schema](ega-1-properties-types-of-output-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/typesOfOutputData")                          |
| [experimentTypeSpecifications](#experimenttypespecifications)     | Merged   | Required | cannot be null | [EGA Experiment metadata schema](ega-1-properties-experiment-type-specifications.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications")     |
| [experimentRelationships](#experimentrelationships)               | `array`  | Optional | cannot be null | [EGA Experiment metadata schema](ega-1-properties-experiment-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentRelationships")                |
| [experimentAttributes](#experimentattributes)                     | `array`  | Optional | cannot be null | [EGA Experiment metadata schema](ega-1-properties-experiment-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentAttributes")               |

## objectId

Node containing the main identifiers of the object (e.g. alias, centerName...), inherited from the common definitions.

`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-1-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-1-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that experiment EGA ID (EGAX) is correct](ega-1-properties-objects-ids-block-allof-check-that-experiment-ega-id-egax-is-correct.md "check type definition")

## schemaDescriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schemaDescriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/schemaDescriptor")

### schemaDescriptor Type

`object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

## objectTitle

An informative experiment title that should serve as an overview of the experiment, including: used technology, samples, purpose... (e.g. 'Affymetrix-X microarray of human breast cancer cell line MCF-7 treated with tamoxifen compared with untreated controls'). This short text can be used to call out experiment records in searches or in displays.

`objectTitle`

*   is optional

*   Type: `string` ([Title of the experiment](ega-1-properties-title-of-the-experiment.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-title-of-the-experiment.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/objectTitle")

### objectTitle Type

`string` ([Title of the experiment](ega-1-properties-title-of-the-experiment.md))

### objectTitle Examples

```json
"Affymetrix-X microarray of human breast cancer cell line MCF-7 treated with tamoxifen compared with untreated controls"
```

## objectDescription

An in-depth description of the biological relevance and intent of the experiment, including the experimental workflow.

`objectDescription`

*   is optional

*   Type: `string` ([Description of the experiment](ega-1-properties-description-of-the-experiment.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-description-of-the-experiment.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/objectDescription")

### objectDescription Type

`string` ([Description of the experiment](ega-1-properties-description-of-the-experiment.md))

### objectDescription Examples

```json
"The experiment was conducted with the objective of... ...and for that purpose we compared untreated controls against..."
```

## targetedLoci

Array of items that unambiguously define the loci of targeted genomic features in the experiment. For example, if the experiment aim was to detect variants in the human gene TAF1 and TP53, their identifiers will be expected in two items of this array.

`targetedLoci`

*   is optional

*   Type: `object[]` ([Locus identifier](ega-4-definitions-locus-identifier.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-loci-of-the-targeted-genomic-feature.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/targetedLoci")

### targetedLoci Type

`object[]` ([Locus identifier](ega-4-definitions-locus-identifier.md))

### targetedLoci Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## assayTechnology

Metadata of the assay instrument (e.g. sequencer Illumina NextSeq 500) used to obtain the raw data (e.g. sequence files) of an assay.

`assayTechnology`

*   is required

*   Type: `object` ([Assay technology](ega-4-definitions-assay-technology.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-4-definitions-assay-technology.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayTechnology")

### assayTechnology Type

`object` ([Assay technology](ega-4-definitions-assay-technology.md))

## assayType

Node defining the type of assay applicable to the experiment. Notice how, depending on the complexity of the assay type (i.e. how many subtypes it may have), the assay type can be a high level term (e.g. 'single cell sequencing') or very specific (e.g. '454 Sequencing'). We recommend to use the most specific term possible if available: for example, in case your assay was an 'RNA-seq of coding RNA from single cells' \[EFO:0005684], we advise to provide the specific term \[EFO:0005684], instead of the generic 'assay by high throughput sequencer' \[EFO:0002697].

`assayType`

*   is required

*   Type: `object` ([Type of used assay](ega-1-properties-type-of-used-assay.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-type-of-used-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayType")

### assayType Type

`object` ([Type of used assay](ega-1-properties-type-of-used-assay.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

## assayedBiologicalMacromolecule

Node containing information about the assayed biological macromolecule: the material entity (e.g. 'nuclear RNA') that was assayed to generate the data. We recommend that you choose the most specific term that applies to your case: for example, if the assayed molecule is 'long non polyA RNA', choose the specific term 'long non polyA RNA' \[EFO:0005018], instead of the generic term 'ribonucleic acid' \[CHEBI:33697].

`assayedBiologicalMacromolecule`

*   is required

*   Type: `object` ([Assayed biological macromolecule](ega-1-properties-assayed-biological-macromolecule.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-assayed-biological-macromolecule.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayedBiologicalMacromolecule")

### assayedBiologicalMacromolecule Type

`object` ([Assayed biological macromolecule](ega-1-properties-assayed-biological-macromolecule.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

## typesOfOutputData

Types of data the experiment produces.

`typesOfOutputData`

*   is optional

*   Type: `string[]` ([Type of data](ega-4-definitions-type-of-data.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-types-of-output-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/typesOfOutputData")

### typesOfOutputData Type

`string[]` ([Type of data](ega-4-definitions-type-of-data.md))

### typesOfOutputData Constraints

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## experimentTypeSpecifications

Node containing additional attributes to describe the experiment, either array experiments (those in which an [array instrument \[EFO:0002698\]](http://www.ebi.ac.uk/efo/EFO_0002698) was used) or sequencing experiments (those in which a [sequencing instrument \[EFO:0003739\]](http://www.ebi.ac.uk/efo/EFO_0003739) was used). For example, if an array was used, its Array Design Format (ADF) will be expected.

`experimentTypeSpecifications`

*   is required

*   Type: `object` ([Experiment type specifications](ega-1-properties-experiment-type-specifications.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-experiment-type-specifications.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications")

### experimentTypeSpecifications Type

`object` ([Experiment type specifications](ega-1-properties-experiment-type-specifications.md))

one (and only one) of

*   [The sequencing experiment descriptors are required](ega-1-properties-experiment-type-specifications-oneof-the-sequencing-experiment-descriptors-are-required.md "check type definition")

*   [The array experiment descriptors are required](ega-1-properties-experiment-type-specifications-oneof-the-array-experiment-descriptors-are-required.md "check type definition")

## experimentRelationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. an experiment being linked to a Sample) the EGA.

`experimentRelationships`

*   is optional

*   Type: an array of merged types ([Details](ega-1-properties-experiment-relationships-items.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-experiment-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentRelationships")

### experimentRelationships Type

an array of merged types ([Details](ega-1-properties-experiment-relationships-items.md))

### experimentRelationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## experimentAttributes

Custom attributes of an experiment: reusable attributes to encode tag-value pairs (e.g. Tag being 'additional description' and its Value 'this experiment is a re-do of another 3 experiments due to...') with optional units. Its properties are inherited from the common-definitions.json schema.

`experimentAttributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-experiment-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentAttributes")

### experimentAttributes Type

`object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

### experimentAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
