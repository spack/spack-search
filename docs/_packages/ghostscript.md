---
name: "ghostscript"
layout: package
next_package: coreutils
previous_package: cln
languages: ['cpp', 'bash']
---
## 9.27
19 / 4764 files match

 - [configure.ac](#configureac)
 - [jpeg/ltmain.sh](#jpegltmainsh)
 - [jpeg/aclocal.m4](#jpegaclocalm4)
 - [lcms2mt/ltmain.sh](#lcms2mtltmainsh)
 - [lcms2mt/m4/libtool.m4](#lcms2mtm4libtoolm4)
 - [lcms2mt/m4/ltoptions.m4](#lcms2mtm4ltoptionsm4)
 - [base/gp_unix.c](#basegp_unixc)
 - [base/memento.c](#basemementoc)
 - [libpng/ltmain.sh](#libpngltmainsh)
 - [libpng/scripts/libtool.m4](#libpngscriptslibtoolm4)
 - [libpng/scripts/ltoptions.m4](#libpngscriptsltoptionsm4)
 - [jbig2dec/memento.c](#jbig2decmementoc)
 - [contrib/opvp/gdevopvp.c](#contribopvpgdevopvpc)
 - [tiff/config/ltmain.sh](#tiffconfigltmainsh)
 - [tiff/m4/libtool.m4](#tiffm4libtoolm4)
 - [tiff/m4/ltoptions.m4](#tiffm4ltoptionsm4)
 - [freetype/builds/unix/ltmain.sh](#freetypebuildsunixltmainsh)
 - [freetype/builds/unix/aclocal.m4](#freetypebuildsunixaclocalm4)
 - [ijs/ltmain.sh](#ijsltmainsh)

### configure.ac

```

{% raw %}
582 | AC_CHECK_LIB([dl], [dlopen],
2131 |                 if test x$ac_cv_lib_dl_dlopen != xno -a x$found_iconv != xno; then
2238 |                 if test x$ac_cv_lib_dl_dlopen != xno -a x$found_iconv != xno; then
{% endraw %}

```
### jpeg/ltmain.sh

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
### jpeg/aclocal.m4

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
### lcms2mt/ltmain.sh

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
5903 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5971 | 	  # This library was specified with -dlopen.
6088 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6099 | 	passes="conv scan dlopen dlpreopen link"
6125 | 	dlopen) libs="$dlfiles" ;;
6153 |       if test "$pass" = dlopen; then
6372 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6373 | 	      # If there is no dlopen support or we're linking statically,
6403 | 	dlopen=
6433 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6479 | 	# This library was specified with -dlopen.
6480 | 	if test "$pass" = dlopen; then
6482 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6485 | 	     test "$dlopen_support" != yes ||
6487 | 	    # If there is no dlname, no dlopen support or we're linking
6496 | 	fi # $pass = dlopen
6552 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6554 | 	      # We recover the dlopen module name by 'saving' the la file
6578 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6707 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6708 | 	  dlopenmodule=""
6711 | 	      dlopenmodule="$dlpremoduletest"
6715 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6812 | 		    # if the lib is a (non-dlopened) module then we can not
6816 | 		      if test "X$dlopenmodule" != "X$lib"; then
6968 | 	      echo "*** a static module, that should work as long as the dlopening application"
6969 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7113 |       if test "$pass" != dlopen; then
7212 | 	func_warning "\`-dlopen' is ignored for archives"
7279 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7955 | 	    echo "*** a static module, that should work as long as the dlopening"
7956 | 	    echo "*** application is linked with the -dlopen flag."
7974 | 	    echo "*** or is declared to -dlopen it."
8585 | 	func_warning "\`-dlopen' is ignored for objects"
8703 |         && test "$dlopen_support" = unknown \
8704 | 	&& test "$dlopen_self" = unknown \
8705 | 	&& test "$dlopen_self_static" = unknown && \
8706 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9387 | # The name that we can dlopen(3).
9416 | # Files to dlopen/dlpreopen
9417 | dlopen='$dlfiles'
{% endraw %}

```
### lcms2mt/m4/libtool.m4

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
### lcms2mt/m4/ltoptions.m4

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
### base/gp_unix.c

```cpp

{% raw %}
77 |     if ((handle = dlopen(buff, RTLD_NOW)) != 0) {
{% endraw %}

```
### base/memento.c

```cpp

{% raw %}
555 |     libbt = dlopen("libbacktrace.so", RTLD_LAZY);
557 |         libbt = dlopen("/opt/lib/libbacktrace.so", RTLD_LAZY);
559 |         libbt = dlopen("/lib/libbacktrace.so", RTLD_LAZY);
561 |         libbt = dlopen("/usr/lib/libbacktrace.so", RTLD_LAZY);
563 |         libbt = dlopen("/usr/local/lib/libbacktrace.so", RTLD_LAZY);
{% endraw %}

```
### libpng/ltmain.sh

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
### libpng/scripts/libtool.m4

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
### libpng/scripts/ltoptions.m4

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
### jbig2dec/memento.c

```cpp

{% raw %}
555 |     libbt = dlopen("libbacktrace.so", RTLD_LAZY);
557 |         libbt = dlopen("/opt/lib/libbacktrace.so", RTLD_LAZY);
559 |         libbt = dlopen("/lib/libbacktrace.so", RTLD_LAZY);
561 |         libbt = dlopen("/usr/lib/libbacktrace.so", RTLD_LAZY);
563 |         libbt = dlopen("/usr/local/lib/libbacktrace.so", RTLD_LAZY);
{% endraw %}

```
### contrib/opvp/gdevopvp.c

```cpp

{% raw %}
1780 |             if ((h = dlopen(list[i],RTLD_NOW))) {
{% endraw %}

```
### tiff/config/ltmain.sh

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
### tiff/m4/libtool.m4

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
### tiff/m4/ltoptions.m4

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
### freetype/builds/unix/ltmain.sh

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
### freetype/builds/unix/aclocal.m4

```

{% raw %}
1827 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1830 | m4_defun([_LT_TRY_DLOPEN_SELF],
1888 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1921 | ])# _LT_TRY_DLOPEN_SELF
1924 | # LT_SYS_DLOPEN_SELF
1926 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1928 | if test yes != "$enable_dlopen"; then
1929 |   enable_dlopen=unknown
1930 |   enable_dlopen_self=unknown
1931 |   enable_dlopen_self_static=unknown
1933 |   lt_cv_dlopen=no
1934 |   lt_cv_dlopen_libs=
1938 |     lt_cv_dlopen=load_add_on
1939 |     lt_cv_dlopen_libs=
1940 |     lt_cv_dlopen_self=yes
1944 |     lt_cv_dlopen=LoadLibrary
1945 |     lt_cv_dlopen_libs=
1949 |     lt_cv_dlopen=dlopen
1950 |     lt_cv_dlopen_libs=
1955 |     AC_CHECK_LIB([dl], [dlopen],
1956 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1957 |     lt_cv_dlopen=dyld
1958 |     lt_cv_dlopen_libs=
1959 |     lt_cv_dlopen_self=yes
1966 |     lt_cv_dlopen=dlopen
1967 |     lt_cv_dlopen_libs=
1968 |     lt_cv_dlopen_self=no
1973 | 	  [lt_cv_dlopen=shl_load],
1975 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1976 | 	[AC_CHECK_FUNC([dlopen],
1977 | 	      [lt_cv_dlopen=dlopen],
1978 | 	  [AC_CHECK_LIB([dl], [dlopen],
1979 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1980 | 	    [AC_CHECK_LIB([svld], [dlopen],
1981 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1983 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1992 |   if test no = "$lt_cv_dlopen"; then
1993 |     enable_dlopen=no
1995 |     enable_dlopen=yes
1998 |   case $lt_cv_dlopen in
1999 |   dlopen)
2007 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2009 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2010 | 	  lt_cv_dlopen_self, [dnl
2011 | 	  _LT_TRY_DLOPEN_SELF(
2012 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2013 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2016 |     if test yes = "$lt_cv_dlopen_self"; then
2018 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2019 | 	  lt_cv_dlopen_self_static, [dnl
2020 | 	  _LT_TRY_DLOPEN_SELF(
2021 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2022 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2032 |   case $lt_cv_dlopen_self in
2033 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2034 |   *) enable_dlopen_self=unknown ;;
2037 |   case $lt_cv_dlopen_self_static in
2038 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2039 |   *) enable_dlopen_self_static=unknown ;;
2042 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2043 | 	 [Whether dlopen is supported])
2044 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2045 | 	 [Whether dlopen of programs is supported])
2046 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2047 | 	 [Whether dlopen of statically linked programs is supported])
2048 | ])# LT_SYS_DLOPEN_SELF
2051 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2053 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6128 |     [Compiler flag to allow reflexive dlopens])
6237 |   LT_SYS_DLOPEN_SELF
8546 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8580 | # dlopen
8582 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8585 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8586 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8589 | put the 'dlopen' option into LT_INIT's first parameter.])
8593 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
9107 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### ijs/ltmain.sh

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