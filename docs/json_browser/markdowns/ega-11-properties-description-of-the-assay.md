# Description of the assay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/object_description
```

An in-depth description (e.g. used technology, sample groups, purpose...) of the assay.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## object\_description Type

`string` ([Description of the assay](ega-11-properties-description-of-the-assay.md))

## object\_description Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## object\_description Examples

```json
"Sequencing assay number 3409 of 4000. Sequenced through Illumina MiSeq to find SNPs of colorectal cancer samples..."
```
