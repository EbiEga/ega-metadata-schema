# Assembly common name Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/assemblyName
```

A free-text common name (e.g. 'GRCh38') that is used to denote the sequence assembly.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## assemblyName Type

`string` ([Assembly common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md))

## assemblyName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## assemblyName Examples

```json
"GRCh38.p14"
```

```json
"GRCh38"
```

```json
"GRCh37.p13"
```

```json
"GRCh37"
```
