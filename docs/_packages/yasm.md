---
name: "yasm"
layout: package
next_package: gtkplus
previous_package: prism
languages: ['cmake', 'cpp']
---
## 1.3.0
3 / 1400 files match

 - [ConfigureChecks.cmake](#configurecheckscmake)
 - [m4/lib-link.m4](#m4lib-linkm4)
 - [frontends/yasm/yasm-plugin.c](#frontendsyasmyasm-pluginc)

### ConfigureChecks.cmake

```cmake

{% raw %}
22 | CHECK_LIBRARY_EXISTS(dl dlopen "" HAVE_LIBDL)
{% endraw %}

```
### m4/lib-link.m4

```

{% raw %}
518 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### frontends/yasm/yasm-plugin.c

```cpp

{% raw %}
48 |     return dlopen(name, RTLD_NOW);
{% endraw %}

```