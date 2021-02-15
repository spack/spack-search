---
name: "hpctoolkit"
layout: package
next_package: vampirtrace
previous_package: linux-pam
languages: ['cpp', 'bash']
---
## 2020.08.03
39 / 1254 files match

 - [config/libtool.m4](#configlibtoolm4)
 - [config/ltoptions.m4](#configltoptionsm4)
 - [config/ltmain.sh](#configltmainsh)
 - [src/tool/hpcrun/module-ignore-map.c](#srctoolhpcrunmodule-ignore-mapc)
 - [src/tool/hpcrun/device-initializers.c](#srctoolhpcrundevice-initializersc)
 - [src/tool/hpcrun/thread_data.h](#srctoolhpcrunthread_datah)
 - [src/tool/hpcrun/hpcrun_stats.h](#srctoolhpcrunhpcrun_statsh)
 - [src/tool/hpcrun/custom-init-dynamic.c](#srctoolhpcruncustom-init-dynamicc)
 - [src/tool/hpcrun/hpcrun_stats.c](#srctoolhpcrunhpcrun_statsc)
 - [src/tool/hpcrun/epoch.c](#srctoolhpcrunepochc)
 - [src/tool/hpcrun/hpcrun_dlfns.h](#srctoolhpcrunhpcrun_dlfnsh)
 - [src/tool/hpcrun/main.h](#srctoolhpcrunmainh)
 - [src/tool/hpcrun/main.c](#srctoolhpcrunmainc)
 - [src/tool/hpcrun/hpcrun_dlfns.c](#srctoolhpcrunhpcrun_dlfnsc)
 - [src/tool/hpcrun/loadmap.h](#srctoolhpcrunloadmaph)
 - [src/tool/hpcrun/fnbounds/fnbounds_dynamic.c](#srctoolhpcrunfnboundsfnbounds_dynamicc)
 - [src/tool/hpcrun/lush/lush.c](#srctoolhpcrunlushlushc)
 - [src/tool/hpcrun/lush/lush.h](#srctoolhpcrunlushlushh)
 - [src/tool/hpcrun/lush/lushi.h](#srctoolhpcrunlushlushih)
 - [src/tool/hpcrun/gpu/nvidia/cupti-api.c](#srctoolhpcrungpunvidiacupti-apic)
 - [src/tool/hpcrun/gpu/amd/roctracer-api.c](#srctoolhpcrungpuamdroctracer-apic)
 - [src/tool/hpcrun/sample-sources/papi-c-cupti.c](#srctoolhpcrunsample-sourcespapi-c-cuptic)
 - [src/tool/hpcrun/sample-sources/libdl.h](#srctoolhpcrunsample-sourceslibdlh)
 - [src/tool/hpcrun/sample-sources/gpu_blame-overrides.c](#srctoolhpcrunsample-sourcesgpu_blame-overridesc)
 - [src/tool/hpcrun/sample-sources/memleak-overrides.c](#srctoolhpcrunsample-sourcesmemleak-overridesc)
 - [src/tool/hpcrun/sample-sources/dynlib.c](#srctoolhpcrunsample-sourcesdynlibc)
 - [src/tool/hpcrun/lush-agents/agent-cilk.c](#srctoolhpcrunlush-agentsagent-cilkc)
 - [src/tool/hpcrun/lush-agents/agent-tbb.c](#srctoolhpcrunlush-agentsagent-tbbc)
 - [src/tool/hpcrun/lush-agents/agent-pthread.c](#srctoolhpcrunlush-agentsagent-pthreadc)
 - [src/tool/hpcrun/doc/hpcrun-internals.txt](#srctoolhpcrundochpcrun-internalstxt)
 - [src/tool/hpcrun-flat/monitor_preload.c](#srctoolhpcrun-flatmonitor_preloadc)
 - [src/tool/hpcrun-flat/monitor.c](#srctoolhpcrun-flatmonitorc)
 - [src/tool/hpcrun-flat/monitor.h](#srctoolhpcrun-flatmonitorh)
 - [src/tool/hpcrun-flat/dlpapi.c](#srctoolhpcrun-flatdlpapic)
 - [src/tool/hpcrun-flat/dlpapi.h](#srctoolhpcrun-flatdlpapih)
 - [src/tool/hpcrun-flat/hpcrun.cpp](#srctoolhpcrun-flathpcruncpp)
 - [src/tool/hpcfnbounds/eh-frames.cpp](#srctoolhpcfnboundseh-framescpp)
 - [src/tool/hpcfnbounds/hpcfnbounds.in](#srctoolhpcfnboundshpcfnboundsin)
 - [src/lib/analysis/Flat-SrcCorrelation.cpp](#srclibanalysisflat-srccorrelationcpp)

### config/libtool.m4

```

{% raw %}
1821 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1824 | m4_defun([_LT_TRY_DLOPEN_SELF],
1882 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1915 | ])# _LT_TRY_DLOPEN_SELF
1918 | # LT_SYS_DLOPEN_SELF
1920 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1922 | if test yes != "$enable_dlopen"; then
1923 |   enable_dlopen=unknown
1924 |   enable_dlopen_self=unknown
1925 |   enable_dlopen_self_static=unknown
1927 |   lt_cv_dlopen=no
1928 |   lt_cv_dlopen_libs=
1932 |     lt_cv_dlopen=load_add_on
1933 |     lt_cv_dlopen_libs=
1934 |     lt_cv_dlopen_self=yes
1938 |     lt_cv_dlopen=LoadLibrary
1939 |     lt_cv_dlopen_libs=
1943 |     lt_cv_dlopen=dlopen
1944 |     lt_cv_dlopen_libs=
1949 |     AC_CHECK_LIB([dl], [dlopen],
1950 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1951 |     lt_cv_dlopen=dyld
1952 |     lt_cv_dlopen_libs=
1953 |     lt_cv_dlopen_self=yes
1960 |     lt_cv_dlopen=dlopen
1961 |     lt_cv_dlopen_libs=
1962 |     lt_cv_dlopen_self=no
1967 | 	  [lt_cv_dlopen=shl_load],
1969 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1970 | 	[AC_CHECK_FUNC([dlopen],
1971 | 	      [lt_cv_dlopen=dlopen],
1972 | 	  [AC_CHECK_LIB([dl], [dlopen],
1973 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1974 | 	    [AC_CHECK_LIB([svld], [dlopen],
1975 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1977 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1986 |   if test no = "$lt_cv_dlopen"; then
1987 |     enable_dlopen=no
1989 |     enable_dlopen=yes
1992 |   case $lt_cv_dlopen in
1993 |   dlopen)
2001 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2003 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2004 | 	  lt_cv_dlopen_self, [dnl
2005 | 	  _LT_TRY_DLOPEN_SELF(
2006 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2007 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2010 |     if test yes = "$lt_cv_dlopen_self"; then
2012 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2013 | 	  lt_cv_dlopen_self_static, [dnl
2014 | 	  _LT_TRY_DLOPEN_SELF(
2015 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2016 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2026 |   case $lt_cv_dlopen_self in
2027 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2028 |   *) enable_dlopen_self=unknown ;;
2031 |   case $lt_cv_dlopen_self_static in
2032 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2033 |   *) enable_dlopen_self_static=unknown ;;
2036 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2037 | 	 [Whether dlopen is supported])
2038 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2039 | 	 [Whether dlopen of programs is supported])
2040 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2041 | 	 [Whether dlopen of statically linked programs is supported])
2042 | ])# LT_SYS_DLOPEN_SELF
2045 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2047 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6122 |     [Compiler flag to allow reflexive dlopens])
6235 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### config/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
107 | # dlopen
109 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
112 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
113 | [_LT_SET_OPTION([LT_INIT], [dlopen])
116 | put the 'dlopen' option into LT_INIT's first parameter.])
120 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### src/tool/hpcrun/module-ignore-map.c

```cpp

{% raw %}
64 | #include <dlfcn.h>  // dlopen
278 |   // Guarantee dlopen modules before notification are updated.  
{% endraw %}

```
### src/tool/hpcrun/device-initializers.c

```cpp

{% raw %}
12 |   // TODO(Keren): improve the mechanism by inserting every module into the map and avoiding dlopen test
{% endraw %}

```
### src/tool/hpcrun/thread_data.h

```cpp

{% raw %}
276 |   // True if this thread is inside dlopen or dlclose.  A synchronous
277 |   // override that is called from dlopen (eg, malloc) must skip this
278 |   // sample or else deadlock on the dlopen lock.
{% endraw %}

```
### src/tool/hpcrun/hpcrun_stats.h

```cpp

{% raw %}
78 | // samples blocked dlopen 
81 | void hpcrun_stats_num_samples_blocked_dlopen_inc(void);
82 | long hpcrun_stats_num_samples_blocked_dlopen(void);
{% endraw %}

```
### src/tool/hpcrun/custom-init-dynamic.c

```cpp

{% raw %}
84 |     void* custom_fns = monitor_real_dlopen("./hpcrun-custom.so", RTLD_LAZY);
{% endraw %}

```
### src/tool/hpcrun/hpcrun_stats.c

```cpp

{% raw %}
68 | static atomic_long num_samples_blocked_dlopen = ATOMIC_VAR_INIT(0);
97 |   atomic_store_explicit(&num_samples_blocked_dlopen, 0, memory_order_relaxed);
177 | // samples blocked dlopen 
181 | hpcrun_stats_num_samples_blocked_dlopen_inc(void)
183 |   atomic_fetch_add_explicit(&num_samples_blocked_dlopen, 1L, memory_order_relaxed);
188 | hpcrun_stats_num_samples_blocked_dlopen(void)
190 |   return atomic_load_explicit(&num_samples_blocked_dlopen, memory_order_relaxed);
444 |   long cpu_blocked_dlopen = atomic_load_explicit(&num_samples_blocked_dlopen, memory_order_relaxed);
445 |   long cpu_blocked = cpu_blocked_async + cpu_blocked_dlopen;
480 |   AMSG("SAMPLE ANOMALIES: blocks: %ld (async: %ld, dlopen: %ld), "
482 |        cpu_blocked, cpu_blocked_async, cpu_blocked_dlopen, 
{% endraw %}

```
### src/tool/hpcrun/epoch.c

```cpp

{% raw %}
96 |   dlopen()'s a new shared object, which begins an entirely
{% endraw %}

```
### src/tool/hpcrun/hpcrun_dlfns.h

```cpp

{% raw %}
49 | void hpcrun_pre_dlopen(const char *path, int flags);
50 | void hpcrun_dlopen(const char *module_name, int flags, void *handle);
54 | long hpcrun_dlopen_pending(void);
{% endraw %}

```
### src/tool/hpcrun/main.h

```cpp

{% raw %}
62 | extern void hpcrun_force_dlopen(bool forced);
{% endraw %}

```
### src/tool/hpcrun/main.c

```cpp

{% raw %}
238 | static bool hpcrun_dlopen_forced = false;
340 | hpcrun_force_dlopen(bool forced)
342 |   hpcrun_dlopen_forced = forced;
409 | // and thread are run in sequence, but dlopen, fork, pthread-create
1669 | monitor_pre_dlopen(const char* path, int flags)
1677 |   hpcrun_pre_dlopen(path, flags);
1683 | monitor_dlopen(const char *path, int flags, void* handle)
1686 |   hpcrun_dlopen(path, flags, handle);
{% endraw %}

```
### src/tool/hpcrun/hpcrun_dlfns.c

```cpp

{% raw %}
73 | // Protect dlopen(), dlclose() and dl_iterate_phdr() with a readers-
77 | // dlopen and dlclose modify the internal dl data structures, so
82 | // thread id of the writer and if a nested dlopen (from init ctor)
86 | // This is necessary to handle nested dlopens in an init constructor.
88 | // And if we could just separate dlopen() into mmap() and its init
91 | // DLOPEN_RISKY disables the read locks (always succeed), so that
97 | static spinlock_t dlopen_lock = SPINLOCK_UNLOCKED;
98 | static atomic_long dlopen_num_readers = ATOMIC_VAR_INIT(0);
99 | static volatile long dlopen_num_writers = 0;
100 | static int  dlopen_writer_tid = -1;
103 | static atomic_long num_dlopen_pending = ATOMIC_VAR_INIT(0);
106 | // We use this only in the DLOPEN_RISKY case.
108 | hpcrun_dlopen_pending(void)
110 |   return atomic_load_explicit(&num_dlopen_pending, memory_order_relaxed);
114 | hpcrun_pre_dlopen(const char *path, int flags)
121 | hpcrun_dlopen(const char *module_name, int flags, void *handle)
{% endraw %}

```
### src/tool/hpcrun/loadmap.h

```cpp

{% raw %}
53 |    an loadmap can span across dlopen and dlclose operations. an loadmap
54 |    ends when a dlopen maps a new load module on top of a region of 
{% endraw %}

```
### src/tool/hpcrun/fnbounds/fnbounds_dynamic.c

```cpp

{% raw %}
69 | #include <dlfcn.h>     // for dlopen/dlclose
516 |   // sample at just the wrong point inside dlopen() will segfault or
522 |   if (!dso && ENABLED(DLOPEN_RISKY) && hpcrun_dlopen_pending() > 0) {
{% endraw %}

```
### src/tool/hpcrun/lush/lush.c

```cpp

{% raw %}
104 |   //x->dlhandle = dlopen(path, RTLD_LAZY);
105 |   x->dlhandle = monitor_real_dlopen(path, RTLD_LAZY);
115 |   CALL_DLSYM(pool, LUSHI_reg_dlopen,   id, x->dlhandle);
181 |   FN_TBL_ALLOC(x, LUSHI_reg_dlopen,      num_agents + 1);
210 |   FN_TBL_FREE(x, LUSHI_reg_dlopen);
{% endraw %}

```
### src/tool/hpcrun/lush/lush.h

```cpp

{% raw %}
105 |   POOL_DECL(LUSHI_reg_dlopen);
{% endraw %}

```
### src/tool/hpcrun/lush/lushi.h

```cpp

{% raw %}
113 | LUSHI_DECL(int, LUSHI_reg_dlopen, ());
{% endraw %}

```
### src/tool/hpcrun/gpu/nvidia/cupti-api.c

```cpp

{% raw %}
82 | #include <hpcrun/main.h> // hpcrun_force_dlopen
502 |   // already be loaded. thus, even if the dlopen fails, we search with
504 |   void *h = monitor_real_dlopen("libcudart.so", RTLD_LOCAL | RTLD_LAZY);
554 |   hpcrun_force_dlopen(true);
555 |   CHK_DLOPEN(cupti, cupti_path(), RTLD_NOW | RTLD_GLOBAL);
556 |   hpcrun_force_dlopen(false);
{% endraw %}

```
### src/tool/hpcrun/gpu/amd/roctracer-api.c

```cpp

{% raw %}
442 |   hpcrun_force_dlopen(true);
443 |   CHK_DLOPEN(roctracer, roctracer_path(), RTLD_NOW | RTLD_GLOBAL);
444 |   hpcrun_force_dlopen(false);
{% endraw %}

```
### src/tool/hpcrun/sample-sources/papi-c-cupti.c

```cpp

{% raw %}
61 | #define Chk_dlopen(v, lib, flags)                     \
62 |   void* v = monitor_real_dlopen(lib, flags);          \
64 |     fprintf(stderr, "gpu dlopen %s failed\n", lib);   \
94 | // Some cuda/cupti functions must not be wrapped! So, we fetch them via dlopen.
121 | // populate the cuda/cupti functions via dlopen
129 |   Chk_dlopen(cudart, "libcudart.so", RTLD_NOW | RTLD_GLOBAL);
132 |   Chk_dlopen(cupti, "libcupti.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/tool/hpcrun/sample-sources/libdl.h

```cpp

{% raw %}
52 | //   simple wrappers that facilitate using dlopen and dlsym to dynamically 
84 | #define CHK_DLOPEN(h, lib, flags)		      \
85 |   void* h = dlopen(lib, flags);          \
{% endraw %}

```
### src/tool/hpcrun/sample-sources/gpu_blame-overrides.c

```cpp

{% raw %}
362 | //  Decide on RTLD_NEXT or dlopen of library for the function pointer set
377 |     dlsym_arg = monitor_real_dlopen(#library, RTLD_LAZY);			   \
379 |       fprintf(stderr, "fallback dlopen of " #library " failed,"			   \
634 |   // no dlopen calls in static case
{% endraw %}

```
### src/tool/hpcrun/sample-sources/memleak-overrides.c

```cpp

{% raw %}
500 |   // inside dlopen, that would lead to deadlock.
814 |   // again, can't track malloc inside dlopen.
{% endraw %}

```
### src/tool/hpcrun/sample-sources/dynlib.c

```cpp

{% raw %}
81 |   *handle = monitor_real_dlopen(libname, flags);
{% endraw %}

```
### src/tool/hpcrun/lush-agents/agent-cilk.c

```cpp

{% raw %}
162 | LUSHI_reg_dlopen()
{% endraw %}

```
### src/tool/hpcrun/lush-agents/agent-tbb.c

```cpp

{% raw %}
132 | LUSHI_reg_dlopen()
{% endraw %}

```
### src/tool/hpcrun/lush-agents/agent-pthread.c

```cpp

{% raw %}
139 | LUSHI_reg_dlopen()
{% endraw %}

```
### src/tool/hpcrun/doc/hpcrun-internals.txt

```

{% raw %}
170 | independent sources to be loaded via dlopen() or similar, it might
179 | when certain events occur.  Such functions include dlopen(),
207 | back to the functions in which they occurred.  Every dlopen(), then,
{% endraw %}

```
### src/tool/hpcrun-flat/monitor_preload.c

```cpp

{% raw %}
164 | monitor_dlopen(char* lib)
167 |     fprintf(stderr, "dlopen(%s) callback from monitor received\n", lib); 
170 |   //handle_dlopen();
{% endraw %}

```
### src/tool/hpcrun-flat/monitor.c

```cpp

{% raw %}
449 |  * Called after the loading of a module using dlopen() to update the
454 | handle_dlopen()
457 |     DIE0("dlopen before process initialization!");
498 |   if (opt_debug >= 1) { MSG0(stderr, "*** dlopen handling complete ***"); }
{% endraw %}

```
### src/tool/hpcrun-flat/monitor.h

```cpp

{% raw %}
227 | typedef void* (*dlopen_fptr_t) (const char *filename, int flag);
276 | extern void handle_dlopen();
{% endraw %}

```
### src/tool/hpcrun-flat/dlpapi.c

```cpp

{% raw %}
99 | dlopen_papi()
102 |   libpapi = dlopen(HPC_LIBPAPI_SO, RTLD_LAZY);
{% endraw %}

```
### src/tool/hpcrun-flat/dlpapi.h

```cpp

{% raw %}
81 | extern int dlopen_papi();
{% endraw %}

```
### src/tool/hpcrun-flat/hpcrun.cpp

```

{% raw %}
343 |   // For a (security?) reason I do not understand, dlopen may *ignore*
373 |     dlopen_papi();
{% endraw %}

```
### src/tool/hpcfnbounds/eh-frames.cpp

```

{% raw %}
53 | // libdwarf via dlopen() and dlsym().
56 | // file, we re-dlopen libdwarf.so, save the addrs in a set, dlclose
93 | #define DLOPEN_OPTS    (RTLD_NOW | RTLD_LOCAL)
101 | // get libdwarf.so functions via dlopen() and dlsym()
139 | static int dlopen_done = 0;
144 | // direct function calls, no dlopen
158 | // In the libdw case, we use dlopen() and dlsym() to access the
178 |       libdwarf_handle = dlopen(library_file.c_str(), DLOPEN_OPTS);
182 | 	dlopen_done = 1;
208 | 	libdwarf_handle = dlopen(library_file.c_str(), DLOPEN_OPTS);
212 | 	  dlopen_done = 1;
226 |   // step 2 -- dlopen()
227 |   if (! dlopen_done) {
228 |     libdwarf_handle = dlopen(library_file.c_str(), DLOPEN_OPTS);
235 |     dlopen_done = 1;
279 |   dlopen_done = 0;
{% endraw %}

```
### src/tool/hpcfnbounds/hpcfnbounds.in

```

{% raw %}
49 | # Tell fnbounds where to find libdwarf.so for dlopen.
{% endraw %}

```
### src/lib/analysis/Flat-SrcCorrelation.cpp

```

{% raw %}
669 |     // This will have to change when true dlopen support is available.
{% endraw %}

```