# Dataset type Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/datasetType
```

Type of the dataset, expressing the overall purpose of the dataset. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition. The CV was inherited from ENA's dataset types.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.dataset.json\*](../../../schemas/EGA.dataset.json "open original schema") |

## datasetType Type

`string` ([Dataset type](ega-5-properties-dataset-type.md))

## datasetType Constraints

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

## datasetType Examples

```json
"whole genome sequencing"
```
