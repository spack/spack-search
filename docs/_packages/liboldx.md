---
name: "liboldx"
layout: package
next_package: libical
previous_package: ufo-core
languages: ['bash']
---
## 1.0.1
2 / 19 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
370 |   -dlopen)
371 |     prevopt="-dlopen"
443 |   # Only execute mode is allowed to have -dlopen flags.
445 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
965 | 	    dlopen_self=$dlopen_self_static
969 | 	    dlopen_self=$dlopen_self_static
1025 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1117 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1262 |       -dlopen)
1606 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1674 | 	  # This library was specified with -dlopen.
1816 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1828 | 	passes="conv scan dlopen dlpreopen link"
1841 | 	dlopen) libs="$dlfiles" ;;
1846 |       if test "$pass" = dlopen; then
2014 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2015 | 	      # If there is no dlopen support or we're linking statically,
2048 | 	dlopen=
2067 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2110 | 	# This library was specified with -dlopen.
2111 | 	if test "$pass" = dlopen; then
2113 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2117 | 	     test "$dlopen_support" != yes ||
2119 | 	    # If there is no dlname, no dlopen support or we're linking
2128 | 	fi # $pass = dlopen
2173 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2540 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2541 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2694 |       if test "$pass" != dlopen; then
2795 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
2862 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3495 | 	    $echo "*** a static module, that should work as long as the dlopening"
3496 | 	    $echo "*** application is linked with the -dlopen flag."
3514 | 	    $echo "*** or is declared to -dlopen it."
3926 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4112 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4113 | 	   test "$dlopen_self_static" = unknown; then
4114 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5239 | # The name that we can dlopen(3).
5262 | # Files to dlopen/dlpreopen
5263 | dlopen='$dlfiles'
5878 |     # Handle -dlopen flags immediately.
5907 | 	# Skip this library if it cannot be dlopened.
5932 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6283 |   -dlopen FILE      add the directory containing FILE to the library path
6285 | This mode sets the library path environment variable according to \`-dlopen'
6334 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6343 |   -module           build a library that can dlopened
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1089 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
1592 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1595 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
1651 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1678 | ])# _LT_AC_TRY_DLOPEN_SELF
1681 | # AC_LIBTOOL_DLOPEN_SELF
1683 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1685 | if test "x$enable_dlopen" != xyes; then
1686 |   enable_dlopen=unknown
1687 |   enable_dlopen_self=unknown
1688 |   enable_dlopen_self_static=unknown
1690 |   lt_cv_dlopen=no
1691 |   lt_cv_dlopen_libs=
1695 |     lt_cv_dlopen="load_add_on"
1696 |     lt_cv_dlopen_libs=
1697 |     lt_cv_dlopen_self=yes
1701 |     lt_cv_dlopen="LoadLibrary"
1702 |     lt_cv_dlopen_libs=
1706 |     lt_cv_dlopen="dlopen"
1707 |     lt_cv_dlopen_libs=
1712 |     AC_CHECK_LIB([dl], [dlopen],
1713 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1714 |     lt_cv_dlopen="dyld"
1715 |     lt_cv_dlopen_libs=
1716 |     lt_cv_dlopen_self=yes
1722 | 	  [lt_cv_dlopen="shl_load"],
1724 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
1725 | 	[AC_CHECK_FUNC([dlopen],
1726 | 	      [lt_cv_dlopen="dlopen"],
1727 | 	  [AC_CHECK_LIB([dl], [dlopen],
1728 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1729 | 	    [AC_CHECK_LIB([svld], [dlopen],
1730 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1732 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
1741 |   if test "x$lt_cv_dlopen" != xno; then
1742 |     enable_dlopen=yes
1744 |     enable_dlopen=no
1747 |   case $lt_cv_dlopen in
1748 |   dlopen)
1756 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1758 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1759 | 	  lt_cv_dlopen_self, [dnl
1760 | 	  _LT_AC_TRY_DLOPEN_SELF(
1761 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1762 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1765 |     if test "x$lt_cv_dlopen_self" = xyes; then
1767 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1768 |     	  lt_cv_dlopen_self_static, [dnl
1769 | 	  _LT_AC_TRY_DLOPEN_SELF(
1770 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1771 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1781 |   case $lt_cv_dlopen_self in
1782 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1783 |   *) enable_dlopen_self=unknown ;;
1786 |   case $lt_cv_dlopen_self_static in
1787 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1788 |   *) enable_dlopen_self_static=unknown ;;
1791 | ])# AC_LIBTOOL_DLOPEN_SELF
2621 | # AC_LIBTOOL_DLOPEN
2623 | # enable checks for dlopen support
2624 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2626 | ])# AC_LIBTOOL_DLOPEN
3421 | AC_LIBTOOL_DLOPEN_SELF($1)
4371 | AC_LIBTOOL_DLOPEN_SELF($1)
4666 | AC_LIBTOOL_DLOPEN_SELF($1)
4971 | # Whether dlopen is supported.
4972 | dlopen_support=$enable_dlopen
4974 | # Whether dlopen of programs is supported.
4975 | dlopen_self=$enable_dlopen_self
4977 | # Whether dlopen of statically linked programs is supported.
4978 | dlopen_self_static=$enable_dlopen_self_static
4986 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```