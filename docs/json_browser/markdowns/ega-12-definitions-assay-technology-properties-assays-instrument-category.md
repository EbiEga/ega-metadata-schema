# Assay's instrument category Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayTechnologyDescriptor/properties/assayInstrument
```

The general categories (e.g. sequencer) in which assay instruments are categorized. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## assayInstrument Type

`string` ([Assay's instrument category](ega-12-definitions-assay-technology-properties-assays-instrument-category.md))

## assayInstrument Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation                                                                                                                                                         |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"array"`     | \[EFO:0002698]\[Array instrument]\(http\://www\.ebi.ac.uk/efo/EFO\_0002698), an instrument which consists of nucleic acid or protein molecules bound to a substrate |
| `"sequencer"` | \[EFO:0003739]\[Sequencer instrument]\(http\://www\.ebi.ac.uk/efo/EFO\_0003739), an instrument that determines the order of nucleic acids in their sequences.       |
