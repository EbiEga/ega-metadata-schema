# Assay type Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/assayInstrument
```

The general categories, either sequencing or array, in which assays are categorized based on the used instruments. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## assayInstrument Type

`string` ([Assay type](ega-11-properties-assay-type-specifications-properties-assay-type.md))

## assayInstrument Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation                                                                                                    |
| :------------ | :------------------------------------------------------------------------------------------------------------- |
| `"array"`     | An assay in which an \[array instrument \[EFO:0002698]]\(http\://www\.ebi.ac.uk/efo/EFO\_0002698) was used.    |
| `"sequencer"` | An assay in which a \[sequencer instrument \[EFO:0003739]]\(http\://www\.ebi.ac.uk/efo/EFO\_0003739) was used. |
