# NCBI Assembly CURIE pattern Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/curieNcbiAssemblyPattern
```

The assembly accession starts with a three letter prefix, GCA for GenBank assemblies and GCF for RefSeq assemblies. This is followed by an underscore and 9 digits (e.g. '\_000001405'). A version (e.g. '.26') is then added to the accession. See further details here: <https://registry.identifiers.org/registry/assembly>

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## curieNcbiAssemblyPattern Type

`string` ([NCBI Assembly CURIE pattern](ega-4-defs-ncbi-assembly-curie-pattern.md))

all of

* [Compact URI (CURIE) pattern](ega-4-defs-compact-uri-curie-pattern.md "check type definition")

## curieNcbiAssemblyPattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^assembly:(GCF|GCA)_\d+(\.\d+)?$
```

[try pattern](https://regexr.com/?expression=%5Eassembly%3A\(GCF%7CGCA\)_%5Cd%2B\(%5C.%5Cd%2B\)%3F%24 "try regular expression with regexr.com")

## curieNcbiAssemblyPattern Examples

```json
"assembly:GCF_000001405.26"
```

```json
"assembly:GCA_000001405.1"
```

```json
"assembly:GCF_000005845.2"
```
