# Untitled undefined type in EGA assay metadata schema Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/allOf/0/if/properties/assay_files/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.assay.json\*](../../../schemas/EGA.assay.json "open original schema") |

## items Type

unknown

# items Properties

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                 |
| :-------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filetype](#filetype) | Not specified | Optional | cannot be null | [EGA assay metadata schema](ega-11-allof-if-the-files-are-aligned-reads-the-reference-alignment-details-are-expected-if-properties-assay_files-items-properties-filetype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/allOf/0/if/properties/assay_files/items/properties/filetype") |

## filetype



`filetype`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-allof-if-the-files-are-aligned-reads-the-reference-alignment-details-are-expected-if-properties-assay_files-items-properties-filetype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.assay.json#/allOf/0/if/properties/assay_files/items/properties/filetype")

### filetype Type

unknown

### filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"BAM"`  |             |
| `"CRAM"` |             |
