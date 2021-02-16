---
name: "opencv"
layout: package
next_package: gperftools
previous_package: libsigsegv
languages: ['c']
---
## 3.4.4
8 / 5975 files match

 - [3rdparty/cpufeatures/cpu-features.c](#3rdpartycpufeaturescpu-featuresc)
 - [3rdparty/ittnotify/src/ittnotify/jitprofiling.c](#3rdpartyittnotifysrcittnotifyjitprofilingc)
 - [3rdparty/ittnotify/src/ittnotify/ittnotify_config.h](#3rdpartyittnotifysrcittnotifyittnotify_configh)

### 3rdparty/cpufeatures/cpu-features.c

```c

{% raw %}
541 |     void* libc_handle = dlopen("libc.so", RTLD_NOW);
543 |         D("Could not dlopen() C library: %s\n", dlerror());
{% endraw %}

```
### 3rdparty/ittnotify/src/ittnotify/jitprofiling.c

```c

{% raw %}
253 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
262 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
{% endraw %}

```
### 3rdparty/ittnotify/src/ittnotify/ittnotify_config.h

```c

{% raw %}
373 | void* dlopen(const char*, int) __attribute__((weak));
{% endraw %}

```