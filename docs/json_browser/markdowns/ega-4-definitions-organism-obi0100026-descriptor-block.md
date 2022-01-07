# Organism \[OBI:0100026] descriptor block Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/organism_descriptor
```

This node describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or made up, like humans, of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance by default.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json*](../out/EGA.sample.json "open original schema") |

## organism_descriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-4-definitions-organism-obi0100026-descriptor-block.md))

any of

*   [Either the taxon ID is provided](ega-4-definitions-organism-obi0100026-descriptor-block-anyof-either-the-taxon-id-is-provided.md "check type definition")

*   [Or the scientific name is provided](ega-4-definitions-organism-obi0100026-descriptor-block-anyof-or-the-scientific-name-is-provided.md "check type definition")

# organism_descriptor Properties

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                  |
| :---------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [taxon_id](#taxon_id)               | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier-apollo_sv00000203.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id")                               |
| [scientific_name](#scientific_name) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name-ncitc43459.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/scientific_name") |
| [common_name](#common_name)         | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name-ncitc164690.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/common_name")        |

## taxon_id

Taxonomy Identifier (e.g. '9606' for humans) curated by the NCBI Taxonomy (search for your sample's here: <https://www.ncbi.nlm.nih.gov/taxonomy>). You can find further details at '<https://www.uniprot.org/help/taxonomic_identifier>'. This is appropriate for individual organisms and some environmental samples.

`taxon_id`

*   is optional

*   Type: `string` ([Taxon identifier \[APOLLO_SV:00000203\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier-apollo_sv00000203.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier-apollo_sv00000203.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id")

### taxon_id Type

`string` ([Taxon identifier \[APOLLO_SV:00000203\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier-apollo_sv00000203.md))

### taxon_id Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[0-9]{1,7}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B1%2C7%7D%24 "try regular expression with regexr.com")

### taxon_id Examples

```json
"9606"
```

## scientific_name

The name applied to a plant, animal, or other organism, according to the Codes of Nomenclature, consisting of a Genus and species (e.g. 'homo sapiens').

`scientific_name`

*   is optional

*   Type: `string` ([Biologic entity classification scientific name \[NCIT:C43459\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name-ncitc43459.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name-ncitc43459.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/scientific_name")

### scientific_name Type

`string` ([Biologic entity classification scientific name \[NCIT:C43459\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name-ncitc43459.md))

### scientific_name Examples

```json
"homo sapiens"
```

## common_name

Common name (e.g. 'human') used to designate a plant, animal or other organism, as opposed to the scientific name.

`common_name`

*   is optional

*   Type: `string` ([Biologic entity classification common name \[NCIT:C164690\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name-ncitc164690.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name-ncitc164690.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/common_name")

### common_name Type

`string` ([Biologic entity classification common name \[NCIT:C164690\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name-ncitc164690.md))

### common_name Examples

```json
"human"
```
