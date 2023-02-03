# Subtype of the protocol Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolSubtype
```

Ontology term of the protocol subtype. Search for yours at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index). This allows for a specific designation of the protocol within the high level 'protocolType' field. For instance, for Treatment's subtype 'clinical treatment' ('termLabel') we would use 'EFO:0003814' ('termId'). In case the protocol does not have a subtype, use 'NCIT:C48660' for 'Not applicable'.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## protocolSubtype Type

`object` ([Subtype of the protocol](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# protocolSubtype Properties

| Property          | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                             |
| :---------------- | :----- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Merged | Optional | cannot be null | [EGA protocol metadata schema](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolSubtype/properties/termId") |

## termId



`termId`

*   is optional

*   Type: merged type ([Ontology constraints for this specific termId](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA protocol metadata schema](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolSubtype/properties/termId")

### termId Type

merged type ([Ontology constraints for this specific termId](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol-properties-ontology-constraints-for-this-specific-termid.md))

any of

*   [Untitled undefined type in EGA protocol metadata schema](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol-properties-ontology-constraints-for-this-specific-termid-anyof-0.md "check type definition")

*   [Untitled undefined type in EGA protocol metadata schema](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol-properties-ontology-constraints-for-this-specific-termid-anyof-1.md "check type definition")

*   [Untitled undefined type in EGA protocol metadata schema](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol-properties-ontology-constraints-for-this-specific-termid-anyof-2.md "check type definition")

*   [Untitled undefined type in EGA protocol metadata schema](ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol-properties-ontology-constraints-for-this-specific-termid-anyof-3.md "check type definition")

### termId Examples

```json
"EFO:0005518"
```

```json
"EFO:0002944"
```

```json
"EFO:0003813"
```

```json
"EFO:0003815"
```

```json
"EFO:0003814"
```

```json
"EFO:0004184"
```

```json
"EFO:0003789"
```

```json
"EFO:0009088"
```

```json
"EFO:0009089"
```

```json
"EFO:0003969"
```

```json
"EFO:0005520"
```

```json
"EFO:0000355"
```

```json
"EFO:0005519"
```

```json
"EFO:0003788"
```

```json
"EFO:0000395"
```

```json
"EFO:0010892"
```

```json
"EFO:0010214"
```

```json
"EFO:0000494"
```

```json
"operation:3223"
```
