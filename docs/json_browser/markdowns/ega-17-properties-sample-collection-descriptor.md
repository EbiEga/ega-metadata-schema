# Sample collection descriptor Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection
```

Node containing the provenance details (when and where) of the sample. This information does not include the whole sample collection protocol (expected at experiment's protocols), only the sampling date (when the sample was taken from the individual) and site (where was it taken within the individual).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sample\_collection Type

`object` ([Sample collection descriptor](ega-17-properties-sample-collection-descriptor.md))

any of

*   [Either the collection date is required](ega-17-properties-sample-collection-descriptor-anyof-either-the-collection-date-is-required.md "check type definition")

*   [Or the collection site is required](ega-17-properties-sample-collection-descriptor-anyof-or-the-collection-site-is-required.md "check type definition")

# sample\_collection Properties

| Property                                                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                    |
| :--------------------------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [sample\_collection\_date](#sample_collection_date)              | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-12-definitions-pattern-of-an-ega-iso-date-yyyy-mm-dd.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sample_collection_date")                                   |
| [sample\_collection\_site](#sample_collection_site)              | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-12-definitions-uberons-anatomical-entity.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sample_collection_site")                                               |
| [sample\_collection\_site\_curie](#sample_collection_site_curie) | Merged   | Optional | cannot be null | [EGA sample metadata schema](ega-17-properties-sample-collection-descriptor-properties-curie-of-the-sampling-site.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sample_collection_site_curie") |

## sample\_collection\_date

ISO date (format YYYY-MM-DD - e.g. '2021-05-15') when the sample was collected. If the protocols are long enough, the date shall be the day the collection concluded.

`sample_collection_date`

*   is optional

*   Type: `string` ([Pattern of an EGA ISO date (YYYY-MM-DD)](ega-12-definitions-pattern-of-an-ega-iso-date-yyyy-mm-dd.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-12-definitions-pattern-of-an-ega-iso-date-yyyy-mm-dd.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sample_collection_date")

### sample\_collection\_date Type

`string` ([Pattern of an EGA ISO date (YYYY-MM-DD)](ega-12-definitions-pattern-of-an-ega-iso-date-yyyy-mm-dd.md))

### sample\_collection\_date Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]{4}-(0[0-9]|1[0-2])-([012][0-9]|3[01])$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-\(0%5B0-9%5D%7C1%5B0-2%5D\)-\(%5B012%5D%5B0-9%5D%7C3%5B01%5D\)%24 "try regular expression with regexr.com")

### sample\_collection\_date Examples

```json
"2021-04-30"
```

## sample\_collection\_site

Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species. Term shall be one of UBERON's ontologized terms beneath anatomical entity \[UBERON:0001062]. Search for yours at: <http://purl.obolibrary.org/obo/UBERON_0001062>. It can be used to describe a sampling site or the morphological site of a disease, for example. #! To be used as an ontology validation node in the future.

`sample_collection_site`

*   is optional

*   Type: `string` ([UBERON's Anatomical entity](ega-12-definitions-uberons-anatomical-entity.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-12-definitions-uberons-anatomical-entity.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sample_collection_site")

### sample\_collection\_site Type

`string` ([UBERON's Anatomical entity](ega-12-definitions-uberons-anatomical-entity.md))

### sample\_collection\_site Examples

```json
"liver"
```

```json
"gut wall"
```

```json
"nasal cavity"
```

## sample\_collection\_site\_curie

Ontology term in CURIE format (e.g. 'UBERON:0000167') of the sampling site. The ontology to use is UBERON's anatomical entity \[UBERON:0001062]. Search for your ontologized term at <http://purl.obolibrary.org/obo/UBERON_0001062>. For example, in the case of a nasal swab, it would be 'UBERON:0001707'; in a liver biopsy it would be 'UBERON:0002107'.

`sample_collection_site_curie`

*   is optional

*   Type: `string` ([CURIE of the sampling site](ega-17-properties-sample-collection-descriptor-properties-curie-of-the-sampling-site.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-sample-collection-descriptor-properties-curie-of-the-sampling-site.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection/properties/sample_collection_site_curie")

### sample\_collection\_site\_curie Type

`string` ([CURIE of the sampling site](ega-17-properties-sample-collection-descriptor-properties-curie-of-the-sampling-site.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

### sample\_collection\_site\_curie Examples

```json
"UBERON:0000167"
```

```json
"UBERON:0001707"
```

```json
"UBERON:0000328"
```

```json
"UBERON:0002107"
```
