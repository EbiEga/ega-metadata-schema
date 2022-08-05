# Collaborator Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additional_collaborators/items
```

Collaborator item comprising both the collaborator's contact details and rights.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## items Type

`object` ([Collaborator](ega-19-properties-submission-collaborator-details-collaborator.md))

# items Properties

| Property                                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                   |
| :-------------------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [collaborator\_rights](#collaborator_rights)                    | `string` | Required | cannot be null | [EGA submission metadata schema](ega-19-properties-submission-collaborator-details-collaborator-properties-collaborator-rights.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additional_collaborators/items/properties/collaborator_rights") |
| [collaborator\_contact\_details](#collaborator_contact_details) | Merged   | Required | cannot be null | [EGA submission metadata schema](ega-12-definitions-contact-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additional_collaborators/items/properties/collaborator_contact_details")                                                   |

## collaborator\_rights

Property defining the rights of the specified collaborator. Either read-only or read and write rights.

`collaborator_rights`

*   is required

*   Type: `string` ([Collaborator rights](ega-19-properties-submission-collaborator-details-collaborator-properties-collaborator-rights.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-19-properties-submission-collaborator-details-collaborator-properties-collaborator-rights.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additional_collaborators/items/properties/collaborator_rights")

### collaborator\_rights Type

`string` ([Collaborator rights](ega-19-properties-submission-collaborator-details-collaborator-properties-collaborator-rights.md))

### collaborator\_rights Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation                                                                              |
| :----------------- | :--------------------------------------------------------------------------------------- |
| `"read_only"`      | Collaborator will only be capable of reading the details of the submission.              |
| `"read_and_write"` | Collaborator will be able to not only read, but modify or add changes to the submission. |

## collaborator\_contact\_details

An object to contain the required metadata to identify and reach an individual or institution. Used, for instance, to list who needs to be informed (1) in case of a erroneous submission (2) or in case access to a dataset is requested by a user.

`collaborator_contact_details`

*   is required

*   Type: `object` ([Contact details](ega-12-definitions-contact-details.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-definitions-contact-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additional_collaborators/items/properties/collaborator_contact_details")

### collaborator\_contact\_details Type

`object` ([Contact details](ega-12-definitions-contact-details.md))

any of

*   [Either the individual's name is required.](ega-12-definitions-contact-details-anyof-either-the-individuals-name-is-required.md "check type definition")

*   [Or the institution's name is required.](ega-12-definitions-contact-details-anyof-or-the-institutions-name-is-required.md "check type definition")
