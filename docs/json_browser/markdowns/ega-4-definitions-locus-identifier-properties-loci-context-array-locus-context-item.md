# Locus context item Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor/items
```

Node providing the context of the locus: its sequence, coordinates, encompassed genes...

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([Locus context item](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

any of

*   [Either the gene description is given](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item-anyof-either-the-gene-description-is-given.md "check type definition")

*   [Or the genomic sequence context](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item-anyof-or-the-genomic-sequence-context.md "check type definition")

*   [Or an external reference to the locus context](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item-anyof-or-an-external-reference-to-the-locus-context.md "check type definition")

# items Properties

| Property                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                          |
| :-------------------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [geneDescriptor](#genedescriptor)                         | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-gene-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor/items/properties/geneDescriptor")                                                                                                              |
| [genomicSequenceDescriptor](#genomicsequencedescriptor)   | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-genomic-sequence-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor/items/properties/genomicSequenceDescriptor")                                                                                       |
| [locusExternalReference](#locusexternalreference)         | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-object-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor/items/properties/locusExternalReference")                                                                                            |
| [locusAdditionalDescription](#locusadditionaldescription) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item-properties-additional-description-of-the-locus.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor/items/properties/locusAdditionalDescription") |

## geneDescriptor

Node to uniquely identify a gene \[SO:0000704]: a region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene may include regulatory regions, transcribed regions and/or other functional sequence regions. For human genes, the standard is to use nomenclature provided by the HUGO Gene Nomenclature Committee (HGNC).

`geneDescriptor`

*   is optional

*   Type: `object` ([Gene descriptor](ega-4-definitions-gene-descriptor.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-gene-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor/items/properties/geneDescriptor")

### geneDescriptor Type

`object` ([Gene descriptor](ega-4-definitions-gene-descriptor.md))

## genomicSequenceDescriptor

Node used to describe with sufficient detail a genomic sequence (e.g. Human Chromosome X: 71366222-71532374 forward strand), defined as a biological sequence that is of genomic origin (i.e. carries sequence from the genome of a cell or organism).

`genomicSequenceDescriptor`

*   is optional

*   Type: `object` ([Genomic sequence descriptor](ega-4-definitions-genomic-sequence-descriptor.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-genomic-sequence-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor/items/properties/genomicSequenceDescriptor")

### genomicSequenceDescriptor Type

`object` ([Genomic sequence descriptor](ega-4-definitions-genomic-sequence-descriptor.md))

any of

*   [Either the full position context is given](ega-4-definitions-genomic-sequence-descriptor-anyof-either-the-full-position-context-is-given.md "check type definition")

*   [Or at least the sequence itself is given](ega-4-definitions-genomic-sequence-descriptor-anyof-or-at-least-the-sequence-itself-is-given.md "check type definition")

## locusExternalReference

External accession property defining a reference to an external record in another resource. For example, a reference to a sequence deposited in NCBI's Nucleotide database (e.g. '<https://identifiers.org/nucleotide:T35715.1>'); or a sample record in BioSamples (e.g. '<https://identifiers.org/biosample:SAMEA7616999>').

`locusExternalReference`

*   is optional

*   Type: `object` ([Object External accession](ega-4-definitions-object-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-object-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor/items/properties/locusExternalReference")

### locusExternalReference Type

`object` ([Object External accession](ega-4-definitions-object-external-accession.md))

any of

*   [Either the identifier is needed](ega-4-definitions-object-external-accession-anyof-either-the-identifier-is-needed.md "check type definition")

*   [Or the reference is needed](ega-4-definitions-object-external-accession-anyof-or-the-reference-is-needed.md "check type definition")

## locusAdditionalDescription

Optional free-text description of the locus to add any additional context.

`locusAdditionalDescription`

*   is optional

*   Type: `string` ([Additional description of the locus](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item-properties-additional-description-of-the-locus.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item-properties-additional-description-of-the-locus.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor/items/properties/locusAdditionalDescription")

### locusAdditionalDescription Type

`string` ([Additional description of the locus](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item-properties-additional-description-of-the-locus.md))

### locusAdditionalDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### locusAdditionalDescription Examples

```json
"Targeted locus number 1 out of 3 possible loci that our experimental procedure aimed at."
```

```json
"The locus corresponds to a variant version of the defined gene, only existing in patients with X disease."
```
