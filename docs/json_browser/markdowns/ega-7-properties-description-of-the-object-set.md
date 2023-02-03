# Description of the object-set Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/objectDescription
```

More extensive free-form description of the object-set. Used to provide context on why the items (i.e. individual objects) of the array are grouped together.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.object-set.json\*](../../../schemas/EGA.object-set.json "open original schema") |

## objectDescription Type

`string` ([Description of the object-set](ega-7-properties-description-of-the-object-set.md))

## objectDescription Examples

```json
"This object-set corresponds to a whole example of a Single Cell Sequencing submission, being grouped together and submitted together."
```

```json
"When submitting the previous object set, 4 samples were wrong and need to be re-submitted, and that's the purpose of this object-set."
```
