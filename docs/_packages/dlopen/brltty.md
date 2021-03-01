---
name: "brltty"
layout: package
next_package: cairo
previous_package: boost
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.5
3 / 1334 files match, 2 filtered matches.

 - [Programs/dynld_dlfcn.c](#programsdynld_dlfcnc)
 - [Programs/brltty_jni.c](#programsbrltty_jnic)

### Programs/dynld_dlfcn.c

```c

{% raw %}
59 |   void *object;
60 | 
61 |   clearError();
62 |   object = dlopen(path, getSharedObjectLoadFlags());
63 |   if (!object) logError();
64 |   return object;
{% endraw %}

```
### Programs/brltty_jni.c

```c

{% raw %}
206 | loadCoreLibrary (JNIEnv *env) {
207 |   if (coreHandle) return 1;
208 | 
209 |   if ((coreHandle = dlopen("libbrltty_core.so", RTLD_NOW | RTLD_GLOBAL))) {
210 |     int allFound = 1;
211 |     const SymbolEntry *symbol = symbolTable;
{% endraw %}

```