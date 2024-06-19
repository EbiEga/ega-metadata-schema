# Email address Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/contactDetails/properties/emailAddress
```

Current email address that would be used in case the contact needs to be reached. Its expected format is of a local-part (e.g. 'myname'), followed by an 'at' sign (i.e. '@') and the domain of the address (e.g. 'gmail.com' or 'ebi.ac.uk').

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## emailAddress Type

`string` ([Email address](ega-4-defs-contact-details-properties-email-address.md))

## emailAddress Constraints

**(international) email**: the string must be an (international) email address, according to [RFC 6531](https://tools.ietf.org/html/rfc6531 "check the specification")

## emailAddress Examples

```json
"myname@ebi.ac.uk"
```

```json
"üser@example.com"
```
