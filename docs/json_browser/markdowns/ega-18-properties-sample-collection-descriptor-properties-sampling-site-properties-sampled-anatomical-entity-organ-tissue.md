# Sampled anatomical entity (organ, tissue...) Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/samplingSite/properties/sampledOrganismPart
```

A site or entity from which a sample, i.e. a statistically representative of the whole, is extracted from the whole. The ontology to use is UBERON's anatomical entity \[UBERON:0001062]. Search for your sample collection site at <http://purl.obolibrary.org/obo/UBERON_0001062>. For example, in the case of a nasal swab, it would be 'nasal cavity'; in a liver biopsy it would be 'liver'.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sampledOrganismPart Type

`string` ([Sampled anatomical entity (organ, tissue...)](ega-18-properties-sample-collection-descriptor-properties-sampling-site-properties-sampled-anatomical-entity-organ-tissue.md))

## sampledOrganismPart Examples

```json
"nasal cavity"
```

```json
"liver"
```

```json
"gut wall"
```

```json
"oral cavity"
```
