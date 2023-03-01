# Release Workflow for Ega Metadata Schemas
In this document you will find the workflow for creating releases of the Ega Metadata Schemas GitHub project. It provides a step-by-step diagram to help illustrate the steps involved.

## Workflow Diagram
![Release Workflow Diagram](Release_workflow_diagram.svg)


The above diagram illustrates the process for creating a new release of the EGA Metadata Schemas project.

## Version Manifest
To keep track of which JSON schema versions are included in each release version of the Ega Metadata Schemas project, a manifest ([``version_manifest.json``](./version_manifest.json)) is maintained in this same directory. This file lists the schema versions included in each release, along with other relevant metadata of the releases.

To ensure that the "version_manifest.json" file is properly formatted, a JSON Schema called [``VM_schema.json``](./VM_schema.json)) is included in the same directory. This schema can be used to validate the "version_manifest.json" file before each release.

We hope that this document and the accompanying diagram help to clarify the release workflow for the EGA Metadata Schemas project. If you have any questions or concerns, please don't hesitate to reach out to us.