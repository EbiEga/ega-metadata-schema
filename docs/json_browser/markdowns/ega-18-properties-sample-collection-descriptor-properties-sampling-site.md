# Sampling site Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sampling_site
```

A site from which a sample, i.e. a statistically representative of the whole, is extracted from the whole.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sampling\_site Type

`object` ([Sampling site](ega-18-properties-sample-collection-descriptor-properties-sampling-site.md))

# sampling\_site Properties

| Property                                                       | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sampled\_organism\_part](#sampled_organism_part)              | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-18-properties-sample-collection-descriptor-properties-sampling-site-properties-sampled-anatomical-entity-organ-tissue.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sampling_site/properties/sampled_organism_part") |
| [sampled\_organism\_part\_curie](#sampled_organism_part_curie) | Merged   | Optional | cannot be null | [EGA sample metadata schema](ega-12-definitions-compact-uri-curie-of-the-uberons-organism-part.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sampling_site/properties/sampled_organism_part_curie")                                                   |

## sampled\_organism\_part

A site or entity from which a sample, i.e. a statistically representative of the whole, is extracted from the whole. The ontology to use is UBERON's anatomical entity \[UBERON:0001062]. Search for your sample collection site at <http://purl.obolibrary.org/obo/UBERON_0001062>. For example, in the case of a nasal swab, it would be 'nasal cavity'; in a liver biopsy it would be 'liver'.

`sampled_organism_part`

*   is optional

*   Type: `string` ([Sampled anatomical entity (organ, tissue...)](ega-18-properties-sample-collection-descriptor-properties-sampling-site-properties-sampled-anatomical-entity-organ-tissue.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-sample-collection-descriptor-properties-sampling-site-properties-sampled-anatomical-entity-organ-tissue.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sampling_site/properties/sampled_organism_part")

### sampled\_organism\_part Type

`string` ([Sampled anatomical entity (organ, tissue...)](ega-18-properties-sample-collection-descriptor-properties-sampling-site-properties-sampled-anatomical-entity-organ-tissue.md))

### sampled\_organism\_part Examples

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

## sampled\_organism\_part\_curie

The part of organism's anatomy or substance arising from an organism from which the biomaterial was derived, excludes cells. E.g. tissue, organ, system, sperm, blood or body location (arm). Search for yours at: <http://www.ebi.ac.uk/efo/EFO_0000635>. This property can be used to describe a sampling site or the morphological site of a disease, for example.

`sampled_organism_part_curie`

*   is optional

*   Type: `string` ([Compact URI (CURIE) of the UBERON's organism part](ega-12-definitions-compact-uri-curie-of-the-uberons-organism-part.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-12-definitions-compact-uri-curie-of-the-uberons-organism-part.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sampling_site/properties/sampled_organism_part_curie")

### sampled\_organism\_part\_curie Type

`string` ([Compact URI (CURIE) of the UBERON's organism part](ega-12-definitions-compact-uri-curie-of-the-uberons-organism-part.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

### sampled\_organism\_part\_curie Examples

```json
"UBERON:0000956"
```

```json
"UBERON:0006530"
```
