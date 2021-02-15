---
name: "ompt-openmp"
layout: package
next_package: mozjs
previous_package: util-linux-uuid
languages: ['cpp']
---
## 0.1
3 / 416 files match

 - [runtime/src/z_Linux_util.c](#runtimesrcz_linux_utilc)
 - [runtime/src/thirdparty/ittnotify/ittnotify_config.h](#runtimesrcthirdpartyittnotifyittnotify_configh)
 - [offload/src/offload_util.h](#offloadsrcoffload_utilh)

### runtime/src/z_Linux_util.c

```cpp

{% raw %}
1615 |        handler. Mathworks: dlsym() is unsafe. We call dlsym and dlopen
{% endraw %}

```
### runtime/src/thirdparty/ittnotify/ittnotify_config.h

```cpp

{% raw %}
268 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
{% endraw %}

```
### offload/src/offload_util.h

```cpp

{% raw %}
120 | #define DL_open(path)           dlopen((path), RTLD_NOW)
{% endraw %}

```