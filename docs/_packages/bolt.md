---
name: "bolt"
layout: package
next_package: boost
previous_package: bmi
languages: ['c']
---
## 1.0
6 / 813 files match, 1 filtered matches.

 - [runtime/src/thirdparty/ittnotify/ittnotify_config.h](#runtimesrcthirdpartyittnotifyittnotify_configh)

### runtime/src/thirdparty/ittnotify/ittnotify_config.h

```c

{% raw %}
349 | }
350 | #endif /* ITT_SIMPLE_INIT */
351 | 
352 | void* dlopen(const char*, int) __attribute__((weak));
353 | void* dlsym(void*, const char*) __attribute__((weak));
354 | int dlclose(void*) __attribute__((weak));
{% endraw %}

```