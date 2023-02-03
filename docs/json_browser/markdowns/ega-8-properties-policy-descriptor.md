# Policy descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyDescriptor
```

Node containing the full description of the policy, whether it is hosted at some public resourced and referenced here; or directly written here.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.policy.json\*](../../../schemas/EGA.policy.json "open original schema") |

## policyDescriptor Type

`object` ([Policy descriptor](ega-8-properties-policy-descriptor.md))

any of

*   [Either the policy reference is given](ega-8-properties-policy-descriptor-anyof-either-the-policy-reference-is-given.md "check type definition")

*   [Or the policy text is given](ega-8-properties-policy-descriptor-anyof-or-the-policy-text-is-given.md "check type definition")

# policyDescriptor Properties

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                 |
| :---------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [policyReference](#policyreference) | `string` | Optional | cannot be null | [EGA policy metadata schema](ega-8-properties-policy-descriptor-properties-reference-to-the-policy.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyDescriptor/properties/policyReference") |
| [policyText](#policytext)           | `string` | Optional | cannot be null | [EGA policy metadata schema](ega-8-properties-policy-descriptor-properties-policy-text.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyDescriptor/properties/policyText")                  |

## policyReference

A publicly accessible reference to the policy, where the updated text of the policy is hosted.

`policyReference`

*   is optional

*   Type: `string` ([Reference to the policy](ega-8-properties-policy-descriptor-properties-reference-to-the-policy.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-8-properties-policy-descriptor-properties-reference-to-the-policy.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyDescriptor/properties/policyReference")

### policyReference Type

`string` ([Reference to the policy](ega-8-properties-policy-descriptor-properties-reference-to-the-policy.md))

### policyReference Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$
```

[try pattern](https://regexr.com/?expression=%5E\(http\(s\)%3F%3A%5C%2F%5C%2F.\)%3F\(www%5C.\)%3F%5B-a-zA-Z0-9%40%3A%25._%5C%2B~%23%3D%5D%7B2%2C256%7D%5C.%5Ba-z%5D%7B2%2C6%7D%5Cb\(%5B-a-zA-Z0-9%40%3A%25_%5C%2B.~%23%3F%26%2F%2F%3D%5D*\)%24 "try regular expression with regexr.com")

### policyReference Examples

```json
"https://github.com/EbiEga/ega-metadata-schema/blob/main/schemas/EGA.policy.json"
```

```json
"https://ega-archive.org/submission/dac/documentation"
```

## policyText

Text describing in detail the Data Access Agreement (DAA) of the policy.

`policyText`

*   is optional

*   Type: `string` ([Policy text](ega-8-properties-policy-descriptor-properties-policy-text.md))

*   cannot be null

*   defined in: [EGA policy metadata schema](ega-8-properties-policy-descriptor-properties-policy-text.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/policyDescriptor/properties/policyText")

### policyText Type

`string` ([Policy text](ega-8-properties-policy-descriptor-properties-policy-text.md))

### policyText Examples

```json
"The data is fully available upon request with the data-access committee of this study."
```

```json
"Access to data generated is available by emailing application to the Data Access Committee and will be granted to qualified investigators for appropriate use.\\nThe following two documents may be required by the Data Access Committee.\\n1) DATA ACCESS AGREEMENT\\nIn signing this agreement, You are agreeing to be bound by the terms and conditions of access set out in this agreement.\\nDefinitions:\\n- Data means all and any human genetic data obtained related to the 'Study on the proliferation history of lung adenomas'.\\n- User means a researcher whose User Institution has previously completed this Data Access Agreement and has received acknowledgment of its acceptance.\\n- User Institution means the organization at which the User is employed, affiliated or enrolled.\\nYou agree to use the Data only for the advancement of medical research, according to the consent obtained from sample donors.\\n- Publications means, without limitation, articles published in print journals, electronic journals, reviews, books, posters and other written and verbal presentations of research.\\nYou agree not to use the data for the creation of products for sale or for any commercial purpose.\\nYou agree to preserve, at all times, the confidentiality of any information related to Data and to not transfer or disclose the Data.\\nYou agree to use the data for the approved purpose and project described in your Application.\\nYou agree to acknowledge in any work based in whole or part on the Data, the published paper from which the Data derives.\\nFor and on behalf of User:\\n Report the name of Applicants, Signature of Applicants and Date.\\nFor and on behalf of User Institution:\\nReport the name of Institutional Authority, his/her and Date.\\n\\n2) DATA ACCESS APPLICATION FORM:\\nApplications for access to data can be submitted at any time. The Data Access Committee will consider applications on a rolling basis and aim to provide a decision within one months of receipt. The Application must include:\\n- A full postal and email address for each Applicant. PhD student applicants must include their supervisors as a co-applicant and provide their full contact details.\\n- Title of the project.\\n- A clear description of the project and its specific aims, including specific details of what You plan to do with the data and including key references.\\n- Signature, name and date of each Applicant.\\n- Data Access Agreement dated and signed."
```
