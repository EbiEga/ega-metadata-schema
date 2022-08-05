# Subject ID Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/minimal_public_attributes/properties/subject_id
```

A unique identifier (e.g. 'Donor-10031') for the subject the sample derives from, providing context for the sample to be better understood through its provenance. It **shall not** contain personal sensitive data, since it will be publicly displayed for queries and searches.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## subject\_id Type

`string` ([Subject ID](ega-12-definitions-subject-id.md))

## subject\_id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## subject\_id Examples

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
