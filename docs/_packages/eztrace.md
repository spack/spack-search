---
name: "eztrace"
layout: package
next_package: postgis
previous_package: ntirpc
languages: ['cpp', 'bash']
---
## 1.1-10
36 / 1095 files match

 - [configure.ac](#configureac)
 - [extlib/gtg/ltmain.sh](#extlibgtgltmainsh)
 - [extlib/gtg/aclocal.m4](#extlibgtgaclocalm4)
 - [extlib/gtg/extlib/otf/config/ltmain.sh](#extlibgtgextlibotfconfigltmainsh)
 - [extlib/gtg/extlib/otf/config/m4/libtool.m4](#extlibgtgextlibotfconfigm4libtoolm4)
 - [extlib/gtg/extlib/otf/config/m4/ltoptions.m4](#extlibgtgextlibotfconfigm4ltoptionsm4)
 - [extlib/gtg/extlib/otf/autom4te.cache/output.3](#extlibgtgextlibotfautom4tecacheoutput3)
 - [extlib/gtg/extlib/otf/autom4te.cache/output.0](#extlibgtgextlibotfautom4tecacheoutput0)
 - [extlib/gtg/extlib/otf/autom4te.cache/traces.3](#extlibgtgextlibotfautom4tecachetraces3)
 - [extlib/gtg/extlib/otf/autom4te.cache/output.1](#extlibgtgextlibotfautom4tecacheoutput1)
 - [extlib/gtg/extlib/otf/autom4te.cache/output.2](#extlibgtgextlibotfautom4tecacheoutput2)
 - [extlib/gtg/extlib/otf/autom4te.cache/traces.0](#extlibgtgextlibotfautom4tecachetraces0)
 - [extlib/gtg/extlib/otf/autom4te.cache/traces.2](#extlibgtgextlibotfautom4tecachetraces2)
 - [extlib/gtg/autom4te.cache/output.2](#extlibgtgautom4tecacheoutput2)
 - [extlib/gtg/autom4te.cache/traces.2](#extlibgtgautom4tecachetraces2)
 - [extlib/litl/ltmain.sh](#extliblitlltmainsh)
 - [extlib/litl/autom4te.cache/output.1](#extliblitlautom4tecacheoutput1)
 - [extlib/litl/autom4te.cache/output.2](#extliblitlautom4tecacheoutput2)
 - [extlib/litl/autom4te.cache/traces.2](#extliblitlautom4tecachetraces2)
 - [extlib/litl/m4/libtool.m4](#extliblitlm4libtoolm4)
 - [extlib/litl/m4/ltoptions.m4](#extliblitlm4ltoptionsm4)
 - [extlib/opari2/build-config/ltmain.sh](#extlibopari2build-configltmainsh)
 - [extlib/opari2/vendor/common/build-config/m4/libtool.m4](#extlibopari2vendorcommonbuild-configm4libtoolm4)
 - [extlib/opari2/vendor/common/build-config/m4/ltoptions.m4](#extlibopari2vendorcommonbuild-configm4ltoptionsm4)
 - [extlib/opari2/build-frontend/autom4te.cache/output.3](#extlibopari2build-frontendautom4tecacheoutput3)
 - [extlib/opari2/build-frontend/autom4te.cache/output.0](#extlibopari2build-frontendautom4tecacheoutput0)
 - [extlib/opari2/build-frontend/autom4te.cache/traces.3](#extlibopari2build-frontendautom4tecachetraces3)
 - [extlib/opari2/build-frontend/autom4te.cache/output.1](#extlibopari2build-frontendautom4tecacheoutput1)
 - [extlib/opari2/build-frontend/autom4te.cache/output.2](#extlibopari2build-frontendautom4tecacheoutput2)
 - [extlib/opari2/build-frontend/autom4te.cache/traces.0](#extlibopari2build-frontendautom4tecachetraces0)
 - [extlib/opari2/build-frontend/autom4te.cache/traces.4](#extlibopari2build-frontendautom4tecachetraces4)
 - [extlib/opari2/build-frontend/autom4te.cache/output.4](#extlibopari2build-frontendautom4tecacheoutput4)
 - [extlib/opari2/build-frontend/autom4te.cache/traces.2](#extlibopari2build-frontendautom4tecachetraces2)
 - [src/pptrace/pptrace.c](#srcpptracepptracec)
 - [src/core/eztrace_convert_core.c](#srccoreeztrace_convert_corec)
 - [test/pptrace/perf/tests/libpreload.c](#testpptraceperftestslibpreloadc)

### configure.ac

```

{% raw %}
325 | dlopen_method=openat
326 | AC_ARG_WITH(dlopen_method,
327 | 	    [AS_HELP_STRING([--with-dlopen_method],
330 | 		     dlopen_method=open
332 | 		 [ dlopen_method=openat ])
334 | AC_MSG_RESULT(dlopen method: $dlopen_method)
336 | AM_CONDITIONAL([USE_OPENAT], [test x"$dlopen_method" = xopenat])
{% endraw %}

```
### extlib/gtg/ltmain.sh

```bash

{% raw %}
2335 |     opt_dlopen=
2408 |         --dlopen|-dlopen)
2409 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2532 |       # Only execute mode is allowed to have -dlopen flags.
2533 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2534 |         func_error "unrecognized option '-dlopen'"
3760 |   -dlopen FILE      add the directory containing FILE to the library path
3762 | This mode sets the library path environment variable according to '-dlopen'
3817 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3826 |   -module           build a library that can dlopened
3934 |     # Handle -dlopen flags immediately.
3935 |     for file in $opt_dlopen; do
3954 | 	# Skip this library if it cannot be dlopened.
3981 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6674 | 	    dlopen_self=$dlopen_self_static
6680 | 	    dlopen_self=$dlopen_self_static
6686 | 	    dlopen_self=$dlopen_self_static
6744 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6834 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7001 |       -dlopen)
7441 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7509 | 	  # This library was specified with -dlopen.
7629 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7640 | 	passes="conv scan dlopen dlpreopen link"
7666 | 	dlopen) libs=$dlfiles ;;
7697 |       if test dlopen = "$pass"; then
7917 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7918 | 	      # If there is no dlopen support or we're linking statically,
7946 | 	dlopen=
7976 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8022 | 	# This library was specified with -dlopen.
8023 | 	if test dlopen = "$pass"; then
8025 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8027 | 	     test yes != "$dlopen_support" ||
8030 | 	    # If there is no dlname, no dlopen support or we're linking
8039 | 	fi # $pass = dlopen
8095 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8097 | 	      # We recover the dlopen module name by 'saving' the la file
8121 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8250 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8251 | 	  dlopenmodule=
8254 | 	      dlopenmodule=$dlpremoduletest
8258 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8355 | 		    # if the lib is a (non-dlopened) module then we cannot
8359 | 		      if test "X$dlopenmodule" != "X$lib"; then
8511 | 	      echo "*** a static module, that should work as long as the dlopening application"
8512 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8656 |       if test dlopen != "$pass"; then
8786 | 	func_warning "'-dlopen' is ignored for archives"
8853 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9550 | 	    echo "*** a static module, that should work as long as the dlopening"
9551 | 	    echo "*** application is linked with the -dlopen flag."
9569 | 	    echo "*** or is declared to -dlopen it."
10181 | 	func_warning "'-dlopen' is ignored for objects"
10301 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10302 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10983 | # The name that we can dlopen(3).
11012 | # Files to dlopen/dlpreopen
11013 | dlopen='$dlfiles'
{% endraw %}

```
### extlib/gtg/aclocal.m4

```

{% raw %}
1834 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1837 | m4_defun([_LT_TRY_DLOPEN_SELF],
1895 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1928 | ])# _LT_TRY_DLOPEN_SELF
1931 | # LT_SYS_DLOPEN_SELF
1933 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1935 | if test yes != "$enable_dlopen"; then
1936 |   enable_dlopen=unknown
1937 |   enable_dlopen_self=unknown
1938 |   enable_dlopen_self_static=unknown
1940 |   lt_cv_dlopen=no
1941 |   lt_cv_dlopen_libs=
1945 |     lt_cv_dlopen=load_add_on
1946 |     lt_cv_dlopen_libs=
1947 |     lt_cv_dlopen_self=yes
1951 |     lt_cv_dlopen=LoadLibrary
1952 |     lt_cv_dlopen_libs=
1956 |     lt_cv_dlopen=dlopen
1957 |     lt_cv_dlopen_libs=
1962 |     AC_CHECK_LIB([dl], [dlopen],
1963 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1964 |     lt_cv_dlopen=dyld
1965 |     lt_cv_dlopen_libs=
1966 |     lt_cv_dlopen_self=yes
1973 |     lt_cv_dlopen=dlopen
1974 |     lt_cv_dlopen_libs=
1975 |     lt_cv_dlopen_self=no
1980 | 	  [lt_cv_dlopen=shl_load],
1982 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1983 | 	[AC_CHECK_FUNC([dlopen],
1984 | 	      [lt_cv_dlopen=dlopen],
1985 | 	  [AC_CHECK_LIB([dl], [dlopen],
1986 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1987 | 	    [AC_CHECK_LIB([svld], [dlopen],
1988 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1990 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1999 |   if test no = "$lt_cv_dlopen"; then
2000 |     enable_dlopen=no
2002 |     enable_dlopen=yes
2005 |   case $lt_cv_dlopen in
2006 |   dlopen)
2014 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2016 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2017 | 	  lt_cv_dlopen_self, [dnl
2018 | 	  _LT_TRY_DLOPEN_SELF(
2019 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2020 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2023 |     if test yes = "$lt_cv_dlopen_self"; then
2025 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2026 | 	  lt_cv_dlopen_self_static, [dnl
2027 | 	  _LT_TRY_DLOPEN_SELF(
2028 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2029 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2039 |   case $lt_cv_dlopen_self in
2040 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2041 |   *) enable_dlopen_self=unknown ;;
2044 |   case $lt_cv_dlopen_self_static in
2045 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2046 |   *) enable_dlopen_self_static=unknown ;;
2049 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2050 | 	 [Whether dlopen is supported])
2051 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2052 | 	 [Whether dlopen of programs is supported])
2053 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2054 | 	 [Whether dlopen of statically linked programs is supported])
2055 | ])# LT_SYS_DLOPEN_SELF
2058 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2060 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6161 |     [Compiler flag to allow reflexive dlopens])
6270 |   LT_SYS_DLOPEN_SELF
8465 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8499 | # dlopen
8501 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8504 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8505 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8508 | put the 'dlopen' option into LT_INIT's first parameter.])
8512 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
9026 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### extlib/gtg/extlib/otf/config/ltmain.sh

```bash

{% raw %}
2335 |     opt_dlopen=
2408 |         --dlopen|-dlopen)
2409 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2532 |       # Only execute mode is allowed to have -dlopen flags.
2533 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2534 |         func_error "unrecognized option '-dlopen'"
3760 |   -dlopen FILE      add the directory containing FILE to the library path
3762 | This mode sets the library path environment variable according to '-dlopen'
3817 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3826 |   -module           build a library that can dlopened
3934 |     # Handle -dlopen flags immediately.
3935 |     for file in $opt_dlopen; do
3954 | 	# Skip this library if it cannot be dlopened.
3981 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6674 | 	    dlopen_self=$dlopen_self_static
6680 | 	    dlopen_self=$dlopen_self_static
6686 | 	    dlopen_self=$dlopen_self_static
6744 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6834 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7001 |       -dlopen)
7441 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7509 | 	  # This library was specified with -dlopen.
7629 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7640 | 	passes="conv scan dlopen dlpreopen link"
7666 | 	dlopen) libs=$dlfiles ;;
7697 |       if test dlopen = "$pass"; then
7917 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7918 | 	      # If there is no dlopen support or we're linking statically,
7946 | 	dlopen=
7976 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8022 | 	# This library was specified with -dlopen.
8023 | 	if test dlopen = "$pass"; then
8025 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8027 | 	     test yes != "$dlopen_support" ||
8030 | 	    # If there is no dlname, no dlopen support or we're linking
8039 | 	fi # $pass = dlopen
8095 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8097 | 	      # We recover the dlopen module name by 'saving' the la file
8121 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8250 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8251 | 	  dlopenmodule=
8254 | 	      dlopenmodule=$dlpremoduletest
8258 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8355 | 		    # if the lib is a (non-dlopened) module then we cannot
8359 | 		      if test "X$dlopenmodule" != "X$lib"; then
8511 | 	      echo "*** a static module, that should work as long as the dlopening application"
8512 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8656 |       if test dlopen != "$pass"; then
8786 | 	func_warning "'-dlopen' is ignored for archives"
8853 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9550 | 	    echo "*** a static module, that should work as long as the dlopening"
9551 | 	    echo "*** application is linked with the -dlopen flag."
9569 | 	    echo "*** or is declared to -dlopen it."
10181 | 	func_warning "'-dlopen' is ignored for objects"
10301 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10302 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10983 | # The name that we can dlopen(3).
11012 | # Files to dlopen/dlpreopen
11013 | dlopen='$dlfiles'
{% endraw %}

```
### extlib/gtg/extlib/otf/config/m4/libtool.m4

```

{% raw %}
1820 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1823 | m4_defun([_LT_TRY_DLOPEN_SELF],
1881 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1914 | ])# _LT_TRY_DLOPEN_SELF
1917 | # LT_SYS_DLOPEN_SELF
1919 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1921 | if test yes != "$enable_dlopen"; then
1922 |   enable_dlopen=unknown
1923 |   enable_dlopen_self=unknown
1924 |   enable_dlopen_self_static=unknown
1926 |   lt_cv_dlopen=no
1927 |   lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen=load_add_on
1932 |     lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen_self=yes
1937 |     lt_cv_dlopen=LoadLibrary
1938 |     lt_cv_dlopen_libs=
1942 |     lt_cv_dlopen=dlopen
1943 |     lt_cv_dlopen_libs=
1948 |     AC_CHECK_LIB([dl], [dlopen],
1949 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1950 |     lt_cv_dlopen=dyld
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1959 |     lt_cv_dlopen=dlopen
1960 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen_self=no
1966 | 	  [lt_cv_dlopen=shl_load],
1968 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1969 | 	[AC_CHECK_FUNC([dlopen],
1970 | 	      [lt_cv_dlopen=dlopen],
1971 | 	  [AC_CHECK_LIB([dl], [dlopen],
1972 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1973 | 	    [AC_CHECK_LIB([svld], [dlopen],
1974 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1976 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1985 |   if test no = "$lt_cv_dlopen"; then
1986 |     enable_dlopen=no
1988 |     enable_dlopen=yes
1991 |   case $lt_cv_dlopen in
1992 |   dlopen)
2000 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2002 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2003 | 	  lt_cv_dlopen_self, [dnl
2004 | 	  _LT_TRY_DLOPEN_SELF(
2005 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2006 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2009 |     if test yes = "$lt_cv_dlopen_self"; then
2011 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2012 | 	  lt_cv_dlopen_self_static, [dnl
2013 | 	  _LT_TRY_DLOPEN_SELF(
2014 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2015 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2025 |   case $lt_cv_dlopen_self in
2026 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2027 |   *) enable_dlopen_self=unknown ;;
2030 |   case $lt_cv_dlopen_self_static in
2031 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2032 |   *) enable_dlopen_self_static=unknown ;;
2035 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2036 | 	 [Whether dlopen is supported])
2037 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2038 | 	 [Whether dlopen of programs is supported])
2039 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2040 | 	 [Whether dlopen of statically linked programs is supported])
2041 | ])# LT_SYS_DLOPEN_SELF
2044 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2046 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6147 |     [Compiler flag to allow reflexive dlopens])
6260 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extlib/gtg/extlib/otf/config/m4/ltoptions.m4

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
### extlib/gtg/extlib/otf/autom4te.cache/output.3

```

{% raw %}
8622 |         enable_dlopen=no
11995 |   if test "x$enable_dlopen" != xyes; then
11996 |   enable_dlopen=unknown
11997 |   enable_dlopen_self=unknown
11998 |   enable_dlopen_self_static=unknown
12000 |   lt_cv_dlopen=no
12001 |   lt_cv_dlopen_libs=
12005 |     lt_cv_dlopen="load_add_on"
12006 |     lt_cv_dlopen_libs=
12007 |     lt_cv_dlopen_self=yes
12011 |     lt_cv_dlopen="LoadLibrary"
12012 |     lt_cv_dlopen_libs=
12016 |     lt_cv_dlopen="dlopen"
12017 |     lt_cv_dlopen_libs=
12022 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12023 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12024 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12038 | char dlopen ();
12042 | return dlopen ();
12048 |   ac_cv_lib_dl_dlopen=yes
12050 |   ac_cv_lib_dl_dlopen=no
12056 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12057 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12058 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12059 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12062 |     lt_cv_dlopen="dyld"
12063 |     lt_cv_dlopen_libs=
12064 |     lt_cv_dlopen_self=yes
12073 |   lt_cv_dlopen="shl_load"
12112 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
12114 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
12115 | if test "x$ac_cv_func_dlopen" = xyes; then :
12116 |   lt_cv_dlopen="dlopen"
12118 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12119 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12120 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12134 | char dlopen ();
12138 | return dlopen ();
12144 |   ac_cv_lib_dl_dlopen=yes
12146 |   ac_cv_lib_dl_dlopen=no
12152 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12153 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12154 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12155 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12157 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
12158 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
12159 | if ${ac_cv_lib_svld_dlopen+:} false; then :
12173 | char dlopen ();
12177 | return dlopen ();
12183 |   ac_cv_lib_svld_dlopen=yes
12185 |   ac_cv_lib_svld_dlopen=no
12191 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
12192 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
12193 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
12194 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12233 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
12254 |   if test "x$lt_cv_dlopen" != xno; then
12255 |     enable_dlopen=yes
12257 |     enable_dlopen=no
12260 |   case $lt_cv_dlopen in
12261 |   dlopen)
12269 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12271 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
12272 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12273 | if ${lt_cv_dlopen_self+:} false; then :
12277 |   lt_cv_dlopen_self=cross
12332 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12359 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12360 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12361 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12365 |     lt_cv_dlopen_self=no
12372 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
12373 | $as_echo "$lt_cv_dlopen_self" >&6; }
12375 |     if test "x$lt_cv_dlopen_self" = xyes; then
12377 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
12378 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12379 | if ${lt_cv_dlopen_self_static+:} false; then :
12383 |   lt_cv_dlopen_self_static=cross
12438 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12465 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12466 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12467 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12471 |     lt_cv_dlopen_self_static=no
12478 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
12479 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12488 |   case $lt_cv_dlopen_self in
12489 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12490 |   *) enable_dlopen_self=unknown ;;
12493 |   case $lt_cv_dlopen_self_static in
12494 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12495 |   *) enable_dlopen_self_static=unknown ;;
19183 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
19184 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
19185 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
20404 | # Whether dlopen is supported.
20405 | dlopen_support=$enable_dlopen
20407 | # Whether dlopen of programs is supported.
20408 | dlopen_self=$enable_dlopen_self
20410 | # Whether dlopen of statically linked programs is supported.
20411 | dlopen_self_static=$enable_dlopen_self_static
20455 | # Compiler flag to allow reflexive dlopens.
20797 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/gtg/extlib/otf/autom4te.cache/output.0

```

{% raw %}
8824 |         enable_dlopen=no
12494 |   if test yes != "$enable_dlopen"; then
12495 |   enable_dlopen=unknown
12496 |   enable_dlopen_self=unknown
12497 |   enable_dlopen_self_static=unknown
12499 |   lt_cv_dlopen=no
12500 |   lt_cv_dlopen_libs=
12504 |     lt_cv_dlopen=load_add_on
12505 |     lt_cv_dlopen_libs=
12506 |     lt_cv_dlopen_self=yes
12510 |     lt_cv_dlopen=LoadLibrary
12511 |     lt_cv_dlopen_libs=
12515 |     lt_cv_dlopen=dlopen
12516 |     lt_cv_dlopen_libs=
12521 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12522 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12523 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12537 | char dlopen ();
12541 | return dlopen ();
12547 |   ac_cv_lib_dl_dlopen=yes
12549 |   ac_cv_lib_dl_dlopen=no
12555 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12556 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12557 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12558 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
12561 |     lt_cv_dlopen=dyld
12562 |     lt_cv_dlopen_libs=
12563 |     lt_cv_dlopen_self=yes
12572 |     lt_cv_dlopen=dlopen
12573 |     lt_cv_dlopen_libs=
12574 |     lt_cv_dlopen_self=no
12580 |   lt_cv_dlopen=shl_load
12619 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
12621 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
12622 | if test "x$ac_cv_func_dlopen" = xyes; then :
12623 |   lt_cv_dlopen=dlopen
12625 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12626 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12627 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12641 | char dlopen ();
12645 | return dlopen ();
12651 |   ac_cv_lib_dl_dlopen=yes
12653 |   ac_cv_lib_dl_dlopen=no
12659 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12660 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12661 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12662 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
12664 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
12665 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
12666 | if ${ac_cv_lib_svld_dlopen+:} false; then :
12680 | char dlopen ();
12684 | return dlopen ();
12690 |   ac_cv_lib_svld_dlopen=yes
12692 |   ac_cv_lib_svld_dlopen=no
12698 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
12699 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
12700 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
12701 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
12740 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
12761 |   if test no = "$lt_cv_dlopen"; then
12762 |     enable_dlopen=no
12764 |     enable_dlopen=yes
12767 |   case $lt_cv_dlopen in
12768 |   dlopen)
12776 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12778 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
12779 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12780 | if ${lt_cv_dlopen_self+:} false; then :
12784 |   lt_cv_dlopen_self=cross
12839 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12866 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12867 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12868 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12872 |     lt_cv_dlopen_self=no
12879 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
12880 | $as_echo "$lt_cv_dlopen_self" >&6; }
12882 |     if test yes = "$lt_cv_dlopen_self"; then
12884 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
12885 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12886 | if ${lt_cv_dlopen_self_static+:} false; then :
12890 |   lt_cv_dlopen_self_static=cross
12945 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12972 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12973 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12974 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12978 |     lt_cv_dlopen_self_static=no
12985 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
12986 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12995 |   case $lt_cv_dlopen_self in
12996 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12997 |   *) enable_dlopen_self=unknown ;;
13000 |   case $lt_cv_dlopen_self_static in
13001 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
13002 |   *) enable_dlopen_self_static=unknown ;;
19829 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
19830 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
19831 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
21064 | # Whether dlopen is supported.
21065 | dlopen_support=$enable_dlopen
21067 | # Whether dlopen of programs is supported.
21068 | dlopen_self=$enable_dlopen_self
21070 | # Whether dlopen of statically linked programs is supported.
21071 | dlopen_self_static=$enable_dlopen_self_static
21115 | # Compiler flag to allow reflexive dlopens.
21357 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/gtg/extlib/otf/autom4te.cache/traces.3

```

{% raw %}
244 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
288 | eval "LTDLOPEN=\"$libname_spec\""
289 | AC_SUBST([LTDLOPEN])
291 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
292 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
293 |   [lt_cv_sys_dlopen_deplibs],
294 |   [# PORTME does your system automatically load deplibs for dlopen?
298 |   lt_cv_sys_dlopen_deplibs=unknown
303 |     lt_cv_sys_dlopen_deplibs=unknown
306 |     lt_cv_sys_dlopen_deplibs=yes
311 |       lt_cv_sys_dlopen_deplibs=no
318 |     lt_cv_sys_dlopen_deplibs=yes
321 |     lt_cv_sys_dlopen_deplibs=yes
325 |     lt_cv_sys_dlopen_deplibs=yes
328 |     lt_cv_sys_dlopen_deplibs=yes
331 |     lt_cv_sys_dlopen_deplibs=yes
336 |     lt_cv_sys_dlopen_deplibs=unknown
340 |     # at 6.2 and later dlopen does load deplibs.
341 |     lt_cv_sys_dlopen_deplibs=yes
344 |     lt_cv_sys_dlopen_deplibs=yes
347 |     lt_cv_sys_dlopen_deplibs=yes
350 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
353 |     lt_cv_sys_dlopen_deplibs=no
356 |     # dlopen *does* load deplibs and with the right loader patch applied
362 |     lt_cv_sys_dlopen_deplibs=unknown
369 |     lt_cv_sys_dlopen_deplibs=yes
372 |     lt_cv_sys_dlopen_deplibs=yes
375 |     lt_cv_sys_dlopen_deplibs=yes
378 |     libltdl_cv_sys_dlopen_deplibs=yes
382 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
383 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
384 |     [Define if the OS needs help to load dependent libraries for dlopen().])
387 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
388 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
390 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
456 | LIBADD_DLOPEN=
457 | AC_SEARCH_LIBS([dlopen], [dl],
460 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
461 | 	  LIBADD_DLOPEN="-ldl"
463 | 	libltdl_cv_lib_dl_dlopen="yes"
464 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
468 |     ]], [[dlopen(0, 0);]])],
471 | 	    libltdl_cv_func_dlopen="yes"
472 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
473 | 	[AC_CHECK_LIB([svld], [dlopen],
476 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
477 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
478 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
481 |   LIBS="$LIBS $LIBADD_DLOPEN"
485 | AC_SUBST([LIBADD_DLOPEN])
491 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
495 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
505 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
508 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
512 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
519 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
535 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
584 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
585 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
590 |           LIBS="$LIBS $LIBADD_DLOPEN"
591 | 	  _LT_TRY_DLOPEN_SELF(
1964 | m4trace:config/m4/libtool.m4:1858: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
1965 | if test "x$enable_dlopen" != xyes; then
1966 |   enable_dlopen=unknown
1967 |   enable_dlopen_self=unknown
1968 |   enable_dlopen_self_static=unknown
1970 |   lt_cv_dlopen=no
1971 |   lt_cv_dlopen_libs=
1975 |     lt_cv_dlopen="load_add_on"
1976 |     lt_cv_dlopen_libs=
1977 |     lt_cv_dlopen_self=yes
1981 |     lt_cv_dlopen="LoadLibrary"
1982 |     lt_cv_dlopen_libs=
1986 |     lt_cv_dlopen="dlopen"
1987 |     lt_cv_dlopen_libs=
1992 |     AC_CHECK_LIB([dl], [dlopen],
1993 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1994 |     lt_cv_dlopen="dyld"
1995 |     lt_cv_dlopen_libs=
1996 |     lt_cv_dlopen_self=yes
2002 | 	  [lt_cv_dlopen="shl_load"],
2004 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
2005 | 	[AC_CHECK_FUNC([dlopen],
2006 | 	      [lt_cv_dlopen="dlopen"],
2007 | 	  [AC_CHECK_LIB([dl], [dlopen],
2008 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2009 | 	    [AC_CHECK_LIB([svld], [dlopen],
2010 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2012 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
2021 |   if test "x$lt_cv_dlopen" != xno; then
2022 |     enable_dlopen=yes
2024 |     enable_dlopen=no
2027 |   case $lt_cv_dlopen in
2028 |   dlopen)
2036 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2038 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2039 | 	  lt_cv_dlopen_self, [dnl
2040 | 	  _LT_TRY_DLOPEN_SELF(
2041 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2042 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2045 |     if test "x$lt_cv_dlopen_self" = xyes; then
2047 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2048 | 	  lt_cv_dlopen_self_static, [dnl
2049 | 	  _LT_TRY_DLOPEN_SELF(
2050 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2051 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2061 |   case $lt_cv_dlopen_self in
2062 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2063 |   *) enable_dlopen_self=unknown ;;
2066 |   case $lt_cv_dlopen_self_static in
2067 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2068 |   *) enable_dlopen_self_static=unknown ;;
2071 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2072 | 	 [Whether dlopen is supported])
2073 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2074 | 	 [Whether dlopen of programs is supported])
2075 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2076 | 	 [Whether dlopen of statically linked programs is supported])
2078 | m4trace:config/m4/libtool.m4:1975: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2079 | m4trace:config/m4/libtool.m4:1975: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2081 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2377 | m4trace:config/m4/ltoptions.m4:111: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2380 | put the `dlopen' option into LT_INIT's first parameter.])
2382 | m4trace:config/m4/ltoptions.m4:111: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2384 | _LT_SET_OPTION([LT_INIT], [dlopen])
2387 | put the `dlopen' option into LT_INIT's first parameter.])
2479 | m4trace:config/m4/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
3666 | m4trace:configure.ac:53: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extlib/gtg/extlib/otf/autom4te.cache/output.1

```

{% raw %}
8824 |         enable_dlopen=no
12494 |   if test yes != "$enable_dlopen"; then
12495 |   enable_dlopen=unknown
12496 |   enable_dlopen_self=unknown
12497 |   enable_dlopen_self_static=unknown
12499 |   lt_cv_dlopen=no
12500 |   lt_cv_dlopen_libs=
12504 |     lt_cv_dlopen=load_add_on
12505 |     lt_cv_dlopen_libs=
12506 |     lt_cv_dlopen_self=yes
12510 |     lt_cv_dlopen=LoadLibrary
12511 |     lt_cv_dlopen_libs=
12515 |     lt_cv_dlopen=dlopen
12516 |     lt_cv_dlopen_libs=
12521 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12522 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12523 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12537 | char dlopen ();
12541 | return dlopen ();
12547 |   ac_cv_lib_dl_dlopen=yes
12549 |   ac_cv_lib_dl_dlopen=no
12555 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12556 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12557 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12558 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
12561 |     lt_cv_dlopen=dyld
12562 |     lt_cv_dlopen_libs=
12563 |     lt_cv_dlopen_self=yes
12572 |     lt_cv_dlopen=dlopen
12573 |     lt_cv_dlopen_libs=
12574 |     lt_cv_dlopen_self=no
12580 |   lt_cv_dlopen=shl_load
12619 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
12621 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
12622 | if test "x$ac_cv_func_dlopen" = xyes; then :
12623 |   lt_cv_dlopen=dlopen
12625 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12626 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12627 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12641 | char dlopen ();
12645 | return dlopen ();
12651 |   ac_cv_lib_dl_dlopen=yes
12653 |   ac_cv_lib_dl_dlopen=no
12659 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12660 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12661 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12662 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
12664 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
12665 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
12666 | if ${ac_cv_lib_svld_dlopen+:} false; then :
12680 | char dlopen ();
12684 | return dlopen ();
12690 |   ac_cv_lib_svld_dlopen=yes
12692 |   ac_cv_lib_svld_dlopen=no
12698 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
12699 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
12700 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
12701 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
12740 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
12761 |   if test no = "$lt_cv_dlopen"; then
12762 |     enable_dlopen=no
12764 |     enable_dlopen=yes
12767 |   case $lt_cv_dlopen in
12768 |   dlopen)
12776 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12778 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
12779 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12780 | if ${lt_cv_dlopen_self+:} false; then :
12784 |   lt_cv_dlopen_self=cross
12839 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12866 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12867 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12868 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12872 |     lt_cv_dlopen_self=no
12879 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
12880 | $as_echo "$lt_cv_dlopen_self" >&6; }
12882 |     if test yes = "$lt_cv_dlopen_self"; then
12884 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
12885 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12886 | if ${lt_cv_dlopen_self_static+:} false; then :
12890 |   lt_cv_dlopen_self_static=cross
12945 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12972 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12973 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12974 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12978 |     lt_cv_dlopen_self_static=no
12985 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
12986 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12995 |   case $lt_cv_dlopen_self in
12996 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12997 |   *) enable_dlopen_self=unknown ;;
13000 |   case $lt_cv_dlopen_self_static in
13001 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
13002 |   *) enable_dlopen_self_static=unknown ;;
19829 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
19830 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
19831 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
21064 | # Whether dlopen is supported.
21065 | dlopen_support=$enable_dlopen
21067 | # Whether dlopen of programs is supported.
21068 | dlopen_self=$enable_dlopen_self
21070 | # Whether dlopen of statically linked programs is supported.
21071 | dlopen_self_static=$enable_dlopen_self_static
21115 | # Compiler flag to allow reflexive dlopens.
21357 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/gtg/extlib/otf/autom4te.cache/output.2

```

{% raw %}
8827 |         enable_dlopen=no
12491 |   if test yes != "$enable_dlopen"; then
12492 |   enable_dlopen=unknown
12493 |   enable_dlopen_self=unknown
12494 |   enable_dlopen_self_static=unknown
12496 |   lt_cv_dlopen=no
12497 |   lt_cv_dlopen_libs=
12501 |     lt_cv_dlopen=load_add_on
12502 |     lt_cv_dlopen_libs=
12503 |     lt_cv_dlopen_self=yes
12507 |     lt_cv_dlopen=LoadLibrary
12508 |     lt_cv_dlopen_libs=
12512 |     lt_cv_dlopen=dlopen
12513 |     lt_cv_dlopen_libs=
12518 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12519 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12520 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12534 | char dlopen ();
12538 | return dlopen ();
12544 |   ac_cv_lib_dl_dlopen=yes
12546 |   ac_cv_lib_dl_dlopen=no
12552 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12553 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12554 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12555 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
12558 |     lt_cv_dlopen=dyld
12559 |     lt_cv_dlopen_libs=
12560 |     lt_cv_dlopen_self=yes
12569 |     lt_cv_dlopen=dlopen
12570 |     lt_cv_dlopen_libs=
12571 |     lt_cv_dlopen_self=no
12577 |   lt_cv_dlopen=shl_load
12616 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
12618 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
12619 | if test "x$ac_cv_func_dlopen" = xyes; then :
12620 |   lt_cv_dlopen=dlopen
12622 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12623 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12624 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12638 | char dlopen ();
12642 | return dlopen ();
12648 |   ac_cv_lib_dl_dlopen=yes
12650 |   ac_cv_lib_dl_dlopen=no
12656 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12657 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12658 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12659 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
12661 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
12662 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
12663 | if ${ac_cv_lib_svld_dlopen+:} false; then :
12677 | char dlopen ();
12681 | return dlopen ();
12687 |   ac_cv_lib_svld_dlopen=yes
12689 |   ac_cv_lib_svld_dlopen=no
12695 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
12696 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
12697 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
12698 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
12737 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
12758 |   if test no = "$lt_cv_dlopen"; then
12759 |     enable_dlopen=no
12761 |     enable_dlopen=yes
12764 |   case $lt_cv_dlopen in
12765 |   dlopen)
12773 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12775 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
12776 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12777 | if ${lt_cv_dlopen_self+:} false; then :
12781 |   lt_cv_dlopen_self=cross
12836 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12863 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12864 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12865 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12869 |     lt_cv_dlopen_self=no
12876 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
12877 | $as_echo "$lt_cv_dlopen_self" >&6; }
12879 |     if test yes = "$lt_cv_dlopen_self"; then
12881 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
12882 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12883 | if ${lt_cv_dlopen_self_static+:} false; then :
12887 |   lt_cv_dlopen_self_static=cross
12942 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12969 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12970 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12971 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12975 |     lt_cv_dlopen_self_static=no
12982 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
12983 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12992 |   case $lt_cv_dlopen_self in
12993 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12994 |   *) enable_dlopen_self=unknown ;;
12997 |   case $lt_cv_dlopen_self_static in
12998 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12999 |   *) enable_dlopen_self_static=unknown ;;
19826 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
19827 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
19828 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
21061 | # Whether dlopen is supported.
21062 | dlopen_support=$enable_dlopen
21064 | # Whether dlopen of programs is supported.
21065 | dlopen_self=$enable_dlopen_self
21067 | # Whether dlopen of statically linked programs is supported.
21068 | dlopen_self_static=$enable_dlopen_self_static
21112 | # Compiler flag to allow reflexive dlopens.
21354 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/gtg/extlib/otf/autom4te.cache/traces.0

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
290 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
291 |   [lt_cv_sys_dlopen_deplibs],
292 |   [# PORTME does your system automatically load deplibs for dlopen?
296 |   lt_cv_sys_dlopen_deplibs=unknown
301 |     lt_cv_sys_dlopen_deplibs=unknown
304 |     lt_cv_sys_dlopen_deplibs=yes
309 |       lt_cv_sys_dlopen_deplibs=no
314 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
326 |     lt_cv_sys_dlopen_deplibs=yes
329 |     lt_cv_sys_dlopen_deplibs=yes
332 |     lt_cv_sys_dlopen_deplibs=yes
337 |     lt_cv_sys_dlopen_deplibs=unknown
341 |     # at 6.2 and later dlopen does load deplibs.
342 |     lt_cv_sys_dlopen_deplibs=yes
345 |     lt_cv_sys_dlopen_deplibs=yes
348 |     lt_cv_sys_dlopen_deplibs=yes
351 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
354 |     lt_cv_sys_dlopen_deplibs=no
357 |     # dlopen *does* load deplibs and with the right loader patch applied
363 |     lt_cv_sys_dlopen_deplibs=unknown
370 |     lt_cv_sys_dlopen_deplibs=yes
373 |     lt_cv_sys_dlopen_deplibs=yes
376 |     lt_cv_sys_dlopen_deplibs=yes
379 |     libltdl_cv_sys_dlopen_deplibs=yes
383 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
384 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
385 |     [Define if the OS needs help to load dependent libraries for dlopen().])
388 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
391 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
463 | LIBADD_DLOPEN=
464 | AC_SEARCH_LIBS([dlopen], [dl],
467 | 	if test "$ac_cv_search_dlopen" != "none required"; then
468 | 	  LIBADD_DLOPEN=-ldl
470 | 	libltdl_cv_lib_dl_dlopen=yes
471 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
475 |     ]], [[dlopen(0, 0);]])],
478 | 	    libltdl_cv_func_dlopen=yes
479 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
480 | 	[AC_CHECK_LIB([svld], [dlopen],
483 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
484 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
485 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
488 |   LIBS="$LIBS $LIBADD_DLOPEN"
492 | AC_SUBST([LIBADD_DLOPEN])
498 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
502 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
512 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
515 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
519 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
526 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
542 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
594 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
599 |       LIBS="$LIBS $LIBADD_DLOPEN"
657 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
2041 | m4trace:config/m4/libtool.m4:1920: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
2042 | if test yes != "$enable_dlopen"; then
2043 |   enable_dlopen=unknown
2044 |   enable_dlopen_self=unknown
2045 |   enable_dlopen_self_static=unknown
2047 |   lt_cv_dlopen=no
2048 |   lt_cv_dlopen_libs=
2052 |     lt_cv_dlopen=load_add_on
2053 |     lt_cv_dlopen_libs=
2054 |     lt_cv_dlopen_self=yes
2058 |     lt_cv_dlopen=LoadLibrary
2059 |     lt_cv_dlopen_libs=
2063 |     lt_cv_dlopen=dlopen
2064 |     lt_cv_dlopen_libs=
2069 |     AC_CHECK_LIB([dl], [dlopen],
2070 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
2071 |     lt_cv_dlopen=dyld
2072 |     lt_cv_dlopen_libs=
2073 |     lt_cv_dlopen_self=yes
2080 |     lt_cv_dlopen=dlopen
2081 |     lt_cv_dlopen_libs=
2082 |     lt_cv_dlopen_self=no
2087 | 	  [lt_cv_dlopen=shl_load],
2089 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
2090 | 	[AC_CHECK_FUNC([dlopen],
2091 | 	      [lt_cv_dlopen=dlopen],
2092 | 	  [AC_CHECK_LIB([dl], [dlopen],
2093 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
2094 | 	    [AC_CHECK_LIB([svld], [dlopen],
2095 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
2097 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2106 |   if test no = "$lt_cv_dlopen"; then
2107 |     enable_dlopen=no
2109 |     enable_dlopen=yes
2112 |   case $lt_cv_dlopen in
2113 |   dlopen)
2121 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2123 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2124 | 	  lt_cv_dlopen_self, [dnl
2125 | 	  _LT_TRY_DLOPEN_SELF(
2126 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2127 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2130 |     if test yes = "$lt_cv_dlopen_self"; then
2132 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2133 | 	  lt_cv_dlopen_self_static, [dnl
2134 | 	  _LT_TRY_DLOPEN_SELF(
2135 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2136 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2146 |   case $lt_cv_dlopen_self in
2147 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2148 |   *) enable_dlopen_self=unknown ;;
2151 |   case $lt_cv_dlopen_self_static in
2152 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2153 |   *) enable_dlopen_self_static=unknown ;;
2156 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2157 | 	 [Whether dlopen is supported])
2158 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2159 | 	 [Whether dlopen of programs is supported])
2160 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2161 | 	 [Whether dlopen of statically linked programs is supported])
2163 | m4trace:config/m4/libtool.m4:2045: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2164 | m4trace:config/m4/libtool.m4:2045: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2166 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2475 | m4trace:config/m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2478 | put the 'dlopen' option into LT_INIT's first parameter.])
2480 | m4trace:config/m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2482 | _LT_SET_OPTION([LT_INIT], [dlopen])
2485 | put the 'dlopen' option into LT_INIT's first parameter.])
2577 | m4trace:config/m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
3768 | m4trace:configure.ac:53: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extlib/gtg/extlib/otf/autom4te.cache/traces.2

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
290 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
291 |   [lt_cv_sys_dlopen_deplibs],
292 |   [# PORTME does your system automatically load deplibs for dlopen?
296 |   lt_cv_sys_dlopen_deplibs=unknown
301 |     lt_cv_sys_dlopen_deplibs=unknown
304 |     lt_cv_sys_dlopen_deplibs=yes
309 |       lt_cv_sys_dlopen_deplibs=no
314 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
326 |     lt_cv_sys_dlopen_deplibs=yes
329 |     lt_cv_sys_dlopen_deplibs=yes
332 |     lt_cv_sys_dlopen_deplibs=yes
337 |     lt_cv_sys_dlopen_deplibs=unknown
341 |     # at 6.2 and later dlopen does load deplibs.
342 |     lt_cv_sys_dlopen_deplibs=yes
345 |     lt_cv_sys_dlopen_deplibs=yes
348 |     lt_cv_sys_dlopen_deplibs=yes
351 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
354 |     lt_cv_sys_dlopen_deplibs=no
357 |     # dlopen *does* load deplibs and with the right loader patch applied
363 |     lt_cv_sys_dlopen_deplibs=unknown
370 |     lt_cv_sys_dlopen_deplibs=yes
373 |     lt_cv_sys_dlopen_deplibs=yes
376 |     lt_cv_sys_dlopen_deplibs=yes
379 |     libltdl_cv_sys_dlopen_deplibs=yes
383 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
384 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
385 |     [Define if the OS needs help to load dependent libraries for dlopen().])
388 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
391 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
463 | LIBADD_DLOPEN=
464 | AC_SEARCH_LIBS([dlopen], [dl],
467 | 	if test "$ac_cv_search_dlopen" != "none required"; then
468 | 	  LIBADD_DLOPEN=-ldl
470 | 	libltdl_cv_lib_dl_dlopen=yes
471 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
475 |     ]], [[dlopen(0, 0);]])],
478 | 	    libltdl_cv_func_dlopen=yes
479 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
480 | 	[AC_CHECK_LIB([svld], [dlopen],
483 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
484 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
485 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
488 |   LIBS="$LIBS $LIBADD_DLOPEN"
492 | AC_SUBST([LIBADD_DLOPEN])
498 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
502 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
512 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
515 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
519 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
526 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
542 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
594 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
599 |       LIBS="$LIBS $LIBADD_DLOPEN"
657 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
2041 | m4trace:config/m4/libtool.m4:1920: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
2042 | if test yes != "$enable_dlopen"; then
2043 |   enable_dlopen=unknown
2044 |   enable_dlopen_self=unknown
2045 |   enable_dlopen_self_static=unknown
2047 |   lt_cv_dlopen=no
2048 |   lt_cv_dlopen_libs=
2052 |     lt_cv_dlopen=load_add_on
2053 |     lt_cv_dlopen_libs=
2054 |     lt_cv_dlopen_self=yes
2058 |     lt_cv_dlopen=LoadLibrary
2059 |     lt_cv_dlopen_libs=
2063 |     lt_cv_dlopen=dlopen
2064 |     lt_cv_dlopen_libs=
2069 |     AC_CHECK_LIB([dl], [dlopen],
2070 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
2071 |     lt_cv_dlopen=dyld
2072 |     lt_cv_dlopen_libs=
2073 |     lt_cv_dlopen_self=yes
2080 |     lt_cv_dlopen=dlopen
2081 |     lt_cv_dlopen_libs=
2082 |     lt_cv_dlopen_self=no
2087 | 	  [lt_cv_dlopen=shl_load],
2089 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
2090 | 	[AC_CHECK_FUNC([dlopen],
2091 | 	      [lt_cv_dlopen=dlopen],
2092 | 	  [AC_CHECK_LIB([dl], [dlopen],
2093 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
2094 | 	    [AC_CHECK_LIB([svld], [dlopen],
2095 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
2097 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2106 |   if test no = "$lt_cv_dlopen"; then
2107 |     enable_dlopen=no
2109 |     enable_dlopen=yes
2112 |   case $lt_cv_dlopen in
2113 |   dlopen)
2121 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2123 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2124 | 	  lt_cv_dlopen_self, [dnl
2125 | 	  _LT_TRY_DLOPEN_SELF(
2126 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2127 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2130 |     if test yes = "$lt_cv_dlopen_self"; then
2132 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2133 | 	  lt_cv_dlopen_self_static, [dnl
2134 | 	  _LT_TRY_DLOPEN_SELF(
2135 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2136 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2146 |   case $lt_cv_dlopen_self in
2147 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2148 |   *) enable_dlopen_self=unknown ;;
2151 |   case $lt_cv_dlopen_self_static in
2152 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2153 |   *) enable_dlopen_self_static=unknown ;;
2156 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2157 | 	 [Whether dlopen is supported])
2158 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2159 | 	 [Whether dlopen of programs is supported])
2160 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2161 | 	 [Whether dlopen of statically linked programs is supported])
2163 | m4trace:config/m4/libtool.m4:2045: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2164 | m4trace:config/m4/libtool.m4:2045: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2166 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2475 | m4trace:config/m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2478 | put the 'dlopen' option into LT_INIT's first parameter.])
2480 | m4trace:config/m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2482 | _LT_SET_OPTION([LT_INIT], [dlopen])
2485 | put the 'dlopen' option into LT_INIT's first parameter.])
2577 | m4trace:config/m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
3768 | m4trace:configure.ac:53: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extlib/gtg/autom4te.cache/output.2

```

{% raw %}
8027 |         enable_dlopen=no
11691 |   if test yes != "$enable_dlopen"; then
11692 |   enable_dlopen=unknown
11693 |   enable_dlopen_self=unknown
11694 |   enable_dlopen_self_static=unknown
11696 |   lt_cv_dlopen=no
11697 |   lt_cv_dlopen_libs=
11701 |     lt_cv_dlopen=load_add_on
11702 |     lt_cv_dlopen_libs=
11703 |     lt_cv_dlopen_self=yes
11707 |     lt_cv_dlopen=LoadLibrary
11708 |     lt_cv_dlopen_libs=
11712 |     lt_cv_dlopen=dlopen
11713 |     lt_cv_dlopen_libs=
11718 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11719 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11720 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11734 | char dlopen ();
11738 | return dlopen ();
11744 |   ac_cv_lib_dl_dlopen=yes
11746 |   ac_cv_lib_dl_dlopen=no
11752 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11753 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11754 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11755 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11758 |     lt_cv_dlopen=dyld
11759 |     lt_cv_dlopen_libs=
11760 |     lt_cv_dlopen_self=yes
11769 |     lt_cv_dlopen=dlopen
11770 |     lt_cv_dlopen_libs=
11771 |     lt_cv_dlopen_self=no
11777 |   lt_cv_dlopen=shl_load
11816 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
11818 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
11819 | if test "x$ac_cv_func_dlopen" = xyes; then :
11820 |   lt_cv_dlopen=dlopen
11822 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11823 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11824 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11838 | char dlopen ();
11842 | return dlopen ();
11848 |   ac_cv_lib_dl_dlopen=yes
11850 |   ac_cv_lib_dl_dlopen=no
11856 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11857 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11858 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11859 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11861 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
11862 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11863 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11877 | char dlopen ();
11881 | return dlopen ();
11887 |   ac_cv_lib_svld_dlopen=yes
11889 |   ac_cv_lib_svld_dlopen=no
11895 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11896 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11897 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11898 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
11937 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
11958 |   if test no = "$lt_cv_dlopen"; then
11959 |     enable_dlopen=no
11961 |     enable_dlopen=yes
11964 |   case $lt_cv_dlopen in
11965 |   dlopen)
11973 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11975 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11976 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11977 | if ${lt_cv_dlopen_self+:} false; then :
11981 |   lt_cv_dlopen_self=cross
12036 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12063 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12064 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12065 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12069 |     lt_cv_dlopen_self=no
12076 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
12077 | $as_echo "$lt_cv_dlopen_self" >&6; }
12079 |     if test yes = "$lt_cv_dlopen_self"; then
12081 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
12082 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12083 | if ${lt_cv_dlopen_self_static+:} false; then :
12087 |   lt_cv_dlopen_self_static=cross
12142 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12169 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12170 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12171 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12175 |     lt_cv_dlopen_self_static=no
12182 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
12183 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12192 |   case $lt_cv_dlopen_self in
12193 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12194 |   *) enable_dlopen_self=unknown ;;
12197 |   case $lt_cv_dlopen_self_static in
12198 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12199 |   *) enable_dlopen_self_static=unknown ;;
16773 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
16774 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
16775 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
17836 | # Whether dlopen is supported.
17837 | dlopen_support=$enable_dlopen
17839 | # Whether dlopen of programs is supported.
17840 | dlopen_self=$enable_dlopen_self
17842 | # Whether dlopen of statically linked programs is supported.
17843 | dlopen_self_static=$enable_dlopen_self_static
17887 | # Compiler flag to allow reflexive dlopens.
18115 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/gtg/autom4te.cache/traces.2

```

{% raw %}
411 | m4trace:/usr/share/aclocal/libtool.m4:1920: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
412 | if test yes != "$enable_dlopen"; then
413 |   enable_dlopen=unknown
414 |   enable_dlopen_self=unknown
415 |   enable_dlopen_self_static=unknown
417 |   lt_cv_dlopen=no
418 |   lt_cv_dlopen_libs=
422 |     lt_cv_dlopen=load_add_on
423 |     lt_cv_dlopen_libs=
424 |     lt_cv_dlopen_self=yes
428 |     lt_cv_dlopen=LoadLibrary
429 |     lt_cv_dlopen_libs=
433 |     lt_cv_dlopen=dlopen
434 |     lt_cv_dlopen_libs=
439 |     AC_CHECK_LIB([dl], [dlopen],
440 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
441 |     lt_cv_dlopen=dyld
442 |     lt_cv_dlopen_libs=
443 |     lt_cv_dlopen_self=yes
450 |     lt_cv_dlopen=dlopen
451 |     lt_cv_dlopen_libs=
452 |     lt_cv_dlopen_self=no
457 | 	  [lt_cv_dlopen=shl_load],
459 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
460 | 	[AC_CHECK_FUNC([dlopen],
461 | 	      [lt_cv_dlopen=dlopen],
462 | 	  [AC_CHECK_LIB([dl], [dlopen],
463 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
464 | 	    [AC_CHECK_LIB([svld], [dlopen],
465 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
467 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
476 |   if test no = "$lt_cv_dlopen"; then
477 |     enable_dlopen=no
479 |     enable_dlopen=yes
482 |   case $lt_cv_dlopen in
483 |   dlopen)
491 |     LIBS="$lt_cv_dlopen_libs $LIBS"
493 |     AC_CACHE_CHECK([whether a program can dlopen itself],
494 | 	  lt_cv_dlopen_self, [dnl
495 | 	  _LT_TRY_DLOPEN_SELF(
496 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
497 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
500 |     if test yes = "$lt_cv_dlopen_self"; then
502 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
503 | 	  lt_cv_dlopen_self_static, [dnl
504 | 	  _LT_TRY_DLOPEN_SELF(
505 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
506 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
516 |   case $lt_cv_dlopen_self in
517 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
518 |   *) enable_dlopen_self=unknown ;;
521 |   case $lt_cv_dlopen_self_static in
522 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
523 |   *) enable_dlopen_self_static=unknown ;;
526 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
527 | 	 [Whether dlopen is supported])
528 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
529 | 	 [Whether dlopen of programs is supported])
530 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
531 | 	 [Whether dlopen of statically linked programs is supported])
533 | m4trace:/usr/share/aclocal/libtool.m4:2045: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
534 | m4trace:/usr/share/aclocal/libtool.m4:2045: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
536 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1086 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1130 | eval "LTDLOPEN=\"$libname_spec\""
1131 | AC_SUBST([LTDLOPEN])
1133 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1134 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1135 |   [lt_cv_sys_dlopen_deplibs],
1136 |   [# PORTME does your system automatically load deplibs for dlopen?
1140 |   lt_cv_sys_dlopen_deplibs=unknown
1145 |     lt_cv_sys_dlopen_deplibs=unknown
1148 |     lt_cv_sys_dlopen_deplibs=yes
1153 |       lt_cv_sys_dlopen_deplibs=no
1158 |     lt_cv_sys_dlopen_deplibs=yes
1163 |     lt_cv_sys_dlopen_deplibs=yes
1166 |     lt_cv_sys_dlopen_deplibs=yes
1170 |     lt_cv_sys_dlopen_deplibs=yes
1173 |     lt_cv_sys_dlopen_deplibs=yes
1176 |     lt_cv_sys_dlopen_deplibs=yes
1181 |     lt_cv_sys_dlopen_deplibs=unknown
1185 |     # at 6.2 and later dlopen does load deplibs.
1186 |     lt_cv_sys_dlopen_deplibs=yes
1189 |     lt_cv_sys_dlopen_deplibs=yes
1192 |     lt_cv_sys_dlopen_deplibs=yes
1195 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1198 |     lt_cv_sys_dlopen_deplibs=no
1201 |     # dlopen *does* load deplibs and with the right loader patch applied
1207 |     lt_cv_sys_dlopen_deplibs=unknown
1214 |     lt_cv_sys_dlopen_deplibs=yes
1217 |     lt_cv_sys_dlopen_deplibs=yes
1220 |     lt_cv_sys_dlopen_deplibs=yes
1223 |     libltdl_cv_sys_dlopen_deplibs=yes
1227 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
1228 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1229 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1232 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1233 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1235 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1307 | LIBADD_DLOPEN=
1308 | AC_SEARCH_LIBS([dlopen], [dl],
1311 | 	if test "$ac_cv_search_dlopen" != "none required"; then
1312 | 	  LIBADD_DLOPEN=-ldl
1314 | 	libltdl_cv_lib_dl_dlopen=yes
1315 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1319 |     ]], [[dlopen(0, 0);]])],
1322 | 	    libltdl_cv_func_dlopen=yes
1323 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1324 | 	[AC_CHECK_LIB([svld], [dlopen],
1327 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
1328 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1329 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
1332 |   LIBS="$LIBS $LIBADD_DLOPEN"
1336 | AC_SUBST([LIBADD_DLOPEN])
1342 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1346 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1356 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1359 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1363 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1370 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
1386 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
1438 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
1443 |       LIBS="$LIBS $LIBADD_DLOPEN"
1501 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
1543 | m4trace:/usr/share/aclocal/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1546 | put the 'dlopen' option into LT_INIT's first parameter.])
1548 | m4trace:/usr/share/aclocal/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1550 | _LT_SET_OPTION([LT_INIT], [dlopen])
1553 | put the 'dlopen' option into LT_INIT's first parameter.])
1645 | m4trace:/usr/share/aclocal/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2676 | m4trace:configure.ac:16: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extlib/litl/ltmain.sh

```bash

{% raw %}
2335 |     opt_dlopen=
2408 |         --dlopen|-dlopen)
2409 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2532 |       # Only execute mode is allowed to have -dlopen flags.
2533 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2534 |         func_error "unrecognized option '-dlopen'"
3760 |   -dlopen FILE      add the directory containing FILE to the library path
3762 | This mode sets the library path environment variable according to '-dlopen'
3817 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3826 |   -module           build a library that can dlopened
3934 |     # Handle -dlopen flags immediately.
3935 |     for file in $opt_dlopen; do
3954 | 	# Skip this library if it cannot be dlopened.
3981 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6674 | 	    dlopen_self=$dlopen_self_static
6680 | 	    dlopen_self=$dlopen_self_static
6686 | 	    dlopen_self=$dlopen_self_static
6744 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6834 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7001 |       -dlopen)
7441 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7509 | 	  # This library was specified with -dlopen.
7629 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7640 | 	passes="conv scan dlopen dlpreopen link"
7666 | 	dlopen) libs=$dlfiles ;;
7697 |       if test dlopen = "$pass"; then
7917 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7918 | 	      # If there is no dlopen support or we're linking statically,
7946 | 	dlopen=
7976 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8022 | 	# This library was specified with -dlopen.
8023 | 	if test dlopen = "$pass"; then
8025 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8027 | 	     test yes != "$dlopen_support" ||
8030 | 	    # If there is no dlname, no dlopen support or we're linking
8039 | 	fi # $pass = dlopen
8095 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8097 | 	      # We recover the dlopen module name by 'saving' the la file
8121 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8250 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8251 | 	  dlopenmodule=
8254 | 	      dlopenmodule=$dlpremoduletest
8258 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8355 | 		    # if the lib is a (non-dlopened) module then we cannot
8359 | 		      if test "X$dlopenmodule" != "X$lib"; then
8511 | 	      echo "*** a static module, that should work as long as the dlopening application"
8512 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8656 |       if test dlopen != "$pass"; then
8786 | 	func_warning "'-dlopen' is ignored for archives"
8853 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9550 | 	    echo "*** a static module, that should work as long as the dlopening"
9551 | 	    echo "*** application is linked with the -dlopen flag."
9569 | 	    echo "*** or is declared to -dlopen it."
10181 | 	func_warning "'-dlopen' is ignored for objects"
10301 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10302 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10983 | # The name that we can dlopen(3).
11012 | # Files to dlopen/dlpreopen
11013 | dlopen='$dlfiles'
{% endraw %}

```
### extlib/litl/autom4te.cache/output.1

```

{% raw %}
8023 |         enable_dlopen=no
11693 |   if test yes != "$enable_dlopen"; then
11694 |   enable_dlopen=unknown
11695 |   enable_dlopen_self=unknown
11696 |   enable_dlopen_self_static=unknown
11698 |   lt_cv_dlopen=no
11699 |   lt_cv_dlopen_libs=
11703 |     lt_cv_dlopen=load_add_on
11704 |     lt_cv_dlopen_libs=
11705 |     lt_cv_dlopen_self=yes
11709 |     lt_cv_dlopen=LoadLibrary
11710 |     lt_cv_dlopen_libs=
11714 |     lt_cv_dlopen=dlopen
11715 |     lt_cv_dlopen_libs=
11720 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11721 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11722 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11736 | char dlopen ();
11740 | return dlopen ();
11746 |   ac_cv_lib_dl_dlopen=yes
11748 |   ac_cv_lib_dl_dlopen=no
11754 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11755 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11756 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11757 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11760 |     lt_cv_dlopen=dyld
11761 |     lt_cv_dlopen_libs=
11762 |     lt_cv_dlopen_self=yes
11771 |     lt_cv_dlopen=dlopen
11772 |     lt_cv_dlopen_libs=
11773 |     lt_cv_dlopen_self=no
11779 |   lt_cv_dlopen=shl_load
11818 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
11820 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
11821 | if test "x$ac_cv_func_dlopen" = xyes; then :
11822 |   lt_cv_dlopen=dlopen
11824 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11825 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11826 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11840 | char dlopen ();
11844 | return dlopen ();
11850 |   ac_cv_lib_dl_dlopen=yes
11852 |   ac_cv_lib_dl_dlopen=no
11858 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11859 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11860 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11861 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11863 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
11864 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11865 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11879 | char dlopen ();
11883 | return dlopen ();
11889 |   ac_cv_lib_svld_dlopen=yes
11891 |   ac_cv_lib_svld_dlopen=no
11897 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11898 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11899 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11900 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
11939 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
11960 |   if test no = "$lt_cv_dlopen"; then
11961 |     enable_dlopen=no
11963 |     enable_dlopen=yes
11966 |   case $lt_cv_dlopen in
11967 |   dlopen)
11975 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11977 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11978 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11979 | if ${lt_cv_dlopen_self+:} false; then :
11983 |   lt_cv_dlopen_self=cross
12038 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12065 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12066 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12067 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12071 |     lt_cv_dlopen_self=no
12078 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
12079 | $as_echo "$lt_cv_dlopen_self" >&6; }
12081 |     if test yes = "$lt_cv_dlopen_self"; then
12083 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
12084 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12085 | if ${lt_cv_dlopen_self_static+:} false; then :
12089 |   lt_cv_dlopen_self_static=cross
12144 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12171 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12172 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12173 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12177 |     lt_cv_dlopen_self_static=no
12184 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
12185 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12194 |   case $lt_cv_dlopen_self in
12195 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12196 |   *) enable_dlopen_self=unknown ;;
12199 |   case $lt_cv_dlopen_self_static in
12200 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12201 |   *) enable_dlopen_self_static=unknown ;;
13798 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
13799 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
13800 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
14790 | # Whether dlopen is supported.
14791 | dlopen_support=$enable_dlopen
14793 | # Whether dlopen of programs is supported.
14794 | dlopen_self=$enable_dlopen_self
14796 | # Whether dlopen of statically linked programs is supported.
14797 | dlopen_self_static=$enable_dlopen_self_static
14841 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/litl/autom4te.cache/output.2

```

{% raw %}
8026 |         enable_dlopen=no
11690 |   if test yes != "$enable_dlopen"; then
11691 |   enable_dlopen=unknown
11692 |   enable_dlopen_self=unknown
11693 |   enable_dlopen_self_static=unknown
11695 |   lt_cv_dlopen=no
11696 |   lt_cv_dlopen_libs=
11700 |     lt_cv_dlopen=load_add_on
11701 |     lt_cv_dlopen_libs=
11702 |     lt_cv_dlopen_self=yes
11706 |     lt_cv_dlopen=LoadLibrary
11707 |     lt_cv_dlopen_libs=
11711 |     lt_cv_dlopen=dlopen
11712 |     lt_cv_dlopen_libs=
11717 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11718 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11719 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11733 | char dlopen ();
11737 | return dlopen ();
11743 |   ac_cv_lib_dl_dlopen=yes
11745 |   ac_cv_lib_dl_dlopen=no
11751 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11752 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11753 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11754 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11757 |     lt_cv_dlopen=dyld
11758 |     lt_cv_dlopen_libs=
11759 |     lt_cv_dlopen_self=yes
11768 |     lt_cv_dlopen=dlopen
11769 |     lt_cv_dlopen_libs=
11770 |     lt_cv_dlopen_self=no
11776 |   lt_cv_dlopen=shl_load
11815 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
11817 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
11818 | if test "x$ac_cv_func_dlopen" = xyes; then :
11819 |   lt_cv_dlopen=dlopen
11821 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11822 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11823 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11837 | char dlopen ();
11841 | return dlopen ();
11847 |   ac_cv_lib_dl_dlopen=yes
11849 |   ac_cv_lib_dl_dlopen=no
11855 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11856 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11857 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11858 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11860 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
11861 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11862 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11876 | char dlopen ();
11880 | return dlopen ();
11886 |   ac_cv_lib_svld_dlopen=yes
11888 |   ac_cv_lib_svld_dlopen=no
11894 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11895 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11896 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11897 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
11936 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
11957 |   if test no = "$lt_cv_dlopen"; then
11958 |     enable_dlopen=no
11960 |     enable_dlopen=yes
11963 |   case $lt_cv_dlopen in
11964 |   dlopen)
11972 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11974 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11975 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11976 | if ${lt_cv_dlopen_self+:} false; then :
11980 |   lt_cv_dlopen_self=cross
12035 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12062 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12063 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12064 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12068 |     lt_cv_dlopen_self=no
12075 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
12076 | $as_echo "$lt_cv_dlopen_self" >&6; }
12078 |     if test yes = "$lt_cv_dlopen_self"; then
12080 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
12081 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12082 | if ${lt_cv_dlopen_self_static+:} false; then :
12086 |   lt_cv_dlopen_self_static=cross
12141 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12168 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12169 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12170 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12174 |     lt_cv_dlopen_self_static=no
12181 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
12182 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12191 |   case $lt_cv_dlopen_self in
12192 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12193 |   *) enable_dlopen_self=unknown ;;
12196 |   case $lt_cv_dlopen_self_static in
12197 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12198 |   *) enable_dlopen_self_static=unknown ;;
13795 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
13796 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
13797 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
14787 | # Whether dlopen is supported.
14788 | dlopen_support=$enable_dlopen
14790 | # Whether dlopen of programs is supported.
14791 | dlopen_self=$enable_dlopen_self
14793 | # Whether dlopen of statically linked programs is supported.
14794 | dlopen_self_static=$enable_dlopen_self_static
14838 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/litl/autom4te.cache/traces.2

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
290 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
291 |   [lt_cv_sys_dlopen_deplibs],
292 |   [# PORTME does your system automatically load deplibs for dlopen?
296 |   lt_cv_sys_dlopen_deplibs=unknown
301 |     lt_cv_sys_dlopen_deplibs=unknown
304 |     lt_cv_sys_dlopen_deplibs=yes
309 |       lt_cv_sys_dlopen_deplibs=no
314 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
326 |     lt_cv_sys_dlopen_deplibs=yes
329 |     lt_cv_sys_dlopen_deplibs=yes
332 |     lt_cv_sys_dlopen_deplibs=yes
337 |     lt_cv_sys_dlopen_deplibs=unknown
341 |     # at 6.2 and later dlopen does load deplibs.
342 |     lt_cv_sys_dlopen_deplibs=yes
345 |     lt_cv_sys_dlopen_deplibs=yes
348 |     lt_cv_sys_dlopen_deplibs=yes
351 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
354 |     lt_cv_sys_dlopen_deplibs=no
357 |     # dlopen *does* load deplibs and with the right loader patch applied
363 |     lt_cv_sys_dlopen_deplibs=unknown
370 |     lt_cv_sys_dlopen_deplibs=yes
373 |     lt_cv_sys_dlopen_deplibs=yes
376 |     lt_cv_sys_dlopen_deplibs=yes
379 |     libltdl_cv_sys_dlopen_deplibs=yes
383 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
384 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
385 |     [Define if the OS needs help to load dependent libraries for dlopen().])
388 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
391 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
463 | LIBADD_DLOPEN=
464 | AC_SEARCH_LIBS([dlopen], [dl],
467 | 	if test "$ac_cv_search_dlopen" != "none required"; then
468 | 	  LIBADD_DLOPEN=-ldl
470 | 	libltdl_cv_lib_dl_dlopen=yes
471 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
475 |     ]], [[dlopen(0, 0);]])],
478 | 	    libltdl_cv_func_dlopen=yes
479 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
480 | 	[AC_CHECK_LIB([svld], [dlopen],
483 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
484 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
485 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
488 |   LIBS="$LIBS $LIBADD_DLOPEN"
492 | AC_SUBST([LIBADD_DLOPEN])
498 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
502 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
512 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
515 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
519 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
526 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
542 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
594 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
599 |       LIBS="$LIBS $LIBADD_DLOPEN"
657 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
1857 | m4trace:m4/libtool.m4:1920: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
1858 | if test yes != "$enable_dlopen"; then
1859 |   enable_dlopen=unknown
1860 |   enable_dlopen_self=unknown
1861 |   enable_dlopen_self_static=unknown
1863 |   lt_cv_dlopen=no
1864 |   lt_cv_dlopen_libs=
1868 |     lt_cv_dlopen=load_add_on
1869 |     lt_cv_dlopen_libs=
1870 |     lt_cv_dlopen_self=yes
1874 |     lt_cv_dlopen=LoadLibrary
1875 |     lt_cv_dlopen_libs=
1879 |     lt_cv_dlopen=dlopen
1880 |     lt_cv_dlopen_libs=
1885 |     AC_CHECK_LIB([dl], [dlopen],
1886 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1887 |     lt_cv_dlopen=dyld
1888 |     lt_cv_dlopen_libs=
1889 |     lt_cv_dlopen_self=yes
1896 |     lt_cv_dlopen=dlopen
1897 |     lt_cv_dlopen_libs=
1898 |     lt_cv_dlopen_self=no
1903 | 	  [lt_cv_dlopen=shl_load],
1905 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1906 | 	[AC_CHECK_FUNC([dlopen],
1907 | 	      [lt_cv_dlopen=dlopen],
1908 | 	  [AC_CHECK_LIB([dl], [dlopen],
1909 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1910 | 	    [AC_CHECK_LIB([svld], [dlopen],
1911 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1913 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1922 |   if test no = "$lt_cv_dlopen"; then
1923 |     enable_dlopen=no
1925 |     enable_dlopen=yes
1928 |   case $lt_cv_dlopen in
1929 |   dlopen)
1937 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1939 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1940 | 	  lt_cv_dlopen_self, [dnl
1941 | 	  _LT_TRY_DLOPEN_SELF(
1942 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1943 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1946 |     if test yes = "$lt_cv_dlopen_self"; then
1948 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1949 | 	  lt_cv_dlopen_self_static, [dnl
1950 | 	  _LT_TRY_DLOPEN_SELF(
1951 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1952 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1962 |   case $lt_cv_dlopen_self in
1963 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1964 |   *) enable_dlopen_self=unknown ;;
1967 |   case $lt_cv_dlopen_self_static in
1968 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1969 |   *) enable_dlopen_self_static=unknown ;;
1972 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1973 | 	 [Whether dlopen is supported])
1974 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1975 | 	 [Whether dlopen of programs is supported])
1976 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1977 | 	 [Whether dlopen of statically linked programs is supported])
1979 | m4trace:m4/libtool.m4:2045: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1980 | m4trace:m4/libtool.m4:2045: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
1982 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2291 | m4trace:m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2294 | put the 'dlopen' option into LT_INIT's first parameter.])
2296 | m4trace:m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2298 | _LT_SET_OPTION([LT_INIT], [dlopen])
2301 | put the 'dlopen' option into LT_INIT's first parameter.])
2393 | m4trace:m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2689 | m4trace:configure.ac:15: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extlib/litl/m4/libtool.m4

```

{% raw %}
1820 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1823 | m4_defun([_LT_TRY_DLOPEN_SELF],
1881 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1914 | ])# _LT_TRY_DLOPEN_SELF
1917 | # LT_SYS_DLOPEN_SELF
1919 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1921 | if test yes != "$enable_dlopen"; then
1922 |   enable_dlopen=unknown
1923 |   enable_dlopen_self=unknown
1924 |   enable_dlopen_self_static=unknown
1926 |   lt_cv_dlopen=no
1927 |   lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen=load_add_on
1932 |     lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen_self=yes
1937 |     lt_cv_dlopen=LoadLibrary
1938 |     lt_cv_dlopen_libs=
1942 |     lt_cv_dlopen=dlopen
1943 |     lt_cv_dlopen_libs=
1948 |     AC_CHECK_LIB([dl], [dlopen],
1949 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1950 |     lt_cv_dlopen=dyld
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1959 |     lt_cv_dlopen=dlopen
1960 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen_self=no
1966 | 	  [lt_cv_dlopen=shl_load],
1968 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1969 | 	[AC_CHECK_FUNC([dlopen],
1970 | 	      [lt_cv_dlopen=dlopen],
1971 | 	  [AC_CHECK_LIB([dl], [dlopen],
1972 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1973 | 	    [AC_CHECK_LIB([svld], [dlopen],
1974 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1976 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1985 |   if test no = "$lt_cv_dlopen"; then
1986 |     enable_dlopen=no
1988 |     enable_dlopen=yes
1991 |   case $lt_cv_dlopen in
1992 |   dlopen)
2000 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2002 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2003 | 	  lt_cv_dlopen_self, [dnl
2004 | 	  _LT_TRY_DLOPEN_SELF(
2005 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2006 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2009 |     if test yes = "$lt_cv_dlopen_self"; then
2011 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2012 | 	  lt_cv_dlopen_self_static, [dnl
2013 | 	  _LT_TRY_DLOPEN_SELF(
2014 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2015 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2025 |   case $lt_cv_dlopen_self in
2026 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2027 |   *) enable_dlopen_self=unknown ;;
2030 |   case $lt_cv_dlopen_self_static in
2031 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2032 |   *) enable_dlopen_self_static=unknown ;;
2035 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2036 | 	 [Whether dlopen is supported])
2037 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2038 | 	 [Whether dlopen of programs is supported])
2039 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2040 | 	 [Whether dlopen of statically linked programs is supported])
2041 | ])# LT_SYS_DLOPEN_SELF
2044 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2046 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6147 |     [Compiler flag to allow reflexive dlopens])
6260 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extlib/litl/m4/ltoptions.m4

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
### extlib/opari2/build-config/ltmain.sh

```bash

{% raw %}
2335 |     opt_dlopen=
2408 |         --dlopen|-dlopen)
2409 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2532 |       # Only execute mode is allowed to have -dlopen flags.
2533 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2534 |         func_error "unrecognized option '-dlopen'"
3760 |   -dlopen FILE      add the directory containing FILE to the library path
3762 | This mode sets the library path environment variable according to '-dlopen'
3817 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3826 |   -module           build a library that can dlopened
3934 |     # Handle -dlopen flags immediately.
3935 |     for file in $opt_dlopen; do
3954 | 	# Skip this library if it cannot be dlopened.
3981 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6674 | 	    dlopen_self=$dlopen_self_static
6680 | 	    dlopen_self=$dlopen_self_static
6686 | 	    dlopen_self=$dlopen_self_static
6744 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6834 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7001 |       -dlopen)
7441 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7509 | 	  # This library was specified with -dlopen.
7629 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7640 | 	passes="conv scan dlopen dlpreopen link"
7666 | 	dlopen) libs=$dlfiles ;;
7697 |       if test dlopen = "$pass"; then
7917 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7918 | 	      # If there is no dlopen support or we're linking statically,
7946 | 	dlopen=
7976 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8022 | 	# This library was specified with -dlopen.
8023 | 	if test dlopen = "$pass"; then
8025 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8027 | 	     test yes != "$dlopen_support" ||
8030 | 	    # If there is no dlname, no dlopen support or we're linking
8039 | 	fi # $pass = dlopen
8095 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8097 | 	      # We recover the dlopen module name by 'saving' the la file
8121 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8250 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8251 | 	  dlopenmodule=
8254 | 	      dlopenmodule=$dlpremoduletest
8258 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8355 | 		    # if the lib is a (non-dlopened) module then we cannot
8359 | 		      if test "X$dlopenmodule" != "X$lib"; then
8511 | 	      echo "*** a static module, that should work as long as the dlopening application"
8512 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8656 |       if test dlopen != "$pass"; then
8786 | 	func_warning "'-dlopen' is ignored for archives"
8853 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9550 | 	    echo "*** a static module, that should work as long as the dlopening"
9551 | 	    echo "*** application is linked with the -dlopen flag."
9569 | 	    echo "*** or is declared to -dlopen it."
10181 | 	func_warning "'-dlopen' is ignored for objects"
10301 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10302 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10983 | # The name that we can dlopen(3).
11012 | # Files to dlopen/dlpreopen
11013 | dlopen='$dlfiles'
{% endraw %}

```
### extlib/opari2/vendor/common/build-config/m4/libtool.m4

```

{% raw %}
1820 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1823 | m4_defun([_LT_TRY_DLOPEN_SELF],
1881 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1914 | ])# _LT_TRY_DLOPEN_SELF
1917 | # LT_SYS_DLOPEN_SELF
1919 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1921 | if test yes != "$enable_dlopen"; then
1922 |   enable_dlopen=unknown
1923 |   enable_dlopen_self=unknown
1924 |   enable_dlopen_self_static=unknown
1926 |   lt_cv_dlopen=no
1927 |   lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen=load_add_on
1932 |     lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen_self=yes
1937 |     lt_cv_dlopen=LoadLibrary
1938 |     lt_cv_dlopen_libs=
1942 |     lt_cv_dlopen=dlopen
1943 |     lt_cv_dlopen_libs=
1948 |     AC_CHECK_LIB([dl], [dlopen],
1949 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1950 |     lt_cv_dlopen=dyld
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1959 |     lt_cv_dlopen=dlopen
1960 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen_self=no
1966 | 	  [lt_cv_dlopen=shl_load],
1968 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1969 | 	[AC_CHECK_FUNC([dlopen],
1970 | 	      [lt_cv_dlopen=dlopen],
1971 | 	  [AC_CHECK_LIB([dl], [dlopen],
1972 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1973 | 	    [AC_CHECK_LIB([svld], [dlopen],
1974 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1976 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1985 |   if test no = "$lt_cv_dlopen"; then
1986 |     enable_dlopen=no
1988 |     enable_dlopen=yes
1991 |   case $lt_cv_dlopen in
1992 |   dlopen)
2000 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2002 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2003 | 	  lt_cv_dlopen_self, [dnl
2004 | 	  _LT_TRY_DLOPEN_SELF(
2005 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2006 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2009 |     if test yes = "$lt_cv_dlopen_self"; then
2011 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2012 | 	  lt_cv_dlopen_self_static, [dnl
2013 | 	  _LT_TRY_DLOPEN_SELF(
2014 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2015 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2025 |   case $lt_cv_dlopen_self in
2026 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2027 |   *) enable_dlopen_self=unknown ;;
2030 |   case $lt_cv_dlopen_self_static in
2031 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2032 |   *) enable_dlopen_self_static=unknown ;;
2035 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2036 | 	 [Whether dlopen is supported])
2037 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2038 | 	 [Whether dlopen of programs is supported])
2039 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2040 | 	 [Whether dlopen of statically linked programs is supported])
2041 | ])# LT_SYS_DLOPEN_SELF
2044 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2046 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6147 |     [Compiler flag to allow reflexive dlopens])
6260 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extlib/opari2/vendor/common/build-config/m4/ltoptions.m4

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
### extlib/opari2/build-frontend/autom4te.cache/output.3

```

{% raw %}
10341 |         enable_dlopen=no
13684 |   if test "x$enable_dlopen" != xyes; then
13685 |   enable_dlopen=unknown
13686 |   enable_dlopen_self=unknown
13687 |   enable_dlopen_self_static=unknown
13689 |   lt_cv_dlopen=no
13690 |   lt_cv_dlopen_libs=
13694 |     lt_cv_dlopen="load_add_on"
13695 |     lt_cv_dlopen_libs=
13696 |     lt_cv_dlopen_self=yes
13700 |     lt_cv_dlopen="LoadLibrary"
13701 |     lt_cv_dlopen_libs=
13705 |     lt_cv_dlopen="dlopen"
13706 |     lt_cv_dlopen_libs=
13711 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
13712 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
13713 | if ${ac_cv_lib_dl_dlopen+:} false; then :
13727 | char dlopen ();
13731 | return dlopen ();
13737 |   ac_cv_lib_dl_dlopen=yes
13739 |   ac_cv_lib_dl_dlopen=no
13745 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
13746 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
13747 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
13748 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
13751 |     lt_cv_dlopen="dyld"
13752 |     lt_cv_dlopen_libs=
13753 |     lt_cv_dlopen_self=yes
13762 |   lt_cv_dlopen="shl_load"
13801 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
13803 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
13804 | if test "x$ac_cv_func_dlopen" = xyes; then :
13805 |   lt_cv_dlopen="dlopen"
13807 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
13808 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
13809 | if ${ac_cv_lib_dl_dlopen+:} false; then :
13823 | char dlopen ();
13827 | return dlopen ();
13833 |   ac_cv_lib_dl_dlopen=yes
13835 |   ac_cv_lib_dl_dlopen=no
13841 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
13842 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
13843 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
13844 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
13846 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
13847 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
13848 | if ${ac_cv_lib_svld_dlopen+:} false; then :
13862 | char dlopen ();
13866 | return dlopen ();
13872 |   ac_cv_lib_svld_dlopen=yes
13874 |   ac_cv_lib_svld_dlopen=no
13880 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
13881 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
13882 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
13883 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
13922 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
13943 |   if test "x$lt_cv_dlopen" != xno; then
13944 |     enable_dlopen=yes
13946 |     enable_dlopen=no
13949 |   case $lt_cv_dlopen in
13950 |   dlopen)
13958 |     LIBS="$lt_cv_dlopen_libs $LIBS"
13960 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
13961 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
13962 | if ${lt_cv_dlopen_self+:} false; then :
13966 |   lt_cv_dlopen_self=cross
14021 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14048 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14049 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14050 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14054 |     lt_cv_dlopen_self=no
14061 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14062 | $as_echo "$lt_cv_dlopen_self" >&6; }
14064 |     if test "x$lt_cv_dlopen_self" = xyes; then
14066 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14067 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14068 | if ${lt_cv_dlopen_self_static+:} false; then :
14072 |   lt_cv_dlopen_self_static=cross
14127 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14154 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14155 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14156 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14160 |     lt_cv_dlopen_self_static=no
14167 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14168 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14177 |   case $lt_cv_dlopen_self in
14178 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14179 |   *) enable_dlopen_self=unknown ;;
14182 |   case $lt_cv_dlopen_self_static in
14183 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14184 |   *) enable_dlopen_self_static=unknown ;;
24066 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
24067 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
24068 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
25478 | # Whether dlopen is supported.
25479 | dlopen_support=$enable_dlopen
25481 | # Whether dlopen of programs is supported.
25482 | dlopen_self=$enable_dlopen_self
25484 | # Whether dlopen of statically linked programs is supported.
25485 | dlopen_self_static=$enable_dlopen_self_static
25529 | # Compiler flag to allow reflexive dlopens.
25871 | # Compiler flag to allow reflexive dlopens.
26024 | # Compiler flag to allow reflexive dlopens.
26177 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/opari2/build-frontend/autom4te.cache/output.0

```

{% raw %}
10531 |         enable_dlopen=no
14171 |   if test yes != "$enable_dlopen"; then
14172 |   enable_dlopen=unknown
14173 |   enable_dlopen_self=unknown
14174 |   enable_dlopen_self_static=unknown
14176 |   lt_cv_dlopen=no
14177 |   lt_cv_dlopen_libs=
14181 |     lt_cv_dlopen=load_add_on
14182 |     lt_cv_dlopen_libs=
14183 |     lt_cv_dlopen_self=yes
14187 |     lt_cv_dlopen=LoadLibrary
14188 |     lt_cv_dlopen_libs=
14192 |     lt_cv_dlopen=dlopen
14193 |     lt_cv_dlopen_libs=
14198 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14199 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14200 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14214 | char dlopen ();
14218 | return dlopen ();
14224 |   ac_cv_lib_dl_dlopen=yes
14226 |   ac_cv_lib_dl_dlopen=no
14232 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14233 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14234 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14235 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14238 |     lt_cv_dlopen=dyld
14239 |     lt_cv_dlopen_libs=
14240 |     lt_cv_dlopen_self=yes
14249 |     lt_cv_dlopen=dlopen
14250 |     lt_cv_dlopen_libs=
14251 |     lt_cv_dlopen_self=no
14257 |   lt_cv_dlopen=shl_load
14296 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
14298 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
14299 | if test "x$ac_cv_func_dlopen" = xyes; then :
14300 |   lt_cv_dlopen=dlopen
14302 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14303 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14304 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14318 | char dlopen ();
14322 | return dlopen ();
14328 |   ac_cv_lib_dl_dlopen=yes
14330 |   ac_cv_lib_dl_dlopen=no
14336 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14337 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14338 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14339 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14341 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14342 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14343 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14357 | char dlopen ();
14361 | return dlopen ();
14367 |   ac_cv_lib_svld_dlopen=yes
14369 |   ac_cv_lib_svld_dlopen=no
14375 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14376 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14377 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14378 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
14417 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
14438 |   if test no = "$lt_cv_dlopen"; then
14439 |     enable_dlopen=no
14441 |     enable_dlopen=yes
14444 |   case $lt_cv_dlopen in
14445 |   dlopen)
14453 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14455 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14456 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14457 | if ${lt_cv_dlopen_self+:} false; then :
14461 |   lt_cv_dlopen_self=cross
14516 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14543 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14544 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14545 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14549 |     lt_cv_dlopen_self=no
14556 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14557 | $as_echo "$lt_cv_dlopen_self" >&6; }
14559 |     if test yes = "$lt_cv_dlopen_self"; then
14561 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14562 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14563 | if ${lt_cv_dlopen_self_static+:} false; then :
14567 |   lt_cv_dlopen_self_static=cross
14622 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14649 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14650 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14651 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14655 |     lt_cv_dlopen_self_static=no
14662 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14663 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14672 |   case $lt_cv_dlopen_self in
14673 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14674 |   *) enable_dlopen_self=unknown ;;
14677 |   case $lt_cv_dlopen_self_static in
14678 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14679 |   *) enable_dlopen_self_static=unknown ;;
25182 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
25183 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
25184 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
26608 | # Whether dlopen is supported.
26609 | dlopen_support=$enable_dlopen
26611 | # Whether dlopen of programs is supported.
26612 | dlopen_self=$enable_dlopen_self
26614 | # Whether dlopen of statically linked programs is supported.
26615 | dlopen_self_static=$enable_dlopen_self_static
26659 | # Compiler flag to allow reflexive dlopens.
26901 | # Compiler flag to allow reflexive dlopens.
27054 | # Compiler flag to allow reflexive dlopens.
27207 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/opari2/build-frontend/autom4te.cache/traces.3

```

{% raw %}
244 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
288 | eval "LTDLOPEN=\"$libname_spec\""
289 | AC_SUBST([LTDLOPEN])
291 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
292 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
293 |   [lt_cv_sys_dlopen_deplibs],
294 |   [# PORTME does your system automatically load deplibs for dlopen?
298 |   lt_cv_sys_dlopen_deplibs=unknown
303 |     lt_cv_sys_dlopen_deplibs=unknown
306 |     lt_cv_sys_dlopen_deplibs=yes
311 |       lt_cv_sys_dlopen_deplibs=no
318 |     lt_cv_sys_dlopen_deplibs=yes
321 |     lt_cv_sys_dlopen_deplibs=yes
325 |     lt_cv_sys_dlopen_deplibs=yes
328 |     lt_cv_sys_dlopen_deplibs=yes
331 |     lt_cv_sys_dlopen_deplibs=yes
336 |     lt_cv_sys_dlopen_deplibs=unknown
340 |     # at 6.2 and later dlopen does load deplibs.
341 |     lt_cv_sys_dlopen_deplibs=yes
344 |     lt_cv_sys_dlopen_deplibs=yes
347 |     lt_cv_sys_dlopen_deplibs=yes
350 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
353 |     lt_cv_sys_dlopen_deplibs=no
356 |     # dlopen *does* load deplibs and with the right loader patch applied
362 |     lt_cv_sys_dlopen_deplibs=unknown
369 |     lt_cv_sys_dlopen_deplibs=yes
372 |     lt_cv_sys_dlopen_deplibs=yes
375 |     lt_cv_sys_dlopen_deplibs=yes
378 |     libltdl_cv_sys_dlopen_deplibs=yes
382 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
383 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
384 |     [Define if the OS needs help to load dependent libraries for dlopen().])
387 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
388 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
390 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
456 | LIBADD_DLOPEN=
457 | AC_SEARCH_LIBS([dlopen], [dl],
460 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
461 | 	  LIBADD_DLOPEN="-ldl"
463 | 	libltdl_cv_lib_dl_dlopen="yes"
464 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
468 |     ]], [[dlopen(0, 0);]])],
471 | 	    libltdl_cv_func_dlopen="yes"
472 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
473 | 	[AC_CHECK_LIB([svld], [dlopen],
476 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
477 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
478 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
481 |   LIBS="$LIBS $LIBADD_DLOPEN"
485 | AC_SUBST([LIBADD_DLOPEN])
491 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
495 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
505 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
508 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
512 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
519 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
535 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
584 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
585 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
590 |           LIBS="$LIBS $LIBADD_DLOPEN"
591 | 	  _LT_TRY_DLOPEN_SELF(
2548 | m4trace:../vendor/common/build-config/m4/libtool.m4:1858: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
2549 | if test "x$enable_dlopen" != xyes; then
2550 |   enable_dlopen=unknown
2551 |   enable_dlopen_self=unknown
2552 |   enable_dlopen_self_static=unknown
2554 |   lt_cv_dlopen=no
2555 |   lt_cv_dlopen_libs=
2559 |     lt_cv_dlopen="load_add_on"
2560 |     lt_cv_dlopen_libs=
2561 |     lt_cv_dlopen_self=yes
2565 |     lt_cv_dlopen="LoadLibrary"
2566 |     lt_cv_dlopen_libs=
2570 |     lt_cv_dlopen="dlopen"
2571 |     lt_cv_dlopen_libs=
2576 |     AC_CHECK_LIB([dl], [dlopen],
2577 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
2578 |     lt_cv_dlopen="dyld"
2579 |     lt_cv_dlopen_libs=
2580 |     lt_cv_dlopen_self=yes
2586 | 	  [lt_cv_dlopen="shl_load"],
2588 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
2589 | 	[AC_CHECK_FUNC([dlopen],
2590 | 	      [lt_cv_dlopen="dlopen"],
2591 | 	  [AC_CHECK_LIB([dl], [dlopen],
2592 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2593 | 	    [AC_CHECK_LIB([svld], [dlopen],
2594 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2596 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
2605 |   if test "x$lt_cv_dlopen" != xno; then
2606 |     enable_dlopen=yes
2608 |     enable_dlopen=no
2611 |   case $lt_cv_dlopen in
2612 |   dlopen)
2620 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2622 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2623 | 	  lt_cv_dlopen_self, [dnl
2624 | 	  _LT_TRY_DLOPEN_SELF(
2625 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2626 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2629 |     if test "x$lt_cv_dlopen_self" = xyes; then
2631 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2632 | 	  lt_cv_dlopen_self_static, [dnl
2633 | 	  _LT_TRY_DLOPEN_SELF(
2634 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2635 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2645 |   case $lt_cv_dlopen_self in
2646 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2647 |   *) enable_dlopen_self=unknown ;;
2650 |   case $lt_cv_dlopen_self_static in
2651 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2652 |   *) enable_dlopen_self_static=unknown ;;
2655 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2656 | 	 [Whether dlopen is supported])
2657 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2658 | 	 [Whether dlopen of programs is supported])
2659 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2660 | 	 [Whether dlopen of statically linked programs is supported])
2662 | m4trace:../vendor/common/build-config/m4/libtool.m4:1975: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2663 | m4trace:../vendor/common/build-config/m4/libtool.m4:1975: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2665 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2961 | m4trace:../vendor/common/build-config/m4/ltoptions.m4:111: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2964 | put the `dlopen' option into LT_INIT's first parameter.])
2966 | m4trace:../vendor/common/build-config/m4/ltoptions.m4:111: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2968 | _LT_SET_OPTION([LT_INIT], [dlopen])
2971 | put the `dlopen' option into LT_INIT's first parameter.])
3063 | m4trace:../vendor/common/build-config/m4/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
4071 | m4trace:configure.ac:44: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extlib/opari2/build-frontend/autom4te.cache/output.1

```

{% raw %}
10531 |         enable_dlopen=no
14171 |   if test yes != "$enable_dlopen"; then
14172 |   enable_dlopen=unknown
14173 |   enable_dlopen_self=unknown
14174 |   enable_dlopen_self_static=unknown
14176 |   lt_cv_dlopen=no
14177 |   lt_cv_dlopen_libs=
14181 |     lt_cv_dlopen=load_add_on
14182 |     lt_cv_dlopen_libs=
14183 |     lt_cv_dlopen_self=yes
14187 |     lt_cv_dlopen=LoadLibrary
14188 |     lt_cv_dlopen_libs=
14192 |     lt_cv_dlopen=dlopen
14193 |     lt_cv_dlopen_libs=
14198 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14199 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14200 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14214 | char dlopen ();
14218 | return dlopen ();
14224 |   ac_cv_lib_dl_dlopen=yes
14226 |   ac_cv_lib_dl_dlopen=no
14232 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14233 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14234 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14235 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14238 |     lt_cv_dlopen=dyld
14239 |     lt_cv_dlopen_libs=
14240 |     lt_cv_dlopen_self=yes
14249 |     lt_cv_dlopen=dlopen
14250 |     lt_cv_dlopen_libs=
14251 |     lt_cv_dlopen_self=no
14257 |   lt_cv_dlopen=shl_load
14296 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
14298 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
14299 | if test "x$ac_cv_func_dlopen" = xyes; then :
14300 |   lt_cv_dlopen=dlopen
14302 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14303 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14304 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14318 | char dlopen ();
14322 | return dlopen ();
14328 |   ac_cv_lib_dl_dlopen=yes
14330 |   ac_cv_lib_dl_dlopen=no
14336 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14337 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14338 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14339 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14341 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14342 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14343 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14357 | char dlopen ();
14361 | return dlopen ();
14367 |   ac_cv_lib_svld_dlopen=yes
14369 |   ac_cv_lib_svld_dlopen=no
14375 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14376 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14377 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14378 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
14417 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
14438 |   if test no = "$lt_cv_dlopen"; then
14439 |     enable_dlopen=no
14441 |     enable_dlopen=yes
14444 |   case $lt_cv_dlopen in
14445 |   dlopen)
14453 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14455 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14456 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14457 | if ${lt_cv_dlopen_self+:} false; then :
14461 |   lt_cv_dlopen_self=cross
14516 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14543 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14544 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14545 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14549 |     lt_cv_dlopen_self=no
14556 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14557 | $as_echo "$lt_cv_dlopen_self" >&6; }
14559 |     if test yes = "$lt_cv_dlopen_self"; then
14561 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14562 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14563 | if ${lt_cv_dlopen_self_static+:} false; then :
14567 |   lt_cv_dlopen_self_static=cross
14622 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14649 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14650 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14651 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14655 |     lt_cv_dlopen_self_static=no
14662 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14663 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14672 |   case $lt_cv_dlopen_self in
14673 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14674 |   *) enable_dlopen_self=unknown ;;
14677 |   case $lt_cv_dlopen_self_static in
14678 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14679 |   *) enable_dlopen_self_static=unknown ;;
25182 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
25183 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
25184 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
26608 | # Whether dlopen is supported.
26609 | dlopen_support=$enable_dlopen
26611 | # Whether dlopen of programs is supported.
26612 | dlopen_self=$enable_dlopen_self
26614 | # Whether dlopen of statically linked programs is supported.
26615 | dlopen_self_static=$enable_dlopen_self_static
26659 | # Compiler flag to allow reflexive dlopens.
26901 | # Compiler flag to allow reflexive dlopens.
27054 | # Compiler flag to allow reflexive dlopens.
27207 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/opari2/build-frontend/autom4te.cache/output.2

```

{% raw %}
10534 |         enable_dlopen=no
14168 |   if test yes != "$enable_dlopen"; then
14169 |   enable_dlopen=unknown
14170 |   enable_dlopen_self=unknown
14171 |   enable_dlopen_self_static=unknown
14173 |   lt_cv_dlopen=no
14174 |   lt_cv_dlopen_libs=
14178 |     lt_cv_dlopen=load_add_on
14179 |     lt_cv_dlopen_libs=
14180 |     lt_cv_dlopen_self=yes
14184 |     lt_cv_dlopen=LoadLibrary
14185 |     lt_cv_dlopen_libs=
14189 |     lt_cv_dlopen=dlopen
14190 |     lt_cv_dlopen_libs=
14195 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14196 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14197 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14211 | char dlopen ();
14215 | return dlopen ();
14221 |   ac_cv_lib_dl_dlopen=yes
14223 |   ac_cv_lib_dl_dlopen=no
14229 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14230 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14231 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14232 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14235 |     lt_cv_dlopen=dyld
14236 |     lt_cv_dlopen_libs=
14237 |     lt_cv_dlopen_self=yes
14246 |     lt_cv_dlopen=dlopen
14247 |     lt_cv_dlopen_libs=
14248 |     lt_cv_dlopen_self=no
14254 |   lt_cv_dlopen=shl_load
14293 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
14295 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
14296 | if test "x$ac_cv_func_dlopen" = xyes; then :
14297 |   lt_cv_dlopen=dlopen
14299 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14300 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14301 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14315 | char dlopen ();
14319 | return dlopen ();
14325 |   ac_cv_lib_dl_dlopen=yes
14327 |   ac_cv_lib_dl_dlopen=no
14333 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14334 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14335 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14336 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14338 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14339 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14340 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14354 | char dlopen ();
14358 | return dlopen ();
14364 |   ac_cv_lib_svld_dlopen=yes
14366 |   ac_cv_lib_svld_dlopen=no
14372 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14373 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14374 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14375 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
14414 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
14435 |   if test no = "$lt_cv_dlopen"; then
14436 |     enable_dlopen=no
14438 |     enable_dlopen=yes
14441 |   case $lt_cv_dlopen in
14442 |   dlopen)
14450 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14452 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14453 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14454 | if ${lt_cv_dlopen_self+:} false; then :
14458 |   lt_cv_dlopen_self=cross
14513 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14540 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14541 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14542 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14546 |     lt_cv_dlopen_self=no
14553 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14554 | $as_echo "$lt_cv_dlopen_self" >&6; }
14556 |     if test yes = "$lt_cv_dlopen_self"; then
14558 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14559 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14560 | if ${lt_cv_dlopen_self_static+:} false; then :
14564 |   lt_cv_dlopen_self_static=cross
14619 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14646 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14647 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14648 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14652 |     lt_cv_dlopen_self_static=no
14659 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14660 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14669 |   case $lt_cv_dlopen_self in
14670 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14671 |   *) enable_dlopen_self=unknown ;;
14674 |   case $lt_cv_dlopen_self_static in
14675 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14676 |   *) enable_dlopen_self_static=unknown ;;
25167 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
25168 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
25169 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
26593 | # Whether dlopen is supported.
26594 | dlopen_support=$enable_dlopen
26596 | # Whether dlopen of programs is supported.
26597 | dlopen_self=$enable_dlopen_self
26599 | # Whether dlopen of statically linked programs is supported.
26600 | dlopen_self_static=$enable_dlopen_self_static
26644 | # Compiler flag to allow reflexive dlopens.
26886 | # Compiler flag to allow reflexive dlopens.
27039 | # Compiler flag to allow reflexive dlopens.
27192 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/opari2/build-frontend/autom4te.cache/traces.0

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
290 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
291 |   [lt_cv_sys_dlopen_deplibs],
292 |   [# PORTME does your system automatically load deplibs for dlopen?
296 |   lt_cv_sys_dlopen_deplibs=unknown
301 |     lt_cv_sys_dlopen_deplibs=unknown
304 |     lt_cv_sys_dlopen_deplibs=yes
309 |       lt_cv_sys_dlopen_deplibs=no
314 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
326 |     lt_cv_sys_dlopen_deplibs=yes
329 |     lt_cv_sys_dlopen_deplibs=yes
332 |     lt_cv_sys_dlopen_deplibs=yes
337 |     lt_cv_sys_dlopen_deplibs=unknown
341 |     # at 6.2 and later dlopen does load deplibs.
342 |     lt_cv_sys_dlopen_deplibs=yes
345 |     lt_cv_sys_dlopen_deplibs=yes
348 |     lt_cv_sys_dlopen_deplibs=yes
351 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
354 |     lt_cv_sys_dlopen_deplibs=no
357 |     # dlopen *does* load deplibs and with the right loader patch applied
363 |     lt_cv_sys_dlopen_deplibs=unknown
370 |     lt_cv_sys_dlopen_deplibs=yes
373 |     lt_cv_sys_dlopen_deplibs=yes
376 |     lt_cv_sys_dlopen_deplibs=yes
379 |     libltdl_cv_sys_dlopen_deplibs=yes
383 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
384 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
385 |     [Define if the OS needs help to load dependent libraries for dlopen().])
388 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
391 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
463 | LIBADD_DLOPEN=
464 | AC_SEARCH_LIBS([dlopen], [dl],
467 | 	if test "$ac_cv_search_dlopen" != "none required"; then
468 | 	  LIBADD_DLOPEN=-ldl
470 | 	libltdl_cv_lib_dl_dlopen=yes
471 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
475 |     ]], [[dlopen(0, 0);]])],
478 | 	    libltdl_cv_func_dlopen=yes
479 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
480 | 	[AC_CHECK_LIB([svld], [dlopen],
483 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
484 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
485 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
488 |   LIBS="$LIBS $LIBADD_DLOPEN"
492 | AC_SUBST([LIBADD_DLOPEN])
498 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
502 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
512 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
515 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
519 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
526 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
542 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
594 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
599 |       LIBS="$LIBS $LIBADD_DLOPEN"
657 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
2622 | m4trace:../vendor/common/build-config/m4/libtool.m4:1920: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
2623 | if test yes != "$enable_dlopen"; then
2624 |   enable_dlopen=unknown
2625 |   enable_dlopen_self=unknown
2626 |   enable_dlopen_self_static=unknown
2628 |   lt_cv_dlopen=no
2629 |   lt_cv_dlopen_libs=
2633 |     lt_cv_dlopen=load_add_on
2634 |     lt_cv_dlopen_libs=
2635 |     lt_cv_dlopen_self=yes
2639 |     lt_cv_dlopen=LoadLibrary
2640 |     lt_cv_dlopen_libs=
2644 |     lt_cv_dlopen=dlopen
2645 |     lt_cv_dlopen_libs=
2650 |     AC_CHECK_LIB([dl], [dlopen],
2651 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
2652 |     lt_cv_dlopen=dyld
2653 |     lt_cv_dlopen_libs=
2654 |     lt_cv_dlopen_self=yes
2661 |     lt_cv_dlopen=dlopen
2662 |     lt_cv_dlopen_libs=
2663 |     lt_cv_dlopen_self=no
2668 | 	  [lt_cv_dlopen=shl_load],
2670 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
2671 | 	[AC_CHECK_FUNC([dlopen],
2672 | 	      [lt_cv_dlopen=dlopen],
2673 | 	  [AC_CHECK_LIB([dl], [dlopen],
2674 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
2675 | 	    [AC_CHECK_LIB([svld], [dlopen],
2676 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
2678 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2687 |   if test no = "$lt_cv_dlopen"; then
2688 |     enable_dlopen=no
2690 |     enable_dlopen=yes
2693 |   case $lt_cv_dlopen in
2694 |   dlopen)
2702 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2704 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2705 | 	  lt_cv_dlopen_self, [dnl
2706 | 	  _LT_TRY_DLOPEN_SELF(
2707 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2708 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2711 |     if test yes = "$lt_cv_dlopen_self"; then
2713 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2714 | 	  lt_cv_dlopen_self_static, [dnl
2715 | 	  _LT_TRY_DLOPEN_SELF(
2716 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2717 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2727 |   case $lt_cv_dlopen_self in
2728 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2729 |   *) enable_dlopen_self=unknown ;;
2732 |   case $lt_cv_dlopen_self_static in
2733 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2734 |   *) enable_dlopen_self_static=unknown ;;
2737 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2738 | 	 [Whether dlopen is supported])
2739 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2740 | 	 [Whether dlopen of programs is supported])
2741 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2742 | 	 [Whether dlopen of statically linked programs is supported])
2744 | m4trace:../vendor/common/build-config/m4/libtool.m4:2045: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2745 | m4trace:../vendor/common/build-config/m4/libtool.m4:2045: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2747 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
3056 | m4trace:../vendor/common/build-config/m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
3059 | put the 'dlopen' option into LT_INIT's first parameter.])
3061 | m4trace:../vendor/common/build-config/m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
3063 | _LT_SET_OPTION([LT_INIT], [dlopen])
3066 | put the 'dlopen' option into LT_INIT's first parameter.])
3158 | m4trace:../vendor/common/build-config/m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
4169 | m4trace:configure.ac:44: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extlib/opari2/build-frontend/autom4te.cache/traces.4

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
290 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
291 |   [lt_cv_sys_dlopen_deplibs],
292 |   [# PORTME does your system automatically load deplibs for dlopen?
296 |   lt_cv_sys_dlopen_deplibs=unknown
301 |     lt_cv_sys_dlopen_deplibs=unknown
304 |     lt_cv_sys_dlopen_deplibs=yes
309 |       lt_cv_sys_dlopen_deplibs=no
314 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
326 |     lt_cv_sys_dlopen_deplibs=yes
329 |     lt_cv_sys_dlopen_deplibs=yes
332 |     lt_cv_sys_dlopen_deplibs=yes
337 |     lt_cv_sys_dlopen_deplibs=unknown
341 |     # at 6.2 and later dlopen does load deplibs.
342 |     lt_cv_sys_dlopen_deplibs=yes
345 |     lt_cv_sys_dlopen_deplibs=yes
348 |     lt_cv_sys_dlopen_deplibs=yes
351 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
354 |     lt_cv_sys_dlopen_deplibs=no
357 |     # dlopen *does* load deplibs and with the right loader patch applied
363 |     lt_cv_sys_dlopen_deplibs=unknown
370 |     lt_cv_sys_dlopen_deplibs=yes
373 |     lt_cv_sys_dlopen_deplibs=yes
376 |     lt_cv_sys_dlopen_deplibs=yes
379 |     libltdl_cv_sys_dlopen_deplibs=yes
383 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
384 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
385 |     [Define if the OS needs help to load dependent libraries for dlopen().])
388 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
391 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
463 | LIBADD_DLOPEN=
464 | AC_SEARCH_LIBS([dlopen], [dl],
467 | 	if test "$ac_cv_search_dlopen" != "none required"; then
468 | 	  LIBADD_DLOPEN=-ldl
470 | 	libltdl_cv_lib_dl_dlopen=yes
471 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
475 |     ]], [[dlopen(0, 0);]])],
478 | 	    libltdl_cv_func_dlopen=yes
479 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
480 | 	[AC_CHECK_LIB([svld], [dlopen],
483 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
484 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
485 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
488 |   LIBS="$LIBS $LIBADD_DLOPEN"
492 | AC_SUBST([LIBADD_DLOPEN])
498 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
502 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
512 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
515 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
519 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
526 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
542 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
594 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
599 |       LIBS="$LIBS $LIBADD_DLOPEN"
657 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
2639 | m4trace:../vendor/common/build-config/m4/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
2640 | if test yes != "$enable_dlopen"; then
2641 |   enable_dlopen=unknown
2642 |   enable_dlopen_self=unknown
2643 |   enable_dlopen_self_static=unknown
2645 |   lt_cv_dlopen=no
2646 |   lt_cv_dlopen_libs=
2650 |     lt_cv_dlopen=load_add_on
2651 |     lt_cv_dlopen_libs=
2652 |     lt_cv_dlopen_self=yes
2656 |     lt_cv_dlopen=LoadLibrary
2657 |     lt_cv_dlopen_libs=
2661 |     lt_cv_dlopen=dlopen
2662 |     lt_cv_dlopen_libs=
2667 |     AC_CHECK_LIB([dl], [dlopen],
2668 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
2669 |     lt_cv_dlopen=dyld
2670 |     lt_cv_dlopen_libs=
2671 |     lt_cv_dlopen_self=yes
2678 |     lt_cv_dlopen=dlopen
2679 |     lt_cv_dlopen_libs=
2680 |     lt_cv_dlopen_self=no
2685 | 	  [lt_cv_dlopen=shl_load],
2687 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
2688 | 	[AC_CHECK_FUNC([dlopen],
2689 | 	      [lt_cv_dlopen=dlopen],
2690 | 	  [AC_CHECK_LIB([dl], [dlopen],
2691 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
2692 | 	    [AC_CHECK_LIB([svld], [dlopen],
2693 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
2695 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2704 |   if test no = "$lt_cv_dlopen"; then
2705 |     enable_dlopen=no
2707 |     enable_dlopen=yes
2710 |   case $lt_cv_dlopen in
2711 |   dlopen)
2719 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2721 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2722 | 	  lt_cv_dlopen_self, [dnl
2723 | 	  _LT_TRY_DLOPEN_SELF(
2724 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2725 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2728 |     if test yes = "$lt_cv_dlopen_self"; then
2730 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2731 | 	  lt_cv_dlopen_self_static, [dnl
2732 | 	  _LT_TRY_DLOPEN_SELF(
2733 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2734 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2744 |   case $lt_cv_dlopen_self in
2745 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2746 |   *) enable_dlopen_self=unknown ;;
2749 |   case $lt_cv_dlopen_self_static in
2750 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2751 |   *) enable_dlopen_self_static=unknown ;;
2754 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2755 | 	 [Whether dlopen is supported])
2756 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2757 | 	 [Whether dlopen of programs is supported])
2758 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2759 | 	 [Whether dlopen of statically linked programs is supported])
2761 | m4trace:../vendor/common/build-config/m4/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2762 | m4trace:../vendor/common/build-config/m4/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2764 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
3073 | m4trace:../vendor/common/build-config/m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
3076 | put the 'dlopen' option into LT_INIT's first parameter.])
3078 | m4trace:../vendor/common/build-config/m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
3080 | _LT_SET_OPTION([LT_INIT], [dlopen])
3083 | put the 'dlopen' option into LT_INIT's first parameter.])
3175 | m4trace:../vendor/common/build-config/m4/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
4186 | m4trace:configure.ac:44: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extlib/opari2/build-frontend/autom4te.cache/output.4

```

{% raw %}
10534 |         enable_dlopen=no
14168 |   if test yes != "$enable_dlopen"; then
14169 |   enable_dlopen=unknown
14170 |   enable_dlopen_self=unknown
14171 |   enable_dlopen_self_static=unknown
14173 |   lt_cv_dlopen=no
14174 |   lt_cv_dlopen_libs=
14178 |     lt_cv_dlopen=load_add_on
14179 |     lt_cv_dlopen_libs=
14180 |     lt_cv_dlopen_self=yes
14184 |     lt_cv_dlopen=LoadLibrary
14185 |     lt_cv_dlopen_libs=
14189 |     lt_cv_dlopen=dlopen
14190 |     lt_cv_dlopen_libs=
14195 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14196 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14197 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14211 | char dlopen ();
14215 | return dlopen ();
14221 |   ac_cv_lib_dl_dlopen=yes
14223 |   ac_cv_lib_dl_dlopen=no
14229 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14230 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14231 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14232 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14235 |     lt_cv_dlopen=dyld
14236 |     lt_cv_dlopen_libs=
14237 |     lt_cv_dlopen_self=yes
14246 |     lt_cv_dlopen=dlopen
14247 |     lt_cv_dlopen_libs=
14248 |     lt_cv_dlopen_self=no
14254 |   lt_cv_dlopen=shl_load
14293 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
14295 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
14296 | if test "x$ac_cv_func_dlopen" = xyes; then :
14297 |   lt_cv_dlopen=dlopen
14299 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14300 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14301 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14315 | char dlopen ();
14319 | return dlopen ();
14325 |   ac_cv_lib_dl_dlopen=yes
14327 |   ac_cv_lib_dl_dlopen=no
14333 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14334 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14335 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14336 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14338 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14339 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14340 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14354 | char dlopen ();
14358 | return dlopen ();
14364 |   ac_cv_lib_svld_dlopen=yes
14366 |   ac_cv_lib_svld_dlopen=no
14372 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14373 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14374 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14375 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
14414 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
14435 |   if test no = "$lt_cv_dlopen"; then
14436 |     enable_dlopen=no
14438 |     enable_dlopen=yes
14441 |   case $lt_cv_dlopen in
14442 |   dlopen)
14450 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14452 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14453 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14454 | if ${lt_cv_dlopen_self+:} false; then :
14458 |   lt_cv_dlopen_self=cross
14513 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14540 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14541 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14542 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14546 |     lt_cv_dlopen_self=no
14553 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14554 | $as_echo "$lt_cv_dlopen_self" >&6; }
14556 |     if test yes = "$lt_cv_dlopen_self"; then
14558 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14559 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14560 | if ${lt_cv_dlopen_self_static+:} false; then :
14564 |   lt_cv_dlopen_self_static=cross
14619 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14646 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14647 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14648 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14652 |     lt_cv_dlopen_self_static=no
14659 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14660 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14669 |   case $lt_cv_dlopen_self in
14670 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14671 |   *) enable_dlopen_self=unknown ;;
14674 |   case $lt_cv_dlopen_self_static in
14675 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14676 |   *) enable_dlopen_self_static=unknown ;;
25167 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
25168 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
25169 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
26593 | # Whether dlopen is supported.
26594 | dlopen_support=$enable_dlopen
26596 | # Whether dlopen of programs is supported.
26597 | dlopen_self=$enable_dlopen_self
26599 | # Whether dlopen of statically linked programs is supported.
26600 | dlopen_self_static=$enable_dlopen_self_static
26644 | # Compiler flag to allow reflexive dlopens.
26886 | # Compiler flag to allow reflexive dlopens.
27039 | # Compiler flag to allow reflexive dlopens.
27192 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### extlib/opari2/build-frontend/autom4te.cache/traces.2

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
290 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
291 |   [lt_cv_sys_dlopen_deplibs],
292 |   [# PORTME does your system automatically load deplibs for dlopen?
296 |   lt_cv_sys_dlopen_deplibs=unknown
301 |     lt_cv_sys_dlopen_deplibs=unknown
304 |     lt_cv_sys_dlopen_deplibs=yes
309 |       lt_cv_sys_dlopen_deplibs=no
314 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
326 |     lt_cv_sys_dlopen_deplibs=yes
329 |     lt_cv_sys_dlopen_deplibs=yes
332 |     lt_cv_sys_dlopen_deplibs=yes
337 |     lt_cv_sys_dlopen_deplibs=unknown
341 |     # at 6.2 and later dlopen does load deplibs.
342 |     lt_cv_sys_dlopen_deplibs=yes
345 |     lt_cv_sys_dlopen_deplibs=yes
348 |     lt_cv_sys_dlopen_deplibs=yes
351 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
354 |     lt_cv_sys_dlopen_deplibs=no
357 |     # dlopen *does* load deplibs and with the right loader patch applied
363 |     lt_cv_sys_dlopen_deplibs=unknown
370 |     lt_cv_sys_dlopen_deplibs=yes
373 |     lt_cv_sys_dlopen_deplibs=yes
376 |     lt_cv_sys_dlopen_deplibs=yes
379 |     libltdl_cv_sys_dlopen_deplibs=yes
383 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
384 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
385 |     [Define if the OS needs help to load dependent libraries for dlopen().])
388 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
391 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
463 | LIBADD_DLOPEN=
464 | AC_SEARCH_LIBS([dlopen], [dl],
467 | 	if test "$ac_cv_search_dlopen" != "none required"; then
468 | 	  LIBADD_DLOPEN=-ldl
470 | 	libltdl_cv_lib_dl_dlopen=yes
471 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
475 |     ]], [[dlopen(0, 0);]])],
478 | 	    libltdl_cv_func_dlopen=yes
479 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
480 | 	[AC_CHECK_LIB([svld], [dlopen],
483 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
484 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
485 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
488 |   LIBS="$LIBS $LIBADD_DLOPEN"
492 | AC_SUBST([LIBADD_DLOPEN])
498 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
502 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
512 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
515 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
519 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
526 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
542 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
594 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
599 |       LIBS="$LIBS $LIBADD_DLOPEN"
657 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
2622 | m4trace:../vendor/common/build-config/m4/libtool.m4:1920: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
2623 | if test yes != "$enable_dlopen"; then
2624 |   enable_dlopen=unknown
2625 |   enable_dlopen_self=unknown
2626 |   enable_dlopen_self_static=unknown
2628 |   lt_cv_dlopen=no
2629 |   lt_cv_dlopen_libs=
2633 |     lt_cv_dlopen=load_add_on
2634 |     lt_cv_dlopen_libs=
2635 |     lt_cv_dlopen_self=yes
2639 |     lt_cv_dlopen=LoadLibrary
2640 |     lt_cv_dlopen_libs=
2644 |     lt_cv_dlopen=dlopen
2645 |     lt_cv_dlopen_libs=
2650 |     AC_CHECK_LIB([dl], [dlopen],
2651 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
2652 |     lt_cv_dlopen=dyld
2653 |     lt_cv_dlopen_libs=
2654 |     lt_cv_dlopen_self=yes
2661 |     lt_cv_dlopen=dlopen
2662 |     lt_cv_dlopen_libs=
2663 |     lt_cv_dlopen_self=no
2668 | 	  [lt_cv_dlopen=shl_load],
2670 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
2671 | 	[AC_CHECK_FUNC([dlopen],
2672 | 	      [lt_cv_dlopen=dlopen],
2673 | 	  [AC_CHECK_LIB([dl], [dlopen],
2674 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
2675 | 	    [AC_CHECK_LIB([svld], [dlopen],
2676 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
2678 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2687 |   if test no = "$lt_cv_dlopen"; then
2688 |     enable_dlopen=no
2690 |     enable_dlopen=yes
2693 |   case $lt_cv_dlopen in
2694 |   dlopen)
2702 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2704 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2705 | 	  lt_cv_dlopen_self, [dnl
2706 | 	  _LT_TRY_DLOPEN_SELF(
2707 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2708 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2711 |     if test yes = "$lt_cv_dlopen_self"; then
2713 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2714 | 	  lt_cv_dlopen_self_static, [dnl
2715 | 	  _LT_TRY_DLOPEN_SELF(
2716 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2717 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2727 |   case $lt_cv_dlopen_self in
2728 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2729 |   *) enable_dlopen_self=unknown ;;
2732 |   case $lt_cv_dlopen_self_static in
2733 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2734 |   *) enable_dlopen_self_static=unknown ;;
2737 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2738 | 	 [Whether dlopen is supported])
2739 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2740 | 	 [Whether dlopen of programs is supported])
2741 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2742 | 	 [Whether dlopen of statically linked programs is supported])
2744 | m4trace:../vendor/common/build-config/m4/libtool.m4:2045: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2745 | m4trace:../vendor/common/build-config/m4/libtool.m4:2045: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2747 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
3056 | m4trace:../vendor/common/build-config/m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
3059 | put the 'dlopen' option into LT_INIT's first parameter.])
3061 | m4trace:../vendor/common/build-config/m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
3063 | _LT_SET_OPTION([LT_INIT], [dlopen])
3066 | put the 'dlopen' option into LT_INIT's first parameter.])
3158 | m4trace:../vendor/common/build-config/m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
4169 | m4trace:configure.ac:44: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### src/pptrace/pptrace.c

```cpp

{% raw %}
592 |   // Wait for dlopen(argv[1])
{% endraw %}

```
### src/core/eztrace_convert_core.c

```cpp

{% raw %}
854 |       void* dlret = dlopen(libname, RTLD_NOW);
{% endraw %}

```
### test/pptrace/perf/tests/libpreload.c

```cpp

{% raw %}
35 |   void* handle = dlopen("libalacon.so", RTLD_NOW);
{% endraw %}

```