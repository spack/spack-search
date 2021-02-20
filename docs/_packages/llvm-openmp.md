---
name: "llvm-openmp"
layout: package
next_package: ltrace
previous_package: llvm-doe
languages: ['c']
---
## 8.0.0
6 / 416 files match, 1 filtered matches.

 - [runtime/src/thirdparty/ittnotify/ittnotify_config.h](#runtimesrcthirdpartyittnotifyittnotify_configh)

### runtime/src/thirdparty/ittnotify/ittnotify_config.h

```c

{% raw %}
342 | }
343 | #endif /* ITT_SIMPLE_INIT */
344 | 
345 | void* dlopen(const char*, int) __attribute__((weak));
346 | void* dlsym(void*, const char*) __attribute__((weak));
347 | int dlclose(void*) __attribute__((weak));
{% endraw %}

```