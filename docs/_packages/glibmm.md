---
name: "glibmm"
layout: package
next_package: ganglia
previous_package: minuit
languages: ['html', 'cpp', 'bash']
---
## 2.4.8
5 / 779 files match

 - [aclocal.m4](#aclocalm4)
 - [glib/src/module.hg](#glibsrcmodulehg)
 - [glib/glibmm/module.h](#glibglibmmmoduleh)
 - [scripts/ltmain.sh](#scriptsltmainsh)
 - [docs/reference/html/classGlib_1_1Module.html](#docsreferencehtmlclassglib_1_1modulehtml)

### aclocal.m4

```

{% raw %}
1082 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
1661 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1664 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
1720 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1747 | ])# _LT_AC_TRY_DLOPEN_SELF
1750 | # AC_LIBTOOL_DLOPEN_SELF
1752 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1754 | if test "x$enable_dlopen" != xyes; then
1755 |   enable_dlopen=unknown
1756 |   enable_dlopen_self=unknown
1757 |   enable_dlopen_self_static=unknown
1759 |   lt_cv_dlopen=no
1760 |   lt_cv_dlopen_libs=
1764 |     lt_cv_dlopen="load_add_on"
1765 |     lt_cv_dlopen_libs=
1766 |     lt_cv_dlopen_self=yes
1770 |     lt_cv_dlopen="LoadLibrary"
1771 |     lt_cv_dlopen_libs=
1775 |     lt_cv_dlopen="dlopen"
1776 |     lt_cv_dlopen_libs=
1781 |     AC_CHECK_LIB([dl], [dlopen],
1782 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1783 |     lt_cv_dlopen="dyld"
1784 |     lt_cv_dlopen_libs=
1785 |     lt_cv_dlopen_self=yes
1791 | 	  [lt_cv_dlopen="shl_load"],
1793 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
1794 | 	[AC_CHECK_FUNC([dlopen],
1795 | 	      [lt_cv_dlopen="dlopen"],
1796 | 	  [AC_CHECK_LIB([dl], [dlopen],
1797 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1798 | 	    [AC_CHECK_LIB([svld], [dlopen],
1799 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1801 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
1810 |   if test "x$lt_cv_dlopen" != xno; then
1811 |     enable_dlopen=yes
1813 |     enable_dlopen=no
1816 |   case $lt_cv_dlopen in
1817 |   dlopen)
1825 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1827 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1828 | 	  lt_cv_dlopen_self, [dnl
1829 | 	  _LT_AC_TRY_DLOPEN_SELF(
1830 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1831 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1834 |     if test "x$lt_cv_dlopen_self" = xyes; then
1836 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1837 |     	  lt_cv_dlopen_self_static, [dnl
1838 | 	  _LT_AC_TRY_DLOPEN_SELF(
1839 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1840 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1850 |   case $lt_cv_dlopen_self in
1851 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1852 |   *) enable_dlopen_self=unknown ;;
1855 |   case $lt_cv_dlopen_self_static in
1856 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1857 |   *) enable_dlopen_self_static=unknown ;;
1860 | ])# AC_LIBTOOL_DLOPEN_SELF
2696 | # AC_LIBTOOL_DLOPEN
2698 | # enable checks for dlopen support
2699 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2701 | ])# AC_LIBTOOL_DLOPEN
3509 | AC_LIBTOOL_DLOPEN_SELF($1)
4485 | AC_LIBTOOL_DLOPEN_SELF($1)
4793 | AC_LIBTOOL_DLOPEN_SELF($1)
5109 | # Whether dlopen is supported.
5110 | dlopen_support=$enable_dlopen
5112 | # Whether dlopen of programs is supported.
5113 | dlopen_self=$enable_dlopen_self
5115 | # Whether dlopen of statically linked programs is supported.
5116 | dlopen_self_static=$enable_dlopen_self_static
5124 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### glib/src/module.hg

```

{% raw %}
42 |  * supports all systems that provide an implementation of dlopen()
{% endraw %}

```
### glib/glibmm/module.h

```cpp

{% raw %}
93 |  * supports all systems that provide an implementation of dlopen()
{% endraw %}

```
### scripts/ltmain.sh

```bash

{% raw %}
478 |   -dlopen)
479 |     prevopt="-dlopen"
551 |   # Only execute mode is allowed to have -dlopen flags.
553 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1090 | 	    dlopen_self=$dlopen_self_static
1094 | 	    dlopen_self=$dlopen_self_static
1150 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1242 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1392 |       -dlopen)
1755 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1823 | 	  # This library was specified with -dlopen.
1965 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1977 | 	passes="conv scan dlopen dlpreopen link"
1990 | 	dlopen) libs="$dlfiles" ;;
1995 |       if test "$pass" = dlopen; then
2174 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2175 | 	      # If there is no dlopen support or we're linking statically,
2208 | 	dlopen=
2229 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2272 | 	# This library was specified with -dlopen.
2273 | 	if test "$pass" = dlopen; then
2275 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2279 | 	     test "$dlopen_support" != yes ||
2281 | 	    # If there is no dlname, no dlopen support or we're linking
2290 | 	fi # $pass = dlopen
2343 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2710 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2711 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2864 |       if test "$pass" != dlopen; then
2965 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3032 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3665 | 	    $echo "*** a static module, that should work as long as the dlopening"
3666 | 	    $echo "*** application is linked with the -dlopen flag."
3684 | 	    $echo "*** or is declared to -dlopen it."
4043 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4175 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4176 | 	   test "$dlopen_self_static" = unknown; then
4177 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5310 | # The name that we can dlopen(3).
5333 | # Files to dlopen/dlpreopen
5334 | dlopen='$dlfiles'
5949 |     # Handle -dlopen flags immediately.
5978 | 	# Skip this library if it cannot be dlopened.
6003 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6354 |   -dlopen FILE      add the directory containing FILE to the library path
6356 | This mode sets the library path environment variable according to \`-dlopen'
6405 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6414 |   -module           build a library that can dlopened
{% endraw %}

```
### docs/reference/html/classGlib_1_1Module.html

```html

{% raw %}
66 | The current implementation supports all systems that provide an implementation of dlopen() (e.g. Linux/Sun), as well as HP-UX via its shl_load() mechanism, and Windows platforms via DLLs. 
{% endraw %}

```