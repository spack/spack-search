---
name: "bdw-gc"
layout: package
next_package: berkeley-db
previous_package: bcftools
languages: ['c']
---
## 8.0.0
18 / 179 files match, 6 filtered matches.

 - [pthread_support.c](#pthread_supportc)
 - [dyn_load.c](#dyn_loadc)
 - [gc_dlopen.c](#gc_dlopenc)
 - [include/gc_pthread_redirects.h](#includegc_pthread_redirectsh)
 - [tests/test.c](#teststestc)
 - [tools/threadlibs.c](#toolsthreadlibsc)

### pthread_support.c

```c

{% raw %}
221 |       dl_handle = dlopen("libpthread.so.0", RTLD_LAZY);
223 |         dl_handle = dlopen("libpthread.so", RTLD_LAZY); /* without ".0" */
{% endraw %}

```
### dyn_load.c

```c

{% raw %}
184 |           void* startupSyms = dlopen(0, RTLD_LAZY);
{% endraw %}

```
### gc_dlopen.c

```c

{% raw %}
43 |   static void disable_gc_for_dlopen(void)
63 |   void * REAL_DLFUNC(dlopen)(const char *, int);
69 | GC_API void * WRAP_DLFUNC(dlopen)(const char *path, int mode)
76 |     disable_gc_for_dlopen();
78 |   result = REAL_DLFUNC(dlopen)(path, mode);
80 |     GC_enable(); /* undoes disable_gc_for_dlopen */
89 |   GC_API void *GC_dlopen(const char *path, int mode)
91 |     return dlopen(path, mode);
{% endraw %}

```
### include/gc_pthread_redirects.h

```c

{% raw %}
51 |     GC_API void *GC_dlopen(const char * /* path */, int /* mode */);
{% endraw %}

```
### tests/test.c

```c

{% raw %}
2372 |         UNTESTED(GC_dlopen);
{% endraw %}

```
### tools/threadlibs.c

```c

{% raw %}
24 |         printf("-Wl,--wrap -Wl,dlopen "
{% endraw %}

```