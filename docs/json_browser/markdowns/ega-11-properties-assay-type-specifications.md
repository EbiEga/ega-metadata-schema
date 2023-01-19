# Assay type specifications Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications
```

Node containing different sets of fields that depend on the instrument used for the assay: either array assays (those in which an [array instrument \[EFO:0002698\]](http://www.ebi.ac.uk/efo/EFO_0002698) was used) or sequencing assays (those in which a [sequencing instrument \[EFO:0003739\]](http://www.ebi.ac.uk/efo/EFO_0003739) was used). Depending on the used technology, different types of fields will be required. For example, if an array was used, its arraySampleLabels will be expected. Having this modular assay type-related node allows for easy additions of new technology-specific requirements.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## assayTypeSpecifications Type

`object` ([Assay type specifications](ega-11-properties-assay-type-specifications.md))

all of

*   [If the assay is of type array its specifications will be expected](ega-11-properties-assay-type-specifications-allof-if-the-assay-is-of-type-array-its-specifications-will-be-expected.md "check type definition")

# assayTypeSpecifications Properties

| Property                                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                          |
| :-------------------------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assayInstrument](#assayinstrument)                             | `string` | Required | cannot be null | [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-assay-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/assayInstrument")                                         |
| [arrayAssaySpecifications](#arrayassayspecifications)           | Merged   | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications")          |
| [sequencingAssaySpecifications](#sequencingassayspecifications) | `object` | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-a-sequencing-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/sequencingAssaySpecifications") |

## assayInstrument

The general categories, either sequencing or array, in which assays are categorized based on the used instruments. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`assayInstrument`

*   is required

*   Type: `string` ([Assay type](ega-11-properties-assay-type-specifications-properties-assay-type.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-assay-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/assayInstrument")

### assayInstrument Type

`string` ([Assay type](ega-11-properties-assay-type-specifications-properties-assay-type.md))

### assayInstrument Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation                                                                                                    |
| :------------ | :------------------------------------------------------------------------------------------------------------- |
| `"array"`     | An assay in which an \[array instrument \[EFO:0002698]]\(http\://www\.ebi.ac.uk/efo/EFO\_0002698) was used.    |
| `"sequencer"` | An assay in which a \[sequencer instrument \[EFO:0003739]]\(http\://www\.ebi.ac.uk/efo/EFO\_0003739) was used. |

## arrayAssaySpecifications

Node containing the set of fields specific to an assay of type 'array' (i.e. an array was used to obtain the raw data).

`arrayAssaySpecifications`

*   is optional

*   Type: `object` ([Specifications of an array assay](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications")

### arrayAssaySpecifications Type

`object` ([Specifications of an array assay](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay.md))

any of

*   [2 labels per array check](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-2-labels-per-array-check.md "check type definition")

*   [3 labels per array check](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-3-labels-per-array-check.md "check type definition")

*   [4 labels per array check](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-4-labels-per-array-check.md "check type definition")

## sequencingAssaySpecifications

Node containing the set of fields specific to an assay of type 'sequencer' (i.e. a sequencer was used to obtain the raw data).

`sequencingAssaySpecifications`

*   is optional

*   Type: `object` ([Specifications of a sequencing assay](ega-11-properties-assay-type-specifications-properties-specifications-of-a-sequencing-assay.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-a-sequencing-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/sequencingAssaySpecifications")

### sequencingAssaySpecifications Type

`object` ([Specifications of a sequencing assay](ega-11-properties-assay-type-specifications-properties-specifications-of-a-sequencing-assay.md))
