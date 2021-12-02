# Object of external accession of the object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions/items
```

External accession node containing the object accession (i.e. unique identifier -  each following their respective formats) assigned by other archives, the name of the archive (e.g. biosample, ena, ensembl...) and an optional label.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([Object of external accession of the object](ega-2-definitions-object-of-external-accession-of-the-object.md))

# items Properties

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                               |
| :---------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [external_accession](#external_accession) | Multiple | Required | cannot be null | [EGA common metadata definitions v0.0.1](ega-2-definitions-object-of-external-accession-of-the-object-properties-external-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/external_accession") |
| [accession_archive](#accession_archive)   | `string` | Required | cannot be null | [EGA common metadata definitions v0.0.1](ega-2-definitions-object-of-external-accession-of-the-object-properties-name-of-the-archive.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_archive")               |
| [accession_label](#accession_label)       | Multiple | Optional | cannot be null | [EGA common metadata definitions v0.0.1](ega-2-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_label")     |

## external_accession

Unique identifier of the object (e.g. SAMEA7616999), assigned by other archives (e.g. biosample).

`external_accession`

*   is required

*   Type: any of the folllowing: `string` or `number` ([External accession of the object](ega-2-definitions-object-of-external-accession-of-the-object-properties-external-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions v0.0.1](ega-2-definitions-object-of-external-accession-of-the-object-properties-external-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/external_accession")

### external_accession Type

any of the folllowing: `string` or `number` ([External accession of the object](ega-2-definitions-object-of-external-accession-of-the-object-properties-external-accession-of-the-object.md))

### external_accession Examples

```json
"SAMEA7616999"
```

## accession_archive

Name of the archive (e.g. biosample) from which the external accession is taken.

`accession_archive`

*   is required

*   Type: `string` ([Name of the archive](ega-2-definitions-object-of-external-accession-of-the-object-properties-name-of-the-archive.md))

*   cannot be null

*   defined in: [EGA common metadata definitions v0.0.1](ega-2-definitions-object-of-external-accession-of-the-object-properties-name-of-the-archive.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_archive")

### accession_archive Type

`string` ([Name of the archive](ega-2-definitions-object-of-external-accession-of-the-object-properties-name-of-the-archive.md))

### accession_archive Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"ensembl"`         |             |
| `"ena"`             |             |
| `"pubmed"`          |             |
| `"protein"`         |             |
| `"nuccore"`         |             |
| `"ipg"`             |             |
| `"nucleotide"`      |             |
| `"structure"`       |             |
| `"genome"`          |             |
| `"annotinfo"`       |             |
| `"assembly"`        |             |
| `"bioproject"`      |             |
| `"biosample"`       |             |
| `"blastdbinfo"`     |             |
| `"books"`           |             |
| `"cdd"`             |             |
| `"clinvar"`         |             |
| `"gap"`             |             |
| `"gapplus"`         |             |
| `"grasp"`           |             |
| `"dbvar"`           |             |
| `"gene"`            |             |
| `"gds"`             |             |
| `"geoprofiles"`     |             |
| `"homologene"`      |             |
| `"medgen"`          |             |
| `"mesh"`            |             |
| `"ncbisearch"`      |             |
| `"nlmcatalog"`      |             |
| `"omim"`            |             |
| `"orgtrack"`        |             |
| `"pmc"`             |             |
| `"popset"`          |             |
| `"proteinclusters"` |             |
| `"pcassay"`         |             |
| `"protfam"`         |             |
| `"biosystems"`      |             |
| `"pccompound"`      |             |
| `"pcsubstance"`     |             |
| `"seqannot"`        |             |
| `"snp"`             |             |
| `"sra"`             |             |
| `"taxonomy"`        |             |
| `"biocollections"`  |             |
| `"gtr"`             |             |

### accession_archive Examples

```json
"biosample"
```

## accession_label

Optional label (e.g. 'taken from biosample temporarily') of the external accession, used to add extra information to the identifier.

`accession_label`

*   is optional

*   Type: any of the folllowing: `string` or `number` ([Label of the external accession](ega-2-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions v0.0.1](ega-2-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_label")

### accession_label Type

any of the folllowing: `string` or `number` ([Label of the external accession](ega-2-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

### accession_label Examples

```json
"taken from biosample temporarily"
```
