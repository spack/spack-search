---
name: "bdw-gc"
layout: package
next_package: libxshmfence
previous_package: mongo-c-driver
languages: ['cpp', 'bash']
---
## 8.0.0
18 / 179 files match

 - [pthread_support.c](#pthread_supportc)
 - [configure.ac](#configureac)
 - [Makefile.direct](#makefiledirect)
 - [ltmain.sh](#ltmainsh)
 - [dyn_load.c](#dyn_loadc)
 - [Makefile.am](#makefileam)
 - [gc_dlopen.c](#gc_dlopenc)
 - [Makefile.in](#makefilein)
 - [include/gc_pthread_redirects.h](#includegc_pthread_redirectsh)
 - [include/gc_config_macros.h](#includegc_config_macrosh)
 - [tests/test.c](#teststestc)
 - [extra/gc.c](#extragcc)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [tools/threadlibs.c](#toolsthreadlibsc)
 - [doc/README.linux](#docreadmelinux)
 - [doc/README.macros](#docreadmemacros)
 - [doc/README.solaris2](#docreadmesolaris2)

### pthread_support.c

```cpp

{% raw %}
127 | #   ifdef GC_USE_DLOPEN_WRAP
166 | #if defined(GC_USE_LD_WRAP) || defined(GC_USE_DLOPEN_WRAP)
210 | #ifdef GC_USE_DLOPEN_WRAP
221 |       dl_handle = dlopen("libpthread.so.0", RTLD_LAZY);
223 |         dl_handle = dlopen("libpthread.so", RTLD_LAZY); /* without ".0" */
1206 |     /* in response to dlopen calls.                             */
{% endraw %}

```
### configure.ac

```

{% raw %}
463 |     AC_CHECK_LIB(dl, dlopen, THREADDLLIBS="$THREADDLLIBS -ldl")
582 |     if test x"${ac_cv_lib_dl_dlopen}" != xyes ; then
584 |          "OpenBSD/Alpha without dlopen(). Shared library support is disabled.")
836 |     AC_DEFINE([GC_USE_DLOPEN_WRAP], 1, [See doc/README.macros.])
{% endraw %}

```
### Makefile.direct

```

{% raw %}
55 | # -DGC_USE_DLOPEN_WRAP -DREDIRECT_MALLOC=GC_malloc -fpic
84 |   gc_dlopen.o backgraph.o win32_threads.o pthread_start.o \
91 |   typd_mlc.c ptr_chck.c mallocx.c gcj_mlc.c specific.c gc_dlopen.c \
{% endraw %}

```
### ltmain.sh

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
### dyn_load.c

```cpp

{% raw %}
20 |  * that this is a bug in the design of the dlopen interface.  THIS CODE
33 | /* BTL: avoid circular redefinition of dlopen if GC_SOLARIS_THREADS defined */
34 | #undef GC_MUST_RESTORE_REDEFINED_DLOPEN
35 | #if defined(GC_PTHREADS) && !defined(GC_NO_DLOPEN) \
37 |   /* To support threads in Solaris, gc.h interposes on dlopen by        */
38 |   /* defining "dlopen" to be "GC_dlopen", which is implemented below.   */
39 |   /* However, both GC_FirstDLOpenedLinkMap() and GC_dlopen() use the    */
40 |   /* real system dlopen() in their implementation. We first remove      */
41 |   /* gc.h's dlopen definition and restore it later, after GC_dlopen().  */
42 | # undef dlopen
43 | # define GC_MUST_RESTORE_REDEFINED_DLOPEN
44 | #endif /* !GC_NO_DLOPEN */
171 |   GC_FirstDLOpenedLinkMap(void)
184 |           void* startupSyms = dlopen(0, RTLD_LAZY);
214 | /* BTL: added to fix circular dlopen definition if GC_SOLARIS_THREADS defined */
215 | # ifdef GC_MUST_RESTORE_REDEFINED_DLOPEN
216 | #   define dlopen GC_dlopen
224 | #   error Fix mutual exclusion with dlopen
232 |   for (lm = GC_FirstDLOpenedLinkMap(); lm != 0; lm = lm->l_next) {
706 | GC_FirstDLOpenedLinkMap(void)
761 |   for (lm = GC_FirstDLOpenedLinkMap(); lm != 0; lm = lm->l_next)
{% endraw %}

```
### Makefile.am

```

{% raw %}
72 |     dyn_load.c finalize.c gc_dlopen.c gcj_mlc.c headers.c \
{% endraw %}

```
### gc_dlopen.c

```cpp

{% raw %}
19 | /* doesn't call dlopen.  Of course this fails if the collector is in    */
21 | #if defined(GC_PTHREADS) && !defined(GC_NO_DLOPEN)
23 | #undef GC_MUST_RESTORE_REDEFINED_DLOPEN
24 | #if defined(dlopen) && !defined(GC_USE_LD_WRAP)
25 |   /* To support various threads pkgs, gc.h interposes on dlopen by      */
26 |   /* defining "dlopen" to be "GC_dlopen", which is implemented below.   */
27 |   /* However, both GC_FirstDLOpenedLinkMap() and GC_dlopen() use the    */
28 |   /* real system dlopen() in their implementation. We first remove      */
29 |   /* gc.h's dlopen definition and restore it later, after GC_dlopen().  */
30 | # undef dlopen
31 | # define GC_MUST_RESTORE_REDEFINED_DLOPEN
35 | /* don't start any.  This is invoked prior to a dlopen call to avoid    */
37 | /* since startup code in dlopen may try to allocate.  This solution     */
39 | /* dlopen calls in either a multi-threaded environment, or if the       */
43 |   static void disable_gc_for_dlopen(void)
55 | /* Redefine dlopen to guarantee mutual exclusion with           */
63 |   void * REAL_DLFUNC(dlopen)(const char *, int);
69 | GC_API void * WRAP_DLFUNC(dlopen)(const char *path, int mode)
76 |     disable_gc_for_dlopen();
78 |   result = REAL_DLFUNC(dlopen)(path, mode);
80 |     GC_enable(); /* undoes disable_gc_for_dlopen */
89 |   GC_API void *GC_dlopen(const char *path, int mode)
91 |     return dlopen(path, mode);
95 | #ifdef GC_MUST_RESTORE_REDEFINED_DLOPEN
96 | # define dlopen GC_dlopen
99 | #endif  /* GC_PTHREADS && !GC_NO_DLOPEN */
{% endraw %}

```
### Makefile.in

```

{% raw %}
239 | 	dyn_load.c finalize.c gc_dlopen.c gcj_mlc.c headers.c \
260 | @SINGLE_GC_OBJ_FALSE@	finalize.lo gc_dlopen.lo gcj_mlc.lo \
1032 | @SINGLE_GC_OBJ_FALSE@	gc_dlopen.c gcj_mlc.c headers.c \
1479 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/gc_dlopen.Plo@am__quote@
{% endraw %}

```
### include/gc_pthread_redirects.h

```cpp

{% raw %}
35 | # ifndef GC_NO_DLOPEN
50 | # ifndef GC_NO_DLOPEN
51 |     GC_API void *GC_dlopen(const char * /* path */, int /* mode */);
52 | # endif /* !GC_NO_DLOPEN */
104 | # ifndef GC_NO_DLOPEN
105 | #   undef dlopen
106 | #   define dlopen GC_dlopen
{% endraw %}

```
### include/gc_config_macros.h

```cpp

{% raw %}
360 |       && !defined(GC_NO_DLOPEN)
361 |     /* Either there is no dlopen() or we do not need to intercept it.   */
362 | #   define GC_NO_DLOPEN
{% endraw %}

```
### tests/test.c

```cpp

{% raw %}
2371 | #     ifndef GC_NO_DLOPEN
2372 |         UNTESTED(GC_dlopen);
{% endraw %}

```
### extra/gc.c

```cpp

{% raw %}
68 | #include "../gc_dlopen.c"
{% endraw %}

```
### m4/libtool.m4

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
### m4/ltoptions.m4

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
### tools/threadlibs.c

```cpp

{% raw %}
24 |         printf("-Wl,--wrap -Wl,dlopen "
32 | #       ifdef GC_USE_DLOPEN_WRAP
41 | #       ifdef GC_USE_DLOPEN_WRAP
{% endraw %}

```
### doc/README.linux

```

{% raw %}
37 |    (for ld) --wrap dlopen --wrap pthread_create \
41 |    (for gcc) -Wl,--wrap -Wl,dlopen -Wl,--wrap -Wl,pthread_create \
48 | 4) Dlopen() disables collection during its execution.  (It can't run
51 |    user startup code may run as part of dlopen().)  Under unusual
64 |    and if dlopen is not used.)
{% endraw %}

```
### doc/README.macros

```

{% raw %}
390 | GC_USE_DLOPEN_WRAP      Causes the collector to redefine malloc and
392 |   dlopen and dlsym to refer to the original versions.  This makes it possible
{% endraw %}

```
### doc/README.solaris2

```

{% raw %}
35 | pthread_join, pthread_detach, or dlopen.  gc.h macro defines these to also do
40 | Since 5.0 alpha5, dlopen disables collection temporarily,
{% endraw %}

```