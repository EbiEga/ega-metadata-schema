# NCBI Taxon of the organism Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/organismTaxon
```

Taxonomic classification of the organism (e.g. 'NCBITaxon:9606' and 'homo sapiens' for humans) curated by the NCBI Taxonomy (search for organisms here: <https://www.ncbi.nlm.nih.gov/taxonomy>; or use the OLS: <https://www.ebi.ac.uk/ols/ontologies/ncbitaxon>). You can find further details at '<https://www.uniprot.org/help/taxonomic_identifier>'. This is appropriate for individual organisms and some environmental samples.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## organismTaxon Type

`object` ([NCBI Taxon of the organism](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# organismTaxon Properties

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                     |
| :---------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/organismTaxon/properties/termId") |

## termId



`termId`

*   is optional

*   Type: unknown ([Ontology constraints for this specific termId](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/organismTaxon/properties/termId")

### termId Type

unknown ([Ontology constraints for this specific termId](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism-properties-ontology-constraints-for-this-specific-termid.md))

### termId Examples

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
