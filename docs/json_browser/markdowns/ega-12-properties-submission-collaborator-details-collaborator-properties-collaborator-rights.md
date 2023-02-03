# Collaborator rights Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators/items/properties/collaboratorRights
```

Property defining the rights of the specified collaborator. Either read-only or read and write rights.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## collaboratorRights Type

`string` ([Collaborator rights](ega-12-properties-submission-collaborator-details-collaborator-properties-collaborator-rights.md))

## collaboratorRights Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation                                                                              |
| :----------------- | :--------------------------------------------------------------------------------------- |
| `"read_only"`      | Collaborator will only be capable of reading the details of the submission.              |
| `"read_and_write"` | Collaborator will be able to not only read, but modify or add changes to the submission. |
