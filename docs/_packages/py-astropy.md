---
name: "py-astropy"
layout: package
next_package: opendx
previous_package: canal
languages: ['bash']
---
## 1.1.post1
4 / 1716 files match

 - [cextern/expat/aclocal.m4](#cexternexpataclocalm4)
 - [cextern/expat/m4/libtool.m4](#cexternexpatm4libtoolm4)
 - [cextern/expat/m4/ltoptions.m4](#cexternexpatm4ltoptionsm4)
 - [cextern/expat/conftools/ltmain.sh](#cexternexpatconftoolsltmainsh)

### cextern/expat/aclocal.m4

```

{% raw %}
1689 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1692 | m4_defun([_LT_TRY_DLOPEN_SELF],
1750 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1783 | ])# _LT_TRY_DLOPEN_SELF
1786 | # LT_SYS_DLOPEN_SELF
1788 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1790 | if test "x$enable_dlopen" != xyes; then
1791 |   enable_dlopen=unknown
1792 |   enable_dlopen_self=unknown
1793 |   enable_dlopen_self_static=unknown
1795 |   lt_cv_dlopen=no
1796 |   lt_cv_dlopen_libs=
1800 |     lt_cv_dlopen="load_add_on"
1801 |     lt_cv_dlopen_libs=
1802 |     lt_cv_dlopen_self=yes
1806 |     lt_cv_dlopen="LoadLibrary"
1807 |     lt_cv_dlopen_libs=
1811 |     lt_cv_dlopen="dlopen"
1812 |     lt_cv_dlopen_libs=
1817 |     AC_CHECK_LIB([dl], [dlopen],
1818 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1819 |     lt_cv_dlopen="dyld"
1820 |     lt_cv_dlopen_libs=
1821 |     lt_cv_dlopen_self=yes
1827 | 	  [lt_cv_dlopen="shl_load"],
1829 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1830 | 	[AC_CHECK_FUNC([dlopen],
1831 | 	      [lt_cv_dlopen="dlopen"],
1832 | 	  [AC_CHECK_LIB([dl], [dlopen],
1833 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1834 | 	    [AC_CHECK_LIB([svld], [dlopen],
1835 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1837 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1846 |   if test "x$lt_cv_dlopen" != xno; then
1847 |     enable_dlopen=yes
1849 |     enable_dlopen=no
1852 |   case $lt_cv_dlopen in
1853 |   dlopen)
1861 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1863 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1864 | 	  lt_cv_dlopen_self, [dnl
1865 | 	  _LT_TRY_DLOPEN_SELF(
1866 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1867 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1870 |     if test "x$lt_cv_dlopen_self" = xyes; then
1872 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1873 | 	  lt_cv_dlopen_self_static, [dnl
1874 | 	  _LT_TRY_DLOPEN_SELF(
1875 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1876 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1886 |   case $lt_cv_dlopen_self in
1887 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1888 |   *) enable_dlopen_self=unknown ;;
1891 |   case $lt_cv_dlopen_self_static in
1892 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1893 |   *) enable_dlopen_self_static=unknown ;;
1896 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1897 | 	 [Whether dlopen is supported])
1898 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1899 | 	 [Whether dlopen of programs is supported])
1900 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1901 | 	 [Whether dlopen of statically linked programs is supported])
1902 | ])# LT_SYS_DLOPEN_SELF
1905 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1907 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5612 |     [Compiler flag to allow reflexive dlopens])
5724 |   LT_SYS_DLOPEN_SELF
7919 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7951 | # dlopen
7953 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7956 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7957 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7960 | put the `dlopen' option into LT_INIT's first parameter.])
7964 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8410 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### cextern/expat/m4/libtool.m4

```

{% raw %}
1682 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1685 | m4_defun([_LT_TRY_DLOPEN_SELF],
1743 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1776 | ])# _LT_TRY_DLOPEN_SELF
1779 | # LT_SYS_DLOPEN_SELF
1781 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1783 | if test "x$enable_dlopen" != xyes; then
1784 |   enable_dlopen=unknown
1785 |   enable_dlopen_self=unknown
1786 |   enable_dlopen_self_static=unknown
1788 |   lt_cv_dlopen=no
1789 |   lt_cv_dlopen_libs=
1793 |     lt_cv_dlopen="load_add_on"
1794 |     lt_cv_dlopen_libs=
1795 |     lt_cv_dlopen_self=yes
1799 |     lt_cv_dlopen="LoadLibrary"
1800 |     lt_cv_dlopen_libs=
1804 |     lt_cv_dlopen="dlopen"
1805 |     lt_cv_dlopen_libs=
1810 |     AC_CHECK_LIB([dl], [dlopen],
1811 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1812 |     lt_cv_dlopen="dyld"
1813 |     lt_cv_dlopen_libs=
1814 |     lt_cv_dlopen_self=yes
1820 | 	  [lt_cv_dlopen="shl_load"],
1822 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1823 | 	[AC_CHECK_FUNC([dlopen],
1824 | 	      [lt_cv_dlopen="dlopen"],
1825 | 	  [AC_CHECK_LIB([dl], [dlopen],
1826 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1827 | 	    [AC_CHECK_LIB([svld], [dlopen],
1828 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1830 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1839 |   if test "x$lt_cv_dlopen" != xno; then
1840 |     enable_dlopen=yes
1842 |     enable_dlopen=no
1845 |   case $lt_cv_dlopen in
1846 |   dlopen)
1854 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1856 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1857 | 	  lt_cv_dlopen_self, [dnl
1858 | 	  _LT_TRY_DLOPEN_SELF(
1859 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1860 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1863 |     if test "x$lt_cv_dlopen_self" = xyes; then
1865 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1866 | 	  lt_cv_dlopen_self_static, [dnl
1867 | 	  _LT_TRY_DLOPEN_SELF(
1868 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1869 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1879 |   case $lt_cv_dlopen_self in
1880 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1881 |   *) enable_dlopen_self=unknown ;;
1884 |   case $lt_cv_dlopen_self_static in
1885 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1886 |   *) enable_dlopen_self_static=unknown ;;
1889 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1890 | 	 [Whether dlopen is supported])
1891 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1892 | 	 [Whether dlopen of programs is supported])
1893 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1894 | 	 [Whether dlopen of statically linked programs is supported])
1895 | ])# LT_SYS_DLOPEN_SELF
1898 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1900 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5605 |     [Compiler flag to allow reflexive dlopens])
5721 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### cextern/expat/m4/ltoptions.m4

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
### cextern/expat/conftools/ltmain.sh

```bash

{% raw %}
1078 |       --dlopen|-dlopen)
1080 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1201 |     # Only execute mode is allowed to have -dlopen flags.
1202 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1203 |       func_error "unrecognized option \`-dlopen'"
2351 |   -dlopen FILE      add the directory containing FILE to the library path
2353 | This mode sets the library path environment variable according to \`-dlopen'
2408 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2417 |   -module           build a library that can dlopened
2523 |     # Handle -dlopen flags immediately.
2524 |     for file in $opt_dlopen; do
2543 | 	# Skip this library if it cannot be dlopened.
2570 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5171 | 	    dlopen_self=$dlopen_self_static
5177 | 	    dlopen_self=$dlopen_self_static
5183 | 	    dlopen_self=$dlopen_self_static
5241 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5325 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5487 |       -dlopen)
5889 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5957 | 	  # This library was specified with -dlopen.
6074 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6085 | 	passes="conv scan dlopen dlpreopen link"
6111 | 	dlopen) libs="$dlfiles" ;;
6142 |       if test "$pass" = dlopen; then
6360 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6361 | 	      # If there is no dlopen support or we're linking statically,
6391 | 	dlopen=
6421 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6467 | 	# This library was specified with -dlopen.
6468 | 	if test "$pass" = dlopen; then
6470 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6473 | 	     test "$dlopen_support" != yes ||
6475 | 	    # If there is no dlname, no dlopen support or we're linking
6484 | 	fi # $pass = dlopen
6540 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6542 | 	      # We recover the dlopen module name by 'saving' the la file
6566 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6695 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6696 | 	  dlopenmodule=""
6699 | 	      dlopenmodule="$dlpremoduletest"
6703 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6800 | 		    # if the lib is a (non-dlopened) module then we can not
6804 | 		      if test "X$dlopenmodule" != "X$lib"; then
6956 | 	      echo "*** a static module, that should work as long as the dlopening application"
6957 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7101 |       if test "$pass" != dlopen; then
7200 | 	func_warning "\`-dlopen' is ignored for archives"
7267 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7945 | 	    echo "*** a static module, that should work as long as the dlopening"
7946 | 	    echo "*** application is linked with the -dlopen flag."
7964 | 	    echo "*** or is declared to -dlopen it."
8574 | 	func_warning "\`-dlopen' is ignored for objects"
8692 |         && test "$dlopen_support" = unknown \
8693 | 	&& test "$dlopen_self" = unknown \
8694 | 	&& test "$dlopen_self_static" = unknown && \
8695 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9373 | # The name that we can dlopen(3).
9402 | # Files to dlopen/dlpreopen
9403 | dlopen='$dlfiles'
{% endraw %}

```