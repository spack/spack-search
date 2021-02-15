---
name: "boost"
layout: package
next_package: kbd
previous_package: gmake
languages: ['html', 'bash', 'cpp', 'python']
---
## 1.49.0
21 / 38128 files match

 - [libs/serialization/test/test_dll_plugin.cpp](#libsserializationtesttest_dll_plugincpp)
 - [libs/serialization/doc/special.html](#libsserializationdocspecialhtml)
 - [libs/mpi/build/__init__.py](#libsmpibuild__init__py)
 - [libs/test/tools/console_test_runner/src/console_test_runner.cpp](#libstesttoolsconsole_test_runnersrcconsole_test_runnercpp)
 - [tools/build/v2/engine/mem.c](#toolsbuildv2enginememc)
 - [tools/build/v2/engine/boehm_gc/pthread_support.c](#toolsbuildv2engineboehm_gcpthread_supportc)
 - [tools/build/v2/engine/boehm_gc/libtool.m4](#toolsbuildv2engineboehm_gclibtoolm4)
 - [tools/build/v2/engine/boehm_gc/configure.ac](#toolsbuildv2engineboehm_gcconfigureac)
 - [tools/build/v2/engine/boehm_gc/win32_threads.c](#toolsbuildv2engineboehm_gcwin32_threadsc)
 - [tools/build/v2/engine/boehm_gc/Makefile.direct](#toolsbuildv2engineboehm_gcmakefiledirect)
 - [tools/build/v2/engine/boehm_gc/threadlibs.c](#toolsbuildv2engineboehm_gcthreadlibsc)
 - [tools/build/v2/engine/boehm_gc/ltmain.sh](#toolsbuildv2engineboehm_gcltmainsh)
 - [tools/build/v2/engine/boehm_gc/dyn_load.c](#toolsbuildv2engineboehm_gcdyn_loadc)
 - [tools/build/v2/engine/boehm_gc/Makefile.am](#toolsbuildv2engineboehm_gcmakefileam)
 - [tools/build/v2/engine/boehm_gc/gc_dlopen.c](#toolsbuildv2engineboehm_gcgc_dlopenc)
 - [tools/build/v2/engine/boehm_gc/Makefile.in](#toolsbuildv2engineboehm_gcmakefilein)
 - [tools/build/v2/engine/boehm_gc/include/gc_pthread_redirects.h](#toolsbuildv2engineboehm_gcincludegc_pthread_redirectsh)
 - [tools/build/v2/engine/boehm_gc/doc/README.changes](#toolsbuildv2engineboehm_gcdocreadmechanges)
 - [tools/build/v2/engine/boehm_gc/doc/README.linux](#toolsbuildv2engineboehm_gcdocreadmelinux)
 - [tools/build/v2/engine/boehm_gc/doc/README.solaris2](#toolsbuildv2engineboehm_gcdocreadmesolaris2)
 - [tools/build/v2/tools/python.jam](#toolsbuildv2toolspythonjam)

### libs/serialization/test/test_dll_plugin.cpp

```

{% raw %}
194 |     hDLL = dlopen("plugin_polymorphic_derived2.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### libs/serialization/doc/special.html

```html

{% raw %}
489 |   <li>If DLLS are to be loaded an unloaded explicitly (e.g. using <code>dlopen</code> in *nix or 
{% endraw %}

```
### libs/mpi/build/__init__.py

```python

{% raw %}
3 |     flags = sys.getdlopenflags()
4 |     sys.setdlopenflags(dl.RTLD_NOW|dl.RTLD_GLOBAL)
6 |     sys.setdlopenflags(flags)
{% endraw %}

```
### libs/test/tools/console_test_runner/src/console_test_runner.cpp

```

{% raw %}
97 |     return dlopen( file_name.c_str(), RTLD_LOCAL | RTLD_LAZY );
{% endraw %}

```
### tools/build/v2/engine/mem.c

```cpp

{% raw %}
59 |     #include "boehm_gc/gc_dlopen.c"
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/pthread_support.c

```cpp

{% raw %}
125 | #   ifdef GC_USE_DLOPEN_WRAP
152 | #if defined(GC_USE_DL_WRAP) || defined(GC_USE_DLOPEN_WRAP)
171 | #ifdef GC_USE_DLOPEN_WRAP
187 |       dl_handle = dlopen(libpthread_name, RTLD_LAZY);
193 |         dl_handle = dlopen(namebuf, RTLD_LAZY);
732 |       /* in response to dlopen calls.					*/  
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/libtool.m4

```

{% raw %}
199 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
814 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
817 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
873 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
902 | ])# _LT_AC_TRY_DLOPEN_SELF
905 | # AC_LIBTOOL_DLOPEN_SELF
907 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
909 | if test "x$enable_dlopen" != xyes; then
910 |   enable_dlopen=unknown
911 |   enable_dlopen_self=unknown
912 |   enable_dlopen_self_static=unknown
914 |   lt_cv_dlopen=no
915 |   lt_cv_dlopen_libs=
919 |     lt_cv_dlopen="load_add_on"
920 |     lt_cv_dlopen_libs=
921 |     lt_cv_dlopen_self=yes
925 |     lt_cv_dlopen="LoadLibrary"
926 |     lt_cv_dlopen_libs=
930 |     lt_cv_dlopen="dlopen"
931 |     lt_cv_dlopen_libs=
936 |     AC_CHECK_LIB([dl], [dlopen],
937 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
938 |     lt_cv_dlopen="dyld"
939 |     lt_cv_dlopen_libs=
940 |     lt_cv_dlopen_self=yes
946 | 	  [lt_cv_dlopen="shl_load"],
948 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
949 | 	[AC_CHECK_FUNC([dlopen],
950 | 	      [lt_cv_dlopen="dlopen"],
951 | 	  [AC_CHECK_LIB([dl], [dlopen],
952 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
953 | 	    [AC_CHECK_LIB([svld], [dlopen],
954 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
956 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
965 |   if test "x$lt_cv_dlopen" != xno; then
966 |     enable_dlopen=yes
968 |     enable_dlopen=no
971 |   case $lt_cv_dlopen in
972 |   dlopen)
980 |     LIBS="$lt_cv_dlopen_libs $LIBS"
982 |     AC_CACHE_CHECK([whether a program can dlopen itself],
983 | 	  lt_cv_dlopen_self, [dnl
984 | 	  _LT_AC_TRY_DLOPEN_SELF(
985 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
986 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
989 |     if test "x$lt_cv_dlopen_self" = xyes; then
991 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
992 |     	  lt_cv_dlopen_self_static, [dnl
993 | 	  _LT_AC_TRY_DLOPEN_SELF(
994 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
995 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1005 |   case $lt_cv_dlopen_self in
1006 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1007 |   *) enable_dlopen_self=unknown ;;
1010 |   case $lt_cv_dlopen_self_static in
1011 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1012 |   *) enable_dlopen_self_static=unknown ;;
1015 | ])# AC_LIBTOOL_DLOPEN_SELF
1888 | # AC_LIBTOOL_DLOPEN
1890 | # enable checks for dlopen support
1891 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1893 | ])# AC_LIBTOOL_DLOPEN
2685 | AC_LIBTOOL_DLOPEN_SELF
4364 | # Whether dlopen is supported.
4365 | dlopen_support=$enable_dlopen
4367 | # Whether dlopen of programs is supported.
4368 | dlopen_self=$enable_dlopen_self
4370 | # Whether dlopen of statically linked programs is supported.
4371 | dlopen_self_static=$enable_dlopen_self_static
4379 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/configure.ac

```

{% raw %}
297 |     AC_CHECK_LIB(dl, dlopen, THREADDLLIBS="$THREADDLLIBS -ldl")
366 |     if test x"${ac_cv_lib_dl_dlopen}" != xyes ; then
367 |        AC_MSG_WARN(OpenBSD/Alpha without dlopen(). Shared library support is disabled)
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/win32_threads.c

```cpp

{% raw %}
40 | # undef dlopen 
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/Makefile.direct

```

{% raw %}
43 | # malloc, add -DGC_USE_DLOPEN_WRAP -DREDIRECT_MALLOC=GC_malloc -fpic
251 | # -DGC_USE_DLOPEN_WRAP causes the collector to redefine malloc and intercepted
252 | #   pthread routines with their real names, and causes it to use dlopen
332 |   gc_dlopen.o backgraph.o win32_threads.o thread_local_alloc.o
338 |   typd_mlc.c ptr_chck.c mallocx.c gcj_mlc.c specific.c gc_dlopen.c \
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/threadlibs.c

```cpp

{% raw %}
7 | 	printf("-Wl,--wrap -Wl,dlopen "
15 | #       ifdef GC_USE_DLOPEN_WRAP
21 | #       ifdef GC_USE_DLOPEN_WRAP
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/ltmain.sh

```bash

{% raw %}
522 |   -dlopen)
523 |     prevopt="-dlopen"
607 |   # Only execute mode is allowed to have -dlopen flags.
609 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1146 | 	    dlopen_self=$dlopen_self_static
1151 | 	    dlopen_self=$dlopen_self_static
1207 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1299 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1456 |       -dlopen)
1843 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1916 | 	  # This library was specified with -dlopen.
2057 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2069 | 	passes="conv scan dlopen dlpreopen link"
2082 | 	dlopen) libs="$dlfiles" ;;
2087 |       if test "$pass" = dlopen; then
2266 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2267 | 	      # If there is no dlopen support or we're linking statically,
2300 | 	dlopen=
2321 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2364 | 	# This library was specified with -dlopen.
2365 | 	if test "$pass" = dlopen; then
2367 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2371 | 	     test "$dlopen_support" != yes ||
2373 | 	    # If there is no dlname, no dlopen support or we're linking
2382 | 	fi # $pass = dlopen
2435 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2810 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2811 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2962 |       if test "$pass" != dlopen; then
3063 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3130 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3768 | 	    $echo "*** a static module, that should work as long as the dlopening"
3769 | 	    $echo "*** application is linked with the -dlopen flag."
3787 | 	    $echo "*** or is declared to -dlopen it."
4197 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4329 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4330 | 	   test "$dlopen_self_static" = unknown; then
4331 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5669 | # The name that we can dlopen(3).
5692 | # Files to dlopen/dlpreopen
5693 | dlopen='$dlfiles'
6308 |     # Handle -dlopen flags immediately.
6337 | 	# Skip this library if it cannot be dlopened.
6362 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6722 |   -dlopen FILE      add the directory containing FILE to the library path
6724 | This mode sets the library path environment variable according to \`-dlopen'
6773 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6782 |   -module           build a library that can dlopened
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/dyn_load.c

```cpp

{% raw %}
21 |  * that this is a bug in the design of the dlopen interface.  THIS CODE
38 | /* BTL: avoid circular redefinition of dlopen if GC_SOLARIS_THREADS defined */
40 |       && defined(dlopen) && !defined(GC_USE_LD_WRAP)
41 |     /* To support threads in Solaris, gc.h interposes on dlopen by       */
42 |     /* defining "dlopen" to be "GC_dlopen", which is implemented below.  */
43 |     /* However, both GC_FirstDLOpenedLinkMap() and GC_dlopen() use the   */
44 |     /* real system dlopen() in their implementation. We first remove     */
45 |     /* gc.h's dlopen definition and restore it later, after GC_dlopen(). */
46 | #   undef dlopen
47 | #   define GC_must_restore_redefined_dlopen
49 | #   undef GC_must_restore_redefined_dlopen
123 | GC_FirstDLOpenedLinkMap()
138 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
164 | /* BTL: added to fix circular dlopen definition if GC_SOLARIS_THREADS defined */
165 | # if defined(GC_must_restore_redefined_dlopen)
166 | #   define dlopen GC_dlopen
172 | 	--> fix mutual exclusion with dlopen
178 |   struct link_map *lm = GC_FirstDLOpenedLinkMap();
181 |   for (lm = GC_FirstDLOpenedLinkMap();
441 | GC_FirstDLOpenedLinkMap()
474 |   lm = GC_FirstDLOpenedLinkMap();
475 |   for (lm = GC_FirstDLOpenedLinkMap();
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/Makefile.am

```

{% raw %}
52 | 	dyn_load.c finalize.c gc_dlopen.c gcj_mlc.c headers.c \
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/gc_dlopen.c

```cpp

{% raw %}
21 |  * dlopen.  Of course this fails if the collector is in a dynamic
30 | # if defined(dlopen) && !defined(GC_USE_LD_WRAP)
31 |     /* To support various threads pkgs, gc.h interposes on dlopen by     */
32 |     /* defining "dlopen" to be "GC_dlopen", which is implemented below.  */
33 |     /* However, both GC_FirstDLOpenedLinkMap() and GC_dlopen() use the   */
34 |     /* real system dlopen() in their implementation. We first remove     */
35 |     /* gc.h's dlopen definition and restore it later, after GC_dlopen(). */
36 | #   undef dlopen
41 |   /* This is invoked prior to a dlopen call to avoid synchronization	*/
43 |   /* code in dlopen may try to allocate.				*/
44 |   /* This solution risks heap growth in the presence of many dlopen	*/
48 |   static void disable_gc_for_dlopen()
58 |   /* Redefine dlopen to guarantee mutual exclusion with	*/
65 |   void * __wrap_dlopen(const char *path, int mode)
67 |   void * GC_dlopen(const char *path, int mode)
73 |       disable_gc_for_dlopen();
76 |       result = (void *)__real_dlopen(path, mode);
78 |       result = dlopen(path, mode);
81 |       GC_enable(); /* undoes disable_gc_for_dlopen */
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/Makefile.in

```

{% raw %}
156 | 	dbg_mlc.c dyn_load.c finalize.c gc_dlopen.c gcj_mlc.c \
167 | 	dbg_mlc.lo dyn_load.lo finalize.lo gc_dlopen.lo gcj_mlc.lo \
497 | 	dyn_load.c finalize.c gc_dlopen.c gcj_mlc.c headers.c malloc.c \
752 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/gc_dlopen.Plo@am__quote@
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/include/gc_pthread_redirects.h

```cpp

{% raw %}
48 | # define dlopen GC_dlopen
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/doc/README.changes

```

{% raw %}
935 |  - Added an attempt at a more general solution to dlopen races/deadlocks.
936 |    GC_dlopen now temporarily disables collection.  Still not ideal, but ...
2423 |  - Added support for dlopen-based interception of pthread functions.
2568 |  - A dynamic libgc.so references dlopen unconditionally, but doesn't link
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/doc/README.linux

```

{% raw %}
39 |    (for ld) --wrap read --wrap dlopen --wrap pthread_create \
43 |    (for gcc) -Wl,--wrap -Wl,read -Wl,--wrap -Wl,dlopen -Wl,--wrap \
50 | 4) Dlopen() disables collection during its execution.  (It can't run
53 |    user startup code may run as part of dlopen().)  Under unusual
66 |    and if dlopen is not used.)
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/doc/README.solaris2

```

{% raw %}
27 | thr_join, thr_suspend, thr_continue, or dlopen.  Gc.h macro defines
34 | Since 5.0 alpha5, dlopen disables collection temporarily,
{% endraw %}

```
### tools/build/v2/tools/python.jam

```

{% raw %}
983 |     # the Python interpreter. Dynamic libraries opened with dlopen() do not
{% endraw %}

```