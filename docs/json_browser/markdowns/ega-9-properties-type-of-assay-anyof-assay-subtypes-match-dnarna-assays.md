# Assay subtypes match DNA/RNA assays Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayTypeDescriptor/anyOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## 0 Type

unknown ([Assay subtypes match DNA/RNA assays](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays.md))

# 0 Properties

| Property                      | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                           |
| :---------------------------- | :----- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assaySubtype](#assaysubtype) | Merged | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assaysubtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayTypeDescriptor/anyOf/0/properties/assaySubtype") |

## assaySubtype



`assaySubtype`

*   is optional

*   Type: merged type ([Details](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assaysubtype.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assaysubtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayTypeDescriptor/anyOf/0/properties/assaySubtype")

### assaySubtype Type

merged type ([Details](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assaysubtype.md))

any of

*   [DNA-Assay subtype controlled vocabulary (CV) list](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assaysubtype-anyof-dna-assay-subtype-controlled-vocabulary-cv-list.md "check type definition")

*   [RNA-Assay subtype controlled vocabulary (CV) list](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assaysubtype-anyof-rna-assay-subtype-controlled-vocabulary-cv-list.md "check type definition")
