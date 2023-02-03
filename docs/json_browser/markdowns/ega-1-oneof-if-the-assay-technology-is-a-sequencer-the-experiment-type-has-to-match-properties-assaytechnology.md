# Untitled undefined type in EGA Experiment metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/oneOf/0/properties/assayTechnology
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## assayTechnology Type

unknown

# assayTechnology Properties

| Property                            | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                    |
| :---------------------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assayInstrument](#assayinstrument) | Not specified | Optional | cannot be null | [EGA Experiment metadata schema](ega-1-oneof-if-the-assay-technology-is-a-sequencer-the-experiment-type-has-to-match-properties-assaytechnology-properties-assayinstrument.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/oneOf/0/properties/assayTechnology/properties/assayInstrument") |

## assayInstrument



`assayInstrument`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-oneof-if-the-assay-technology-is-a-sequencer-the-experiment-type-has-to-match-properties-assaytechnology-properties-assayinstrument.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/oneOf/0/properties/assayTechnology/properties/assayInstrument")

### assayInstrument Type

unknown

### assayInstrument Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation |
| :------------ | :---------- |
| `"sequencer"` |             |
