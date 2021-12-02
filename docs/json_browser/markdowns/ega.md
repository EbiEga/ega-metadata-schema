# EGA ArrayAssay metadata schema Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its ArrayAssay metadata object. This object is intended to contain metadata about the physical array to which the assayed molecule is hybridized. Used exclusively an Array Format (AF) submission. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                               |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.ArrayAssay.json](../out/EGA.ArrayAssay.json "open original schema") |

## EGA ArrayAssay metadata schema Type

`object` ([EGA ArrayAssay metadata schema](ega.md))

# EGA ArrayAssay metadata schema Properties

| Property                                                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                        |
| :------------------------------------------------------ | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object_id](#object_id)                                 | Merged    | Required | cannot be null | [EGA ArrayAssay metadata schema](ega-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/object_id")                                 |
| [array_assay_center](#array_assay_center)               | `string`  | Required | cannot be null | [EGA ArrayAssay metadata schema](ega-properties-centername-that-performed-the-arrayassay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_center") |
| [array_assay_date](#array_assay_date)                   | `string`  | Optional | cannot be null | [EGA ArrayAssay metadata schema](ega-properties-pattern-of-an-ega-iso-date-yyyy-mm-dd.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_date")      |
| [sample_number](#sample_number)                         | `integer` | Optional | cannot be null | [EGA ArrayAssay metadata schema](ega-properties-number-of-samples-of-the-arrayassay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/sample_number")           |
| [sample_labels](#sample_labels)                         | `array`   | Optional | cannot be null | [EGA ArrayAssay metadata schema](ega-properties-array-of-sample-label-pairs-of-the-arrayassay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/sample_labels") |
| [array_assay_relationships](#array_assay_relationships) | `array`   | Optional | cannot be null | [EGA ArrayAssay metadata schema](ega-properties-arrayassay-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_relationships")          |
| [assay_files](#assay_files)                             | `array`   | Required | cannot be null | [EGA ArrayAssay metadata schema](ega-properties-assay-files-object-from-an-arrayassay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/assay_files")           |
| [array_assay_attributes](#array_assay_attributes)       | `array`   | Optional | cannot be null | [EGA ArrayAssay metadata schema](ega-properties-arrayassay-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_attributes")         |

## object_id

Node containing the main identifiers of the object (e.g. alias, center_name...), inherited from the common definitions. #! We extend the core object (object_core_id) by adding a pattern check based on this schema's nature: an ArrayAssay (by using EGA-ArrayAssay-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA ArrayAssay metadata schema](ega-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/object_id")

### object_id Type

`object` ([Object's IDs block](ega-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that ArrayAssay EGA ID (EGAA) is correct](ega-properties-objects-ids-block-allof-check-that-arrayassay-ega-id-egaa-is-correct.md "check type definition")

## array_assay_center

The name of the center (e.g. 'EBI-TEST') responsible for the profiling by microarray (executed the ArrayAssay), if applicable (in case it’s different from the center submitting metadata).

`array_assay_center`

*   is required

*   Type: `string` ([Centername that performed the ArrayAssay](ega-properties-centername-that-performed-the-arrayassay.md))

*   cannot be null

*   defined in: [EGA ArrayAssay metadata schema](ega-properties-centername-that-performed-the-arrayassay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_center")

### array_assay_center Type

`string` ([Centername that performed the ArrayAssay](ega-properties-centername-that-performed-the-arrayassay.md))

### array_assay_center Examples

```json
"EBI-TEST"
```

## array_assay_date

ISO date (format YYYY-MM-DD - e.g. '2021-05-15') when the ArrayAssay took place. If the protocols are long enough, the date shall be the day the ArrayAssay concluded.

`array_assay_date`

*   is optional

*   Type: `string` ([Pattern of an EGA ISO date (YYYY-MM-DD)](ega-properties-pattern-of-an-ega-iso-date-yyyy-mm-dd.md))

*   cannot be null

*   defined in: [EGA ArrayAssay metadata schema](ega-properties-pattern-of-an-ega-iso-date-yyyy-mm-dd.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_date")

### array_assay_date Type

`string` ([Pattern of an EGA ISO date (YYYY-MM-DD)](ega-properties-pattern-of-an-ega-iso-date-yyyy-mm-dd.md))

### array_assay_date Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(19|20)[0-9]{2}-(0[0-9]|1[0-2])-([012][0-9]|3[01])$
```

[try pattern](https://regexr.com/?expression=%5E\(19%7C20\)%5B0-9%5D%7B2%7D-\(0%5B0-9%5D%7C1%5B0-2%5D\)-\(%5B012%5D%5B0-9%5D%7C3%5B01%5D\)%24 "try regular expression with regexr.com")

### array_assay_date Examples

```json
"2021-04-30"
```

## sample_number

Number of samples included in the Assay (i.e. pooled into one single microarray, labelled differently). One sample corresponds to one biological replicate \[EFO:0002091] (it could be the genetic content from a single cell, a tissue… from a single individual or from several individuals). Shall not be mistaken for technical replicates \[CHEBI:24432] being used several times (see <https://www.ebi.ac.uk/seqdb/confluence/pages/viewpage.action?spaceKey=EGA&title=Sample+Representation>).

`sample_number`

*   is optional

*   Type: `integer` ([Number of samples of the ArrayAssay](ega-properties-number-of-samples-of-the-arrayassay.md))

*   cannot be null

*   defined in: [EGA ArrayAssay metadata schema](ega-properties-number-of-samples-of-the-arrayassay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/sample_number")

### sample_number Type

`integer` ([Number of samples of the ArrayAssay](ega-properties-number-of-samples-of-the-arrayassay.md))

### sample_number Examples

```json
30
```

## sample_labels

Sample-Label pairs (format being 'EGAN\[0-9]{11}:Label' - e.g. 'EGAN00000000001:Cy3') to know which samples used in this assay are labelled by which chemicals. Could be omitted if the array is of one single label and colour. #! Using an empty item list but defining the sample-label pairs as possible additionalItems we create the correct constraint: anything but a sample-label pair is rejected, but EGA can add as many as required.

`sample_labels`

*   is optional

*   Type: `object[]` ([Repeatable Sample-label node](ega-2-definitions-repeatable-sample-label-node.md))

*   cannot be null

*   defined in: [EGA ArrayAssay metadata schema](ega-properties-array-of-sample-label-pairs-of-the-arrayassay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/sample_labels")

### sample_labels Type

`object[]` ([Repeatable Sample-label node](ega-2-definitions-repeatable-sample-label-node.md))

### sample_labels Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## array_assay_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. an ArrayAssay being linked to a Sample) the EGA. #! Using an empty item list but defining the relationship as possible additionalItems we create the correct constraint: anything but a relationship object is rejected, but EGA can add as many as required.

`array_assay_relationships`

*   is optional

*   Type: `object[]` ([EGA Relationships object](ega-2-definitions-ega-relationships-object.md))

*   cannot be null

*   defined in: [EGA ArrayAssay metadata schema](ega-properties-arrayassay-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_relationships")

### array_assay_relationships Type

`object[]` ([EGA Relationships object](ega-2-definitions-ega-relationships-object.md))

### array_assay_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## assay_files

This array object contains the specific files derived from performing an hybridization of the assayed molecule to a physical array. Given the amount of technologies available for such purpose, the allowed filetypes shall be agreed upon and updated accordingly. #! Using an empty item list but defining the file object as possible additionalItems we create the correct constraint: anything but a file object is rejected, but EGA can add as many as required.

`assay_files`

*   is required

*   Type: `object[]` ([EGA File object](ega-2-definitions-ega-file-object.md))

*   cannot be null

*   defined in: [EGA ArrayAssay metadata schema](ega-properties-assay-files-object-from-an-arrayassay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/assay_files")

### assay_files Type

`object[]` ([EGA File object](ega-2-definitions-ega-file-object.md))

### assay_files Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## array_assay_attributes

Custom attributes of an ArrayAssay: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema. #! Using an empty item list but defining the custom attributes as possible additionalItems we create the correct constraint: anything but a custom attribute is rejected, but EGA can add as many as required.

`array_assay_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-2-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA ArrayAssay metadata schema](ega-properties-arrayassay-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_attributes")

### array_assay_attributes Type

`object[]` ([Custom attribute of an object](ega-2-definitions-custom-attribute-of-an-object.md))

### array_assay_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
