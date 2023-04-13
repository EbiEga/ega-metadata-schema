# Release Workflow for Ega Metadata Schemas
In this document you will find the workflow for creating releases of the EGA Metadata Schemas project. It provides a step-by-step diagram to help illustrate the steps involved.

## Workflow Diagram
![Release Workflow Diagram](images/Release_workflow_diagram.svg)


The above diagram illustrates the process for creating a new release of the EGA Metadata Schemas project.

![Release GitHub Diagram](images/Release_github_diagram.svg)

The above diagram represents a simplified example of how the branches are managed in GitHub for a release to be done.
In case it is needed to modify any of the above schemas, please go to the [editor's URL](https://app.diagrams.net/?libs=general;flowchart#G1bWcDQRYVkDVWP7ArPkxlZUo5pSZzHfZF). Only EGA members have access to it.

## Version Manifest
### Introduction
To keep track of which JSON schema versions are included in each release version of the EGA Metadata Schemas project, a manifest ([``version_manifest.json``](./version_manifest.json)) is maintained in this same directory. This file lists the schema versions included in the last release, the schema versions that changed in each release, and any other relevant metadata of the releases. 

Each release contains at their version manifest file the schema versions of all objects. Whenever a new release is made and this file is edited, the previous releases are summarized, only containing the schema versions that were modified at their specific release, instead of all. This was designed for an easier reading without any information loss.

To ensure that the "version_manifest.json" file is properly formatted, a JSON Schema called [``VM_schema.json``](./VM_schema.json) is included alongside it. This schema can be used to validate the "version_manifest.json" file before each release. There are multiple ways to validate the data with the schema, in many languages (e.g. bash, python, etc.). For example, we can deploy BioValidator and provide it with both the VM schema and document. 
````bash
# Assuming you have Biovalidator cloned and installed on a directory above EGA's repo
$ node src/biovalidator -s ../ega-metadata-schema/docs/releases/VM_schema.json -d ../ega-metadata-schema/docs/releases/version_manifest.json
````

We hope that this document and the accompanying diagram help to clarify the release workflow for the EGA Metadata Schemas project. If you have any questions or concerns, please don't hesitate to reach out to us.

### Updating the version manifest
In order to keep the version manifest updated every time there is a new release to be merged to ``main``, there is an automatic way to modify it. It is making use of the [``update_version_manifest.py``](../../.github/scripts/update_version_manifest.py) script. Check details of the script in its help (i.e. ``--help``) documentation.

The script is **automatically** triggered by a GitHub action (see [file](../../.github/workflows/update_version_manifest.yml) and [diagram](../../docs/gh_workflows/README.md#version-manifest-update)), but can also be triggered **manually**. If the latter, one can, within the release branch (e.g. ``v2.0.1``) execute the script as follows:
````
$ python3 .github/scripts/update_version_manifest.py
````
If, during the review of a PR the version of some schemas change with respect to the ones at the beginning of the PR (which were automatically saved by the GH action), then the version manifest needs to be updated. This update during the PR to ``main`` should overwrite the existing project version that was saved at its creation. In order to do so, one can simply add ``--overwrite_mode``, but use with **caution**:
````
python3 .github/scripts/update_version_manifest.py --overwrite_mode
````

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
