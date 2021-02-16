---
name: "intel-tbb"
layout: package
next_package: libuuid
previous_package: vtk
languages: ['c']
---
## 2018.2
11 / 1460 files match, 1 filtered matches.

 - [src/test/harness_dynamic_libs.h](#srctestharness_dynamic_libsh)

### src/test/harness_dynamic_libs.h

```c

{% raw %}
90 |     return dlopen(name, RTLD_NOW|RTLD_GLOBAL);
{% endraw %}

```