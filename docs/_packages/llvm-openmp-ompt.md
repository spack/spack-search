---
name: "llvm-openmp-ompt"
layout: package
next_package: weechat
previous_package: xts
languages: ['cpp']
---
## 3.9.2b
5 / 396 files match

 - [runtime/src/z_Linux_util.cpp](#runtimesrcz_linux_utilcpp)
 - [runtime/src/ompt-general.cpp](#runtimesrcompt-generalcpp)
 - [runtime/src/thirdparty/ittnotify/ittnotify_config.h](#runtimesrcthirdpartyittnotifyittnotify_configh)
 - [libomptarget/src/rtl.cpp](#libomptargetsrcrtlcpp)
 - [libomptarget/plugins/generic-elf-64bit/src/rtl.cpp](#libomptargetpluginsgeneric-elf-64bitsrcrtlcpp)

### runtime/src/z_Linux_util.cpp

```

{% raw %}
1348 |      handler. Mathworks: dlsym() is unsafe. We call dlsym and dlopen
{% endraw %}

```
### runtime/src/ompt-general.cpp

```

{% raw %}
254 |       void *h = dlopen(fname, RTLD_LAZY);
{% endraw %}

```
### runtime/src/thirdparty/ittnotify/ittnotify_config.h

```cpp

{% raw %}
280 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
{% endraw %}

```
### libomptarget/src/rtl.cpp

```

{% raw %}
60 |     void *dynlib_handle = dlopen(Name, RTLD_NOW);
{% endraw %}

```
### libomptarget/plugins/generic-elf-64bit/src/rtl.cpp

```

{% raw %}
214 |   // 2) Use dlopen to load the file and dlsym to retrieve the symbols.
233 |   DynLibTy Lib = {tmp_name, dlopen(tmp_name, RTLD_LAZY)};
{% endraw %}

```