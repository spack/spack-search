---
name: "source-highlight"
layout: package
next_package: sdl2-image
previous_package: percona-server
languages: ['bash']
---
## 3.1.8
3 / 995 files match

 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)

### m4/libtool.m4

```

{% raw %}
1682 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1685 | m4_defun([_LT_TRY_DLOPEN_SELF],
1743 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1776 | ])# _LT_TRY_DLOPEN_SELF
1779 | # LT_SYS_DLOPEN_SELF
1781 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1783 | if test "x$enable_dlopen" != xyes; then
1784 |   enable_dlopen=unknown
1785 |   enable_dlopen_self=unknown
1786 |   enable_dlopen_self_static=unknown
1788 |   lt_cv_dlopen=no
1789 |   lt_cv_dlopen_libs=
1793 |     lt_cv_dlopen="load_add_on"
1794 |     lt_cv_dlopen_libs=
1795 |     lt_cv_dlopen_self=yes
1799 |     lt_cv_dlopen="LoadLibrary"
1800 |     lt_cv_dlopen_libs=
1804 |     lt_cv_dlopen="dlopen"
1805 |     lt_cv_dlopen_libs=
1810 |     AC_CHECK_LIB([dl], [dlopen],
1811 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1812 |     lt_cv_dlopen="dyld"
1813 |     lt_cv_dlopen_libs=
1814 |     lt_cv_dlopen_self=yes
1820 | 	  [lt_cv_dlopen="shl_load"],
1822 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1823 | 	[AC_CHECK_FUNC([dlopen],
1824 | 	      [lt_cv_dlopen="dlopen"],
1825 | 	  [AC_CHECK_LIB([dl], [dlopen],
1826 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1827 | 	    [AC_CHECK_LIB([svld], [dlopen],
1828 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1830 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1839 |   if test "x$lt_cv_dlopen" != xno; then
1840 |     enable_dlopen=yes
1842 |     enable_dlopen=no
1845 |   case $lt_cv_dlopen in
1846 |   dlopen)
1854 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1856 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1857 | 	  lt_cv_dlopen_self, [dnl
1858 | 	  _LT_TRY_DLOPEN_SELF(
1859 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1860 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1863 |     if test "x$lt_cv_dlopen_self" = xyes; then
1865 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1866 | 	  lt_cv_dlopen_self_static, [dnl
1867 | 	  _LT_TRY_DLOPEN_SELF(
1868 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1869 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1879 |   case $lt_cv_dlopen_self in
1880 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1881 |   *) enable_dlopen_self=unknown ;;
1884 |   case $lt_cv_dlopen_self_static in
1885 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1886 |   *) enable_dlopen_self_static=unknown ;;
1889 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1890 | 	 [Whether dlopen is supported])
1891 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1892 | 	 [Whether dlopen of programs is supported])
1893 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1894 | 	 [Whether dlopen of statically linked programs is supported])
1895 | ])# LT_SYS_DLOPEN_SELF
1898 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1900 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5605 |     [Compiler flag to allow reflexive dlopens])
5721 |   LT_SYS_DLOPEN_SELF
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