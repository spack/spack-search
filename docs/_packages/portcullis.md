---
name: "portcullis"
layout: package
next_package: postgresql
previous_package: poppler
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
### deps/boost/tools/build/src/engine/boehm_gc/threadlibs.c

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
### deps/boost/tools/build/src/engine/boehm_gc/dyn_load.c

```c

{% raw %}
37 | 
38 | /* BTL: avoid circular redefinition of dlopen if GC_SOLARIS_THREADS defined */
39 | # if (defined(GC_PTHREADS) || defined(GC_SOLARIS_THREADS)) \
40 |       && defined(dlopen) && !defined(GC_USE_LD_WRAP)
41 |     /* To support threads in Solaris, gc.h interposes on dlopen by       */
42 |     /* defining "dlopen" to be "GC_dlopen", which is implemented below.  */
139 | 	/* to use its value in the set of original object files loaded	*/
140 | 	/* at program startup.						*/
141 | 	if( dynStructureAddr == 0 ) {
142 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
143 | 	  dynStructureAddr = (ElfW(Dyn)*)dlsym(startupSyms, "_DYNAMIC");
144 | 		}
173 | # if defined(SOLARISDL)
174 | /* Add dynamic library data sections to the root set.		*/
175 | # if !defined(PCR) && !defined(GC_SOLARIS_THREADS) && defined(THREADS)
176 | 	--> fix mutual exclusion with dlopen
177 | # endif
178 | 
{% endraw %}

```
### deps/boost/tools/build/src/engine/boehm_gc/gc_dlopen.c

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
### deps/htslib-1.3/plugin.c

```c

{% raw %}
136 | 
137 | void *load_plugin(void **pluginp, const char *filename, const char *symbol)
138 | {
139 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
140 |     if (lib == NULL) goto error;
141 | 
{% endraw %}

```