# NCBI Taxon identifier Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id_curie
```

Taxonomy Identifier (e.g. 'NCBITaxon:9606' for humans) curated by the NCBI Taxonomy (search for organisms here: <https://www.ncbi.nlm.nih.gov/taxonomy>; or use the OLS: <https://www.ebi.ac.uk/ols/ontologies/ncbitaxon>). You can find further details at '<https://www.uniprot.org/help/taxonomic_identifier>'. This is appropriate for individual organisms and some environmental samples.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## taxon\_id\_curie Type

`string` ([NCBI Taxon identifier](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

## taxon\_id\_curie Examples

```json
"NCBITaxon:9606"
```

```json
"NCBITaxon:155900"
```

```json
"NCBITaxon:408170"
```

```json
"NCBITaxon:447426"
```
