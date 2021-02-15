---
name: "nvhpc"
layout: package
next_package: atompaw
previous_package: netcdf-fortran
languages: ['cpp']
---
## 20.11
16 / 18177 files match

 - [install_components/Linux_x86_64/20.11/comm_libs/openmpi/openmpi-3.1.5/share/openmpi/help-mpi-common-cuda.txt](#install_componentslinux_x86_642011comm_libsopenmpiopenmpi-315shareopenmpihelp-mpi-common-cudatxt)
 - [install_components/Linux_x86_64/20.11/comm_libs/openmpi4/openmpi-4.0.5/include/ucm/api/ucm.h](#install_componentslinux_x86_642011comm_libsopenmpi4openmpi-405includeucmapiucmh)
 - [install_components/Linux_x86_64/20.11/comm_libs/openmpi4/openmpi-4.0.5/share/openmpi/help-mpi-common-cuda.txt](#install_componentslinux_x86_642011comm_libsopenmpi4openmpi-405shareopenmpihelp-mpi-common-cudatxt)
 - [install_components/Linux_x86_64/20.11/compilers/extras/qd/lib/libqd.la](#install_componentslinux_x86_642011compilersextrasqdliblibqdla)
 - [install_components/Linux_x86_64/20.11/compilers/extras/qd/lib/libqdmod.la](#install_componentslinux_x86_642011compilersextrasqdliblibqdmodla)
 - [install_components/Linux_x86_64/20.11/compilers/extras/qd/lib/libqd_f_main.la](#install_componentslinux_x86_642011compilersextrasqdliblibqd_f_mainla)
 - [install_components/Linux_x86_64/20.11/profilers/Nsight_Systems/target-linux-x64/nvtx/include/nvtx3/nvtxDetail/nvtxInit.h](#install_componentslinux_x86_642011profilersnsight_systemstarget-linux-x64nvtxincludenvtx3nvtxdetailnvtxinith)
 - [install_components/Linux_x86_64/20.11/cuda/10.2/include/nvtx3/nvtxDetail/nvtxInit.h](#install_componentslinux_x86_642011cuda102includenvtx3nvtxdetailnvtxinith)
 - [install_components/Linux_x86_64/20.11/cuda/11.1/extras/CUPTI/include/nvperf_target.h](#install_componentslinux_x86_642011cuda111extrascuptiincludenvperf_targeth)
 - [install_components/Linux_x86_64/20.11/cuda/11.1/extras/CUPTI/include/nvperf_host.h](#install_componentslinux_x86_642011cuda111extrascuptiincludenvperf_hosth)
 - [install_components/Linux_x86_64/20.11/cuda/11.1/extras/CUPTI/include/nvperf_cuda_host.h](#install_componentslinux_x86_642011cuda111extrascuptiincludenvperf_cuda_hosth)
 - [install_components/Linux_x86_64/20.11/cuda/11.1/targets/x86_64-linux/include/nvtx3/nvtxDetail/nvtxInit.h](#install_componentslinux_x86_642011cuda111targetsx86_64-linuxincludenvtx3nvtxdetailnvtxinith)
 - [install_components/Linux_x86_64/20.11/cuda/11.0/extras/CUPTI/include/nvperf_target.h](#install_componentslinux_x86_642011cuda110extrascuptiincludenvperf_targeth)
 - [install_components/Linux_x86_64/20.11/cuda/11.0/extras/CUPTI/include/nvperf_host.h](#install_componentslinux_x86_642011cuda110extrascuptiincludenvperf_hosth)
 - [install_components/Linux_x86_64/20.11/cuda/11.0/extras/CUPTI/include/nvperf_cuda_host.h](#install_componentslinux_x86_642011cuda110extrascuptiincludenvperf_cuda_hosth)
 - [install_components/Linux_x86_64/20.11/cuda/11.0/targets/x86_64-linux/include/nvtx3/nvtxDetail/nvtxInit.h](#install_componentslinux_x86_642011cuda110targetsx86_64-linuxincludenvtx3nvtxdetailnvtxinith)

### install_components/Linux_x86_64/20.11/comm_libs/openmpi/openmpi-3.1.5/share/openmpi/help-mpi-common-cuda.txt

```

{% raw %}
157 | [dlopen disabled]
159 |  --disable-dlopen flag), and therefore cannot utilize CUDA support.
163 | [dlopen failed]
{% endraw %}

```
### install_components/Linux_x86_64/20.11/comm_libs/openmpi4/openmpi-4.0.5/include/ucm/api/ucm.h

```cpp

{% raw %}
196 |     int                  dlopen_process_rpath;        /* Process RPATH section in dlopen hook */
459 |  * @brief Call the original implementation of @ref dlopen and all handlers
462 | void *ucm_dlopen(const char *filename, int flag);
{% endraw %}

```
### install_components/Linux_x86_64/20.11/comm_libs/openmpi4/openmpi-4.0.5/share/openmpi/help-mpi-common-cuda.txt

```

{% raw %}
157 | [dlopen disabled]
159 |  --disable-dlopen flag), and therefore cannot utilize CUDA support.
163 | [dlopen failed]
{% endraw %}

```
### install_components/Linux_x86_64/20.11/compilers/extras/qd/lib/libqd.la

```

{% raw %}
6 | # The name that we can dlopen(3).
35 | # Files to dlopen/dlpreopen
36 | dlopen=''
{% endraw %}

```
### install_components/Linux_x86_64/20.11/compilers/extras/qd/lib/libqdmod.la

```

{% raw %}
6 | # The name that we can dlopen(3).
35 | # Files to dlopen/dlpreopen
36 | dlopen=''
{% endraw %}

```
### install_components/Linux_x86_64/20.11/compilers/extras/qd/lib/libqd_f_main.la

```

{% raw %}
6 | # The name that we can dlopen(3).
35 | # Files to dlopen/dlpreopen
36 | dlopen=''
{% endraw %}

```
### install_components/Linux_x86_64/20.11/profilers/Nsight_Systems/target-linux-x64/nvtx/include/nvtx3/nvtxDetail/nvtxInit.h

```cpp

{% raw %}
66 | #define NVTX_DLLOPEN(x) dlopen(x, RTLD_LAZY)
222 |             /* For dlopen, if the filename contains a leading slash, then it is interpreted as a */
{% endraw %}

```
### install_components/Linux_x86_64/20.11/cuda/10.2/include/nvtx3/nvtxDetail/nvtxInit.h

```cpp

{% raw %}
66 | #define NVTX_DLLOPEN(x) dlopen(x, RTLD_LAZY)
222 |             /* For dlopen, if the filename contains a leading slash, then it is interpreted as a */
{% endraw %}

```
### install_components/Linux_x86_64/20.11/cuda/11.1/extras/CUPTI/include/nvperf_target.h

```cpp

{% raw %}
201 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
237 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
{% endraw %}

```
### install_components/Linux_x86_64/20.11/cuda/11.1/extras/CUPTI/include/nvperf_host.h

```cpp

{% raw %}
201 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
237 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
{% endraw %}

```
### install_components/Linux_x86_64/20.11/cuda/11.1/extras/CUPTI/include/nvperf_cuda_host.h

```cpp

{% raw %}
201 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
237 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
{% endraw %}

```
### install_components/Linux_x86_64/20.11/cuda/11.1/targets/x86_64-linux/include/nvtx3/nvtxDetail/nvtxInit.h

```cpp

{% raw %}
66 | #define NVTX_DLLOPEN(x) dlopen(x, RTLD_LAZY)
222 |             /* For dlopen, if the filename contains a leading slash, then it is interpreted as a */
{% endraw %}

```
### install_components/Linux_x86_64/20.11/cuda/11.0/extras/CUPTI/include/nvperf_target.h

```cpp

{% raw %}
201 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
237 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
{% endraw %}

```
### install_components/Linux_x86_64/20.11/cuda/11.0/extras/CUPTI/include/nvperf_host.h

```cpp

{% raw %}
201 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
237 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
{% endraw %}

```
### install_components/Linux_x86_64/20.11/cuda/11.0/extras/CUPTI/include/nvperf_cuda_host.h

```cpp

{% raw %}
201 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
237 |     /// ordered paths that will be searched with the LoadLibrary() or dlopen() call.
{% endraw %}

```
### install_components/Linux_x86_64/20.11/cuda/11.0/targets/x86_64-linux/include/nvtx3/nvtxDetail/nvtxInit.h

```cpp

{% raw %}
66 | #define NVTX_DLLOPEN(x) dlopen(x, RTLD_LAZY)
222 |             /* For dlopen, if the filename contains a leading slash, then it is interpreted as a */
{% endraw %}

```