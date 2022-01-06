# Assayed molecule in the ArrayExperiment \[EFO:0002772] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/assayed_molecule
```

Type of molecule assayed. It contains both the human readable ID (e.g. DNA assay) and CURIE (e.g. EFO:0001456) of the assayed molecule.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## assayed_molecule Type

`object` ([Assayed molecule in the ArrayExperiment \[EFO:0002772\]](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772.md))

# assayed_molecule Properties

| Property                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                   |
| :------------------------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assayed_molecule_id](#assayed_molecule_id)       | `string` | Required | cannot be null | [EGA ArrayExperiment metadata schema](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772-properties-array-type-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/assayed_molecule/properties/assayed_molecule_id")       |
| [assayed_molecule_curie](#assayed_molecule_curie) | `string` | Optional | cannot be null | [EGA ArrayExperiment metadata schema](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772-properties-array-type-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/assayed_molecule/properties/assayed_molecule_curie") |

## assayed_molecule_id

The human readable ID (e.g. DNA assay), chosen from a list of CVs, of the assayed molecule.

`assayed_molecule_id`

*   is required

*   Type: `string` ([Array type of the ArrayExperiment - ID](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772-properties-array-type-of-the-arrayexperiment---id.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772-properties-array-type-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/assayed_molecule/properties/assayed_molecule_id")

### assayed_molecule_id Type

`string` ([Array type of the ArrayExperiment - ID](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772-properties-array-type-of-the-arrayexperiment---id.md))

### assayed_molecule_id Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                     | Explanation |
| :------------------------ | :---------- |
| `"DNA assay"`             |             |
| `"RNA assay"`             |             |
| `"Metabolomic profiling"` |             |
| `"Protein assay"`         |             |

### assayed_molecule_id Examples

```json
"DNA assay"
```

## assayed_molecule_curie

The CURIE (i.e. ontologized term - e.g. EFO:0001456), chosen from a list of CVs, of the assayed molecule.

`assayed_molecule_curie`

*   is optional

*   Type: `string` ([Array type of the ArrayExperiment - CURIE](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772-properties-array-type-of-the-arrayexperiment---curie.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772-properties-array-type-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/assayed_molecule/properties/assayed_molecule_curie")

### assayed_molecule_curie Type

`string` ([Array type of the ArrayExperiment - CURIE](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772-properties-array-type-of-the-arrayexperiment---curie.md))

### assayed_molecule_curie Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"EFO:0001456"` |             |
| `"EFO:0001457"` |             |
| `"EFO:0000752"` |             |
| `"EFO:0001458"` |             |

### assayed_molecule_curie Examples

```json
"EFO:0001456"
```
