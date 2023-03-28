# GitHub Action workflows
EGA's metadata repository makes use of [GitHub Actions](https://docs.github.com/en/actions) in different ways, here summarized through diagrams. All workflows are stored in the [``workflows/``](../../.github/workflows/) directory and you can find documentation within each of the YAML files (one per action type). 

In case the diagrams need to be updated, go to their [original URL](https://app.diagrams.net/#G1COZ89uK1GVNBZ1tr-1GNKZjF5xoA7Mgn): only EGA members have access to it.

## Super-linter
![Super-linter workflow](diagrams/20220419_super_linter.drawio.png)

## JSON docs validation - EGA API
![JSON docs validation workflow](diagrams/20221201_json_validation_against_EGA_API.drawio.png)

## JSON docs validation - Local Biovalidator
![JSON docs validation workflow](diagrams/20221201_github_workflows-json_validation_deploying_biovalidator.drawio.png)

## Markdown creation
![Markdown creation workflow](diagrams/20220419_Markdown_creation.drawio.png)

## Version manifest update
![Version manifest update](diagrams/20230328_github_workflows-version_manifest_update.drawio.svg)
