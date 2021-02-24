---
name: "boost"
layout: package
next_package: curl
previous_package: libiberty
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c', 'python']
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
1 | if sys.platform == 'linux2':
2 |     import DLFCN as dl
3 |     flags = sys.getdlopenflags()
4 |     sys.setdlopenflags(dl.RTLD_NOW|dl.RTLD_GLOBAL)
5 |     import mpi
6 |     sys.setdlopenflags(flags)
7 | else:
8 |     import mpi
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/pthread_support.c

```c

{% raw %}
184 | #   ifdef RTLD_NEXT
185 |       dl_handle = RTLD_NEXT;
186 | #   else
187 |       dl_handle = dlopen(libpthread_name, RTLD_LAZY);
188 |       if (NULL == dl_handle) {
189 |         while (isdigit(libpthread_name[len-1])) --len;
190 |         if (libpthread_name[len-1] == '.') --len;
191 |         memcpy(namebuf, libpthread_name, len);
192 |         namebuf[len] = '\0';
193 |         dl_handle = dlopen(namebuf, RTLD_LAZY);
194 |       }
195 |       if (NULL == dl_handle) ABORT("Couldn't open libpthread\n");
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/threadlibs.c

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
### tools/build/v2/engine/boehm_gc/dyn_load.c

```c

{% raw %}
37 | 
38 | /* BTL: avoid circular redefinition of dlopen if GC_SOLARIS_THREADS defined */
39 | # if (defined(GC_PTHREADS) || defined(GC_SOLARIS_THREADS)) \
40 |       && defined(dlopen) && !defined(GC_USE_LD_WRAP)
41 |     /* To support threads in Solaris, gc.h interposes on dlopen by       */
42 |     /* defining "dlopen" to be "GC_dlopen", which is implemented below.  */
135 | 	/* to use its value in the set of original object files loaded	*/
136 | 	/* at program startup.						*/
137 | 	if( dynStructureAddr == 0 ) {
138 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
139 | 	  dynStructureAddr = (ElfW(Dyn)*)dlsym(startupSyms, "_DYNAMIC");
140 | 		}
169 | # if defined(SOLARISDL)
170 | /* Add dynamic library data sections to the root set.		*/
171 | # if !defined(PCR) && !defined(GC_SOLARIS_THREADS) && defined(THREADS)
172 | 	--> fix mutual exclusion with dlopen
173 | # endif
174 | 
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/gc_dlopen.c

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
67 |   void * GC_dlopen(const char *path, int mode)
68 | #endif
69 | {
70 |     void * result;
71 |     
72 | #   ifndef USE_PROC_FOR_LIBRARIES
73 |       disable_gc_for_dlopen();
74 | #   endif
75 | #   ifdef GC_USE_LD_WRAP
76 |       result = (void *)__real_dlopen(path, mode);
77 | #   else
78 |       result = dlopen(path, mode);
79 | #   endif
80 | #   ifndef USE_PROC_FOR_LIBRARIES
81 |       GC_enable(); /* undoes disable_gc_for_dlopen */
82 | #   endif
83 |     return(result);
{% endraw %}

```