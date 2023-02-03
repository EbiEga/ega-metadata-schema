# Alternate gene identifier item Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneIdentifiers/items
```

One of the possible alternate gene identifiers for the designated gene. The 'termId' of these elements, contrary to the main identifier, can include references to other resources beyond NCBI and HGNC (e.g. 'OMIM:600296', 'ensembl:ENST00000423759', 'ucsc:uc003ldc.6', etcetera).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([Alternate gene identifier item](ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers-alternate-gene-identifier-item.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")
