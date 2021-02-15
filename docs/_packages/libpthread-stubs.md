---
name: "libpthread-stubs"
layout: package
next_package: meme
previous_package: adios2
languages: ['bash']
---
## 0.3
2 / 10 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
737 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
787 |       -dlopen=*|--mode=*|--tag=*)
876 |   # Only execute mode is allowed to have -dlopen flags.
878 |     func_error "unrecognized option \`-dlopen'"
1505 |   -dlopen FILE      add the directory containing FILE to the library path
1507 | This mode sets the library path environment variable according to \`-dlopen'
1560 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1569 |   -module           build a library that can dlopened
1644 |     # Handle -dlopen flags immediately.
1661 | 	# Skip this library if it cannot be dlopened.
1688 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4121 | 	    dlopen_self=$dlopen_self_static
4127 | 	    dlopen_self=$dlopen_self_static
4133 | 	    dlopen_self=$dlopen_self_static
4186 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4270 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4427 |       -dlopen)
4814 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4881 | 	  # This library was specified with -dlopen.
4996 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5007 | 	passes="conv scan dlopen dlpreopen link"
5033 | 	dlopen) libs="$dlfiles" ;;
5062 |       if test "$pass" = dlopen; then
5274 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5275 | 	      # If there is no dlopen support or we're linking statically,
5305 | 	dlopen=
5335 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5375 | 	# This library was specified with -dlopen.
5376 | 	if test "$pass" = dlopen; then
5378 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5381 | 	     test "$dlopen_support" != yes ||
5383 | 	    # If there is no dlname, no dlopen support or we're linking
5392 | 	fi # $pass = dlopen
5450 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5576 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5577 | 	  dlopenmodule=""
5580 | 	      dlopenmodule="$dlpremoduletest"
5584 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5681 | 		    # if the lib is a (non-dlopened) module then we can not
5685 | 		      if test "X$dlopenmodule" != "X$lib"; then
5837 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5838 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5974 |       if test "$pass" != dlopen; then
6073 | 	func_warning "\`-dlopen' is ignored for archives"
6140 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6805 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6806 | 	    $ECHO "*** application is linked with the -dlopen flag."
6824 | 	    $ECHO "*** or is declared to -dlopen it."
7391 | 	func_warning "\`-dlopen' is ignored for objects"
7506 |         && test "$dlopen_support" = unknown \
7507 | 	&& test "$dlopen_self" = unknown \
7508 | 	&& test "$dlopen_self_static" = unknown && \
7509 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8141 | # The name that we can dlopen(3).
8170 | # Files to dlopen/dlpreopen
8171 | dlopen='$dlfiles'
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1649 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1652 | m4_defun([_LT_TRY_DLOPEN_SELF],
1704 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1733 | ])# _LT_TRY_DLOPEN_SELF
1736 | # LT_SYS_DLOPEN_SELF
1738 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1740 | if test "x$enable_dlopen" != xyes; then
1741 |   enable_dlopen=unknown
1742 |   enable_dlopen_self=unknown
1743 |   enable_dlopen_self_static=unknown
1745 |   lt_cv_dlopen=no
1746 |   lt_cv_dlopen_libs=
1750 |     lt_cv_dlopen="load_add_on"
1751 |     lt_cv_dlopen_libs=
1752 |     lt_cv_dlopen_self=yes
1756 |     lt_cv_dlopen="LoadLibrary"
1757 |     lt_cv_dlopen_libs=
1761 |     lt_cv_dlopen="dlopen"
1762 |     lt_cv_dlopen_libs=
1767 |     AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1769 |     lt_cv_dlopen="dyld"
1770 |     lt_cv_dlopen_libs=
1771 |     lt_cv_dlopen_self=yes
1777 | 	  [lt_cv_dlopen="shl_load"],
1779 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1780 | 	[AC_CHECK_FUNC([dlopen],
1781 | 	      [lt_cv_dlopen="dlopen"],
1782 | 	  [AC_CHECK_LIB([dl], [dlopen],
1783 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1784 | 	    [AC_CHECK_LIB([svld], [dlopen],
1785 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1787 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1796 |   if test "x$lt_cv_dlopen" != xno; then
1797 |     enable_dlopen=yes
1799 |     enable_dlopen=no
1802 |   case $lt_cv_dlopen in
1803 |   dlopen)
1811 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1813 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1814 | 	  lt_cv_dlopen_self, [dnl
1815 | 	  _LT_TRY_DLOPEN_SELF(
1816 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1817 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1820 |     if test "x$lt_cv_dlopen_self" = xyes; then
1822 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1823 | 	  lt_cv_dlopen_self_static, [dnl
1824 | 	  _LT_TRY_DLOPEN_SELF(
1825 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1826 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1836 |   case $lt_cv_dlopen_self in
1837 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1838 |   *) enable_dlopen_self=unknown ;;
1841 |   case $lt_cv_dlopen_self_static in
1842 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1843 |   *) enable_dlopen_self_static=unknown ;;
1846 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1847 | 	 [Whether dlopen is supported])
1848 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1849 | 	 [Whether dlopen of programs is supported])
1850 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1851 | 	 [Whether dlopen of statically linked programs is supported])
1852 | ])# LT_SYS_DLOPEN_SELF
1855 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1857 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5189 |     [Compiler flag to allow reflexive dlopens])
5301 |   LT_SYS_DLOPEN_SELF
7451 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7483 | # dlopen
7485 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7488 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7489 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7492 | put the `dlopen' option into LT_INIT's first parameter.])
7496 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
7942 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```