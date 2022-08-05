# Assay instrument label Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument_platform
```

Label (e.g. 'Illumina HiSeq 2500'), chosen from a list of controlled vocabulary (CV), of the technology used at the experiment. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## assay\_instrument\_platform Type

`string` ([Assay instrument label](ega-12-definitions-assay-technology-properties-assay-instrument-label.md))

## assay\_instrument\_platform Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## assay\_instrument\_platform Examples

```json
"Illumina HiSeq 2500"
```

```json
"[HuGene-1_1-st] Affymetrix Human Gene 1.1 ST Array [probe set (exon) version]"
```

```json
"DNBSEQ-G400 FAST"
```
