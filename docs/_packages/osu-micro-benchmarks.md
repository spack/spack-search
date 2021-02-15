---
name: "osu-micro-benchmarks"
layout: package
next_package: netcdf-fortran
previous_package: py-numpy
languages: ['bash']
---
## 5.6.3
5 / 109 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)
 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [autom4te.cache/output.1](#autom4tecacheoutput1)
 - [autom4te.cache/traces.0](#autom4tecachetraces0)

### ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1758 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1761 | m4_defun([_LT_TRY_DLOPEN_SELF],
1819 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1852 | ])# _LT_TRY_DLOPEN_SELF
1855 | # LT_SYS_DLOPEN_SELF
1857 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1859 | if test "x$enable_dlopen" != xyes; then
1860 |   enable_dlopen=unknown
1861 |   enable_dlopen_self=unknown
1862 |   enable_dlopen_self_static=unknown
1864 |   lt_cv_dlopen=no
1865 |   lt_cv_dlopen_libs=
1869 |     lt_cv_dlopen="load_add_on"
1870 |     lt_cv_dlopen_libs=
1871 |     lt_cv_dlopen_self=yes
1875 |     lt_cv_dlopen="LoadLibrary"
1876 |     lt_cv_dlopen_libs=
1880 |     lt_cv_dlopen="dlopen"
1881 |     lt_cv_dlopen_libs=
1886 |     AC_CHECK_LIB([dl], [dlopen],
1887 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1888 |     lt_cv_dlopen="dyld"
1889 |     lt_cv_dlopen_libs=
1890 |     lt_cv_dlopen_self=yes
1896 | 	  [lt_cv_dlopen="shl_load"],
1898 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1899 | 	[AC_CHECK_FUNC([dlopen],
1900 | 	      [lt_cv_dlopen="dlopen"],
1901 | 	  [AC_CHECK_LIB([dl], [dlopen],
1902 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1903 | 	    [AC_CHECK_LIB([svld], [dlopen],
1904 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1906 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1915 |   if test "x$lt_cv_dlopen" != xno; then
1916 |     enable_dlopen=yes
1918 |     enable_dlopen=no
1921 |   case $lt_cv_dlopen in
1922 |   dlopen)
1930 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1932 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1933 | 	  lt_cv_dlopen_self, [dnl
1934 | 	  _LT_TRY_DLOPEN_SELF(
1935 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1936 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1939 |     if test "x$lt_cv_dlopen_self" = xyes; then
1941 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1942 | 	  lt_cv_dlopen_self_static, [dnl
1943 | 	  _LT_TRY_DLOPEN_SELF(
1944 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1945 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1955 |   case $lt_cv_dlopen_self in
1956 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1957 |   *) enable_dlopen_self=unknown ;;
1960 |   case $lt_cv_dlopen_self_static in
1961 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1962 |   *) enable_dlopen_self_static=unknown ;;
1965 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1966 | 	 [Whether dlopen is supported])
1967 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1968 | 	 [Whether dlopen of programs is supported])
1969 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1970 | 	 [Whether dlopen of statically linked programs is supported])
1971 | ])# LT_SYS_DLOPEN_SELF
1974 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1976 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5676 |     [Compiler flag to allow reflexive dlopens])
5785 |   LT_SYS_DLOPEN_SELF
8057 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8089 | # dlopen
8091 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8094 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8095 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8098 | put the `dlopen' option into LT_INIT's first parameter.])
8102 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8563 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### autom4te.cache/output.0

```

{% raw %}
7566 |         enable_dlopen=no
10938 |   if test "x$enable_dlopen" != xyes; then
10939 |   enable_dlopen=unknown
10940 |   enable_dlopen_self=unknown
10941 |   enable_dlopen_self_static=unknown
10943 |   lt_cv_dlopen=no
10944 |   lt_cv_dlopen_libs=
10948 |     lt_cv_dlopen="load_add_on"
10949 |     lt_cv_dlopen_libs=
10950 |     lt_cv_dlopen_self=yes
10954 |     lt_cv_dlopen="LoadLibrary"
10955 |     lt_cv_dlopen_libs=
10959 |     lt_cv_dlopen="dlopen"
10960 |     lt_cv_dlopen_libs=
10965 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10966 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10967 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10981 | char dlopen ();
10985 | return dlopen ();
10991 |   ac_cv_lib_dl_dlopen=yes
10993 |   ac_cv_lib_dl_dlopen=no
10999 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11000 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11001 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11002 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11005 |     lt_cv_dlopen="dyld"
11006 |     lt_cv_dlopen_libs=
11007 |     lt_cv_dlopen_self=yes
11016 |   lt_cv_dlopen="shl_load"
11055 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
11057 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
11058 | if test "x$ac_cv_func_dlopen" = xyes; then :
11059 |   lt_cv_dlopen="dlopen"
11061 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11062 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11063 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11077 | char dlopen ();
11081 | return dlopen ();
11087 |   ac_cv_lib_dl_dlopen=yes
11089 |   ac_cv_lib_dl_dlopen=no
11095 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11096 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11097 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11098 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11100 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
11101 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11102 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11116 | char dlopen ();
11120 | return dlopen ();
11126 |   ac_cv_lib_svld_dlopen=yes
11128 |   ac_cv_lib_svld_dlopen=no
11134 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11135 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11136 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11137 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
11176 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
11197 |   if test "x$lt_cv_dlopen" != xno; then
11198 |     enable_dlopen=yes
11200 |     enable_dlopen=no
11203 |   case $lt_cv_dlopen in
11204 |   dlopen)
11212 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11214 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11215 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11216 | if ${lt_cv_dlopen_self+:} false; then :
11220 |   lt_cv_dlopen_self=cross
11275 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11302 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
11303 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
11304 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
11308 |     lt_cv_dlopen_self=no
11315 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
11316 | $as_echo "$lt_cv_dlopen_self" >&6; }
11318 |     if test "x$lt_cv_dlopen_self" = xyes; then
11320 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
11321 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
11322 | if ${lt_cv_dlopen_self_static+:} false; then :
11326 |   lt_cv_dlopen_self_static=cross
11381 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11408 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
11409 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
11410 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
11414 |     lt_cv_dlopen_self_static=no
11421 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
11422 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
11431 |   case $lt_cv_dlopen_self in
11432 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
11433 |   *) enable_dlopen_self=unknown ;;
11436 |   case $lt_cv_dlopen_self_static in
11437 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
11438 |   *) enable_dlopen_self_static=unknown ;;
17222 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
17223 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
17224 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
18297 | # Whether dlopen is supported.
18298 | dlopen_support=$enable_dlopen
18300 | # Whether dlopen of programs is supported.
18301 | dlopen_self=$enable_dlopen_self
18303 | # Whether dlopen of statically linked programs is supported.
18304 | dlopen_self_static=$enable_dlopen_self_static
18348 | # Compiler flag to allow reflexive dlopens.
18690 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.1

```

{% raw %}
7566 |         enable_dlopen=no
10934 |   if test "x$enable_dlopen" != xyes; then
10935 |   enable_dlopen=unknown
10936 |   enable_dlopen_self=unknown
10937 |   enable_dlopen_self_static=unknown
10939 |   lt_cv_dlopen=no
10940 |   lt_cv_dlopen_libs=
10944 |     lt_cv_dlopen="load_add_on"
10945 |     lt_cv_dlopen_libs=
10946 |     lt_cv_dlopen_self=yes
10950 |     lt_cv_dlopen="LoadLibrary"
10951 |     lt_cv_dlopen_libs=
10955 |     lt_cv_dlopen="dlopen"
10956 |     lt_cv_dlopen_libs=
10961 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10962 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10963 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10977 | char dlopen ();
10981 | return dlopen ();
10987 |   ac_cv_lib_dl_dlopen=yes
10989 |   ac_cv_lib_dl_dlopen=no
10995 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10996 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10997 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
10998 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11001 |     lt_cv_dlopen="dyld"
11002 |     lt_cv_dlopen_libs=
11003 |     lt_cv_dlopen_self=yes
11012 |   lt_cv_dlopen="shl_load"
11051 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
11053 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
11054 | if test "x$ac_cv_func_dlopen" = xyes; then :
11055 |   lt_cv_dlopen="dlopen"
11057 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11058 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11059 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11073 | char dlopen ();
11077 | return dlopen ();
11083 |   ac_cv_lib_dl_dlopen=yes
11085 |   ac_cv_lib_dl_dlopen=no
11091 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11092 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11093 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11094 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11096 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
11097 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11098 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11112 | char dlopen ();
11116 | return dlopen ();
11122 |   ac_cv_lib_svld_dlopen=yes
11124 |   ac_cv_lib_svld_dlopen=no
11130 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11131 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11132 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11133 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
11172 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
11193 |   if test "x$lt_cv_dlopen" != xno; then
11194 |     enable_dlopen=yes
11196 |     enable_dlopen=no
11199 |   case $lt_cv_dlopen in
11200 |   dlopen)
11208 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11210 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11211 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11212 | if ${lt_cv_dlopen_self+:} false; then :
11216 |   lt_cv_dlopen_self=cross
11271 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11298 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
11299 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
11300 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
11304 |     lt_cv_dlopen_self=no
11311 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
11312 | $as_echo "$lt_cv_dlopen_self" >&6; }
11314 |     if test "x$lt_cv_dlopen_self" = xyes; then
11316 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
11317 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
11318 | if ${lt_cv_dlopen_self_static+:} false; then :
11322 |   lt_cv_dlopen_self_static=cross
11377 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11404 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
11405 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
11406 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
11410 |     lt_cv_dlopen_self_static=no
11417 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
11418 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
11427 |   case $lt_cv_dlopen_self in
11428 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
11429 |   *) enable_dlopen_self=unknown ;;
11432 |   case $lt_cv_dlopen_self_static in
11433 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
11434 |   *) enable_dlopen_self_static=unknown ;;
17218 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
17219 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
17220 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
18293 | # Whether dlopen is supported.
18294 | dlopen_support=$enable_dlopen
18296 | # Whether dlopen of programs is supported.
18297 | dlopen_self=$enable_dlopen_self
18299 | # Whether dlopen of statically linked programs is supported.
18300 | dlopen_self_static=$enable_dlopen_self_static
18344 | # Compiler flag to allow reflexive dlopens.
18686 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.0

```

{% raw %}
474 | m4trace:/usr/share/aclocal/libtool.m4:1844: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
475 | if test "x$enable_dlopen" != xyes; then
476 |   enable_dlopen=unknown
477 |   enable_dlopen_self=unknown
478 |   enable_dlopen_self_static=unknown
480 |   lt_cv_dlopen=no
481 |   lt_cv_dlopen_libs=
485 |     lt_cv_dlopen="load_add_on"
486 |     lt_cv_dlopen_libs=
487 |     lt_cv_dlopen_self=yes
491 |     lt_cv_dlopen="LoadLibrary"
492 |     lt_cv_dlopen_libs=
496 |     lt_cv_dlopen="dlopen"
497 |     lt_cv_dlopen_libs=
502 |     AC_CHECK_LIB([dl], [dlopen],
503 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
504 |     lt_cv_dlopen="dyld"
505 |     lt_cv_dlopen_libs=
506 |     lt_cv_dlopen_self=yes
512 | 	  [lt_cv_dlopen="shl_load"],
514 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
515 | 	[AC_CHECK_FUNC([dlopen],
516 | 	      [lt_cv_dlopen="dlopen"],
517 | 	  [AC_CHECK_LIB([dl], [dlopen],
518 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
519 | 	    [AC_CHECK_LIB([svld], [dlopen],
520 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
522 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
531 |   if test "x$lt_cv_dlopen" != xno; then
532 |     enable_dlopen=yes
534 |     enable_dlopen=no
537 |   case $lt_cv_dlopen in
538 |   dlopen)
546 |     LIBS="$lt_cv_dlopen_libs $LIBS"
548 |     AC_CACHE_CHECK([whether a program can dlopen itself],
549 | 	  lt_cv_dlopen_self, [dnl
550 | 	  _LT_TRY_DLOPEN_SELF(
551 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
552 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
555 |     if test "x$lt_cv_dlopen_self" = xyes; then
557 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
558 | 	  lt_cv_dlopen_self_static, [dnl
559 | 	  _LT_TRY_DLOPEN_SELF(
560 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
561 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
571 |   case $lt_cv_dlopen_self in
572 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
573 |   *) enable_dlopen_self=unknown ;;
576 |   case $lt_cv_dlopen_self_static in
577 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
578 |   *) enable_dlopen_self_static=unknown ;;
581 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
582 | 	 [Whether dlopen is supported])
583 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
584 | 	 [Whether dlopen of programs is supported])
585 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
586 | 	 [Whether dlopen of statically linked programs is supported])
588 | m4trace:/usr/share/aclocal/libtool.m4:1961: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
589 | m4trace:/usr/share/aclocal/libtool.m4:1961: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
591 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1065 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1109 | eval "LTDLOPEN=\"$libname_spec\""
1110 | AC_SUBST([LTDLOPEN])
1112 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1113 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1114 |   [lt_cv_sys_dlopen_deplibs],
1115 |   [# PORTME does your system automatically load deplibs for dlopen?
1119 |   lt_cv_sys_dlopen_deplibs=unknown
1124 |     lt_cv_sys_dlopen_deplibs=unknown
1127 |     lt_cv_sys_dlopen_deplibs=yes
1132 |       lt_cv_sys_dlopen_deplibs=no
1139 |     lt_cv_sys_dlopen_deplibs=yes
1142 |     lt_cv_sys_dlopen_deplibs=yes
1146 |     lt_cv_sys_dlopen_deplibs=yes
1149 |     lt_cv_sys_dlopen_deplibs=yes
1152 |     lt_cv_sys_dlopen_deplibs=yes
1157 |     lt_cv_sys_dlopen_deplibs=unknown
1161 |     # at 6.2 and later dlopen does load deplibs.
1162 |     lt_cv_sys_dlopen_deplibs=yes
1165 |     lt_cv_sys_dlopen_deplibs=yes
1168 |     lt_cv_sys_dlopen_deplibs=yes
1171 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1174 |     lt_cv_sys_dlopen_deplibs=no
1177 |     # dlopen *does* load deplibs and with the right loader patch applied
1183 |     lt_cv_sys_dlopen_deplibs=unknown
1190 |     lt_cv_sys_dlopen_deplibs=yes
1193 |     lt_cv_sys_dlopen_deplibs=yes
1196 |     lt_cv_sys_dlopen_deplibs=yes
1199 |     libltdl_cv_sys_dlopen_deplibs=yes
1203 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
1204 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1205 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1208 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1209 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1211 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1277 | LIBADD_DLOPEN=
1278 | AC_SEARCH_LIBS([dlopen], [dl],
1281 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
1282 | 	  LIBADD_DLOPEN="-ldl"
1284 | 	libltdl_cv_lib_dl_dlopen="yes"
1285 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1289 |     ]], [[dlopen(0, 0);]])],
1292 | 	    libltdl_cv_func_dlopen="yes"
1293 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1294 | 	[AC_CHECK_LIB([svld], [dlopen],
1297 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
1298 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1299 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
1302 |   LIBS="$LIBS $LIBADD_DLOPEN"
1306 | AC_SUBST([LIBADD_DLOPEN])
1312 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1316 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1326 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1329 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1333 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1340 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
1356 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
1405 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
1406 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
1411 |           LIBS="$LIBS $LIBADD_DLOPEN"
1412 | 	  _LT_TRY_DLOPEN_SELF(
1430 | m4trace:/usr/share/aclocal/ltoptions.m4:111: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1433 | put the `dlopen' option into LT_INIT's first parameter.])
1435 | m4trace:/usr/share/aclocal/ltoptions.m4:111: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1437 | _LT_SET_OPTION([LT_INIT], [dlopen])
1440 | put the `dlopen' option into LT_INIT's first parameter.])
1532 | m4trace:/usr/share/aclocal/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2484 | m4trace:configure.ac:9: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```