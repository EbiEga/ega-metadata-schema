# Description of the assay Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/objectDescription
```

An in-depth description (e.g. used technology, sample groups, purpose...) of the assay.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## objectDescription Type

`string` ([Description of the assay](ega-3-properties-description-of-the-assay.md))

## objectDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## objectDescription Examples

```json
"Sequencing assay number 3409 of 4000. Sequenced through Illumina MiSeq to find SNPs of colorectal cancer samples..."
```
