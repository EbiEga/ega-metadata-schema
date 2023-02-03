# Locus identifier Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/targetedLoci/items
```

Node to unambiguously identify loci \[OGI:0000022]: the unique chromosomal location defining the position of an individual gene or DNA sequence. This node shall be used to precisely define: (1) the organism of said locus; (2) the gene and other genomic feature references in other accessions; (3) the genomic sequence per se, including its assembly and position. These details, in different combinations, shall allow identification of any genomic feature, such as SNPs (e.g. coordinates of a variant) or genes (e.g. PT53).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## items Type

`object` ([Locus identifier](ega-4-definitions-locus-identifier.md))

# items Properties

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                            |
| :---------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [organismDescriptor](#organismdescriptor) | `object` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/organismDescriptor")       |
| [lociDescriptor](#locidescriptor)         | `array`  | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-locus-identifier-properties-loci-context-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor") |

## organismDescriptor

This property describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or, like humans, made up of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance.

`organismDescriptor`

*   is required

*   Type: `object` ([Organism \[OBI:0100026\] descriptor block](ega-4-definitions-organism-obi0100026-descriptor-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/organismDescriptor")

### organismDescriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-4-definitions-organism-obi0100026-descriptor-block.md))

## lociDescriptor

Array of locus context items. Multiple loci can be described in the array if the organism remains the same.

`lociDescriptor`

*   is required

*   Type: `object[]` ([Locus context item](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-locus-identifier-properties-loci-context-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor")

### lociDescriptor Type

`object[]` ([Locus context item](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

### lociDescriptor Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
