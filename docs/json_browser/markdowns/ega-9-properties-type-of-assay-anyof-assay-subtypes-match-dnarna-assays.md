# Assay subtypes match DNA/RNA assays Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/anyOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## 0 Type

unknown ([Assay subtypes match DNA/RNA assays](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays.md))

# 0 Properties

| Property                         | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                     |
| :------------------------------- | :----- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assay\_subtype](#assay_subtype) | Merged | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assay_subtype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/anyOf/0/properties/assay_subtype") |

## assay\_subtype



`assay_subtype`

*   is optional

*   Type: merged type ([Details](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assay_subtype.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assay_subtype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/anyOf/0/properties/assay_subtype")

### assay\_subtype Type

merged type ([Details](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assay_subtype.md))

any of

*   [EGA Controlled Vocabulary (CV) for assay subtypes by DNA \[EFO:0001456\]](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assay_subtype-anyof-ega-controlled-vocabulary-cv-for-assay-subtypes-by-dna-efo0001456.md "check type definition")

*   [EGA Controlled Vocabulary (CV) for assay subtypes by RNA \[EFO:0001457\]](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assay_subtype-anyof-ega-controlled-vocabulary-cv-for-assay-subtypes-by-rna-efo0001457.md "check type definition")
