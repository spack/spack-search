---
name: "lesstif"
layout: package
next_package: imp
previous_package: libiberty
languages: ['bash']
---
## 0.95.2
3 / 1657 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)
 - [test/aclocal.m4](#testaclocalm4)

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
5973 |       if test "$pass" != dlopen; then
6072 | 	func_warning "\`-dlopen' is ignored for archives"
6139 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6804 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6805 | 	    $ECHO "*** application is linked with the -dlopen flag."
6823 | 	    $ECHO "*** or is declared to -dlopen it."
7390 | 	func_warning "\`-dlopen' is ignored for objects"
7505 |         && test "$dlopen_support" = unknown \
7506 | 	&& test "$dlopen_self" = unknown \
7507 | 	&& test "$dlopen_self_static" = unknown && \
7508 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8140 | # The name that we can dlopen(3).
8169 | # Files to dlopen/dlpreopen
8170 | dlopen='$dlfiles'
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1641 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1644 | m4_defun([_LT_TRY_DLOPEN_SELF],
1696 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1725 | ])# _LT_TRY_DLOPEN_SELF
1728 | # LT_SYS_DLOPEN_SELF
1730 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1732 | if test "x$enable_dlopen" != xyes; then
1733 |   enable_dlopen=unknown
1734 |   enable_dlopen_self=unknown
1735 |   enable_dlopen_self_static=unknown
1737 |   lt_cv_dlopen=no
1738 |   lt_cv_dlopen_libs=
1742 |     lt_cv_dlopen="load_add_on"
1743 |     lt_cv_dlopen_libs=
1744 |     lt_cv_dlopen_self=yes
1748 |     lt_cv_dlopen="LoadLibrary"
1749 |     lt_cv_dlopen_libs=
1753 |     lt_cv_dlopen="dlopen"
1754 |     lt_cv_dlopen_libs=
1759 |     AC_CHECK_LIB([dl], [dlopen],
1760 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1761 |     lt_cv_dlopen="dyld"
1762 |     lt_cv_dlopen_libs=
1763 |     lt_cv_dlopen_self=yes
1769 | 	  [lt_cv_dlopen="shl_load"],
1771 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1772 | 	[AC_CHECK_FUNC([dlopen],
1773 | 	      [lt_cv_dlopen="dlopen"],
1774 | 	  [AC_CHECK_LIB([dl], [dlopen],
1775 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1776 | 	    [AC_CHECK_LIB([svld], [dlopen],
1777 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1779 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1788 |   if test "x$lt_cv_dlopen" != xno; then
1789 |     enable_dlopen=yes
1791 |     enable_dlopen=no
1794 |   case $lt_cv_dlopen in
1795 |   dlopen)
1803 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1805 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1806 | 	  lt_cv_dlopen_self, [dnl
1807 | 	  _LT_TRY_DLOPEN_SELF(
1808 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1809 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1812 |     if test "x$lt_cv_dlopen_self" = xyes; then
1814 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1815 | 	  lt_cv_dlopen_self_static, [dnl
1816 | 	  _LT_TRY_DLOPEN_SELF(
1817 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1818 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1828 |   case $lt_cv_dlopen_self in
1829 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1830 |   *) enable_dlopen_self=unknown ;;
1833 |   case $lt_cv_dlopen_self_static in
1834 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1835 |   *) enable_dlopen_self_static=unknown ;;
1838 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1839 | 	 [Whether dlopen is supported])
1840 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1841 | 	 [Whether dlopen of programs is supported])
1842 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1843 | 	 [Whether dlopen of statically linked programs is supported])
1844 | ])# LT_SYS_DLOPEN_SELF
1847 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1849 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5178 |     [Compiler flag to allow reflexive dlopens])
5290 |   LT_SYS_DLOPEN_SELF
7440 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7472 | # dlopen
7474 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7477 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7478 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7481 | put the `dlopen' option into LT_INIT's first parameter.])
7485 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
7931 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### test/aclocal.m4

```

{% raw %}
1641 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1644 | m4_defun([_LT_TRY_DLOPEN_SELF],
1696 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1725 | ])# _LT_TRY_DLOPEN_SELF
1728 | # LT_SYS_DLOPEN_SELF
1730 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1732 | if test "x$enable_dlopen" != xyes; then
1733 |   enable_dlopen=unknown
1734 |   enable_dlopen_self=unknown
1735 |   enable_dlopen_self_static=unknown
1737 |   lt_cv_dlopen=no
1738 |   lt_cv_dlopen_libs=
1742 |     lt_cv_dlopen="load_add_on"
1743 |     lt_cv_dlopen_libs=
1744 |     lt_cv_dlopen_self=yes
1748 |     lt_cv_dlopen="LoadLibrary"
1749 |     lt_cv_dlopen_libs=
1753 |     lt_cv_dlopen="dlopen"
1754 |     lt_cv_dlopen_libs=
1759 |     AC_CHECK_LIB([dl], [dlopen],
1760 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1761 |     lt_cv_dlopen="dyld"
1762 |     lt_cv_dlopen_libs=
1763 |     lt_cv_dlopen_self=yes
1769 | 	  [lt_cv_dlopen="shl_load"],
1771 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1772 | 	[AC_CHECK_FUNC([dlopen],
1773 | 	      [lt_cv_dlopen="dlopen"],
1774 | 	  [AC_CHECK_LIB([dl], [dlopen],
1775 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1776 | 	    [AC_CHECK_LIB([svld], [dlopen],
1777 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1779 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1788 |   if test "x$lt_cv_dlopen" != xno; then
1789 |     enable_dlopen=yes
1791 |     enable_dlopen=no
1794 |   case $lt_cv_dlopen in
1795 |   dlopen)
1803 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1805 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1806 | 	  lt_cv_dlopen_self, [dnl
1807 | 	  _LT_TRY_DLOPEN_SELF(
1808 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1809 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1812 |     if test "x$lt_cv_dlopen_self" = xyes; then
1814 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1815 | 	  lt_cv_dlopen_self_static, [dnl
1816 | 	  _LT_TRY_DLOPEN_SELF(
1817 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1818 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1828 |   case $lt_cv_dlopen_self in
1829 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1830 |   *) enable_dlopen_self=unknown ;;
1833 |   case $lt_cv_dlopen_self_static in
1834 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1835 |   *) enable_dlopen_self_static=unknown ;;
1838 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1839 | 	 [Whether dlopen is supported])
1840 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1841 | 	 [Whether dlopen of programs is supported])
1842 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1843 | 	 [Whether dlopen of statically linked programs is supported])
1844 | ])# LT_SYS_DLOPEN_SELF
1847 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1849 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5178 |     [Compiler flag to allow reflexive dlopens])
5290 |   LT_SYS_DLOPEN_SELF
7440 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7472 | # dlopen
7474 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7477 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7478 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7481 | put the `dlopen' option into LT_INIT's first parameter.])
7485 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
7931 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```