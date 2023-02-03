# Subject ID Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/subjectId
```

A unique identifier (e.g. 'Donor-10031') for the subject the sample derives from, providing context for the sample to be better understood through its provenance. It **shall not** contain personal sensitive data, since it will be publicly displayed for queries and searches.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## subjectId Type

`string` ([Subject ID](ega-4-definitions-subject-id.md))

## subjectId Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## subjectId Examples

```json
"Donor-10031"
```

```json
"ID001"
```

```json
"9001"
```

```json
"AX_Dli"
```
