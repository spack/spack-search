---
name: "libxml2"
layout: package
next_package: lis
previous_package: glib
languages: ['cpp', 'bash']
---
## 2.7.8
6 / 6220 files match

 - [config.h.in](#confighin)
 - [xmlmodule.c](#xmlmodulec)
 - [ltmain.sh](#ltmainsh)
 - [configure.in](#configurein)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)

### config.h.in

```

{% raw %}
42 | /* Have dlopen based dso */
43 | #undef HAVE_DLOPEN
{% endraw %}

```
### xmlmodule.c

```cpp

{% raw %}
192 | #if defined(HAVE_DLOPEN) && !defined(_WIN32)
211 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
243 | #else /* ! HAVE_DLOPEN */
288 | #endif /* ! HAVE_DLOPEN */
{% endraw %}

```
### ltmain.sh

```bash

{% raw %}
885 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
946 |       -dlopen=*|--mode=*|--tag=*)
1036 |   # Only execute mode is allowed to have -dlopen flags.
1038 |     func_error "unrecognized option \`-dlopen'"
1672 |   -dlopen FILE      add the directory containing FILE to the library path
1674 | This mode sets the library path environment variable according to \`-dlopen'
1729 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1738 |   -module           build a library that can dlopened
1844 |     # Handle -dlopen flags immediately.
1861 | 	# Skip this library if it cannot be dlopened.
1888 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4436 | 	    dlopen_self=$dlopen_self_static
4442 | 	    dlopen_self=$dlopen_self_static
4448 | 	    dlopen_self=$dlopen_self_static
4506 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4590 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4752 |       -dlopen)
5140 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5207 | 	  # This library was specified with -dlopen.
5322 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5333 | 	passes="conv scan dlopen dlpreopen link"
5359 | 	dlopen) libs="$dlfiles" ;;
5386 |       if test "$pass" = dlopen; then
5598 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5599 | 	      # If there is no dlopen support or we're linking statically,
5629 | 	dlopen=
5659 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5699 | 	# This library was specified with -dlopen.
5700 | 	if test "$pass" = dlopen; then
5702 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5705 | 	     test "$dlopen_support" != yes ||
5707 | 	    # If there is no dlname, no dlopen support or we're linking
5716 | 	fi # $pass = dlopen
5774 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5900 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5901 | 	  dlopenmodule=""
5904 | 	      dlopenmodule="$dlpremoduletest"
5908 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6005 | 		    # if the lib is a (non-dlopened) module then we can not
6009 | 		      if test "X$dlopenmodule" != "X$lib"; then
6161 | 	      echo "*** a static module, that should work as long as the dlopening application"
6162 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
6298 |       if test "$pass" != dlopen; then
6397 | 	func_warning "\`-dlopen' is ignored for archives"
6464 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7126 | 	    echo "*** a static module, that should work as long as the dlopening"
7127 | 	    echo "*** application is linked with the -dlopen flag."
7145 | 	    echo "*** or is declared to -dlopen it."
7716 | 	func_warning "\`-dlopen' is ignored for objects"
7831 |         && test "$dlopen_support" = unknown \
7832 | 	&& test "$dlopen_self" = unknown \
7833 | 	&& test "$dlopen_self_static" = unknown && \
7834 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8473 | # The name that we can dlopen(3).
8502 | # Files to dlopen/dlpreopen
8503 | dlopen='$dlfiles'
{% endraw %}

```
### configure.in

```

{% raw %}
796 |   AC_CHECK_LIB(cygwin, dlopen, [
799 |     AC_DEFINE([HAVE_DLOPEN], [], [Have dlopen based dso])
811 |       AC_CHECK_FUNC(dlopen, libxml_have_dlopen=yes, [
812 |         AC_CHECK_LIB(dl, dlopen, [
814 |           libxml_have_dlopen=yes])])])])
822 |   if test "${libxml_have_dlopen}" = "yes"; then
833 |     AC_DEFINE([HAVE_DLOPEN], [], [Have dlopen based dso])
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1605 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1608 | m4_defun([_LT_TRY_DLOPEN_SELF],
1666 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1699 | ])# _LT_TRY_DLOPEN_SELF
1702 | # LT_SYS_DLOPEN_SELF
1704 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1706 | if test "x$enable_dlopen" != xyes; then
1707 |   enable_dlopen=unknown
1708 |   enable_dlopen_self=unknown
1709 |   enable_dlopen_self_static=unknown
1711 |   lt_cv_dlopen=no
1712 |   lt_cv_dlopen_libs=
1716 |     lt_cv_dlopen="load_add_on"
1717 |     lt_cv_dlopen_libs=
1718 |     lt_cv_dlopen_self=yes
1722 |     lt_cv_dlopen="LoadLibrary"
1723 |     lt_cv_dlopen_libs=
1727 |     lt_cv_dlopen="dlopen"
1728 |     lt_cv_dlopen_libs=
1733 |     AC_CHECK_LIB([dl], [dlopen],
1734 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1735 |     lt_cv_dlopen="dyld"
1736 |     lt_cv_dlopen_libs=
1737 |     lt_cv_dlopen_self=yes
1743 | 	  [lt_cv_dlopen="shl_load"],
1745 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1746 | 	[AC_CHECK_FUNC([dlopen],
1747 | 	      [lt_cv_dlopen="dlopen"],
1748 | 	  [AC_CHECK_LIB([dl], [dlopen],
1749 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1750 | 	    [AC_CHECK_LIB([svld], [dlopen],
1751 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1753 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1762 |   if test "x$lt_cv_dlopen" != xno; then
1763 |     enable_dlopen=yes
1765 |     enable_dlopen=no
1768 |   case $lt_cv_dlopen in
1769 |   dlopen)
1777 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1779 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1780 | 	  lt_cv_dlopen_self, [dnl
1781 | 	  _LT_TRY_DLOPEN_SELF(
1782 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1783 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1786 |     if test "x$lt_cv_dlopen_self" = xyes; then
1788 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1789 | 	  lt_cv_dlopen_self_static, [dnl
1790 | 	  _LT_TRY_DLOPEN_SELF(
1791 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1792 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1802 |   case $lt_cv_dlopen_self in
1803 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1804 |   *) enable_dlopen_self=unknown ;;
1807 |   case $lt_cv_dlopen_self_static in
1808 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1809 |   *) enable_dlopen_self_static=unknown ;;
1812 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1813 | 	 [Whether dlopen is supported])
1814 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1815 | 	 [Whether dlopen of programs is supported])
1816 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1817 | 	 [Whether dlopen of statically linked programs is supported])
1818 | ])# LT_SYS_DLOPEN_SELF
1821 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1823 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5265 |     [Compiler flag to allow reflexive dlopens])
5381 |   LT_SYS_DLOPEN_SELF
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