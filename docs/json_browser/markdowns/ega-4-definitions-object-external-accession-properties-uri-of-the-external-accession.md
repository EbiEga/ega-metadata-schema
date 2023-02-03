# URI of the external accession Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionURI
```

Full or partial URL/URI of the external accession, for systems to resolve it. Should only be used in case identifiers.org does not contain a namespace for the required resource or the mapping to the URI from its identifier is faulty.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## objectExternalAccessionURI Type

`string` ([URI of the external accession](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession.md))

all of

*   [URL/URI pattern](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession-allof-urluri-pattern.md "check type definition")

## objectExternalAccessionURI Examples

```json
"https://www.ebi.ac.uk/biosamples/samples/SAMN11716999"
```

```json
"https://pubmed.ncbi.nlm.nih.gov/19491253"
```

```json
"https://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-1712/"
```
