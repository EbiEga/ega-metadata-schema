# Reference to the policy Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyDescriptor/properties/policyReference
```

A publicly accessible reference to the policy, where the updated text of the policy is hosted.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.policy.json\*](../../../schemas/EGA.policy.json "open original schema") |

## policyReference Type

`string` ([Reference to the policy](ega-8-properties-policy-descriptor-properties-reference-to-the-policy.md))

## policyReference Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

## policyReference Examples

```json
"https://github.com/EbiEga/ega-metadata-schema/blob/main/schemas/EGA.policy.json"
```

```json
"https://ega-archive.org/submission/dac/documentation"
```
