# Collaborator Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators/items
```

Collaborator item comprising both the collaborator's contact details and rights.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## items Type

`object` ([Collaborator](ega-12-properties-submission-collaborator-details-collaborator.md))

# items Properties

| Property                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                 |
| :-------------------------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [collaboratorRights](#collaboratorrights)                 | `string` | Required | cannot be null | [EGA submission metadata schema](ega-12-properties-submission-collaborator-details-collaborator-properties-collaborator-rights.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators/items/properties/collaboratorRights") |
| [collaboratorContactDetails](#collaboratorcontactdetails) | Merged   | Required | cannot be null | [EGA submission metadata schema](ega-4-definitions-contact-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators/items/properties/collaboratorContactDetails")                                                     |

## collaboratorRights

Property defining the rights of the specified collaborator. Either read-only or read and write rights.

`collaboratorRights`

*   is required

*   Type: `string` ([Collaborator rights](ega-12-properties-submission-collaborator-details-collaborator-properties-collaborator-rights.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-submission-collaborator-details-collaborator-properties-collaborator-rights.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators/items/properties/collaboratorRights")

### collaboratorRights Type

`string` ([Collaborator rights](ega-12-properties-submission-collaborator-details-collaborator-properties-collaborator-rights.md))

### collaboratorRights Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation                                                                              |
| :----------------- | :--------------------------------------------------------------------------------------- |
| `"read_only"`      | Collaborator will only be capable of reading the details of the submission.              |
| `"read_and_write"` | Collaborator will be able to not only read, but modify or add changes to the submission. |

## collaboratorContactDetails

An object to contain the required metadata to identify and reach an individual or institution. Used, for instance, to list who needs to be informed (1) in case of a erroneous submission (2) or in case access to a dataset is requested by a user.

`collaboratorContactDetails`

*   is required

*   Type: `object` ([Contact details](ega-4-definitions-contact-details.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-4-definitions-contact-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators/items/properties/collaboratorContactDetails")

### collaboratorContactDetails Type

`object` ([Contact details](ega-4-definitions-contact-details.md))

any of

*   [Either the individual's name is required.](ega-4-definitions-contact-details-anyof-either-the-individuals-name-is-required.md "check type definition")

*   [Or the institution's name is required.](ega-4-definitions-contact-details-anyof-or-the-institutions-name-is-required.md "check type definition")
