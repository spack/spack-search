---
name: "gengetopt"
layout: package
next_package: exonerate
previous_package: nghttp2
languages: ['bash']
---
## 2.23
3 / 355 files match

 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)

### m4/libtool.m4

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
6146 |     [Compiler flag to allow reflexive dlopens])
6259 |   LT_SYS_DLOPEN_SELF
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
### build-aux/ltmain.sh

```bash

{% raw %}
2461 |     opt_dlopen=
2532 |         --dlopen|-dlopen)
2533 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2654 |       # Only execute mode is allowed to have -dlopen flags.
2655 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2656 |         func_error "unrecognized option '-dlopen'"
3882 |   -dlopen FILE      add the directory containing FILE to the library path
3884 | This mode sets the library path environment variable according to '-dlopen'
3939 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3948 |   -module           build a library that can dlopened
4056 |     # Handle -dlopen flags immediately.
4057 |     for file in $opt_dlopen; do
4076 | 	# Skip this library if it cannot be dlopened.
4103 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6797 | 	    dlopen_self=$dlopen_self_static
6803 | 	    dlopen_self=$dlopen_self_static
6809 | 	    dlopen_self=$dlopen_self_static
6867 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6957 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7124 |       -dlopen)
7562 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7630 | 	  # This library was specified with -dlopen.
7750 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7761 | 	passes="conv scan dlopen dlpreopen link"
7787 | 	dlopen) libs=$dlfiles ;;
7815 |       if test dlopen = "$pass"; then
8035 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
8036 | 	      # If there is no dlopen support or we're linking statically,
8064 | 	dlopen=
8094 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8140 | 	# This library was specified with -dlopen.
8141 | 	if test dlopen = "$pass"; then
8143 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8145 | 	     test yes != "$dlopen_support" ||
8148 | 	    # If there is no dlname, no dlopen support or we're linking
8157 | 	fi # $pass = dlopen
8213 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8215 | 	      # We recover the dlopen module name by 'saving' the la file
8239 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8368 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8369 | 	  dlopenmodule=
8372 | 	      dlopenmodule=$dlpremoduletest
8376 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8473 | 		    # if the lib is a (non-dlopened) module then we cannot
8477 | 		      if test "X$dlopenmodule" != "X$lib"; then
8629 | 	      echo "*** a static module, that should work as long as the dlopening application"
8630 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8774 |       if test dlopen != "$pass"; then
8904 | 	func_warning "'-dlopen' is ignored for archives"
8971 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9665 | 	    echo "*** a static module, that should work as long as the dlopening"
9666 | 	    echo "*** application is linked with the -dlopen flag."
9684 | 	    echo "*** or is declared to -dlopen it."
10296 | 	func_warning "'-dlopen' is ignored for objects"
10416 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10417 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
11101 | # The name that we can dlopen(3).
11130 | # Files to dlopen/dlpreopen
11131 | dlopen='$dlfiles'
{% endraw %}

```