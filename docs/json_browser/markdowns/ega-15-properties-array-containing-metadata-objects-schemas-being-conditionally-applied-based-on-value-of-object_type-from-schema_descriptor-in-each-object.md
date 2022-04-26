# Schemas being conditionally applied based on value of 'object\_type' from 'schema\_descriptor' in each object. Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.object-set.json#/properties/object_array/items
```

Based on the value found within 'object\_type' (i.e. if it matches the 'enum' of each type), the corresponding schema (defined within '$ref') is evaluated.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.object-set.json\*](../../../schemas/EGA.object-set.json "open original schema") |

## items Type

merged type ([Schemas being conditionally applied based on value of 'object\_type' from 'schema\_descriptor' in each object.](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object.md))

any of

*   one (and only one) of

    *   [If the assay technology is a sequencer, the experiment type has to match](ega-9-oneof-if-the-assay-technology-is-a-sequencer-the-experiment-type-has-to-match.md "check type definition")

    *   [If the assay technology is an array, the experiment type has to match](ega-9-oneof-if-the-assay-technology-is-an-array-the-experiment-type-has-to-match.md "check type definition")

*   [EGA study metadata schema](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object-anyof-ega-study-metadata-schema.md "check type definition")

*   [EGA sample metadata schema](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object-anyof-ega-sample-metadata-schema.md "check type definition")

*   [EGA individual metadata schema](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object-anyof-ega-individual-metadata-schema.md "check type definition")

*   [EGA submission metadata schema](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object-anyof-ega-submission-metadata-schema.md "check type definition")

*   [EGA dataset metadata schema](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object-anyof-ega-dataset-metadata-schema.md "check type definition")

*   [EGA analysis metadata schema](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object-anyof-ega-analysis-metadata-schema.md "check type definition")

*   [EGA policy metadata schema](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object-anyof-ega-policy-metadata-schema.md "check type definition")

*   [EGA DAC metadata schema](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object-anyof-ega-dac-metadata-schema.md "check type definition")

*   all of

    *   [If the files are aligned reads, the reference alignment details are expected](ega-11-allof-if-the-files-are-aligned-reads-the-reference-alignment-details-are-expected.md "check type definition")

    *   [Allowed filetypes for a sequencing assay](ega-11-allof-allowed-filetypes-for-a-sequencing-assay.md "check type definition")

    *   [Allowed filetypes for an array assay](ega-11-allof-allowed-filetypes-for-an-array-assay.md "check type definition")
