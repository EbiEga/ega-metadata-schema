# Identifier of the external accession Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionIdentifier
```

Unique identifier of an external record. Its 'termId' (e.g. 'biosample:SAMEA7616999', 'pubmed:30962759', 'biostudies:S-EPMC3314381', etc.) shall follow CURIE format of `prefix`:`accession`, where: (1) the prefix (e.g. 'biosample') is unique and assigned to the external resource at identifiers.org; (2) and the unique accession of the object (e.g. SAMEA7616999) should resolve to an existing record within the resource. If in doubt, use identifiers.org to resolve your external accession: '<https://identifiers.org/>' + 'termId', e.g. '<https://identifiers.org/biosample:SAMEA7616999>'

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## objectExternalAccessionIdentifier Type

`object` ([Identifier of the external accession](ega-4-definitions-object-external-accession-properties-identifier-of-the-external-accession.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")
