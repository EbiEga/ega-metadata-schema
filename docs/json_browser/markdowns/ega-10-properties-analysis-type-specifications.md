# Analysis type specifications Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_type_specifications
```

Node containing different sets of fields that depend on the specific analysis type. Depending on the analysis types different metadata will be required.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## analysis\_type\_specifications Type

`object` ([Analysis type specifications](ega-10-properties-analysis-type-specifications.md))

# analysis\_type\_specifications Properties

| Property                                                      | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                 |
| :------------------------------------------------------------ | :------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [analysis\_types](#analysis_types)                            | `array` | Required | cannot be null | [EGA analysis metadata schema](ega-10-properties-analysis-type-specifications-properties-list-of-analysis-types.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_type_specifications/properties/analysis_types") |
| [reference\_alignment\_details](#reference_alignment_details) | `array` | Optional | cannot be null | [EGA analysis metadata schema](ega-12-definitions-reference-assembly-and-sequence-details.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_type_specifications/properties/reference_alignment_details")          |

## analysis\_types

Array of all analysis types applicable to this analysis. Details on how the analysis was performed (instruments, software, procedure...) shall be included in the 'analysis\_protocols' field, not here. For example, if the analysis includes sequence variation files (e.g. VCF) that were obtained by a sequencing assay (i.e. from the sequenced reads), at least the analysis type 'sequence variation' would be expected. Furthermore, depending on the types of analysis, different details may be required (e.g. reference sequence details in a 'sequence alignment' type).

`analysis_types`

*   is required

*   Type: `string[]` ([Type of analysis](ega-10-properties-analysis-type-specifications-properties-list-of-analysis-types-type-of-analysis.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-analysis-type-specifications-properties-list-of-analysis-types.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_type_specifications/properties/analysis_types")

### analysis\_types Type

`string[]` ([Type of analysis](ega-10-properties-analysis-type-specifications-properties-list-of-analysis-types-type-of-analysis.md))

### analysis\_types Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## reference\_alignment\_details

Node containing the information of the reference assembly that was used to obtain the sequence alignment. For example, processing raw sequence FastQ files aligning it to a reference sequence (e.g. human Chromosome X of GRCh38's assembly), obtaining aligned sequences (e.g. BAM format). In this array one can list the used assembly (e.g. GRCh38.p14), the used assembly units (e.g. refseq:NC\_000001.11), or a combination of both. In order to ease the interpretation of the data, it is important to notice that the field 'assembly\_unit\_name' shall correspond to how the Reference Sequence is labelled in submission file(s) (e.g. '1' for chromosome 1). This name is equivalent to the SQ label (the reference sequence dictionary) in BAM (see [documentation for v1](https://samtools.github.io/hts-specs/SAMv1.pdf)) and optional when submitted file uses INSDC accession.version

`reference_alignment_details`

*   is optional

*   Type: `object[]` ([NCBI's Assembly descriptor](ega-12-definitions-ncbis-assembly-descriptor.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-12-definitions-reference-assembly-and-sequence-details.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_type_specifications/properties/reference_alignment_details")

### reference\_alignment\_details Type

`object[]` ([NCBI's Assembly descriptor](ega-12-definitions-ncbis-assembly-descriptor.md))

### reference\_alignment\_details Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
