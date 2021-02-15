---
name: "nccl"
layout: package
next_package: netcdf-c
previous_package: libunistring
languages: ['cpp']
---
## 2.8.3-1
4 / 121 files match

 - [src/init.cc](#srcinitcc)
 - [src/include/nvtx3/nvtxDetail/nvtxInit.h](#srcincludenvtx3nvtxdetailnvtxinith)
 - [src/misc/ibvwrap.cc](#srcmiscibvwrapcc)
 - [src/misc/nvmlwrap.cc](#srcmiscnvmlwrapcc)

### src/init.cc

```cpp

{% raw %}
68 |   void* netPluginLib = dlopen("libnccl-net.so", RTLD_NOW | RTLD_LOCAL);
70 |     // dlopen does not guarantee to set errno, but dlerror only gives us a
{% endraw %}

```
### src/include/nvtx3/nvtxDetail/nvtxInit.h

```cpp

{% raw %}
35 | #define NVTX_DLLOPEN(x) dlopen(x, RTLD_LAZY)
191 |             /* For dlopen, if the filename contains a leading slash, then it is interpreted as a */
{% endraw %}

```
### src/misc/ibvwrap.cc

```cpp

{% raw %}
58 |   ibvhandle=dlopen("libibverbs.so", RTLD_NOW);
60 |     ibvhandle=dlopen("libibverbs.so.1", RTLD_NOW);
{% endraw %}

```
### src/misc/nvmlwrap.cc

```cpp

{% raw %}
44 |   nvmlhandle=dlopen("libnvidia-ml.so.1", RTLD_NOW);
{% endraw %}

```