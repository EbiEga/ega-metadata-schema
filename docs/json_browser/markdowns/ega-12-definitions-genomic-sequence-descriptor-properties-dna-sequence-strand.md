# DNA Sequence strand Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/dna_sequence_strand
```

DNA sequence is double-stranded. By convention, for a reference chromosome, one whole strand is designated the 'forward strand' and the other the 'reverse strand'. This designation is arbitrary and sometimes the terms 'plus strand' and 'minus strand', respectively, are used instead. A genomic feature can live on a DNA strand in one of two orientations. For instance, a gene is said to have a coding strand (also known as its 'sense strand'), and a template strand (also known as its 'antisense strand'), which can be forward or reverse strands depending on which contain the nucleotide sequence the RNA polymerase reads to create its RNA product. Annotations such as Ensembl and UCSC are concerned with the coding sequences of genes, so when they say a gene is on the forward strand, it means the gene's coding sequence is on the forward strand. To follow through again, that means that during transcription of this forward-strand gene, the gene's template sequence is read from the reverse strand, producing an mRNA that matches the sequence on the forward strand. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## dna_sequence_strand Type

`string` ([DNA Sequence strand](ega-12-definitions-genomic-sequence-descriptor-properties-dna-sequence-strand.md))

## dna_sequence_strand Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation                          |
| :---------- | :----------------------------------- |
| `"forward"` |                                      |
| `"reverse"` | function reverse() { [native code] } |
