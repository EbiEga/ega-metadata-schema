# Check: checksum checks based on its method Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/checksumPatternCheck
```

This object exists with the only purpose of being a reference of pattern checks of the given checksum (e.g. 'c6779ec2960296ed9a04f08d67f64423') of a file based on its corresponding method (e.g. if the given checksum method is 'MD5' the checksum shall fit into MD5's format of '^[0-9a-z](?:-?\[0-9a-z]){31}$')

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## checksumPatternCheck Type

`object` ([Check: checksum checks based on its method](ega-4-defs-check-checksum-checks-based-on-its-method.md))

any of

* [Checksum pattern check - MD5](ega-4-defs-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5.md "check type definition")

* [Checksum pattern check - SHA-256](ega-4-defs-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256.md "check type definition")
