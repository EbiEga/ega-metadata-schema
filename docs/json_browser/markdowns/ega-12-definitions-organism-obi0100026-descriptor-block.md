# Organism \[OBI:0100026] descriptor block Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/organism_descriptor
```

This property describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or made up, like humans, of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance by default.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## organism\_descriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

# organism\_descriptor Properties

| Property                             | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                  |
| :----------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [taxon\_id\_curie](#taxon_id_curie)  | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id_curie")                           |
| [scientific\_name](#scientific_name) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/scientific_name") |
| [common\_name](#common_name)         | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/common_name")         |

## taxon\_id\_curie

Taxonomy Identifier (e.g. 'NCBITaxon:9606' for humans) curated by the NCBI Taxonomy (search for organisms here: <https://www.ncbi.nlm.nih.gov/taxonomy>; or use the OLS: <https://www.ebi.ac.uk/ols/ontologies/ncbitaxon>). You can find further details at '<https://www.uniprot.org/help/taxonomic_identifier>'. This is appropriate for individual organisms and some environmental samples.

`taxon_id_curie`

*   is required

*   Type: `string` ([NCBI Taxon identifier](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id_curie")

### taxon\_id\_curie Type

`string` ([NCBI Taxon identifier](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

### taxon\_id\_curie Examples

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

## scientific\_name

The name applied to a plant, animal, or other organism, according to the Codes of Nomenclature, consisting of a Genus and species (e.g. 'homo sapiens').

`scientific_name`

*   is optional

*   Type: `string` ([Biologic entity classification scientific name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/scientific_name")

### scientific\_name Type

`string` ([Biologic entity classification scientific name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md))

### scientific\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### scientific\_name Examples

```json
"homo sapiens"
```

```json
"uncultured organism"
```

```json
"human gut metagenome"
```

```json
"human oral metagenome"
```

## common\_name

Common name (e.g. 'human') used to designate a plant, animal or other organism, as opposed to the scientific name.

`common_name`

*   is optional

*   Type: `string` ([Biologic entity classification common name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/common_name")

### common\_name Type

`string` ([Biologic entity classification common name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

### common\_name Examples

```json
"human"
```
