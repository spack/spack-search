---
name: "r"
layout: package
next_package: fakexrandr
previous_package: libmaxminddb
languages: ['cpp', 'bash']
---
## 3.3.1
12 / 4124 files match

 - [configure.ac](#configureac)
 - [src/main/Rdynload.c](#srcmainrdynloadc)
 - [src/library/base/man/dynload.Rd](#srclibrarybasemandynloadrd)
 - [src/extra/intl/libgnuintl.h.in](#srcextraintllibgnuintlhin)
 - [src/unix/hpdlfcn.c](#srcunixhpdlfcnc)
 - [src/unix/dynload.c](#srcunixdynloadc)
 - [src/unix/hpdlfcn.h](#srcunixhpdlfcnh)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/gettext-lib.m4](#m4gettext-libm4)
 - [tools/ltmain.sh](#toolsltmainsh)
 - [doc/NEWS.1](#docnews1)

### configure.ac

```

{% raw %}
750 |     AC_CHECK_LIB(dl, dlopen)
{% endraw %}

```
### src/main/Rdynload.c

```cpp

{% raw %}
40 |  *  done under Unix with dlopen, dlclose and dlsym (the exception is
45 |  *  1. The dlopen interface is available.
48 |  *  dlopen routines.  We maintain a list of currently loaded shared
521 | 	/* or if dlopen fails for some reason. */
819 |     /* the dlopen() interface, in which systems data and  */
{% endraw %}

```
### src/library/base/man/dynload.Rd

```

{% raw %}
79 |   aspects of the mode argument to the \code{dlopen()} routine on POSIX
166 |   \code{dlopen} has become the POSIX standard for doing this.  Under
167 |   Unix-alikes \code{dyn.load} uses the \code{dlopen} mechanism and
{% endraw %}

```
### src/extra/intl/libgnuintl.h.in

```

{% raw %}
70 |      4. in the dlopen()ed shared libraries, in the order in which they were
71 |         dlopen()ed.
76 |      * libintl.so is a dependency of a dlopen()ed shared library but not
{% endraw %}

```
### src/unix/hpdlfcn.c

```cpp

{% raw %}
38 |  * This is a minimal implementation of the ELF dlopen, dlclose, dlsym
127 | void *dlopen(const char *fname, int mode)
{% endraw %}

```
### src/unix/dynload.c

```cpp

{% raw %}
24 |    We include this table, even when we have dlopen and friends.
64 | static int computeDLOpenFlag(int asLocal, int now);
90 |     openFlag = computeDLOpenFlag(asLocal, now);
91 |     handle = (void *) dlopen(path,openFlag);
126 |     Computes the flag to be passed as the second argument to dlopen(),
138 | static int computeDLOpenFlag(int asLocal, int now)
165 | 				   resulting dlopen(). */
{% endraw %}

```
### src/unix/hpdlfcn.h

```cpp

{% raw %}
0 | void *dlopen(const char *, int);
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1822 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1825 | m4_defun([_LT_TRY_DLOPEN_SELF],
1883 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1916 | ])# _LT_TRY_DLOPEN_SELF
1919 | # LT_SYS_DLOPEN_SELF
1921 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1923 | if test yes != "$enable_dlopen"; then
1924 |   enable_dlopen=unknown
1925 |   enable_dlopen_self=unknown
1926 |   enable_dlopen_self_static=unknown
1928 |   lt_cv_dlopen=no
1929 |   lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen=load_add_on
1934 |     lt_cv_dlopen_libs=
1935 |     lt_cv_dlopen_self=yes
1939 |     lt_cv_dlopen=LoadLibrary
1940 |     lt_cv_dlopen_libs=
1944 |     lt_cv_dlopen=dlopen
1945 |     lt_cv_dlopen_libs=
1950 |     AC_CHECK_LIB([dl], [dlopen],
1951 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1952 |     lt_cv_dlopen=dyld
1953 |     lt_cv_dlopen_libs=
1954 |     lt_cv_dlopen_self=yes
1961 |     lt_cv_dlopen=dlopen
1962 |     lt_cv_dlopen_libs=
1963 |     lt_cv_dlopen_self=no
1968 | 	  [lt_cv_dlopen=shl_load],
1970 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1971 | 	[AC_CHECK_FUNC([dlopen],
1972 | 	      [lt_cv_dlopen=dlopen],
1973 | 	  [AC_CHECK_LIB([dl], [dlopen],
1974 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1975 | 	    [AC_CHECK_LIB([svld], [dlopen],
1976 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1978 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1987 |   if test no = "$lt_cv_dlopen"; then
1988 |     enable_dlopen=no
1990 |     enable_dlopen=yes
1993 |   case $lt_cv_dlopen in
1994 |   dlopen)
2002 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2004 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2005 | 	  lt_cv_dlopen_self, [dnl
2006 | 	  _LT_TRY_DLOPEN_SELF(
2007 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2008 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2011 |     if test yes = "$lt_cv_dlopen_self"; then
2013 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2014 | 	  lt_cv_dlopen_self_static, [dnl
2015 | 	  _LT_TRY_DLOPEN_SELF(
2016 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2017 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2027 |   case $lt_cv_dlopen_self in
2028 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2029 |   *) enable_dlopen_self=unknown ;;
2032 |   case $lt_cv_dlopen_self_static in
2033 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2034 |   *) enable_dlopen_self_static=unknown ;;
2037 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2038 | 	 [Whether dlopen is supported])
2039 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2040 | 	 [Whether dlopen of programs is supported])
2041 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2042 | 	 [Whether dlopen of statically linked programs is supported])
2043 | ])# LT_SYS_DLOPEN_SELF
2046 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2048 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6123 |     [Compiler flag to allow reflexive dlopens])
6236 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

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
### m4/gettext-lib.m4

```

{% raw %}
640 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### tools/ltmain.sh

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
### doc/NEWS.1

```

{% raw %}
5526 |     o	dlopen on Compaq Tru64 was finding the wrong entry points:
{% endraw %}

```