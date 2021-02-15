---
name: "jose"
layout: package
next_package: rdc
previous_package: bolt
languages: ['bash']
---
## 8
2 / 236 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

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
### aclocal.m4

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
6139 |     [Compiler flag to allow reflexive dlopens])
6248 |   LT_SYS_DLOPEN_SELF
8443 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8477 | # dlopen
8479 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8482 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8483 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8486 | put the 'dlopen' option into LT_INIT's first parameter.])
8490 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
9004 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```