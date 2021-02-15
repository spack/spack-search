---
name: "boinc-client"
layout: package
next_package: conduit
previous_package: libpulsar
languages: ['cpp']
---
## 7.16.5
12 / 6111 files match

 - [configure.ac](#configureac)
 - [lib/diagnostics.cpp](#libdiagnosticscpp)
 - [lib/mac/mac_backtrace.cpp](#libmacmac_backtracecpp)
 - [lib/mac/mac_util.mm](#libmacmac_utilmm)
 - [clientgui/gtk/taskbarex.cpp](#clientguigtktaskbarexcpp)
 - [clientgui/mac/MacNotification.mm](#clientguimacmacnotificationmm)
 - [m4/check_ssl.m4](#m4check_sslm4)
 - [client/gpu_nvidia.cpp](#clientgpu_nvidiacpp)
 - [client/gpu_amd.cpp](#clientgpu_amdcpp)
 - [client/gpu_opencl.cpp](#clientgpu_openclcpp)
 - [api/graphics_impl.h](#apigraphics_implh)
 - [api/graphics_lib.cpp](#apigraphics_libcpp)

### configure.ac

```

{% raw %}
373 | AC_LIBTOOL_DLOPEN
504 | SAH_CHECK_LIB([dl], [dlopen],
{% endraw %}

```
### lib/diagnostics.cpp

```

{% raw %}
419 |     if ((libhandle=dlopen("libcorkscrew.so",RTLD_NOW|RTLD_GLOBAL))) {
{% endraw %}

```
### lib/mac/mac_backtrace.cpp

```

{% raw %}
85 | #define DLOPEN_NO_WARN
185 |     systemlib = dlopen ("/usr/lib/libSystem.dylib", RTLD_NOW );
{% endraw %}

```
### lib/mac/mac_util.mm

```

{% raw %}
21 | #define DLOPEN_NO_WARN
92 |     void *LSlib = dlopen("/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/LaunchServices", RTLD_NOW | RTLD_NODELETE);
{% endraw %}

```
### clientgui/gtk/taskbarex.cpp

```

{% raw %}
134 |     notify_lib = dlopen("libnotify.so", RTLD_NOW);
{% endraw %}

```
### clientgui/mac/MacNotification.mm

```

{% raw %}
27 | // objective-C equivalent of dlopen() and dlsym().
{% endraw %}

```
### m4/check_ssl.m4

```

{% raw %}
49 |       AC_CHECK_LIB([dl], [dlopen], 
61 |       AC_CHECK_LIB([dl], [dlopen], 
{% endraw %}

```
### client/gpu_nvidia.cpp

```

{% raw %}
75 | #define DLOPEN_NO_WARN
109 |     handle  = dlopen("libnvidia-ml.so.1", RTLD_NOW);
111 |         handle  = dlopen("libnvidia-ml.so", RTLD_NOW);
293 |     cudalib = dlopen("/usr/local/cuda/lib/libcuda.dylib", RTLD_NOW);
295 |     cudalib = dlopen("libcuda.so", RTLD_NOW);
{% endraw %}

```
### client/gpu_amd.cpp

```

{% raw %}
31 | #define DLOPEN_NO_WARN
160 |     void* callib = dlopen("libaticalrt.so", RTLD_NOW);
{% endraw %}

```
### client/gpu_opencl.cpp

```

{% raw %}
29 | #define DLOPEN_NO_WARN
223 |     opencl_lib = dlopen("/System/Library/Frameworks/OpenCL.framework/Versions/Current/OpenCL", RTLD_NOW);
225 |     opencl_lib = dlopen("libOpenCL.so", RTLD_NOW);
227 |         opencl_lib = dlopen("libOpenCL.so.1", RTLD_NOW);
{% endraw %}

```
### api/graphics_impl.h

```cpp

{% raw %}
45 | // See http://www.isotton.com/howtos/C++-dlopen-mini-HOWTO/C++-dlopen-mini-HOWTO.html
{% endraw %}

```
### api/graphics_lib.cpp

```

{% raw %}
108 |     graphics_lib_handle = dlopen(resolved_name,  RTLD_NOW);
112 |             "dlopen() failed: %s\nNo graphics.\n", errormsg?errormsg:""
{% endraw %}

```