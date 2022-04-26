# Reference to the policy Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.policy.json#/properties/policy_descriptor/properties/policy_reference
```

A publicly accessible reference to the policy, where the updated text of the policy is hosted.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.policy.json\*](../../../schemas/EGA.policy.json "open original schema") |

## policy\_reference Type

`string` ([Reference to the policy](ega-16-properties-policy-descriptor-properties-reference-to-the-policy.md))

## policy\_reference Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$
```

[try pattern](https://regexr.com/?expression=%5E\(http\(s\)%3F%3A%5C%2F%5C%2F.\)%3F\(www%5C.\)%3F%5B-a-zA-Z0-9%40%3A%25._%5C%2B\~%23%3D%5D%7B2%2C256%7D%5C.%5Ba-z%5D%7B2%2C6%7D%5Cb\(%5B-a-zA-Z0-9%40%3A%25_%5C%2B.\~%23%3F%26%2F%2F%3D%5D*\)%24 "try regular expression with regexr.com")

## policy\_reference Examples

```json
"https://github.com/EbiEga/ega-metadata-schema/blob/main/schemas/EGA.policy.json"
```

```json
"https://ega-archive.org/submission/dac/documentation"
```
