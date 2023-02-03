# Object External accession Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession
```

External accession property defining a reference to an external record in another resource. For example, a reference to a sequence deposited in NCBI's Nucleotide database (e.g. '<https://identifiers.org/nucleotide:T35715.1>'); or a sample record in BioSamples (e.g. '<https://identifiers.org/biosample:SAMEA7616999>').

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## objectExternalAccession Type

`object` ([Object External accession](ega-4-definitions-object-external-accession.md))

any of

*   [Either the identifier is needed](ega-4-definitions-object-external-accession-anyof-either-the-identifier-is-needed.md "check type definition")

*   [Or the reference is needed](ega-4-definitions-object-external-accession-anyof-or-the-reference-is-needed.md "check type definition")

# objectExternalAccession Properties

| Property                                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                    |
| :------------------------------------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectExternalAccessionIdentifier](#objectexternalaccessionidentifier)   | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-identifier-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionIdentifier")   |
| [objectExternalAccessionURI](#objectexternalaccessionuri)                 | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionURI")                 |
| [objectExternalAccessionDescription](#objectexternalaccessiondescription) | Multiple | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-description-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionDescription") |

## objectExternalAccessionIdentifier

Unique identifier of an external record. Its 'termId' (e.g. 'biosample:SAMEA7616999', 'pubmed:30962759', 'biostudies:S-EPMC3314381', etc.) shall follow CURIE format of `prefix`:`accession`, where: (1) the prefix (e.g. 'biosample') is unique and assigned to the external resource at identifiers.org; (2) and the unique accession of the object (e.g. SAMEA7616999) should resolve to an existing record within the resource. If in doubt, use identifiers.org to resolve your external accession: '<https://identifiers.org/>' + 'termId', e.g. '<https://identifiers.org/biosample:SAMEA7616999>'

`objectExternalAccessionIdentifier`

*   is optional

*   Type: `object` ([Identifier of the external accession](ega-4-definitions-object-external-accession-properties-identifier-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-identifier-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionIdentifier")

### objectExternalAccessionIdentifier Type

`object` ([Identifier of the external accession](ega-4-definitions-object-external-accession-properties-identifier-of-the-external-accession.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

## objectExternalAccessionURI

Full or partial URL/URI of the external accession, for systems to resolve it. Should only be used in case identifiers.org does not contain a namespace for the required resource or the mapping to the URI from its identifier is faulty.

`objectExternalAccessionURI`

*   is optional

*   Type: `string` ([URI of the external accession](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionURI")

### objectExternalAccessionURI Type

`string` ([URI of the external accession](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession.md))

all of

*   [URL/URI pattern](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession-allof-urluri-pattern.md "check type definition")

### objectExternalAccessionURI Examples

```json
"https://www.ebi.ac.uk/biosamples/samples/SAMN11716999"
```

```json
"https://pubmed.ncbi.nlm.nih.gov/19491253"
```

```json
"https://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-1712/"
```

## objectExternalAccessionDescription

Optional description of the external accession, used to add context to the identifier if applicable.

`objectExternalAccessionDescription`

*   is optional

*   Type: any of the following: `string` or `number` ([Description of the external accession](ega-4-definitions-object-external-accession-properties-description-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-description-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionDescription")

### objectExternalAccessionDescription Type

any of the following: `string` or `number` ([Description of the external accession](ega-4-definitions-object-external-accession-properties-description-of-the-external-accession.md))

### objectExternalAccessionDescription Examples

```json
"taken from biosample temporarily"
```

```json
"Ensembl's part of the accessions"
```

```json
"first"
```

```json
2
```

```json
"Recurrent Erythema Nodosum in a Child with a SHOC2 Gene Mutation"
```
