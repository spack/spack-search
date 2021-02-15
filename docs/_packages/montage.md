---
name: "montage"
layout: package
next_package: treelite
previous_package: munge
languages: ['bash']
---
## 6.0
13 / 4098 files match

 - [Windows/lib/libpng-1.6.29/ltmain.sh](#windowsliblibpng-1629ltmainsh)
 - [Windows/lib/libpng-1.6.29/scripts/libtool.m4](#windowsliblibpng-1629scriptslibtoolm4)
 - [Windows/lib/libpng-1.6.29/scripts/ltoptions.m4](#windowsliblibpng-1629scriptsltoptionsm4)
 - [lib/src/freetype-2.4.4/objs/libfreetype.la](#libsrcfreetype-244objslibfreetypela)
 - [lib/src/freetype-2.4.4/builds/unix/config.status](#libsrcfreetype-244buildsunixconfigstatus)
 - [lib/src/freetype-2.4.4/builds/unix/ltmain.sh](#libsrcfreetype-244buildsunixltmainsh)
 - [lib/src/freetype-2.4.4/builds/unix/aclocal.m4](#libsrcfreetype-244buildsunixaclocalm4)
 - [lib/src/freetype-2.5.4/builds/unix/ltmain.sh](#libsrcfreetype-254buildsunixltmainsh)
 - [lib/src/freetype-2.5.4/builds/unix/aclocal.m4](#libsrcfreetype-254buildsunixaclocalm4)
 - [lib/src/freetype-2.9.1/builds/unix/ltmain.sh](#libsrcfreetype-291buildsunixltmainsh)
 - [lib/src/freetype-2.9.1/builds/unix/aclocal.m4](#libsrcfreetype-291buildsunixaclocalm4)
 - [lib/src/jpeg-8b/ltmain.sh](#libsrcjpeg-8bltmainsh)
 - [lib/src/jpeg-8b/aclocal.m4](#libsrcjpeg-8baclocalm4)

### Windows/lib/libpng-1.6.29/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### Windows/lib/libpng-1.6.29/scripts/libtool.m4

```

{% raw %}
1821 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1824 | m4_defun([_LT_TRY_DLOPEN_SELF],
1882 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1915 | ])# _LT_TRY_DLOPEN_SELF
1918 | # LT_SYS_DLOPEN_SELF
1920 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1922 | if test yes != "$enable_dlopen"; then
1923 |   enable_dlopen=unknown
1924 |   enable_dlopen_self=unknown
1925 |   enable_dlopen_self_static=unknown
1927 |   lt_cv_dlopen=no
1928 |   lt_cv_dlopen_libs=
1932 |     lt_cv_dlopen=load_add_on
1933 |     lt_cv_dlopen_libs=
1934 |     lt_cv_dlopen_self=yes
1938 |     lt_cv_dlopen=LoadLibrary
1939 |     lt_cv_dlopen_libs=
1943 |     lt_cv_dlopen=dlopen
1944 |     lt_cv_dlopen_libs=
1949 |     AC_CHECK_LIB([dl], [dlopen],
1950 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1951 |     lt_cv_dlopen=dyld
1952 |     lt_cv_dlopen_libs=
1953 |     lt_cv_dlopen_self=yes
1960 |     lt_cv_dlopen=dlopen
1961 |     lt_cv_dlopen_libs=
1962 |     lt_cv_dlopen_self=no
1967 | 	  [lt_cv_dlopen=shl_load],
1969 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1970 | 	[AC_CHECK_FUNC([dlopen],
1971 | 	      [lt_cv_dlopen=dlopen],
1972 | 	  [AC_CHECK_LIB([dl], [dlopen],
1973 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1974 | 	    [AC_CHECK_LIB([svld], [dlopen],
1975 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1977 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1986 |   if test no = "$lt_cv_dlopen"; then
1987 |     enable_dlopen=no
1989 |     enable_dlopen=yes
1992 |   case $lt_cv_dlopen in
1993 |   dlopen)
2001 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2003 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2004 | 	  lt_cv_dlopen_self, [dnl
2005 | 	  _LT_TRY_DLOPEN_SELF(
2006 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2007 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2010 |     if test yes = "$lt_cv_dlopen_self"; then
2012 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2013 | 	  lt_cv_dlopen_self_static, [dnl
2014 | 	  _LT_TRY_DLOPEN_SELF(
2015 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2016 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2026 |   case $lt_cv_dlopen_self in
2027 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2028 |   *) enable_dlopen_self=unknown ;;
2031 |   case $lt_cv_dlopen_self_static in
2032 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2033 |   *) enable_dlopen_self_static=unknown ;;
2036 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2037 | 	 [Whether dlopen is supported])
2038 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2039 | 	 [Whether dlopen of programs is supported])
2040 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2041 | 	 [Whether dlopen of statically linked programs is supported])
2042 | ])# LT_SYS_DLOPEN_SELF
2045 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2047 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6122 |     [Compiler flag to allow reflexive dlopens])
6235 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### Windows/lib/libpng-1.6.29/scripts/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
107 | # dlopen
109 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
112 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
113 | [_LT_SET_OPTION([LT_INIT], [dlopen])
116 | put the 'dlopen' option into LT_INIT's first parameter.])
120 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### lib/src/freetype-2.4.4/objs/libfreetype.la

```

{% raw %}
6 | # The name that we can dlopen(3).
35 | # Files to dlopen/dlpreopen
36 | dlopen=''
{% endraw %}

```
### lib/src/freetype-2.4.4/builds/unix/config.status

```

{% raw %}
674 | enable_dlopen='unknown'
675 | enable_dlopen_self='unknown'
676 | enable_dlopen_self_static='unknown'
1518 | # Whether dlopen is supported.
1519 | dlopen_support=$enable_dlopen
1521 | # Whether dlopen of programs is supported.
1522 | dlopen_self=$enable_dlopen_self
1524 | # Whether dlopen of statically linked programs is supported.
1525 | dlopen_self_static=$enable_dlopen_self_static
1565 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### lib/src/freetype-2.4.4/builds/unix/ltmain.sh

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
### lib/src/freetype-2.4.4/builds/unix/aclocal.m4

```

{% raw %}
1640 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1643 | m4_defun([_LT_TRY_DLOPEN_SELF],
1695 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1724 | ])# _LT_TRY_DLOPEN_SELF
1727 | # LT_SYS_DLOPEN_SELF
1729 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1731 | if test "x$enable_dlopen" != xyes; then
1732 |   enable_dlopen=unknown
1733 |   enable_dlopen_self=unknown
1734 |   enable_dlopen_self_static=unknown
1736 |   lt_cv_dlopen=no
1737 |   lt_cv_dlopen_libs=
1741 |     lt_cv_dlopen="load_add_on"
1742 |     lt_cv_dlopen_libs=
1743 |     lt_cv_dlopen_self=yes
1747 |     lt_cv_dlopen="LoadLibrary"
1748 |     lt_cv_dlopen_libs=
1752 |     lt_cv_dlopen="dlopen"
1753 |     lt_cv_dlopen_libs=
1758 |     AC_CHECK_LIB([dl], [dlopen],
1759 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1760 |     lt_cv_dlopen="dyld"
1761 |     lt_cv_dlopen_libs=
1762 |     lt_cv_dlopen_self=yes
1768 | 	  [lt_cv_dlopen="shl_load"],
1770 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1771 | 	[AC_CHECK_FUNC([dlopen],
1772 | 	      [lt_cv_dlopen="dlopen"],
1773 | 	  [AC_CHECK_LIB([dl], [dlopen],
1774 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1775 | 	    [AC_CHECK_LIB([svld], [dlopen],
1776 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1778 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1787 |   if test "x$lt_cv_dlopen" != xno; then
1788 |     enable_dlopen=yes
1790 |     enable_dlopen=no
1793 |   case $lt_cv_dlopen in
1794 |   dlopen)
1802 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1804 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1805 | 	  lt_cv_dlopen_self, [dnl
1806 | 	  _LT_TRY_DLOPEN_SELF(
1807 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1808 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1811 |     if test "x$lt_cv_dlopen_self" = xyes; then
1813 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1814 | 	  lt_cv_dlopen_self_static, [dnl
1815 | 	  _LT_TRY_DLOPEN_SELF(
1816 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1817 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1827 |   case $lt_cv_dlopen_self in
1828 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1829 |   *) enable_dlopen_self=unknown ;;
1832 |   case $lt_cv_dlopen_self_static in
1833 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1834 |   *) enable_dlopen_self_static=unknown ;;
1837 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1838 | 	 [Whether dlopen is supported])
1839 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1840 | 	 [Whether dlopen of programs is supported])
1841 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1842 | 	 [Whether dlopen of statically linked programs is supported])
1843 | ])# LT_SYS_DLOPEN_SELF
1846 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1848 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5161 |     [Compiler flag to allow reflexive dlopens])
5273 |   LT_SYS_DLOPEN_SELF
7423 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7455 | # dlopen
7457 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7460 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7461 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7464 | put the `dlopen' option into LT_INIT's first parameter.])
7468 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
7914 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### lib/src/freetype-2.5.4/builds/unix/ltmain.sh

```bash

{% raw %}
2255 |     opt_dlopen=
2316 |         --dlopen|-dlopen)
2317 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2433 |       # Only execute mode is allowed to have -dlopen flags.
2434 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2435 |         func_error "unrecognized option '-dlopen'"
3653 |   -dlopen FILE      add the directory containing FILE to the library path
3655 | This mode sets the library path environment variable according to '-dlopen'
3710 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3719 |   -module           build a library that can dlopened
3826 |     # Handle -dlopen flags immediately.
3827 |     for file in $opt_dlopen; do
3846 | 	# Skip this library if it cannot be dlopened.
3873 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6535 | 	    dlopen_self=$dlopen_self_static
6541 | 	    dlopen_self=$dlopen_self_static
6547 | 	    dlopen_self=$dlopen_self_static
6605 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6695 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6857 |       -dlopen)
7266 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7334 | 	  # This library was specified with -dlopen.
7451 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7462 | 	passes="conv scan dlopen dlpreopen link"
7488 | 	dlopen) libs=$dlfiles ;;
7516 |       if test dlopen = "$pass"; then
7736 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7737 | 	      # If there is no dlopen support or we're linking statically,
7765 | 	dlopen=
7795 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7841 | 	# This library was specified with -dlopen.
7842 | 	if test dlopen = "$pass"; then
7844 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7846 | 	     test yes != "$dlopen_support" ||
7849 | 	    # If there is no dlname, no dlopen support or we're linking
7858 | 	fi # $pass = dlopen
7914 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7916 | 	      # We recover the dlopen module name by 'saving' the la file
7940 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8069 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8070 | 	  dlopenmodule=
8073 | 	      dlopenmodule=$dlpremoduletest
8077 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8174 | 		    # if the lib is a (non-dlopened) module then we cannot
8178 | 		      if test "X$dlopenmodule" != "X$lib"; then
8330 | 	      echo "*** a static module, that should work as long as the dlopening application"
8331 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8475 |       if test dlopen != "$pass"; then
8574 | 	func_warning "'-dlopen' is ignored for archives"
8641 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9329 | 	    echo "*** a static module, that should work as long as the dlopening"
9330 | 	    echo "*** application is linked with the -dlopen flag."
9348 | 	    echo "*** or is declared to -dlopen it."
9960 | 	func_warning "'-dlopen' is ignored for objects"
10080 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10081 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10762 | # The name that we can dlopen(3).
10791 | # Files to dlopen/dlpreopen
10792 | dlopen='$dlfiles'
{% endraw %}

```
### lib/src/freetype-2.5.4/builds/unix/aclocal.m4

```

{% raw %}
1795 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1798 | m4_defun([_LT_TRY_DLOPEN_SELF],
1856 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1889 | ])# _LT_TRY_DLOPEN_SELF
1892 | # LT_SYS_DLOPEN_SELF
1894 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1896 | if test yes != "$enable_dlopen"; then
1897 |   enable_dlopen=unknown
1898 |   enable_dlopen_self=unknown
1899 |   enable_dlopen_self_static=unknown
1901 |   lt_cv_dlopen=no
1902 |   lt_cv_dlopen_libs=
1906 |     lt_cv_dlopen=load_add_on
1907 |     lt_cv_dlopen_libs=
1908 |     lt_cv_dlopen_self=yes
1912 |     lt_cv_dlopen=LoadLibrary
1913 |     lt_cv_dlopen_libs=
1917 |     lt_cv_dlopen=dlopen
1918 |     lt_cv_dlopen_libs=
1923 |     AC_CHECK_LIB([dl], [dlopen],
1924 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1925 |     lt_cv_dlopen=dyld
1926 |     lt_cv_dlopen_libs=
1927 |     lt_cv_dlopen_self=yes
1934 |     lt_cv_dlopen=dlopen
1935 |     lt_cv_dlopen_libs=
1936 |     lt_cv_dlopen_self=no
1941 | 	  [lt_cv_dlopen=shl_load],
1943 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1944 | 	[AC_CHECK_FUNC([dlopen],
1945 | 	      [lt_cv_dlopen=dlopen],
1946 | 	  [AC_CHECK_LIB([dl], [dlopen],
1947 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1948 | 	    [AC_CHECK_LIB([svld], [dlopen],
1949 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1951 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1960 |   if test no = "$lt_cv_dlopen"; then
1961 |     enable_dlopen=no
1963 |     enable_dlopen=yes
1966 |   case $lt_cv_dlopen in
1967 |   dlopen)
1975 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1977 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1978 | 	  lt_cv_dlopen_self, [dnl
1979 | 	  _LT_TRY_DLOPEN_SELF(
1980 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1981 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1984 |     if test yes = "$lt_cv_dlopen_self"; then
1986 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1987 | 	  lt_cv_dlopen_self_static, [dnl
1988 | 	  _LT_TRY_DLOPEN_SELF(
1989 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1990 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2000 |   case $lt_cv_dlopen_self in
2001 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2002 |   *) enable_dlopen_self=unknown ;;
2005 |   case $lt_cv_dlopen_self_static in
2006 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2007 |   *) enable_dlopen_self_static=unknown ;;
2010 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2011 | 	 [Whether dlopen is supported])
2012 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2013 | 	 [Whether dlopen of programs is supported])
2014 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2015 | 	 [Whether dlopen of statically linked programs is supported])
2016 | ])# LT_SYS_DLOPEN_SELF
2019 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2021 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5786 |     [Compiler flag to allow reflexive dlopens])
5895 |   LT_SYS_DLOPEN_SELF
8047 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8079 | # dlopen
8081 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8084 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8085 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8088 | put the 'dlopen' option into LT_INIT's first parameter.])
8092 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8553 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### lib/src/freetype-2.9.1/builds/unix/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### lib/src/freetype-2.9.1/builds/unix/aclocal.m4

```

{% raw %}
1827 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1830 | m4_defun([_LT_TRY_DLOPEN_SELF],
1888 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1921 | ])# _LT_TRY_DLOPEN_SELF
1924 | # LT_SYS_DLOPEN_SELF
1926 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1928 | if test yes != "$enable_dlopen"; then
1929 |   enable_dlopen=unknown
1930 |   enable_dlopen_self=unknown
1931 |   enable_dlopen_self_static=unknown
1933 |   lt_cv_dlopen=no
1934 |   lt_cv_dlopen_libs=
1938 |     lt_cv_dlopen=load_add_on
1939 |     lt_cv_dlopen_libs=
1940 |     lt_cv_dlopen_self=yes
1944 |     lt_cv_dlopen=LoadLibrary
1945 |     lt_cv_dlopen_libs=
1949 |     lt_cv_dlopen=dlopen
1950 |     lt_cv_dlopen_libs=
1955 |     AC_CHECK_LIB([dl], [dlopen],
1956 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1957 |     lt_cv_dlopen=dyld
1958 |     lt_cv_dlopen_libs=
1959 |     lt_cv_dlopen_self=yes
1966 |     lt_cv_dlopen=dlopen
1967 |     lt_cv_dlopen_libs=
1968 |     lt_cv_dlopen_self=no
1973 | 	  [lt_cv_dlopen=shl_load],
1975 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1976 | 	[AC_CHECK_FUNC([dlopen],
1977 | 	      [lt_cv_dlopen=dlopen],
1978 | 	  [AC_CHECK_LIB([dl], [dlopen],
1979 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1980 | 	    [AC_CHECK_LIB([svld], [dlopen],
1981 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1983 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1992 |   if test no = "$lt_cv_dlopen"; then
1993 |     enable_dlopen=no
1995 |     enable_dlopen=yes
1998 |   case $lt_cv_dlopen in
1999 |   dlopen)
2007 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2009 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2010 | 	  lt_cv_dlopen_self, [dnl
2011 | 	  _LT_TRY_DLOPEN_SELF(
2012 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2013 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2016 |     if test yes = "$lt_cv_dlopen_self"; then
2018 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2019 | 	  lt_cv_dlopen_self_static, [dnl
2020 | 	  _LT_TRY_DLOPEN_SELF(
2021 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2022 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2032 |   case $lt_cv_dlopen_self in
2033 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2034 |   *) enable_dlopen_self=unknown ;;
2037 |   case $lt_cv_dlopen_self_static in
2038 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2039 |   *) enable_dlopen_self_static=unknown ;;
2042 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2043 | 	 [Whether dlopen is supported])
2044 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2045 | 	 [Whether dlopen of programs is supported])
2046 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2047 | 	 [Whether dlopen of statically linked programs is supported])
2048 | ])# LT_SYS_DLOPEN_SELF
2051 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2053 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6128 |     [Compiler flag to allow reflexive dlopens])
6237 |   LT_SYS_DLOPEN_SELF
8546 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8580 | # dlopen
8582 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8585 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8586 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8589 | put the 'dlopen' option into LT_INIT's first parameter.])
8593 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
9107 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### lib/src/jpeg-8b/ltmain.sh

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
### lib/src/jpeg-8b/aclocal.m4

```

{% raw %}
1649 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1652 | m4_defun([_LT_TRY_DLOPEN_SELF],
1704 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1733 | ])# _LT_TRY_DLOPEN_SELF
1736 | # LT_SYS_DLOPEN_SELF
1738 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1740 | if test "x$enable_dlopen" != xyes; then
1741 |   enable_dlopen=unknown
1742 |   enable_dlopen_self=unknown
1743 |   enable_dlopen_self_static=unknown
1745 |   lt_cv_dlopen=no
1746 |   lt_cv_dlopen_libs=
1750 |     lt_cv_dlopen="load_add_on"
1751 |     lt_cv_dlopen_libs=
1752 |     lt_cv_dlopen_self=yes
1756 |     lt_cv_dlopen="LoadLibrary"
1757 |     lt_cv_dlopen_libs=
1761 |     lt_cv_dlopen="dlopen"
1762 |     lt_cv_dlopen_libs=
1767 |     AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1769 |     lt_cv_dlopen="dyld"
1770 |     lt_cv_dlopen_libs=
1771 |     lt_cv_dlopen_self=yes
1777 | 	  [lt_cv_dlopen="shl_load"],
1779 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1780 | 	[AC_CHECK_FUNC([dlopen],
1781 | 	      [lt_cv_dlopen="dlopen"],
1782 | 	  [AC_CHECK_LIB([dl], [dlopen],
1783 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1784 | 	    [AC_CHECK_LIB([svld], [dlopen],
1785 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1787 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1796 |   if test "x$lt_cv_dlopen" != xno; then
1797 |     enable_dlopen=yes
1799 |     enable_dlopen=no
1802 |   case $lt_cv_dlopen in
1803 |   dlopen)
1811 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1813 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1814 | 	  lt_cv_dlopen_self, [dnl
1815 | 	  _LT_TRY_DLOPEN_SELF(
1816 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1817 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1820 |     if test "x$lt_cv_dlopen_self" = xyes; then
1822 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1823 | 	  lt_cv_dlopen_self_static, [dnl
1824 | 	  _LT_TRY_DLOPEN_SELF(
1825 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1826 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1836 |   case $lt_cv_dlopen_self in
1837 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1838 |   *) enable_dlopen_self=unknown ;;
1841 |   case $lt_cv_dlopen_self_static in
1842 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1843 |   *) enable_dlopen_self_static=unknown ;;
1846 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1847 | 	 [Whether dlopen is supported])
1848 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1849 | 	 [Whether dlopen of programs is supported])
1850 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1851 | 	 [Whether dlopen of statically linked programs is supported])
1852 | ])# LT_SYS_DLOPEN_SELF
1855 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1857 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5170 |     [Compiler flag to allow reflexive dlopens])
5282 |   LT_SYS_DLOPEN_SELF
7432 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7464 | # dlopen
7466 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7469 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7470 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7473 | put the `dlopen' option into LT_INIT's first parameter.])
7477 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
7923 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```