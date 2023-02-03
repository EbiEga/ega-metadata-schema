# Minimal public attributes describing an individual Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes
```

Among all attributes describing an individual, some may contain identifiable metadata and thus must be private. Nevertheless, there are three/four required attributes (even if they are unknown): subject id, biological sex, phenotypicAbnormalities and/or diseases. These shall be displayed and queryable on our portal. In the case of a healthy individual (with no phenotypic abnormalities nor diseases), the 'phenotypicAbnormalities' and 'diseases' arrays will contain a reference to 'Unaffected' \[NCIT:C94232]. Do take into account the 'excluded' property of each 'disease' or 'phenotypicAbnormality' in order to evaluate it correctly, since logic negation can be provided using that property.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## minimalPublicAttributes Type

`object` ([Minimal public attributes describing an individual](ega-6-properties-minimal-public-attributes-describing-an-individual.md))

any of

*   [Either the phenotypicAbnormalities array is given](ega-6-properties-minimal-public-attributes-describing-an-individual-anyof-either-the-phenotypicabnormalities-array-is-given.md "check type definition")

*   [Or the diseases array is given](ega-6-properties-minimal-public-attributes-describing-an-individual-anyof-or-the-diseases-array-is-given.md "check type definition")

# minimalPublicAttributes Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                   |
| :-------------------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [subjectId](#subjectid)                             | `string` | Required | cannot be null | [EGA individual metadata schema](ega-4-definitions-subject-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/subjectId")                                                                                                   |
| [biologicalSex](#biologicalsex)                     | `string` | Required | cannot be null | [EGA individual metadata schema](ega-4-definitions-biological-sex-of-the-individual.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/biologicalSex")                                                                         |
| [phenotypicAbnormalities](#phenotypicabnormalities) | `array`  | Optional | cannot be null | [EGA individual metadata schema](ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-phenotypic-abnormalities.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/phenotypicAbnormalities") |
| [diseases](#diseases)                               | `array`  | Optional | cannot be null | [EGA individual metadata schema](ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases")                                |

## subjectId

A unique identifier (e.g. 'Donor-10031') for the subject the sample derives from, providing context for the sample to be better understood through its provenance. It **shall not** contain personal sensitive data, since it will be publicly displayed for queries and searches.

`subjectId`

*   is required

*   Type: `string` ([Subject ID](ega-4-definitions-subject-id.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-4-definitions-subject-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/subjectId")

### subjectId Type

`string` ([Subject ID](ega-4-definitions-subject-id.md))

### subjectId Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### subjectId Examples

```json
"Donor-10031"
```

```json
"ID001"
```

```json
"9001"
```

```json
"AX_Dli"
```

## biologicalSex

An organismal quality inhering in a bearer by virtue of the bearer's physical expression of sexual characteristics. In other words, the trait that determines the individual's (from which the sample derives) reproductive function: mainly male or female. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`biologicalSex`

*   is required

*   Type: `string` ([Biological sex of the individual](ega-4-definitions-biological-sex-of-the-individual.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-4-definitions-biological-sex-of-the-individual.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/biologicalSex")

### biologicalSex Type

`string` ([Biological sex of the individual](ega-4-definitions-biological-sex-of-the-individual.md))

### biologicalSex Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                   | Explanation                                                                                                                                                                                                             |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"male"`                | \[PATO:0000384]: A biological sex quality inhering in an individual or a population whose sex organs contain only male gametes.                                                                                         |
| `"female"`              | \[PATO:0000383]: A biological sex quality inhering in an individual or a population that only produces gametes that can be fertilised by male gametes.                                                                  |
| `"hermaphrodite"`       | \[PATO:0001340]: An organism having both male and female sexual characteristics and organs. A biological sex quality inhering in an organism or a population with both male and female sexual organs in one individual. |
| `"pseudohermaphrodite"` | \[PATO:0001827]: A biological sex quality inhering in an individual or a population by virtue of having internal reproductive organs of one sex and external sexual characteristics of the other sex.                   |
| `"unknown"`             | \[NCIT:C17998]: The biological sex is unknown, not assesed or not available.                                                                                                                                            |

### biologicalSex Examples

```json
"male"
```

## phenotypicAbnormalities



`phenotypicAbnormalities`

*   is optional

*   Type: `object[]` ([Phenotypic abnormality item](ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-phenotypic-abnormalities-phenotypic-abnormality-item.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-phenotypic-abnormalities.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/phenotypicAbnormalities")

### phenotypicAbnormalities Type

`object[]` ([Phenotypic abnormality item](ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-phenotypic-abnormalities-phenotypic-abnormality-item.md))

### phenotypicAbnormalities Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## diseases



`diseases`

*   is optional

*   Type: `object[]` ([Disease item](ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases-disease-item.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases")

### diseases Type

`object[]` ([Disease item](ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases-disease-item.md))

### diseases Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
