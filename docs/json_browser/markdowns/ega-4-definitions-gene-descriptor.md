# Gene descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor
```

Node to uniquely identify a gene \[SO:0000704]: a region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene may include regulatory regions, transcribed regions and/or other functional sequence regions. For human genes, the standard is to use nomenclature provided by the HUGO Gene Nomenclature Committee (HGNC).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## geneDescriptor Type

`object` ([Gene descriptor](ega-4-definitions-gene-descriptor.md))

# geneDescriptor Properties

| Property                                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                       |
| :---------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [geneIdentifier](#geneidentifier)                     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-gene-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneIdentifier")                                 |
| [geneDescription](#genedescription)                   | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-description-of-the-gene.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneDescription")                        |
| [alternateGeneIdentifiers](#alternategeneidentifiers) | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneIdentifiers")            |
| [relatedGeneIdentifiers](#relatedgeneidentifiers)     | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-related-not-equivalent-gene-identifiers.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/relatedGeneIdentifiers") |

## geneIdentifier

Property uniquely identifying a gene. It consists of a 'termId' and 'termLabel', which correspond to: (1)  'termId': A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol (e.g. HGNC:11535 for gene TAF1). There are 2 types of allowed databases to reference: NCBIGene and HGNC. Other archives' accessions (e.g. ensembl:ENSDARG00000035330) can be cross referenced with NCBIGene to obtain its gene ID (e.g. ncbigene:555452). (2) 'termLabel': the official gene symbol (e.g. 'TAF1'). It is typically derived from the gene name. There are several resources to search for a gene of interest, although we recommend [NCBI's service](https://www.ncbi.nlm.nih.gov/gene). For example: in the case of human genes, the symbol follows [HGNC](https://www.genenames.org/)'s nomenclature, while in the case of mice genes they are provided by [MGI](http://www.informatics.jax.org/).

`geneIdentifier`

*   is required

*   Type: `object` ([Gene identifier](ega-4-definitions-gene-descriptor-properties-gene-identifier.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-gene-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneIdentifier")

### geneIdentifier Type

`object` ([Gene identifier](ega-4-definitions-gene-descriptor-properties-gene-identifier.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

## geneDescription

Free-text description of the gene, only to be used to provide additional context that would otherwise be impossible to add encoded in the schema. In other words, kindly refrain from providing alternative gene identifiers in the description, when they could be added at 'alternateGeneIdentifiers'.

`geneDescription`

*   is optional

*   Type: `string` ([Description of the gene](ega-4-definitions-gene-descriptor-properties-description-of-the-gene.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-description-of-the-gene.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneDescription")

### geneDescription Type

`string` ([Description of the gene](ega-4-definitions-gene-descriptor-properties-description-of-the-gene.md))

### geneDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### geneDescription Examples

```json
"In the mutated cells, the only difference with the reference gene is that at locus ... position +23 was modified: thymine was transitioned to cytosine (T-C)..."
```

## alternateGeneIdentifiers

Array of alternate identifiers for this gene. This array can be used to provide any other alternate gene identifiers that refer to a gene, including previously approved gene symbols, Ensembl identifiers, gene transcripts (e.g. 'ensembl:ENST00000423759'), etcetera.

`alternateGeneIdentifiers`

*   is optional

*   Type: `object[]` ([Alternate gene identifier item](ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers-alternate-gene-identifier-item.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneIdentifiers")

### alternateGeneIdentifiers Type

`object[]` ([Alternate gene identifier item](ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers-alternate-gene-identifier-item.md))

### alternateGeneIdentifiers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## relatedGeneIdentifiers

Array of related identifiers (e.g. termIds 'VGNC:97422', 'MGI:2385071', 'RGD:1305712' for gene ETF1). This field can be used to provide identifiers to resources representing related, but not equivalent gene identifiers. For example: paralog, analog or ortholog identifiers.

`relatedGeneIdentifiers`

*   is optional

*   Type: `object[]` ([Related gene identifier item](ega-4-definitions-gene-descriptor-properties-related-not-equivalent-gene-identifiers-related-gene-identifier-item.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-related-not-equivalent-gene-identifiers.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/relatedGeneIdentifiers")

### relatedGeneIdentifiers Type

`object[]` ([Related gene identifier item](ega-4-definitions-gene-descriptor-properties-related-not-equivalent-gene-identifiers-related-gene-identifier-item.md))

### relatedGeneIdentifiers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
