---
name: "zfs"
layout: package
next_package: libpmemobj-cpp
previous_package: keepalived
languages: ['python', 'cpp', 'bash']
---
## 0.8.2
6 / 3305 files match

 - [config/libtool.m4](#configlibtoolm4)
 - [config/ltoptions.m4](#configltoptionsm4)
 - [config/ltmain.sh](#configltmainsh)
 - [config/lib-link.m4](#configlib-linkm4)
 - [lib/libzpool/util.c](#liblibzpoolutilc)
 - [contrib/pyzfs/libzfs_core/bindings/__init__.py](#contribpyzfslibzfs_corebindings__init__py)

### config/libtool.m4

```

{% raw %}
1634 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1637 | m4_defun([_LT_TRY_DLOPEN_SELF],
1689 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1718 | ])# _LT_TRY_DLOPEN_SELF
1721 | # LT_SYS_DLOPEN_SELF
1723 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1725 | if test "x$enable_dlopen" != xyes; then
1726 |   enable_dlopen=unknown
1727 |   enable_dlopen_self=unknown
1728 |   enable_dlopen_self_static=unknown
1730 |   lt_cv_dlopen=no
1731 |   lt_cv_dlopen_libs=
1735 |     lt_cv_dlopen="load_add_on"
1736 |     lt_cv_dlopen_libs=
1737 |     lt_cv_dlopen_self=yes
1741 |     lt_cv_dlopen="LoadLibrary"
1742 |     lt_cv_dlopen_libs=
1746 |     lt_cv_dlopen="dlopen"
1747 |     lt_cv_dlopen_libs=
1752 |     AC_CHECK_LIB([dl], [dlopen],
1753 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1754 |     lt_cv_dlopen="dyld"
1755 |     lt_cv_dlopen_libs=
1756 |     lt_cv_dlopen_self=yes
1762 | 	  [lt_cv_dlopen="shl_load"],
1764 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1765 | 	[AC_CHECK_FUNC([dlopen],
1766 | 	      [lt_cv_dlopen="dlopen"],
1767 | 	  [AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1769 | 	    [AC_CHECK_LIB([svld], [dlopen],
1770 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1772 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1781 |   if test "x$lt_cv_dlopen" != xno; then
1782 |     enable_dlopen=yes
1784 |     enable_dlopen=no
1787 |   case $lt_cv_dlopen in
1788 |   dlopen)
1796 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1798 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1799 | 	  lt_cv_dlopen_self, [dnl
1800 | 	  _LT_TRY_DLOPEN_SELF(
1801 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1802 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1805 |     if test "x$lt_cv_dlopen_self" = xyes; then
1807 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1808 | 	  lt_cv_dlopen_self_static, [dnl
1809 | 	  _LT_TRY_DLOPEN_SELF(
1810 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1811 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1821 |   case $lt_cv_dlopen_self in
1822 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1823 |   *) enable_dlopen_self=unknown ;;
1826 |   case $lt_cv_dlopen_self_static in
1827 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1828 |   *) enable_dlopen_self_static=unknown ;;
1831 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1832 | 	 [Whether dlopen is supported])
1833 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1834 | 	 [Whether dlopen of programs is supported])
1835 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1836 | 	 [Whether dlopen of statically linked programs is supported])
1837 | ])# LT_SYS_DLOPEN_SELF
1840 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1842 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5158 |     [Compiler flag to allow reflexive dlopens])
5274 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### config/ltoptions.m4

```

{% raw %}
69 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
104 | # dlopen
106 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
109 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
110 | [_LT_SET_OPTION([LT_INIT], [dlopen])
113 | put the `dlopen' option into LT_INIT's first parameter.])
117 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### config/ltmain.sh

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
### config/lib-link.m4

```

{% raw %}
516 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### lib/libzpool/util.c

```cpp

{% raw %}
184 | 	zpoolhdl = dlopen("libzpool.so", RTLD_LAZY);
{% endraw %}

```
### contrib/pyzfs/libzfs_core/bindings/__init__.py

```python

{% raw %}
42 |                         self._lib = self._ffi.dlopen(self._libname)
{% endraw %}

```