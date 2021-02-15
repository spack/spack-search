---
name: "freetype"
layout: package
next_package: clp
previous_package: libxpm
languages: ['bash']
---
## 2.5.3
2 / 694 files match

 - [builds/unix/ltmain.sh](#buildsunixltmainsh)
 - [builds/unix/aclocal.m4](#buildsunixaclocalm4)

### builds/unix/ltmain.sh

```bash

{% raw %}
2255 |     opt_dlopen=
2316 |         --dlopen|-dlopen)
2317 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2433 |       # Only execute mode is allowed to have -dlopen flags.
2434 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2435 |         func_error "unrecognized option '-dlopen'"
3653 |   -dlopen FILE      add the directory containing FILE to the library path
3655 | This mode sets the library path environment variable according to '-dlopen'
3710 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3719 |   -module           build a library that can dlopened
3826 |     # Handle -dlopen flags immediately.
3827 |     for file in $opt_dlopen; do
3846 | 	# Skip this library if it cannot be dlopened.
3873 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6535 | 	    dlopen_self=$dlopen_self_static
6541 | 	    dlopen_self=$dlopen_self_static
6547 | 	    dlopen_self=$dlopen_self_static
6605 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6695 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6857 |       -dlopen)
7266 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7334 | 	  # This library was specified with -dlopen.
7451 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7462 | 	passes="conv scan dlopen dlpreopen link"
7488 | 	dlopen) libs=$dlfiles ;;
7516 |       if test dlopen = "$pass"; then
7736 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7737 | 	      # If there is no dlopen support or we're linking statically,
7765 | 	dlopen=
7795 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7841 | 	# This library was specified with -dlopen.
7842 | 	if test dlopen = "$pass"; then
7844 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7846 | 	     test yes != "$dlopen_support" ||
7849 | 	    # If there is no dlname, no dlopen support or we're linking
7858 | 	fi # $pass = dlopen
7914 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7916 | 	      # We recover the dlopen module name by 'saving' the la file
7940 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8069 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8070 | 	  dlopenmodule=
8073 | 	      dlopenmodule=$dlpremoduletest
8077 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8174 | 		    # if the lib is a (non-dlopened) module then we cannot
8178 | 		      if test "X$dlopenmodule" != "X$lib"; then
8330 | 	      echo "*** a static module, that should work as long as the dlopening application"
8331 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8475 |       if test dlopen != "$pass"; then
8574 | 	func_warning "'-dlopen' is ignored for archives"
8641 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9329 | 	    echo "*** a static module, that should work as long as the dlopening"
9330 | 	    echo "*** application is linked with the -dlopen flag."
9348 | 	    echo "*** or is declared to -dlopen it."
9960 | 	func_warning "'-dlopen' is ignored for objects"
10080 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10081 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10762 | # The name that we can dlopen(3).
10791 | # Files to dlopen/dlpreopen
10792 | dlopen='$dlfiles'
{% endraw %}

```
### builds/unix/aclocal.m4

```

{% raw %}
1795 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1798 | m4_defun([_LT_TRY_DLOPEN_SELF],
1856 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1889 | ])# _LT_TRY_DLOPEN_SELF
1892 | # LT_SYS_DLOPEN_SELF
1894 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1896 | if test yes != "$enable_dlopen"; then
1897 |   enable_dlopen=unknown
1898 |   enable_dlopen_self=unknown
1899 |   enable_dlopen_self_static=unknown
1901 |   lt_cv_dlopen=no
1902 |   lt_cv_dlopen_libs=
1906 |     lt_cv_dlopen=load_add_on
1907 |     lt_cv_dlopen_libs=
1908 |     lt_cv_dlopen_self=yes
1912 |     lt_cv_dlopen=LoadLibrary
1913 |     lt_cv_dlopen_libs=
1917 |     lt_cv_dlopen=dlopen
1918 |     lt_cv_dlopen_libs=
1923 |     AC_CHECK_LIB([dl], [dlopen],
1924 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1925 |     lt_cv_dlopen=dyld
1926 |     lt_cv_dlopen_libs=
1927 |     lt_cv_dlopen_self=yes
1934 |     lt_cv_dlopen=dlopen
1935 |     lt_cv_dlopen_libs=
1936 |     lt_cv_dlopen_self=no
1941 | 	  [lt_cv_dlopen=shl_load],
1943 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1944 | 	[AC_CHECK_FUNC([dlopen],
1945 | 	      [lt_cv_dlopen=dlopen],
1946 | 	  [AC_CHECK_LIB([dl], [dlopen],
1947 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1948 | 	    [AC_CHECK_LIB([svld], [dlopen],
1949 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1951 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1960 |   if test no = "$lt_cv_dlopen"; then
1961 |     enable_dlopen=no
1963 |     enable_dlopen=yes
1966 |   case $lt_cv_dlopen in
1967 |   dlopen)
1975 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1977 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1978 | 	  lt_cv_dlopen_self, [dnl
1979 | 	  _LT_TRY_DLOPEN_SELF(
1980 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1981 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1984 |     if test yes = "$lt_cv_dlopen_self"; then
1986 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1987 | 	  lt_cv_dlopen_self_static, [dnl
1988 | 	  _LT_TRY_DLOPEN_SELF(
1989 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1990 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2000 |   case $lt_cv_dlopen_self in
2001 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2002 |   *) enable_dlopen_self=unknown ;;
2005 |   case $lt_cv_dlopen_self_static in
2006 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2007 |   *) enable_dlopen_self_static=unknown ;;
2010 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2011 | 	 [Whether dlopen is supported])
2012 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2013 | 	 [Whether dlopen of programs is supported])
2014 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2015 | 	 [Whether dlopen of statically linked programs is supported])
2016 | ])# LT_SYS_DLOPEN_SELF
2019 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2021 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5786 |     [Compiler flag to allow reflexive dlopens])
5895 |   LT_SYS_DLOPEN_SELF
8047 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8079 | # dlopen
8081 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8084 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8085 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8088 | put the 'dlopen' option into LT_INIT's first parameter.])
8092 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8553 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```