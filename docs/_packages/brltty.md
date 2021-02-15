---
name: "brltty"
layout: package
next_package: buddy
previous_package: cmake
languages: ['cpp']
---
## 5.5
3 / 1334 files match

 - [configure.ac](#configureac)
 - [Programs/dynld_dlfcn.c](#programsdynld_dlfcnc)
 - [Programs/brltty_jni.c](#programsbrltty_jnic)

### configure.ac

```

{% raw %}
1163 |          AC_SEARCH_LIBS([dlopen], [dl], [dnl
{% endraw %}

```
### Programs/dynld_dlfcn.c

```cpp

{% raw %}
62 |   object = dlopen(path, getSharedObjectLoadFlags());
{% endraw %}

```
### Programs/brltty_jni.c

```cpp

{% raw %}
209 |   if ((coreHandle = dlopen("libbrltty_core.so", RTLD_NOW | RTLD_GLOBAL))) {
{% endraw %}

```