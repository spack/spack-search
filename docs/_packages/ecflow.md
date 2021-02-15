---
name: "ecflow"
layout: package
next_package: libice
previous_package: fenics
languages: ['cmake']
---
## 4.12.0
2 / 2757 files match

 - [Jamroot.jam](#jamrootjam)
 - [cmake/ecbuild_add_library.cmake](#cmakeecbuild_add_librarycmake)

### Jamroot.jam

```

{% raw %}
18 | # link with libdl.so, shared lib containing dlopen(),dlclose()dysym(),
24 | lib dl ;      # this dependency for using libcrypto, i.e dlopen,dlclose etc, when using static libcrypto
{% endraw %}

```
### cmake/ecbuild_add_library.cmake

```cmake

{% raw %}
61 | #            dynamically at runtime using dlopen-like functionality
{% endraw %}

```