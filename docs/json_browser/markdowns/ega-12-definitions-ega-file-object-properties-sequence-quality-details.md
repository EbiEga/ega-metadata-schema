# Sequence quality details Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details
```

Sequencing quality scores measure the probability that a base is called (i.e. sequenced) incorrectly. New sequencing technologies assign a quality score to each of the bases in the sequence.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## sequence\_quality\_details Type

`object` ([Sequence quality details](ega-12-definitions-ega-file-object-properties-sequence-quality-details.md))

# sequence\_quality\_details Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                            |
| :-------------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [quality\_scoring\_system](#quality_scoring_system) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/quality_scoring_system") |
| [quality\_encoding](#quality_encoding)              | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/quality_encoding")      |
| [ascii\_offset](#ascii_offset)                      | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/ascii_offset")                     |

## quality\_scoring\_system

How the quality score was computed for the data.

`quality_scoring_system`

*   is required

*   Type: `string` ([Quality scoring system](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/quality_scoring_system")

### quality\_scoring\_system Type

`string` ([Quality scoring system](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md))

### quality\_scoring\_system Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation                                                                                                                                                                                                     |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"phred"`    | The quality score is expressed as a probability of error in log form: -10 log(1/p) where p is the probability of error, with value range 0..63 (0 meaning no base call).                                        |
| `"log-odds"` | The quality score is expressed as the ratio of error to non-error in log form: -10 log(p/(1-p)) where p is the of error, with value range -40..40. The SRA will convert these into phred scale during loadtime. |

## quality\_encoding

Encoding system used to represent the quality score.

`quality_encoding`

*   is optional

*   Type: `string` ([Quality encoding format](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/quality_encoding")

### quality\_encoding Type

`string` ([Quality encoding format](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md))

### quality\_encoding Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation                                 |
| :-------------- | :------------------------------------------ |
| `"ascii"`       | ASCII character based encoding.             |
| `"decimal"`     | Single decimal value per quality score.     |
| `"hexadecimal"` | Single hexadecimal value per quality score. |

## ascii\_offset

Character used in representing the minimum quality value.  Helps specify how to decode text rendering of quality data.

`ascii_offset`

*   is optional

*   Type: `string` ([ASCII offset](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/ascii_offset")

### ascii\_offset Type

`string` ([ASCII offset](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md))

### ascii\_offset Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation                                      |
| :---- | :----------------------------------------------- |
| `"!"` | ASCII value 33.  Typically used for range 0..63. |
| `"@"` | ASCII value 64.  Typically used for range 0..60. |
