# RefSeq accessions' \[data:1098] CURIE pattern Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_unit_accession/allOf/0
```

The Reference Sequence (RefSeq) CURIEs take the structure of `refseq`:`accession`. [RefSeq accessions](https://registry.identifiers.org/registry/refseq) \[data:1098] have special prefixes (e.g. 'NM\_' for protein-coding transcripts - mRNA) based on the category of the object. The accession can also have a version attached as a suffix (e.g. '.23'). Their records are integrated into [NCBI's resources](https://www.ncbi.nlm.nih.gov/refseq/) including the Nucleotide, Protein, and BLAST databases and can be easily identified by the keyword 'RefSeq' and by their distinct accession prefixes that define their type (see further details at [doi:10.1093/nar/gkv1189](https://academic.oup.com/nar/article/44/D1/D733/2502674).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 0 Type

`string` ([RefSeq accessions' \[data:1098\] CURIE pattern](ega-12-definitions-refseq-accessions-data1098-curie-pattern.md))

one (and only one) of

*   [NC - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nc---molecule-type-dna.md "check type definition")

*   [AC - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-ac---molecule-type-dna.md "check type definition")

*   [NZ - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nz---molecule-type-dna.md "check type definition")

*   [NT - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nt---molecule-type-dna.md "check type definition")

*   [NW - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nw---molecule-type-dna.md "check type definition")

*   [NG - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-ng---molecule-type-dna.md "check type definition")

*   [NM - Molecule type: mRNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nm---molecule-type-mrna.md "check type definition")

*   [XM - Molecule type: mRNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-xm---molecule-type-mrna.md "check type definition")

*   [NR - Molecule type: RNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nr---molecule-type-rna.md "check type definition")

*   [XR - Molecule type: RNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-xr---molecule-type-rna.md "check type definition")

*   [NP - Molecule type: protein](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-np---molecule-type-protein.md "check type definition")

*   [AP - Molecule type: protein](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-ap---molecule-type-protein.md "check type definition")

*   [XP - Molecule type: protein](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-xp---molecule-type-protein.md "check type definition")

*   [YP - Molecule type: protein](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-yp---molecule-type-protein.md "check type definition")

*   [WP - Molecule type: protein](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-wp---molecule-type-protein.md "check type definition")

## 0 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(RefSeq|refseq):
```

[try pattern](https://regexr.com/?expression=%5E\(RefSeq%7Crefseq\)%3A "try regular expression with regexr.com")

## 0 Examples

```json
"NC_001502.1"
```

```json
"NZ_AP024564.1"
```

```json
"NG_046887.1"
```

```json
"NP_001006685.1"
```

```json
"NZ_AMGO01000001.1"
```
