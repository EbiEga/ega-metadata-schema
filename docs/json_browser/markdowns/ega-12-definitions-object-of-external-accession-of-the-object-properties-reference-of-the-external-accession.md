# Reference of the external accession Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/accessionReference
```

Full or partial URL/URI of the external accession, for systems to resolve it.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## accessionReference Type

`string` ([Reference of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession.md))

all of

*   [URL/URI pattern](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession-allof-urluri-pattern.md "check type definition")

## accessionReference Examples

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
