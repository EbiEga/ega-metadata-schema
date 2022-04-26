# Locus identifier Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/targeted_loci/items
```

Node to unambiguously identify loci \[OGI:0000022]: the unique chromosomal location defining the position of an individual gene or DNA sequence. This node shall be used to precisely define: (1) the organism of said locus; (2) the gene and other genomic feature references in other accessions; (3) the genomic sequence per se, including its assembly and position. These details, in different combinations, shall allow identification of any genomic feature, such as SNPs (e.g. coordinates of a variant) or genes (e.g. PT53).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## items Type

`object` ([Locus identifier](ega-12-definitions-locus-identifier.md))

# items Properties

| Property                                     | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                     |
| :------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [organism\_descriptor](#organism_descriptor) | `object` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/organism_descriptor")       |
| [loci\_descriptor](#loci_descriptor)         | `array`  | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-locus-identifier-properties-loci-context-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor") |

## organism\_descriptor

This node describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or made up, like humans, of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance by default.

`organism_descriptor`

*   is required

*   Type: `object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/organism_descriptor")

### organism\_descriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

## loci\_descriptor

Array of locus context items. Multiple loci can be described in the array if the organism remains the same.

`loci_descriptor`

*   is required

*   Type: `object[]` ([Locus context item](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-locus-identifier-properties-loci-context-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor")

### loci\_descriptor Type

`object[]` ([Locus context item](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

### loci\_descriptor Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
