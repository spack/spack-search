---
name: "libksba"
layout: package
next_package: autoconf-archive
previous_package: dbus-glib
languages: ['bash']
---
## 1.3.5
3 / 122 files match

 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)

### m4/libtool.m4

```

{% raw %}
1750 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1753 | m4_defun([_LT_TRY_DLOPEN_SELF],
1811 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1844 | ])# _LT_TRY_DLOPEN_SELF
1847 | # LT_SYS_DLOPEN_SELF
1849 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1851 | if test "x$enable_dlopen" != xyes; then
1852 |   enable_dlopen=unknown
1853 |   enable_dlopen_self=unknown
1854 |   enable_dlopen_self_static=unknown
1856 |   lt_cv_dlopen=no
1857 |   lt_cv_dlopen_libs=
1861 |     lt_cv_dlopen="load_add_on"
1862 |     lt_cv_dlopen_libs=
1863 |     lt_cv_dlopen_self=yes
1867 |     lt_cv_dlopen="LoadLibrary"
1868 |     lt_cv_dlopen_libs=
1872 |     lt_cv_dlopen="dlopen"
1873 |     lt_cv_dlopen_libs=
1878 |     AC_CHECK_LIB([dl], [dlopen],
1879 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1880 |     lt_cv_dlopen="dyld"
1881 |     lt_cv_dlopen_libs=
1882 |     lt_cv_dlopen_self=yes
1888 | 	  [lt_cv_dlopen="shl_load"],
1890 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1891 | 	[AC_CHECK_FUNC([dlopen],
1892 | 	      [lt_cv_dlopen="dlopen"],
1893 | 	  [AC_CHECK_LIB([dl], [dlopen],
1894 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1895 | 	    [AC_CHECK_LIB([svld], [dlopen],
1896 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1898 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1907 |   if test "x$lt_cv_dlopen" != xno; then
1908 |     enable_dlopen=yes
1910 |     enable_dlopen=no
1913 |   case $lt_cv_dlopen in
1914 |   dlopen)
1922 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1924 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1925 | 	  lt_cv_dlopen_self, [dnl
1926 | 	  _LT_TRY_DLOPEN_SELF(
1927 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1928 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1931 |     if test "x$lt_cv_dlopen_self" = xyes; then
1933 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1934 | 	  lt_cv_dlopen_self_static, [dnl
1935 | 	  _LT_TRY_DLOPEN_SELF(
1936 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1937 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1947 |   case $lt_cv_dlopen_self in
1948 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1949 |   *) enable_dlopen_self=unknown ;;
1952 |   case $lt_cv_dlopen_self_static in
1953 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1954 |   *) enable_dlopen_self_static=unknown ;;
1957 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1958 | 	 [Whether dlopen is supported])
1959 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1960 | 	 [Whether dlopen of programs is supported])
1961 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1962 | 	 [Whether dlopen of statically linked programs is supported])
1963 | ])# LT_SYS_DLOPEN_SELF
1966 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1968 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5703 |     [Compiler flag to allow reflexive dlopens])
5816 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### build-aux/ltmain.sh

```bash

{% raw %}
1079 |       --dlopen|-dlopen)
1081 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1206 |     # Only execute mode is allowed to have -dlopen flags.
1207 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1208 |       func_error "unrecognized option \`-dlopen'"
2356 |   -dlopen FILE      add the directory containing FILE to the library path
2358 | This mode sets the library path environment variable according to \`-dlopen'
2413 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2422 |   -module           build a library that can dlopened
2528 |     # Handle -dlopen flags immediately.
2529 |     for file in $opt_dlopen; do
2548 | 	# Skip this library if it cannot be dlopened.
2575 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5187 | 	    dlopen_self=$dlopen_self_static
5193 | 	    dlopen_self=$dlopen_self_static
5199 | 	    dlopen_self=$dlopen_self_static
5257 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5341 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5503 |       -dlopen)
5906 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5974 | 	  # This library was specified with -dlopen.
6091 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6102 | 	passes="conv scan dlopen dlpreopen link"
6128 | 	dlopen) libs="$dlfiles" ;;
6159 |       if test "$pass" = dlopen; then
6378 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6379 | 	      # If there is no dlopen support or we're linking statically,
6409 | 	dlopen=
6439 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6485 | 	# This library was specified with -dlopen.
6486 | 	if test "$pass" = dlopen; then
6488 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6491 | 	     test "$dlopen_support" != yes ||
6493 | 	    # If there is no dlname, no dlopen support or we're linking
6502 | 	fi # $pass = dlopen
6558 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6560 | 	      # We recover the dlopen module name by 'saving' the la file
6584 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6713 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6714 | 	  dlopenmodule=""
6717 | 	      dlopenmodule="$dlpremoduletest"
6721 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6818 | 		    # if the lib is a (non-dlopened) module then we can not
6822 | 		      if test "X$dlopenmodule" != "X$lib"; then
6974 | 	      echo "*** a static module, that should work as long as the dlopening application"
6975 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7119 |       if test "$pass" != dlopen; then
7218 | 	func_warning "\`-dlopen' is ignored for archives"
7285 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7964 | 	    echo "*** a static module, that should work as long as the dlopening"
7965 | 	    echo "*** application is linked with the -dlopen flag."
7983 | 	    echo "*** or is declared to -dlopen it."
8594 | 	func_warning "\`-dlopen' is ignored for objects"
8712 |         && test "$dlopen_support" = unknown \
8713 | 	&& test "$dlopen_self" = unknown \
8714 | 	&& test "$dlopen_self_static" = unknown && \
8715 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9396 | # The name that we can dlopen(3).
9425 | # Files to dlopen/dlpreopen
9426 | dlopen='$dlfiles'
{% endraw %}

```