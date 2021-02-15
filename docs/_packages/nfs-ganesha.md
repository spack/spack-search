---
name: "nfs-ganesha"
layout: package
next_package: hadoop
previous_package: 3proxy
languages: ['cmake', 'cpp']
---
## 3.1
14 / 834 files match

 - [src/SAL/nfs4_recovery.c](#srcsalnfs4_recoveryc)
 - [src/include/fsal_api.h](#srcincludefsal_apih)
 - [src/include/FSAL/fsal_init.h](#srcincludefsalfsal_inith)
 - [src/config_parsing/conf_url.c](#srcconfig_parsingconf_urlc)
 - [src/FSAL/fsal_manager.c](#srcfsalfsal_managerc)
 - [src/FSAL/FSAL_GPFS/main.c](#srcfsalfsal_gpfsmainc)
 - [src/FSAL/FSAL_VFS/vfs/main-c.in.cmake](#srcfsalfsal_vfsvfsmain-cincmake)
 - [src/FSAL/FSAL_VFS/xfs/main.c](#srcfsalfsal_vfsxfsmainc)
 - [src/FSAL/FSAL_VFS/panfs/main.c](#srcfsalfsal_vfspanfsmainc)
 - [src/FSAL/FSAL_MEM/mem_main.c](#srcfsalfsal_memmem_mainc)
 - [src/FSAL/FSAL_PSEUDO/main.c](#srcfsalfsal_pseudomainc)
 - [src/FSAL/Stackable_FSALs/FSAL_MDCACHE/mdcache_main.c](#srcfsalstackable_fsalsfsal_mdcachemdcache_mainc)
 - [src/FSAL/Stackable_FSALs/FSAL_NULL/main.c](#srcfsalstackable_fsalsfsal_nullmainc)
 - [src/tracing/README.md](#srctracingreadmemd)

### src/SAL/nfs4_recovery.c

```cpp

{% raw %}
695 | 	rados.dl = dlopen("libganesha_rados_recov.so",
{% endraw %}

```
### src/include/fsal_api.h

```cpp

{% raw %}
2779 | 	void *dl_handle;	/*< Handle to the dlopen()d shared
{% endraw %}

```
### src/include/FSAL/fsal_init.h

```cpp

{% raw %}
11 |  * before dlopen returns.  This is where you register your fsal.
{% endraw %}

```
### src/config_parsing/conf_url.c

```cpp

{% raw %}
83 | 	rados_urls.dl = dlopen("libganesha_rados_urls.so",
{% endraw %}

```
### src/FSAL/fsal_manager.c

```cpp

{% raw %}
88 | 	loading,	/*< In dlopen(). set by load_fsal() just prior */
170 |  * The dlopen() will trigger a .init constructor which will do the
185 |  * @retval other general dlopen errors are possible, all of them bad
225 | 	dl = dlopen(path, RTLD_NOW | RTLD_LOCAL | RTLD_DEEPBIND);
227 | 	dl = dlopen(path, RTLD_NOW | RTLD_LOCAL);
234 | 			 "Could not dlopen module: %s Error: %s. You might want to install the nfs-ganesha-%s package",
362 |  *  + from the shared object's 'fsal_init' function if dlopen does not support
{% endraw %}

```
### src/FSAL/FSAL_GPFS/main.c

```cpp

{% raw %}
211 |  *  Called by dlopen() to register the module
{% endraw %}

```
### src/FSAL/FSAL_VFS/vfs/main-c.in.cmake

```cmake

{% raw %}
203 |  * Called by dlopen() to register the module
{% endraw %}

```
### src/FSAL/FSAL_VFS/xfs/main.c

```cpp

{% raw %}
194 |  * Called by dlopen() to register the module
{% endraw %}

```
### src/FSAL/FSAL_VFS/panfs/main.c

```cpp

{% raw %}
157 |  * Called by dlopen() to register the module
{% endraw %}

```
### src/FSAL/FSAL_MEM/mem_main.c

```cpp

{% raw %}
239 |  * Called by dlopen() to register the module
{% endraw %}

```
### src/FSAL/FSAL_PSEUDO/main.c

```cpp

{% raw %}
95 |  * Called by dlopen() to register the module
{% endraw %}

```
### src/FSAL/Stackable_FSALs/FSAL_MDCACHE/mdcache_main.c

```cpp

{% raw %}
306 |  * Called by dlopen() to register the module
{% endraw %}

```
### src/FSAL/Stackable_FSALs/FSAL_NULL/main.c

```cpp

{% raw %}
126 |  * Called by dlopen() to register the module
{% endraw %}

```
### src/tracing/README.md

```

{% raw %}
44 | loading (dlopen) the modul  This would be useful for production environments
{% endraw %}

```