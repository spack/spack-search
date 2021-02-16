---
name: "llvm-openmp"
layout: package
next_package: llvm-openmp-ompt
previous_package: llvm-doe
languages: ['c']
---
## 8.0.0
6 / 416 files match, 1 filtered matches.

 - [runtime/src/thirdparty/ittnotify/ittnotify_config.h](#runtimesrcthirdpartyittnotifyittnotify_configh)

### runtime/src/thirdparty/ittnotify/ittnotify_config.h

```c

{% raw %}
345 | void* dlopen(const char*, int) __attribute__((weak));
{% endraw %}

```