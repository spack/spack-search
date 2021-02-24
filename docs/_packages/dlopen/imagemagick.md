---
name: "imagemagick"
layout: package
next_package: bear
previous_package: brltty
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.0.8-7
8 / 2378 files match, 3 filtered matches.

 - [MagickCore/opencl.c](#magickcoreopenclc)
 - [MagickCore/nt-base.c](#magickcorent-basec)
 - [MagickCore/module.c](#magickcoremodulec)

### MagickCore/opencl.c

```c

{% raw %}
2459 | #ifdef MAGICKCORE_WINDOWS_SUPPORT
2460 |   openCL_library->library=(void *)LoadLibraryA("OpenCL.dll");
2461 | #else
2462 |   openCL_library->library=(void *)dlopen("libOpenCL.so", RTLD_NOW);
2463 | #endif
2464 | #define BIND(X) \
{% endraw %}

```
### MagickCore/nt-base.c

```c

{% raw %}
1540 |       UnlockSemaphoreInfo(ghost_semaphore);
1541 |       return(FALSE);
1542 |     }
1543 |   ghost_handle=lt_dlopen(path);
1544 |   if (ghost_handle == (void *) NULL)
1545 |     {
{% endraw %}

```
### MagickCore/module.c

```c

{% raw %}
987 |   /*
988 |     Open the module.
989 |   */
990 |   handle=(ModuleHandle) lt_dlopen(path);
991 |   if (handle == (ModuleHandle) NULL)
992 |     {
1268 |   */
1269 |   (void) LogMagickEvent(ModuleEvent,GetMagickModule(),
1270 |     "Opening module at path \"%s\"",path);
1271 |   handle=(ModuleHandle) lt_dlopen(path);
1272 |   if (handle == (ModuleHandle) NULL)
1273 |     {
{% endraw %}

```