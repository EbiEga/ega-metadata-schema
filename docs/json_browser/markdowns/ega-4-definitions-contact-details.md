# Contact details Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators/items/properties/collaboratorContactDetails
```

An object to contain the required metadata to identify and reach an individual or institution. Used, for instance, to list who needs to be informed (1) in case of a erroneous submission (2) or in case access to a dataset is requested by a user.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## collaboratorContactDetails Type

`object` ([Contact details](ega-4-definitions-contact-details.md))

any of

*   [Either the individual's name is required.](ega-4-definitions-contact-details-anyof-either-the-individuals-name-is-required.md "check type definition")

*   [Or the institution's name is required.](ega-4-definitions-contact-details-anyof-or-the-institutions-name-is-required.md "check type definition")

# collaboratorContactDetails Properties

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                      |
| :---------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [individualFullName](#individualfullname) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-contact-details-properties-full-name-of-an-individual.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/individualFullName") |
| [institutionName](#institutionname)       | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-contact-details-properties-institution-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/institutionName")              |
| [emailAddress](#emailaddress)             | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-contact-details-properties-email-address.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/emailAddress")                    |
| [phoneNumber](#phonenumber)               | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-contact-details-properties-phone-number.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/phoneNumber")                      |

## individualFullName

A full set of all personal names by which an individual is known and that can be recited as a word-group, with the understanding that, taken together, they all relate to that one individual. In case there are several, separate them with semicolons (;).

`individualFullName`

*   is optional

*   Type: `string` ([Full name of an individual](ega-4-definitions-contact-details-properties-full-name-of-an-individual.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-contact-details-properties-full-name-of-an-individual.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/individualFullName")

### individualFullName Type

`string` ([Full name of an individual](ega-4-definitions-contact-details-properties-full-name-of-an-individual.md))

### individualFullName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### individualFullName Examples

```json
"Wayne Jr., Bruce"
```

## institutionName

The full name of an institution the contact belongs to. In case there are several, separate them with semicolons (;).

`institutionName`

*   is optional

*   Type: `string` ([Institution name](ega-4-definitions-contact-details-properties-institution-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-contact-details-properties-institution-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/institutionName")

### institutionName Type

`string` ([Institution name](ega-4-definitions-contact-details-properties-institution-name.md))

### institutionName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### institutionName Examples

```json
"European Genome-phenome Archive (EGA)"
```

## emailAddress

Current email address that would be used in case the contact needs to be reached. Its expected format is of a local-part (e.g. 'myname'), followed by an 'at' sign (i.e. '@') and the domain of the address (e.g. 'gmail.com' or 'ebi.ac.uk').

`emailAddress`

*   is required

*   Type: `string` ([Email address](ega-4-definitions-contact-details-properties-email-address.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-contact-details-properties-email-address.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/emailAddress")

### emailAddress Type

`string` ([Email address](ega-4-definitions-contact-details-properties-email-address.md))

### emailAddress Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Ba-zA-Z0-9_%5C-%5C.%5D%2B\)%40\(%5Ba-zA-Z0-9_%5C-%5C.%5D%2B\)%5C.\(%5Ba-zA-Z%5D%7B2%2C5%7D\)%24 "try regular expression with regexr.com")

### emailAddress Examples

```json
"myname@ebi.ac.uk"
```

## phoneNumber

Current phone number that would be used in case the contact needs to be reached. Theoretically would only be used in case the email address was not provided, does not exist or is unresponsive.

`phoneNumber`

*   is optional

*   Type: `string` ([Phone number](ega-4-definitions-contact-details-properties-phone-number.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-contact-details-properties-phone-number.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/phoneNumber")

### phoneNumber Type

`string` ([Phone number](ega-4-definitions-contact-details-properties-phone-number.md))

### phoneNumber Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^\+?\(?[0-9]{1,4}\)?[-\s\./0-9]+$
```

[try pattern](https://regexr.com/?expression=%5E%5C%2B%3F%5C\(%3F%5B0-9%5D%7B1%2C4%7D%5C\)%3F%5B-%5Cs%5C.%2F0-9%5D%2B%24 "try regular expression with regexr.com")

### phoneNumber Examples

```json
"+44 7427512529"
```
