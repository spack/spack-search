---
name: "gtkorvo-dill"
layout: package
next_package: harfbuzz
previous_package: vampirtrace
languages: ['cmake']
---
## 2.1
1 / 77 files match

 - [cmake/CreateLibtoolFile.cmake](#cmakecreatelibtoolfilecmake)

### cmake/CreateLibtoolFile.cmake

```cmake

{% raw %}
20 |    GET_TARGET_PROPERTY_WITH_DEFAULT(_target_dlopen ${_target} LT_DLOPEN "")
28 |    FILE(APPEND ${_laname} "# The name that we can dlopen(3).\n")
48 |    FILE(APPEND ${_laname} "# Files to dlopen/dlpreopen\n")
49 |    FILE(APPEND ${_laname} "dlopen='${_target_dlopen}'\n")
{% endraw %}

```