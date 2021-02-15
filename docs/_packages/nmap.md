---
name: "nmap"
layout: package
next_package: py-quast
previous_package: fenics-dolfinx
languages: ['cpp', 'bash']
---
## 7.70
11 / 2242 files match

 - [configure.ac](#configureac)
 - [ltmain.sh](#ltmainsh)
 - [nsock/src/configure.ac](#nsocksrcconfigureac)
 - [libdnet-stripped/aclocal.m4](#libdnet-strippedaclocalm4)
 - [nping/configure.ac](#npingconfigureac)
 - [ncat/configure.ac](#ncatconfigureac)
 - [liblua/loadlib.c](#liblualoadlibc)
 - [libssh2/ltmain.sh](#libssh2ltmainsh)
 - [libssh2/m4/libtool.m4](#libssh2m4libtoolm4)
 - [libssh2/m4/ltoptions.m4](#libssh2m4ltoptionsm4)
 - [libssh2/m4/lib-link.m4](#libssh2m4lib-linkm4)

### configure.ac

```

{% raw %}
110 | LUA_CFLAGS="-DLUA_USE_POSIX -DLUA_USE_DLOPEN"
809 | # OpenSSL and NSE C modules can require dlopen
810 | AC_SEARCH_LIBS(dlopen, dl)
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
### nsock/src/configure.ac

```

{% raw %}
255 | # OpenSSL requires dlopen on some platforms
256 | AC_SEARCH_LIBS(dlopen, dl)
{% endraw %}

```
### libdnet-stripped/aclocal.m4

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
### nping/configure.ac

```

{% raw %}
114 | # OpenSSL and NSE C modules can require dlopen
115 | AC_SEARCH_LIBS(dlopen, dl)
{% endraw %}

```
### ncat/configure.ac

```

{% raw %}
62 | # OpenSSL requires dlopen on some platforms
63 | AC_SEARCH_LIBS(dlopen, dl)
242 | LUA_CFLAGS="-DLUA_USE_POSIX -DLUA_USE_DLOPEN"
{% endraw %}

```
### liblua/loadlib.c

```cpp

{% raw %}
126 | #if defined(LUA_USE_DLOPEN)	/* { */
156 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```
### libssh2/ltmain.sh

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
7346 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7414 | 	  # This library was specified with -dlopen.
7534 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7545 | 	passes="conv scan dlopen dlpreopen link"
7571 | 	dlopen) libs=$dlfiles ;;
7602 |       if test dlopen = "$pass"; then
7822 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7823 | 	      # If there is no dlopen support or we're linking statically,
7851 | 	dlopen=
7881 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7927 | 	# This library was specified with -dlopen.
7928 | 	if test dlopen = "$pass"; then
7930 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7932 | 	     test yes != "$dlopen_support" ||
7935 | 	    # If there is no dlname, no dlopen support or we're linking
7944 | 	fi # $pass = dlopen
8000 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8002 | 	      # We recover the dlopen module name by 'saving' the la file
8026 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8155 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8156 | 	  dlopenmodule=
8159 | 	      dlopenmodule=$dlpremoduletest
8163 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8260 | 		    # if the lib is a (non-dlopened) module then we cannot
8264 | 		      if test "X$dlopenmodule" != "X$lib"; then
8416 | 	      echo "*** a static module, that should work as long as the dlopening application"
8417 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8561 |       if test dlopen != "$pass"; then
8691 | 	func_warning "'-dlopen' is ignored for archives"
8758 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9455 | 	    echo "*** a static module, that should work as long as the dlopening"
9456 | 	    echo "*** application is linked with the -dlopen flag."
9474 | 	    echo "*** or is declared to -dlopen it."
10086 | 	func_warning "'-dlopen' is ignored for objects"
10206 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10207 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10888 | # The name that we can dlopen(3).
10917 | # Files to dlopen/dlpreopen
10918 | dlopen='$dlfiles'
{% endraw %}

```
### libssh2/m4/libtool.m4

```

{% raw %}
1820 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1823 | m4_defun([_LT_TRY_DLOPEN_SELF],
1881 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1914 | ])# _LT_TRY_DLOPEN_SELF
1917 | # LT_SYS_DLOPEN_SELF
1919 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1921 | if test yes != "$enable_dlopen"; then
1922 |   enable_dlopen=unknown
1923 |   enable_dlopen_self=unknown
1924 |   enable_dlopen_self_static=unknown
1926 |   lt_cv_dlopen=no
1927 |   lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen=load_add_on
1932 |     lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen_self=yes
1937 |     lt_cv_dlopen=LoadLibrary
1938 |     lt_cv_dlopen_libs=
1942 |     lt_cv_dlopen=dlopen
1943 |     lt_cv_dlopen_libs=
1948 |     AC_CHECK_LIB([dl], [dlopen],
1949 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1950 |     lt_cv_dlopen=dyld
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1959 |     lt_cv_dlopen=dlopen
1960 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen_self=no
1966 | 	  [lt_cv_dlopen=shl_load],
1968 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1969 | 	[AC_CHECK_FUNC([dlopen],
1970 | 	      [lt_cv_dlopen=dlopen],
1971 | 	  [AC_CHECK_LIB([dl], [dlopen],
1972 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1973 | 	    [AC_CHECK_LIB([svld], [dlopen],
1974 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1976 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1985 |   if test no = "$lt_cv_dlopen"; then
1986 |     enable_dlopen=no
1988 |     enable_dlopen=yes
1991 |   case $lt_cv_dlopen in
1992 |   dlopen)
2000 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2002 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2003 | 	  lt_cv_dlopen_self, [dnl
2004 | 	  _LT_TRY_DLOPEN_SELF(
2005 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2006 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2009 |     if test yes = "$lt_cv_dlopen_self"; then
2011 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2012 | 	  lt_cv_dlopen_self_static, [dnl
2013 | 	  _LT_TRY_DLOPEN_SELF(
2014 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2015 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2025 |   case $lt_cv_dlopen_self in
2026 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2027 |   *) enable_dlopen_self=unknown ;;
2030 |   case $lt_cv_dlopen_self_static in
2031 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2032 |   *) enable_dlopen_self_static=unknown ;;
2035 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2036 | 	 [Whether dlopen is supported])
2037 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2038 | 	 [Whether dlopen of programs is supported])
2039 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2040 | 	 [Whether dlopen of statically linked programs is supported])
2041 | ])# LT_SYS_DLOPEN_SELF
2044 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2046 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6140 |     [Compiler flag to allow reflexive dlopens])
6253 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### libssh2/m4/ltoptions.m4

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
### libssh2/m4/lib-link.m4

```

{% raw %}
459 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```