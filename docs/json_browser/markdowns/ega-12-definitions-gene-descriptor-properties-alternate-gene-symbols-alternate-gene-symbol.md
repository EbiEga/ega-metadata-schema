# Alternate gene symbol Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/alternate_gene_symbols/items
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`string` ([Alternate gene symbol](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols-alternate-gene-symbol.md))

## items Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## items Examples

```json
"SUP45L1"
```

```json
"eRF1"
```

```json
"RF1"
```

```json
"ERF1"
```
