# Name of the archive Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_archive
```

Name of the archive (e.g. biosample) from which the external accession is taken.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## accession_archive Type

`string` ([Name of the archive](ega-4-definitions-object-of-external-accession-of-the-object-properties-name-of-the-archive.md))

## accession_archive Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"ensembl"`         |             |
| `"ena"`             |             |
| `"pubmed"`          |             |
| `"protein"`         |             |
| `"nuccore"`         |             |
| `"ipg"`             |             |
| `"nucleotide"`      |             |
| `"structure"`       |             |
| `"genome"`          |             |
| `"annotinfo"`       |             |
| `"assembly"`        |             |
| `"bioproject"`      |             |
| `"biosample"`       |             |
| `"blastdbinfo"`     |             |
| `"books"`           |             |
| `"cdd"`             |             |
| `"clinvar"`         |             |
| `"gap"`             |             |
| `"gapplus"`         |             |
| `"grasp"`           |             |
| `"dbvar"`           |             |
| `"gene"`            |             |
| `"gds"`             |             |
| `"geoprofiles"`     |             |
| `"homologene"`      |             |
| `"medgen"`          |             |
| `"mesh"`            |             |
| `"ncbisearch"`      |             |
| `"nlmcatalog"`      |             |
| `"omim"`            |             |
| `"orgtrack"`        |             |
| `"pmc"`             |             |
| `"popset"`          |             |
| `"proteinclusters"` |             |
| `"pcassay"`         |             |
| `"protfam"`         |             |
| `"biosystems"`      |             |
| `"pccompound"`      |             |
| `"pcsubstance"`     |             |
| `"seqannot"`        |             |
| `"snp"`             |             |
| `"sra"`             |             |
| `"taxonomy"`        |             |
| `"biocollections"`  |             |
| `"gtr"`             |             |

## accession_archive Examples

```json
"biosample"
```
