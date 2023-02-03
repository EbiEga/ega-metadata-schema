# Cell type Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items/properties/cellType
```

Property to describe a cell type: a distinct morphological or functional form of cell.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## cellType Type

`object` ([Cell type](ega-4-definitions-cell-type.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# cellType Properties

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                 |
| :---------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-cell-type-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cellType/properties/termId") |

## termId



`termId`

*   is optional

*   Type: unknown ([Ontology constraints for this specific termId](ega-4-definitions-cell-type-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-cell-type-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cellType/properties/termId")

### termId Type

unknown ([Ontology constraints for this specific termId](ega-4-definitions-cell-type-properties-ontology-constraints-for-this-specific-termid.md))

### termId Examples

```json
"CL:0002092"
```

```json
"CL:0000127"
```

```json
"CL:0000128"
```
