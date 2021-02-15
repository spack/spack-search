---
name: "opencv"
layout: package
next_package: gperftools
previous_package: libsigsegv
languages: ['cpp']
---
## 3.4.4
8 / 5975 files match

 - [3rdparty/cpufeatures/cpu-features.c](#3rdpartycpufeaturescpu-featuresc)
 - [3rdparty/ittnotify/src/ittnotify/jitprofiling.c](#3rdpartyittnotifysrcittnotifyjitprofilingc)
 - [3rdparty/ittnotify/src/ittnotify/ittnotify_config.h](#3rdpartyittnotifysrcittnotifyittnotify_configh)
 - [modules/core/src/gl_core_3_1.cpp](#modulescoresrcgl_core_3_1cpp)
 - [modules/core/src/ocl_deprecated.hpp](#modulescoresrcocl_deprecatedhpp)
 - [modules/core/src/opencl/runtime/opencl_core.cpp](#modulescoresrcopenclruntimeopencl_corecpp)
 - [modules/core/src/opencl/runtime/opencl_clamdblas.cpp](#modulescoresrcopenclruntimeopencl_clamdblascpp)
 - [modules/core/src/opencl/runtime/opencl_clamdfft.cpp](#modulescoresrcopenclruntimeopencl_clamdfftcpp)

### 3rdparty/cpufeatures/cpu-features.c

```cpp

{% raw %}
519 | // (under other dlopen() call).
520 | // Unfortunatelly, calling dlopen() recursively is not supported on some old
541 |     void* libc_handle = dlopen("libc.so", RTLD_NOW);
543 |         D("Could not dlopen() C library: %s\n", dlerror());
{% endraw %}

```
### 3rdparty/ittnotify/src/ittnotify/jitprofiling.c

```cpp

{% raw %}
253 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
262 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
{% endraw %}

```
### 3rdparty/ittnotify/src/ittnotify/ittnotify_config.h

```cpp

{% raw %}
323 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
373 | void* dlopen(const char*, int) __attribute__((weak));
376 | #define DL_SYMBOLS (dlopen && dlsym && dlclose)
{% endraw %}

```
### modules/core/src/gl_core_3_1.cpp

```

{% raw %}
61 |                     handle = dlopen(path, RTLD_LAZY | RTLD_GLOBAL);
83 |                 h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### modules/core/src/ocl_deprecated.hpp

```

{% raw %}
565 |             handle = dlopen(oclpath, RTLD_LAZY);
628 |             handle = dlopen("libOpenCL.so", RTLD_LAZY);
630 |                 handle = dlopen("libCL.so", RTLD_LAZY);
{% endraw %}

```
### modules/core/src/opencl/runtime/opencl_core.cpp

```

{% raw %}
94 |                 handle = dlopen(path, RTLD_LAZY | RTLD_GLOBAL);
164 |     handle = dlopen(file, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### modules/core/src/opencl/runtime/opencl_clamdblas.cpp

```

{% raw %}
78 |             h = dlopen("libclAmdBlas.so", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### modules/core/src/opencl/runtime/opencl_clamdfft.cpp

```

{% raw %}
78 |             h = dlopen("libclAmdFft.Runtime.so", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```