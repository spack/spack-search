---
name: "bdw-gc"
layout: package
next_package: bedtools2
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
218 | #   ifdef RTLD_NEXT
219 |       dl_handle = RTLD_NEXT;
220 | #   else
221 |       dl_handle = dlopen("libpthread.so.0", RTLD_LAZY);
222 |       if (NULL == dl_handle) {
223 |         dl_handle = dlopen("libpthread.so", RTLD_LAZY); /* without ".0" */
224 |       }
225 |       if (NULL == dl_handle) ABORT("Couldn't open libpthread");
{% endraw %}

```
### dyn_load.c

```c

{% raw %}
181 |         /* to use its value in the set of original object files loaded  */
182 |         /* at program startup.                                          */
183 |         if( dynStructureAddr == 0 ) {
184 |           void* startupSyms = dlopen(0, RTLD_LAZY);
185 |           dynStructureAddr = (ElfW(Dyn)*)(word)dlsym(startupSyms, "_DYNAMIC");
186 |         }
{% endraw %}

```
### gc_dlopen.c

```c

{% raw %}
40 | /* library initialization code allocates substantial amounts of GC'ed   */
41 | /* memory.                                                              */
42 | #ifndef USE_PROC_FOR_LIBRARIES
43 |   static void disable_gc_for_dlopen(void)
44 |   {
45 |     DCL_LOCK_STATE;
60 | #ifdef GC_USE_LD_WRAP
61 | # define WRAP_DLFUNC(f) __wrap_##f
62 | # define REAL_DLFUNC(f) __real_##f
63 |   void * REAL_DLFUNC(dlopen)(const char *, int);
64 | #else
65 | # define WRAP_DLFUNC(f) GC_##f
66 | # define REAL_DLFUNC(f) f
67 | #endif
68 | 
69 | GC_API void * WRAP_DLFUNC(dlopen)(const char *path, int mode)
70 | {
71 |   void * result;
73 | # ifndef USE_PROC_FOR_LIBRARIES
74 |     /* Disable collections.  This solution risks heap growth (or,       */
75 |     /* even, heap overflow) but there seems no better solutions.        */
76 |     disable_gc_for_dlopen();
77 | # endif
78 |   result = REAL_DLFUNC(dlopen)(path, mode);
79 | # ifndef USE_PROC_FOR_LIBRARIES
80 |     GC_enable(); /* undoes disable_gc_for_dlopen */
81 | # endif
82 |   return(result);
86 |   /* Define GC_ function as an alias for the plain one, which will be   */
87 |   /* intercepted.  This allows files which include gc.h, and hence      */
88 |   /* generate references to the GC_ symbol, to see the right symbol.    */
89 |   GC_API void *GC_dlopen(const char *path, int mode)
90 |   {
91 |     return dlopen(path, mode);
92 |   }
93 | #endif /* GC_USE_LD_WRAP */
{% endraw %}

```
### include/gc_pthread_redirects.h

```c

{% raw %}
48 | # endif
49 | 
50 | # ifndef GC_NO_DLOPEN
51 |     GC_API void *GC_dlopen(const char * /* path */, int /* mode */);
52 | # endif /* !GC_NO_DLOPEN */
53 | 
{% endraw %}

```
### tests/test.c

```c

{% raw %}
2369 |       UNTESTED(GC_stop_world_external);
2370 |       UNTESTED(GC_start_world_external);
2371 | #     ifndef GC_NO_DLOPEN
2372 |         UNTESTED(GC_dlopen);
2373 | #     endif
2374 | #     ifndef GC_NO_PTHREAD_CANCEL
{% endraw %}

```
### tools/threadlibs.c

```c

{% raw %}
21 | int main(void)
22 | {
23 | #   if defined(GC_USE_LD_WRAP)
24 |         printf("-Wl,--wrap -Wl,dlopen "
25 |                "-Wl,--wrap -Wl,pthread_create -Wl,--wrap -Wl,pthread_join "
26 |                "-Wl,--wrap -Wl,pthread_detach -Wl,--wrap -Wl,pthread_sigmask "
{% endraw %}

```