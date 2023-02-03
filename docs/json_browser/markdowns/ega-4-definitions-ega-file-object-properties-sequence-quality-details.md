# Sequence quality details Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails
```

Sequencing quality scores measure the probability that a base is called (i.e. sequenced) incorrectly. New sequencing technologies assign a quality score to each of the bases in the sequence.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## sequenceQualityDetails Type

`object` ([Sequence quality details](ega-4-definitions-ega-file-object-properties-sequence-quality-details.md))

# sequenceQualityDetails Properties

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                      |
| :-------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [qualityScoringSystem](#qualityscoringsystem) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails/properties/qualityScoringSystem") |
| [qualityEncoding](#qualityencoding)           | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails/properties/qualityEncoding")     |
| [asciiOffset](#asciioffset)                   | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails/properties/asciiOffset")                    |

## qualityScoringSystem

How the quality score was computed for the data.

`qualityScoringSystem`

*   is required

*   Type: `string` ([Quality scoring system](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails/properties/qualityScoringSystem")

### qualityScoringSystem Type

`string` ([Quality scoring system](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-scoring-system.md))

### qualityScoringSystem Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation                                                                                                                                                                                                     |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"phred"`   | The quality score is expressed as a probability of error in log form: -10 log(1/p) where p is the probability of error, with value range 0..63 (0 meaning no base call).                                        |
| `"logOdds"` | The quality score is expressed as the ratio of error to non-error in log form: -10 log(p/(1-p)) where p is the of error, with value range -40..40. The SRA will convert these into phred scale during loadtime. |

## qualityEncoding

Encoding system used to represent the quality score.

`qualityEncoding`

*   is optional

*   Type: `string` ([Quality encoding format](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails/properties/qualityEncoding")

### qualityEncoding Type

`string` ([Quality encoding format](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md))

### qualityEncoding Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation                                 |
| :-------------- | :------------------------------------------ |
| `"ascii"`       | ASCII character based encoding.             |
| `"decimal"`     | Single decimal value per quality score.     |
| `"hexadecimal"` | Single hexadecimal value per quality score. |

## asciiOffset

Character used in representing the minimum quality value.  Helps specify how to decode text rendering of quality data.

`asciiOffset`

*   is optional

*   Type: `string` ([ASCII offset](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails/properties/asciiOffset")

### asciiOffset Type

`string` ([ASCII offset](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md))

### asciiOffset Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation                                      |
| :---- | :----------------------------------------------- |
| `"!"` | ASCII value 33.  Typically used for range 0..63. |
| `"@"` | ASCII value 64.  Typically used for range 0..60. |
