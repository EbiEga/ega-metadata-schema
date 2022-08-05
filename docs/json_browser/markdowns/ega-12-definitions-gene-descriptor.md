# Gene descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor/items/properties/gene_descriptor
```

Node to uniquely identify a gene \[SO:0000704]: a region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene may include regulatory regions, transcribed regions and/or other functional sequence regions. For human genes, the standard is to use nomenclature provided by the HUGO Gene Nomenclature Committee (HGNC).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## gene\_descriptor Type

`object` ([Gene descriptor](ega-12-definitions-gene-descriptor.md))

# gene\_descriptor Properties

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                   |
| :------------------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [gene\_symbol](#gene_symbol)                            | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-symbol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_symbol")                                  |
| [gene\_id\_curie](#gene_id_curie)                       | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_id_curie")                              |
| [gene\_description](#gene_description)                  | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_description")                 |
| [alternate\_gene\_ids](#alternate_gene_ids)             | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/alternate_gene_ids")                    |
| [alternate\_gene\_symbols](#alternate_gene_symbols)     | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/alternate_gene_symbols")            |
| [gene\_external\_references](#gene_external_references) | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_external_references") |

## gene\_symbol

The official gene symbol. It is typically derived from the gene name. This optional field exists to provide the common identifier of the gene. There are several resources to search for a gene of interest, although we recommend [NCBI's service](https://www.ncbi.nlm.nih.gov/gene). For example: (1) in the case of human genes, the symbol follows [HGNC](https://www.genenames.org/)'s nomenclature; (2) while in the case of mice genes they are provided by [MGI](http://www.informatics.jax.org/).

`gene_symbol`

*   is optional

*   Type: `string` ([Gene Symbol](ega-12-definitions-gene-descriptor-properties-gene-symbol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-symbol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_symbol")

### gene\_symbol Type

`string` ([Gene Symbol](ega-12-definitions-gene-descriptor-properties-gene-symbol.md))

### gene\_symbol Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### gene\_symbol Examples

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

## gene\_id\_curie

A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol (e.g. HGNC:11535 for gene TAF1). The identifier has to follow CURIE format. Additionally, there are 2 types of allowed databases to reference: NCBIGene and HGNC. Other archives' accessions (e.g. ensembl:ENSDARG00000035330) can be cross referenced with NCBIGene to obtain its gene ID (e.g. ncbigene:555452).

`gene_id_curie`

*   is required

*   Type: `string` ([Gene CURIE ID](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_id_curie")

### gene\_id\_curie Type

`string` ([Gene CURIE ID](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md))

one (and only one) of

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

### gene\_id\_curie Examples

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

## gene\_description

Free-text description of the gene, only to be used to provide additional context that would otherwise be impossible to add encoded in the schema. In other words, kindly refrain from providing alternative gene symbols in the description if they are not added likewise in the 'alternate\_gene\_symbols' property.

`gene_description`

*   is optional

*   Type: `string` ([Description of the gene](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_description")

### gene\_description Type

`string` ([Description of the gene](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md))

### gene\_description Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### gene\_description Examples

```json
"In the used cells, locus of gene ... was modified at positions +23, where thymine was transitioned to cytosine (T-C)..."
```

## alternate\_gene\_ids

Array of alternate identifiers for this gene. For example, Ensemble identifiers for genes and its transcripts.

`alternate_gene_ids`

*   is optional

*   Type: `string[]` ([Alternate gene ID](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids-alternate-gene-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/alternate_gene_ids")

### alternate\_gene\_ids Type

`string[]` ([Alternate gene ID](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids-alternate-gene-id.md))

### alternate\_gene\_ids Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## alternate\_gene\_symbols

Array of alternate gene sumbols. This field can be used to provide any other alternate gene symbol to refer to the gene, including previously approved gene symbols. There are several resources to search for a gene of interest, although we recommend [NCBI's service](https://www.ncbi.nlm.nih.gov/gene). For example: (1) in the case of human genes, the symbol follows [HGNC](https://www.genenames.org/)'s nomenclature; (2) while in the case of mice genes they are provided by [MGI](http://www.informatics.jax.org/).

`alternate_gene_symbols`

*   is optional

*   Type: `string[]` ([Alternate gene symbol](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols-alternate-gene-symbol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/alternate_gene_symbols")

### alternate\_gene\_symbols Type

`string[]` ([Alternate gene symbol](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols-alternate-gene-symbol.md))

### alternate\_gene\_symbols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## gene\_external\_references

Array of related identifiers. This field can be used to provide identifiers to alternative resources representing related, but not equivalent concepts, for example gene paralog, analog or ortholog IDs.

`gene_external_references`

*   is optional

*   Type: `string[]` ([Related gene ID](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids-related-gene-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_external_references")

### gene\_external\_references Type

`string[]` ([Related gene ID](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids-related-gene-id.md))

### gene\_external\_references Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
