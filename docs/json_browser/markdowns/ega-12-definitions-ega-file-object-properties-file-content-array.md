# File content array Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/file_content
```

Array of file content items. This array exists to clarify what the purpose of a file, regardless of its format, may be. For example, a TXT formatted file could contain multiple types of data, from gene annotations to READMEs. Therefore, select the items from the used ontology that best describe the content of your file.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## file\_content Type

`object[]` ([File content item](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item.md))

## file\_content Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
