# Assay type specifications Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications
```

Node containing different sets of fields that depend on the specific assay type. The main categories of assay types follow a similar pattern as the used technology: either array assays (those in which an [array instrument \[EFO:0002698\]](http://www.ebi.ac.uk/efo/EFO\_0002698) was used) or sequencing assays (those in which a [sequencing instrument \[EFO:0003739\]](http://www.ebi.ac.uk/efo/EFO\_0003739) was used). Depending on the used technology, different types of fields will be required. For example, if an array was used, its sample_array_labels will be expected. Having this modular assay type-related node allows for easy additions of new technology-specific requirements.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                      |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.assay.json*](../out/EGA.assay.json "open original schema") |

## assay_type_specifications Type

`object` ([Assay type specifications](ega-11-properties-assay-type-specifications.md))

all of

*   [If the assay is of type array its specifications will be expected](ega-11-properties-assay-type-specifications-allof-if-the-assay-is-of-type-array-its-specifications-will-be-expected.md "check type definition")

# assay_type_specifications Properties

| Property                                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                    |
| :------------------------------------------------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assay_type](#assay_type)                                           | `string` | Required | cannot be null | [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-assay-type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/assay_type")                                                |
| [array_assay_specifications](#array_assay_specifications)           | Merged   | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/array_assay_specifications")          |
| [sequencing_assay_specifications](#sequencing_assay_specifications) | `object` | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-a-sequencing-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/sequencing_assay_specifications") |

## assay_type

The general categories, either sequencing or array, in which assays are categorized based on the used instruments. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`assay_type`

*   is required

*   Type: `string` ([Assay type](ega-11-properties-assay-type-specifications-properties-assay-type.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-assay-type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/assay_type")

### assay_type Type

`string` ([Assay type](ega-11-properties-assay-type-specifications-properties-assay-type.md))

### assay_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"array"`      |             |
| `"sequencing"` |             |

## array_assay_specifications

Node containing the set of fields specific to an assay of type 'array' (i.e. an array was used to obtain the raw data).

`array_assay_specifications`

*   is optional

*   Type: `object` ([Specifications of an array assay](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/array_assay_specifications")

### array_assay_specifications Type

`object` ([Specifications of an array assay](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay.md))

any of

*   [2 labels per array check](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-2-labels-per-array-check.md "check type definition")

*   [3 labels per array check](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-3-labels-per-array-check.md "check type definition")

*   [4 labels per array check](ega-11-properties-assay-type-specifications-properties-specifications-of-an-array-assay-anyof-4-labels-per-array-check.md "check type definition")

## sequencing_assay_specifications

Node containing the set of fields specific to an assay of type 'sequencing' (i.e. a sequencer was used to obtain the raw data).

`sequencing_assay_specifications`

*   is optional

*   Type: `object` ([Specifications of a sequencing assay](ega-11-properties-assay-type-specifications-properties-specifications-of-a-sequencing-assay.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-assay-type-specifications-properties-specifications-of-a-sequencing-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/properties/assay_type_specifications/properties/sequencing_assay_specifications")

### sequencing_assay_specifications Type

`object` ([Specifications of a sequencing assay](ega-11-properties-assay-type-specifications-properties-specifications-of-a-sequencing-assay.md))
