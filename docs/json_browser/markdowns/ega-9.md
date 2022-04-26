# EGA Experiment metadata schema Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its experiment metadata object. An experiment is considered a planned and intentionally designed process performed as part of a study. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json](../../../schemas/EGA.experiment.json "open original schema") |

## EGA Experiment metadata schema Type

`object` ([EGA Experiment metadata schema](ega-9.md))

one (and only one) of

*   [If the assay technology is a sequencer, the experiment type has to match](ega-9-oneof-if-the-assay-technology-is-a-sequencer-the-experiment-type-has-to-match.md "check type definition")

*   [If the assay technology is an array, the experiment type has to match](ega-9-oneof-if-the-assay-technology-is-an-array-the-experiment-type-has-to-match.md "check type definition")

# EGA Experiment metadata schema Properties

| Property                                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                   |
| :------------------------------------------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object\_id](#object_id)                                            | Merged   | Required | cannot be null | [EGA Experiment metadata schema](ega-9-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/object_id")                                          |
| [schema\_descriptor](#schema_descriptor)                            | `object` | Optional | cannot be null | [EGA Experiment metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/schema_descriptor")                                |
| [object\_title](#object_title)                                      | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-title-of-the-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/object_title")                                 |
| [object\_description](#object_description)                          | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-description-of-the-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/object_description")                     |
| [experiment\_protocols](#experiment_protocols)                      | `array`  | Required | cannot be null | [EGA Experiment metadata schema](ega-9-properties-protocols-related-to-an-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_protocols")              |
| [targeted\_loci](#targeted_loci)                                    | `array`  | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-loci-of-the-targeted-genomic-feature.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/targeted_loci")                   |
| [assay\_technology](#assay_technology)                              | Merged   | Required | cannot be null | [EGA Experiment metadata schema](ega-12-definitions-assay-technology.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_technology")                                  |
| [assay\_type\_descriptor](#assay_type_descriptor)                   | Merged   | Required | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor")                                  |
| [assayed\_molecule\_type](#assayed_molecule_type)                   | `string` | Required | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-the-assayed-molecule-of-the-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assayed_molecule_type") |
| [types\_of\_output\_data](#types_of_output_data)                    | `array`  | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-types-of-output-data.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/types_of_output_data")                            |
| [experiment\_type\_specifications](#experiment_type_specifications) | Merged   | Required | cannot be null | [EGA Experiment metadata schema](ega-9-properties-experiment-type-specifications.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications")        |
| [experiment\_relationships](#experiment_relationships)              | `array`  | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-experiment-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_relationships")                    |
| [experiment\_attributes](#experiment_attributes)                    | `array`  | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-experiment-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_attributes")                   |

## object\_id

Node containing the main identifiers of the object (e.g. alias, center\_name...), inherited from the common definitions.

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-9-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/object_id")

### object\_id Type

`object` ([Object's IDs block](ega-9-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that experiment EGA ID (EGAX) is correct](ega-9-properties-objects-ids-block-allof-check-that-experiment-ega-id-egax-is-correct.md "check type definition")

## schema\_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/schema_descriptor")

### schema\_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## object\_title

An informative experiment title that should serve as an overview of the experiment, including: used technology, samples, purpose... (e.g. 'Affymetrix-X microarray of human breast cancer cell line MCF-7 treated with tamoxifen compared with untreated controls'). This short text can be used to call out experiment records in searches or in displays.

`object_title`

*   is optional

*   Type: `string` ([Title of the experiment](ega-9-properties-title-of-the-experiment.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-title-of-the-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/object_title")

### object\_title Type

`string` ([Title of the experiment](ega-9-properties-title-of-the-experiment.md))

### object\_title Examples

```json
"Affymetrix-X microarray of human breast cancer cell line MCF-7 treated with tamoxifen compared with untreated controls"
```

## object\_description

An in-depth description of the biological relevance and intent of the experiment, including the experimental workflow.

`object_description`

*   is optional

*   Type: `string` ([Description of the experiment](ega-9-properties-description-of-the-experiment.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-description-of-the-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/object_description")

### object\_description Type

`string` ([Description of the experiment](ega-9-properties-description-of-the-experiment.md))

### object\_description Examples

```json
"The experiment was conducted with the objective of... ...and for that purpose we compared untreated controls against..."
```

## experiment\_protocols

Comprises metadata (e.g. Type of protocol) of a plan specification executed during an experiment. It shall have a sufficient level of detail and quantitative information to communicate it (and thus reproduce it) between investigation agents.

`experiment_protocols`

*   is required

*   Type: `object[]` ([EGA Protocols object](ega-12-definitions-ega-protocols-object.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-protocols-related-to-an-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_protocols")

### experiment\_protocols Type

`object[]` ([EGA Protocols object](ega-12-definitions-ega-protocols-object.md))

### experiment\_protocols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## targeted\_loci

Array of items that unambiguously define the loci of targeted genomic features in the experiment. For example, if the experiment aim was to detect variants in the human gene TAF1 and TP53, their identifiers will be expected in two items of this array.

`targeted_loci`

*   is optional

*   Type: `object[]` ([Locus identifier](ega-12-definitions-locus-identifier.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-loci-of-the-targeted-genomic-feature.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/targeted_loci")

### targeted\_loci Type

`object[]` ([Locus identifier](ega-12-definitions-locus-identifier.md))

### targeted\_loci Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## assay\_technology

Metadata of the assay instrument (e.g. sequencer Illumina NextSeq 500) used to obtain the raw data (e.g. sequence files) of an assay.

`assay_technology`

*   is required

*   Type: `object` ([Assay technology](ega-12-definitions-assay-technology.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-12-definitions-assay-technology.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_technology")

### assay\_technology Type

`object` ([Assay technology](ega-12-definitions-assay-technology.md))

one (and only one) of

*   [Asserting array technology controlled vocabulary (CV)](ega-12-definitions-assay-technology-oneof-asserting-array-technology-controlled-vocabulary-cv.md "check type definition")

*   [Asserting sequencer technology controlled vocabulary (CV)](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv.md "check type definition")

## assay\_type\_descriptor

Node defining the type of assay applicable to the experiment. Consists in an overall category (based on the purpose and technology of the instrument \[EFO:0002773]) and its possible subtype. Both types and subtypes are taken from controlled vocabulary (CV) lists, stored in the controlled\_vocabulary\_schemas folder. For example, in a single cell RNA-seq assay the assay type would be 'assay by high throughput sequencer' \[EFO:0002697] and its subtype 'RNA-seq of coding RNA from single cells' \[EFO:0005684].

`assay_type_descriptor`

*   is required

*   Type: `object` ([Type of assay](ega-9-properties-type-of-assay.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor")

### assay\_type\_descriptor Type

`object` ([Type of assay](ega-9-properties-type-of-assay.md))

any of

*   [Assay subtypes match DNA/RNA assays](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays.md "check type definition")

*   one (and only one) of

    *   [Assay type and subtype terms are from the array CV list](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-array-cv-list.md "check type definition")

    *   [Assay type and subtype terms are from the sequencer CV list](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-sequencer-cv-list.md "check type definition")

## assayed\_molecule\_type

Node containing information about the assayed molecule: the material entity (e.g. DNA) that was used to generate the data. Choose the specific terms if possible (e.g. if the assayed molecule is cDNA, pick 'cDNA' instead of just 'DNA'). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`assayed_molecule_type`

*   is required

*   Type: `string` ([Type of the assayed molecule of the experiment](ega-9-properties-type-of-the-assayed-molecule-of-the-experiment.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-the-assayed-molecule-of-the-experiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assayed_molecule_type")

### assayed\_molecule\_type Type

`string` ([Type of the assayed molecule of the experiment](ega-9-properties-type-of-the-assayed-molecule-of-the-experiment.md))

### assayed\_molecule\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation    |
| :--------------------- | :------------- |
| `"DNA"`                | \[CHEBI:16991] |
| `"RNA"`                | \[CHEBI:33697] |
| `"metabolite"`         | \[EFO:0004727] |
| `"protein"`            | \[CHEBI:36080] |
| `"cDNA"`               | \[EFO:0008481] |
| `"genomic DNA"`        | \[EFO:0008479] |
| `"mitochondrial DNA"`  | \[EFO:0008480] |
| `"messenger RNA"`      | \[CHEBI:33699] |
| `"ncRNA"`              | \[SO:0000655]  |
| `"non polyA RNA"`      | \[EFO:0005017] |
| `"long non polyA RNA"` | \[EFO:0005018] |
| `"nuclear RNA"`        | \[EFO:0030052] |
| `"polyA RNA"`          | \[OBI:0000869] |
| `"long polyA RNA"`     | \[EFO:0005019] |
| `"snRNA"`              | \[SO:0000274]  |
| `"total RNA"`          | \[EFO:0004964] |

## types\_of\_output\_data

Types of data the experiment produces.

`types_of_output_data`

*   is optional

*   Type: `string[]` ([Type of data](ega-12-definitions-type-of-data.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-types-of-output-data.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/types_of_output_data")

### types\_of\_output\_data Type

`string[]` ([Type of data](ega-12-definitions-type-of-data.md))

### types\_of\_output\_data Constraints

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## experiment\_type\_specifications

Node containing additional attributes to describe the experiment, either array experiments (those in which an [array instrument \[EFO:0002698\]](http://www.ebi.ac.uk/efo/EFO_0002698) was used) or sequencing experiments (those in which a [sequencing instrument \[EFO:0003739\]](http://www.ebi.ac.uk/efo/EFO_0003739) was used). For example, if an array was used, its Array Design Format (ADF) will be expected.

`experiment_type_specifications`

*   is required

*   Type: `object` ([Experiment type specifications](ega-9-properties-experiment-type-specifications.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-experiment-type-specifications.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications")

### experiment\_type\_specifications Type

`object` ([Experiment type specifications](ega-9-properties-experiment-type-specifications.md))

one (and only one) of

*   [The sequencing experiment descriptors are required](ega-9-properties-experiment-type-specifications-oneof-the-sequencing-experiment-descriptors-are-required.md "check type definition")

*   [The array experiment descriptors are required](ega-9-properties-experiment-type-specifications-oneof-the-array-experiment-descriptors-are-required.md "check type definition")

## experiment\_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. an experiment being linked to a Sample) the EGA.

`experiment_relationships`

*   is optional

*   Type: an array of merged types ([Details](ega-9-properties-experiment-relationships-items.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-experiment-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_relationships")

### experiment\_relationships Type

an array of merged types ([Details](ega-9-properties-experiment-relationships-items.md))

### experiment\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## experiment\_attributes

Custom attributes of an experiment: reusable attributes to encode tag-value pairs (e.g. Tag being 'additional description' and its Value 'this experiment is a re-do of another 3 experiments due to...') with optional units. Its properties are inherited from the common-definitions.json schema.

`experiment_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-experiment-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_attributes")

### experiment\_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### experiment\_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
