---
name: "bazel"
layout: package
next_package: bcftools
previous_package: bash
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 0.29.0
9 / 10999 files match, 1 filtered matches.

 - [third_party/grpc/src/core/lib/gpr/env_linux.cc](#third_partygrpcsrccorelibgprenv_linuxcc)

### third_party/grpc/src/core/lib/gpr/env_linux.cc

```cpp

{% raw %}
47 |    * to least secure) */
48 |   const char* names[] = {"secure_getenv", "__secure_getenv", "getenv"};
49 |   for (size_t i = 0; getenv_func == NULL && i < GPR_ARRAY_SIZE(names); i++) {
50 |     getenv_func = (getenv_type)dlsym(RTLD_DEFAULT, names[i]);
51 |     if (getenv_func != NULL && strstr(names[i], "secure") == NULL) {
52 |       insecure_func_used = names[i];
{% endraw %}

```