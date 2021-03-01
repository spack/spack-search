---
name: "mono"
layout: package
next_package: multiverso
previous_package: mivisionx
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.10.1.57
46 / 82201 files match, 7 filtered matches.

 - [mono/utils/mono-dl-posix.c](#monoutilsmono-dl-posixc)
 - [mono/mini/mini-darwin.c](#monominimini-darwinc)
 - [mono/eglib/gmodule-unix.c](#monoeglibgmodule-unixc)
 - [libgc/threadlibs.c](#libgcthreadlibsc)
 - [libgc/dyn_load.c](#libgcdyn_loadc)
 - [libgc/gc_dlopen.c](#libgcgc_dlopenc)
 - [libgc/include/gc_pthread_redirects.h](#libgcincludegc_pthread_redirectsh)

### mono/utils/mono-dl-posix.c

```c

{% raw %}
65 | 	if (!file)
66 | 		return NULL;
67 | #endif
68 | 	return dlopen (file, flags);
69 | }
70 | 
{% endraw %}

```
### mono/mini/mini-darwin.c

```c

{% raw %}
70 | /* This is #define'd by Boehm GC to _GC_dlopen. */
71 | #undef dlopen
72 | 
73 | void* dlopen(const char* path, int mode);
74 | 
75 | void
84 | 	 */
85 | #if defined (__APPLE__) && (defined (__i386__) || defined (__x86_64__))
86 | 	{
87 | 		void *handle = dlopen ("/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation", RTLD_LAZY);
88 | 		if (handle == NULL)
89 | 			return;
{% endraw %}

```
### mono/eglib/gmodule-unix.c

```c

{% raw %}
56 | 	if ((flags & G_MODULE_BIND_LOCAL) != 0)
57 | 		f |= RTLD_LOCAL;
58 | 
59 | 	handle = dlopen (file, f);
60 | 	if (handle == NULL)
61 | 		return NULL;
{% endraw %}

```
### libgc/threadlibs.c

```c

{% raw %}
4 | int main()
5 | {
6 | #   if defined(GC_USE_LD_WRAP)
7 | 	printf("-Wl,--wrap -Wl,dlopen "
8 | 	       "-Wl,--wrap -Wl,pthread_create -Wl,--wrap -Wl,pthread_join "
9 | 	       "-Wl,--wrap -Wl,pthread_detach "
{% endraw %}

```
### libgc/dyn_load.c

```c

{% raw %}
36 | 
37 | /* BTL: avoid circular redefinition of dlopen if GC_SOLARIS_THREADS defined */
38 | # if (defined(GC_PTHREADS) || defined(GC_SOLARIS_THREADS)) \
39 |       && defined(dlopen) && !defined(GC_USE_LD_WRAP)
40 |     /* To support threads in Solaris, gc.h interposes on dlopen by       */
41 |     /* defining "dlopen" to be "GC_dlopen", which is implemented below.  */
149 | 	/* to use its value in the set of original object files loaded	*/
150 | 	/* at program startup.						*/
151 | 	if( dynStructureAddr == 0 ) {
152 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
153 | 	  dynStructureAddr = (ElfW(Dyn)*)dlsym(startupSyms, "_DYNAMIC");
154 | 		}
224 | /* Add dynamic library data sections to the root set.		*/
225 | # if !defined(PCR) && !defined(GC_SOLARIS_THREADS) && defined(THREADS)
226 | #   ifndef SRC_M3
227 | 	--> fix mutual exclusion with dlopen
228 | #   endif  /* We assume M3 programs don't call dlopen for now */
229 | # endif
{% endraw %}

```
### libgc/gc_dlopen.c

```c

{% raw %}
45 |   /* calls in either a multithreaded environment, or if the library	*/
46 |   /* initialization code allocates substantial amounts of GC'ed memory.	*/
47 |   /* But I don't know of a better solution.				*/
48 |   static void disable_gc_for_dlopen()
49 |   {
50 |     LOCK();
62 | #include <dlfcn.h>
63 | 
64 | #ifdef GC_USE_LD_WRAP
65 |   void * __wrap_dlopen(const char *path, int mode)
66 | #else
67 |   void * GC_dlopen(path, mode)
68 |   GC_CONST char * path;
69 |   int mode;
72 |     void * result;
73 |     
74 | #   ifndef USE_PROC_FOR_LIBRARIES
75 |       disable_gc_for_dlopen();
76 | #   endif
77 | #   ifdef GC_USE_LD_WRAP
78 |       result = (void *)__real_dlopen(path, mode);
79 | #   else
80 |       result = dlopen(path, mode);
81 | #   endif
82 | #   ifndef USE_PROC_FOR_LIBRARIES
83 |       GC_enable(); /* undoes disable_gc_for_dlopen */
84 | #   endif
85 |     return(result);
{% endraw %}

```
### libgc/include/gc_pthread_redirects.h

```c

{% raw %}
20 |   int GC_thr_join(thread_t wait_for, thread_t *departed, void **status);
21 |   int GC_thr_suspend(thread_t target_thread);
22 |   int GC_thr_continue(thread_t target_thread);
23 |   void * GC_dlopen(const char *path, int mode);
24 | # define thr_create GC_thr_create
25 | # define thr_join GC_thr_join
{% endraw %}

```