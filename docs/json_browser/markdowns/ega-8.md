# EGA policy metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json
```

A policy, also known as Data Access Agreement (DAA), is a contract made between Data User and Data Access Committee. The policy object is expected to contain metadata about such agreement, which should be drafted by the DAC and includes, but is not limited to, details of data use, publication embargoes and storage. Completion of a DAA by the applicant/s should form part of the application process to the DAC. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/submission/dac/documentation>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.policy.json](../../../schemas/EGA.policy.json "open original schema") |

## EGA policy metadata schema Type

`object` ([EGA policy metadata schema](ega-8.md))

# EGA policy metadata schema Properties

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                          |
| :------------------------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)                       | Merged   | Required | cannot be null | [EGA policy metadata schema](ega-8-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/objectId")                |
| [schemaDescriptor](#schemadescriptor)       | `object` | Optional | cannot be null | [EGA policy metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/schemaDescriptor")       |
| [objectTitle](#objecttitle)                 | `string` | Required | cannot be null | [EGA policy metadata schema](ega-8-properties-title-of-the-policy.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/objectTitle")           |
| [policyDescriptor](#policydescriptor)       | Merged   | Required | cannot be null | [EGA policy metadata schema](ega-8-properties-policy-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyDescriptor")        |
| [duoCodes](#duocodes)                       | `array`  | Optional | cannot be null | [EGA policy metadata schema](ega-8-properties-data-use-ontology-duo-codes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/duoCodes")      |
| [policyRelationships](#policyrelationships) | `array`  | Optional | cannot be null | [EGA policy metadata schema](ega-8-properties-policy-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyRelationships")  |
| [policyAttributes](#policyattributes)       | `array`  | Optional | cannot be null | [EGA policy metadata schema](ega-8-properties-policy-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyAttributes") |

## objectId

Node containing the main identifiers of the object (e.g. alias, centerName...), inherited from the common definitions. #! We extend the core object (objectCoreId) by adding a pattern check based on this schema's nature: an policy (by using EGAPolicyIdPattern)

`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-8-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-8-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-8-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that policy EGA ID (EGAP) is correct](ega-8-properties-objects-ids-block-allof-check-that-policy-ega-id-egap-is-correct.md "check type definition")

## schemaDescriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schemaDescriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/schemaDescriptor")

### schemaDescriptor Type

`object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

## objectTitle

Free-form title of the policy. Can be used to call out policy records in searches or displays.

`objectTitle`

*   is required

*   Type: `string` ([Title of the policy](ega-8-properties-title-of-the-policy.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-8-properties-title-of-the-policy.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/objectTitle")

### objectTitle Type

`string` ([Title of the policy](ega-8-properties-title-of-the-policy.md))

### objectTitle Examples

```json
"EBI colon cancer policy"
```

## policyDescriptor

Node containing the full description of the policy, whether it is hosted at some public resourced and referenced here; or directly written here.

`policyDescriptor`

*   is required

*   Type: `object` ([Policy descriptor](ega-8-properties-policy-descriptor.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-8-properties-policy-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyDescriptor")

### policyDescriptor Type

`object` ([Policy descriptor](ega-8-properties-policy-descriptor.md))

any of

*   [Either the policy reference is given](ega-8-properties-policy-descriptor-anyof-either-the-policy-reference-is-given.md "check type definition")

*   [Or the policy text is given](ega-8-properties-policy-descriptor-anyof-or-the-policy-text-is-given.md "check type definition")

## duoCodes

Collection of Data Use Ontology (DUO) codes. These allow to semantically tag datasets (bound by policies) with restriction about their usage, improving their discoverability based on the authorization level of users, or intended usage. See more info at <https://obofoundry.org/ontology/duo.html> and search for DUO codes at <https://www.ebi.ac.uk/ols/ontologies/duo>

`duoCodes`

*   is optional

*   Type: `object[]` ([Data Use Ontology (DUO)](ega-8-properties-data-use-ontology-duo-codes-data-use-ontology-duo.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-8-properties-data-use-ontology-duo-codes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/duoCodes")

### duoCodes Type

`object[]` ([Data Use Ontology (DUO)](ega-8-properties-data-use-ontology-duo-codes-data-use-ontology-duo.md))

### duoCodes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## policyRelationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. a policy being linked to a policy) the EGA.

`policyRelationships`

*   is optional

*   Type: an array of merged types ([Details](ega-8-properties-policy-relationships-items.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-8-properties-policy-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyRelationships")

### policyRelationships Type

an array of merged types ([Details](ega-8-properties-policy-relationships-items.md))

### policyRelationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## policyAttributes

Custom attributes of a policy: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

`policyAttributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-8-properties-policy-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyAttributes")

### policyAttributes Type

`object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

### policyAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
