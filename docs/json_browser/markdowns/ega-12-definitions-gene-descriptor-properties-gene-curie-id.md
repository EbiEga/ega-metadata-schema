# Gene CURIE ID Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneIdCurie
```

A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol (e.g. HGNC:11535 for gene TAF1). The identifier has to follow CURIE format. Additionally, there are 2 types of allowed databases to reference: NCBIGene and HGNC. Other archives' accessions (e.g. ensembl:ENSDARG00000035330) can be cross referenced with NCBIGene to obtain its gene ID (e.g. ncbigene:555452).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## geneIdCurie Type

`string` ([Gene CURIE ID](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md))

one (and only one) of

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-ncbi-gene-identifier-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-hgnc-identifier-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

## geneIdCurie Examples

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
