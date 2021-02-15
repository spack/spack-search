---
name: "pocl"
layout: package
next_package: py-spacy-models-en-vectors-web-lg
previous_package: blast-legacy
languages: ['cpp']
---
## 1.6
7 / 1647 files match

 - [CMakeLists.txt](#cmakeliststxt)
 - [lib/CL/pocl_llvm_api.h](#libclpocl_llvm_apih)
 - [lib/CL/devices/common.c](#libcldevicescommonc)
 - [lib/CL/devices/devices.c](#libcldevicesdevicesc)
 - [include/vccompat.hpp](#includevccompathpp)
 - [doc/sphinx/source/faq.rst](#docsphinxsourcefaqrst)
 - [doc/sphinx/source/install.rst](#docsphinxsourceinstallrst)

### CMakeLists.txt

```

{% raw %}
772 | set(HAVE_LIBDL OFF CACHE BOOL "dlopen" FORCE)
795 |       set(HAVE_LIBDL ON CACHE BOOL "dlopen" FORCE)
{% endraw %}

```
### lib/CL/pocl_llvm_api.h

```cpp

{% raw %}
45 |  * if pocl is dlopened from a C++ program, pocl's C++ object destructors
{% endraw %}

```
### lib/CL/devices/common.c

```cpp

{% raw %}
1041 |  * dlopen, and reuses its handle. If not, checks if a built binary is found
1086 |   ci->dlhandle = dlopen (module_fn, RTLD_NOW | RTLD_LOCAL);
1090 |     POCL_ABORT ("dlopen(\"%s\") failed with '%s'.\n"
{% endraw %}

```
### lib/CL/devices/devices.c

```cpp

{% raw %}
588 |           pocl_device_handles[i] = dlopen (device_library, RTLD_LAZY);
{% endraw %}

```
### include/vccompat.hpp

```

{% raw %}
71 | static inline void* dlopen(const char* filename, int flags) {
{% endraw %}

```
### doc/sphinx/source/faq.rst

```

{% raw %}
89 | * the ICD loader will try to dlopen libpocl.so -> you get the error.
{% endraw %}

```
### doc/sphinx/source/install.rst

```

{% raw %}
114 | which is then dlopened):
{% endraw %}

```