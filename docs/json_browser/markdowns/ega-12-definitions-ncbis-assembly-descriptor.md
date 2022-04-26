# NCBI's Assembly descriptor Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/assembly_descriptor
```

Node describing a sequence assembly referenced in [NCBI's Assembly database](https://www.ncbi.nlm.nih.gov/assembly). Assembly is a database providing information on the structure of assembled genomes, assembly names and other meta-data, statistical reports, and links to genomic sequence data. An assembly is defined as the set of chromosomes, unlocalized and unplaced (sometimes called 'random') and alternate sequences used to represent an organism's genome. Assemblies are constructed from 1 or more assembly units.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## assembly\_descriptor Type

`object` ([NCBI's Assembly descriptor](ega-12-definitions-ncbis-assembly-descriptor.md))

any of

*   [Or the Assembly accession is required](ega-12-definitions-ncbis-assembly-descriptor-anyof-or-the-assembly-accession-is-required.md "check type definition")

*   [Or the Assembly unit accession is required](ega-12-definitions-ncbis-assembly-descriptor-anyof-or-the-assembly-unit-accession-is-required.md "check type definition")

# assembly\_descriptor Properties

| Property                                                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                             |
| :--------------------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assembly\_name](#assembly_name)                                 | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_name")                        |
| [ncbi\_assembly\_accession](#ncbi_assembly_accession)            | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_accession")           |
| [assembly\_unit\_name](#assembly_unit_name)                      | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_unit_name")              |
| [ncbi\_assembly\_unit\_accession](#ncbi_assembly_unit_accession) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_unit_accession") |

## assembly\_name

A free-text common name (e.g. 'GRCh38') that is used to denote the sequence assembly.

`assembly_name`

*   is optional

*   Type: `string` ([Assembly common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_name")

### assembly\_name Type

`string` ([Assembly common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md))

### assembly\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### assembly\_name Examples

```json
"GRCh38.p14"
```

```json
"GRCh38"
```

```json
"GRCh37.p13"
```

```json
"GRCh37"
```

## ncbi\_assembly\_accession

Assembly's identifier (e.g. GCF\_000001405.26) of the assembly. For example, the assembly accession for the GenBank version of the public human reference assembly (GRCh38.p14) is GCA\_000001405.29. See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

`ncbi_assembly_accession`

*   is optional

*   Type: `string` ([NCBI Assembly accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_accession")

### ncbi\_assembly\_accession Type

`string` ([NCBI Assembly accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md))

all of

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

### ncbi\_assembly\_accession Examples

```json
"assembly:GCF_000001405.26"
```

```json
"assembly:GCA_000001405.1"
```

```json
"assembly:GCF_000005845.2"
```

## assembly\_unit\_name

A free-text common name (e.g. 'chr17') that is used to denote the sequence assembly unit.

`assembly_unit_name`

*   is optional

*   Type: `string` ([Assembly unit common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_unit_name")

### assembly\_unit\_name Type

`string` ([Assembly unit common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md))

### assembly\_unit\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### assembly\_unit\_name Examples

```json
"Chromosome 2"
```

```json
"MT"
```

```json
"chr17"
```

```json
"chr20"
```

```json
"18"
```

## ncbi\_assembly\_unit\_accession

NCBI's identifier (e.g. ) of the assembly unit. An assembly unit is defined as the collection of sequences used to define discrete parts of an assembly. Commonly assembly units are entire chromosomes (e.g. Chromosome 1 of human genome), scaffolds or different types of sequences (e.g. Mitochondrial DNA). For example, GenBank's accession: (1) for the assembly unit of the human chromosome 1 is [NC\_000001.11](https://www.ncbi.nlm.nih.gov/nuccore/NC_000001.11) (for the human reference assembly GRCh38.p14); (2) and for the complete mitochondrion genome of a human it is [NC\_012920.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_012920.1). See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

`ncbi_assembly_unit_accession`

*   is optional

*   Type: `string` ([NCBI Assembly unit accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_unit_accession")

### ncbi\_assembly\_unit\_accession Type

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

### ncbi\_assembly\_unit\_accession Examples

```json
"refseq:NC_000001.11"
```

```json
"refseq:NC_012920.1"
```
