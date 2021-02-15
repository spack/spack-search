---
name: "compiz"
layout: package
next_package: log4cxx
previous_package: regcm
languages: ['cpp', 'bash']
---
## 0.7.8
4 / 222 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)
 - [src/screen.c](#srcscreenc)
 - [src/plugin.c](#srcpluginc)

### ltmain.sh

```bash

{% raw %}
551 |   -dlopen)
552 |     prevopt="-dlopen"
636 |   # Only execute mode is allowed to have -dlopen flags.
638 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1177 | 	    dlopen_self=$dlopen_self_static
1183 | 	    dlopen_self=$dlopen_self_static
1189 | 	    dlopen_self=$dlopen_self_static
1246 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1338 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1495 |       -dlopen)
1883 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1956 | 	  # This library was specified with -dlopen.
2097 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2109 | 	passes="conv scan dlopen dlpreopen link"
2122 | 	dlopen) libs="$dlfiles" ;;
2127 |       if test "$pass" = dlopen; then
2306 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2307 | 	      # If there is no dlopen support or we're linking statically,
2340 | 	dlopen=
2361 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2404 | 	# This library was specified with -dlopen.
2405 | 	if test "$pass" = dlopen; then
2407 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2411 | 	     test "$dlopen_support" != yes ||
2413 | 	    # If there is no dlname, no dlopen support or we're linking
2422 | 	fi # $pass = dlopen
2475 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2852 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2853 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
3004 |       if test "$pass" != dlopen; then
3105 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3172 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3812 | 	    $echo "*** a static module, that should work as long as the dlopening"
3813 | 	    $echo "*** application is linked with the -dlopen flag."
3831 | 	    $echo "*** or is declared to -dlopen it."
4244 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4378 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4379 | 	   test "$dlopen_self_static" = unknown; then
4380 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5732 | # The name that we can dlopen(3).
5755 | # Files to dlopen/dlpreopen
5756 | dlopen='$dlfiles'
6371 |     # Handle -dlopen flags immediately.
6400 | 	# Skip this library if it cannot be dlopened.
6427 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6787 |   -dlopen FILE      add the directory containing FILE to the library path
6789 | This mode sets the library path environment variable according to \`-dlopen'
6838 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6847 |   -module           build a library that can dlopened
{% endraw %}

```
### aclocal.m4

```

{% raw %}
898 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
1535 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1538 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
1594 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1623 | ])# _LT_AC_TRY_DLOPEN_SELF
1626 | # AC_LIBTOOL_DLOPEN_SELF
1628 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1630 | if test "x$enable_dlopen" != xyes; then
1631 |   enable_dlopen=unknown
1632 |   enable_dlopen_self=unknown
1633 |   enable_dlopen_self_static=unknown
1635 |   lt_cv_dlopen=no
1636 |   lt_cv_dlopen_libs=
1640 |     lt_cv_dlopen="load_add_on"
1641 |     lt_cv_dlopen_libs=
1642 |     lt_cv_dlopen_self=yes
1646 |     lt_cv_dlopen="LoadLibrary"
1647 |     lt_cv_dlopen_libs=
1651 |     lt_cv_dlopen="dlopen"
1652 |     lt_cv_dlopen_libs=
1657 |     AC_CHECK_LIB([dl], [dlopen],
1658 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1659 |     lt_cv_dlopen="dyld"
1660 |     lt_cv_dlopen_libs=
1661 |     lt_cv_dlopen_self=yes
1667 | 	  [lt_cv_dlopen="shl_load"],
1669 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
1670 | 	[AC_CHECK_FUNC([dlopen],
1671 | 	      [lt_cv_dlopen="dlopen"],
1672 | 	  [AC_CHECK_LIB([dl], [dlopen],
1673 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1674 | 	    [AC_CHECK_LIB([svld], [dlopen],
1675 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1677 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
1686 |   if test "x$lt_cv_dlopen" != xno; then
1687 |     enable_dlopen=yes
1689 |     enable_dlopen=no
1692 |   case $lt_cv_dlopen in
1693 |   dlopen)
1701 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1703 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1704 | 	  lt_cv_dlopen_self, [dnl
1705 | 	  _LT_AC_TRY_DLOPEN_SELF(
1706 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1707 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1710 |     if test "x$lt_cv_dlopen_self" = xyes; then
1712 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1713 |     	  lt_cv_dlopen_self_static, [dnl
1714 | 	  _LT_AC_TRY_DLOPEN_SELF(
1715 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1716 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1726 |   case $lt_cv_dlopen_self in
1727 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1728 |   *) enable_dlopen_self=unknown ;;
1731 |   case $lt_cv_dlopen_self_static in
1732 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1733 |   *) enable_dlopen_self_static=unknown ;;
1736 | ])# AC_LIBTOOL_DLOPEN_SELF
2629 | # AC_LIBTOOL_DLOPEN
2631 | # enable checks for dlopen support
2632 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2634 | ])# AC_LIBTOOL_DLOPEN
3432 | AC_LIBTOOL_DLOPEN_SELF
5170 | # Whether dlopen is supported.
5171 | dlopen_support=$enable_dlopen
5173 | # Whether dlopen of programs is supported.
5174 | dlopen_self=$enable_dlopen_self
5176 | # Whether dlopen of statically linked programs is supported.
5177 | dlopen_self_static=$enable_dlopen_self_static
5185 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/screen.c

```cpp

{% raw %}
942 | 	    dlhand = dlopen (NULL, RTLD_LAZY);
{% endraw %}

```
### src/plugin.c

```cpp

{% raw %}
159 |     dlhand = dlopen (file, RTLD_LAZY);
{% endraw %}

```