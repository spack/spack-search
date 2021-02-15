---
name: "ginac"
layout: package
next_package: hdf-eos2
previous_package: fluxbox
languages: ['bash']
---
## 1.7.11
8 / 298 files match

 - [acinclude.m4](#acincludem4)
 - [config/config.h.in](#configconfighin)
 - [config/ltmain.sh](#configltmainsh)
 - [ginac/utils.cpp](#ginacutilscpp)
 - [ginac/excompiler.cpp](#ginacexcompilercpp)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/lib-link.m4](#m4lib-linkm4)

### acinclude.m4

```

{% raw %}
200 | dnl - Checks if dlopen is available
232 | 	dnl Some systems (GNU/Linux, Solaris) have dlopen in -ldl, some
234 | 	found_dlopen_lib="no"
236 | 	AC_CHECK_LIB(dl, dlopen, [found_dlopen_lib="yes"])
237 | 	if test "$found_dlopen_lib" = "no"; then
239 | 		AC_CHECK_FUNC(dlopen, [found_dlopen_lib="yes"])
241 | 	if test "$found_dlopen_lib" = "no"; then
243 | 		AC_MSG_WARN([Could not found working dlopen(). GiNaC::compile_ex will be disabled.])
245 | 		AC_DEFINE(HAVE_LIBDL, 1, [set to 1 if dlopen() works.])
{% endraw %}

```
### config/config.h.in

```

{% raw %}
11 | /* set to 1 if dlopen() works. */
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
2431 |     opt_dlopen=
2504 |         --dlopen|-dlopen)
2505 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2628 |       # Only execute mode is allowed to have -dlopen flags.
2629 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2630 |         func_error "unrecognized option '-dlopen'"
3856 |   -dlopen FILE      add the directory containing FILE to the library path
3858 | This mode sets the library path environment variable according to '-dlopen'
3913 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3922 |   -module           build a library that can dlopened
4030 |     # Handle -dlopen flags immediately.
4031 |     for file in $opt_dlopen; do
4050 | 	# Skip this library if it cannot be dlopened.
4077 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6771 | 	    dlopen_self=$dlopen_self_static
6777 | 	    dlopen_self=$dlopen_self_static
6783 | 	    dlopen_self=$dlopen_self_static
6841 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6931 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7098 |       -dlopen)
7535 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7603 | 	  # This library was specified with -dlopen.
7723 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7734 | 	passes="conv scan dlopen dlpreopen link"
7760 | 	dlopen) libs=$dlfiles ;;
7791 |       if test dlopen = "$pass"; then
8011 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
8012 | 	      # If there is no dlopen support or we're linking statically,
8040 | 	dlopen=
8070 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8116 | 	# This library was specified with -dlopen.
8117 | 	if test dlopen = "$pass"; then
8119 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8121 | 	     test yes != "$dlopen_support" ||
8124 | 	    # If there is no dlname, no dlopen support or we're linking
8133 | 	fi # $pass = dlopen
8189 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8191 | 	      # We recover the dlopen module name by 'saving' the la file
8215 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8344 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8345 | 	  dlopenmodule=
8348 | 	      dlopenmodule=$dlpremoduletest
8352 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8449 | 		    # if the lib is a (non-dlopened) module then we cannot
8453 | 		      if test "X$dlopenmodule" != "X$lib"; then
8605 | 	      echo "*** a static module, that should work as long as the dlopening application"
8606 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8750 |       if test dlopen != "$pass"; then
8880 | 	func_warning "'-dlopen' is ignored for archives"
8947 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9644 | 	    echo "*** a static module, that should work as long as the dlopening"
9645 | 	    echo "*** application is linked with the -dlopen flag."
9663 | 	    echo "*** or is declared to -dlopen it."
10275 | 	func_warning "'-dlopen' is ignored for objects"
10395 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10396 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
11078 | # The name that we can dlopen(3).
11107 | # Files to dlopen/dlpreopen
11108 | dlopen='$dlfiles'
{% endraw %}

```
### ginac/utils.cpp

```

{% raw %}
405 | 		// (e.g. consider // dlopen/dlsym/dlclose sequence).
{% endraw %}

```
### ginac/excompiler.cpp

```

{% raw %}
166 | 		module = dlopen(filename.c_str(), RTLD_NOW);
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
### m4/lib-link.m4

```

{% raw %}
516 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```