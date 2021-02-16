---
name: "portcullis"
layout: package
next_package: r-stringi
previous_package: sandbox
languages: ['c']
---
## 1.1.2
21 / 11496 files match, 5 filtered matches.

 - [deps/boost/tools/build/src/engine/boehm_gc/pthread_support.c](#depsboosttoolsbuildsrcengineboehm_gcpthread_supportc)
 - [deps/boost/tools/build/src/engine/boehm_gc/threadlibs.c](#depsboosttoolsbuildsrcengineboehm_gcthreadlibsc)
 - [deps/boost/tools/build/src/engine/boehm_gc/dyn_load.c](#depsboosttoolsbuildsrcengineboehm_gcdyn_loadc)
 - [deps/boost/tools/build/src/engine/boehm_gc/gc_dlopen.c](#depsboosttoolsbuildsrcengineboehm_gcgc_dlopenc)
 - [deps/htslib-1.3/plugin.c](#depshtslib-13pluginc)

### deps/boost/tools/build/src/engine/boehm_gc/pthread_support.c

```c

{% raw %}
187 |       dl_handle = dlopen(libpthread_name, RTLD_LAZY);
193 |         dl_handle = dlopen(namebuf, RTLD_LAZY);
{% endraw %}

```
### deps/boost/tools/build/src/engine/boehm_gc/threadlibs.c

```c

{% raw %}
7 | 	printf("-Wl,--wrap -Wl,dlopen "
{% endraw %}

```
### deps/boost/tools/build/src/engine/boehm_gc/dyn_load.c

```c

{% raw %}
40 |       && defined(dlopen) && !defined(GC_USE_LD_WRAP)
142 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
176 | 	--> fix mutual exclusion with dlopen
{% endraw %}

```
### deps/boost/tools/build/src/engine/boehm_gc/gc_dlopen.c

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
### deps/htslib-1.3/plugin.c

```c

{% raw %}
139 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```