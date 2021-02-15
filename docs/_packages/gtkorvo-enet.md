---
name: "gtkorvo-enet"
layout: package
next_package: openslp
previous_package: uvw
languages: ['bash']
---
## 1.3.13
3 / 44 files match

 - [ltmain.sh](#ltmainsh)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)

### ltmain.sh

```bash

{% raw %}
1073 |       --dlopen|-dlopen)
1075 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1196 |     # Only execute mode is allowed to have -dlopen flags.
1197 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1198 |       func_error "unrecognized option \`-dlopen'"
2346 |   -dlopen FILE      add the directory containing FILE to the library path
2348 | This mode sets the library path environment variable according to \`-dlopen'
2403 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2412 |   -module           build a library that can dlopened
2518 |     # Handle -dlopen flags immediately.
2519 |     for file in $opt_dlopen; do
2538 | 	# Skip this library if it cannot be dlopened.
2565 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5177 | 	    dlopen_self=$dlopen_self_static
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5247 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5331 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5493 |       -dlopen)
5896 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5964 | 	  # This library was specified with -dlopen.
6081 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6092 | 	passes="conv scan dlopen dlpreopen link"
6118 | 	dlopen) libs="$dlfiles" ;;
6146 |       if test "$pass" = dlopen; then
6365 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6366 | 	      # If there is no dlopen support or we're linking statically,
6396 | 	dlopen=
6426 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6472 | 	# This library was specified with -dlopen.
6473 | 	if test "$pass" = dlopen; then
6475 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6478 | 	     test "$dlopen_support" != yes ||
6480 | 	    # If there is no dlname, no dlopen support or we're linking
6489 | 	fi # $pass = dlopen
6545 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6547 | 	      # We recover the dlopen module name by 'saving' the la file
6571 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6700 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6701 | 	  dlopenmodule=""
6704 | 	      dlopenmodule="$dlpremoduletest"
6708 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6805 | 		    # if the lib is a (non-dlopened) module then we can not
6809 | 		      if test "X$dlopenmodule" != "X$lib"; then
6961 | 	      echo "*** a static module, that should work as long as the dlopening application"
6962 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7106 |       if test "$pass" != dlopen; then
7205 | 	func_warning "\`-dlopen' is ignored for archives"
7272 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7947 | 	    echo "*** a static module, that should work as long as the dlopening"
7948 | 	    echo "*** application is linked with the -dlopen flag."
7966 | 	    echo "*** or is declared to -dlopen it."
8577 | 	func_warning "\`-dlopen' is ignored for objects"
8695 |         && test "$dlopen_support" = unknown \
8696 | 	&& test "$dlopen_self" = unknown \
8697 | 	&& test "$dlopen_self_static" = unknown && \
8698 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9379 | # The name that we can dlopen(3).
9408 | # Files to dlopen/dlpreopen
9409 | dlopen='$dlfiles'
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