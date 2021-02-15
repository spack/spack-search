---
name: "charmpp"
layout: package
next_package: py-pysam
previous_package: py-exodus-bundler
languages: ['cpp', 'bash']
---
## 6.9.0
15 / 4475 files match

 - [src/libs/conv-libs/openmp_llvm/runtime/src/z_Linux_util.cpp](#srclibsconv-libsopenmp_llvmruntimesrcz_linux_utilcpp)
 - [src/libs/conv-libs/openmp_llvm/runtime/src/thirdparty/ittnotify/ittnotify_config.h](#srclibsconv-libsopenmp_llvmruntimesrcthirdpartyittnotifyittnotify_configh)
 - [src/util/ckdll_dlopen.C](#srcutilckdll_dlopenc)
 - [src/util/ckdll.C](#srcutilckdllc)
 - [src/scripts/configure.ac](#srcscriptsconfigureac)
 - [src/scripts/Make.depends](#srcscriptsmakedepends)
 - [tests/ampi/privatization/test-cxx.C](#testsampiprivatizationtest-cxxc)
 - [contrib/hwloc/configure.ac](#contribhwlocconfigureac)
 - [contrib/hwloc/config/libtool.m4](#contribhwlocconfiglibtoolm4)
 - [contrib/hwloc/config/ltoptions.m4](#contribhwlocconfigltoptionsm4)
 - [contrib/hwloc/config/hwloc.m4](#contribhwlocconfighwlocm4)
 - [contrib/hwloc/config/ltmain.sh](#contribhwlocconfigltmainsh)
 - [contrib/hwloc/src/components.c](#contribhwlocsrccomponentsc)
 - [contrib/hwloc/include/hwloc/plugins.h](#contribhwlocincludehwlocpluginsh)
 - [contrib/hwloc/contrib/hwloc-valgrind.supp](#contribhwloccontribhwloc-valgrindsupp)

### src/libs/conv-libs/openmp_llvm/runtime/src/z_Linux_util.cpp

```

{% raw %}
1372 |      handler. Mathworks: dlsym() is unsafe. We call dlsym and dlopen
{% endraw %}

```
### src/libs/conv-libs/openmp_llvm/runtime/src/thirdparty/ittnotify/ittnotify_config.h

```cpp

{% raw %}
280 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
{% endraw %}

```
### src/util/ckdll_dlopen.C

```cpp

{% raw %}
1 |  dlopen version of CkDll class.  
8 | #include <dlfcn.h> //for dlopen, etc.
11 | 	handle=dlopen(name,RTLD_NOW);
{% endraw %}

```
### src/util/ckdll.C

```cpp

{% raw %}
14 | #if CMK_DLL_USE_DLOPEN  /*********** UNIX .so/dlopen Version ******/
15 | #include "ckdll_dlopen.C"
{% endraw %}

```
### src/scripts/configure.ac

```

{% raw %}
1971 | #### check if dlopen works ####
1986 | #include "ckdll_dlopen.C"
1992 | test_link "whether dlopen links without $dl_opt" "yes" "no" ""
1994 | test_link "whether dlopen links with $dl_opt" "yes" "no" "$dl_opt"
1997 | #dlopen requires -ldl: add it to our link line
1998 | 	add_flag CMK_LIBS='"$CMK_LIBS '$dl_opt'"' "dlopen"
2003 | # One version or another of dlopen worked: compile it in
2004 | 	AC_DEFINE_UNQUOTED(CMK_DLL_USE_DLOPEN, 1, [dlopen])
{% endraw %}

```
### src/scripts/Make.depends

```

{% raw %}
1959 |  ckdll_dlopen.C ckdll_system.C
{% endraw %}

```
### tests/ampi/privatization/test-cxx.C

```cpp

{% raw %}
61 |   void * dynamiclib = dlopen("libcxx-" privatization_method_str "-shared-library-dynamic.so", RTLD_NOW);
64 |     fprintf(stderr, "dlopen failed: %s\n", dlerror());
{% endraw %}

```
### contrib/hwloc/configure.ac

```

{% raw %}
175 | AM_PROG_LIBTOOL([dlopen win32-dll])
{% endraw %}

```
### contrib/hwloc/config/libtool.m4

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
### contrib/hwloc/config/ltoptions.m4

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
### contrib/hwloc/config/hwloc.m4

```

{% raw %}
1136 |       AC_CHECK_LIB([ltdl], [lt_dlopenext],
1393 |   save_lt_cv_dlopen="$lt_cv_dlopen"
1394 |   save_lt_cv_dlopen_libs="$lt_cv_dlopen_libs"
1395 |   save_lt_cv_dlopen_self="$lt_cv_dlopen_self"
1397 |   # code stolen from LT_SYS_DLOPEN_SELF in libtool.m4
1400 |     lt_cv_dlopen="load_add_on"
1401 |     lt_cv_dlopen_libs=
1402 |     lt_cv_dlopen_self=yes
1406 |     lt_cv_dlopen="LoadLibrary"
1407 |     lt_cv_dlopen_libs=
1411 |     lt_cv_dlopen="dlopen"
1412 |     lt_cv_dlopen_libs=
1417 |     AC_CHECK_LIB([dl], [dlopen],
1418 |                 [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1419 |     lt_cv_dlopen="dyld"
1420 |     lt_cv_dlopen_libs=
1421 |     lt_cv_dlopen_self=yes
1427 |           [lt_cv_dlopen="shl_load"],
1429 |             [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1430 |         [AC_CHECK_FUNC([dlopen],
1431 |               [lt_cv_dlopen="dlopen"],
1432 |           [AC_CHECK_LIB([dl], [dlopen],
1433 |                 [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1434 |             [AC_CHECK_LIB([svld], [dlopen],
1435 |                   [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1437 |                     [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1445 |   # end of code stolen from LT_SYS_DLOPEN_SELF in libtool.m4
1448 |   HWLOC_LIBS_PRIVATE="$HWLOC_LIBS_PRIVATE $lt_cv_dlopen_libs"
1451 |   lt_cv_dlopen="$save_lt_cv_dlopen"
1452 |   lt_cv_dlopen_libs="$save_lt_cv_dlopen_libs"
1453 |   lt_cv_dlopen_self="$save_lt_cv_dlopen_self"
{% endraw %}

```
### contrib/hwloc/config/ltmain.sh

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
### contrib/hwloc/src/components.c

```cpp

{% raw %}
99 |   /* dlopen and get the component structure */
100 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### contrib/hwloc/include/hwloc/plugins.h

```cpp

{% raw %}
356 |  * loaded hwloc (e.g. OpenCL implementations using dlopen with RTLD_LAZY).
370 |   handle = lt_dlopen(NULL);
{% endraw %}

```
### contrib/hwloc/contrib/hwloc-valgrind.supp

```

{% raw %}
32 | # ltdl dlopen global state?
34 |    ltdl_dlopen_doit_leak
40 |    fun:dlopen_doit
{% endraw %}

```