---
name: "nvhpc"
layout: package
next_package: nwchem
previous_package: ntirpc
languages: ['c']
---
## 20.11
16 / 18177 files match, 1 filtered matches.

 - [install_components/Linux_x86_64/20.11/comm_libs/openmpi4/openmpi-4.0.5/include/ucm/api/ucm.h](#install_componentslinux_x86_642011comm_libsopenmpi4openmpi-405includeucmapiucmh)

### install_components/Linux_x86_64/20.11/comm_libs/openmpi4/openmpi-4.0.5/include/ucm/api/ucm.h

```c

{% raw %}
193 |     int                  enable_cuda_reloc;           /* Enable installing CUDA relocations */
194 |     int                  enable_dynamic_mmap_thresh;  /* Enable adaptive mmap threshold */
195 |     size_t               alloc_alignment;             /* Alignment for memory allocations */
196 |     int                  dlopen_process_rpath;        /* Process RPATH section in dlopen hook */
197 | } ucm_global_config_t;
198 | 
459 |  * @brief Call the original implementation of @ref dlopen and all handlers
460 |  * associated with it.
461 |  */
462 | void *ucm_dlopen(const char *filename, int flag);
463 | 
464 | 
{% endraw %}

```