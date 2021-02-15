---
name: "soci"
layout: package
next_package: ns-3-dev
previous_package: capnproto
languages: ['cmake']
---
## 4.0.0
2 / 367 files match

 - [src/core/backend-loader.cpp](#srccorebackend-loadercpp)
 - [cmake/modules/FindDL.cmake](#cmakemodulesfinddlcmake)

### src/core/backend-loader.cpp

```

{% raw %}
36 | #define DLOPEN(x) LoadLibraryA(x)
38 | #define DLOPEN(x) LoadLibrary(x)
65 | #define DLOPEN(x) dlopen(x, RTLD_LAZY)
205 |         h = DLOPEN(shared_object.c_str());
210 |         h = DLOPEN(LIBNAME(name).c_str());
217 |                 h = DLOPEN(fullFileName.c_str());
{% endraw %}

```
### cmake/modules/FindDL.cmake

```cmake

{% raw %}
11 |     # if dlopen can be found without linking in dl then,
12 |     # dlopen is part of libc, so don't need to link extra libs.
14 |     check_function_exists(dlopen DL_FOUND)
{% endraw %}

```