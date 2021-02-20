---
name: "raft"
layout: package
next_package: rccl
previous_package: r-rsqlite
languages: ['c']
---
## develop
1 / 112 files match, 1 filtered matches.

 - [src/common/inc/cuda_drvapi_dynlink.c](#srccommoninccuda_drvapi_dynlinkc)

### src/common/inc/cuda_drvapi_dynlink.c

```c

{% raw %}
253 | 
254 |     if (*pInstance == NULL)
255 |     {
256 |         printf("dlopen \"%s\" failed!\n", __CudaLibName);
257 |         return CUDA_ERROR_UNKNOWN;
258 |     }
{% endraw %}

```