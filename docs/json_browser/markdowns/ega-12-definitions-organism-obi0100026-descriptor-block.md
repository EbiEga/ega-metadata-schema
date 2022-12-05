# Organism \[OBI:0100026] descriptor block Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/organismDescriptor
```

This property describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or made up, like humans, of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance by default.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## organismDescriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

# organismDescriptor Properties

| Property                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                |
| :-------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [taxonIdCurie](#taxonidcurie)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/taxonIdCurie")                            |
| [scientificName](#scientificname) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/scientificName") |
| [commonName](#commonname)         | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/commonName")         |

## taxonIdCurie

Taxonomy Identifier (e.g. 'NCBITaxon:9606' for humans) curated by the NCBI Taxonomy (search for organisms here: <https://www.ncbi.nlm.nih.gov/taxonomy>; or use the OLS: <https://www.ebi.ac.uk/ols/ontologies/ncbitaxon>). You can find further details at '<https://www.uniprot.org/help/taxonomic_identifier>'. This is appropriate for individual organisms and some environmental samples.

`taxonIdCurie`

*   is required

*   Type: `string` ([NCBI Taxon identifier](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/taxonIdCurie")

### taxonIdCurie Type

`string` ([NCBI Taxon identifier](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

### taxonIdCurie Examples

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

## scientificName

The name applied to a plant, animal, or other organism, according to the Codes of Nomenclature, consisting of a Genus and species (e.g. 'homo sapiens').

`scientificName`

*   is optional

*   Type: `string` ([Biologic entity classification scientific name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/scientificName")

### scientificName Type

`string` ([Biologic entity classification scientific name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md))

### scientificName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### scientificName Examples

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

## commonName

Common name (e.g. 'human') used to designate a plant, animal or other organism, as opposed to the scientific name.

`commonName`

*   is optional

*   Type: `string` ([Biologic entity classification common name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/commonName")

### commonName Type

`string` ([Biologic entity classification common name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

### commonName Examples

```json
"human"
```
