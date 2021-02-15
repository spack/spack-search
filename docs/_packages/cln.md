---
name: "cln"
layout: package
next_package: ghostscript
previous_package: librdkafka
languages: ['bash']
---
## 1.2.2
2 / 1338 files match

 - [m4/libtool.m4](#m4libtoolm4)
 - [autoconf/ltmain.sh](#autoconfltmainsh)

### m4/libtool.m4

```

{% raw %}
200 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
911 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
914 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
970 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
999 | ])# _LT_AC_TRY_DLOPEN_SELF
1002 | # AC_LIBTOOL_DLOPEN_SELF
1004 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1006 | if test "x$enable_dlopen" != xyes; then
1007 |   enable_dlopen=unknown
1008 |   enable_dlopen_self=unknown
1009 |   enable_dlopen_self_static=unknown
1011 |   lt_cv_dlopen=no
1012 |   lt_cv_dlopen_libs=
1016 |     lt_cv_dlopen="load_add_on"
1017 |     lt_cv_dlopen_libs=
1018 |     lt_cv_dlopen_self=yes
1022 |     lt_cv_dlopen="LoadLibrary"
1023 |     lt_cv_dlopen_libs=
1027 |     lt_cv_dlopen="dlopen"
1028 |     lt_cv_dlopen_libs=
1033 |     AC_CHECK_LIB([dl], [dlopen],
1034 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1035 |     lt_cv_dlopen="dyld"
1036 |     lt_cv_dlopen_libs=
1037 |     lt_cv_dlopen_self=yes
1043 | 	  [lt_cv_dlopen="shl_load"],
1045 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1046 | 	[AC_CHECK_FUNC([dlopen],
1047 | 	      [lt_cv_dlopen="dlopen"],
1048 | 	  [AC_CHECK_LIB([dl], [dlopen],
1049 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1050 | 	    [AC_CHECK_LIB([svld], [dlopen],
1051 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1053 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1062 |   if test "x$lt_cv_dlopen" != xno; then
1063 |     enable_dlopen=yes
1065 |     enable_dlopen=no
1068 |   case $lt_cv_dlopen in
1069 |   dlopen)
1077 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1079 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1080 | 	  lt_cv_dlopen_self, [dnl
1081 | 	  _LT_AC_TRY_DLOPEN_SELF(
1082 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1083 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1086 |     if test "x$lt_cv_dlopen_self" = xyes; then
1088 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1089 |     	  lt_cv_dlopen_self_static, [dnl
1090 | 	  _LT_AC_TRY_DLOPEN_SELF(
1091 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1092 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1102 |   case $lt_cv_dlopen_self in
1103 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1104 |   *) enable_dlopen_self=unknown ;;
1107 |   case $lt_cv_dlopen_self_static in
1108 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1109 |   *) enable_dlopen_self_static=unknown ;;
1112 | ])# AC_LIBTOOL_DLOPEN_SELF
2010 | # AC_LIBTOOL_DLOPEN
2012 | # enable checks for dlopen support
2013 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2015 | ])# AC_LIBTOOL_DLOPEN
2817 | AC_LIBTOOL_DLOPEN_SELF
4542 | # Whether dlopen is supported.
4543 | dlopen_support=$enable_dlopen
4545 | # Whether dlopen of programs is supported.
4546 | dlopen_self=$enable_dlopen_self
4548 | # Whether dlopen of statically linked programs is supported.
4549 | dlopen_self_static=$enable_dlopen_self_static
4557 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autoconf/ltmain.sh

```bash

{% raw %}
557 |   -dlopen)
558 |     prevopt="-dlopen"
642 |   # Only execute mode is allowed to have -dlopen flags.
644 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1185 | 	    dlopen_self=$dlopen_self_static
1191 | 	    dlopen_self=$dlopen_self_static
1197 | 	    dlopen_self=$dlopen_self_static
1254 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1346 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1503 |       -dlopen)
1896 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1969 | 	  # This library was specified with -dlopen.
2110 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2122 | 	passes="conv scan dlopen dlpreopen link"
2135 | 	dlopen) libs="$dlfiles" ;;
2140 |       if test "$pass" = dlopen; then
2324 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2325 | 	      # If there is no dlopen support or we're linking statically,
2358 | 	dlopen=
2379 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2422 | 	# This library was specified with -dlopen.
2423 | 	if test "$pass" = dlopen; then
2425 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2429 | 	     test "$dlopen_support" != yes ||
2431 | 	    # If there is no dlname, no dlopen support or we're linking
2440 | 	fi # $pass = dlopen
2493 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2870 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2871 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
3028 |       if test "$pass" != dlopen; then
3130 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3197 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3837 | 	    $echo "*** a static module, that should work as long as the dlopening"
3838 | 	    $echo "*** application is linked with the -dlopen flag."
3856 | 	    $echo "*** or is declared to -dlopen it."
4270 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4404 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4405 | 	   test "$dlopen_self_static" = unknown; then
4406 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5758 | # The name that we can dlopen(3).
5781 | # Files to dlopen/dlpreopen
5782 | dlopen='$dlfiles'
6397 |     # Handle -dlopen flags immediately.
6426 | 	# Skip this library if it cannot be dlopened.
6453 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6813 |   -dlopen FILE      add the directory containing FILE to the library path
6815 | This mode sets the library path environment variable according to \`-dlopen'
6864 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6873 |   -module           build a library that can dlopened
{% endraw %}

```