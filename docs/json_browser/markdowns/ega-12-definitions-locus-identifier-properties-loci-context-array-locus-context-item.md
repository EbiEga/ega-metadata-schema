# Locus context item Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor/items
```

Node providing the context of the locus: its sequence, coordinates, encompassed genes...

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([Locus context item](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

any of

*   [Either the gene description is given](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item-anyof-either-the-gene-description-is-given.md "check type definition")

*   [Or the genomic sequence context](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item-anyof-or-the-genomic-sequence-context.md "check type definition")

*   [Or an external reference to the locus context](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item-anyof-or-an-external-reference-to-the-locus-context.md "check type definition")

# items Properties

| Property                                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                     |
| :-------------------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [gene\_descriptor](#gene_descriptor)                            | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor/items/properties/gene_descriptor")                                                                                                               |
| [genomic\_sequence\_descriptor](#genomic_sequence_descriptor)   | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-genomic-sequence-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor/items/properties/genomic_sequence_descriptor")                                                                                       |
| [locus\_external\_reference](#locus_external_reference)         | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor/items/properties/locus_external_reference")                                                                           |
| [locus\_additional\_description](#locus_additional_description) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item-properties-additional-description-of-the-locus.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor/items/properties/locus_additional_description") |

## gene\_descriptor

Node to uniquely identify a gene \[SO:0000704]: a region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene may include regulatory regions, transcribed regions and/or other functional sequence regions. For human genes, the standard is to use nomenclature provided by the HUGO Gene Nomenclature Committee (HGNC).

`gene_descriptor`

*   is optional

*   Type: `object` ([Gene descriptor](ega-12-definitions-gene-descriptor.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor/items/properties/gene_descriptor")

### gene\_descriptor Type

`object` ([Gene descriptor](ega-12-definitions-gene-descriptor.md))

## genomic\_sequence\_descriptor

Node used to describe with sufficient detail a genomic sequence (e.g. Human Chromosome X: 71366222-71532374 forward strand), defined as a biological sequence that is of genomic origin (i.e. carries sequence from the genome of a cell or organism).

`genomic_sequence_descriptor`

*   is optional

*   Type: `object` ([Genomic sequence descriptor](ega-12-definitions-genomic-sequence-descriptor.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-genomic-sequence-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor/items/properties/genomic_sequence_descriptor")

### genomic\_sequence\_descriptor Type

`object` ([Genomic sequence descriptor](ega-12-definitions-genomic-sequence-descriptor.md))

any of

*   [Either the full position context is given](ega-12-definitions-genomic-sequence-descriptor-anyof-either-the-full-position-context-is-given.md "check type definition")

*   [Or at least the sequence itself is given](ega-12-definitions-genomic-sequence-descriptor-anyof-or-at-least-the-sequence-itself-is-given.md "check type definition")

## locus\_external\_reference

External accession node containing the object accession (i.e. unique identifier -  each following their respective formats) assigned by other archives (e.g. biosample, ena, ensembl...) and an optional label to add context to the reference.

`locus_external_reference`

*   is optional

*   Type: `object` ([Object of external accession of the object](ega-12-definitions-object-of-external-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor/items/properties/locus_external_reference")

### locus\_external\_reference Type

`object` ([Object of external accession of the object](ega-12-definitions-object-of-external-accession-of-the-object.md))

### locus\_external\_reference Examples

```json
"ensembl:ENST00000423759.6"
```

## locus\_additional\_description

Optional free-text description of the locus to add any additional context.

`locus_additional_description`

*   is optional

*   Type: `string` ([Additional description of the locus](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item-properties-additional-description-of-the-locus.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item-properties-additional-description-of-the-locus.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor/items/properties/locus_additional_description")

### locus\_additional\_description Type

`string` ([Additional description of the locus](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item-properties-additional-description-of-the-locus.md))

### locus\_additional\_description Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### locus\_additional\_description Examples

```json
"Targeted locus number 1 out of 3 possible loci that our experimental procedure aimed at."
```

```json
"The locus corresponds to a variant version of the defined gene, only existing in patients with X disease."
```
