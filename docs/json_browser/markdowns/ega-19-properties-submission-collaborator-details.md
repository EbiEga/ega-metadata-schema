# Submission collaborator details Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/additional_collaborators
```

Object containing optional collaborators of the submission project, who shall have different capabilities granted by the owner: 'read' or 'read and write' rights.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## additional\_collaborators Type

`object[]` ([Collaborator](ega-19-properties-submission-collaborator-details-collaborator.md))

## additional\_collaborators Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
