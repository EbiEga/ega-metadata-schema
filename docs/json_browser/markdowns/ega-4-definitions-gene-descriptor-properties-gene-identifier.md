# Gene identifier Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneIdentifier
```

Property uniquely identifying a gene. It consists of a 'termId' and 'termLabel', which correspond to: (1)  'termId': A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol (e.g. HGNC:11535 for gene TAF1). There are 2 types of allowed databases to reference: NCBIGene and HGNC. Other archives' accessions (e.g. ensembl:ENSDARG00000035330) can be cross referenced with NCBIGene to obtain its gene ID (e.g. ncbigene:555452). (2) 'termLabel': the official gene symbol (e.g. 'TAF1'). It is typically derived from the gene name. There are several resources to search for a gene of interest, although we recommend [NCBI's service](https://www.ncbi.nlm.nih.gov/gene). For example: in the case of human genes, the symbol follows [HGNC](https://www.genenames.org/)'s nomenclature, while in the case of mice genes they are provided by [MGI](http://www.informatics.jax.org/).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## geneIdentifier Type

`object` ([Gene identifier](ega-4-definitions-gene-descriptor-properties-gene-identifier.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# geneIdentifier Properties

| Property          | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                  |
| :---------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [termId](#termid) | Merged | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-gene-identifier-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneIdentifier/properties/termId") |

## termId



`termId`

*   is optional

*   Type: merged type ([Ontology constraints for this specific termId](ega-4-definitions-gene-descriptor-properties-gene-identifier-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-gene-identifier-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneIdentifier/properties/termId")

### termId Type

merged type ([Ontology constraints for this specific termId](ega-4-definitions-gene-descriptor-properties-gene-identifier-properties-ontology-constraints-for-this-specific-termid.md))

any of

*   all of

    *   [Compact URI (CURIE) pattern](ega-4-definitions-ncbi-gene-identifier-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

*   all of

    *   [Compact URI (CURIE) pattern](ega-4-definitions-hgnc-identifier-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

### termId Examples

```json
"NCBIGene:100010"
```

```json
"hgnc:2674"
```
