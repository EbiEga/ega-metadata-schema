# Core identifiers of an object Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/objectId/allOf/0
```

Base definition containing the properties (e.g. Sample's alias) of a minimal identification layer of an EGA object (e.g. Sample).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## 0 Type

`object` ([Core identifiers of an object](ega-4-definitions-core-identifiers-of-an-object.md))

any of

*   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

*   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

*   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

# 0 Properties

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                 |
| :---------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [alias](#alias)                           | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/alias")                     |
| [centerName](#centername)                 | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/centerName")      |
| [egaAccession](#egaaccession)             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/egaAccession")    |
| [externalAccessions](#externalaccessions) | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/externalAccessions") |

## alias

Submitter designated name (e.g. 'my\_sample\_J13') for the object (e.g. Sample). The name must be unique within the submission account (e.g. 'ega-box-79'), since the aliases and submission accounts are concatenated within our database to obtain the unique alias (e.g. 'ega-box-79::my\_sample\_J13').

`alias`

*   is optional

*   Type: `string` ([Alias of an object](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/alias")

### alias Type

`string` ([Alias of an object](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

### alias Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### alias Examples

```json
"my_sample_J13"
```

## centerName

Center name (e.g. 'EBI-TEST') associated to the submitter. In other words, it is the acronym of the submitter's account (provided by the HelpDesk team).

`centerName`

*   is optional

*   Type: `string` ([Center name of the submitter](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/centerName")

### centerName Type

`string` ([Center name of the submitter](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

### centerName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### centerName Examples

```json
"EBI-TEST"
```

## egaAccession

The object accession (i.e. unique identifier) assigned by the archive (EGA). Object accessions can be found in the 'Identifiers' section of the EGA-archive website (<https://ega-archive.org/metadata/how-to-use-the-api>) and commonly start with EGA, followed by the distinctive letter of the object and finally the numeric ID of the instance.

`egaAccession`

*   is optional

*   Type: `string` ([EGA's accession of the object](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/egaAccession")

### egaAccession Type

`string` ([EGA's accession of the object](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

### egaAccession Examples

```json
"EGAN00003245489"
```

## externalAccessions

External accession node to reference objects in other archives (e.g. an already existing sample at BioSamples).

`externalAccessions`

*   is optional

*   Type: `object[]` ([Object External accession](ega-4-definitions-object-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/externalAccessions")

### externalAccessions Type

`object[]` ([Object External accession](ega-4-definitions-object-external-accession.md))

### externalAccessions Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
