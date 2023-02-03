# Organism \[OBI:0100026] descriptor block Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/organismDescriptor
```

This property describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or, like humans, made up of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## organismDescriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-4-definitions-organism-obi0100026-descriptor-block.md))

# organismDescriptor Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                       |
| :------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [organismTaxon](#organismtaxon) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/organismTaxon")              |
| [commonName](#commonname)       | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/commonName") |

## organismTaxon

Taxonomic classification of the organism (e.g. 'NCBITaxon:9606' and 'homo sapiens' for humans) curated by the NCBI Taxonomy (search for organisms here: <https://www.ncbi.nlm.nih.gov/taxonomy>; or use the OLS: <https://www.ebi.ac.uk/ols/ontologies/ncbitaxon>). You can find further details at '<https://www.uniprot.org/help/taxonomic_identifier>'. This is appropriate for individual organisms and some environmental samples.

`organismTaxon`

*   is required

*   Type: `object` ([NCBI Taxon of the organism](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/organismTaxon")

### organismTaxon Type

`object` ([NCBI Taxon of the organism](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

## commonName

Common name (e.g. 'human') used to designate a plant, animal or other organism, as opposed to the scientific name.

`commonName`

*   is optional

*   Type: `string` ([Biologic entity classification common name](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/commonName")

### commonName Type

`string` ([Biologic entity classification common name](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

### commonName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### commonName Examples

```json
"human"
```

```json
"goat"
```

```json
"horse"
```
