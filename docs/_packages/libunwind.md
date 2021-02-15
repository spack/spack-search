---
name: "libunwind"
layout: package
next_package: wonton
previous_package: bcftools
languages: ['bash']
---
## 1.5.0
5 / 773 files match

 - [configure.ac](#configureac)
 - [aclocal.m4](#aclocalm4)
 - [config/ltmain.sh](#configltmainsh)
 - [doc/libunwind-dynamic.tex](#doclibunwind-dynamictex)
 - [doc/libunwind-dynamic.man](#doclibunwind-dynamicman)

### configure.ac

```

{% raw %}
27 | AC_SEARCH_LIBS(dlopen, dl)
29 | case "$ac_cv_search_dlopen" in
30 |   -l*) DLLIB=$ac_cv_search_dlopen;;
{% endraw %}

```
### aclocal.m4

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
### config/ltmain.sh

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
### doc/libunwind-dynamic.tex

```

{% raw %}
163 | \Func{dlopen}()).  In this format, the details of a group of procedures
{% endraw %}

```
### doc/libunwind-dynamic.man

```

{% raw %}
221 | dlopen()).
{% endraw %}

```