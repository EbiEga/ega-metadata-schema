# CURIE of the sampling site Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sample_collection_site_curie
```

Ontology term in CURIE format (e.g. 'UBERON:0000167') of the sampling site. The ontology to use is UBERON's anatomical entity \[UBERON:0001062]. Search for your ontologized term at <http://purl.obolibrary.org/obo/UBERON_0001062>. For example, in the case of a nasal swab, it would be 'UBERON:0001707'; in a liver biopsy it would be 'UBERON:0002107'.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sample\_collection\_site\_curie Type

`string` ([CURIE of the sampling site](ega-17-properties-sample-collection-descriptor-properties-curie-of-the-sampling-site.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

## sample\_collection\_site\_curie Examples

```json
"UBERON:0000167"
```

```json
"UBERON:0001707"
```

```json
"UBERON:0000328"
```

```json
"UBERON:0002107"
```
