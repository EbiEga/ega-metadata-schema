# EGA dataset metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Dataset metadata object. This object is intended to contain metadata about the collection of file-containing objects (ArrayAssay, runs or analyses) subject to controlled access. In other words, a dataset encompasses a set of objects to which access is granted as a whole, since access given to a data requester is access to a dataset, and fall under the same Policy. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/studies>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.dataset.json](../../../schemas/EGA.dataset.json "open original schema") |

## EGA dataset metadata schema Type

`object` ([EGA dataset metadata schema](ega-5.md))

# EGA dataset metadata schema Properties

| Property                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                 |
| :------------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)                             | Merged   | Required | cannot be null | [EGA dataset metadata schema](ega-5-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/objectId")                                     |
| [schemaDescriptor](#schemadescriptor)             | `object` | Optional | cannot be null | [EGA dataset metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/schemaDescriptor")                            |
| [objectTitle](#objecttitle)                       | `string` | Required | cannot be null | [EGA dataset metadata schema](ega-5-properties-title-of-the-dataset.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/objectTitle")                               |
| [objectDescription](#objectdescription)           | `string` | Optional | cannot be null | [EGA dataset metadata schema](ega-5-properties-description-of-the-dataset.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/objectDescription")                   |
| [datasetType](#datasettype)                       | `string` | Required | cannot be null | [EGA dataset metadata schema](ega-5-properties-dataset-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/datasetType")                                       |
| [approximateReleaseDate](#approximatereleasedate) | Merged   | Optional | cannot be null | [EGA dataset metadata schema](ega-5-properties-approximate-release-date-of-the-dataset.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/approximateReleaseDate") |
| [datasetRelationships](#datasetrelationships)     | `array`  | Optional | cannot be null | [EGA dataset metadata schema](ega-5-properties-dataset-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/datasetRelationships")                     |
| [datasetAttributes](#datasetattributes)           | `array`  | Optional | cannot be null | [EGA dataset metadata schema](ega-5-properties-dataset-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/datasetAttributes")                    |

## objectId

Node containing the main identifiers of the object (e.g. alias, centerName...), inherited from the common definitions. #! We extend the core object (objectCoreId) by adding a pattern check based on this schema's nature: an dataset (by using EGADatasetIdPattern)

`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-5-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-5-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-5-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that dataset EGA ID (EGAD) is correct](ega-5-properties-objects-ids-block-allof-check-that-dataset-ega-id-egad-is-correct.md "check type definition")

## schemaDescriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schemaDescriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/schemaDescriptor")

### schemaDescriptor Type

`object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

## objectTitle

Free-form title of the Dataset. It should be the first picture of the dataset content and not contain more than 30 words. It can be used to call out dataset records in searches or displays.

`objectTitle`

*   is required

*   Type: `string` ([Title of the dataset](ega-5-properties-title-of-the-dataset.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-5-properties-title-of-the-dataset.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/objectTitle")

### objectTitle Type

`string` ([Title of the dataset](ega-5-properties-title-of-the-dataset.md))

### objectTitle Examples

```json
"EBI colon cancer dataset"
```

## objectDescription

More extensive free-form description of the Dataset. It should include the content of the dataset (number of samples, file types, technology/protocol used to obtain the data…) and not extend more than 4 sentences.

`objectDescription`

*   is optional

*   Type: `string` ([Description of the dataset](ega-5-properties-description-of-the-dataset.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-5-properties-description-of-the-dataset.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/objectDescription")

### objectDescription Type

`string` ([Description of the dataset](ega-5-properties-description-of-the-dataset.md))

### objectDescription Examples

```json
"This dataset is related to Project X by grant Y and encompasses samples from group Z, whose DNA was hybridized against a microarray designed for SNPs."
```

## datasetType

Type of the dataset, expressing the overall purpose of the dataset. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition. The CV was inherited from ENA's dataset types.

`datasetType`

*   is required

*   Type: `string` ([Dataset type](ega-5-properties-dataset-type.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-5-properties-dataset-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/datasetType")

### datasetType Type

`string` ([Dataset type](ega-5-properties-dataset-type.md))

### datasetType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                                               | Explanation                                                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"whole genome sequencing"`                                         | \[topic:3673]: laboratory technique to sequence the complete DNA sequence of an organism's genome at a single time                                                                                                                                                                                                                                      |
| `"exome sequencing"`                                                | \[EFO:0005396]: exome sequencing, also known as whole exome sequencing (WES), is a genomic technique for sequencing all of the protein-coding regions of genes in a genome (known as the exome). Exons (the subset of DNA that encodes proteins) are selected, and the exonic DNA is then sequenced using any high-throughput DNA sequencing technology |
| `"genotyping by array"`                                             | \[EFO:0002767]: An assay in which an array is used detect polymorphisms in DNA samples                                                                                                                                                                                                                                                                  |
| `"transcriptome profiling by high-throughput sequencing"`           | \[EFO:0002770]: A method used to assess the transcriptome of a biological sample using a high-throughput sequencing platform                                                                                                                                                                                                                            |
| `"transcriptome profiling by array"`                                | \[EFO:0002768]: An assay in which the transcriptome of a biological sample is analysed using array technology                                                                                                                                                                                                                                           |
| `"amplicon sequencing"`                                             | \[EFO:0003747]: An assay in which a DNA or RNA input molecule amplified by PCR is sequenced                                                                                                                                                                                                                                                             |
| `"methylation binding domain sequencing"`                           | \[EFO:0003750]: An assay in which DNA is the input molecule derived from a selection process using methyl binding domain protein to enrich for methylated fractions of DNA, then sequenced using high throughput sequencing                                                                                                                             |
| `"methylation profiling by high-throughput sequencing"`             | \[EFO:0002761]: An assay in which the methylation state of DNA is determined and is compared between samples using sequencing based technology                                                                                                                                                                                                          |
| `"phenotype information"`                                           | \[EFO:0000651]: The observable form taken by some character (or group of characters) in an individual or an organism, excluding pathology and disease. The detectable outward manifestations of a specific genotype                                                                                                                                     |
| `"genomic variant calling"`                                         | \[operation:3227]: Detect, identify and map mutations, such as single nucleotide polymorphisms, short indels and structural variants, in multiple DNA sequences. Typically the alignment and comparison of the fluorescent traces produced by DNA sequencing hardware, to study genomic alterations                                                     |
| `"chromatin accessibility profiling by high-throughput sequencing"` | \[EFO:0007045]: Assay for transposase-accessible chromatin using sequencing (ATAC-seq), is a method based on direct in vitro transposition of sequencing adaptors into native chromatin, and is a rapid and sensitive method for integrative epigenomic analysis. ATAC-seq captures open chromatin sites using a simple two-step protocol               |
| `"histone modification profiling by high-throughput sequencing"`    | Sequencing assay revolving around post-translational processing of amino acids within histone proteins                                                                                                                                                                                                                                                  |
| `"chip-Seq"`                                                        | \[EFO:0002692]: ChIP-seq is an assay in which chromatin immunoprecipitation with high throughput sequencing is used to identify the cistrome of DNA-associated proteins                                                                                                                                                                                 |
| `"study summary information"`                                       | Object containing complementary summaries of other objects                                                                                                                                                                                                                                                                                              |

### datasetType Examples

```json
"whole genome sequencing"
```

## approximateReleaseDate

An approximate date of the desired release of the dataset. Bare in mind that this will NOT automatically release the dataset, but instead may be used to set a reminder to the submitter (and EGA's HelpDesk team) in case the dataset was not released by this time. This would help in cases where this step was forgotten by the submitter or release was stalled for some reason.

`approximateReleaseDate`

*   is optional

*   Type: `string` ([Approximate release date of the dataset](ega-5-properties-approximate-release-date-of-the-dataset.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-5-properties-approximate-release-date-of-the-dataset.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/approximateReleaseDate")

### approximateReleaseDate Type

`string` ([Approximate release date of the dataset](ega-5-properties-approximate-release-date-of-the-dataset.md))

all of

*   [Pattern of EGA ISO 8601 date](ega-4-definitions-pattern-of-ega-iso-8601-date.md "check type definition")

*   [We cap the reminder up to 3 years](ega-5-properties-approximate-release-date-of-the-dataset-allof-we-cap-the-reminder-up-to-3-years.md "check type definition")

### approximateReleaseDate Examples

```json
"2023-12-01"
```

```json
"2024-01-10"
```

## datasetRelationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. a policy being linked to a dataset) the EGA.

`datasetRelationships`

*   is optional

*   Type: an array of merged types ([Details](ega-5-properties-dataset-relationships-items.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-5-properties-dataset-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/datasetRelationships")

### datasetRelationships Type

an array of merged types ([Details](ega-5-properties-dataset-relationships-items.md))

### datasetRelationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## datasetAttributes

Custom attributes of a dataset: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

`datasetAttributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-5-properties-dataset-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/datasetAttributes")

### datasetAttributes Type

`object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

### datasetAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
