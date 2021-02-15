---
name: "graphite2"
layout: package
next_package: r-pbdzmq
previous_package: erne
languages: ['cmake']
---
## 1.3.13
1 / 349 files match

 - [Graphite.cmake](#graphitecmake)

### Graphite.cmake

```cmake

{% raw %}
34 |   GET_TARGET_PROPERTY_WITH_DEFAULT(_target_dlopen ${_target} LT_DLOPEN "")
44 |   FILE(APPEND ${_laname} "# The name that we can dlopen(3).\n")
66 |   FILE(APPEND ${_laname} "# Files to dlopen/dlpreopen\n")
67 |   FILE(APPEND ${_laname} "dlopen='${_target_dlopen}'\n")
{% endraw %}

```