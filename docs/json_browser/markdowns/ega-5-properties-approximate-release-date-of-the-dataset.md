# Approximate release date of the dataset Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/approximateReleaseDate
```

An approximate date of the desired release of the dataset. Bare in mind that this will NOT automatically release the dataset, but instead may be used to set a reminder to the submitter (and EGA's HelpDesk team) in case the dataset was not released by this time. This would help in cases where this step was forgotten by the submitter or release was stalled for some reason.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.dataset.json\*](../../../schemas/EGA.dataset.json "open original schema") |

## approximateReleaseDate Type

`string` ([Approximate release date of the dataset](ega-5-properties-approximate-release-date-of-the-dataset.md))

all of

*   [We cap the reminder up to 3 years](ega-5-properties-approximate-release-date-of-the-dataset-allof-we-cap-the-reminder-up-to-3-years.md "check type definition")

## approximateReleaseDate Constraints

**date**: the string must be a date string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

## approximateReleaseDate Examples

```json
"2021-04-30"
```

```json
"2020-12-29"
```
