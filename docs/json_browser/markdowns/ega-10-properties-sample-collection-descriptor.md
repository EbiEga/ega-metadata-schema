# Sample collection descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection
```

Node containing the provenance details (when and where) of the sample. This information does not include the whole sample collection protocol (expected at experiment's protocols), only the sampling date (when the sample was taken from the individual) and site (where was it taken within the individual).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sampleCollection Type

`object` ([Sample collection descriptor](ega-10-properties-sample-collection-descriptor.md))

any of

*   [Either the collection date is required](ega-10-properties-sample-collection-descriptor-anyof-either-the-collection-date-is-required.md "check type definition")

*   [Or the age at collection is required](ega-10-properties-sample-collection-descriptor-anyof-or-the-age-at-collection-is-required.md "check type definition")

*   [Or the sampling site is required](ega-10-properties-sample-collection-descriptor-anyof-or-the-sampling-site-is-required.md "check type definition")

# sampleCollection Properties

| Property                                      | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                          |
| :-------------------------------------------- | :----- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sampleCollectionDate](#samplecollectiondate) | Merged | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-collection-descriptor-properties-date-of-the-sample-collection.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/sampleCollectionDate")   |
| [ageAtCollection](#ageatcollection)           | Merged | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection") |
| [samplingSite](#samplingsite)                 | Merged | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-collection-descriptor-properties-sampling-site.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/samplingSite")                           |

## sampleCollectionDate

Date when the sample was collected (e.g. '2021-05-15'). If the protocols are too long, the date shall be the day the collection concluded.

`sampleCollectionDate`

*   is optional

*   Type: `string` ([Date of the sample collection](ega-10-properties-sample-collection-descriptor-properties-date-of-the-sample-collection.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-collection-descriptor-properties-date-of-the-sample-collection.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/sampleCollectionDate")

### sampleCollectionDate Type

`string` ([Date of the sample collection](ega-10-properties-sample-collection-descriptor-properties-date-of-the-sample-collection.md))

all of

*   [Pattern of EGA ISO 8601 date](ega-4-definitions-pattern-of-ega-iso-8601-date.md "check type definition")

## ageAtCollection

Property describing the individual's age at sample collection. Can either be the precise age an age range.

`ageAtCollection`

*   is optional

*   Type: `object` ([Individual's age at sample collection](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection")

### ageAtCollection Type

`object` ([Individual's age at sample collection](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection.md))

any of

*   [Either the age is needed](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-anyof-either-the-age-is-needed.md "check type definition")

*   [Or the age-range is needed](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-anyof-or-the-age-range-is-needed.md "check type definition")

## samplingSite

A site or entity from which a sample (i.e. a statistically representative of the whole) is extracted from the whole. Search for your sample collection site at <http://purl.obolibrary.org/obo/UBERON_0000465>. For example: in the case of a nasal swab, it would be 'nasal cavity'; in a liver biopsy it would be 'liver'.

`samplingSite`

*   is optional

*   Type: `object` ([Sampling site](ega-10-properties-sample-collection-descriptor-properties-sampling-site.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-collection-descriptor-properties-sampling-site.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/samplingSite")

### samplingSite Type

`object` ([Sampling site](ega-10-properties-sample-collection-descriptor-properties-sampling-site.md))

all of

*   all of

    *   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")
