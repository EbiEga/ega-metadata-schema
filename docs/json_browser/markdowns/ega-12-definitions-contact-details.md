# Contact details Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details
```

An object to contain the required metadata to identify and reach an individual or institution. Used, for instance, to list who needs to be informed (1) in case of a erroneous submission (2) or in case access to a dataset is requested by a user.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## contact\_details Type

`object` ([Contact details](ega-12-definitions-contact-details.md))

any of

*   [Either the individual's name is required.](ega-12-definitions-contact-details-anyof-either-the-individuals-name-is-required.md "check type definition")

*   [Or the institution's name is required.](ega-12-definitions-contact-details-anyof-or-the-institutions-name-is-required.md "check type definition")

# contact\_details Properties

| Property                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                |
| :---------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [individual\_full\_name](#individual_full_name) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/individual_full_name") |
| [institution\_name](#institution_name)          | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-institution-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/institution_name")               |
| [email\_address](#email_address)                | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-email-address.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/email_address")                     |
| [phone\_number](#phone_number)                  | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-phone-number.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/phone_number")                       |

## individual\_full\_name

A full set of all personal names by which an individual is known and that can be recited as a word-group, with the understanding that, taken together, they all relate to that one individual. In case there are several, separate them with semicolons (;).

`individual_full_name`

*   is optional

*   Type: `string` ([Full name of an individual](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/individual_full_name")

### individual\_full\_name Type

`string` ([Full name of an individual](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md))

### individual\_full\_name Examples

```json
"Wayne Jr., Bruce"
```

## institution\_name

The full name of an institution the contact belongs to. In case there are several, separate them with semicolons (;).

`institution_name`

*   is optional

*   Type: `string` ([Institution name](ega-12-definitions-contact-details-properties-institution-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-institution-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/institution_name")

### institution\_name Type

`string` ([Institution name](ega-12-definitions-contact-details-properties-institution-name.md))

### institution\_name Examples

```json
"European Genome-phenome Archive (EGA)"
```

## email\_address

Current email address that would be used in case the contact needs to be reached. Its expected format is of a local-part (e.g. 'myname'), followed by an 'at' sign (i.e. '@') and the domain of the address (e.g. 'gmail.com' or 'ebi.ac.uk').

`email_address`

*   is required

*   Type: `string` ([Email address](ega-12-definitions-contact-details-properties-email-address.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-email-address.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/email_address")

### email\_address Type

`string` ([Email address](ega-12-definitions-contact-details-properties-email-address.md))

### email\_address Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Ba-zA-Z0-9_%5C-%5C.%5D%2B\)%40\(%5Ba-zA-Z0-9_%5C-%5C.%5D%2B\)%5C.\(%5Ba-zA-Z%5D%7B2%2C5%7D\)%24 "try regular expression with regexr.com")

### email\_address Examples

```json
"myname@ebi.ac.uk"
```

## phone\_number

Current phone number that would be used in case the contact needs to be reached. Theoretically would only be used in case the email address was not provided, does not exist or is unresponsive.

`phone_number`

*   is optional

*   Type: `string` ([Phone number](ega-12-definitions-contact-details-properties-phone-number.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-phone-number.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/phone_number")

### phone\_number Type

`string` ([Phone number](ega-12-definitions-contact-details-properties-phone-number.md))

### phone\_number Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^\+?\(?[0-9]{1,4}\)?[-\s\./0-9]+$
```

[try pattern](https://regexr.com/?expression=%5E%5C%2B%3F%5C\(%3F%5B0-9%5D%7B1%2C4%7D%5C\)%3F%5B-%5Cs%5C.%2F0-9%5D%2B%24 "try regular expression with regexr.com")

### phone\_number Examples

```json
"+44 7427512529"
```
