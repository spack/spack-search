---
name: "boost"
layout: package
next_package: kbd
previous_package: gmake
languages: ['python', 'c']
---
## 1.49.0
21 / 38128 files match, 5 filtered matches.

 - [libs/mpi/build/__init__.py](#libsmpibuild__init__py)
 - [tools/build/v2/engine/boehm_gc/pthread_support.c](#toolsbuildv2engineboehm_gcpthread_supportc)
 - [tools/build/v2/engine/boehm_gc/threadlibs.c](#toolsbuildv2engineboehm_gcthreadlibsc)
 - [tools/build/v2/engine/boehm_gc/dyn_load.c](#toolsbuildv2engineboehm_gcdyn_loadc)
 - [tools/build/v2/engine/boehm_gc/gc_dlopen.c](#toolsbuildv2engineboehm_gcgc_dlopenc)

### libs/mpi/build/__init__.py

```python

{% raw %}
3 |     flags = sys.getdlopenflags()
4 |     sys.setdlopenflags(dl.RTLD_NOW|dl.RTLD_GLOBAL)
6 |     sys.setdlopenflags(flags)
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/pthread_support.c

```c

{% raw %}
187 |       dl_handle = dlopen(libpthread_name, RTLD_LAZY);
193 |         dl_handle = dlopen(namebuf, RTLD_LAZY);
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/threadlibs.c

```c

{% raw %}
7 | 	printf("-Wl,--wrap -Wl,dlopen "
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/dyn_load.c

```c

{% raw %}
40 |       && defined(dlopen) && !defined(GC_USE_LD_WRAP)
138 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
172 | 	--> fix mutual exclusion with dlopen
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/gc_dlopen.c

```c

{% raw %}
48 |   static void disable_gc_for_dlopen()
65 |   void * __wrap_dlopen(const char *path, int mode)
67 |   void * GC_dlopen(const char *path, int mode)
73 |       disable_gc_for_dlopen();
76 |       result = (void *)__real_dlopen(path, mode);
78 |       result = dlopen(path, mode);
81 |       GC_enable(); /* undoes disable_gc_for_dlopen */
{% endraw %}

```