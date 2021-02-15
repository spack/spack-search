---
name: "libnbc"
layout: package
next_package: plplot
previous_package: libwebsockets
languages: ['bash']
---
## 1.1.1
2 / 59 files match

 - [aclocal.m4](#aclocalm4)
 - [config/ltmain.sh](#configltmainsh)

### aclocal.m4

```

{% raw %}
1697 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1700 | m4_defun([_LT_TRY_DLOPEN_SELF],
1758 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1791 | ])# _LT_TRY_DLOPEN_SELF
1794 | # LT_SYS_DLOPEN_SELF
1796 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1798 | if test "x$enable_dlopen" != xyes; then
1799 |   enable_dlopen=unknown
1800 |   enable_dlopen_self=unknown
1801 |   enable_dlopen_self_static=unknown
1803 |   lt_cv_dlopen=no
1804 |   lt_cv_dlopen_libs=
1808 |     lt_cv_dlopen="load_add_on"
1809 |     lt_cv_dlopen_libs=
1810 |     lt_cv_dlopen_self=yes
1814 |     lt_cv_dlopen="LoadLibrary"
1815 |     lt_cv_dlopen_libs=
1819 |     lt_cv_dlopen="dlopen"
1820 |     lt_cv_dlopen_libs=
1825 |     AC_CHECK_LIB([dl], [dlopen],
1826 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1827 |     lt_cv_dlopen="dyld"
1828 |     lt_cv_dlopen_libs=
1829 |     lt_cv_dlopen_self=yes
1835 | 	  [lt_cv_dlopen="shl_load"],
1837 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1838 | 	[AC_CHECK_FUNC([dlopen],
1839 | 	      [lt_cv_dlopen="dlopen"],
1840 | 	  [AC_CHECK_LIB([dl], [dlopen],
1841 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1842 | 	    [AC_CHECK_LIB([svld], [dlopen],
1843 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1845 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1854 |   if test "x$lt_cv_dlopen" != xno; then
1855 |     enable_dlopen=yes
1857 |     enable_dlopen=no
1860 |   case $lt_cv_dlopen in
1861 |   dlopen)
1869 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1871 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1872 | 	  lt_cv_dlopen_self, [dnl
1873 | 	  _LT_TRY_DLOPEN_SELF(
1874 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1875 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1878 |     if test "x$lt_cv_dlopen_self" = xyes; then
1880 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1881 | 	  lt_cv_dlopen_self_static, [dnl
1882 | 	  _LT_TRY_DLOPEN_SELF(
1883 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1884 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1894 |   case $lt_cv_dlopen_self in
1895 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1896 |   *) enable_dlopen_self=unknown ;;
1899 |   case $lt_cv_dlopen_self_static in
1900 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1901 |   *) enable_dlopen_self_static=unknown ;;
1904 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1905 | 	 [Whether dlopen is supported])
1906 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1907 | 	 [Whether dlopen of programs is supported])
1908 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1909 | 	 [Whether dlopen of statically linked programs is supported])
1910 | ])# LT_SYS_DLOPEN_SELF
1913 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1915 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5600 |     [Compiler flag to allow reflexive dlopens])
5712 |   LT_SYS_DLOPEN_SELF
7907 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7939 | # dlopen
7941 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7944 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7945 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7948 | put the `dlopen' option into LT_INIT's first parameter.])
7952 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8398 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### config/ltmain.sh

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
5171 | 	    dlopen_self=$dlopen_self_static
5177 | 	    dlopen_self=$dlopen_self_static
5183 | 	    dlopen_self=$dlopen_self_static
5241 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5325 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5487 |       -dlopen)
5889 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5957 | 	  # This library was specified with -dlopen.
6074 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6085 | 	passes="conv scan dlopen dlpreopen link"
6111 | 	dlopen) libs="$dlfiles" ;;
6139 |       if test "$pass" = dlopen; then
6357 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6358 | 	      # If there is no dlopen support or we're linking statically,
6388 | 	dlopen=
6418 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6464 | 	# This library was specified with -dlopen.
6465 | 	if test "$pass" = dlopen; then
6467 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6470 | 	     test "$dlopen_support" != yes ||
6472 | 	    # If there is no dlname, no dlopen support or we're linking
6481 | 	fi # $pass = dlopen
6537 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6539 | 	      # We recover the dlopen module name by 'saving' the la file
6563 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6692 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6693 | 	  dlopenmodule=""
6696 | 	      dlopenmodule="$dlpremoduletest"
6700 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6797 | 		    # if the lib is a (non-dlopened) module then we can not
6801 | 		      if test "X$dlopenmodule" != "X$lib"; then
6953 | 	      echo "*** a static module, that should work as long as the dlopening application"
6954 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7098 |       if test "$pass" != dlopen; then
7197 | 	func_warning "\`-dlopen' is ignored for archives"
7264 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7939 | 	    echo "*** a static module, that should work as long as the dlopening"
7940 | 	    echo "*** application is linked with the -dlopen flag."
7958 | 	    echo "*** or is declared to -dlopen it."
8568 | 	func_warning "\`-dlopen' is ignored for objects"
8686 |         && test "$dlopen_support" = unknown \
8687 | 	&& test "$dlopen_self" = unknown \
8688 | 	&& test "$dlopen_self_static" = unknown && \
8689 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9367 | # The name that we can dlopen(3).
9396 | # Files to dlopen/dlpreopen
9397 | dlopen='$dlfiles'
{% endraw %}

```