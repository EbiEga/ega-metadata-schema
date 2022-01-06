# README

## Top-level Schemas

*   [EGA ArrayAssay metadata schema](./ega.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its ArrayAssay metadata object") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json`

*   [EGA ArrayExperiment metadata schema](./ega-1.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its ArrayExperiment metadata object") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json`

*   [EGA common metadata definitions](./ega-2.md "Metadata schema used by the European Genome-phenome Archive (EGA) to store common definitions for other metadata objects") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json`

*   [EGA individual metadata schema](./ega-3.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its individual metadata object") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json`

*   [EGA sample metadata schema](./ega-4.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its sample metadata object") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json`

## Other Schemas

### Objects

*   [Array type of the ArrayExperiment \[EFO:0002696\]](./ega-1-properties-array-type-of-the-arrayexperiment-efo0002696.md "Type of array (not its purpose per se) providing a glimpse of the used technology") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_type`

*   [Assayed molecule in the ArrayExperiment \[EFO:0002772\]](./ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772.md "Type of molecule assayed") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/assayed_molecule`

*   [Check that the object_id's accession pattern and object_type match](./ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match.md "This object exists with the only purpose of being a reference as a pattern check of a given object_id and object_type") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check`

*   [Check: checksum checks based on its method](./ega-2-definitions-check-checksum-checks-based-on-its-method.md "This object exists with the only purpose of being a reference of pattern checks of the given checksum (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check`

*   [Check: filetype checks based on its filename](./ega-2-definitions-check-filetype-checks-based-on-its-filename.md "This object exists with the only purpose of being a reference of pattern checks of the given filetype of a file based on its corresponding filename (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check`

*   [Checksum method \[ChecksumAlgorithm\]](./ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md "Node containing both the ID (MD5 or SHA-256) and the CURIE (NCIT:C171276 or NCIT:C80226), describing the method which yields the checksum from a data input for the purpose of detecting errors") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method`

*   [Checksum method \[ChecksumAlgorithm\]](./ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md "Node containing both the ID (MD5 or SHA-256) and the CURIE (NCIT:C171276 or NCIT:C80226), describing the method which yields the checksum from a data input for the purpose of detecting errors") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method`

*   [Checksum method \[ChecksumAlgorithm\]](./ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md "Node containing both the ID (MD5 or SHA-256) and the CURIE (NCIT:C171276 or NCIT:C80226), describing the method which yields the checksum from a data input for the purpose of detecting errors") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method`

*   [Core identifiers of an object](./ega-2-definitions-core-identifiers-of-an-object.md "Base definition containing the properties (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id`

*   [Custom attribute of an object](./ega-2-definitions-custom-attribute-of-an-object.md "Reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute`

*   [EGA File object](./ega-2-definitions-ega-file-object.md "Object containing the base metadata attributes of a file object in the EGA") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object`

*   [EGA Protocols object](./ega-2-definitions-ega-protocols-object.md "Object containing the base metadata attributes of a Protocol object in the EGA") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object`

*   [EGA Relationships object](./ega-2-definitions-ega-relationships-object.md "Object containing the base metadata attributes of a relationship object in the EGA") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object`

*   [Experimental condition \[XCO:0000000\]](./ega-2-definitions-experimental-condition-xco0000000.md "A state of being, an external or environmental factor or a treatment observed or administered prior to or concurrent with an investigative procedure such as an assessment of a morphological or physiological state or property in a single individual or sample or in a group of individuals or samples, especially a state, factor or treatment which has the potential to influence the outcome of such an assessment") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor`

*   [Experimental design of the ArrayExperiment \[EFO:0001426\]](./ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426.md "Experimental factor describing the method of investigating particular types of research questions or solving particular types of problems") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/experimental_design`

*   [Filetype \[NCIT:C172272\]](./ega-2-definitions-ega-file-object-properties-filetype-ncitc172272.md "The nature of the content stored in an electronic file") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype`

*   [Filetype \[NCIT:C172272\]](./ega-2-definitions-ega-file-object-properties-filetype-ncitc172272.md "The nature of the content stored in an electronic file") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype`

*   [Filetype \[NCIT:C172272\]](./ega-2-definitions-ega-file-object-properties-filetype-ncitc172272.md "The nature of the content stored in an electronic file") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype`

*   [Microarray technology of the ArrayExperiment \[EFO:0002698\]](./ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698.md "Microarray technology applicable for the ArrayExperiment") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/technology`

*   [Minimal public attributes describing a sample](./ega-4-properties-minimal-public-attributes-describing-a-sample.md "Among all fields describing a sample, some may contain identifiable metadata and thus be private") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/minimal_public_attributes`

*   [Minimal public attributes describing an individual](./ega-3-properties-minimal-public-attributes-describing-an-individual.md "Among all attributes describing an individual, some may contain identifiable metadata and thus must be private") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes`

*   [Object of external accession of the object](./ega-2-definitions-object-of-external-accession-of-the-object.md "External accession node containing the object accession (i") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession`

*   [Object's IDs block](./ega-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/object_id`

*   [Object's IDs block](./ega-2-definitions-repeatable-sample-label-node-properties-objects-ids-block.md) – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id`

*   [Object's IDs block](./ega-1-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/object_id`

*   [Object's IDs block](./ega-2-definitions-repeatable-sample-label-node-properties-objects-ids-block.md) – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id`

*   [Object's IDs block](./ega-3-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/object_id`

*   [Object's IDs block](./ega-4-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_id`

*   [Organism \[OBI:0100026\] descriptor block](./ega-2-definitions-organism-obi0100026-descriptor-block.md "This node describes the material entity the sample consists in") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor`

*   [Relationship's object (either source or target)](./ega-2-definitions-relationships-object-either-source-or-target.md "Node containing metadata (identifiers and the type of reference) of one of the ends of the relationship, whether it is the source or the target of the relationship") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end`

*   [Relationship's object's IDs block](./ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id`

*   [Relationship's object's IDs block](./ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id`

*   [Relationship's object's IDs block](./ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id`

*   [Relationship's object's IDs block](./ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id`

*   [Relationship's object's IDs block](./ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id`

*   [Relationship's object's IDs block](./ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id`

*   [Relationship's object's IDs block](./ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id`

*   [Relationship's object's IDs block](./ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id`

*   [Relationship's object's IDs block](./ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id`

*   [Relationship's object's IDs block](./ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id`

*   [Relationship's object's IDs block](./ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id`

*   [Repeatable Sample-label node](./ega-2-definitions-repeatable-sample-label-node.md "The base node of a label-sample association") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association`

*   [Repeatable array_label node](./ega-2-definitions-repeatable-array_label-node.md "Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label`

*   [Sample group descriptor](./ega-4-properties-sample-group-descriptor.md "Node describing whether the sample object is: (1) a single physical sample (a single blood sample), collected individually through its corresponding protocol; or (2) corresponds to a set of samples that, after being individually collected, was grouped together (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping`

*   [Schema descriptor](./ega-2-definitions-schema-descriptor.md "This node is intended to be used to describe the schemas and standards that a JSON document was based on") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor`

*   [Source of the relationship](./ega-2-definitions-ega-relationships-object-properties-source-of-the-relationship.md "Object reference of the relationship’s source") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source`

*   [Source of the relationship](./ega-2-definitions-ega-relationships-object-properties-source-of-the-relationship.md "Object reference of the relationship’s source") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source`

*   [Source of the relationship](./ega-2-definitions-ega-relationships-object-properties-source-of-the-relationship.md "Object reference of the relationship’s source") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source`

*   [Source of the relationship](./ega-2-definitions-ega-relationships-object-properties-source-of-the-relationship.md "Object reference of the relationship’s source") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source`

*   [Source of the relationship](./ega-2-definitions-ega-relationships-object-properties-source-of-the-relationship.md "Object reference of the relationship’s source") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source`

*   [Target of the relationship](./ega-2-definitions-ega-relationships-object-properties-target-of-the-relationship.md "Object reference of the relationship’s target") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target`

*   [Target of the relationship](./ega-2-definitions-ega-relationships-object-properties-target-of-the-relationship.md "Object reference of the relationship’s target") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target`

*   [Target of the relationship](./ega-2-definitions-ega-relationships-object-properties-target-of-the-relationship.md "Object reference of the relationship’s target") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target`

*   [Target of the relationship](./ega-2-definitions-ega-relationships-object-properties-target-of-the-relationship.md "Object reference of the relationship’s target") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target`

*   [Target of the relationship](./ega-2-definitions-ega-relationships-object-properties-target-of-the-relationship.md "Object reference of the relationship’s target") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target`

*   [Type of the relationship](./ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship.md "The Type of the relationship, containing both its ID (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type`

*   [Type of the relationship](./ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship.md "The Type of the relationship, containing both its ID (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type`

*   [Type of the relationship](./ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship.md "The Type of the relationship, containing both its ID (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type`

*   [Type of the relationship](./ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship.md "The Type of the relationship, containing both its ID (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type`

*   [Type of the relationship](./ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship.md "The Type of the relationship, containing both its ID (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type`

### Arrays

*   [Array Design Format (ADF) \[NCIT:C172213\] file block](./ega-1-properties-array-design-format-adf-ncitc172213-file-block.md "The array design format (ADF) \[NCIT:C172213] is the unique set of probes (with their coordinates) found on the microarray chip") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/adf_files`

*   [Array label of the ArrayExperiment \[EFO:0000562\]](./ega-1-properties-array-label-of-the-arrayexperiment-efo0000562.md "Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_label`

*   [Array of Sample-label pairs of the ArrayAssay](./ega-properties-array-of-sample-label-pairs-of-the-arrayassay.md "Sample-Label pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/sample_labels`

*   [ArrayAssay custom attributes](./ega-properties-arrayassay-custom-attributes.md "Custom attributes of an ArrayAssay: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_attributes`

*   [ArrayAssay relationships](./ega-properties-arrayassay-relationships.md "Comprises metadata (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_relationships`

*   [ArrayExperiment custom attributes](./ega-1-properties-arrayexperiment-custom-attributes.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_experiment_attributes`

*   [ArrayExperiment relationships](./ega-1-properties-arrayexperiment-relationships.md "Comprises metadata (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_experiment_relationships`

*   [Assay files object from an ArrayAssay](./ega-properties-assay-files-object-from-an-arrayassay.md "This array object contains the specific files derived from performing an hybridization of the assayed molecule to a physical array") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/assay_files`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [External accessions array](./ega-2-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions`

*   [Individual custom attributes](./ega-3-properties-individual-custom-attributes.md "Custom attributes of an individual: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/individual_attributes`

*   [Individual relationships](./ega-3-properties-individual-relationships.md "Comprises metadata (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/individual_relationships`

*   [Protocols related to an ArrayExperiment](./ega-1-properties-protocols-related-to-an-arrayexperiment.md "Comprises metadata (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_experiment_protocols`

*   [Sample custom attributes](./ega-4-properties-sample-custom-attributes.md "Custom attributes of a sample: reusable attributes to encode tag-value pairs (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_attributes`

*   [Sample relationships](./ega-4-properties-sample-relationships.md "Comprises metadata (e") – `https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_relationships`

## Version Note

The schemas linked above follow the JSON Schema Spec version: `https://json-schema.org/draft/2019-09/schema`
