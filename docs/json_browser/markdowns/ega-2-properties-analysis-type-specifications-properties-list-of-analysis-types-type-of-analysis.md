# Type of analysis Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisTypeSpecifications/properties/analysisTypes/items
```

Overall type of the analysis. Term chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## items Type

`string` ([Type of analysis](ega-2-properties-analysis-type-specifications-properties-list-of-analysis-types-type-of-analysis.md))

## items Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                          | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :----------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"sequence variation"`         | sequence variation\_\_ERO:0100211: Analysis of variations at specific loci in the genomes of organisms (mutation and polymorphism) across or within a species, population, or individual (e.g healthy vs diseased tissue).                                                                                                                                                                                                                                                        |
| `"sequence alignment"`         | sequence alignment\_\_ERO:0100032: objective to display graphically how the sequences of two or more macromolecules align along a linear axis.                                                                                                                                                                                                                                                                                                                                    |
| `"phenotype characterization"` | phenotype characterization\_\_ERO:0000923: The result of an organismal assay that involves characterization of a phenotype; any observable characteristic or trait of an organism: such as its morphology, development, biochemical or physiological properties, behavior, and products of behavior (such as a bird's nest). Phenotypes result from the expression of an organism's genes as well as the influence of environmental factors and the interactions between the two. |
| `"sequence annotation"`        | sequence annotation\_\_operation:0361: Analysis where molecular sequence records are annotated with terms from a controlled vocabulary. For submitting sequence annotation files, which are usually 'tab' files. Examples include gene count and OTU tables from metagenomic studies.                                                                                                                                                                                             |
| `"sequence assembly"`          | sequence assembly\_\_topic:0196: The assembly of fragments of a DNA sequence to reconstruct the original sequence.                                                                                                                                                                                                                                                                                                                                                                |
| `"gene expression"`            | gene expression\_\_topic:0203: The analysis of levels and patterns of synthesis of gene products (proteins and functional RNA) including interpretation in functional terms of gene expression data.                                                                                                                                                                                                                                                                              |
