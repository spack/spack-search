---
name: "imagemagick"
layout: package
next_package: ipcalc
previous_package: hwloc
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.0.8-7
6 / 2378 files match, 3 filtered matches.

 - [MagickCore/opencl.c](#magickcoreopenclc)
 - [MagickCore/nt-base.c](#magickcorent-basec)
 - [MagickCore/module.c](#magickcoremodulec)

### MagickCore/opencl.c

```c

{% raw %}
2446 | #ifdef MAGICKCORE_WINDOWS_SUPPORT
2447 |     return (void *) GetProcAddress((HMODULE)library,functionName);
2448 | #else
2449 |     return (void *) dlsym(library,functionName);
2450 | #endif
2451 | }
{% endraw %}

```
### MagickCore/nt-base.c

```c

{% raw %}
1548 |     }
1549 |   (void) memset((void *) &nt_ghost_info,0,sizeof(NTGhostInfo));
1550 |   nt_ghost_info.delete_instance=(void (MagickDLLCall *)(gs_main_instance *)) (
1551 |     lt_dlsym(ghost_handle,"gsapi_delete_instance"));
1552 |   nt_ghost_info.new_instance=(int (MagickDLLCall *)(gs_main_instance **,
1553 |     void *)) (lt_dlsym(ghost_handle,"gsapi_new_instance"));
1554 |   nt_ghost_info.has_instance=MagickFalse;
1555 |   (void) memset((void *) &ghost_info,0,sizeof(GhostInfo));
1556 |   ghost_info.delete_instance=NTGhostscriptDeleteInstance;
1557 |   ghost_info.exit=(int (MagickDLLCall *)(gs_main_instance*))
1558 |     lt_dlsym(ghost_handle,"gsapi_exit");
1559 |   ghost_info.init_with_args=(int (MagickDLLCall *)(gs_main_instance *,int,
1560 |     char **)) (lt_dlsym(ghost_handle,"gsapi_init_with_args"));
1561 |   ghost_info.new_instance=NTGhostscriptNewInstance;
1562 |   ghost_info.run_string=(int (MagickDLLCall *)(gs_main_instance *,const char *,
1563 |     int,int *)) (lt_dlsym(ghost_handle,"gsapi_run_string"));
1564 |   ghost_info.set_stdio=(int (MagickDLLCall *)(gs_main_instance *,int(
1565 |     MagickDLLCall *)(void *,char *,int),int(MagickDLLCall *)(void *,
1566 |     const char *,int),int(MagickDLLCall *)(void *,const char *,int)))
1567 |     (lt_dlsym(ghost_handle,"gsapi_set_stdio"));
1568 |   ghost_info.revision=(int (MagickDLLCall *)(gsapi_revision_t *,int)) (
1569 |     lt_dlsym(ghost_handle,"gsapi_revision"));
1570 |   UnlockSemaphoreInfo(ghost_semaphore);
1571 |   return(NTGhostscriptHasValidHandle());
{% endraw %}

```
### MagickCore/module.c

```c

{% raw %}
1007 |     Execute the module.
1008 |   */
1009 |   ClearMagickException(exception);
1010 |   image_filter=(ImageFilterHandler *) lt_dlsym(handle,name);
1011 |   if (image_filter == (ImageFilterHandler *) NULL)
1012 |     (void) ThrowMagickException(exception,GetMagickModule(),ModuleError,
1286 |     Define RegisterFORMATImage method.
1287 |   */
1288 |   TagToModuleName(module_name,"Register%sImage",name);
1289 |   module_info->register_module=(size_t (*)(void)) lt_dlsym(handle,name);
1290 |   if (module_info->register_module == (size_t (*)(void)) NULL)
1291 |     {
1300 |     Define UnregisterFORMATImage method.
1301 |   */
1302 |   TagToModuleName(module_name,"Unregister%sImage",name);
1303 |   module_info->unregister_module=(void (*)(void)) lt_dlsym(handle,name);
1304 |   if (module_info->unregister_module == (void (*)(void)) NULL)
1305 |     {
{% endraw %}

```