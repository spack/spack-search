---
name: "libsigcpp"
layout: package
next_package: py-healpy
previous_package: libusb
languages: ['bash']
---
## 2.0.3
2 / 1494 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
279 |   -dlopen)
280 |     prevopt="-dlopen"
352 |   # Only execute mode is allowed to have -dlopen flags.
354 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
892 | 	    dlopen_self=$dlopen_self_static
896 | 	    dlopen_self=$dlopen_self_static
953 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1040 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1180 |       -dlopen)
1520 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1588 | 	  # This library was specified with -dlopen.
1771 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1783 | 	passes="conv scan dlopen dlpreopen link"
1796 | 	dlopen) libs="$dlfiles" ;;
1801 |       if test "$pass" = dlopen; then
1954 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
1955 | 	      # If there is no dlopen support or we're linking statically,
1988 | 	dlopen=
2007 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2050 | 	# This library was specified with -dlopen.
2051 | 	if test "$pass" = dlopen; then
2053 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2056 | 	  if test -z "$dlname" || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2057 | 	    # If there is no dlname, no dlopen support or we're linking
2066 | 	fi # $pass = dlopen
2111 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2474 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2475 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2623 |       if test "$pass" != dlopen; then
2723 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
2790 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3417 | 	    $echo "*** a static module, that should work as long as the dlopening"
3418 | 	    $echo "*** application is linked with the -dlopen flag."
3436 | 	    $echo "*** or is declared to -dlopen it."
3834 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4018 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4019 | 	   test "$dlopen_self_static" = unknown; then
4020 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5124 | # The name that we can dlopen(3).
5147 | # Files to dlopen/dlpreopen
5148 | dlopen='$dlfiles'
5763 |     # Handle -dlopen flags immediately.
5792 | 	# Skip this library if it cannot be dlopened.
5817 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6166 |   -dlopen FILE      add the directory containing FILE to the library path
6168 | This mode sets the library path environment variable according to \`-dlopen'
6217 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6226 |   -module           build a library that can dlopened
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1048 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
1544 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1547 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
1603 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1630 | ])# _LT_AC_TRY_DLOPEN_SELF
1633 | # AC_LIBTOOL_DLOPEN_SELF
1635 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1637 | if test "x$enable_dlopen" != xyes; then
1638 |   enable_dlopen=unknown
1639 |   enable_dlopen_self=unknown
1640 |   enable_dlopen_self_static=unknown
1642 |   lt_cv_dlopen=no
1643 |   lt_cv_dlopen_libs=
1647 |     lt_cv_dlopen="load_add_on"
1648 |     lt_cv_dlopen_libs=
1649 |     lt_cv_dlopen_self=yes
1653 |     lt_cv_dlopen="LoadLibrary"
1654 |     lt_cv_dlopen_libs=
1658 |     lt_cv_dlopen="dlopen"
1659 |     lt_cv_dlopen_libs=
1664 |     AC_CHECK_LIB([dl], [dlopen],
1665 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1666 |     lt_cv_dlopen="dyld"
1667 |     lt_cv_dlopen_libs=
1668 |     lt_cv_dlopen_self=yes
1674 | 	  [lt_cv_dlopen="shl_load"],
1676 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
1677 | 	[AC_CHECK_FUNC([dlopen],
1678 | 	      [lt_cv_dlopen="dlopen"],
1679 | 	  [AC_CHECK_LIB([dl], [dlopen],
1680 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1681 | 	    [AC_CHECK_LIB([svld], [dlopen],
1682 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1684 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
1693 |   if test "x$lt_cv_dlopen" != xno; then
1694 |     enable_dlopen=yes
1696 |     enable_dlopen=no
1699 |   case $lt_cv_dlopen in
1700 |   dlopen)
1708 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1710 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1711 | 	  lt_cv_dlopen_self, [dnl
1712 | 	  _LT_AC_TRY_DLOPEN_SELF(
1713 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1714 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1717 |     if test "x$lt_cv_dlopen_self" = xyes; then
1719 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1720 |     	  lt_cv_dlopen_self_static, [dnl
1721 | 	  _LT_AC_TRY_DLOPEN_SELF(
1722 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1723 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1733 |   case $lt_cv_dlopen_self in
1734 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1735 |   *) enable_dlopen_self=unknown ;;
1738 |   case $lt_cv_dlopen_self_static in
1739 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1740 |   *) enable_dlopen_self_static=unknown ;;
1743 | ])# AC_LIBTOOL_DLOPEN_SELF
2531 | # AC_LIBTOOL_DLOPEN
2533 | # enable checks for dlopen support
2534 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2536 | ])# AC_LIBTOOL_DLOPEN
3348 | AC_LIBTOOL_DLOPEN_SELF($1)
4276 | AC_LIBTOOL_DLOPEN_SELF($1)
4570 | AC_LIBTOOL_DLOPEN_SELF($1)
4874 | # Whether dlopen is supported.
4875 | dlopen_support=$enable_dlopen
4877 | # Whether dlopen of programs is supported.
4878 | dlopen_self=$enable_dlopen_self
4880 | # Whether dlopen of statically linked programs is supported.
4881 | dlopen_self_static=$enable_dlopen_self_static
4889 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```