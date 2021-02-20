---
name: "intel-tbb"
layout: package
next_package: ipcalc
previous_package: intel-pin
languages: ['c']
---
## 2018.2
11 / 1460 files match, 1 filtered matches.

 - [src/test/harness_dynamic_libs.h](#srctestharness_dynamic_libsh)

### src/test/harness_dynamic_libs.h

```c

{% raw %}
87 |     return ::LoadLibrary(name);
88 | #endif
89 | #else
90 |     return dlopen(name, RTLD_NOW|RTLD_GLOBAL);
91 | #endif
92 | }
{% endraw %}

```