# EGA policy metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json
```

A policy, also known as Data Access Agreement (DAA), is a contract made between Data User and Data Access Committee. The policy object is expected to contain metadata about such agreement, which should be drafted by the DAC and includes, but is not limited to, details of data use, publication embargoes and storage. Completion of a DAA by the applicant/s should form part of the application process to the DAC. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/submission/dac/documentation>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.policy.json](../../../schemas/EGA.policy.json "open original schema") |

## EGA policy metadata schema Type

`object` ([EGA policy metadata schema](ega-16.md))

# EGA policy metadata schema Properties

| Property                                       | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                     |
| :--------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object\_id](#object_id)                       | Merged   | Required | cannot be null | [EGA policy metadata schema](ega-16-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/object_id")                         |
| [schema\_descriptor](#schema_descriptor)       | `object` | Optional | cannot be null | [EGA policy metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/schema_descriptor")                |
| [object\_title](#object_title)                 | `string` | Required | cannot be null | [EGA policy metadata schema](ega-16-properties-title-of-the-policy.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/object_title")                    |
| [policy\_descriptor](#policy_descriptor)       | Merged   | Required | cannot be null | [EGA policy metadata schema](ega-16-properties-policy-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policy_descriptor")                 |
| [duo\_codes\_curies](#duo_codes_curies)        | `array`  | Optional | cannot be null | [EGA policy metadata schema](ega-16-properties-data-use-ontology-duo-codes-curies.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/duo_codes_curies") |
| [policy\_relationships](#policy_relationships) | `array`  | Optional | cannot be null | [EGA policy metadata schema](ega-16-properties-policy-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policy_relationships")           |
| [policy\_attributes](#policy_attributes)       | `array`  | Optional | cannot be null | [EGA policy metadata schema](ega-16-properties-policy-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policy_attributes")          |

## object\_id

Node containing the main identifiers of the object (e.g. alias, center\_name...), inherited from the common definitions. #! We extend the core object (object\_core\_id) by adding a pattern check based on this schema's nature: an policy (by using EGA-policy-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-16-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-16-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/object_id")

### object\_id Type

`object` ([Object's IDs block](ega-16-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that policy EGA ID (EGAP) is correct](ega-16-properties-objects-ids-block-allof-check-that-policy-ega-id-egap-is-correct.md "check type definition")

## schema\_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/schema_descriptor")

### schema\_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## object\_title

Free-form title of the policy. Can be used to call out policy records in searches or displays.

`object_title`

*   is required

*   Type: `string` ([Title of the policy](ega-16-properties-title-of-the-policy.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-16-properties-title-of-the-policy.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/object_title")

### object\_title Type

`string` ([Title of the policy](ega-16-properties-title-of-the-policy.md))

### object\_title Examples

```json
"EBI colon cancer policy"
```

## policy\_descriptor

Node containing the full description of the policy, whether it is hosted at some public resourced and referenced here; or directly written here.

`policy_descriptor`

*   is required

*   Type: `object` ([Policy descriptor](ega-16-properties-policy-descriptor.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-16-properties-policy-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policy_descriptor")

### policy\_descriptor Type

`object` ([Policy descriptor](ega-16-properties-policy-descriptor.md))

any of

*   [Either the policy reference is given](ega-16-properties-policy-descriptor-anyof-either-the-policy-reference-is-given.md "check type definition")

*   [Or the policy text is given](ega-16-properties-policy-descriptor-anyof-or-the-policy-text-is-given.md "check type definition")

## duo\_codes\_curies

Collection of Data Use Ontology (DUO) codes in Shorter Compact URI (CURIE) format. These allow to semantically tag datasets (bound by policies) with restriction about their usage, making them discoverable automatically based on the authorization level of users, or intended usage. See more info at <https://obofoundry.org/ontology/duo.html> and search for DUO codes at <https://www.ebi.ac.uk/ols/ontologies/duo>

`duo_codes_curies`

*   is optional

*   Type: `string[]` ([Data Use Ontology (DUO) code](ega-16-properties-data-use-ontology-duo-codes-curies-data-use-ontology-duo-code.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-16-properties-data-use-ontology-duo-codes-curies.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/duo_codes_curies")

### duo\_codes\_curies Type

`string[]` ([Data Use Ontology (DUO) code](ega-16-properties-data-use-ontology-duo-codes-curies-data-use-ontology-duo-code.md))

### duo\_codes\_curies Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## policy\_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. a policy being linked to a policy) the EGA.

`policy_relationships`

*   is optional

*   Type: an array of merged types ([Details](ega-16-properties-policy-relationships-items.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-16-properties-policy-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policy_relationships")

### policy\_relationships Type

an array of merged types ([Details](ega-16-properties-policy-relationships-items.md))

### policy\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## policy\_attributes

Custom attributes of a policy: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

`policy_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-16-properties-policy-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policy_attributes")

### policy\_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### policy\_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
