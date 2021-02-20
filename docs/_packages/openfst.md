---
name: "openfst"
layout: package
next_package: openldap
previous_package: openfoam-org
languages: ['c']
---
## 1.7.9
5 / 493 files match, 1 filtered matches.

 - [src/include/fst/generic-register.h](#srcincludefstgeneric-registerh)

### src/include/fst/generic-register.h

```c

{% raw %}
64 |     return EntryType();
65 | #else
66 |     const auto so_filename = ConvertKeyToSoFilename(key);
67 |     void *handle = dlopen(so_filename.c_str(), RTLD_LAZY);
68 |     if (handle == nullptr) {
69 |       LOG(ERROR) << "GenericRegister::GetEntry: " << dlerror();
{% endraw %}

```