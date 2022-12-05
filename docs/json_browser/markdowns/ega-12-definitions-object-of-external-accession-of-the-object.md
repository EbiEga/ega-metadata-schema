# Object of external accession of the object Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession
```

External accession node containing the object accession (i.e. unique identifier -  each following their respective formats) assigned by other archives (e.g. biosample, ena, ensembl...) and an optional label to add context to the reference.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## objectExternalAccession Type

`object` ([Object of external accession of the object](ega-12-definitions-object-of-external-accession-of-the-object.md))

any of

*   [Either the CURIE is needed](ega-12-definitions-object-of-external-accession-of-the-object-anyof-either-the-curie-is-needed.md "check type definition")

*   [Or the reference is needed](ega-12-definitions-object-of-external-accession-of-the-object-anyof-or-the-reference-is-needed.md "check type definition")

# objectExternalAccession Properties

| Property                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                    |
| :------------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [externalAccessionCurie](#externalaccessioncurie) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/externalAccessionCurie") |
| [accessionReference](#accessionreference)         | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/accessionReference") |
| [accessionLabel](#accessionlabel)                 | Multiple | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/accessionLabel")         |

## externalAccessionCurie

Unique identifier of an external, to EGA, object. It shall follow CURIE format (`prefix`:`accession`): prefix assigned to the archive (e.g. biosample - search for yours at identifiers.org) and the unique accession of the object (e.g. SAMEA7616999).

`externalAccessionCurie`

*   is optional

*   Type: `string` ([CURIE of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/externalAccessionCurie")

### externalAccessionCurie Type

`string` ([CURIE of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession-allof-compact-uri-curie-pattern.md "check type definition")

### externalAccessionCurie Examples

```json
"biosample:SAMEA7616999"
```

```json
"arrayexpress:E-MEXP-1712"
```

```json
"biostudies:S-EPMC3314381"
```

```json
"pubmed:30962759"
```

## accessionReference

Full or partial URL/URI of the external accession, for systems to resolve it.

`accessionReference`

*   is optional

*   Type: `string` ([Reference of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/accessionReference")

### accessionReference Type

`string` ([Reference of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession.md))

all of

*   [URL/URI pattern](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession-allof-urluri-pattern.md "check type definition")

### accessionReference Examples

```json
"https://www.ebi.ac.uk/biosamples/samples/SAMN11716999"
```

```json
"https://pubmed.ncbi.nlm.nih.gov/19491253"
```

```json
"https://identifiers.org/arrayexpress:E-MEXP-1712"
```

```json
"https://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-1712/"
```

## accessionLabel

Label (e.g. 'taken from biosample temporarily') of the external accession, used to add extra information to the identifier.

`accessionLabel`

*   is optional

*   Type: any of the folllowing: `string` or `number` ([Label of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/accessionLabel")

### accessionLabel Type

any of the folllowing: `string` or `number` ([Label of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

### accessionLabel Examples

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
