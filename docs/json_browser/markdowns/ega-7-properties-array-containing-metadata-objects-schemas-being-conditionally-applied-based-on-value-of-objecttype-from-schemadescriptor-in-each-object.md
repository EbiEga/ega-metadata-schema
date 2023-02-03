# Schemas being conditionally applied based on value of 'objectType' from 'schemaDescriptor' in each object. Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/objectArray/items
```

Based on the value found within 'objectType' (i.e. if it matches the 'enum' of each type), the corresponding schema (defined within '$ref') is evaluated.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.object-set.json\*](../../../schemas/EGA.object-set.json "open original schema") |

## items Type

merged type ([Schemas being conditionally applied based on value of 'objectType' from 'schemaDescriptor' in each object.](ega-7-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-objecttype-from-schemadescriptor-in-each-object.md))

any of

*   one (and only one) of

    *   [If the assay technology is a sequencer, the experiment type has to match](ega-1-oneof-if-the-assay-technology-is-a-sequencer-the-experiment-type-has-to-match.md "check type definition")

    *   [If the assay technology is an array, the experiment type has to match](ega-1-oneof-if-the-assay-technology-is-an-array-the-experiment-type-has-to-match.md "check type definition")

*   [EGA study metadata schema](ega-11.md "check type definition")

*   [EGA sample metadata schema](ega-10.md "check type definition")

*   [EGA individual metadata schema](ega-6.md "check type definition")

*   [EGA submission metadata schema](ega-12.md "check type definition")

*   [EGA dataset metadata schema](ega-5.md "check type definition")

*   [EGA analysis metadata schema](ega-2.md "check type definition")

*   [EGA policy metadata schema](ega-8.md "check type definition")

*   [EGA DAC metadata schema](ega.md "check type definition")

*   all of

    *   [If the files are aligned reads, the reference alignment details are expected](ega-3-allof-if-the-files-are-aligned-reads-the-reference-alignment-details-are-expected.md "check type definition")

    *   [Allowed filetypes for a sequencing assay](ega-3-allof-allowed-filetypes-for-a-sequencing-assay.md "check type definition")

    *   [Allowed filetypes for an array assay](ega-3-allof-allowed-filetypes-for-an-array-assay.md "check type definition")

*   [EGA protocol metadata schema](ega-9.md "check type definition")
