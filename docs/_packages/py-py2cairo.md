---
name: "py-py2cairo"
layout: package
next_package: xdm
previous_package: grafana
languages: ['bash']
---
## 1.10.0
4 / 97 files match

 - [config.status](#configstatus)
 - [config.lt](#configlt)
 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### config.status

```

{% raw %}
674 | enable_dlopen='unknown'
675 | enable_dlopen_self='unknown'
676 | enable_dlopen_self_static='unknown'
1679 | # Whether dlopen is supported.
1680 | dlopen_support=$enable_dlopen
1682 | # Whether dlopen of programs is supported.
1683 | dlopen_self=$enable_dlopen_self
1685 | # Whether dlopen of statically linked programs is supported.
1686 | dlopen_self_static=$enable_dlopen_self_static
1730 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### config.lt

```

{% raw %}
564 | enable_dlopen='unknown'
565 | enable_dlopen_self='unknown'
566 | enable_dlopen_self_static='unknown'
884 | # Whether dlopen is supported.
885 | dlopen_support=$enable_dlopen
887 | # Whether dlopen of programs is supported.
888 | dlopen_self=$enable_dlopen_self
890 | # Whether dlopen of statically linked programs is supported.
891 | dlopen_self_static=$enable_dlopen_self_static
935 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
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
5059 |       if test "$pass" = dlopen; then
5271 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5272 | 	      # If there is no dlopen support or we're linking statically,
5302 | 	dlopen=
5332 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5372 | 	# This library was specified with -dlopen.
5373 | 	if test "$pass" = dlopen; then
5375 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5378 | 	     test "$dlopen_support" != yes ||
5380 | 	    # If there is no dlname, no dlopen support or we're linking
5389 | 	fi # $pass = dlopen
5447 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5573 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5574 | 	  dlopenmodule=""
5577 | 	      dlopenmodule="$dlpremoduletest"
5581 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5678 | 		    # if the lib is a (non-dlopened) module then we can not
5682 | 		      if test "X$dlopenmodule" != "X$lib"; then
5834 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5835 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5970 |       if test "$pass" != dlopen; then
6069 | 	func_warning "\`-dlopen' is ignored for archives"
6136 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6798 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6799 | 	    $ECHO "*** application is linked with the -dlopen flag."
6817 | 	    $ECHO "*** or is declared to -dlopen it."
7384 | 	func_warning "\`-dlopen' is ignored for objects"
7499 |         && test "$dlopen_support" = unknown \
7500 | 	&& test "$dlopen_self" = unknown \
7501 | 	&& test "$dlopen_self_static" = unknown && \
7502 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8134 | # The name that we can dlopen(3).
8163 | # Files to dlopen/dlpreopen
8164 | dlopen='$dlfiles'
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1620 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1623 | m4_defun([_LT_TRY_DLOPEN_SELF],
1681 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1714 | ])# _LT_TRY_DLOPEN_SELF
1717 | # LT_SYS_DLOPEN_SELF
1719 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1721 | if test "x$enable_dlopen" != xyes; then
1722 |   enable_dlopen=unknown
1723 |   enable_dlopen_self=unknown
1724 |   enable_dlopen_self_static=unknown
1726 |   lt_cv_dlopen=no
1727 |   lt_cv_dlopen_libs=
1731 |     lt_cv_dlopen="load_add_on"
1732 |     lt_cv_dlopen_libs=
1733 |     lt_cv_dlopen_self=yes
1737 |     lt_cv_dlopen="LoadLibrary"
1738 |     lt_cv_dlopen_libs=
1742 |     lt_cv_dlopen="dlopen"
1743 |     lt_cv_dlopen_libs=
1748 |     AC_CHECK_LIB([dl], [dlopen],
1749 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1750 |     lt_cv_dlopen="dyld"
1751 |     lt_cv_dlopen_libs=
1752 |     lt_cv_dlopen_self=yes
1758 | 	  [lt_cv_dlopen="shl_load"],
1760 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1761 | 	[AC_CHECK_FUNC([dlopen],
1762 | 	      [lt_cv_dlopen="dlopen"],
1763 | 	  [AC_CHECK_LIB([dl], [dlopen],
1764 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1765 | 	    [AC_CHECK_LIB([svld], [dlopen],
1766 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1768 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1777 |   if test "x$lt_cv_dlopen" != xno; then
1778 |     enable_dlopen=yes
1780 |     enable_dlopen=no
1783 |   case $lt_cv_dlopen in
1784 |   dlopen)
1792 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1794 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1795 | 	  lt_cv_dlopen_self, [dnl
1796 | 	  _LT_TRY_DLOPEN_SELF(
1797 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1798 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1801 |     if test "x$lt_cv_dlopen_self" = xyes; then
1803 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1804 | 	  lt_cv_dlopen_self_static, [dnl
1805 | 	  _LT_TRY_DLOPEN_SELF(
1806 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1807 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1817 |   case $lt_cv_dlopen_self in
1818 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1819 |   *) enable_dlopen_self=unknown ;;
1822 |   case $lt_cv_dlopen_self_static in
1823 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1824 |   *) enable_dlopen_self_static=unknown ;;
1827 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1828 | 	 [Whether dlopen is supported])
1829 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1830 | 	 [Whether dlopen of programs is supported])
1831 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1832 | 	 [Whether dlopen of statically linked programs is supported])
1833 | ])# LT_SYS_DLOPEN_SELF
1836 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1838 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5280 |     [Compiler flag to allow reflexive dlopens])
5392 |   LT_SYS_DLOPEN_SELF
7517 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7549 | # dlopen
7551 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7554 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7555 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7558 | put the `dlopen' option into LT_INIT's first parameter.])
7562 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8008 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```