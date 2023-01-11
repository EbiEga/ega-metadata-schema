# Assay instrument platform Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayTechnologyDescriptor/properties/assayInstrumentPlatform
```

Platform of the used instrument (e.g. 'Illumina HiSeq 2500'). Given the heterogenity in sequencing and array platforms (power of thousands), this property is not restricted by a CV list (i.e. it is free text).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## assayInstrumentPlatform Type

`string` ([Assay instrument platform](ega-12-definitions-assay-technology-properties-assay-instrument-platform.md))

## assayInstrumentPlatform Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## assayInstrumentPlatform Examples

```json
"Illumina HiSeq 2500"
```

```json
"[HuGene-1_1-st] Affymetrix Human Gene 1.1 ST Array [probe set (exon) version]"
```

```json
"DNBSEQ-G400 FAST"
```
