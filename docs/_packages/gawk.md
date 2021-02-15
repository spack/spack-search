---
name: "gawk"
layout: package
next_package: gmake
previous_package: nicstat
languages: ['cpp', 'bash']
---
## 5.1.0
18 / 1886 files match

 - [ext.c](#extc)
 - [ChangeLog.0](#changelog0)
 - [configure.ac](#configureac)
 - [NEWS.0](#news0)
 - [ChangeLog.1](#changelog1)
 - [nonposix.h](#nonposixh)
 - [m4/lib-link.m4](#m4lib-linkm4)
 - [extension/m4/libtool.m4](#extensionm4libtoolm4)
 - [extension/m4/ltoptions.m4](#extensionm4ltoptionsm4)
 - [extension/m4/lib-link.m4](#extensionm4lib-linkm4)
 - [extension/build-aux/ltmain.sh](#extensionbuild-auxltmainsh)
 - [pc/dlfcn.h](#pcdlfcnh)
 - [pc/ChangeLog.1](#pcchangelog1)
 - [pc/gawkmisc.pc](#pcgawkmiscpc)
 - [doc/gawktexi.in](#docgawktexiin)
 - [doc/gawk.info](#docgawkinfo)
 - [doc/gawk.texi](#docgawktexi)
 - [doc/it/gawktexi.in](#docitgawktexiin)

### ext.c

```cpp

{% raw %}
58 | 	if ((dl = dlopen(lib_name, flags)) == NULL)
{% endraw %}

```
### ChangeLog.0

```

{% raw %}
2996 | 	* configure.ac: Check in Tandem's zrldsrl library for dlopen.
{% endraw %}

```
### configure.ac

```

{% raw %}
323 | 		# Check this separately. Some systems have dlopen
326 | 		AC_SEARCH_LIBS(dlopen, dl zrldsrl, gawk_have_dlopen=yes, gawk_have_dlopen=no)
329 | 		if test "$gawk_have_dlopen" = yes
{% endraw %}

```
### NEWS.0

```

{% raw %}
544 |     that support dlopen. This facility is not (yet) as portable or well
{% endraw %}

```
### ChangeLog.1

```

{% raw %}
1241 | 	os2_dlopen and redirect dlopen to os2_dlopen.
{% endraw %}

```
### nonposix.h

```cpp

{% raw %}
92 | #define dlopen(f, m) os2_dlopen(f, m)
93 | void *os2_dlopen(const char *file, int mode);
{% endraw %}

```
### m4/lib-link.m4

```

{% raw %}
518 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### extension/m4/libtool.m4

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
6141 |     [Compiler flag to allow reflexive dlopens])
6254 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### extension/m4/ltoptions.m4

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
### extension/m4/lib-link.m4

```

{% raw %}
518 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### extension/build-aux/ltmain.sh

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
### pc/dlfcn.h

```cpp

{% raw %}
6 | extern void *dlopen (const char *, int);
{% endraw %}

```
### pc/ChangeLog.1

```

{% raw %}
206 | 	* gawkmisc.pc (os2_dlsym, os2_fixdllname, os2_dlopen) [__KLIBC__]:
707 | 	* gawkmisc.pc (dlopen, dlerror, dlclose, dlsym) [DYNAMIC]: New
{% endraw %}

```
### pc/gawkmisc.pc

```

{% raw %}
574 | /* replacement of dlopen(). This limits a length of a base name up to 8
576 | void *os2_dlopen(const char *file, int mode)
580 |     return (dlopen)(os2_fixdllname(dll_file, file, sizeof(dll_file)), mode);
812 | dlopen (const char *file, int mode)
{% endraw %}

```
### doc/gawktexi.in

```

{% raw %}
32988 | that support the C @code{dlopen()} and @code{dlsym()}
{% endraw %}

```
### doc/gawk.info

```

{% raw %}
24423 | that support the C 'dlopen()' and 'dlsym()' functions.  This major node
{% endraw %}

```
### doc/gawk.texi

```

{% raw %}
34017 | that support the C @code{dlopen()} and @code{dlsym()}
{% endraw %}

```
### doc/it/gawktexi.in

```

{% raw %}
35800 | su sistemi che supportano le funzioni C @code{dlopen()} e @code{dlsym()}.
{% endraw %}

```