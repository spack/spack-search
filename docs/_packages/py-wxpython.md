---
name: "py-wxpython"
layout: package
next_package: vecgeom
previous_package: orbit2
languages: ['cpp', 'bash']
---
## 4.0.6
14 / 17129 files match

 - [ext/wxWidgets/setup.h.in](#extwxwidgetssetuphin)
 - [ext/wxWidgets/setup.h_vms](#extwxwidgetssetuph_vms)
 - [ext/wxWidgets/configure.in](#extwxwidgetsconfigurein)
 - [ext/wxWidgets/src/expat/m4/libtool.m4](#extwxwidgetssrcexpatm4libtoolm4)
 - [ext/wxWidgets/src/expat/m4/ltoptions.m4](#extwxwidgetssrcexpatm4ltoptionsm4)
 - [ext/wxWidgets/src/expat/conftools/ltmain.sh](#extwxwidgetssrcexpatconftoolsltmainsh)
 - [ext/wxWidgets/src/png/ltmain.sh](#extwxwidgetssrcpngltmainsh)
 - [ext/wxWidgets/src/png/scripts/libtool.m4](#extwxwidgetssrcpngscriptslibtoolm4)
 - [ext/wxWidgets/src/png/scripts/ltoptions.m4](#extwxwidgetssrcpngscriptsltoptionsm4)
 - [ext/wxWidgets/src/unix/dlunix.cpp](#extwxwidgetssrcunixdlunixcpp)
 - [ext/wxWidgets/src/tiff/config/ltmain.sh](#extwxwidgetssrctiffconfigltmainsh)
 - [ext/wxWidgets/src/tiff/m4/libtool.m4](#extwxwidgetssrctiffm4libtoolm4)
 - [ext/wxWidgets/src/tiff/m4/ltoptions.m4](#extwxwidgetssrctiffm4ltoptionsm4)
 - [ext/wxWidgets/include/wx/dynlib.h](#extwxwidgetsincludewxdynlibh)

### ext/wxWidgets/setup.h.in

```

{% raw %}
937 | /* Define if you have dlopen() */
938 | #undef HAVE_DLOPEN
{% endraw %}

```
### ext/wxWidgets/setup.h_vms

```

{% raw %}
1001 | /* Define if you have dlopen() */
1002 | #define HAVE_DLOPEN 1
{% endraw %}

```
### ext/wxWidgets/configure.in

```

{% raw %}
5409 |             dnl the test is a bit complicated because we check for dlopen() both with
5411 |             dnl dlopen() on this system
5412 |             AC_CHECK_FUNCS(dlopen,
5414 |                 AC_DEFINE(HAVE_DLOPEN)
5418 |                 AC_CHECK_LIB(dl, dlopen,
5420 |                                 AC_DEFINE(HAVE_DLOPEN)
5453 |             dnl dlopen/dlerror is implemented in dynlib.cpp for Darwin/Mac OS X
{% endraw %}

```
### ext/wxWidgets/src/expat/m4/libtool.m4

```

{% raw %}
1758 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1761 | m4_defun([_LT_TRY_DLOPEN_SELF],
1819 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1852 | ])# _LT_TRY_DLOPEN_SELF
1855 | # LT_SYS_DLOPEN_SELF
1857 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1859 | if test "x$enable_dlopen" != xyes; then
1860 |   enable_dlopen=unknown
1861 |   enable_dlopen_self=unknown
1862 |   enable_dlopen_self_static=unknown
1864 |   lt_cv_dlopen=no
1865 |   lt_cv_dlopen_libs=
1869 |     lt_cv_dlopen="load_add_on"
1870 |     lt_cv_dlopen_libs=
1871 |     lt_cv_dlopen_self=yes
1875 |     lt_cv_dlopen="LoadLibrary"
1876 |     lt_cv_dlopen_libs=
1880 |     lt_cv_dlopen="dlopen"
1881 |     lt_cv_dlopen_libs=
1886 |     AC_CHECK_LIB([dl], [dlopen],
1887 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1888 |     lt_cv_dlopen="dyld"
1889 |     lt_cv_dlopen_libs=
1890 |     lt_cv_dlopen_self=yes
1896 | 	  [lt_cv_dlopen="shl_load"],
1898 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1899 | 	[AC_CHECK_FUNC([dlopen],
1900 | 	      [lt_cv_dlopen="dlopen"],
1901 | 	  [AC_CHECK_LIB([dl], [dlopen],
1902 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1903 | 	    [AC_CHECK_LIB([svld], [dlopen],
1904 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1906 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1915 |   if test "x$lt_cv_dlopen" != xno; then
1916 |     enable_dlopen=yes
1918 |     enable_dlopen=no
1921 |   case $lt_cv_dlopen in
1922 |   dlopen)
1930 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1932 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1933 | 	  lt_cv_dlopen_self, [dnl
1934 | 	  _LT_TRY_DLOPEN_SELF(
1935 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1936 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1939 |     if test "x$lt_cv_dlopen_self" = xyes; then
1941 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1942 | 	  lt_cv_dlopen_self_static, [dnl
1943 | 	  _LT_TRY_DLOPEN_SELF(
1944 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1945 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1955 |   case $lt_cv_dlopen_self in
1956 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1957 |   *) enable_dlopen_self=unknown ;;
1960 |   case $lt_cv_dlopen_self_static in
1961 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1962 |   *) enable_dlopen_self_static=unknown ;;
1965 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1966 | 	 [Whether dlopen is supported])
1967 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1968 | 	 [Whether dlopen of programs is supported])
1969 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1970 | 	 [Whether dlopen of statically linked programs is supported])
1971 | ])# LT_SYS_DLOPEN_SELF
1974 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1976 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5676 |     [Compiler flag to allow reflexive dlopens])
5789 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### ext/wxWidgets/src/expat/m4/ltoptions.m4

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
### ext/wxWidgets/src/expat/conftools/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6155 |       if test "$pass" = dlopen; then
6374 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6375 | 	      # If there is no dlopen support or we're linking statically,
6405 | 	dlopen=
6435 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6481 | 	# This library was specified with -dlopen.
6482 | 	if test "$pass" = dlopen; then
6484 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6487 | 	     test "$dlopen_support" != yes ||
6489 | 	    # If there is no dlname, no dlopen support or we're linking
6498 | 	fi # $pass = dlopen
6554 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6556 | 	      # We recover the dlopen module name by 'saving' the la file
6580 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6709 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6710 | 	  dlopenmodule=""
6713 | 	      dlopenmodule="$dlpremoduletest"
6717 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6814 | 		    # if the lib is a (non-dlopened) module then we can not
6818 | 		      if test "X$dlopenmodule" != "X$lib"; then
6970 | 	      echo "*** a static module, that should work as long as the dlopening application"
6971 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7115 |       if test "$pass" != dlopen; then
7214 | 	func_warning "\`-dlopen' is ignored for archives"
7281 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7960 | 	    echo "*** a static module, that should work as long as the dlopening"
7961 | 	    echo "*** application is linked with the -dlopen flag."
7979 | 	    echo "*** or is declared to -dlopen it."
8590 | 	func_warning "\`-dlopen' is ignored for objects"
8708 |         && test "$dlopen_support" = unknown \
8709 | 	&& test "$dlopen_self" = unknown \
8710 | 	&& test "$dlopen_self_static" = unknown && \
8711 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9392 | # The name that we can dlopen(3).
9421 | # Files to dlopen/dlpreopen
9422 | dlopen='$dlfiles'
{% endraw %}

```
### ext/wxWidgets/src/png/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6155 |       if test "$pass" = dlopen; then
6374 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6375 | 	      # If there is no dlopen support or we're linking statically,
6405 | 	dlopen=
6435 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6481 | 	# This library was specified with -dlopen.
6482 | 	if test "$pass" = dlopen; then
6484 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6487 | 	     test "$dlopen_support" != yes ||
6489 | 	    # If there is no dlname, no dlopen support or we're linking
6498 | 	fi # $pass = dlopen
6554 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6556 | 	      # We recover the dlopen module name by 'saving' the la file
6580 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6709 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6710 | 	  dlopenmodule=""
6713 | 	      dlopenmodule="$dlpremoduletest"
6717 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6814 | 		    # if the lib is a (non-dlopened) module then we can not
6818 | 		      if test "X$dlopenmodule" != "X$lib"; then
6970 | 	      echo "*** a static module, that should work as long as the dlopening application"
6971 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7115 |       if test "$pass" != dlopen; then
7214 | 	func_warning "\`-dlopen' is ignored for archives"
7281 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7960 | 	    echo "*** a static module, that should work as long as the dlopening"
7961 | 	    echo "*** application is linked with the -dlopen flag."
7979 | 	    echo "*** or is declared to -dlopen it."
8590 | 	func_warning "\`-dlopen' is ignored for objects"
8708 |         && test "$dlopen_support" = unknown \
8709 | 	&& test "$dlopen_self" = unknown \
8710 | 	&& test "$dlopen_self_static" = unknown && \
8711 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9392 | # The name that we can dlopen(3).
9421 | # Files to dlopen/dlpreopen
9422 | dlopen='$dlfiles'
{% endraw %}

```
### ext/wxWidgets/src/png/scripts/libtool.m4

```

{% raw %}
1752 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1755 | m4_defun([_LT_TRY_DLOPEN_SELF],
1813 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1846 | ])# _LT_TRY_DLOPEN_SELF
1849 | # LT_SYS_DLOPEN_SELF
1851 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1853 | if test "x$enable_dlopen" != xyes; then
1854 |   enable_dlopen=unknown
1855 |   enable_dlopen_self=unknown
1856 |   enable_dlopen_self_static=unknown
1858 |   lt_cv_dlopen=no
1859 |   lt_cv_dlopen_libs=
1863 |     lt_cv_dlopen="load_add_on"
1864 |     lt_cv_dlopen_libs=
1865 |     lt_cv_dlopen_self=yes
1869 |     lt_cv_dlopen="LoadLibrary"
1870 |     lt_cv_dlopen_libs=
1874 |     lt_cv_dlopen="dlopen"
1875 |     lt_cv_dlopen_libs=
1880 |     AC_CHECK_LIB([dl], [dlopen],
1881 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1882 |     lt_cv_dlopen="dyld"
1883 |     lt_cv_dlopen_libs=
1884 |     lt_cv_dlopen_self=yes
1890 | 	  [lt_cv_dlopen="shl_load"],
1892 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1893 | 	[AC_CHECK_FUNC([dlopen],
1894 | 	      [lt_cv_dlopen="dlopen"],
1895 | 	  [AC_CHECK_LIB([dl], [dlopen],
1896 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1897 | 	    [AC_CHECK_LIB([svld], [dlopen],
1898 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1900 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1909 |   if test "x$lt_cv_dlopen" != xno; then
1910 |     enable_dlopen=yes
1912 |     enable_dlopen=no
1915 |   case $lt_cv_dlopen in
1916 |   dlopen)
1924 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1926 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1927 | 	  lt_cv_dlopen_self, [dnl
1928 | 	  _LT_TRY_DLOPEN_SELF(
1929 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1930 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1933 |     if test "x$lt_cv_dlopen_self" = xyes; then
1935 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1936 | 	  lt_cv_dlopen_self_static, [dnl
1937 | 	  _LT_TRY_DLOPEN_SELF(
1938 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1939 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1949 |   case $lt_cv_dlopen_self in
1950 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1951 |   *) enable_dlopen_self=unknown ;;
1954 |   case $lt_cv_dlopen_self_static in
1955 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1956 |   *) enable_dlopen_self_static=unknown ;;
1959 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1960 | 	 [Whether dlopen is supported])
1961 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1962 | 	 [Whether dlopen of programs is supported])
1963 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1964 | 	 [Whether dlopen of statically linked programs is supported])
1965 | ])# LT_SYS_DLOPEN_SELF
1968 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1970 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5670 |     [Compiler flag to allow reflexive dlopens])
5783 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### ext/wxWidgets/src/png/scripts/ltoptions.m4

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
### ext/wxWidgets/src/unix/dlunix.cpp

```

{% raw %}
34 | #ifdef HAVE_DLOPEN
56 | #if defined(HAVE_DLOPEN) || defined(__DARWIN__)
73 |    return dlopen(0, RTLD_LAZY);
86 |     // we need to use either RTLD_NOW or RTLD_LAZY because if we call dlopen()
94 |     return dlopen(libname.fn_str(), rtldFlags);
{% endraw %}

```
### ext/wxWidgets/src/tiff/config/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### ext/wxWidgets/src/tiff/m4/libtool.m4

```

{% raw %}
1744 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1747 | m4_defun([_LT_TRY_DLOPEN_SELF],
1805 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1838 | ])# _LT_TRY_DLOPEN_SELF
1841 | # LT_SYS_DLOPEN_SELF
1843 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1845 | if test "x$enable_dlopen" != xyes; then
1846 |   enable_dlopen=unknown
1847 |   enable_dlopen_self=unknown
1848 |   enable_dlopen_self_static=unknown
1850 |   lt_cv_dlopen=no
1851 |   lt_cv_dlopen_libs=
1855 |     lt_cv_dlopen="load_add_on"
1856 |     lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen_self=yes
1861 |     lt_cv_dlopen="LoadLibrary"
1862 |     lt_cv_dlopen_libs=
1866 |     lt_cv_dlopen="dlopen"
1867 |     lt_cv_dlopen_libs=
1872 |     AC_CHECK_LIB([dl], [dlopen],
1873 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1874 |     lt_cv_dlopen="dyld"
1875 |     lt_cv_dlopen_libs=
1876 |     lt_cv_dlopen_self=yes
1882 | 	  [lt_cv_dlopen="shl_load"],
1884 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1885 | 	[AC_CHECK_FUNC([dlopen],
1886 | 	      [lt_cv_dlopen="dlopen"],
1887 | 	  [AC_CHECK_LIB([dl], [dlopen],
1888 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1889 | 	    [AC_CHECK_LIB([svld], [dlopen],
1890 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1892 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1901 |   if test "x$lt_cv_dlopen" != xno; then
1902 |     enable_dlopen=yes
1904 |     enable_dlopen=no
1907 |   case $lt_cv_dlopen in
1908 |   dlopen)
1916 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1918 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1919 | 	  lt_cv_dlopen_self, [dnl
1920 | 	  _LT_TRY_DLOPEN_SELF(
1921 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1922 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1925 |     if test "x$lt_cv_dlopen_self" = xyes; then
1927 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1928 | 	  lt_cv_dlopen_self_static, [dnl
1929 | 	  _LT_TRY_DLOPEN_SELF(
1930 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1931 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1941 |   case $lt_cv_dlopen_self in
1942 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1943 |   *) enable_dlopen_self=unknown ;;
1946 |   case $lt_cv_dlopen_self_static in
1947 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1948 |   *) enable_dlopen_self_static=unknown ;;
1951 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1952 | 	 [Whether dlopen is supported])
1953 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1954 | 	 [Whether dlopen of programs is supported])
1955 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1956 | 	 [Whether dlopen of statically linked programs is supported])
1957 | ])# LT_SYS_DLOPEN_SELF
1960 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1962 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5658 |     [Compiler flag to allow reflexive dlopens])
5771 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### ext/wxWidgets/src/tiff/m4/ltoptions.m4

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
### ext/wxWidgets/include/wx/dynlib.h

```cpp

{% raw %}
32 | // native version, even if configure detected presence of DLOPEN.
38 | #elif defined(HAVE_DLOPEN)
268 |     // Return the raw handle from dlopen and friends.
{% endraw %}

```