---
name: "brltty"
layout: package
next_package: brpc
previous_package: breseq
languages: ['c']
---
## 5.5
3 / 1334 files match, 2 filtered matches.

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