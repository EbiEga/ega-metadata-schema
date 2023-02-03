# Reference assembly and sequence details Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/referenceAlignmentDetails
```

Node containing the information of the reference assembly that was used to obtain the sequence alignment. For example, processing raw sequence FastQ files aligning it to a reference sequence (e.g. human Chromosome X of GRCh38's assembly), obtaining aligned sequences (e.g. BAM format). In this array one can list the used assembly (e.g. GRCh38.p14), the used assembly units (e.g. refseq:NC\_000001.11), or a combination of both. In order to ease the interpretation of the data, it is important to notice that the field 'assemblyUnitName' shall correspond to how the Reference Sequence is labelled in submission file(s) (e.g. '1' for chromosome 1). This name is equivalent to the SQ label (the reference sequence dictionary) in BAM (see [documentation for v1](https://samtools.github.io/hts-specs/SAMv1.pdf)) and optional when submitted file uses INSDC accession.version

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## referenceAlignmentDetails Type

`object[]` ([NCBI's Assembly descriptor](ega-4-definitions-ncbis-assembly-descriptor.md))

## referenceAlignmentDetails Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
