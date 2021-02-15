---
name: "rocm-opencl"
layout: package
next_package: py-exodus-bundler
previous_package: pnmpi
languages: ['cpp']
---
## 3.10.0
3 / 491 files match

 - [amdocl/cl_icd.cpp](#amdoclcl_icdcpp)
 - [tests/ocltst/env/ocltst.cpp](#testsocltstenvocltstcpp)
 - [khronos/icd/loader/linux/icd_linux.c](#khronosicdloaderlinuxicd_linuxc)

### amdocl/cl_icd.cpp

```

{% raw %}
227 |     otherPlatform = dlopen("libamdocl64.so", RTLD_LAZY);
232 |     otherPlatform = dlopen("libamdocl-orca64.so", RTLD_LAZY);
{% endraw %}

```
### tests/ocltst/env/ocltst.cpp

```

{% raw %}
1385 |     mod.hmodule = dlopen(m_paths[i].c_str(), RTLD_NOW);
{% endraw %}

```
### khronos/icd/loader/linux/icd_linux.c

```cpp

{% raw %}
160 |     void *retVal = dlopen (libraryName, RTLD_NOW);
{% endraw %}

```