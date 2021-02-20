---
name: "yasm"
layout: package
next_package: yorick
previous_package: xrootd
languages: ['c']
---
## 1.3.0
3 / 1400 files match, 1 filtered matches.

 - [frontends/yasm/yasm-plugin.c](#frontendsyasmyasm-pluginc)

### frontends/yasm/yasm-plugin.c

```c

{% raw %}
45 | #if defined(_MSC_VER)
46 |     return LoadLibrary(name);
47 | #elif defined(__GNUC__)
48 |     return dlopen(name, RTLD_NOW);
49 | #else
50 |     return NULL;
{% endraw %}

```