---
name: "fcgi"
layout: package
next_package: mlocate
previous_package: gnupg
languages: ['bash']
---
## 2.4.1-SNAP-0910052249
2 / 111 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
522 |   -dlopen)
523 |     prevopt="-dlopen"
607 |   # Only execute mode is allowed to have -dlopen flags.
609 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1146 | 	    dlopen_self=$dlopen_self_static
1151 | 	    dlopen_self=$dlopen_self_static
1207 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1299 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1456 |       -dlopen)
1843 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1916 | 	  # This library was specified with -dlopen.
2057 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2069 | 	passes="conv scan dlopen dlpreopen link"
2082 | 	dlopen) libs="$dlfiles" ;;
2087 |       if test "$pass" = dlopen; then
2266 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2267 | 	      # If there is no dlopen support or we're linking statically,
2300 | 	dlopen=
2321 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2364 | 	# This library was specified with -dlopen.
2365 | 	if test "$pass" = dlopen; then
2367 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2371 | 	     test "$dlopen_support" != yes ||
2373 | 	    # If there is no dlname, no dlopen support or we're linking
2382 | 	fi # $pass = dlopen
2435 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2810 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2811 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2962 |       if test "$pass" != dlopen; then
3063 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3130 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3768 | 	    $echo "*** a static module, that should work as long as the dlopening"
3769 | 	    $echo "*** application is linked with the -dlopen flag."
3787 | 	    $echo "*** or is declared to -dlopen it."
4197 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4329 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4330 | 	   test "$dlopen_self_static" = unknown; then
4331 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5669 | # The name that we can dlopen(3).
5692 | # Files to dlopen/dlpreopen
5693 | dlopen='$dlfiles'
6308 |     # Handle -dlopen flags immediately.
6337 | 	# Skip this library if it cannot be dlopened.
6362 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6722 |   -dlopen FILE      add the directory containing FILE to the library path
6724 | This mode sets the library path environment variable according to \`-dlopen'
6773 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6782 |   -module           build a library that can dlopened
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1054 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
1669 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1672 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
1728 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1757 | ])# _LT_AC_TRY_DLOPEN_SELF
1760 | # AC_LIBTOOL_DLOPEN_SELF
1762 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1764 | if test "x$enable_dlopen" != xyes; then
1765 |   enable_dlopen=unknown
1766 |   enable_dlopen_self=unknown
1767 |   enable_dlopen_self_static=unknown
1769 |   lt_cv_dlopen=no
1770 |   lt_cv_dlopen_libs=
1774 |     lt_cv_dlopen="load_add_on"
1775 |     lt_cv_dlopen_libs=
1776 |     lt_cv_dlopen_self=yes
1780 |     lt_cv_dlopen="LoadLibrary"
1781 |     lt_cv_dlopen_libs=
1785 |     lt_cv_dlopen="dlopen"
1786 |     lt_cv_dlopen_libs=
1791 |     AC_CHECK_LIB([dl], [dlopen],
1792 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1793 |     lt_cv_dlopen="dyld"
1794 |     lt_cv_dlopen_libs=
1795 |     lt_cv_dlopen_self=yes
1801 | 	  [lt_cv_dlopen="shl_load"],
1803 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
1804 | 	[AC_CHECK_FUNC([dlopen],
1805 | 	      [lt_cv_dlopen="dlopen"],
1806 | 	  [AC_CHECK_LIB([dl], [dlopen],
1807 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1808 | 	    [AC_CHECK_LIB([svld], [dlopen],
1809 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1811 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
1820 |   if test "x$lt_cv_dlopen" != xno; then
1821 |     enable_dlopen=yes
1823 |     enable_dlopen=no
1826 |   case $lt_cv_dlopen in
1827 |   dlopen)
1835 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1837 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1838 | 	  lt_cv_dlopen_self, [dnl
1839 | 	  _LT_AC_TRY_DLOPEN_SELF(
1840 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1841 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1844 |     if test "x$lt_cv_dlopen_self" = xyes; then
1846 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1847 |     	  lt_cv_dlopen_self_static, [dnl
1848 | 	  _LT_AC_TRY_DLOPEN_SELF(
1849 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1850 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1860 |   case $lt_cv_dlopen_self in
1861 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1862 |   *) enable_dlopen_self=unknown ;;
1865 |   case $lt_cv_dlopen_self_static in
1866 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1867 |   *) enable_dlopen_self_static=unknown ;;
1870 | ])# AC_LIBTOOL_DLOPEN_SELF
2743 | # AC_LIBTOOL_DLOPEN
2745 | # enable checks for dlopen support
2746 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2748 | ])# AC_LIBTOOL_DLOPEN
3536 | AC_LIBTOOL_DLOPEN_SELF
5207 | # Whether dlopen is supported.
5208 | dlopen_support=$enable_dlopen
5210 | # Whether dlopen of programs is supported.
5211 | dlopen_self=$enable_dlopen_self
5213 | # Whether dlopen of statically linked programs is supported.
5214 | dlopen_self_static=$enable_dlopen_self_static
5222 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```