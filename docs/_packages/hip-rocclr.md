---
name: "hip-rocclr"
layout: package
next_package: qcachegrind
previous_package: gnutls
languages: ['cpp']
---
## 3.5.0
7 / 508 files match

 - [elf/utils/common/elfdefinitions.h](#elfutilscommonelfdefinitionsh)
 - [device/pal/paldevicegl.cpp](#devicepalpaldeviceglcpp)
 - [device/gpu/gslbe/src/rt/GSLDeviceGL.cpp](#devicegpugslbesrcrtgsldeviceglcpp)
 - [device/rocm/pro/prodevice.cpp](#devicerocmproprodevicecpp)
 - [os/os_posix.cpp](#osos_posixcpp)
 - [opencl-on-vdi/amdocl/cl_icd.cpp](#opencl-on-vdiamdoclcl_icdcpp)
 - [opencl-on-vdi/khronos/icd/loader/linux/icd_linux.c](#opencl-on-vdikhronosicdloaderlinuxicd_linuxc)

### elf/utils/common/elfdefinitions.h

```cpp

{% raw %}
306 | 	"default suffix of DSO to be appended by dlopen")		\
{% endraw %}

```
### device/pal/paldevicegl.cpp

```

{% raw %}
668 |   void* pModule = dlopen("libGL.so.1", RTLD_NOW);
{% endraw %}

```
### device/gpu/gslbe/src/rt/GSLDeviceGL.cpp

```

{% raw %}
626 |     void * pModule = dlopen("libGL.so.1",RTLD_NOW);
{% endraw %}

```
### device/rocm/pro/prodevice.cpp

```

{% raw %}
67 |     lib_drm_handle_ = dlopen("libdrm_amdgpu.so.1", RTLD_NOW);
{% endraw %}

```
### os/os_posix.cpp

```

{% raw %}
173 |   return (*filename == '\0') ? NULL : ::dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### opencl-on-vdi/amdocl/cl_icd.cpp

```

{% raw %}
227 |     otherPlatform = dlopen("libamdocl64.so", RTLD_LAZY);
232 |     otherPlatform = dlopen("libamdocl-orca64.so", RTLD_LAZY);
{% endraw %}

```
### opencl-on-vdi/khronos/icd/loader/linux/icd_linux.c

```cpp

{% raw %}
160 |     return dlopen (libraryName, RTLD_NOW);
{% endraw %}

```