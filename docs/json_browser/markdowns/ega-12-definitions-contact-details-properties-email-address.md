# Email address Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/email_address
```

Current email address that would be used in case the contact needs to be reached. Its expected format is of a local-part (e.g. 'myname'), followed by an 'at' sign (i.e. '@') and the domain of the address (e.g. 'gmail.com' or 'ebi.ac.uk').

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## email\_address Type

`string` ([Email address](ega-12-definitions-contact-details-properties-email-address.md))

## email\_address Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Ba-zA-Z0-9_%5C-%5C.%5D%2B\)%40\(%5Ba-zA-Z0-9_%5C-%5C.%5D%2B\)%5C.\(%5Ba-zA-Z%5D%7B2%2C5%7D\)%24 "try regular expression with regexr.com")

## email\_address Examples

```json
"myname@ebi.ac.uk"
```
