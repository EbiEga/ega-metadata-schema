# Core identifiers of an object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id/allOf/0
```

Base definition containing the properties (e.g. Sample's alias) of a minimal identification layer of an EGA object (e.g. Sample).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## 0 Type

`object` ([Core identifiers of an object](ega-2-definitions-core-identifiers-of-an-object.md))

any of

*   [Check core IDs: combination of Alias and Center name](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

*   [Check core IDs: EGA accession ID](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

*   [Check core IDs: external accessions](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

# 0 Properties

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                          |
| :------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [alias](#alias)                             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-2-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/alias")                      |
| [center_name](#center_name)                 | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-2-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/center_name")      |
| [ega_accession](#ega_accession)             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-2-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/ega_accession")    |
| [external_accessions](#external_accessions) | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions") |

## alias

Submitter designated name (e.g. 'my_sample_J13') for the object (e.g. Sample). The name must be unique within the submission account (e.g. 'ega-box-79'), since the aliases and submission accounts are concatenated within our database to obtain the unique alias (e.g. 'ega-box-79::my_sample_J13').

`alias`

*   is optional

*   Type: `string` ([Alias of an object](ega-2-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/alias")

### alias Type

`string` ([Alias of an object](ega-2-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

### alias Examples

```json
"my_sample_J13"
```

## center_name

Center name (e.g. 'EBI-TEST') associated to the submitter. In other words, it is the acronym of the submitter's account (provided by the HelpDesk team).

`center_name`

*   is optional

*   Type: `string` ([Center name of the submitter](ega-2-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/center_name")

### center_name Type

`string` ([Center name of the submitter](ega-2-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

### center_name Examples

```json
"EBI-TEST"
```

## ega_accession

The object accession (i.e. unique identifier) assigned by the archive (EGA). Object accessions can be found in the 'Identifiers' section of the EGA-archive website (<https://ega-archive.org/metadata/how-to-use-the-api>) and commonly start with EGA, followed by the distinctive letter of the object and finally the numeric ID of the instance.

`ega_accession`

*   is optional

*   Type: `string` ([EGA's accession of the object](ega-2-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/ega_accession")

### ega_accession Type

`string` ([EGA's accession of the object](ega-2-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

### ega_accession Examples

```json
"EGAN00003245489"
```

## external_accessions

Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

`external_accessions`

*   is optional

*   Type: `object[]` ([Object of external accession of the object](ega-2-definitions-object-of-external-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions")

### external_accessions Type

`object[]` ([Object of external accession of the object](ega-2-definitions-object-of-external-accession-of-the-object.md))

### external_accessions Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
