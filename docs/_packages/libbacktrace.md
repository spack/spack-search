---
name: "libbacktrace"
layout: package
next_package: jemalloc
previous_package: libvdwxc
languages: ['cpp', 'bash']
---
## 2020-02-19
7 / 79 files match

 - [libtool.m4](#libtoolm4)
 - [ltoptions.m4](#ltoptionsm4)
 - [dwarf.c](#dwarfc)
 - [ltmain.sh](#ltmainsh)
 - [xcoff.c](#xcoffc)
 - [config/libtool.m4](#configlibtoolm4)
 - [config/ltoptions.m4](#configltoptionsm4)

### libtool.m4

```

{% raw %}
1614 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1617 | m4_defun([_LT_TRY_DLOPEN_SELF],
1675 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1708 | ])# _LT_TRY_DLOPEN_SELF
1711 | # LT_SYS_DLOPEN_SELF
1713 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1715 | if test "x$enable_dlopen" != xyes; then
1716 |   enable_dlopen=unknown
1717 |   enable_dlopen_self=unknown
1718 |   enable_dlopen_self_static=unknown
1720 |   lt_cv_dlopen=no
1721 |   lt_cv_dlopen_libs=
1725 |     lt_cv_dlopen="load_add_on"
1726 |     lt_cv_dlopen_libs=
1727 |     lt_cv_dlopen_self=yes
1731 |     lt_cv_dlopen="LoadLibrary"
1732 |     lt_cv_dlopen_libs=
1736 |     lt_cv_dlopen="dlopen"
1737 |     lt_cv_dlopen_libs=
1742 |     AC_CHECK_LIB([dl], [dlopen],
1743 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1744 |     lt_cv_dlopen="dyld"
1745 |     lt_cv_dlopen_libs=
1746 |     lt_cv_dlopen_self=yes
1752 | 	  [lt_cv_dlopen="shl_load"],
1754 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1755 | 	[AC_CHECK_FUNC([dlopen],
1756 | 	      [lt_cv_dlopen="dlopen"],
1757 | 	  [AC_CHECK_LIB([dl], [dlopen],
1758 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1759 | 	    [AC_CHECK_LIB([svld], [dlopen],
1760 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1762 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1771 |   if test "x$lt_cv_dlopen" != xno; then
1772 |     enable_dlopen=yes
1774 |     enable_dlopen=no
1777 |   case $lt_cv_dlopen in
1778 |   dlopen)
1786 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1788 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1789 | 	  lt_cv_dlopen_self, [dnl
1790 | 	  _LT_TRY_DLOPEN_SELF(
1791 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1792 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1795 |     if test "x$lt_cv_dlopen_self" = xyes; then
1797 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1798 | 	  lt_cv_dlopen_self_static, [dnl
1799 | 	  _LT_TRY_DLOPEN_SELF(
1800 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1801 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1811 |   case $lt_cv_dlopen_self in
1812 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1813 |   *) enable_dlopen_self=unknown ;;
1816 |   case $lt_cv_dlopen_self_static in
1817 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1818 |   *) enable_dlopen_self_static=unknown ;;
1821 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1822 | 	 [Whether dlopen is supported])
1823 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1824 | 	 [Whether dlopen of programs is supported])
1825 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1826 | 	 [Whether dlopen of statically linked programs is supported])
1827 | ])# LT_SYS_DLOPEN_SELF
1830 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1832 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5268 |     [Compiler flag to allow reflexive dlopens])
5384 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### ltoptions.m4

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
### dwarf.c

```cpp

{% raw %}
4155 |   /* FIXME: See if any libraries have been dlopen'ed.  */
{% endraw %}

```
### ltmain.sh

```bash

{% raw %}
895 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
957 |       -dlopen=*|--mode=*|--tag=*)
1047 |   # Only execute mode is allowed to have -dlopen flags.
1049 |     func_error "unrecognized option \`-dlopen'"
1683 |   -dlopen FILE      add the directory containing FILE to the library path
1685 | This mode sets the library path environment variable according to \`-dlopen'
1740 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1749 |   -module           build a library that can dlopened
1855 |     # Handle -dlopen flags immediately.
1872 | 	# Skip this library if it cannot be dlopened.
1899 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4322 | 	    dlopen_self=$dlopen_self_static
4328 | 	    dlopen_self=$dlopen_self_static
4334 | 	    dlopen_self=$dlopen_self_static
4392 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4476 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4638 |       -dlopen)
5029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5096 | 	  # This library was specified with -dlopen.
5211 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5222 | 	passes="conv scan dlopen dlpreopen link"
5248 | 	dlopen) libs="$dlfiles" ;;
5275 |       if test "$pass" = dlopen; then
5487 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5488 | 	      # If there is no dlopen support or we're linking statically,
5518 | 	dlopen=
5548 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5588 | 	# This library was specified with -dlopen.
5589 | 	if test "$pass" = dlopen; then
5591 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5594 | 	     test "$dlopen_support" != yes ||
5596 | 	    # If there is no dlname, no dlopen support or we're linking
5605 | 	fi # $pass = dlopen
5663 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5789 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5790 | 	  dlopenmodule=""
5793 | 	      dlopenmodule="$dlpremoduletest"
5797 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5894 | 		    # if the lib is a (non-dlopened) module then we can not
5898 | 		      if test "X$dlopenmodule" != "X$lib"; then
6050 | 	      echo "*** a static module, that should work as long as the dlopening application"
6051 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
6187 |       if test "$pass" != dlopen; then
6286 | 	func_warning "\`-dlopen' is ignored for archives"
6353 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7015 | 	    echo "*** a static module, that should work as long as the dlopening"
7016 | 	    echo "*** application is linked with the -dlopen flag."
7034 | 	    echo "*** or is declared to -dlopen it."
7607 | 	func_warning "\`-dlopen' is ignored for objects"
7722 |         && test "$dlopen_support" = unknown \
7723 | 	&& test "$dlopen_self" = unknown \
7724 | 	&& test "$dlopen_self_static" = unknown && \
7725 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8364 | # The name that we can dlopen(3).
8393 | # Files to dlopen/dlpreopen
8394 | dlopen='$dlfiles'
{% endraw %}

```
### xcoff.c

```cpp

{% raw %}
854 |   /* FIXME: See if any libraries have been dlopen'ed.  */
{% endraw %}

```
### config/libtool.m4

```

{% raw %}
1614 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1617 | m4_defun([_LT_TRY_DLOPEN_SELF],
1675 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1708 | ])# _LT_TRY_DLOPEN_SELF
1711 | # LT_SYS_DLOPEN_SELF
1713 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1715 | if test "x$enable_dlopen" != xyes; then
1716 |   enable_dlopen=unknown
1717 |   enable_dlopen_self=unknown
1718 |   enable_dlopen_self_static=unknown
1720 |   lt_cv_dlopen=no
1721 |   lt_cv_dlopen_libs=
1725 |     lt_cv_dlopen="load_add_on"
1726 |     lt_cv_dlopen_libs=
1727 |     lt_cv_dlopen_self=yes
1731 |     lt_cv_dlopen="LoadLibrary"
1732 |     lt_cv_dlopen_libs=
1736 |     lt_cv_dlopen="dlopen"
1737 |     lt_cv_dlopen_libs=
1742 |     AC_CHECK_LIB([dl], [dlopen],
1743 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1744 |     lt_cv_dlopen="dyld"
1745 |     lt_cv_dlopen_libs=
1746 |     lt_cv_dlopen_self=yes
1752 | 	  [lt_cv_dlopen="shl_load"],
1754 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1755 | 	[AC_CHECK_FUNC([dlopen],
1756 | 	      [lt_cv_dlopen="dlopen"],
1757 | 	  [AC_CHECK_LIB([dl], [dlopen],
1758 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1759 | 	    [AC_CHECK_LIB([svld], [dlopen],
1760 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1762 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1771 |   if test "x$lt_cv_dlopen" != xno; then
1772 |     enable_dlopen=yes
1774 |     enable_dlopen=no
1777 |   case $lt_cv_dlopen in
1778 |   dlopen)
1786 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1788 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1789 | 	  lt_cv_dlopen_self, [dnl
1790 | 	  _LT_TRY_DLOPEN_SELF(
1791 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1792 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1795 |     if test "x$lt_cv_dlopen_self" = xyes; then
1797 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1798 | 	  lt_cv_dlopen_self_static, [dnl
1799 | 	  _LT_TRY_DLOPEN_SELF(
1800 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1801 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1811 |   case $lt_cv_dlopen_self in
1812 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1813 |   *) enable_dlopen_self=unknown ;;
1816 |   case $lt_cv_dlopen_self_static in
1817 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1818 |   *) enable_dlopen_self_static=unknown ;;
1821 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1822 | 	 [Whether dlopen is supported])
1823 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1824 | 	 [Whether dlopen of programs is supported])
1825 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1826 | 	 [Whether dlopen of statically linked programs is supported])
1827 | ])# LT_SYS_DLOPEN_SELF
1830 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1832 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5268 |     [Compiler flag to allow reflexive dlopens])
5384 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### config/ltoptions.m4

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