---
name: "brltty"
layout: package
next_package: buddy
previous_package: cmake
languages: ['c']
---
## 5.5
3 / 1334 files match

 - [Programs/dynld_dlfcn.c](#programsdynld_dlfcnc)
 - [Programs/brltty_jni.c](#programsbrltty_jnic)

### Programs/dynld_dlfcn.c

```c

{% raw %}
62 |   object = dlopen(path, getSharedObjectLoadFlags());
{% endraw %}

```
### Programs/brltty_jni.c

```c

{% raw %}
209 |   if ((coreHandle = dlopen("libbrltty_core.so", RTLD_NOW | RTLD_GLOBAL))) {
{% endraw %}

```