---
name: "grpc"
layout: package
next_package: weechat
previous_package: bash
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 1.28.1
3 / 5251 files match, 1 filtered matches.

 - [src/core/lib/gpr/env_linux.cc](#srccorelibgprenv_linuxcc)

### src/core/lib/gpr/env_linux.cc

```cpp

{% raw %}
47 |   if (getenv_func == nullptr) {
48 |     const char* names[] = {"secure_getenv", "__secure_getenv", "getenv"};
49 |     for (size_t i = 0; i < GPR_ARRAY_SIZE(names); i++) {
50 |       getenv_func = (getenv_type)dlsym(RTLD_DEFAULT, names[i]);
51 |       if (getenv_func != nullptr) {
52 |         break;
{% endraw %}

```