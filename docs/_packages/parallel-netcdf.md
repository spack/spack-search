---
name: "parallel-netcdf"
layout: package
next_package: libzmq
previous_package: piranha
languages: ['bash']
---
## master
5 / 813 files match

 - [configure.ac](#configureac)
 - [m4/libtool.m4](#m4libtoolm4)
 - [benchmarks/FLASH-IO/m4/libtool.m4](#benchmarksflash-iom4libtoolm4)
 - [benchmarks/FLASH-IO/scripts/ltmain.sh](#benchmarksflash-ioscriptsltmainsh)
 - [scripts/ltmain.sh](#scriptsltmainsh)

### configure.ac

```

{% raw %}
416 | dnl LT_INIT([dlopen disable-shared])
417 | dnl LT_INIT([dlopen])
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1874 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1877 | m4_defun([_LT_TRY_DLOPEN_SELF],
1935 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1968 | ])# _LT_TRY_DLOPEN_SELF
1971 | # LT_SYS_DLOPEN_SELF
1973 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1975 | if test yes != "$enable_dlopen"; then
1976 |   enable_dlopen=unknown
1977 |   enable_dlopen_self=unknown
1978 |   enable_dlopen_self_static=unknown
1980 |   lt_cv_dlopen=no
1981 |   lt_cv_dlopen_libs=
1985 |     lt_cv_dlopen=load_add_on
1986 |     lt_cv_dlopen_libs=
1987 |     lt_cv_dlopen_self=yes
1991 |     lt_cv_dlopen=LoadLibrary
1992 |     lt_cv_dlopen_libs=
1996 |     lt_cv_dlopen=dlopen
1997 |     lt_cv_dlopen_libs=
2002 |     AC_CHECK_LIB([dl], [dlopen],
2003 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
2004 |     lt_cv_dlopen=dyld
2005 |     lt_cv_dlopen_libs=
2006 |     lt_cv_dlopen_self=yes
2013 |     lt_cv_dlopen=dlopen
2014 |     lt_cv_dlopen_libs=
2015 |     lt_cv_dlopen_self=no
2020 | 	  [lt_cv_dlopen=shl_load],
2022 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
2023 | 	[AC_CHECK_FUNC([dlopen],
2024 | 	      [lt_cv_dlopen=dlopen],
2025 | 	  [AC_CHECK_LIB([dl], [dlopen],
2026 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
2027 | 	    [AC_CHECK_LIB([svld], [dlopen],
2028 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
2030 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2039 |   if test no = "$lt_cv_dlopen"; then
2040 |     enable_dlopen=no
2042 |     enable_dlopen=yes
2045 |   case $lt_cv_dlopen in
2046 |   dlopen)
2054 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2056 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2057 | 	  lt_cv_dlopen_self, [dnl
2058 | 	  _LT_TRY_DLOPEN_SELF(
2059 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2060 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2063 |     if test yes = "$lt_cv_dlopen_self"; then
2065 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2066 | 	  lt_cv_dlopen_self_static, [dnl
2067 | 	  _LT_TRY_DLOPEN_SELF(
2068 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2069 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2079 |   case $lt_cv_dlopen_self in
2080 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2081 |   *) enable_dlopen_self=unknown ;;
2084 |   case $lt_cv_dlopen_self_static in
2085 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2086 |   *) enable_dlopen_self_static=unknown ;;
2089 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2090 | 	 [Whether dlopen is supported])
2091 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2092 | 	 [Whether dlopen of programs is supported])
2093 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2094 | 	 [Whether dlopen of statically linked programs is supported])
2095 | ])# LT_SYS_DLOPEN_SELF
2098 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2100 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6219 |     [Compiler flag to allow reflexive dlopens])
6332 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### benchmarks/FLASH-IO/m4/libtool.m4

```

{% raw %}
1874 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1877 | m4_defun([_LT_TRY_DLOPEN_SELF],
1935 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1968 | ])# _LT_TRY_DLOPEN_SELF
1971 | # LT_SYS_DLOPEN_SELF
1973 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1975 | if test yes != "$enable_dlopen"; then
1976 |   enable_dlopen=unknown
1977 |   enable_dlopen_self=unknown
1978 |   enable_dlopen_self_static=unknown
1980 |   lt_cv_dlopen=no
1981 |   lt_cv_dlopen_libs=
1985 |     lt_cv_dlopen=load_add_on
1986 |     lt_cv_dlopen_libs=
1987 |     lt_cv_dlopen_self=yes
1991 |     lt_cv_dlopen=LoadLibrary
1992 |     lt_cv_dlopen_libs=
1996 |     lt_cv_dlopen=dlopen
1997 |     lt_cv_dlopen_libs=
2002 |     AC_CHECK_LIB([dl], [dlopen],
2003 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
2004 |     lt_cv_dlopen=dyld
2005 |     lt_cv_dlopen_libs=
2006 |     lt_cv_dlopen_self=yes
2013 |     lt_cv_dlopen=dlopen
2014 |     lt_cv_dlopen_libs=
2015 |     lt_cv_dlopen_self=no
2020 | 	  [lt_cv_dlopen=shl_load],
2022 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
2023 | 	[AC_CHECK_FUNC([dlopen],
2024 | 	      [lt_cv_dlopen=dlopen],
2025 | 	  [AC_CHECK_LIB([dl], [dlopen],
2026 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
2027 | 	    [AC_CHECK_LIB([svld], [dlopen],
2028 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
2030 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2039 |   if test no = "$lt_cv_dlopen"; then
2040 |     enable_dlopen=no
2042 |     enable_dlopen=yes
2045 |   case $lt_cv_dlopen in
2046 |   dlopen)
2054 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2056 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2057 | 	  lt_cv_dlopen_self, [dnl
2058 | 	  _LT_TRY_DLOPEN_SELF(
2059 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2060 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2063 |     if test yes = "$lt_cv_dlopen_self"; then
2065 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2066 | 	  lt_cv_dlopen_self_static, [dnl
2067 | 	  _LT_TRY_DLOPEN_SELF(
2068 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2069 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2079 |   case $lt_cv_dlopen_self in
2080 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2081 |   *) enable_dlopen_self=unknown ;;
2084 |   case $lt_cv_dlopen_self_static in
2085 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2086 |   *) enable_dlopen_self_static=unknown ;;
2089 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2090 | 	 [Whether dlopen is supported])
2091 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2092 | 	 [Whether dlopen of programs is supported])
2093 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2094 | 	 [Whether dlopen of statically linked programs is supported])
2095 | ])# LT_SYS_DLOPEN_SELF
2098 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2100 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6219 |     [Compiler flag to allow reflexive dlopens])
6332 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### benchmarks/FLASH-IO/scripts/ltmain.sh

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
7882 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7928 | 	# This library was specified with -dlopen.
7929 | 	if test dlopen = "$pass"; then
7931 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7933 | 	     test yes != "$dlopen_support" ||
7936 | 	    # If there is no dlname, no dlopen support or we're linking
7945 | 	fi # $pass = dlopen
8001 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8003 | 	      # We recover the dlopen module name by 'saving' the la file
8027 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8156 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8157 | 	  dlopenmodule=
8160 | 	      dlopenmodule=$dlpremoduletest
8164 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8261 | 		    # if the lib is a (non-dlopened) module then we cannot
8265 | 		      if test "X$dlopenmodule" != "X$lib"; then
8417 | 	      echo "*** a static module, that should work as long as the dlopening application"
8418 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8562 |       if test dlopen != "$pass"; then
8692 | 	func_warning "'-dlopen' is ignored for archives"
8759 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9454 | 	    echo "*** a static module, that should work as long as the dlopening"
9455 | 	    echo "*** application is linked with the -dlopen flag."
9473 | 	    echo "*** or is declared to -dlopen it."
10092 | 	func_warning "'-dlopen' is ignored for objects"
10212 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10213 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10894 | # The name that we can dlopen(3).
10923 | # Files to dlopen/dlpreopen
10924 | dlopen='$dlfiles'
{% endraw %}

```
### scripts/ltmain.sh

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
7882 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7928 | 	# This library was specified with -dlopen.
7929 | 	if test dlopen = "$pass"; then
7931 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7933 | 	     test yes != "$dlopen_support" ||
7936 | 	    # If there is no dlname, no dlopen support or we're linking
7945 | 	fi # $pass = dlopen
8001 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8003 | 	      # We recover the dlopen module name by 'saving' the la file
8027 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8156 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8157 | 	  dlopenmodule=
8160 | 	      dlopenmodule=$dlpremoduletest
8164 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8261 | 		    # if the lib is a (non-dlopened) module then we cannot
8265 | 		      if test "X$dlopenmodule" != "X$lib"; then
8417 | 	      echo "*** a static module, that should work as long as the dlopening application"
8418 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8562 |       if test dlopen != "$pass"; then
8692 | 	func_warning "'-dlopen' is ignored for archives"
8759 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9454 | 	    echo "*** a static module, that should work as long as the dlopening"
9455 | 	    echo "*** application is linked with the -dlopen flag."
9473 | 	    echo "*** or is declared to -dlopen it."
10092 | 	func_warning "'-dlopen' is ignored for objects"
10212 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10213 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10894 | # The name that we can dlopen(3).
10923 | # Files to dlopen/dlpreopen
10924 | dlopen='$dlfiles'
{% endraw %}

```