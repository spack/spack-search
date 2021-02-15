---
name: "sfcgal"
layout: package
next_package: paraver
previous_package: libp11
languages: ['cmake']
---
## 1.3.7
1 / 368 files match

 - [cmake/Modules/Libtoolize.cmake](#cmakemoduleslibtoolizecmake)

### cmake/Modules/Libtoolize.cmake

```cmake

{% raw %}
16 |    GET_TARGET_PROPERTY_WITH_DEFAULT(_target_dlopen ${_target} LT_DLOPEN "")
24 |    FILE(APPEND ${_laname} "# The name that we can dlopen(3).\n")
42 |    FILE(APPEND ${_laname} "# Files to dlopen/dlpreopen\n")
43 |    FILE(APPEND ${_laname} "dlopen='${_target_dlopen}'\n")
{% endraw %}

```