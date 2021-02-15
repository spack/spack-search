---
name: "file"
layout: package
next_package: libxkbcommon
previous_package: glusterfs
languages: ['cpp', 'bash']
---
## 5.37
4 / 149 files match

 - [ltmain.sh](#ltmainsh)
 - [src/readelf.h](#srcreadelfh)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)

### ltmain.sh

```bash

{% raw %}
1076 |       --dlopen|-dlopen)
1078 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1203 |     # Only execute mode is allowed to have -dlopen flags.
1204 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1205 |       func_error "unrecognized option \`-dlopen'"
2353 |   -dlopen FILE      add the directory containing FILE to the library path
2355 | This mode sets the library path environment variable according to \`-dlopen'
2410 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2419 |   -module           build a library that can dlopened
2525 |     # Handle -dlopen flags immediately.
2526 |     for file in $opt_dlopen; do
2545 | 	# Skip this library if it cannot be dlopened.
2572 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5184 | 	    dlopen_self=$dlopen_self_static
5190 | 	    dlopen_self=$dlopen_self_static
5196 | 	    dlopen_self=$dlopen_self_static
5254 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5338 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5500 |       -dlopen)
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
6972 | 	      echo "*** a static module, that should work as long as the dlopening application"
6973 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7117 |       if test "$pass" != dlopen; then
7216 | 	func_warning "\`-dlopen' is ignored for archives"
7283 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7967 | 	    echo "*** a static module, that should work as long as the dlopening"
7968 | 	    echo "*** application is linked with the -dlopen flag."
7986 | 	    echo "*** or is declared to -dlopen it."
8597 | 	func_warning "\`-dlopen' is ignored for objects"
8715 |         && test "$dlopen_support" = unknown \
8716 | 	&& test "$dlopen_self" = unknown \
8717 | 	&& test "$dlopen_self_static" = unknown && \
8718 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9399 | # The name that we can dlopen(3).
9428 | # Files to dlopen/dlpreopen
9429 | dlopen='$dlfiles'
{% endraw %}

```
### src/readelf.h

```cpp

{% raw %}
522 | #define	DF_1_NOOPEN	0x00000040	/* Do not allow loading on dlopen() */
{% endraw %}

```
### m4/libtool.m4

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