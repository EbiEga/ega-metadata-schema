# README

## Top-level Schemas

*   [EGA DAC metadata schema](./ega.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Data Access Committee (DAC) metadata object") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json`

*   [EGA Experiment metadata schema](./ega-1.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its experiment metadata object") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json`

*   [EGA analysis metadata schema](./ega-2.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its analysis metadata object") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json`

*   [EGA assay metadata schema](./ega-3.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its assay metadata object") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json`

*   [EGA common metadata definitions](./ega-4.md "Metadata schema used by the European Genome-phenome Archive (EGA) to store common definitions for other metadata objects") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json`

*   [EGA dataset metadata schema](./ega-5.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Dataset metadata object") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json`

*   [EGA individual metadata schema](./ega-6.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its individual metadata object") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json`

*   [EGA object-set metadata schema](./ega-7.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate an object-set") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json`

*   [EGA policy metadata schema](./ega-8.md "A policy, also known as Data Access Agreement (DAA), is a contract made between Data User and Data Access Committee") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json`

*   [EGA protocol metadata schema](./ega-9.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its protocol metadata object") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json`

*   [EGA sample metadata schema](./ega-10.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its sample metadata object") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json`

*   [EGA study metadata schema](./ega-11.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Study metadata object") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json`

*   [EGA submission metadata schema](./ega-12.md "Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Submission (also known as submission project) metadata object") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json`

## Other Schemas

### Objects

*   [Alternate gene identifier item](./ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers-alternate-gene-identifier-item.md "One of the possible alternate gene identifiers for the designated gene") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneIdentifiers/items`

*   [Analysis type specifications](./ega-2-properties-analysis-type-specifications.md "Node containing different sets of fields that depend on the specific analysis type") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisTypeSpecifications`

*   [Array label identifier](./ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier.md "The chosen term (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelIdentifier`

*   [Assay technology](./ega-4-definitions-assay-technology.md "Metadata of the assay instrument (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayTechnologyDescriptor`

*   [Assay type specifications](./ega-3-properties-assay-type-specifications.md "Node containing different sets of fields that depend on the instrument used for the assay: either array assays (those in which an array instrument \[EFO:0002698] was used) or sequencing assays (those in which a sequencing instrument \[EFO:0003739] was used)") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications`

*   [Assayed biological macromolecule](./ega-1-properties-assayed-biological-macromolecule.md "Node containing information about the assayed biological macromolecule: the material entity (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayedBiologicalMacromolecule`

*   [Basecall](./ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall.md) – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls/items`

*   [Cell type](./ega-4-definitions-cell-type.md "Property to describe a cell type: a distinct morphological or functional form of cell") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cellType`

*   [Cell type](./ega-10-properties-array-of-cell-types-cell-type.md "One of the cell types that can be found in your sample or from which the genetic content was derived") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes/items`

*   [Check that the objectId's accession pattern and objectType match](./ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match.md "This object exists with the only purpose of being a reference as a pattern check of a given objectId and objectType") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck`

*   [Check: allowed filetypes for an assay](./ega-4-definitions-check-allowed-filetypes-for-an-assay.md "This object exists with the only purpose of being a reference list of the allowed filetypes of an assay (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayFiletypes`

*   [Check: checksum checks based on its method](./ega-4-definitions-check-checksum-checks-based-on-its-method.md "This object exists with the only purpose of being a reference of pattern checks of the given checksum (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck`

*   [Check: filetype checks based on its filename](./ega-4-definitions-check-filetype-checks-based-on-its-filename.md "This object exists with the only purpose of being a reference of pattern checks of the given filetype of a file based on its corresponding filename (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filenameFiletypePatternCheck`

*   [Collaborator](./ega-12-properties-submission-collaborator-details-collaborator.md "Collaborator item comprising both the collaborator's contact details and rights") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators/items`

*   [Contact details](./ega-4-definitions-contact-details.md "An object to contain the required metadata to identify and reach an individual or institution") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails`

*   [Core identifiers of an object](./ega-4-definitions-core-identifiers-of-an-object.md "Base definition containing the properties (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId`

*   [Custom attribute of an object](./ega-4-definitions-custom-attribute-of-an-object.md "Reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/customAttribute`

*   [DAC contacts' details](./ega-properties-dac-contacts-details.md "Object containing the main contact's and optional additional contact's details") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacContacts`

*   [Data Use Ontology (DUO)](./ega-8-properties-data-use-ontology-duo-codes-data-use-ontology-duo.md "Single Data Use Ontology (DUO) code") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/duoCodes/items`

*   [Disease](./ega-4-definitions-disease.md "Property to describe a disease (i") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/disease`

*   [Disease item](./ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases-disease-item.md "One individual disease of the array") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases/items`

*   [EGA File object](./ega-4-definitions-ega-file-object.md "Object containing the base metadata attributes of a file object in the EGA") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject`

*   [EGA Relationships object](./ega-4-definitions-ega-relationships-object.md "Object containing the base metadata attributes of a relationship object in the EGA") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject`

*   [Expected basecall table](./ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table.md "A set of choices of expected basecalls for a current read") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable`

*   [Experiment type specifications](./ega-1-properties-experiment-type-specifications.md "Node containing additional attributes to describe the experiment, either array experiments (those in which an array instrument \[EFO:0002698] was used) or sequencing experiments (those in which a sequencing instrument \[EFO:0003739] was used)") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications`

*   [File content item](./ega-4-definitions-ega-file-object-properties-file-content-array-file-content-item.md "Item describing the type of data a file contains or represents") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent/items`

*   [Gene descriptor](./ega-4-definitions-gene-descriptor.md "Node to uniquely identify a gene \[SO:0000704]: a region (or regions) that includes all of the sequence elements necessary to encode a functional transcript") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor`

*   [Gene identifier](./ega-4-definitions-gene-descriptor-properties-gene-identifier.md "Property uniquely identifying a gene") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneIdentifier`

*   [Genomic sequence descriptor](./ega-4-definitions-genomic-sequence-descriptor.md "Node used to describe with sufficient detail a genomic sequence (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor`

*   [Identifier of the external accession](./ega-4-definitions-object-external-accession-properties-identifier-of-the-external-accession.md "Unique identifier of an external record") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionIdentifier`

*   [Individual's age at sample collection](./ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection.md "Property describing the individual's age at sample collection") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection`

*   [Individual's age range at sample collection](./ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-properties-individuals-age-range-at-sample-collection.md "Age range of the individual when the sample was collected") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection/properties/ageRange`

*   [Locus context item](./ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md "Node providing the context of the locus: its sequence, coordinates, encompassed genes") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor/items`

*   [Locus identifier](./ega-4-definitions-locus-identifier.md "Node to unambiguously identify loci \[OGI:0000022]: the unique chromosomal location defining the position of an individual gene or DNA sequence") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier`

*   [Material anatomical entity](./ega-4-definitions-material-anatomical-entity.md "The part of organism's anatomy or substance arising from an organism from which the biomaterial was derived, exlucing cell types") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/materialAnatomicalEntity`

*   [Minimal public attributes describing an individual](./ega-6-properties-minimal-public-attributes-describing-an-individual.md "Among all attributes describing an individual, some may contain identifiable metadata and thus must be private") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes`

*   [NCBI Assembly](./ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly.md "Node defining an Assembly (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssembly`

*   [NCBI Taxon of the organism](./ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism.md "Taxonomic classification of the organism (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/organismTaxon`

*   [NCBI assembly unit](./ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit.md "NCBI's identifier of the assembly unit") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssemblyUnit`

*   [NCBI's Assembly descriptor](./ega-4-definitions-ncbis-assembly-descriptor.md "Node describing a sequence assembly referenced in NCBI's Assembly database") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor`

*   [Object External accession](./ega-4-definitions-object-external-accession.md "External accession property defining a reference to an external record in another resource") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession`

*   [Object's IDs block](./ega-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/objectId`

*   [Object's IDs block](./ega-2-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectId`

*   [Object's IDs block](./ega-3-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/objectId`

*   [Object's IDs block](./ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md) – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/objectId`

*   [Object's IDs block](./ega-5-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/objectId`

*   [Object's IDs block](./ega-1-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/objectId`

*   [Object's IDs block](./ega-6-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/objectId`

*   [Object's IDs block](./ega-11-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/objectId`

*   [Object's IDs block](./ega-10-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/objectId`

*   [Object's IDs block](./ega-12-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/objectId`

*   [Object's IDs block](./ega-8-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/objectId`

*   [Object's IDs block](./ega-9-properties-objects-ids-block.md "Node containing the main identifiers of the object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/objectId`

*   [Ontology term](./ega-4-definitions-ontology-term.md "This property represents an ontology term (a") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm`

*   [Organism \[OBI:0100026\] descriptor block](./ega-4-definitions-organism-obi0100026-descriptor-block.md "This property describes the material entity the sample consists in") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor`

*   [Phenotypic abnormality](./ega-4-definitions-phenotypic-abnormality.md "Property to describe any abnormal (i") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypicAbnormality`

*   [Phenotypic abnormality item](./ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-phenotypic-abnormalities-phenotypic-abnormality-item.md "One individual Phenotypic abnormality of the array") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/phenotypicAbnormalities/items`

*   [Policy descriptor](./ega-8-properties-policy-descriptor.md "Node containing the full description of the policy, whether it is hosted at some public resourced and referenced here; or directly written here") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyDescriptor`

*   [Protocol type descriptor](./ega-9-properties-protocol-type-descriptor.md "Node to contain the information about the type and subtype of the protocol") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor`

*   [Read spec](./ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec.md) – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items`

*   [Related gene identifier item](./ega-4-definitions-gene-descriptor-properties-related-not-equivalent-gene-identifiers-related-gene-identifier-item.md) – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/relatedGeneIdentifiers/items`

*   [Relationship source: DAC](./ega-4-definitions-relationship-source-dac.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceDAC`

*   [Relationship source: Policy](./ega-4-definitions-relationship-source-policy.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourcePolicy`

*   [Relationship source: analysis](./ega-4-definitions-relationship-source-analysis.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceAnalysis`

*   [Relationship source: assay](./ega-4-definitions-relationship-source-assay.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceAssay`

*   [Relationship source: dataset](./ega-4-definitions-relationship-source-dataset.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceDataset`

*   [Relationship source: experiment](./ega-4-definitions-relationship-source-experiment.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExperiment`

*   [Relationship source: externalAccession](./ega-4-definitions-relationship-source-externalaccession.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExternalAccession`

*   [Relationship source: externalURL](./ega-4-definitions-relationship-source-externalurl.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExternalURL`

*   [Relationship source: individual](./ega-4-definitions-relationship-source-individual.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceIndividual`

*   [Relationship source: protocol](./ega-4-definitions-relationship-source-protocol.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceProtocol`

*   [Relationship source: sample](./ega-4-definitions-relationship-source-sample.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceSample`

*   [Relationship source: study](./ega-4-definitions-relationship-source-study.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceStudy`

*   [Relationship source: submission](./ega-4-definitions-relationship-source-submission.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceSubmission`

*   [Relationship target: DAC](./ega-4-definitions-relationship-target-dac.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetDAC`

*   [Relationship target: Policy](./ega-4-definitions-relationship-target-policy.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetPolicy`

*   [Relationship target: analysis](./ega-4-definitions-relationship-target-analysis.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetAnalysis`

*   [Relationship target: assay](./ega-4-definitions-relationship-target-assay.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetAssay`

*   [Relationship target: dataset](./ega-4-definitions-relationship-target-dataset.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetDataset`

*   [Relationship target: experiment](./ega-4-definitions-relationship-target-experiment.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExperiment`

*   [Relationship target: externalAccession](./ega-4-definitions-relationship-target-externalaccession.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExternalAccession`

*   [Relationship target: externalURL](./ega-4-definitions-relationship-target-externalurl.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExternalURL`

*   [Relationship target: individual](./ega-4-definitions-relationship-target-individual.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetIndividual`

*   [Relationship target: protocol](./ega-4-definitions-relationship-target-protocol.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetProtocol`

*   [Relationship target: sample](./ega-4-definitions-relationship-target-sample.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetSample`

*   [Relationship target: study](./ega-4-definitions-relationship-target-study.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetStudy`

*   [Relationship target: submission](./ega-4-definitions-relationship-target-submission.md "Node to be used as an object type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetSubmission`

*   [Relationship type: childOf](./ega-4-definitions-relationship-type-childof.md "Node to be used as a relationship type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeChildOf`

*   [Relationship type: developsFrom](./ega-4-definitions-relationship-type-developsfrom.md "Node to be used as a relationship type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeDevelopsFrom`

*   [Relationship type: familyRelationshipWith](./ega-4-definitions-relationship-type-familyrelationshipwith.md "Node to be used as a relationship type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeFamilyRelationshipWith`

*   [Relationship type: groupedWith](./ega-4-definitions-relationship-type-groupedwith.md "Node to be used as a relationship type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeGroupedWith`

*   [Relationship type: isAfter](./ega-4-definitions-relationship-type-isafter.md "Node to be used as a relationship type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeIsAfter`

*   [Relationship type: memberOf](./ega-4-definitions-relationship-type-memberof.md "Node to be used as a relationship type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeMemberOf`

*   [Relationship type: referencedBy](./ega-4-definitions-relationship-type-referencedby.md "Node to be used as a relationship type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeReferencedBy`

*   [Relationship type: sameAs](./ega-4-definitions-relationship-type-sameas.md "Node to be used as a relationship type for relationship contraints") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeSameAs`

*   [Relationship's object (either source or target)](./ega-4-definitions-relationships-object-either-source-or-target.md "Node containing metadata (identifiers and the type of reference) of one of the ends of the relationship, whether it is the source or the target of the relationship") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd`

*   [Relationship's object's IDs block](./ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "Node containing the main identifiers of the relationship's object (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd/properties/objectId`

*   [Relative order](./ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order.md "The read is located beginning at the offset or cycle relative to another read") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/relativeOrder`

*   [Repeatable Sample-label node](./ega-4-definitions-repeatable-sample-label-node.md "The base node of a label-sample association") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation`

*   [Repeatable arrayLabel node](./ega-4-definitions-repeatable-arraylabel-node.md "Chemical conjugated to nucleic acid/proteins to label them before microarray hybridisation") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel`

*   [Resource](./ega-12-properties-resources-ontologies-resource.md "Object defining one item of the array: an individual resource (i") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items`

*   [Sample collection descriptor](./ega-10-properties-sample-collection-descriptor.md "Node containing the provenance details (when and where) of the sample") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection`

*   [Sample condition](./ega-10-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md "One of the primary conditions under study (CUS)") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy`

*   [Sample group descriptor](./ega-10-properties-sample-group-descriptor.md "Node describing whether the sample object is: (1) a single physical sample (a single blood sample), collected individually through its corresponding protocol; or (2) corresponds to a set of samples that, after being individually collected, was grouped together (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping`

*   [Sample status item](./ega-10-properties-array-of-sample-statuses-sample-status-item.md "One individual sample status of the array") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items`

*   [Sampling site](./ega-10-properties-sample-collection-descriptor-properties-sampling-site.md "A site or entity from which a sample (i") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/samplingSite`

*   [Schema descriptor](./ega-4-definitions-schema-descriptor.md "This node is intended to be used to describe the schemas and standards that a JSON document was based on") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor`

*   [Sequence coordinates](./ega-4-definitions-sequence-coordinates.md "A position in a map (for example a genetic map), either a single position (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates`

*   [Sequence interval](./ega-4-definitions-sequence-coordinates-properties-sequence-interval.md "The location of a sequence feature in a genome, defined by its start (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates/properties/sequenceInterval`

*   [Sequence quality details](./ega-4-definitions-ega-file-object-properties-sequence-quality-details.md "Sequencing quality scores measure the probability that a base is called (i") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails`

*   [Source of the relationship](./ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md "Object reference of the relationship's source") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rSource`

*   [Specifications of a sequencing assay](./ega-3-properties-assay-type-specifications-properties-specifications-of-a-sequencing-assay.md "Node containing the set of fields specific to an assay of type 'sequencer' (i") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/sequencingAssaySpecifications`

*   [Specifications of a sequencing experiment](./ega-1-properties-experiment-type-specifications-properties-specifications-of-a-sequencing-experiment.md "Node containing the set of fields specific to an experiment of sequencing-type (i") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/sequencingExperiment`

*   [Specifications of an array assay](./ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay.md "Node containing the set of fields specific to an assay of type 'array' (i") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications`

*   [Specifications of an array experiment](./ega-1-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment.md "Node containing the set of fields specific to an experiment of array-type (i") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/arrayExperiment`

*   [Spot decode spec](./ega-4-definitions-spot-descriptor-spot-decode-spec.md) – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items`

*   [Subtype of the protocol](./ega-9-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md "Ontology term of the protocol subtype") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolSubtype`

*   [Target of the relationship](./ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md "Object reference of the relationship's target") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rTarget`

*   [Type of used assay](./ega-1-properties-type-of-used-assay.md "Node defining the type of assay applicable to the experiment") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayType`

### Arrays

*   [Additional DAC contacts' details](./ega-properties-dac-contacts-details-properties-additional-dac-contacts-details.md "An array compromising additional contact details to use when in need to reach the DAC yet the main contact is unresponsive or does not exist") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacContacts/properties/additionalContacts`

*   [Alternate gene identifiers](./ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers.md "Array of alternate identifiers for this gene") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneIdentifiers`

*   [Analysis custom attributes](./ega-2-properties-analysis-custom-attributes.md "Custom attributes of an analysis: reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisAttributes`

*   [Analysis relationships](./ega-2-properties-analysis-relationships.md "Comprises metadata (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisRelationships`

*   [Array Design Format (ADF) \[NCIT:C172213\] file block](./ega-1-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment-properties-array-design-format-adf-ncitc172213-file-block.md "The array design format (ADF) \[NCIT:C172213] is the unique set of probes (with their coordinates) found on the microarray chip") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/arrayExperiment/properties/adfFiles`

*   [Array containing metadata objects](./ega-7-properties-array-containing-metadata-objects.md "The array per se containing the list of metadata objects to be validated") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.object-set.json#/properties/objectArray`

*   [Array label of the experiment](./ega-1-properties-experiment-type-specifications-properties-specifications-of-an-array-experiment-properties-array-label-of-the-experiment.md "Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentTypeSpecifications/properties/arrayExperiment/properties/arrayLabels`

*   [Array of cell types](./ega-10-properties-array-of-cell-types.md "Array of cell types, in case the sample is composed of cells (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes`

*   [Array of diseases](./ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases.md) – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases`

*   [Array of phenotypic abnormalities](./ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-phenotypic-abnormalities.md) – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/phenotypicAbnormalities`

*   [Array of sample statuses](./ega-10-properties-array-of-sample-statuses.md "Array of statuses of the sample") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus`

*   [Array of sample types](./ega-10-properties-array-of-sample-types.md "Array of sample types: the material entity (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleTypes`

*   [Array of sampleLabel pairs of the array assay](./ega-3-properties-assay-type-specifications-properties-specifications-of-an-array-assay-properties-array-of-samplelabel-pairs-of-the-array-assay.md "Sample-Label pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications/properties/arrayAssaySpecifications/properties/arraySampleLabels`

*   [Assay custom attributes](./ega-3-properties-assay-custom-attributes.md "Custom attributes of an assay: reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayAttributes`

*   [Assay relationships](./ega-3-properties-assay-relationships.md "Comprises metadata (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayRelationships`

*   [Basecalls array](./ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array.md "Element's body contains a basecall, attribute provide description of this read meaning as well as matching rules") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls`

*   [DAC custom attributes](./ega-properties-dac-custom-attributes.md "Custom attributes of a DAC: reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacAttributes`

*   [DAC relationships](./ega-properties-dac-relationships.md "Comprises metadata (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacRelationships`

*   [Data Use Ontology (DUO) codes](./ega-8-properties-data-use-ontology-duo-codes.md "Collection of Data Use Ontology (DUO) codes") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/duoCodes`

*   [Data files produced from an assay](./ega-3-properties-data-files-produced-from-an-assay.md "This property contains the specific files (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayFiles`

*   [Dataset custom attributes](./ega-5-properties-dataset-custom-attributes.md "Custom attributes of a dataset: reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/datasetAttributes`

*   [Dataset relationships](./ega-5-properties-dataset-relationships.md "Comprises metadata (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/datasetRelationships`

*   [Experiment custom attributes](./ega-1-properties-experiment-custom-attributes.md "Custom attributes of an experiment: reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentAttributes`

*   [Experiment relationships](./ega-1-properties-experiment-relationships.md "Comprises metadata (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experimentRelationships`

*   [External accessions array](./ega-4-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "External accession node to reference objects in other archives (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/externalAccessions`

*   [File content array](./ega-4-definitions-ega-file-object-properties-file-content-array.md "Array of file content items") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent`

*   [Files of the analysis](./ega-2-properties-files-of-the-analysis.md "This property contains the files derived from performing any processing or analysis over raw data (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisFiles`

*   [Individual custom attributes](./ega-6-properties-individual-custom-attributes.md "Custom attributes of an individual: reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/individualAttributes`

*   [Individual relationships](./ega-6-properties-individual-relationships.md "Comprises metadata (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/individualRelationships`

*   [List of analysis types](./ega-2-properties-analysis-type-specifications-properties-list-of-analysis-types.md "Array of all analysis types applicable to this analysis") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisTypeSpecifications/properties/analysisTypes`

*   [Loci context array](./ega-4-definitions-locus-identifier-properties-loci-context-array.md "Array of locus context items") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor`

*   [Loci of the targeted genomic feature](./ega-2-properties-loci-of-the-targeted-genomic-feature.md "Array of items that unambiguously define the loci of targeted genomic features in the analysis") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/targetedLoci`

*   [Loci of the targeted genomic feature](./ega-1-properties-loci-of-the-targeted-genomic-feature.md "Array of items that unambiguously define the loci of targeted genomic features in the experiment") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/targetedLoci`

*   [Policy custom attributes](./ega-8-properties-policy-custom-attributes.md "Custom attributes of a policy: reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyAttributes`

*   [Policy relationships](./ega-8-properties-policy-relationships.md "Comprises metadata (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyRelationships`

*   [Protocol custom attributes](./ega-9-properties-protocol-custom-attributes.md "Custom attributes of a protocol: reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolAttributes`

*   [Protocol instrument array](./ega-9-properties-protocol-instrument-array.md "Array of instruments used in the protocol") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolInstruments`

*   [Protocol performers array](./ega-9-properties-protocol-performers-array.md "Array of performers' descriptions of those individuals, groups, or institutions that executed the protocol") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolPerformers`

*   [Protocol relationships](./ega-9-properties-protocol-relationships.md "Comprises metadata (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolRelationships`

*   [Protocol software array](./ega-9-properties-protocol-software-array.md "Array of software descriptions used in the protocol") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolSoftware`

*   [Read specs](./ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs.md) – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs`

*   [Reference assembly and sequence details](./ega-4-definitions-reference-assembly-and-sequence-details.md "Node containing the information of the reference assembly that was used to obtain the sequence alignment") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/referenceAlignmentDetails`

*   [Related (not equivalent) gene identifiers](./ega-4-definitions-gene-descriptor-properties-related-not-equivalent-gene-identifiers.md "Array of related identifiers (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/relatedGeneIdentifiers`

*   [Resources (ontologies)](./ega-12-properties-resources-ontologies.md "An array containing metadata of all the ontologies used in the submission") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources`

*   [Sample custom attributes](./ega-10-properties-sample-custom-attributes.md "Custom attributes of a sample: reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleAttributes`

*   [Sample relationships](./ega-10-properties-sample-relationships.md "Comprises metadata (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleRelationships`

*   [Spot descriptor](./ega-4-definitions-spot-descriptor.md "The 'spotDescriptor' specifies how to decode the individual reads of interest from the monolithic spot sequence") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor`

*   [Study custom attributes](./ega-11-properties-study-custom-attributes.md "Custom attributes of a study: reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyAttributes`

*   [Study relationships](./ega-11-properties-study-relationships.md "Comprises metadata (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyRelationships`

*   [Submission collaborator details](./ega-12-properties-submission-collaborator-details.md "Object containing optional collaborators of the submission project, who shall have different capabilities granted by the owner: 'read' or 'read and write' rights") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators`

*   [Submission custom attributes](./ega-12-properties-submission-custom-attributes.md "Custom attributes of a submission: reusable attributes to encode tag-value pairs (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/submissionAttributes`

*   [Submission relationships](./ega-12-properties-submission-relationships.md "Comprises metadata (e") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/submissionRelationships`

*   [Types of input data](./ega-2-properties-types-of-input-data.md "Types of input data the analysis uses to obtain the processed files") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/typesOfInputData`

*   [Types of output data](./ega-2-properties-types-of-output-data.md "Types of output data the analysis uses to obtain the processed files") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/typesOfOutputData`

*   [Types of output data](./ega-1-properties-types-of-output-data.md "Types of data the experiment produces") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/typesOfOutputData`

*   [studyDesigns array](./ega-11-properties-studydesigns-array.md "List of study designs (a") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyDesigns`

*   [studyTypes array](./ega-11-properties-studytypes-array.md "List of study types") – `https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyTypes`

## Version Note

The schemas linked above follow the JSON Schema Spec version: `https://json-schema.org/draft/2019-09/schema`
