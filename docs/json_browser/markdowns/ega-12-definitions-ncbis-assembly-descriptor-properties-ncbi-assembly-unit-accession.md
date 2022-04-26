# NCBI Assembly unit accession Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_unit_accession
```

NCBI's identifier (e.g. ) of the assembly unit. An assembly unit is defined as the collection of sequences used to define discrete parts of an assembly. Commonly assembly units are entire chromosomes (e.g. Chromosome 1 of human genome), scaffolds or different types of sequences (e.g. Mitochondrial DNA). For example, GenBank's accession: (1) for the assembly unit of the human chromosome 1 is [NC\_000001.11](https://www.ncbi.nlm.nih.gov/nuccore/NC_000001.11) (for the human reference assembly GRCh38.p14); (2) and for the complete mitochondrion genome of a human it is [NC\_012920.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_012920.1). See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## ncbi\_assembly\_unit\_accession Type

`string` ([NCBI Assembly unit accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-accession.md))

all of

*   one (and only one) of

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

## ncbi\_assembly\_unit\_accession Examples

```json
"refseq:NC_000001.11"
```

```json
"refseq:NC_012920.1"
```
