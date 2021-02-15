---
name: "mpir"
layout: package
next_package: dracut
previous_package: hydra
languages: ['bash']
---
## 2.7.0
3 / 4700 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)
 - [yasm/m4/lib-link.m4](#yasmm4lib-linkm4)

### ltmain.sh

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
5167 | 	    dlopen_self=$dlopen_self_static
5173 | 	    dlopen_self=$dlopen_self_static
5179 | 	    dlopen_self=$dlopen_self_static
5237 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5321 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5483 |       -dlopen)
5886 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5954 | 	  # This library was specified with -dlopen.
6071 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6082 | 	passes="conv scan dlopen dlpreopen link"
6108 | 	dlopen) libs="$dlfiles" ;;
6139 |       if test "$pass" = dlopen; then
6358 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6359 | 	      # If there is no dlopen support or we're linking statically,
6389 | 	dlopen=
6419 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6465 | 	# This library was specified with -dlopen.
6466 | 	if test "$pass" = dlopen; then
6468 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6471 | 	     test "$dlopen_support" != yes ||
6473 | 	    # If there is no dlname, no dlopen support or we're linking
6482 | 	fi # $pass = dlopen
6538 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6540 | 	      # We recover the dlopen module name by 'saving' the la file
6564 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6693 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6694 | 	  dlopenmodule=""
6697 | 	      dlopenmodule="$dlpremoduletest"
6701 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6798 | 		    # if the lib is a (non-dlopened) module then we can not
6802 | 		      if test "X$dlopenmodule" != "X$lib"; then
6954 | 	      echo "*** a static module, that should work as long as the dlopening application"
6955 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7099 |       if test "$pass" != dlopen; then
7198 | 	func_warning "\`-dlopen' is ignored for archives"
7265 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7944 | 	    echo "*** a static module, that should work as long as the dlopening"
7945 | 	    echo "*** application is linked with the -dlopen flag."
7963 | 	    echo "*** or is declared to -dlopen it."
8574 | 	func_warning "\`-dlopen' is ignored for objects"
8692 |         && test "$dlopen_support" = unknown \
8693 | 	&& test "$dlopen_self" = unknown \
8694 | 	&& test "$dlopen_self_static" = unknown && \
8695 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9376 | # The name that we can dlopen(3).
9405 | # Files to dlopen/dlpreopen
9406 | dlopen='$dlfiles'
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1772 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1775 | m4_defun([_LT_TRY_DLOPEN_SELF],
1833 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1866 | ])# _LT_TRY_DLOPEN_SELF
1869 | # LT_SYS_DLOPEN_SELF
1871 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1873 | if test "x$enable_dlopen" != xyes; then
1874 |   enable_dlopen=unknown
1875 |   enable_dlopen_self=unknown
1876 |   enable_dlopen_self_static=unknown
1878 |   lt_cv_dlopen=no
1879 |   lt_cv_dlopen_libs=
1883 |     lt_cv_dlopen="load_add_on"
1884 |     lt_cv_dlopen_libs=
1885 |     lt_cv_dlopen_self=yes
1889 |     lt_cv_dlopen="LoadLibrary"
1890 |     lt_cv_dlopen_libs=
1894 |     lt_cv_dlopen="dlopen"
1895 |     lt_cv_dlopen_libs=
1900 |     AC_CHECK_LIB([dl], [dlopen],
1901 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1902 |     lt_cv_dlopen="dyld"
1903 |     lt_cv_dlopen_libs=
1904 |     lt_cv_dlopen_self=yes
1910 | 	  [lt_cv_dlopen="shl_load"],
1912 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1913 | 	[AC_CHECK_FUNC([dlopen],
1914 | 	      [lt_cv_dlopen="dlopen"],
1915 | 	  [AC_CHECK_LIB([dl], [dlopen],
1916 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1917 | 	    [AC_CHECK_LIB([svld], [dlopen],
1918 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1920 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1929 |   if test "x$lt_cv_dlopen" != xno; then
1930 |     enable_dlopen=yes
1932 |     enable_dlopen=no
1935 |   case $lt_cv_dlopen in
1936 |   dlopen)
1944 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1946 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1947 | 	  lt_cv_dlopen_self, [dnl
1948 | 	  _LT_TRY_DLOPEN_SELF(
1949 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1950 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1953 |     if test "x$lt_cv_dlopen_self" = xyes; then
1955 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1956 | 	  lt_cv_dlopen_self_static, [dnl
1957 | 	  _LT_TRY_DLOPEN_SELF(
1958 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1959 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1969 |   case $lt_cv_dlopen_self in
1970 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1971 |   *) enable_dlopen_self=unknown ;;
1974 |   case $lt_cv_dlopen_self_static in
1975 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1976 |   *) enable_dlopen_self_static=unknown ;;
1979 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1980 | 	 [Whether dlopen is supported])
1981 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1982 | 	 [Whether dlopen of programs is supported])
1983 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1984 | 	 [Whether dlopen of statically linked programs is supported])
1985 | ])# LT_SYS_DLOPEN_SELF
1988 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1990 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5690 |     [Compiler flag to allow reflexive dlopens])
5799 |   LT_SYS_DLOPEN_SELF
8068 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8100 | # dlopen
8102 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8105 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8106 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8109 | put the `dlopen' option into LT_INIT's first parameter.])
8113 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8574 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### yasm/m4/lib-link.m4

```

{% raw %}
459 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```