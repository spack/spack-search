---
name: "bolt"
layout: package
next_package: jose
previous_package: xerces-c
languages: ['cpp']
---
## 1.0
6 / 813 files match

 - [runtime/src/z_Linux_util.cpp](#runtimesrcz_linux_utilcpp)
 - [runtime/src/ompt-general.cpp](#runtimesrcompt-generalcpp)
 - [runtime/src/kmp_alloc.cpp](#runtimesrckmp_alloccpp)
 - [runtime/src/thirdparty/ittnotify/ittnotify_config.h](#runtimesrcthirdpartyittnotifyittnotify_configh)
 - [libomptarget/src/rtl.cpp](#libomptargetsrcrtlcpp)
 - [libomptarget/plugins/generic-elf-64bit/src/rtl.cpp](#libomptargetpluginsgeneric-elf-64bitsrcrtlcpp)

### runtime/src/z_Linux_util.cpp

```

{% raw %}
1732 |      handler. Mathworks: dlsym() is unsafe. We call dlsym and dlopen
{% endraw %}

```
### runtime/src/ompt-general.cpp

```

{% raw %}
253 |       void *h = dlopen(fname, RTLD_LAZY);
276 |     void *h = dlopen(fname, RTLD_LAZY);
{% endraw %}

```
### runtime/src/kmp_alloc.cpp

```

{% raw %}
1256 |   h_memkind = dlopen(kmp_mk_lib_name, RTLD_LAZY);
{% endraw %}

```
### runtime/src/thirdparty/ittnotify/ittnotify_config.h

```cpp

{% raw %}
300 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
352 | void* dlopen(const char*, int) __attribute__((weak));
355 | #define DL_SYMBOLS (dlopen && dlsym && dlclose)
{% endraw %}

```
### libomptarget/src/rtl.cpp

```

{% raw %}
58 |     void *dynlib_handle = dlopen(Name, RTLD_NOW);
{% endraw %}

```
### libomptarget/plugins/generic-elf-64bit/src/rtl.cpp

```

{% raw %}
214 |   // 2) Use dlopen to load the file and dlsym to retrieve the symbols.
233 |   DynLibTy Lib = {tmp_name, dlopen(tmp_name, RTLD_LAZY)};
{% endraw %}

```