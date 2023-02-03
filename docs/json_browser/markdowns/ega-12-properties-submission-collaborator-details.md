# Submission collaborator details Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators
```

Object containing optional collaborators of the submission project, who shall have different capabilities granted by the owner: 'read' or 'read and write' rights.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## additionalCollaborators Type

`object[]` ([Collaborator](ega-12-properties-submission-collaborator-details-collaborator.md))

## additionalCollaborators Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
