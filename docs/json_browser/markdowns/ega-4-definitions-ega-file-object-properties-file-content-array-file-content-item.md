# File content item Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent/items
```

Item describing the type of data a file contains or represents.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([File content item](ega-4-definitions-ega-file-object-properties-file-content-array-file-content-item.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# items Properties

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                      |
| :---------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent/items/properties/termId") |

## termId

Property containing just the ontology constraints for the file content. Notice the 'direct' being 'true', which makes the constraint more stringent, and only allows for terms one step below \[format:2350].

`termId`

*   is optional

*   Type: unknown ([Ontology constraints for this specific termId](ega-4-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent/items/properties/termId")

### termId Type

unknown ([Ontology constraints for this specific termId](ega-4-definitions-ega-file-object-properties-file-content-array-file-content-item-properties-ontology-constraints-for-this-specific-termid.md))

### termId Examples

```json
"format:1919"
```

```json
"format:3326"
```
