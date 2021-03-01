---
name: "gcc"
layout: package
next_package: gdb
previous_package: gawk
library_name: dlopen
matches: ['dlsym', 'dlopen', 'dlmopen']
languages: ['cpp', 'java', 'c']
---
## 6.1.0
112 / 94447 files match, 37 filtered matches.

 - [gcc/plugin.c](#gccpluginc)
 - [gcc/config/rs6000/aix.h](#gccconfigrs6000aixh)
 - [gcc/jit/jit-playback.h](#gccjitjit-playbackh)
 - [gcc/jit/jit-playback.c](#gccjitjit-playbackc)
 - [gcc/testsuite/c-c++-common/tsan/tsan_barrier.h](#gcctestsuitec-c++-commontsantsan_barrierh)
 - [gcc/testsuite/g++.dg/asan/dlclose-test-1-so.cc](#gcctestsuiteg++dgasandlclose-test-1-socc)
 - [gcc/testsuite/g++.dg/tsan/tsan_barrier.h](#gcctestsuiteg++dgtsantsan_barrierh)
 - [gcc/testsuite/jit.dg/verify-dynamic-library.c](#gcctestsuitejitdgverify-dynamic-libraryc)
 - [libjava/prims.cc](#libjavaprimscc)
 - [libjava/classpath/native/jni/midi-dssi/gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider.c](#libjavaclasspathnativejnimidi-dssignu_javax_sound_midi_dssi_dssimidideviceproviderc)
 - [libjava/classpath/include/gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider.h](#libjavaclasspathincludegnu_javax_sound_midi_dssi_dssimidideviceproviderh)
 - [libjava/classpath/tools/toolwrapper.c](#libjavaclasspathtoolstoolwrapperc)
 - [libjava/classpath/gnu/javax/sound/midi/dssi/DSSIMidiDeviceProvider.java](#libjavaclasspathgnujavaxsoundmididssidssimidideviceproviderjava)
 - [libjava/classpath/gnu/javax/sound/midi/dssi/DSSISynthesizer.java](#libjavaclasspathgnujavaxsoundmididssidssisynthesizerjava)
 - [libjava/libltdl/ltdl.h](#libjavalibltdlltdlh)
 - [libjava/libltdl/ltdl.c](#libjavalibltdlltdlc)
 - [libjava/java/lang/natRuntime.cc](#libjavajavalangnatruntimecc)
 - [libjava/java/net/natVMURLConnection.cc](#libjavajavanetnatvmurlconnectioncc)
 - [libjava/gnu/gcj/runtime/natSharedLibLoader.cc](#libjavagnugcjruntimenatsharedlibloadercc)
 - [libjava/gnu/javax/sound/midi/dssi/DSSIMidiDeviceProvider.h](#libjavagnujavaxsoundmididssidssimidideviceproviderh)
 - [libstdc++-v3/testsuite/ext/mt_allocator/22309_thread.cc](#libstdc++-v3testsuiteextmt_allocator22309_threadcc)
 - [libstdc++-v3/testsuite/18_support/bad_exception/23591_thread-1.c](#libstdc++-v3testsuite18_supportbad_exception23591_thread-1c)
 - [boehm-gc/threadlibs.c](#boehm-gcthreadlibsc)
 - [boehm-gc/dyn_load.c](#boehm-gcdyn_loadc)
 - [boehm-gc/gc_dlopen.c](#boehm-gcgc_dlopenc)
 - [boehm-gc/include/gc_pthread_redirects.h](#boehm-gcincludegc_pthread_redirectsh)
 - [intl/libgnuintl.h](#intllibgnuintlh)
 - [libvtv/vtv_utils.h](#libvtvvtv_utilsh)
 - [libvtv/testsuite/other-tests/dlopen.cc](#libvtvtestsuiteother-testsdlopencc)
 - [libvtv/testsuite/other-tests/dlopen_mt.cc](#libvtvtestsuiteother-testsdlopen_mtcc)
 - [libcilkrts/runtime/sysdep-unix.c](#libcilkrtsruntimesysdep-unixc)
 - [libsanitizer/sanitizer_common/sanitizer_linux.h](#libsanitizersanitizer_commonsanitizer_linuxh)
 - [libsanitizer/sanitizer_common/sanitizer_unwind_linux_libcdep.cc](#libsanitizersanitizer_commonsanitizer_unwind_linux_libcdepcc)
 - [libgcc/config/darwin-crt3.c](#libgccconfigdarwin-crt3c)
 - [lto-plugin/lto-symtab.c](#lto-pluginlto-symtabc)
 - [libgomp/target.c](#libgomptargetc)
 - [libgomp/plugin/plugin-hsa.c](#libgomppluginplugin-hsac)

### gcc/plugin.c

```c

{% raw %}
572 |   /* We use RTLD_NOW to accelerate binding and detect any mismatch
573 |      between the API expected by the plugin and the GCC API; we use
574 |      RTLD_GLOBAL which is useful to plugins which themselves call
575 |      dlopen.  */
576 |   dl_handle = dlopen (plugin->full_name, RTLD_NOW | RTLD_GLOBAL);
577 |   if (!dl_handle)
578 |     {
{% endraw %}

```
### gcc/config/rs6000/aix.h

```c

{% raw %}
67 |    only invoked once in the case of multiple dependencies on a library.
68 | 
69 |    -binitfini is still used in parallel to this solution.
70 |    This handles the case where a library is loaded through dlopen(), and also
71 |    handles the option -blazy.
72 | */
{% endraw %}

```
### gcc/jit/jit-playback.h

```c

{% raw %}
283 |   add_multilib_driver_arguments (vec <char *> *argvec);
284 | 
285 |   result *
286 |   dlopen_built_dso ();
287 | 
288 |  private:
{% endraw %}

```
### gcc/jit/jit-playback.c

```c

{% raw %}
1727 | 
1728 |        For an in-memory compile we have the playback::compile_to_memory
1729 |        subclass; "postprocess" will convert the .s file to a .so DSO,
1730 |        and load it in memory (via dlopen), wrapping the result up as
1731 |        a jit::result and returning it.
1732 | 
1836 | /*  Implementation of the playback::context::process vfunc for compiling
1837 |     to memory.
1838 | 
1839 |     Convert the .s file to a .so DSO, and load it in memory (via dlopen),
1840 |     wrapping the result up as a jit::result and returning it.  */
1841 | 
1846 |   convert_to_dso (ctxt_progname);
1847 |   if (errors_occurred ())
1848 |     return;
1849 |   m_result = dlopen_built_dso ();
1850 | }
1851 | 
2534 | 
2535 | result *
2536 | playback::context::
2537 | dlopen_built_dso ()
2538 | {
2539 |   JIT_LOG_SCOPE (get_logger ());
2545 |   /* Clear any existing error.  */
2546 |   dlerror ();
2547 | 
2548 |   handle = dlopen (m_tempdir->get_path_so_file (),
2549 | 		   RTLD_NOW | RTLD_LOCAL);
2550 |   if ((error = dlerror()) != NULL)  {
{% endraw %}

```
### gcc/testsuite/c-c++-common/tsan/tsan_barrier.h

```c

{% raw %}
6 | static
7 | void barrier_init (pthread_barrier_t *barrier, unsigned count)
8 | {
9 |   void *h = dlopen ("libpthread.so.0", RTLD_LAZY);
10 |   barrier_wait = (__typeof (pthread_barrier_wait) *)
11 | 	 	 dlsym (h, "pthread_barrier_wait");
{% endraw %}

```
### gcc/testsuite/g++.dg/asan/dlclose-test-1-so.cc

```cpp

{% raw %}
22 | }
23 | 
24 | __attribute__((constructor))
25 | void at_dlopen() {
26 |   printf("%s: I am being dlopened\n", __FILE__);
27 | }
28 | __attribute__((destructor))
{% endraw %}

```
### gcc/testsuite/g++.dg/tsan/tsan_barrier.h

```c

{% raw %}
6 | static
7 | void barrier_init (pthread_barrier_t *barrier, unsigned count)
8 | {
9 |   void *h = dlopen ("libpthread.so.0", RTLD_LAZY);
10 |   barrier_wait = (__typeof (pthread_barrier_wait) *)
11 | 	 	 dlsym (h, "pthread_barrier_wait");
{% endraw %}

```
### gcc/testsuite/jit.dg/verify-dynamic-library.c

```c

{% raw %}
10 |   void (*hello_world) (const char *name);
11 |   char *error;
12 | 
13 |   handle = dlopen ("./output-of-test-compile-to-dynamic-library.c.so",
14 | 		   RTLD_NOW | RTLD_LOCAL);
15 |   if (!handle)
16 |     {
17 |       fprintf (stderr, "dlopen failed: %s\n", dlerror());
18 |       exit (1);
19 |     }
{% endraw %}

```
### libjava/prims.cc

```cpp

{% raw %}
1397 |       return -1;
1398 |     }
1399 |  
1400 |   lt_dlhandle lib = lt_dlopenext (name);
1401 |   if (!lib)
1402 |     {
{% endraw %}

```
### libjava/classpath/native/jni/midi-dssi/gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider.c

```c

{% raw %}
49 | }
50 | 
51 | jlong
52 | Java_gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider_dlopen_1 
53 |   (JNIEnv *env, jclass clazz __attribute__((unused)), jstring name)
54 | {
61 |   if (filename == NULL)
62 |     return (0);
63 |   
64 |   handle = dlopen(filename, RTLD_NOW);
65 |   
66 |   if (handle == 0)
{% endraw %}

```
### libjava/classpath/include/gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider.h

```c

{% raw %}
9 | {
10 | #endif
11 | 
12 | JNIEXPORT jlong JNICALL Java_gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider_dlopen_1 (JNIEnv *env, jclass, jstring);
13 | JNIEXPORT void JNICALL Java_gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider_dlclose_1 (JNIEnv *env, jclass, jlong);
14 | JNIEXPORT jlong JNICALL Java_gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider_getDSSIHandle_1 (JNIEnv *env, jclass, jlong, jlong);
{% endraw %}

```
### libjava/classpath/tools/toolwrapper.c

```c

{% raw %}
171 |       goto destroy;
172 |     }
173 | 
174 |   libjvm_handle = lt_dlopenext (LIBJVM);
175 |   if (!libjvm_handle)
176 |     {
{% endraw %}

```
### libjava/classpath/gnu/javax/sound/midi/dssi/DSSIMidiDeviceProvider.java

```java

{% raw %}
83 |     }
84 |   }
85 | 
86 |   static native long dlopen_(String soname);
87 |   static native void dlclose_(long sohandle);
88 |   static native long getDSSIHandle_(long sohandle, long index);
97 |      long index = 0;
98 |      long handle;
99 | 
100 |      long sohandle = dlopen_(soname);
101 |      if (sohandle == 0)
102 |        return list;
{% endraw %}

```
### libjava/classpath/gnu/javax/sound/midi/dssi/DSSISynthesizer.java

```java

{% raw %}
501 |   {
502 |     super();
503 |     this.info = info;
504 |     sohandle = DSSIMidiDeviceProvider.dlopen_(soname);
505 |     handle = DSSIMidiDeviceProvider.getDSSIHandle_(sohandle, index);
506 |     channels[0] = new DSSIMidiChannel(0);
{% endraw %}

```
### libjava/libltdl/ltdl.h

```c

{% raw %}
167 | 			lt_ptr data));
168 | 
169 | /* Portable libltdl versions of the system dlopen() API. */
170 | LT_SCOPE	lt_dlhandle lt_dlopen		LT_PARAMS((const char *filename));
171 | LT_SCOPE	lt_dlhandle lt_dlopenext	LT_PARAMS((const char *filename));
172 | LT_SCOPE	lt_ptr	    lt_dlsym		LT_PARAMS((lt_dlhandle handle,
173 | 						     const char *name));
241 | typedef	struct {
242 |   char	*filename;		/* file name */
243 |   char	*name;			/* module name */
244 |   int	ref_count;		/* number of times lt_dlopened minus
245 | 				   number of times lt_dlclosed. */
246 | } lt_dlinfo;
311 |    onto the table of error strings.  */
312 | #define lt_dlerror_table						\
313 |     LT_ERROR(UNKNOWN,		    "unknown error")			\
314 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available")	\
315 |     LT_ERROR(INVALID_LOADER,	    "invalid loader")			\
316 |     LT_ERROR(INIT_LOADER,	    "loader initialization failed")	\
{% endraw %}

```
### libjava/libltdl/ltdl.c

```c

{% raw %}
843 | 
844 | struct lt_dlhandle_struct {
845 |   struct lt_dlhandle_struct   *next;
846 |   lt_dlloader	       *loader;		/* dlopening interface */
847 |   lt_dlinfo		info;
848 |   int			depcount;	/* number of dependencies */
1110 |      lt_user_data loader_data;
1111 |      const char *filename;
1112 | {
1113 |   lt_module   module   = dlopen (filename, LT_GLOBAL | LT_LAZY_OR_NOW);
1114 | 
1115 |   if (!module)
2171 | 						 char *deplibs));
2172 | static	int	trim		      LT_PARAMS((char **dest,
2173 | 						 const char *str));
2174 | static	int	try_dlopen	      LT_PARAMS((lt_dlhandle *handle,
2175 | 						 const char *filename));
2176 | static	int	tryall_dlopen	      LT_PARAMS((lt_dlhandle *handle,
2177 | 						 const char *filename,
2178 | 						 const char * useloader));
2216 |       user_search_path = 0; /* empty search path */
2217 | 
2218 | #if HAVE_LIBDL
2219 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_dl, "dlopen");
2220 | #endif
2221 | #if HAVE_SHL_LOAD
2222 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_shl, "dlopen");
2223 | #endif
2224 | #ifdef __WINDOWS__
2225 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_wll, "dlopen");
2226 | #endif
2227 | #ifdef __BEOS__
2228 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_bedl, "dlopen");
2229 | #endif
2230 | #if HAVE_DLD
2361 | }
2362 | 
2363 | static int
2364 | tryall_dlopen (handle, filename, useloader)
2365 |      lt_dlhandle *handle;
2366 |      const char *filename;
2464 | }
2465 | 
2466 | static int
2467 | tryall_dlopen_module (handle, prefix, dirname, dlname)
2468 |      lt_dlhandle *handle;
2469 |      const char *prefix;
2502 |      shuffled.  Otherwise, attempt to open FILENAME as a module.  */
2503 |   if (prefix)
2504 |     {
2505 |       error += tryall_dlopen_module (handle,
2506 | 				     (const char *) 0, prefix, filename);
2507 |     }
2508 |   else if (tryall_dlopen (handle, filename, NULL) != 0)
2509 |     {
2510 |       ++error;
2524 |      int installed;
2525 | {
2526 |   /* Try to open the old library first; if it was dlpreopened,
2527 |      we want the preopened version of it, even if a dlopenable
2528 |      module is available.  */
2529 |   if (old_name && tryall_dlopen (handle, old_name, "dlpreload") == 0)
2530 |     {
2531 |       return 0;
2537 |       /* try to open the installed module */
2538 |       if (installed && libdir)
2539 | 	{
2540 | 	  if (tryall_dlopen_module (handle,
2541 | 				    (const char *) 0, libdir, dlname) == 0)
2542 | 	    return 0;
2545 |       /* try to open the not-installed module */
2546 |       if (!installed)
2547 | 	{
2548 | 	  if (tryall_dlopen_module (handle, dir, objdir, dlname) == 0)
2549 | 	    return 0;
2550 | 	}
2551 | 
2552 |       /* maybe it was moved to another directory */
2553 |       {
2554 | 	  if (tryall_dlopen_module (handle,
2555 | 				    (const char *) 0, dir, dlname) == 0)
2556 | 	    return 0;
2790 | 
2791 |   /* Try to dlopen the file, but do not continue searching in any
2792 |      case.  */
2793 |   if (tryall_dlopen (handle, filename,NULL) != 0)
2794 |     *handle = 0;
2795 | 
2952 | 
2953 |       for (i = 0; i < depcount; ++i)
2954 | 	{
2955 | 	  handle->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
2956 | 	  if (handle->deplibs[j])
2957 | 	    {
3047 | }
3048 | 
3049 | static int
3050 | try_dlopen (phandle, filename)
3051 |      lt_dlhandle *phandle;
3052 |      const char *filename;
3078 |       /* lt_dlclose()ing yourself is very bad!  Disallow it.  */
3079 |       LT_DLSET_FLAG (*phandle, LT_DLRESIDENT_FLAG);
3080 | 
3081 |       if (tryall_dlopen (&newhandle, 0, NULL) != 0)
3082 | 	{
3083 | 	  LT_DLFREE (*phandle);
3384 | #endif
3385 | 		   )))
3386 | 	{
3387 |           if (tryall_dlopen (&newhandle, filename, NULL) != 0)
3388 |             {
3389 |               newhandle = NULL;
3423 | }
3424 | 
3425 | lt_dlhandle
3426 | lt_dlopen (filename)
3427 |      const char *filename;
3428 | {
3430 | 
3431 |   /* Just incase we missed a code path in try_dlopen() that reports
3432 |      an error, but forgets to reset handle... */
3433 |   if (try_dlopen (&handle, filename) != 0)
3434 |     return 0;
3435 | 
3455 |    and if a file is still not found try again with SHLIB_EXT appended
3456 |    instead.  */
3457 | lt_dlhandle
3458 | lt_dlopenext (filename)
3459 |      const char *filename;
3460 | {
3466 | 
3467 |   if (!filename)
3468 |     {
3469 |       return lt_dlopen (filename);
3470 |     }
3471 | 
3482 | #endif
3483 |       ))
3484 |     {
3485 |       return lt_dlopen (filename);
3486 |     }
3487 | 
3492 | 
3493 |   strcpy (tmp, filename);
3494 |   strcat (tmp, archive_ext);
3495 |   errors = try_dlopen (&handle, tmp);
3496 | 
3497 |   /* If we found FILENAME, stop searching -- whether we were able to
3522 |     }
3523 | 
3524 |   strcat(tmp, shlib_ext);
3525 |   errors = try_dlopen (&handle, tmp);
3526 | 
3527 |   /* As before, if the file was found but loading failed, return now
3729 | 
3730 | /* Call FUNC for each unique extensionless file in SEARCH_PATH, along
3731 |    with DATA.  The filenames passed to FUNC would be suitable for
3732 |    passing to lt_dlopenext.  The extensions are stripped so that
3733 |    individual modules do not generate several entries (e.g. libfoo.la,
3734 |    libfoo.so, libfoo.so.1, libfoo.so.1.0.0).  If SEARCH_PATH is NULL,
3735 |    then the same directories that lt_dlopen would search are examined.  */
3736 | int
3737 | lt_dlforeachfile (search_path, func, data)
{% endraw %}

```
### libjava/java/lang/natRuntime.cc

```cpp

{% raw %}
176 |     // concurrent modification by class registration calls which may be run
177 |     // during the dlopen().
178 |     JvSynchronize sync (&java::lang::Class::class$);
179 |     h = do_search ? lt_dlopenext (lib_name) : lt_dlopen (lib_name);
180 |   }
181 |   if (h == NULL)
240 |   jsize total = JvGetStringUTFRegion (lib, 0, lib->length(), buf);
241 |   buf[total] = '\0';
242 |   // FIXME: make sure path is absolute.
243 |   lt_dlhandle h = lt_dlopenext (buf);
244 |   return h != NULL;
245 | #else
255 |   // Set module load path.
256 |   lt_dlsetsearchpath (_Jv_Module_Load_Path);
257 |   // Make sure self is opened.
258 |   lt_dlopen (NULL);
259 | #endif
260 | }
{% endraw %}

```
### libjava/java/net/natVMURLConnection.cc

```cpp

{% raw %}
31 | java::net::VMURLConnection::init ()
32 | {
33 | #if defined (HAVE_MAGIC_T) && defined (HAVE_MAGIC_H) && defined (USE_LTDL)
34 |   lt_dlhandle handle = lt_dlopenext ("libmagic.so");
35 |   if (!handle)
36 |     return;
{% endraw %}

```
### libjava/gnu/gcj/runtime/natSharedLibLoader.cc

```cpp

{% raw %}
93 |   curHelper = this;
94 |   _Jv_RegisterClassHook = _Jv_sharedlib_register_hook;
95 |   _Jv_RegisterCoreHook = core_hook;
96 |   void *h = dlopen(lname, flags);
97 |   if (h == NULL)
98 |     {
{% endraw %}

```
### libjava/gnu/javax/sound/midi/dssi/DSSIMidiDeviceProvider.h

```c

{% raw %}
44 | {
45 | 
46 | public: // actually package-private
47 |   static jlong dlopen_(::java::lang::String *);
48 |   static void dlclose_(jlong);
49 |   static jlong getDSSIHandle_(jlong, jlong);
{% endraw %}

```
### libstdc++-v3/testsuite/ext/mt_allocator/22309_thread.cc

```cpp

{% raw %}
23 | #include <stdexcept>
24 | 
25 | void
26 | check_dlopen(void*& h)
27 | {
28 |   dlerror();
29 |   void* tmp = dlopen("./testsuite_shared.so", RTLD_LAZY);
30 |   if (!tmp) 
31 |     {
81 | tf(void* arg)
82 | {
83 |   void* h;
84 |   check_dlopen(h);
85 |   check_dlsym(h);
86 |   check_dlclose(h);
{% endraw %}

```
### libstdc++-v3/testsuite/18_support/bad_exception/23591_thread-1.c

```c

{% raw %}
30 |   void* lib;
31 |   void (*cb)();
32 | 
33 |   lib = dlopen("./testsuite_shared.so", RTLD_NOW);
34 |   if (!lib)
35 |     {
36 |       printf("dlopen failed: %s\n", strerror(errno));
37 |       return 0;
38 |     }
{% endraw %}

```
### boehm-gc/threadlibs.c

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
### boehm-gc/dyn_load.c

```c

{% raw %}
37 | 
38 | /* BTL: avoid circular redefinition of dlopen if GC_SOLARIS_THREADS defined */
39 | # if (defined(GC_PTHREADS) || defined(GC_SOLARIS_THREADS)) \
40 |       && defined(dlopen) && !defined(GC_USE_LD_WRAP)
41 |     /* To support threads in Solaris, gc.h interposes on dlopen by       */
42 |     /* defining "dlopen" to be "GC_dlopen", which is implemented below.  */
166 | 	/* to use its value in the set of original object files loaded	*/
167 | 	/* at program startup.						*/
168 | 	if( dynStructureAddr == 0 ) {
169 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
170 | 	  dynStructureAddr = (ElfW(Dyn)*)dlsym(startupSyms, "_DYNAMIC");
171 | 		}
293 |      && !defined(GC_SOLARIS_PTHREADS) && !defined(GC_IRIX_THREADS) \
294 |      && defined(THREADS)
295 | #   ifndef SRC_M3
296 | 	--> fix mutual exclusion with dlopen
297 | #   endif  /* We assume M3 programs don't call dlopen for now */
298 | # endif
{% endraw %}

```
### boehm-gc/gc_dlopen.c

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
### boehm-gc/include/gc_pthread_redirects.h

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
### intl/libgnuintl.h

```c

{% raw %}
72 |      2. in the shared libraries specified on the link command line, in order,
73 |      3. in the dependencies of the shared libraries specified on the link
74 |         command line,
75 |      4. in the dlopen()ed shared libraries, in the order in which they were
76 |         dlopen()ed.
77 |    The definition in the C library would override the one in libintl.so if
78 |    either
{% endraw %}

```
### libvtv/vtv_utils.h

```c

{% raw %}
52 | 
53 | /* The following logging routines try to use low level file access
54 |    routines and avoid calling malloc. We need this so that we dont
55 |    disturb the order of calls to dlopen.  Changing the order of dlopen
56 |    calls may lead to deadlocks */
57 | int __vtv_open_log (const char * name);
{% endraw %}

```
### libvtv/testsuite/other-tests/dlopen.cc

```cpp

{% raw %}
18 | int main()
19 | {
20 |   char so_name[] = "so0.so";
21 |   void * dlhandle = dlopen(so_name, RTLD_NOW);
22 |   if (!dlhandle)
23 |     {
24 |       fprintf(stderr, "dlopen %s error: %s\n", so_name, dlerror());
25 |       exit(1);
26 |     }
27 |   voidfn so_entry = (voidfn)dlsym(dlhandle, "so_entry_0");
28 |   if (!so_entry)
29 |     {
30 |       fprintf(stderr, "dlopen %s dlsym error: %s\n", so_name, dlerror());
31 |       exit(2);
32 |     }
{% endraw %}

```
### libvtv/testsuite/other-tests/dlopen_mt.cc

```cpp

{% raw %}
22 | }
23 | 
24 | 
25 | void do_dlopen(int so_num)
26 | {
27 |   char so_name [sizeof("soxxx.so")];
28 |   sprintf(so_name, "so%d.so", so_num);
29 |   //  printf("dl-opening %s\n", so_name);
30 |   void * dlhandle = dlopen(so_name, RTLD_NOW);
31 |   if (!dlhandle)
32 |     {
33 |       fprintf(stderr, "dlopen so:%s error: %s\n", so_name, dlerror());
34 |       exit(1);
35 |     }
50 | volatile int threads_completed_it = 0;
51 | volatile int current_wave = -1;
52 | 
53 | void * do_dlopens(void * ptid)
54 | {
55 |   for (int k = 0; k < NUM_REPEATS; k++)
60 | 	  while (current_wave < (k*NUM_SOS_PER_THREAD + i)) /* from 0 to 99 */
61 | 	    ;
62 | 
63 |           do_dlopen((NUM_SOS_PER_THREAD * *(int *)ptid) + i);
64 | 
65 | 	  int old_value;
89 |   for (int t = 0; t < NUM_THREADS; t++ )
90 |   {
91 |     thread_nids[t] = t;
92 |     if (pthread_create(&thread_ids[t], NULL, do_dlopens, &thread_nids[t]) != 0)
93 |       {
94 | 	printf("failed pthread_create\n");
{% endraw %}

```
### libcilkrts/runtime/sysdep-unix.c

```c

{% raw %}
791 | static __attribute__((noinline))
792 | void internal_enforce_global_visibility()
793 | {
794 |     void* handle = dlopen( get_runtime_path(), RTLD_GLOBAL|RTLD_LAZY );
795 | 
796 |     /* For proper reference counting, close the handle immediately. */
{% endraw %}

```
### libsanitizer/sanitizer_common/sanitizer_linux.h

```c

{% raw %}
17 | #include "sanitizer_posix.h"
18 | #include "sanitizer_platform_limits_posix.h"
19 | 
20 | struct link_map;  // Opaque type returned by dlopen().
21 | struct sigaltstack;
22 | 
{% endraw %}

```
### libsanitizer/sanitizer_common/sanitizer_unwind_linux_libcdep.cc

```cpp

{% raw %}
45 | 
46 | #if SANITIZER_ANDROID
47 | void SanitizerInitializeUnwinder() {
48 |   void *p = dlopen("libcorkscrew.so", RTLD_LAZY);
49 |   if (!p) {
50 |     VReport(1,
{% endraw %}

```
### libgcc/config/darwin-crt3.c

```c

{% raw %}
267 |     {
268 |       void *handle;
269 | 
270 |       handle = dlopen ("/usr/lib/libSystem.B.dylib", RTLD_NOLOAD);
271 |       if (!handle)
272 | 	{
{% endraw %}

```
### lto-plugin/lto-symtab.c

```c

{% raw %}
136 | load_plugin (const char *name)
137 | {
138 |   ld_plugin_onload onload;
139 |   plugin_handle = dlopen (name, RTLD_LAZY);
140 | 
141 |   assert (plugin_handle != NULL);
{% endraw %}

```
### libgomp/target.c

```c

{% raw %}
2349 | {
2350 |   const char *err = NULL, *last_missing = NULL;
2351 | 
2352 |   void *plugin_handle = dlopen (plugin_name, RTLD_LAZY);
2353 |   if (!plugin_handle)
2354 |     goto dl_fail;
{% endraw %}

```
### libgomp/plugin/plugin-hsa.c

```c

{% raw %}
686 | {
687 |   struct brig_library_info *library = NULL;
688 | 
689 |   void *f = dlopen (file_name, RTLD_NOW);
690 |   void *start = dlsym (f, "__brig_start");
691 |   void *end = dlsym (f, "__brig_end");
{% endraw %}

```