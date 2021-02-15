---
name: "chapel"
layout: package
next_package: umpire
previous_package: perl-alien-svn
languages: ['html', 'cpp', 'bash']
---
## 1.18.0
28 / 7639 files match

 - [make/compiler/Makefile.cray-prgenv](#makecompilermakefilecray-prgenv)
 - [runtime/src/threads/pthreads/threads-pthreads.c](#runtimesrcthreadspthreadsthreads-pthreadsc)
 - [third-party/massivethreads/massivethreads-src/configure.ac](#third-partymassivethreadsmassivethreads-srcconfigureac)
 - [third-party/massivethreads/massivethreads-src/README.md](#third-partymassivethreadsmassivethreads-srcreadmemd)
 - [third-party/massivethreads/massivethreads-src/ltmain.sh](#third-partymassivethreadsmassivethreads-srcltmainsh)
 - [third-party/massivethreads/massivethreads-src/src/Makefile.am](#third-partymassivethreadsmassivethreads-srcsrcmakefileam)
 - [third-party/massivethreads/massivethreads-src/src/myth_real.c](#third-partymassivethreadsmassivethreads-srcsrcmyth_realc)
 - [third-party/massivethreads/massivethreads-src/src/Makefile.in](#third-partymassivethreadsmassivethreads-srcsrcmakefilein)
 - [third-party/massivethreads/massivethreads-src/m4/libtool.m4](#third-partymassivethreadsmassivethreads-srcm4libtoolm4)
 - [third-party/massivethreads/massivethreads-src/m4/ltoptions.m4](#third-partymassivethreadsmassivethreads-srcm4ltoptionsm4)
 - [third-party/gmp/gmp-src/ltmain.sh](#third-partygmpgmp-srcltmainsh)
 - [third-party/gmp/gmp-src/aclocal.m4](#third-partygmpgmp-srcaclocalm4)
 - [third-party/gasnet/gasnet-src/tests/upcr-harness/external-legion/harness.conf](#third-partygasnetgasnet-srctestsupcr-harnessexternal-legionharnessconf)
 - [third-party/hwloc/hwloc-src/configure.ac](#third-partyhwlochwloc-srcconfigureac)
 - [third-party/hwloc/hwloc-src/config/libtool.m4](#third-partyhwlochwloc-srcconfiglibtoolm4)
 - [third-party/hwloc/hwloc-src/config/ltoptions.m4](#third-partyhwlochwloc-srcconfigltoptionsm4)
 - [third-party/hwloc/hwloc-src/config/hwloc.m4](#third-partyhwlochwloc-srcconfighwlocm4)
 - [third-party/hwloc/hwloc-src/config/ltmain.sh](#third-partyhwlochwloc-srcconfigltmainsh)
 - [third-party/hwloc/hwloc-src/src/components.c](#third-partyhwlochwloc-srcsrccomponentsc)
 - [third-party/hwloc/hwloc-src/include/hwloc/plugins.h](#third-partyhwlochwloc-srcincludehwlocpluginsh)
 - [third-party/hwloc/hwloc-src/contrib/hwloc-valgrind.supp](#third-partyhwlochwloc-srccontribhwloc-valgrindsupp)
 - [third-party/hwloc/hwloc-src/doc/doxygen-doc/html/a00191.html](#third-partyhwlochwloc-srcdocdoxygen-dochtmla00191html)
 - [third-party/hwloc/hwloc-src/doc/doxygen-doc/html/a00146_source.html](#third-partyhwlochwloc-srcdocdoxygen-dochtmla00146_sourcehtml)
 - [third-party/hwloc/hwloc-src/doc/doxygen-doc/man/man3/hwlocality_components_core_funcs.3](#third-partyhwlochwloc-srcdocdoxygen-docmanman3hwlocality_components_core_funcs3)
 - [third-party/qthread/qthread-src/config/libtool.m4](#third-partyqthreadqthread-srcconfiglibtoolm4)
 - [third-party/qthread/qthread-src/config/ltoptions.m4](#third-partyqthreadqthread-srcconfigltoptionsm4)
 - [third-party/qthread/qthread-src/config/ltmain.sh](#third-partyqthreadqthread-srcconfigltmainsh)
 - [third-party/jemalloc/jemalloc-src/src/jemalloc.c](#third-partyjemallocjemalloc-srcsrcjemallocc)

### make/compiler/Makefile.cray-prgenv

```

{% raw %}
57 | # libfabric calls dlopen() and getaddrinfo().  With static linking, the
{% endraw %}

```
### runtime/src/threads/pthreads/threads-pthreads.c

```cpp

{% raw %}
429 |   // that cancellation needs to dlopen(3) a shared object, which fails
{% endraw %}

```
### third-party/massivethreads/massivethreads-src/configure.ac

```

{% raw %}
54 | 	                      [build libmyth-dl or not, a library that wraps some system functions with dlopen/dlsym])],
59 | # we will later check if dlopen/dlsym are available and decide if
228 | # check if dlopen is supported
234 | AC_CHECK_LIB(dl, dlopen,
235 | 		 [have_dlopen="yes"],
236 | 		 [have_dlopen="no"])
239 | 	[test x"$enable_myth_dl" = "xyes" -a x"$have_dlopen" = "xyes" ])
{% endraw %}

```
### third-party/massivethreads/massivethreads-src/README.md

```

{% raw %}
61 | If the configure detects that dlopen is supported, it builds a library libmyth-dl.so.
81 | libmyth-dl.so also wraps pthreads functions, but by using dlopen instead of linker options.  It defines pthread_create, etc. and loads the original pthread_create (in libpthread.so) using dlopen and dlsym.  Unlike libmyth-ld.so, you don't need a special linker flag.
{% endraw %}

```
### third-party/massivethreads/massivethreads-src/ltmain.sh

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
7346 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7414 | 	  # This library was specified with -dlopen.
7534 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7545 | 	passes="conv scan dlopen dlpreopen link"
7571 | 	dlopen) libs=$dlfiles ;;
7602 |       if test dlopen = "$pass"; then
7822 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7823 | 	      # If there is no dlopen support or we're linking statically,
7851 | 	dlopen=
7881 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7927 | 	# This library was specified with -dlopen.
7928 | 	if test dlopen = "$pass"; then
7930 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7932 | 	     test yes != "$dlopen_support" ||
7935 | 	    # If there is no dlname, no dlopen support or we're linking
7944 | 	fi # $pass = dlopen
8000 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8002 | 	      # We recover the dlopen module name by 'saving' the la file
8026 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8155 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8156 | 	  dlopenmodule=
8159 | 	      dlopenmodule=$dlpremoduletest
8163 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8260 | 		    # if the lib is a (non-dlopened) module then we cannot
8264 | 		      if test "X$dlopenmodule" != "X$lib"; then
8416 | 	      echo "*** a static module, that should work as long as the dlopening application"
8417 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8561 |       if test dlopen != "$pass"; then
8691 | 	func_warning "'-dlopen' is ignored for archives"
8758 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9455 | 	    echo "*** a static module, that should work as long as the dlopening"
9456 | 	    echo "*** application is linked with the -dlopen flag."
9474 | 	    echo "*** or is declared to -dlopen it."
10086 | 	func_warning "'-dlopen' is ignored for objects"
10206 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10207 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10888 | # The name that we can dlopen(3).
10917 | # Files to dlopen/dlpreopen
10918 | dlopen='$dlfiles'
{% endraw %}

```
### third-party/massivethreads/massivethreads-src/src/Makefile.am

```

{% raw %}
76 | # wrap by dlopen
{% endraw %}

```
### third-party/massivethreads/massivethreads-src/src/myth_real.c

```cpp

{% raw %}
517 |       handle = dlopen(filename, RTLD_LAZY | RTLD_NOLOAD);
{% endraw %}

```
### third-party/massivethreads/massivethreads-src/src/Makefile.in

```

{% raw %}
513 | # wrap by dlopen
{% endraw %}

```
### third-party/massivethreads/massivethreads-src/m4/libtool.m4

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
6141 |     [Compiler flag to allow reflexive dlopens])
6254 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### third-party/massivethreads/massivethreads-src/m4/ltoptions.m4

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
### third-party/gmp/gmp-src/ltmain.sh

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
### third-party/gmp/gmp-src/aclocal.m4

```

{% raw %}
1835 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1838 | m4_defun([_LT_TRY_DLOPEN_SELF],
1896 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1929 | ])# _LT_TRY_DLOPEN_SELF
1932 | # LT_SYS_DLOPEN_SELF
1934 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1936 | if test yes != "$enable_dlopen"; then
1937 |   enable_dlopen=unknown
1938 |   enable_dlopen_self=unknown
1939 |   enable_dlopen_self_static=unknown
1941 |   lt_cv_dlopen=no
1942 |   lt_cv_dlopen_libs=
1946 |     lt_cv_dlopen=load_add_on
1947 |     lt_cv_dlopen_libs=
1948 |     lt_cv_dlopen_self=yes
1952 |     lt_cv_dlopen=LoadLibrary
1953 |     lt_cv_dlopen_libs=
1957 |     lt_cv_dlopen=dlopen
1958 |     lt_cv_dlopen_libs=
1963 |     AC_CHECK_LIB([dl], [dlopen],
1964 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1965 |     lt_cv_dlopen=dyld
1966 |     lt_cv_dlopen_libs=
1967 |     lt_cv_dlopen_self=yes
1974 |     lt_cv_dlopen=dlopen
1975 |     lt_cv_dlopen_libs=
1976 |     lt_cv_dlopen_self=no
1981 | 	  [lt_cv_dlopen=shl_load],
1983 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1984 | 	[AC_CHECK_FUNC([dlopen],
1985 | 	      [lt_cv_dlopen=dlopen],
1986 | 	  [AC_CHECK_LIB([dl], [dlopen],
1987 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1988 | 	    [AC_CHECK_LIB([svld], [dlopen],
1989 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1991 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2000 |   if test no = "$lt_cv_dlopen"; then
2001 |     enable_dlopen=no
2003 |     enable_dlopen=yes
2006 |   case $lt_cv_dlopen in
2007 |   dlopen)
2015 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2017 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2018 | 	  lt_cv_dlopen_self, [dnl
2019 | 	  _LT_TRY_DLOPEN_SELF(
2020 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2021 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2024 |     if test yes = "$lt_cv_dlopen_self"; then
2026 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2027 | 	  lt_cv_dlopen_self_static, [dnl
2028 | 	  _LT_TRY_DLOPEN_SELF(
2029 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2030 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2040 |   case $lt_cv_dlopen_self in
2041 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2042 |   *) enable_dlopen_self=unknown ;;
2045 |   case $lt_cv_dlopen_self_static in
2046 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2047 |   *) enable_dlopen_self_static=unknown ;;
2050 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2051 | 	 [Whether dlopen is supported])
2052 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2053 | 	 [Whether dlopen of programs is supported])
2054 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2055 | 	 [Whether dlopen of statically linked programs is supported])
2056 | ])# LT_SYS_DLOPEN_SELF
2059 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2061 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6136 |     [Compiler flag to allow reflexive dlopens])
6245 |   LT_SYS_DLOPEN_SELF
8440 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8474 | # dlopen
8476 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8479 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8480 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8483 | put the 'dlopen' option into LT_INIT's first parameter.])
8487 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
9001 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### third-party/gasnet/gasnet-src/tests/upcr-harness/external-legion/harness.conf

```

{% raw %}
24 | WarningFilter:  os_cnl ; .*?warning: Using .dlopen. in statically linked applications.*?
{% endraw %}

```
### third-party/hwloc/hwloc-src/configure.ac

```

{% raw %}
175 | AM_PROG_LIBTOOL([dlopen win32-dll])
{% endraw %}

```
### third-party/hwloc/hwloc-src/config/libtool.m4

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
### third-party/hwloc/hwloc-src/config/ltoptions.m4

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
### third-party/hwloc/hwloc-src/config/hwloc.m4

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
### third-party/hwloc/hwloc-src/config/ltmain.sh

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
### third-party/hwloc/hwloc-src/src/components.c

```cpp

{% raw %}
99 |   /* dlopen and get the component structure */
100 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### third-party/hwloc/hwloc-src/include/hwloc/plugins.h

```cpp

{% raw %}
356 |  * loaded hwloc (e.g. OpenCL implementations using dlopen with RTLD_LAZY).
370 |   handle = lt_dlopen(NULL);
{% endraw %}

```
### third-party/hwloc/hwloc-src/contrib/hwloc-valgrind.supp

```

{% raw %}
32 | # ltdl dlopen global state?
34 |    ltdl_dlopen_doit_leak
40 |    fun:dlopen_doit
{% endraw %}

```
### third-party/hwloc/hwloc-src/doc/doxygen-doc/html/a00191.html

```html

{% raw %}
322 | <p>Plugins should call this function in their init() callback to avoid later crashes if lazy symbol resolution is used by the upper layer that loaded hwloc (e.g. OpenCL implementations using dlopen with RTLD_LAZY).</p>
{% endraw %}

```
### third-party/hwloc/hwloc-src/doc/doxygen-doc/html/a00146_source.html

```html

{% raw %}
48 | <div class="fragment"><div class="line"><a name="l00001"></a><span class="lineno">    1</span>&#160;<span class="comment">/*</span></div><div class="line"><a name="l00002"></a><span class="lineno">    2</span>&#160;<span class="comment"> * Copyright © 2013-2015 Inria.  All rights reserved.</span></div><div class="line"><a name="l00003"></a><span class="lineno">    3</span>&#160;<span class="comment"> * See COPYING in top-level directory.</span></div><div class="line"><a name="l00004"></a><span class="lineno">    4</span>&#160;<span class="comment"> */</span></div><div class="line"><a name="l00005"></a><span class="lineno">    5</span>&#160;</div><div class="line"><a name="l00006"></a><span class="lineno">    6</span>&#160;<span class="preprocessor">#ifndef HWLOC_PLUGINS_H</span></div><div class="line"><a name="l00007"></a><span class="lineno">    7</span>&#160;<span class="preprocessor">#define HWLOC_PLUGINS_H</span></div><div class="line"><a name="l00008"></a><span class="lineno">    8</span>&#160;</div><div class="line"><a name="l00013"></a><span class="lineno">   13</span>&#160;<span class="keyword">struct </span><a class="code" href="a00304.html">hwloc_backend</a>;</div><div class="line"><a name="l00014"></a><span class="lineno">   14</span>&#160;</div><div class="line"><a name="l00015"></a><span class="lineno">   15</span>&#160;<span class="preprocessor">#include &lt;hwloc.h&gt;</span></div><div class="line"><a name="l00016"></a><span class="lineno">   16</span>&#160;<span class="preprocessor">#ifdef HWLOC_INSIDE_PLUGIN</span></div><div class="line"><a name="l00017"></a><span class="lineno">   17</span>&#160;<span class="comment">/* needed for hwloc_plugin_check_namespace() */</span></div><div class="line"><a name="l00018"></a><span class="lineno">   18</span>&#160;<span class="preprocessor">#include &lt;ltdl.h&gt;</span></div><div class="line"><a name="l00019"></a><span class="lineno">   19</span>&#160;<span class="preprocessor">#endif</span></div><div class="line"><a name="l00020"></a><span class="lineno">   20</span>&#160;</div><div class="line"><a name="l00021"></a><span class="lineno">   21</span>&#160;</div><div class="line"><a name="l00022"></a><span class="lineno">   22</span>&#160;</div><div class="line"><a name="l00028"></a><span class="lineno"><a class="line" href="a00188.html#ga0dceb95fada01e5e4558429912053ca7">   28</a></span>&#160;<span class="keyword">typedef</span> <span class="keyword">enum</span> <a class="code" href="a00188.html#ga0dceb95fada01e5e4558429912053ca7">hwloc_disc_component_type_e</a> {</div><div class="line"><a name="l00031"></a><span class="lineno"><a class="line" href="a00188.html#gga0dceb95fada01e5e4558429912053ca7aa09e6a39b61eda5364eada626da88ecc">   31</a></span>&#160;  <a class="code" href="a00188.html#gga0dceb95fada01e5e4558429912053ca7aa09e6a39b61eda5364eada626da88ecc">HWLOC_DISC_COMPONENT_TYPE_CPU</a> = (1&lt;&lt;0),</div><div class="line"><a name="l00032"></a><span class="lineno">   32</span>&#160;</div><div class="line"><a name="l00038"></a><span class="lineno"><a class="line" href="a00188.html#gga0dceb95fada01e5e4558429912053ca7a7d7e7114cca4165eee72efb9b39b3d6d">   38</a></span>&#160;  <a class="code" href="a00188.html#gga0dceb95fada01e5e4558429912053ca7a7d7e7114cca4165eee72efb9b39b3d6d">HWLOC_DISC_COMPONENT_TYPE_GLOBAL</a> = (1&lt;&lt;1),</div><div class="line"><a name="l00039"></a><span class="lineno">   39</span>&#160;</div><div class="line"><a name="l00042"></a><span class="lineno"><a class="line" href="a00188.html#gga0dceb95fada01e5e4558429912053ca7aaf4d61f8e2c7c28e88cd81bb565695b7">   42</a></span>&#160;  <a class="code" href="a00188.html#gga0dceb95fada01e5e4558429912053ca7aaf4d61f8e2c7c28e88cd81bb565695b7">HWLOC_DISC_COMPONENT_TYPE_MISC</a> = (1&lt;&lt;2)</div><div class="line"><a name="l00043"></a><span class="lineno">   43</span>&#160;} <a class="code" href="a00188.html#ga5c6112c1a7497e5f481b9634059d47b1">hwloc_disc_component_type_t</a>;</div><div class="line"><a name="l00044"></a><span class="lineno">   44</span>&#160;</div><div class="line"><a name="l00050"></a><span class="lineno"><a class="line" href="a00300.html">   50</a></span>&#160;<span class="keyword">struct </span><a class="code" href="a00300.html">hwloc_disc_component</a> {</div><div class="line"><a name="l00052"></a><span class="lineno"><a class="line" href="a00300.html#ad070350354cbd665803fc86fe48cdb3d">   52</a></span>&#160;  <a class="code" href="a00188.html#ga5c6112c1a7497e5f481b9634059d47b1">hwloc_disc_component_type_t</a> <a class="code" href="a00300.html#ad070350354cbd665803fc86fe48cdb3d">type</a>;</div><div class="line"><a name="l00053"></a><span class="lineno">   53</span>&#160;</div><div class="line"><a name="l00057"></a><span class="lineno"><a class="line" href="a00300.html#a4064c3b5d9213027e87caebef380a840">   57</a></span>&#160;  <span class="keyword">const</span> <span class="keywordtype">char</span> *<a class="code" href="a00300.html#a4064c3b5d9213027e87caebef380a840">name</a>;</div><div class="line"><a name="l00058"></a><span class="lineno">   58</span>&#160;</div><div class="line"><a name="l00067"></a><span class="lineno"><a class="line" href="a00300.html#a34144f4d59bf46524e4875194652412b">   67</a></span>&#160;  <span class="keywordtype">unsigned</span> <a class="code" href="a00300.html#a34144f4d59bf46524e4875194652412b">excludes</a>;</div><div class="line"><a name="l00068"></a><span class="lineno">   68</span>&#160;</div><div class="line"><a name="l00072"></a><span class="lineno"><a class="line" href="a00300.html#ab8390b4bc16e44d5dfcbc35f38065eb7">   72</a></span>&#160;  <span class="keyword">struct </span><a class="code" href="a00304.html">hwloc_backend</a> * (*instantiate)(<span class="keyword">struct </span><a class="code" href="a00300.html">hwloc_disc_component</a> *component, <span class="keyword">const</span> <span class="keywordtype">void</span> *data1, <span class="keyword">const</span> <span class="keywordtype">void</span> *data2, <span class="keyword">const</span> <span class="keywordtype">void</span> *data3);</div><div class="line"><a name="l00073"></a><span class="lineno">   73</span>&#160;</div><div class="line"><a name="l00086"></a><span class="lineno"><a class="line" href="a00300.html#ae86d283c272c5ae24073a235efbf6b59">   86</a></span>&#160;  <span class="keywordtype">unsigned</span> <a class="code" href="a00300.html#ae86d283c272c5ae24073a235efbf6b59">priority</a>;</div><div class="line"><a name="l00087"></a><span class="lineno">   87</span>&#160;</div><div class="line"><a name="l00092"></a><span class="lineno">   92</span>&#160;  <span class="keyword">struct </span><a class="code" href="a00300.html">hwloc_disc_component</a> * next;</div><div class="line"><a name="l00093"></a><span class="lineno">   93</span>&#160;};</div><div class="line"><a name="l00094"></a><span class="lineno">   94</span>&#160;</div><div class="line"><a name="l00114"></a><span class="lineno"><a class="line" href="a00304.html">  114</a></span>&#160;<span class="keyword">struct </span><a class="code" href="a00304.html">hwloc_backend</a> {</div><div class="line"><a name="l00116"></a><span class="lineno">  116</span>&#160;  <span class="keyword">struct </span><a class="code" href="a00300.html">hwloc_disc_component</a> * component;</div><div class="line"><a name="l00118"></a><span class="lineno">  118</span>&#160;  <span class="keyword">struct </span>hwloc_topology * topology;</div><div class="line"><a name="l00120"></a><span class="lineno">  120</span>&#160;  <span class="keywordtype">int</span> envvar_forced;</div><div class="line"><a name="l00122"></a><span class="lineno">  122</span>&#160;  <span class="keyword">struct </span><a class="code" href="a00304.html">hwloc_backend</a> * next;</div><div class="line"><a name="l00123"></a><span class="lineno">  123</span>&#160;</div><div class="line"><a name="l00125"></a><span class="lineno"><a class="line" href="a00304.html#aaa8eafe495aadd81c2e3c4ec527c10ba">  125</a></span>&#160;  <span class="keywordtype">unsigned</span> <span class="keywordtype">long</span> <a class="code" href="a00304.html#aaa8eafe495aadd81c2e3c4ec527c10ba">flags</a>;</div><div class="line"><a name="l00126"></a><span class="lineno">  126</span>&#160;</div><div class="line"><a name="l00130"></a><span class="lineno"><a class="line" href="a00304.html#a5209e6508c110dcd4c3c296466f07cb3">  130</a></span>&#160;  <span class="keywordtype">int</span> <a class="code" href="a00304.html#a5209e6508c110dcd4c3c296466f07cb3">is_custom</a>;</div><div class="line"><a name="l00131"></a><span class="lineno">  131</span>&#160;</div><div class="line"><a name="l00135"></a><span class="lineno"><a class="line" href="a00304.html#ab8806f6db077f1bb2e9d63ec99223f7a">  135</a></span>&#160;  <span class="keywordtype">int</span> <a class="code" href="a00304.html#ab8806f6db077f1bb2e9d63ec99223f7a">is_thissystem</a>;</div><div class="line"><a name="l00136"></a><span class="lineno">  136</span>&#160;</div><div class="line"><a name="l00138"></a><span class="lineno"><a class="line" href="a00304.html#a2ea5bd36b7f06efdb65b98b32af16c68">  138</a></span>&#160;  <span class="keywordtype">void</span> * <a class="code" href="a00304.html#a2ea5bd36b7f06efdb65b98b32af16c68">private_data</a>;</div><div class="line"><a name="l00142"></a><span class="lineno"><a class="line" href="a00304.html#a36c4fa86350525b46340c67b802c69c7">  142</a></span>&#160;  void (*<a class="code" href="a00304.html#a36c4fa86350525b46340c67b802c69c7">disable</a>)(<span class="keyword">struct </span><a class="code" href="a00304.html">hwloc_backend</a> *backend);</div><div class="line"><a name="l00143"></a><span class="lineno">  143</span>&#160;</div><div class="line"><a name="l00147"></a><span class="lineno"><a class="line" href="a00304.html#aeb9e1dcf68853a65355082b359a3a2d7">  147</a></span>&#160;  int (*<a class="code" href="a00304.html#aeb9e1dcf68853a65355082b359a3a2d7">discover</a>)(<span class="keyword">struct </span><a class="code" href="a00304.html">hwloc_backend</a> *backend);</div><div class="line"><a name="l00148"></a><span class="lineno">  148</span>&#160;</div><div class="line"><a name="l00151"></a><span class="lineno"><a class="line" href="a00304.html#ab3d1836eeda1970a4c51342df186581e">  151</a></span>&#160;  int (*<a class="code" href="a00304.html#ab3d1836eeda1970a4c51342df186581e">get_obj_cpuset</a>)(<span class="keyword">struct </span><a class="code" href="a00304.html">hwloc_backend</a> *backend, <span class="keyword">struct </span><a class="code" href="a00304.html">hwloc_backend</a> *caller, <span class="keyword">struct </span><a class="code" href="a00204.html">hwloc_obj</a> *obj, <a class="code" href="a00174.html#gaa3c2bf4c776d603dcebbb61b0c923d84">hwloc_bitmap_t</a> <a class="code" href="a00204.html#a67925e0f2c47f50408fbdb9bddd0790f">cpuset</a>);</div><div class="line"><a name="l00152"></a><span class="lineno">  152</span>&#160;</div><div class="line"><a name="l00156"></a><span class="lineno"><a class="line" href="a00304.html#a5a4803e23309be318d7cdb641a5f1037">  156</a></span>&#160;  int (*notify_new_object)(<span class="keyword">struct </span><a class="code" href="a00304.html">hwloc_backend</a> *backend, <span class="keyword">struct </span><a class="code" href="a00304.html">hwloc_backend</a> *caller, <span class="keyword">struct </span><a class="code" href="a00204.html">hwloc_obj</a> *obj);</div><div class="line"><a name="l00157"></a><span class="lineno">  157</span>&#160;};</div><div class="line"><a name="l00158"></a><span class="lineno">  158</span>&#160;</div><div class="line"><a name="l00160"></a><span class="lineno"><a class="line" href="a00189.html#ga21513209613570877b6bfa9898106f2a">  160</a></span>&#160;<span class="keyword">enum</span> <a class="code" href="a00189.html#ga21513209613570877b6bfa9898106f2a">hwloc_backend_flag_e</a> {</div><div class="line"><a name="l00163"></a><span class="lineno"><a class="line" href="a00189.html#gga21513209613570877b6bfa9898106f2aadc96f2cf3bdd5d41e102dfa1e1976b24">  163</a></span>&#160;  <a class="code" href="a00189.html#gga21513209613570877b6bfa9898106f2aadc96f2cf3bdd5d41e102dfa1e1976b24">HWLOC_BACKEND_FLAG_NEED_LEVELS</a> = (1UL&lt;&lt;0)</div><div class="line"><a name="l00164"></a><span class="lineno">  164</span>&#160;};</div><div class="line"><a name="l00165"></a><span class="lineno">  165</span>&#160;</div><div class="line"><a name="l00169"></a><span class="lineno">  169</span>&#160;HWLOC_DECLSPEC <span class="keyword">struct </span><a class="code" href="a00304.html">hwloc_backend</a> * <a class="code" href="a00189.html#ga330a0b581de4817d0cf1e7401db22436">hwloc_backend_alloc</a>(<span class="keyword">struct</span> <a class="code" href="a00300.html">hwloc_disc_component</a> *component);</div><div class="line"><a name="l00170"></a><span class="lineno">  170</span>&#160;</div><div class="line"><a name="l00172"></a><span class="lineno">  172</span>&#160;HWLOC_DECLSPEC <span class="keywordtype">int</span> <a class="code" href="a00189.html#gaa4edf46c5d88eef53b3b8f572d88b9c5">hwloc_backend_enable</a>(<span class="keyword">struct</span> hwloc_topology *topology, <span class="keyword">struct</span> <a class="code" href="a00304.html">hwloc_backend</a> *backend);</div><div class="line"><a name="l00173"></a><span class="lineno">  173</span>&#160;</div><div class="line"><a name="l00179"></a><span class="lineno">  179</span>&#160;HWLOC_DECLSPEC <span class="keywordtype">int</span> <a class="code" href="a00189.html#ga505a5470745bf0b601f4d25a69601411">hwloc_backends_get_obj_cpuset</a>(<span class="keyword">struct</span> <a class="code" href="a00304.html">hwloc_backend</a> *caller, <span class="keyword">struct</span> <a class="code" href="a00204.html">hwloc_obj</a> *obj, <a class="code" href="a00174.html#gaa3c2bf4c776d603dcebbb61b0c923d84">hwloc_bitmap_t</a> cpuset);</div><div class="line"><a name="l00180"></a><span class="lineno">  180</span>&#160;</div><div class="line"><a name="l00190"></a><span class="lineno">  190</span>&#160;HWLOC_DECLSPEC <span class="keywordtype">int</span> <a class="code" href="a00189.html#gad8ac8bba9ab6b9af423baba0c8337c6b">hwloc_backends_notify_new_object</a>(<span class="keyword">struct</span> <a class="code" href="a00304.html">hwloc_backend</a> *caller, <span class="keyword">struct</span> <a class="code" href="a00204.html">hwloc_obj</a> *obj);</div><div class="line"><a name="l00191"></a><span class="lineno">  191</span>&#160;</div><div class="line"><a name="l00202"></a><span class="lineno"><a class="line" href="a00190.html#ga397a1bf7d21dd073320ad0045340f463">  202</a></span>&#160;<span class="keyword">typedef</span> <span class="keyword">enum</span> <a class="code" href="a00190.html#ga397a1bf7d21dd073320ad0045340f463">hwloc_component_type_e</a> {</div><div class="line"><a name="l00204"></a><span class="lineno"><a class="line" href="a00190.html#gga397a1bf7d21dd073320ad0045340f463a5d6e561f467fe9795a29e7368b613900">  204</a></span>&#160;  <a class="code" href="a00190.html#gga397a1bf7d21dd073320ad0045340f463a5d6e561f467fe9795a29e7368b613900">HWLOC_COMPONENT_TYPE_DISC</a>,</div><div class="line"><a name="l00205"></a><span class="lineno">  205</span>&#160;</div><div class="line"><a name="l00207"></a><span class="lineno"><a class="line" href="a00190.html#gga397a1bf7d21dd073320ad0045340f463adea00cd839c2141c032e1569fd5592bd">  207</a></span>&#160;  <a class="code" href="a00190.html#gga397a1bf7d21dd073320ad0045340f463adea00cd839c2141c032e1569fd5592bd">HWLOC_COMPONENT_TYPE_XML</a></div><div class="line"><a name="l00208"></a><span class="lineno">  208</span>&#160;} <a class="code" href="a00190.html#ga0aebfa65317af10bb18d7d35f6dc05b8">hwloc_component_type_t</a>;</div><div class="line"><a name="l00209"></a><span class="lineno">  209</span>&#160;</div><div class="line"><a name="l00215"></a><span class="lineno"><a class="line" href="a00308.html">  215</a></span>&#160;<span class="keyword">struct </span><a class="code" href="a00308.html">hwloc_component</a> {</div><div class="line"><a name="l00217"></a><span class="lineno"><a class="line" href="a00308.html#a3250bd6fc9713946991d805e48091b2e">  217</a></span>&#160;  <span class="keywordtype">unsigned</span> <a class="code" href="a00308.html#a3250bd6fc9713946991d805e48091b2e">abi</a>;</div><div class="line"><a name="l00218"></a><span class="lineno">  218</span>&#160;</div><div class="line"><a name="l00236"></a><span class="lineno"><a class="line" href="a00308.html#aea613546886d9b8221cadba920fe3ebc">  236</a></span>&#160;  int (*init)(<span class="keywordtype">unsigned</span> <span class="keywordtype">long</span> flags);</div><div class="line"><a name="l00237"></a><span class="lineno">  237</span>&#160;</div><div class="line"><a name="l00249"></a><span class="lineno"><a class="line" href="a00308.html#a4612015451a1c706e8ba19114cb8baae">  249</a></span>&#160;  void (*finalize)(<span class="keywordtype">unsigned</span> <span class="keywordtype">long</span> flags);</div><div class="line"><a name="l00250"></a><span class="lineno">  250</span>&#160;</div><div class="line"><a name="l00252"></a><span class="lineno"><a class="line" href="a00308.html#a789208ada7e17492cfd3a5a88a6bb0ee">  252</a></span>&#160;  hwloc_component_type_t <a class="code" href="a00308.html#a789208ada7e17492cfd3a5a88a6bb0ee">type</a>;</div><div class="line"><a name="l00253"></a><span class="lineno">  253</span>&#160;</div><div class="line"><a name="l00255"></a><span class="lineno"><a class="line" href="a00308.html#ab8043c5b4cc0e81aabba586ccb194335">  255</a></span>&#160;  <span class="keywordtype">unsigned</span> <span class="keywordtype">long</span> <a class="code" href="a00308.html#ab8043c5b4cc0e81aabba586ccb194335">flags</a>;</div><div class="line"><a name="l00256"></a><span class="lineno">  256</span>&#160;</div><div class="line"><a name="l00258"></a><span class="lineno"><a class="line" href="a00308.html#a4b8cffd1d943c29fdc102b841b8598d4">  258</a></span>&#160;  <span class="keywordtype">void</span> * <a class="code" href="a00308.html#a4b8cffd1d943c29fdc102b841b8598d4">data</a>;</div><div class="line"><a name="l00259"></a><span class="lineno">  259</span>&#160;};</div><div class="line"><a name="l00260"></a><span class="lineno">  260</span>&#160;</div><div class="line"><a name="l00290"></a><span class="lineno">  290</span>&#160;HWLOC_DECLSPEC <span class="keyword">struct </span><a class="code" href="a00204.html">hwloc_obj</a> *<a class="code" href="a00191.html#gafd853fd67e12c32916201d8303ef39d2">hwloc_insert_object_by_cpuset</a>(<span class="keyword">struct</span> hwloc_topology *topology, <a class="code" href="a00204.html">hwloc_obj_t</a> obj);</div><div class="line"><a name="l00291"></a><span class="lineno">  291</span>&#160;</div><div class="line"><a name="l00293"></a><span class="lineno"><a class="line" href="a00191.html#ga1ac8191022b0d3b1bf0070e11d1f1155">  293</a></span>&#160;<span class="keyword">typedef</span> void (*<a class="code" href="a00191.html#ga1ac8191022b0d3b1bf0070e11d1f1155">hwloc_report_error_t</a>)(<span class="keyword">const</span> <span class="keywordtype">char</span> * msg, <span class="keywordtype">int</span> line);</div><div class="line"><a name="l00295"></a><span class="lineno">  295</span>&#160;HWLOC_DECLSPEC <span class="keywordtype">void</span> <a class="code" href="a00191.html#ga3ae154590328522a864f4a7fb453b562">hwloc_report_os_error</a>(<span class="keyword">const</span> <span class="keywordtype">char</span> * msg, <span class="keywordtype">int</span> line);</div><div class="line"><a name="l00297"></a><span class="lineno">  297</span>&#160;HWLOC_DECLSPEC <span class="keywordtype">int</span> <a class="code" href="a00191.html#gab527c1e0f243f057d31a724794ad9f88">hwloc_hide_errors</a>(<span class="keywordtype">void</span>);</div><div class="line"><a name="l00298"></a><span class="lineno">  298</span>&#160;</div><div class="line"><a name="l00303"></a><span class="lineno">  303</span>&#160;HWLOC_DECLSPEC <span class="keyword">struct </span><a class="code" href="a00204.html">hwloc_obj</a> *<a class="code" href="a00191.html#ga56d4e5fec377bf09f136b4e8e280e30f">hwloc__insert_object_by_cpuset</a>(<span class="keyword">struct</span> hwloc_topology *topology, <a class="code" href="a00204.html">hwloc_obj_t</a> obj, <a class="code" href="a00191.html#ga1ac8191022b0d3b1bf0070e11d1f1155">hwloc_report_error_t</a> report_error);</div><div class="line"><a name="l00304"></a><span class="lineno">  304</span>&#160;</div><div class="line"><a name="l00319"></a><span class="lineno">  319</span>&#160;HWLOC_DECLSPEC <span class="keywordtype">void</span> <a class="code" href="a00191.html#ga0ef97debde503b56367689b07bb3e901">hwloc_insert_object_by_parent</a>(<span class="keyword">struct</span> hwloc_topology *topology, <a class="code" href="a00204.html">hwloc_obj_t</a> <a class="code" href="a00204.html#adc494f6aed939992be1c55cca5822900">parent</a>, <a class="code" href="a00204.html">hwloc_obj_t</a> obj);</div><div class="line"><a name="l00320"></a><span class="lineno">  320</span>&#160;</div><div class="line"><a name="l00322"></a><span class="lineno">  322</span>&#160;<span class="keyword">static</span> __hwloc_inline <span class="keyword">struct </span><a class="code" href="a00204.html">hwloc_obj</a> *</div><div class="line"><a name="l00323"></a><span class="lineno"><a class="line" href="a00191.html#ga64d210fcfd7e517095319420bf40ed0a">  323</a></span>&#160;<a class="code" href="a00191.html#ga64d210fcfd7e517095319420bf40ed0a">hwloc_alloc_setup_object</a>(<a class="code" href="a00151.html#gacd37bb612667dc437d66bfb175a8dc55">hwloc_obj_type_t</a> <a class="code" href="a00300.html#ad070350354cbd665803fc86fe48cdb3d">type</a>, <span class="keywordtype">signed</span> <a class="code" href="a00204.html#a61a7a80a68eaccbaaa28269e678c81a9">os_index</a>)</div><div class="line"><a name="l00324"></a><span class="lineno">  324</span>&#160;{</div><div class="line"><a name="l00325"></a><span class="lineno">  325</span>&#160;  <span class="keyword">struct </span><a class="code" href="a00204.html">hwloc_obj</a> *obj = malloc(<span class="keyword">sizeof</span>(*obj));</div><div class="line"><a name="l00326"></a><span class="lineno">  326</span>&#160;  memset(obj, 0, <span class="keyword">sizeof</span>(*obj));</div><div class="line"><a name="l00327"></a><span class="lineno">  327</span>&#160;  obj-&gt;<a class="code" href="a00204.html#acc4f0803f244867e68fe0036800be5de">type</a> = <a class="code" href="a00300.html#ad070350354cbd665803fc86fe48cdb3d">type</a>;</div><div class="line"><a name="l00328"></a><span class="lineno">  328</span>&#160;  obj-&gt;<a class="code" href="a00204.html#a61a7a80a68eaccbaaa28269e678c81a9">os_index</a> = <a class="code" href="a00204.html#a61a7a80a68eaccbaaa28269e678c81a9">os_index</a>;</div><div class="line"><a name="l00329"></a><span class="lineno">  329</span>&#160;  obj-&gt;<a class="code" href="a00204.html#a68766f0b1c4d61b5bad87e3b81dacfde">os_level</a> = -1;</div><div class="line"><a name="l00330"></a><span class="lineno">  330</span>&#160;  obj-&gt;<a class="code" href="a00204.html#accd40e29f71f19e88db62ea3df02adc8">attr</a> = malloc(<span class="keyword">sizeof</span>(*obj-&gt;<a class="code" href="a00204.html#accd40e29f71f19e88db62ea3df02adc8">attr</a>));</div><div class="line"><a name="l00331"></a><span class="lineno">  331</span>&#160;  memset(obj-&gt;<a class="code" href="a00204.html#accd40e29f71f19e88db62ea3df02adc8">attr</a>, 0, <span class="keyword">sizeof</span>(*obj-&gt;<a class="code" href="a00204.html#accd40e29f71f19e88db62ea3df02adc8">attr</a>));</div><div class="line"><a name="l00332"></a><span class="lineno">  332</span>&#160;  <span class="comment">/* do not allocate the cpuset here, let the caller do it */</span></div><div class="line"><a name="l00333"></a><span class="lineno">  333</span>&#160;  <span class="keywordflow">return</span> obj;</div><div class="line"><a name="l00334"></a><span class="lineno">  334</span>&#160;}</div><div class="line"><a name="l00335"></a><span class="lineno">  335</span>&#160;</div><div class="line"><a name="l00342"></a><span class="lineno">  342</span>&#160;HWLOC_DECLSPEC <span class="keywordtype">int</span> <a class="code" href="a00191.html#gabb240e5b856a34963078ccec9a785ac1">hwloc_fill_object_sets</a>(<a class="code" href="a00204.html">hwloc_obj_t</a> obj);</div><div class="line"><a name="l00343"></a><span class="lineno">  343</span>&#160;</div><div class="line"><a name="l00365"></a><span class="lineno">  365</span>&#160;<span class="keyword">static</span> __hwloc_inline <span class="keywordtype">int</span></div><div class="line"><a name="l00366"></a><span class="lineno"><a class="line" href="a00191.html#gac2eaed287bb215cf0bd33014e9e1d374">  366</a></span>&#160;<a class="code" href="a00191.html#gac2eaed287bb215cf0bd33014e9e1d374">hwloc_plugin_check_namespace</a>(<span class="keyword">const</span> <span class="keywordtype">char</span> *pluginname __hwloc_attribute_unused, <span class="keyword">const</span> <span class="keywordtype">char</span> *symbol __hwloc_attribute_unused)</div><div class="line"><a name="l00367"></a><span class="lineno">  367</span>&#160;{</div><div class="line"><a name="l00368"></a><span class="lineno">  368</span>&#160;<span class="preprocessor">#ifdef HWLOC_INSIDE_PLUGIN</span></div><div class="line"><a name="l00369"></a><span class="lineno">  369</span>&#160;  lt_dlhandle handle;</div><div class="line"><a name="l00370"></a><span class="lineno">  370</span>&#160;  <span class="keywordtype">void</span> *sym;</div><div class="line"><a name="l00371"></a><span class="lineno">  371</span>&#160;  handle = lt_dlopen(NULL);</div><div class="line"><a name="l00372"></a><span class="lineno">  372</span>&#160;  <span class="keywordflow">if</span> (!handle)</div><div class="line"><a name="l00373"></a><span class="lineno">  373</span>&#160;    <span class="comment">/* cannot check, assume things will work */</span></div><div class="line"><a name="l00374"></a><span class="lineno">  374</span>&#160;    <span class="keywordflow">return</span> 0;</div><div class="line"><a name="l00375"></a><span class="lineno">  375</span>&#160;  sym = lt_dlsym(handle, symbol);</div><div class="line"><a name="l00376"></a><span class="lineno">  376</span>&#160;  lt_dlclose(handle);</div><div class="line"><a name="l00377"></a><span class="lineno">  377</span>&#160;  <span class="keywordflow">if</span> (!sym) {</div><div class="line"><a name="l00378"></a><span class="lineno">  378</span>&#160;    <span class="keyword">static</span> <span class="keywordtype">int</span> verboseenv_checked = 0;</div><div class="line"><a name="l00379"></a><span class="lineno">  379</span>&#160;    <span class="keyword">static</span> <span class="keywordtype">int</span> verboseenv_value = 0;</div><div class="line"><a name="l00380"></a><span class="lineno">  380</span>&#160;    <span class="keywordflow">if</span> (!verboseenv_checked) {</div><div class="line"><a name="l00381"></a><span class="lineno">  381</span>&#160;      <span class="keyword">const</span> <span class="keywordtype">char</span> *verboseenv = getenv(<span class="stringliteral">&quot;HWLOC_PLUGINS_VERBOSE&quot;</span>);</div><div class="line"><a name="l00382"></a><span class="lineno">  382</span>&#160;      verboseenv_value = verboseenv ? atoi(verboseenv) : 0;</div><div class="line"><a name="l00383"></a><span class="lineno">  383</span>&#160;      verboseenv_checked = 1;</div><div class="line"><a name="l00384"></a><span class="lineno">  384</span>&#160;    }</div><div class="line"><a name="l00385"></a><span class="lineno">  385</span>&#160;    <span class="keywordflow">if</span> (verboseenv_value)</div><div class="line"><a name="l00386"></a><span class="lineno">  386</span>&#160;      fprintf(stderr, <span class="stringliteral">&quot;Plugin `%s&#39; disabling itself because it cannot find the `%s&#39; core symbol.\n&quot;</span>,</div><div class="line"><a name="l00387"></a><span class="lineno">  387</span>&#160;              pluginname, symbol);</div><div class="line"><a name="l00388"></a><span class="lineno">  388</span>&#160;    <span class="keywordflow">return</span> -1;</div><div class="line"><a name="l00389"></a><span class="lineno">  389</span>&#160;  }</div><div class="line"><a name="l00390"></a><span class="lineno">  390</span>&#160;<span class="preprocessor">#endif </span><span class="comment">/* HWLOC_INSIDE_PLUGIN */</span><span class="preprocessor"></span></div><div class="line"><a name="l00391"></a><span class="lineno">  391</span>&#160;  <span class="keywordflow">return</span> 0;</div><div class="line"><a name="l00392"></a><span class="lineno">  392</span>&#160;}</div><div class="line"><a name="l00393"></a><span class="lineno">  393</span>&#160;</div><div class="line"><a name="l00411"></a><span class="lineno">  411</span>&#160;HWLOC_DECLSPEC <span class="keywordtype">int</span> <a class="code" href="a00192.html#ga2ea3e9c02eabd8c5768745c8a99d7fed">hwloc_insert_pci_device_list</a>(<span class="keyword">struct</span> <a class="code" href="a00304.html">hwloc_backend</a> *backend, <span class="keyword">struct</span> <a class="code" href="a00204.html">hwloc_obj</a> *first_obj);</div><div class="line"><a name="l00412"></a><span class="lineno">  412</span>&#160;</div><div class="line"><a name="l00417"></a><span class="lineno">  417</span>&#160;HWLOC_DECLSPEC <span class="keywordtype">unsigned</span> <a class="code" href="a00192.html#ga4bed8bd79337d4bc84b884a6ccd14f16">hwloc_pci_find_cap</a>(<span class="keyword">const</span> <span class="keywordtype">unsigned</span> <span class="keywordtype">char</span> *config, <span class="keywordtype">unsigned</span> cap);</div><div class="line"><a name="l00418"></a><span class="lineno">  418</span>&#160;</div><div class="line"><a name="l00424"></a><span class="lineno">  424</span>&#160;HWLOC_DECLSPEC <span class="keywordtype">int</span> <a class="code" href="a00192.html#ga749e75eeea108be0608fcba7c113f736">hwloc_pci_find_linkspeed</a>(<span class="keyword">const</span> <span class="keywordtype">unsigned</span> <span class="keywordtype">char</span> *config, <span class="keywordtype">unsigned</span> offset, <span class="keywordtype">float</span> *linkspeed);</div><div class="line"><a name="l00425"></a><span class="lineno">  425</span>&#160;</div><div class="line"><a name="l00432"></a><span class="lineno">  432</span>&#160;HWLOC_DECLSPEC <span class="keywordtype">int</span> <a class="code" href="a00192.html#ga80fa1e3d882b5c2225dd6dd01e098ad0">hwloc_pci_prepare_bridge</a>(<a class="code" href="a00204.html">hwloc_obj_t</a> obj, <span class="keyword">const</span> <span class="keywordtype">unsigned</span> <span class="keywordtype">char</span> *config);</div><div class="line"><a name="l00433"></a><span class="lineno">  433</span>&#160;</div><div class="line"><a name="l00439"></a><span class="lineno">  439</span>&#160;<span class="preprocessor">#endif </span><span class="comment">/* HWLOC_PLUGINS_H */</span><span class="preprocessor"></span></div><div class="ttc" id="a00191_html_gab527c1e0f243f057d31a724794ad9f88"><div class="ttname"><a href="a00191.html#gab527c1e0f243f057d31a724794ad9f88">hwloc_hide_errors</a></div><div class="ttdeci">int hwloc_hide_errors(void)</div><div class="ttdoc">Check whether insertion errors are hidden. </div></div>
{% endraw %}

```
### third-party/hwloc/hwloc-src/doc/doxygen-doc/man/man3/hwlocality_components_core_funcs.3

```

{% raw %}
106 | Plugins should call this function in their init() callback to avoid later crashes if lazy symbol resolution is used by the upper layer that loaded hwloc (e\&.g\&. OpenCL implementations using dlopen with RTLD_LAZY)\&.
{% endraw %}

```
### third-party/qthread/qthread-src/config/libtool.m4

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
### third-party/qthread/qthread-src/config/ltoptions.m4

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
### third-party/qthread/qthread-src/config/ltmain.sh

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
### third-party/jemalloc/jemalloc-src/src/jemalloc.c

```cpp

{% raw %}
2066 |  * glibc provides the RTLD_DEEPBIND flag for dlopen which can make it possible
{% endraw %}

```