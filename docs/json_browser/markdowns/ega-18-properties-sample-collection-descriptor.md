# Sample collection descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection
```

Node containing the provenance details (when and where) of the sample. This information does not include the whole sample collection protocol (expected at experiment's protocols), only the sampling date (when the sample was taken from the individual) and site (where was it taken within the individual).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sample\_collection Type

`object` ([Sample collection descriptor](ega-18-properties-sample-collection-descriptor.md))

any of

*   [Either the collection date is required](ega-18-properties-sample-collection-descriptor-anyof-either-the-collection-date-is-required.md "check type definition")

*   [Or the age at collection is required](ega-18-properties-sample-collection-descriptor-anyof-or-the-age-at-collection-is-required.md "check type definition")

*   [Or the sampling site is required](ega-18-properties-sample-collection-descriptor-anyof-or-the-sampling-site-is-required.md "check type definition")

# sample\_collection Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sample\_collection\_date](#sample_collection_date) | Merged   | Optional | cannot be null | [EGA sample metadata schema](ega-18-properties-sample-collection-descriptor-properties-date-of-the-sample-collection.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sample_collection_date")   |
| [age\_at\_collection](#age_at_collection)           | Merged   | Optional | cannot be null | [EGA sample metadata schema](ega-18-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/age_at_collection") |
| [sampling\_site](#sampling_site)                    | `object` | Optional | cannot be null | [EGA sample metadata schema](ega-18-properties-sample-collection-descriptor-properties-sampling-site.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sampling_site")                            |

## sample\_collection\_date

Date when the sample was collected (e.g. '2021-05-15'). If the protocols are too long, the date shall be the day the collection concluded.

`sample_collection_date`

*   is optional

*   Type: `string` ([Date of the sample collection](ega-18-properties-sample-collection-descriptor-properties-date-of-the-sample-collection.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-sample-collection-descriptor-properties-date-of-the-sample-collection.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sample_collection_date")

### sample\_collection\_date Type

`string` ([Date of the sample collection](ega-18-properties-sample-collection-descriptor-properties-date-of-the-sample-collection.md))

all of

*   [Pattern of EGA ISO 8601 date](ega-12-definitions-pattern-of-ega-iso-8601-date.md "check type definition")

## age\_at\_collection

Property describing the individual's age at sample collection. Can either be the precise age an age range.

`age_at_collection`

*   is optional

*   Type: `object` ([Individual's age at sample collection](ega-18-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/age_at_collection")

### age\_at\_collection Type

`object` ([Individual's age at sample collection](ega-18-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection.md))

any of

*   [Either the age is needed](ega-18-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-anyof-either-the-age-is-needed.md "check type definition")

*   [Or the age-range is needed](ega-18-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-anyof-or-the-age-range-is-needed.md "check type definition")

## sampling\_site

A site from which a sample, i.e. a statistically representative of the whole, is extracted from the whole.

`sampling_site`

*   is optional

*   Type: `object` ([Sampling site](ega-18-properties-sample-collection-descriptor-properties-sampling-site.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-sample-collection-descriptor-properties-sampling-site.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sampling_site")

### sampling\_site Type

`object` ([Sampling site](ega-18-properties-sample-collection-descriptor-properties-sampling-site.md))
