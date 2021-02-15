---
name: "cquery"
layout: package
next_package: check
previous_package: ldc
languages: []
---
## 2018-08-23
1 / 3353 files match

 - [third_party/doctest/examples/executable_dll_and_plugin/main.cpp](#third_partydoctestexamplesexecutable_dll_and_pluginmaincpp)

### third_party/doctest/examples/executable_dll_and_plugin/main.cpp

```

{% raw %}
36 | #define LoadDynamicLib(lib) dlopen("lib" lib ".dylib", RTLD_NOW)
38 | #define LoadDynamicLib(lib) dlopen("lib" lib ".so", RTLD_NOW)
{% endraw %}

```