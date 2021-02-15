---
name: "lua-luaposix"
layout: package
next_package: teckit
previous_package: aspect
languages: ['bash']
---
## 33.2.1
4 / 169 files match

 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/ax_lua.m4](#m4ax_luam4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)

### m4/libtool.m4

```

{% raw %}
1790 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1793 | m4_defun([_LT_TRY_DLOPEN_SELF],
1851 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1884 | ])# _LT_TRY_DLOPEN_SELF
1887 | # LT_SYS_DLOPEN_SELF
1889 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1891 | if test yes != "$enable_dlopen"; then
1892 |   enable_dlopen=unknown
1893 |   enable_dlopen_self=unknown
1894 |   enable_dlopen_self_static=unknown
1896 |   lt_cv_dlopen=no
1897 |   lt_cv_dlopen_libs=
1901 |     lt_cv_dlopen=load_add_on
1902 |     lt_cv_dlopen_libs=
1903 |     lt_cv_dlopen_self=yes
1907 |     lt_cv_dlopen=LoadLibrary
1908 |     lt_cv_dlopen_libs=
1912 |     lt_cv_dlopen=dlopen
1913 |     lt_cv_dlopen_libs=
1918 |     AC_CHECK_LIB([dl], [dlopen],
1919 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1920 |     lt_cv_dlopen=dyld
1921 |     lt_cv_dlopen_libs=
1922 |     lt_cv_dlopen_self=yes
1929 |     lt_cv_dlopen=dlopen
1930 |     lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen_self=no
1936 | 	  [lt_cv_dlopen=shl_load],
1938 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1939 | 	[AC_CHECK_FUNC([dlopen],
1940 | 	      [lt_cv_dlopen=dlopen],
1941 | 	  [AC_CHECK_LIB([dl], [dlopen],
1942 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1943 | 	    [AC_CHECK_LIB([svld], [dlopen],
1944 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1946 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1955 |   if test no = "$lt_cv_dlopen"; then
1956 |     enable_dlopen=no
1958 |     enable_dlopen=yes
1961 |   case $lt_cv_dlopen in
1962 |   dlopen)
1970 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1972 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1973 | 	  lt_cv_dlopen_self, [dnl
1974 | 	  _LT_TRY_DLOPEN_SELF(
1975 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1976 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1979 |     if test yes = "$lt_cv_dlopen_self"; then
1981 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1982 | 	  lt_cv_dlopen_self_static, [dnl
1983 | 	  _LT_TRY_DLOPEN_SELF(
1984 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1985 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1995 |   case $lt_cv_dlopen_self in
1996 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1997 |   *) enable_dlopen_self=unknown ;;
2000 |   case $lt_cv_dlopen_self_static in
2001 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2002 |   *) enable_dlopen_self_static=unknown ;;
2005 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2006 | 	 [Whether dlopen is supported])
2007 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2008 | 	 [Whether dlopen of programs is supported])
2009 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2010 | 	 [Whether dlopen of statically linked programs is supported])
2011 | ])# LT_SYS_DLOPEN_SELF
2014 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2016 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6027 |     [Compiler flag to allow reflexive dlopens])
6140 |   LT_SYS_DLOPEN_SELF
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
### m4/ax_lua.m4

```

{% raw %}
550 |     AC_SEARCH_LIBS([dlopen], [dl])
557 |     AS_IF([test "x$ac_cv_search_dlopen" != 'xno' &&
558 |            test "x$ac_cv_search_dlopen" != 'xnone required'],
559 |       [_ax_lua_extra_libs="$_ax_lua_extra_libs $ac_cv_search_dlopen"])
{% endraw %}

```
### build-aux/ltmain.sh

```bash

{% raw %}
2255 |     opt_dlopen=
2316 |         --dlopen|-dlopen)
2317 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2433 |       # Only execute mode is allowed to have -dlopen flags.
2434 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2435 |         func_error "unrecognized option '-dlopen'"
3661 |   -dlopen FILE      add the directory containing FILE to the library path
3663 | This mode sets the library path environment variable according to '-dlopen'
3718 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3727 |   -module           build a library that can dlopened
3835 |     # Handle -dlopen flags immediately.
3836 |     for file in $opt_dlopen; do
3855 | 	# Skip this library if it cannot be dlopened.
3882 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6557 | 	    dlopen_self=$dlopen_self_static
6563 | 	    dlopen_self=$dlopen_self_static
6569 | 	    dlopen_self=$dlopen_self_static
6627 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6717 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6884 |       -dlopen)
7318 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7386 | 	  # This library was specified with -dlopen.
7503 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7514 | 	passes="conv scan dlopen dlpreopen link"
7540 | 	dlopen) libs=$dlfiles ;;
7568 |       if test dlopen = "$pass"; then
7788 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7789 | 	      # If there is no dlopen support or we're linking statically,
7817 | 	dlopen=
7847 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7893 | 	# This library was specified with -dlopen.
7894 | 	if test dlopen = "$pass"; then
7896 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7898 | 	     test yes != "$dlopen_support" ||
7901 | 	    # If there is no dlname, no dlopen support or we're linking
7910 | 	fi # $pass = dlopen
7966 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7968 | 	      # We recover the dlopen module name by 'saving' the la file
7992 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8121 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8122 | 	  dlopenmodule=
8125 | 	      dlopenmodule=$dlpremoduletest
8129 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8226 | 		    # if the lib is a (non-dlopened) module then we cannot
8230 | 		      if test "X$dlopenmodule" != "X$lib"; then
8382 | 	      echo "*** a static module, that should work as long as the dlopening application"
8383 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8527 |       if test dlopen != "$pass"; then
8626 | 	func_warning "'-dlopen' is ignored for archives"
8693 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9387 | 	    echo "*** a static module, that should work as long as the dlopening"
9388 | 	    echo "*** application is linked with the -dlopen flag."
9406 | 	    echo "*** or is declared to -dlopen it."
10018 | 	func_warning "'-dlopen' is ignored for objects"
10138 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10139 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10820 | # The name that we can dlopen(3).
10849 | # Files to dlopen/dlpreopen
10850 | dlopen='$dlfiles'
{% endraw %}

```