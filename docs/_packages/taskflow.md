---
name: "taskflow"
layout: package
next_package: tau
previous_package: talloc
languages: ['c']
---
## 2.7.0
11 / 3426 files match, 2 filtered matches.

 - [3rd-party/tbb/src/tbb/tools_api/ittnotify_config.h](#3rd-partytbbsrctbbtools_apiittnotify_configh)
 - [3rd-party/tbb/src/test/harness_dynamic_libs.h](#3rd-partytbbsrctestharness_dynamic_libsh)

### 3rd-party/tbb/src/tbb/tools_api/ittnotify_config.h

```c

{% raw %}
338 | }
339 | #endif /* ITT_SIMPLE_INIT */
340 | 
341 | void* dlopen(const char*, int) __attribute__((weak));
342 | void* dlsym(void*, const char*) __attribute__((weak));
343 | int dlclose(void*) __attribute__((weak));
{% endraw %}

```
### 3rd-party/tbb/src/test/harness_dynamic_libs.h

```c

{% raw %}
83 |     return ::LoadLibrary(name);
84 | #endif
85 | #else
86 |     return dlopen(name, RTLD_NOW|RTLD_GLOBAL);
87 | #endif
88 | }
{% endraw %}

```