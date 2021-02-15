---
name: "libproxy"
layout: package
next_package: netdata
previous_package: clamr
languages: []
---
## 0.4.15
1 / 107 files match

 - [libmodman/module_manager.cpp](#libmodmanmodule_managercpp)

### libmodman/module_manager.cpp

```

{% raw %}
27 | #include <dlfcn.h>  // For dlopen(), etc...
42 | #define pdlopenl(filename) LoadLibraryEx(filename, NULL, DONT_RESOLVE_DLL_REFERENCES)
86 | #define pdlopenl(filename) dlopen(filename, RTLD_LAZY | RTLD_LOCAL)
98 | 	void* mod = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL);
250 | 	pdlmtype dlobj = pdlopenl(filename.c_str());
{% endraw %}

```