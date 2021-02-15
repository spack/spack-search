---
name: "lftp"
layout: package
next_package: libsamplerate
previous_package: heaptrack
languages: ['cpp', 'bash']
---
## 4.8.1
9 / 797 files match

 - [configure.ac](#configureac)
 - [README.modules](#readmemodules)
 - [src/module.cc](#srcmodulecc)
 - [lib/config.h.in](#libconfighin)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/lib-link.m4](#m4lib-linkm4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)
 - [doc/lftp.1](#doclftp1)

### configure.ac

```

{% raw %}
235 | LT_INIT([dlopen])
249 | AC_SEARCH_LIBS([dlopen],[dl],[AC_DEFINE(HAVE_DLOPEN, 1, [have dlopen])])
{% endraw %}

```
### README.modules

```

{% raw %}
13 | Module is a shared object, after loading it with dlopen(3) lftp does
22 | Note: function _init of a module is called automatically by dlopen. It can
{% endraw %}

```
### src/module.cc

```cpp

{% raw %}
36 | # define DLOPEN_FLAGS RTLD_NOW|RTLD_GLOBAL
39 | # define DLOPEN_FLAGS 1
42 | # define DLOPEN_FLAGS_LAZY RTLD_LAZY|RTLD_GLOBAL
44 | # define DLOPEN_FLAGS_LAZY DLOPEN_FLAGS
116 | /* dlopen can take a file without extension and automatically do the
118 |  * stat before the dlopen call, hence need some help here */
148 | #ifdef HAVE_DLOPEN
175 |    map=dlopen(fullpath,DLOPEN_FLAGS);  // LAZY?
199 | #else // !HAVE_DLOPEN
206 | #ifdef HAVE_DLOPEN
215 | #if defined(HAVE_DLOPEN) && defined(RTLD_DEFAULT)
{% endraw %}

```
### lib/config.h.in

```

{% raw %}
577 | /* have dlopen */
578 | #undef HAVE_DLOPEN
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1794 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1797 | m4_defun([_LT_TRY_DLOPEN_SELF],
1855 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1888 | ])# _LT_TRY_DLOPEN_SELF
1891 | # LT_SYS_DLOPEN_SELF
1893 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1895 | if test yes != "$enable_dlopen"; then
1896 |   enable_dlopen=unknown
1897 |   enable_dlopen_self=unknown
1898 |   enable_dlopen_self_static=unknown
1900 |   lt_cv_dlopen=no
1901 |   lt_cv_dlopen_libs=
1905 |     lt_cv_dlopen=load_add_on
1906 |     lt_cv_dlopen_libs=
1907 |     lt_cv_dlopen_self=yes
1911 |     lt_cv_dlopen=LoadLibrary
1912 |     lt_cv_dlopen_libs=
1916 |     lt_cv_dlopen=dlopen
1917 |     lt_cv_dlopen_libs=
1922 |     AC_CHECK_LIB([dl], [dlopen],
1923 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1924 |     lt_cv_dlopen=dyld
1925 |     lt_cv_dlopen_libs=
1926 |     lt_cv_dlopen_self=yes
1933 |     lt_cv_dlopen=dlopen
1934 |     lt_cv_dlopen_libs=
1935 |     lt_cv_dlopen_self=no
1940 | 	  [lt_cv_dlopen=shl_load],
1942 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1943 | 	[AC_CHECK_FUNC([dlopen],
1944 | 	      [lt_cv_dlopen=dlopen],
1945 | 	  [AC_CHECK_LIB([dl], [dlopen],
1946 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1947 | 	    [AC_CHECK_LIB([svld], [dlopen],
1948 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1950 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1959 |   if test no = "$lt_cv_dlopen"; then
1960 |     enable_dlopen=no
1962 |     enable_dlopen=yes
1965 |   case $lt_cv_dlopen in
1966 |   dlopen)
1974 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1976 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1977 | 	  lt_cv_dlopen_self, [dnl
1978 | 	  _LT_TRY_DLOPEN_SELF(
1979 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1980 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1983 |     if test yes = "$lt_cv_dlopen_self"; then
1985 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1986 | 	  lt_cv_dlopen_self_static, [dnl
1987 | 	  _LT_TRY_DLOPEN_SELF(
1988 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1989 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1999 |   case $lt_cv_dlopen_self in
2000 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2001 |   *) enable_dlopen_self=unknown ;;
2004 |   case $lt_cv_dlopen_self_static in
2005 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2006 |   *) enable_dlopen_self_static=unknown ;;
2009 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2010 | 	 [Whether dlopen is supported])
2011 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2012 | 	 [Whether dlopen of programs is supported])
2013 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2014 | 	 [Whether dlopen of statically linked programs is supported])
2015 | ])# LT_SYS_DLOPEN_SELF
2018 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2020 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5785 |     [Compiler flag to allow reflexive dlopens])
5898 |   LT_SYS_DLOPEN_SELF
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
114 | put the 'dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### m4/lib-link.m4

```

{% raw %}
518 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### build-aux/ltmain.sh

```bash

{% raw %}
2161 |     opt_dlopen=
2222 |         --dlopen|-dlopen)
2223 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2337 |       # Only execute mode is allowed to have -dlopen flags.
2338 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2339 |         func_error "unrecognized option '-dlopen'"
3557 |   -dlopen FILE      add the directory containing FILE to the library path
3559 | This mode sets the library path environment variable according to '-dlopen'
3614 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3623 |   -module           build a library that can dlopened
3730 |     # Handle -dlopen flags immediately.
3731 |     for file in $opt_dlopen; do
3750 | 	# Skip this library if it cannot be dlopened.
3777 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6439 | 	    dlopen_self=$dlopen_self_static
6445 | 	    dlopen_self=$dlopen_self_static
6451 | 	    dlopen_self=$dlopen_self_static
6509 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6599 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6761 |       -dlopen)
7170 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7238 | 	  # This library was specified with -dlopen.
7355 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7366 | 	passes="conv scan dlopen dlpreopen link"
7392 | 	dlopen) libs=$dlfiles ;;
7420 |       if test dlopen = "$pass"; then
7640 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7641 | 	      # If there is no dlopen support or we're linking statically,
7669 | 	dlopen=
7699 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7745 | 	# This library was specified with -dlopen.
7746 | 	if test dlopen = "$pass"; then
7748 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7750 | 	     test yes != "$dlopen_support" ||
7753 | 	    # If there is no dlname, no dlopen support or we're linking
7762 | 	fi # $pass = dlopen
7818 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7820 | 	      # We recover the dlopen module name by 'saving' the la file
7844 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
7973 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
7974 | 	  dlopenmodule=
7977 | 	      dlopenmodule=$dlpremoduletest
7981 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8078 | 		    # if the lib is a (non-dlopened) module then we cannot
8082 | 		      if test "X$dlopenmodule" != "X$lib"; then
8234 | 	      echo "*** a static module, that should work as long as the dlopening application"
8235 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8379 |       if test dlopen != "$pass"; then
8478 | 	func_warning "'-dlopen' is ignored for archives"
8545 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9233 | 	    echo "*** a static module, that should work as long as the dlopening"
9234 | 	    echo "*** application is linked with the -dlopen flag."
9252 | 	    echo "*** or is declared to -dlopen it."
9864 | 	func_warning "'-dlopen' is ignored for objects"
9982 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
9983 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10664 | # The name that we can dlopen(3).
10693 | # Files to dlopen/dlpreopen
10694 | dlopen='$dlfiles'
{% endraw %}

```
### doc/lftp.1

```

{% raw %}
799 | Load given module using \fBdlopen\fR(3) function. If module name does not contain
{% endraw %}

```