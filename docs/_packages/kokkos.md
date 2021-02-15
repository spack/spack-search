---
name: "kokkos"
layout: package
next_package: axom
previous_package: coinutils
languages: []
---
## 3.1.00
1 / 2302 files match

 - [core/src/impl/Kokkos_Profiling_Interface.cpp](#coresrcimplkokkos_profiling_interfacecpp)

### core/src/impl/Kokkos_Profiling_Interface.cpp

```

{% raw %}
229 |     firstProfileLibrary = dlopen(profileLibraryName, RTLD_NOW | RTLD_GLOBAL);
234 |       std::cerr << "dlopen(" << profileLibraryName
{% endraw %}

```