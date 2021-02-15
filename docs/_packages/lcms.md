---
name: "lcms"
layout: package
next_package: nettle
previous_package: libluv
languages: ['bash']
---
## 2.6
2 / 200 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
1078 |       --dlopen|-dlopen)
1080 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1201 |     # Only execute mode is allowed to have -dlopen flags.
1202 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1203 |       func_error "unrecognized option \`-dlopen'"
2351 |   -dlopen FILE      add the directory containing FILE to the library path
2353 | This mode sets the library path environment variable according to \`-dlopen'
2408 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2417 |   -module           build a library that can dlopened
2523 |     # Handle -dlopen flags immediately.
2524 |     for file in $opt_dlopen; do
2543 | 	# Skip this library if it cannot be dlopened.
2570 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5206 | 	    dlopen_self=$dlopen_self_static
5212 | 	    dlopen_self=$dlopen_self_static
5218 | 	    dlopen_self=$dlopen_self_static
5276 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5360 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5522 |       -dlopen)
5929 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5997 | 	  # This library was specified with -dlopen.
6114 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6125 | 	passes="conv scan dlopen dlpreopen link"
6151 | 	dlopen) libs="$dlfiles" ;;
6179 |       if test "$pass" = dlopen; then
6397 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6398 | 	      # If there is no dlopen support or we're linking statically,
6428 | 	dlopen=
6458 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6504 | 	# This library was specified with -dlopen.
6505 | 	if test "$pass" = dlopen; then
6507 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6510 | 	     test "$dlopen_support" != yes ||
6512 | 	    # If there is no dlname, no dlopen support or we're linking
6521 | 	fi # $pass = dlopen
6577 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6579 | 	      # We recover the dlopen module name by 'saving' the la file
6603 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6732 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6733 | 	  dlopenmodule=""
6736 | 	      dlopenmodule="$dlpremoduletest"
6740 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6837 | 		    # if the lib is a (non-dlopened) module then we can not
6841 | 		      if test "X$dlopenmodule" != "X$lib"; then
6993 | 	      echo "*** a static module, that should work as long as the dlopening application"
6994 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7138 |       if test "$pass" != dlopen; then
7237 | 	func_warning "\`-dlopen' is ignored for archives"
7304 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7979 | 	    echo "*** a static module, that should work as long as the dlopening"
7980 | 	    echo "*** application is linked with the -dlopen flag."
7998 | 	    echo "*** or is declared to -dlopen it."
8608 | 	func_warning "\`-dlopen' is ignored for objects"
8726 |         && test "$dlopen_support" = unknown \
8727 | 	&& test "$dlopen_self" = unknown \
8728 | 	&& test "$dlopen_self_static" = unknown && \
8729 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9417 | # The name that we can dlopen(3).
9446 | # Files to dlopen/dlpreopen
9447 | dlopen='$dlfiles'
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1698 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1701 | m4_defun([_LT_TRY_DLOPEN_SELF],
1759 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1792 | ])# _LT_TRY_DLOPEN_SELF
1795 | # LT_SYS_DLOPEN_SELF
1797 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1799 | if test "x$enable_dlopen" != xyes; then
1800 |   enable_dlopen=unknown
1801 |   enable_dlopen_self=unknown
1802 |   enable_dlopen_self_static=unknown
1804 |   lt_cv_dlopen=no
1805 |   lt_cv_dlopen_libs=
1809 |     lt_cv_dlopen="load_add_on"
1810 |     lt_cv_dlopen_libs=
1811 |     lt_cv_dlopen_self=yes
1815 |     lt_cv_dlopen="LoadLibrary"
1816 |     lt_cv_dlopen_libs=
1820 |     lt_cv_dlopen="dlopen"
1821 |     lt_cv_dlopen_libs=
1826 |     AC_CHECK_LIB([dl], [dlopen],
1827 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1828 |     lt_cv_dlopen="dyld"
1829 |     lt_cv_dlopen_libs=
1830 |     lt_cv_dlopen_self=yes
1836 | 	  [lt_cv_dlopen="shl_load"],
1838 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1839 | 	[AC_CHECK_FUNC([dlopen],
1840 | 	      [lt_cv_dlopen="dlopen"],
1841 | 	  [AC_CHECK_LIB([dl], [dlopen],
1842 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1843 | 	    [AC_CHECK_LIB([svld], [dlopen],
1844 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1846 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1855 |   if test "x$lt_cv_dlopen" != xno; then
1856 |     enable_dlopen=yes
1858 |     enable_dlopen=no
1861 |   case $lt_cv_dlopen in
1862 |   dlopen)
1870 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1872 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1873 | 	  lt_cv_dlopen_self, [dnl
1874 | 	  _LT_TRY_DLOPEN_SELF(
1875 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1876 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1879 |     if test "x$lt_cv_dlopen_self" = xyes; then
1881 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1882 | 	  lt_cv_dlopen_self_static, [dnl
1883 | 	  _LT_TRY_DLOPEN_SELF(
1884 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1885 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1895 |   case $lt_cv_dlopen_self in
1896 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1897 |   *) enable_dlopen_self=unknown ;;
1900 |   case $lt_cv_dlopen_self_static in
1901 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1902 |   *) enable_dlopen_self_static=unknown ;;
1905 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1906 | 	 [Whether dlopen is supported])
1907 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1908 | 	 [Whether dlopen of programs is supported])
1909 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1910 | 	 [Whether dlopen of statically linked programs is supported])
1911 | ])# LT_SYS_DLOPEN_SELF
1914 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1916 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5601 |     [Compiler flag to allow reflexive dlopens])
5713 |   LT_SYS_DLOPEN_SELF
7908 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7940 | # dlopen
7942 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7945 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7946 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7949 | put the `dlopen' option into LT_INIT's first parameter.])
7953 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8399 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```