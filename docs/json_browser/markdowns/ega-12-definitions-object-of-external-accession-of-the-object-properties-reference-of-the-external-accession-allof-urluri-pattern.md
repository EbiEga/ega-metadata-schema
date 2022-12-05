# URL/URI pattern Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/accessionReference/allOf/0
```

This object exists to hold the pattern that a URL or URI should have. For it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 0 Type

`string` ([URL/URI pattern](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession-allof-urluri-pattern.md))

## 0 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^((http|https)://)(www.)?[a-zA-Z0-9@:%._\+~#?&//=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%._\+~#?&//=]*)$
```

[try pattern](https://regexr.com/?expression=%5E\(\(http%7Chttps\)%3A%2F%2F\)\(www.\)%3F%5Ba-zA-Z0-9%40%3A%25._%5C%2B~%23%3F%26%2F%2F%3D%5D%7B2%2C256%7D%5C.%5Ba-z%5D%7B2%2C6%7D%5Cb\(%5B-a-zA-Z0-9%40%3A%25._%5C%2B~%23%3F%26%2F%2F%3D%5D*\)%24 "try regular expression with regexr.com")

## 0 Examples

```json
"https://phenopacket-schema.readthedocs.io/en/latest/externalreference.html"
```

```json
"https://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-1712/"
```

```json
"https://www.geeksforgeeks.org/check-if-an-url-is-valid-or-not-using-regular-expression/"
```
