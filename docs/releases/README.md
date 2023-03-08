# Release Workflow for Ega Metadata Schemas
In this document you will find the workflow for creating releases of the Ega Metadata Schemas GitHub project. It provides a step-by-step diagram to help illustrate the steps involved.

## Workflow Diagram
![Release Workflow Diagram](images/Release_workflow_diagram.svg)


The above diagram illustrates the process for creating a new release of the EGA Metadata Schemas project.

![Release GitHub Diagram](images/Release_github_diagram.svg)

The above diagram represents a simplified example of how the branches are managed in GitHub for a release to be done.

## Version Manifest
To keep track of which JSON schema versions are included in each release version of the Ega Metadata Schemas project, a manifest ([``version_manifest.json``](./version_manifest.json)) is maintained in this same directory. This file lists the schema versions included in each release, along with other relevant metadata of the releases.

To ensure that the "version_manifest.json" file is properly formatted, a JSON Schema called [``VM_schema.json``](./VM_schema.json) is included in the same directory. This schema can be used to validate the "version_manifest.json" file before each release.

We hope that this document and the accompanying diagram help to clarify the release workflow for the EGA Metadata Schemas project. If you have any questions or concerns, please don't hesitate to reach out to us.

## Modification of static pointers
At some steps in the release process, there is a need to **modify the static schema and document pointers**. These pointers are basically a URL-resolvable ID of the schemas. It is thanks to these IDs that, during the validation process, we know:
- How to resolve references between schemas. For example, how ``"$ref": "./EGA.common-definitions.json#/definitions/objectCoreId"`` in [``EGA.assay.json``](../../schemas/EGA.assay.json) must be resolved to ``"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId"``, following ``EGA.assay.json``'s ``$id`` property.
- What schema to apply to what document. For example, knowing that for [``assay_valid-1_array.json``](../../examples/json_validation_tests/assay_valid-1_array.json) we need to apply the schema ``https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json`` and not other of the set.

Now, these URIs normally point towards the ``main`` branch, being always the updated version of the JSON schemas, whatever the latest release is. But, if what we want to do is test another branch or release tag, these URLs need to change, both in the JSON schemas and documents. Same applies if what we need to modify is the repository ownership (e.g. ``M-casado`` instead of ``EbiEga``). 

For this reason, we created the script [``modify_static_pointers.py``](../../.github/scripts/modify_static_pointers.py) so that these changes can be easily made with one single command.
```` bash
# To modify the branch name of the JSON schemas and documents, replacing "main" with "v1.0.0"
python3 ../../.github/scripts/modify_static_pointers.py --input_directory "../../examples/json_validation_tests/" --new_str "v1.0.0"
python3 ../../.github/scripts/modify_static_pointers.py --input_directory "../../schemas/" --new_str "v1.0.0"

# To modify the account hosting the repo, in case it was forked, replacing "EbiEga" by "M-casado"
python3 ../../.github/scripts/modify_static_pointers.py --input_directory "../../examples/json_validation_tests/" --new_str "M-casado" --previous_str "raw.githubusercontent.com"
python3 ../../.github/scripts/modify_static_pointers.py --input_directory "../../schemas/" --new_str "M-casado" --previous_str "raw.githubusercontent.com"
````
