# Taxon identifier \[APOLLO_SV:00000203] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id
```

Taxonomy Identifier (e.g. '9606' for humans) curated by the NCBI Taxonomy (search for your sample's here: <https://www.ncbi.nlm.nih.gov/taxonomy>). You can find further details at '<https://www.uniprot.org/help/taxonomic_identifier>'. This is appropriate for individual organisms and some environmental samples.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## taxon_id Type

`string` ([Taxon identifier \[APOLLO_SV:00000203\]](ega-2-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier-apollo_sv00000203.md))

## taxon_id Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[0-9]{1,7}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B1%2C7%7D%24 "try regular expression with regexr.com")

## taxon_id Examples

```json
"9606"
```
