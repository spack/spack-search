---
name: "yasm"
layout: package
next_package: yorick
previous_package: xrootd
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.3.0
1 / 1400 files match, 1 filtered matches.

 - [frontends/yasm/yasm-plugin.c](#frontendsyasmyasm-pluginc)

### frontends/yasm/yasm-plugin.c

```c

{% raw %}
95 |     init_plugin =
96 |         (void (*)(void))GetProcAddress((HINSTANCE)lib, "yasm_init_plugin");
97 | #elif defined(__GNUC__)
98 |     init_plugin = (void (*)(void))(uintptr_t)dlsym(lib, "yasm_init_plugin");
99 | #endif
100 | 
{% endraw %}

```