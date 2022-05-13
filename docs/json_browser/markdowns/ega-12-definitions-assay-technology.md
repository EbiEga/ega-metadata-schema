# Assay technology Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_technology
```

Metadata of the assay instrument (e.g. sequencer Illumina NextSeq 500) used to obtain the raw data (e.g. sequence files) of an assay.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## assay\_technology Type

`object` ([Assay technology](ega-12-definitions-assay-technology.md))

one (and only one) of

*   [Asserting array technology controlled vocabulary (CV)](ega-12-definitions-assay-technology-oneof-asserting-array-technology-controlled-vocabulary-cv.md "check type definition")

*   [Asserting sequencer technology controlled vocabulary (CV)](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv.md "check type definition")

# assay\_technology Properties

| Property                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                              |
| :-------------------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assay\_instrument](#assay_instrument)                    | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assays-instrument-category.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument")      |
| [assay\_instrument\_platform](#assay_instrument_platform) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assay-instrument-label.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument_platform") |

## assay\_instrument

The general categories (e.g. sequencers) in which assay instruments are categorized. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`assay_instrument`

*   is required

*   Type: `string` ([Assay's instrument category](ega-12-definitions-assay-technology-properties-assays-instrument-category.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assays-instrument-category.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument")

### assay\_instrument Type

`string` ([Assay's instrument category](ega-12-definitions-assay-technology-properties-assays-instrument-category.md))

### assay\_instrument Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation                                                                                                                                                         |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"array"`     | \[EFO:0002698]\[Array instrument]\(http\://www\.ebi.ac.uk/efo/EFO\_0002698), an instrument which consists of nucleic acid or protein molecules bound to a substrate |
| `"sequencer"` | \[EFO:0003739]\[Sequencer instrument]\(http\://www\.ebi.ac.uk/efo/EFO\_0003739), an instrument that determines the order of nucleic acids in their sequences.       |

## assay\_instrument\_platform

Label (e.g. 'Illumina HiSeq 2500'), chosen from a list of controlled vocabulary (CV), of the technology used at the experiment. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`assay_instrument_platform`

*   is required

*   Type: `string` ([Assay instrument label](ega-12-definitions-assay-technology-properties-assay-instrument-label.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assay-instrument-label.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument_platform")

### assay\_instrument\_platform Type

`string` ([Assay instrument label](ega-12-definitions-assay-technology-properties-assay-instrument-label.md))

### assay\_instrument\_platform Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### assay\_instrument\_platform Examples

```json
"Illumina HiSeq 2500"
```

```json
"[HuGene-1_1-st] Affymetrix Human Gene 1.1 ST Array [probe set (exon) version]"
```

```json
"DNBSEQ-G400 FAST"
```
