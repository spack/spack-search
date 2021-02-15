---
name: "hip"
layout: package
next_package: libxevie
previous_package: unifyfs
languages: []
---
## 3.10.0
2 / 745 files match

 - [amdocl/cl_icd.cpp](#amdoclcl_icdcpp)
 - [tests/src/dynamicLoading/complex_loading_behavior.cpp](#testssrcdynamicloadingcomplex_loading_behaviorcpp)

### amdocl/cl_icd.cpp

```

{% raw %}
227 |     otherPlatform = dlopen("libamdocl64.so", RTLD_LAZY);
232 |     otherPlatform = dlopen("libamdocl-orca64.so", RTLD_LAZY);
{% endraw %}

```
### tests/src/dynamicLoading/complex_loading_behavior.cpp

```

{% raw %}
99 |   void* handle = dlopen("./libfoo.so", RTLD_LAZY);
{% endraw %}

```