---
name: "neovim"
layout: package
next_package: rngstreams
previous_package: py-pybind11
languages: ['cmake', 'cpp']
---
## 0.2.1
2 / 2259 files match

 - [src/nvim/os/dl.c](#srcnvimosdlc)
 - [cmake/FindLibUV.cmake](#cmakefindlibuvcmake)

### src/nvim/os/dl.c

```cpp

{% raw %}
53 |   if (uv_dlopen(libname, &lib)) {
{% endraw %}

```
### cmake/FindLibUV.cmake

```cmake

{% raw %}
56 | check_library_exists(dl dlopen "dlfcn.h" HAVE_LIBDL)
{% endraw %}

```