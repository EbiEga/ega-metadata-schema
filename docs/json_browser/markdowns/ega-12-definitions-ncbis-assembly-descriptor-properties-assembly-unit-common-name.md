# Assembly unit common name Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/assemblyUnitName
```

A free-text common name (e.g. 'chr17') that is used to denote the sequence assembly unit.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## assemblyUnitName Type

`string` ([Assembly unit common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md))

## assemblyUnitName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## assemblyUnitName Examples

```json
"Chromosome 2"
```

```json
"MT"
```

```json
"chr17"
```

```json
"chr20"
```

```json
"18"
```
