# Genomic sequence descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor
```

Node used to describe with sufficient detail a genomic sequence (e.g. Human Chromosome X: 71366222-71532374 forward strand), defined as a biological sequence that is of genomic origin (i.e. carries sequence from the genome of a cell or organism).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## genomicSequenceDescriptor Type

`object` ([Genomic sequence descriptor](ega-4-definitions-genomic-sequence-descriptor.md))

any of

*   [Either the full position context is given](ega-4-definitions-genomic-sequence-descriptor-anyof-either-the-full-position-context-is-given.md "check type definition")

*   [Or at least the sequence itself is given](ega-4-definitions-genomic-sequence-descriptor-anyof-or-at-least-the-sequence-itself-is-given.md "check type definition")

# genomicSequenceDescriptor Properties

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                         |
| :------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assemblyDescriptor](#assemblydescriptor)   | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/assemblyDescriptor")                                     |
| [sequenceCoordinates](#sequencecoordinates) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-sequence-coordinates.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/sequenceCoordinates")                                         |
| [dnaSequenceStrand](#dnasequencestrand)     | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-dna-sequence-strand.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/dnaSequenceStrand")                                            |
| [nucleicAcidSequence](#nucleicacidsequence) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/nucleicAcidSequence") |

## assemblyDescriptor

Node describing a sequence assembly referenced in [NCBI's Assembly database](https://www.ncbi.nlm.nih.gov/assembly). Assembly is a database providing information on the structure of assembled genomes, assembly names and other meta-data, statistical reports, and links to genomic sequence data. An assembly is defined as the set of chromosomes, unlocalized and unplaced (sometimes called 'random') and alternate sequences used to represent an organism's genome. Assemblies are constructed from 1 or more assembly units.

`assemblyDescriptor`

*   is optional

*   Type: `object` ([NCBI's Assembly descriptor](ega-4-definitions-ncbis-assembly-descriptor.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/assemblyDescriptor")

### assemblyDescriptor Type

`object` ([NCBI's Assembly descriptor](ega-4-definitions-ncbis-assembly-descriptor.md))

## sequenceCoordinates

A position in a map (for example a genetic map), either a single position (e.g. 71366222) or a region interval (e.g. 71366222-71532374). Used to define coordinates within an assembly unit.

`sequenceCoordinates`

*   is optional

*   Type: `object` ([Sequence coordinates](ega-4-definitions-sequence-coordinates.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-sequence-coordinates.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/sequenceCoordinates")

### sequenceCoordinates Type

`object` ([Sequence coordinates](ega-4-definitions-sequence-coordinates.md))

any of

*   [Either a single position is given](ega-4-definitions-sequence-coordinates-anyof-either-a-single-position-is-given.md "check type definition")

*   [Or the whole sequence interval](ega-4-definitions-sequence-coordinates-anyof-or-the-whole-sequence-interval.md "check type definition")

## dnaSequenceStrand

DNA sequence is double-stranded. By convention, for a reference chromosome, one whole strand is designated the 'forward strand' and the other the 'reverse strand'. This designation is arbitrary and sometimes the terms 'plus strand' and 'minus strand', respectively, are used instead. A genomic feature can live on a DNA strand in one of two orientations. For instance, a gene is said to have a coding strand (also known as its 'sense strand'), and a template strand (also known as its 'antisense strand'), which can be forward or reverse strands depending on which contain the nucleotide sequence the RNA polymerase reads to create its RNA product. Annotations such as Ensembl and UCSC are concerned with the coding sequences of genes, so when they say a gene is on the forward strand, it means the gene's coding sequence is on the forward strand. To follow through again, that means that during transcription of this forward-strand gene, the gene's template sequence is read from the reverse strand, producing an mRNA that matches the sequence on the forward strand. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`dnaSequenceStrand`

*   is optional

*   Type: `string` ([DNA Sequence strand](ega-4-definitions-dna-sequence-strand.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-dna-sequence-strand.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/dnaSequenceStrand")

### dnaSequenceStrand Type

`string` ([DNA Sequence strand](ega-4-definitions-dna-sequence-strand.md))

### dnaSequenceStrand Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation                                                                                                                                                                                                                                                                                              |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"forward"` | Forward strand \[ENSGLOSSARY:0000369]: DNA strand arbitrary defined as the strand with its 5' end at the tip of the short chromosome arm (p). If a gene is forward-stranded, its sense (sequence matching cDNA) is on the forward strand. Forward strand is reverse complementary to the reverse strand. |
| `"reverse"` | Reverse strand \[ENSGLOSSARY:0000370]: DNA strand arbitrary defined as the strand with its 5' end at the tip of the long chromosome arm (q). If a gene is reverse-stranded, its sense (sequence matching cDNA) is on the reverse strand. Reverse strand is reverse complementary to the forward strand.  |

## nucleicAcidSequence

Sequence of characters representing a specific nucleic (i.e. molecular species - e.g. Adenine) or groupings of these (through ambiguity codes), using [one-letter IUPAC abbreviations](https://en.wikipedia.org/wiki/International_Union_of_Pure_and_Applied_Chemistry#Amino_acid_and_nucleotide_base_codes).

`nucleicAcidSequence`

*   is optional

*   Type: `string` ([Nucleic acid sequence](ega-4-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/nucleicAcidSequence")

### nucleicAcidSequence Type

`string` ([Nucleic acid sequence](ega-4-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md))

### nucleicAcidSequence Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([\.-]*[ACGTURYKMSWBDHVNX]+[\.-]*)+$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B%5C.-%5D*%5BACGTURYKMSWBDHVNX%5D%2B%5B%5C.-%5D*\)%2B%24 "try regular expression with regexr.com")

### nucleicAcidSequence Examples

```json
"ACTGCCG"
```

```json
"CTGCGCGCGCT"
```

```json
"KM-AGT-X-N"
```
