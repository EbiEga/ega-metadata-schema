# Gene descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor
```

Node to uniquely identify a gene \[SO:0000704]: a region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene may include regulatory regions, transcribed regions and/or other functional sequence regions. For human genes, the standard is to use nomenclature provided by the HUGO Gene Nomenclature Committee (HGNC).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## geneDescriptor Type

`object` ([Gene descriptor](ega-12-definitions-gene-descriptor.md))

# geneDescriptor Properties

| Property                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                |
| :------------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [geneSymbol](#genesymbol)                         | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-symbol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneSymbol")                                 |
| [geneIdCurie](#geneidcurie)                       | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneIdCurie")                              |
| [geneDescription](#genedescription)               | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneDescription")                |
| [alternateGeneIds](#alternategeneids)             | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneIds")                    |
| [alternateGeneSymbols](#alternategenesymbols)     | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneSymbols")            |
| [geneExternalReferences](#geneexternalreferences) | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneExternalReferences") |

## geneSymbol

The official gene symbol. It is typically derived from the gene name. This optional field exists to provide the common identifier of the gene. There are several resources to search for a gene of interest, although we recommend [NCBI's service](https://www.ncbi.nlm.nih.gov/gene). For example: (1) in the case of human genes, the symbol follows [HGNC](https://www.genenames.org/)'s nomenclature; (2) while in the case of mice genes they are provided by [MGI](http://www.informatics.jax.org/).

`geneSymbol`

*   is optional

*   Type: `string` ([Gene Symbol](ega-12-definitions-gene-descriptor-properties-gene-symbol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-symbol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneSymbol")

### geneSymbol Type

`string` ([Gene Symbol](ega-12-definitions-gene-descriptor-properties-gene-symbol.md))

### geneSymbol Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### geneSymbol Examples

```json
"TAF1"
```

```json
"TP53"
```

```json
"BRAF"
```

```json
"16S"
```

## geneIdCurie

A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol (e.g. HGNC:11535 for gene TAF1). The identifier has to follow CURIE format. Additionally, there are 2 types of allowed databases to reference: NCBIGene and HGNC. Other archives' accessions (e.g. ensembl:ENSDARG00000035330) can be cross referenced with NCBIGene to obtain its gene ID (e.g. ncbigene:555452).

`geneIdCurie`

*   is required

*   Type: `string` ([Gene CURIE ID](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneIdCurie")

### geneIdCurie Type

`string` ([Gene CURIE ID](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md))

one (and only one) of

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-ncbi-gene-identifier-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-hgnc-identifier-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

### geneIdCurie Examples

```json
"HGNC:11535"
```

```json
"hgnc:11998"
```

```json
"HGNC:1097"
```

```json
"ncbigene:100010"
```

```json
"ncbigene:6872"
```

## geneDescription

Free-text description of the gene, only to be used to provide additional context that would otherwise be impossible to add encoded in the schema. In other words, kindly refrain from providing alternative gene symbols in the description if they are not added likewise in the 'alternateGeneSymbols' property.

`geneDescription`

*   is optional

*   Type: `string` ([Description of the gene](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneDescription")

### geneDescription Type

`string` ([Description of the gene](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md))

### geneDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### geneDescription Examples

```json
"In the used cells, locus of gene ... was modified at positions +23, where thymine was transitioned to cytosine (T-C)..."
```

## alternateGeneIds

Array of alternate identifiers for this gene. For example, Ensemble identifiers for genes and its transcripts.

`alternateGeneIds`

*   is optional

*   Type: `string[]` ([Alternate gene ID](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids-alternate-gene-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneIds")

### alternateGeneIds Type

`string[]` ([Alternate gene ID](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids-alternate-gene-id.md))

### alternateGeneIds Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## alternateGeneSymbols

Array of alternate gene sumbols. This field can be used to provide any other alternate gene symbol to refer to the gene, including previously approved gene symbols. There are several resources to search for a gene of interest, although we recommend [NCBI's service](https://www.ncbi.nlm.nih.gov/gene). For example: (1) in the case of human genes, the symbol follows [HGNC](https://www.genenames.org/)'s nomenclature; (2) while in the case of mice genes they are provided by [MGI](http://www.informatics.jax.org/).

`alternateGeneSymbols`

*   is optional

*   Type: `string[]` ([Alternate gene symbol](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols-alternate-gene-symbol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneSymbols")

### alternateGeneSymbols Type

`string[]` ([Alternate gene symbol](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols-alternate-gene-symbol.md))

### alternateGeneSymbols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## geneExternalReferences

Array of related identifiers. This field can be used to provide identifiers to alternative resources representing related, but not equivalent concepts, for example gene paralog, analog or ortholog IDs.

`geneExternalReferences`

*   is optional

*   Type: `string[]` ([Related gene ID](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids-related-gene-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneExternalReferences")

### geneExternalReferences Type

`string[]` ([Related gene ID](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids-related-gene-id.md))

### geneExternalReferences Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
