---
name: "ddd"
layout: package
next_package: sst-elements
previous_package: rngstreams
languages: ['bash']
---
## 3.3.12
2 / 953 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

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
2143 |       if test "$pass" = dlopen; then
2327 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2328 | 	      # If there is no dlopen support or we're linking statically,
2361 | 	dlopen=
2382 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2425 | 	# This library was specified with -dlopen.
2426 | 	if test "$pass" = dlopen; then
2428 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2432 | 	     test "$dlopen_support" != yes ||
2434 | 	    # If there is no dlname, no dlopen support or we're linking
2443 | 	fi # $pass = dlopen
2496 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2873 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2874 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
3031 |       if test "$pass" != dlopen; then
3133 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3200 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3845 | 	    $echo "*** a static module, that should work as long as the dlopening"
3846 | 	    $echo "*** application is linked with the -dlopen flag."
3864 | 	    $echo "*** or is declared to -dlopen it."
4278 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4412 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4413 | 	   test "$dlopen_self_static" = unknown; then
4414 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5766 | # The name that we can dlopen(3).
5789 | # Files to dlopen/dlpreopen
5790 | dlopen='$dlfiles'
6405 |     # Handle -dlopen flags immediately.
6434 | 	# Skip this library if it cannot be dlopened.
6461 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6821 |   -dlopen FILE      add the directory containing FILE to the library path
6823 | This mode sets the library path environment variable according to \`-dlopen'
6872 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6881 |   -module           build a library that can dlopened
{% endraw %}

```
### aclocal.m4

```

{% raw %}
214 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
925 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
928 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
984 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1013 | ])# _LT_AC_TRY_DLOPEN_SELF
1016 | # AC_LIBTOOL_DLOPEN_SELF
1018 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1020 | if test "x$enable_dlopen" != xyes; then
1021 |   enable_dlopen=unknown
1022 |   enable_dlopen_self=unknown
1023 |   enable_dlopen_self_static=unknown
1025 |   lt_cv_dlopen=no
1026 |   lt_cv_dlopen_libs=
1030 |     lt_cv_dlopen="load_add_on"
1031 |     lt_cv_dlopen_libs=
1032 |     lt_cv_dlopen_self=yes
1036 |     lt_cv_dlopen="LoadLibrary"
1037 |     lt_cv_dlopen_libs=
1041 |     lt_cv_dlopen="dlopen"
1042 |     lt_cv_dlopen_libs=
1047 |     AC_CHECK_LIB([dl], [dlopen],
1048 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1049 |     lt_cv_dlopen="dyld"
1050 |     lt_cv_dlopen_libs=
1051 |     lt_cv_dlopen_self=yes
1057 | 	  [lt_cv_dlopen="shl_load"],
1059 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1060 | 	[AC_CHECK_FUNC([dlopen],
1061 | 	      [lt_cv_dlopen="dlopen"],
1062 | 	  [AC_CHECK_LIB([dl], [dlopen],
1063 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1064 | 	    [AC_CHECK_LIB([svld], [dlopen],
1065 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1067 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1076 |   if test "x$lt_cv_dlopen" != xno; then
1077 |     enable_dlopen=yes
1079 |     enable_dlopen=no
1082 |   case $lt_cv_dlopen in
1083 |   dlopen)
1091 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1093 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1094 | 	  lt_cv_dlopen_self, [dnl
1095 | 	  _LT_AC_TRY_DLOPEN_SELF(
1096 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1097 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1100 |     if test "x$lt_cv_dlopen_self" = xyes; then
1102 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1103 |     	  lt_cv_dlopen_self_static, [dnl
1104 | 	  _LT_AC_TRY_DLOPEN_SELF(
1105 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1106 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1116 |   case $lt_cv_dlopen_self in
1117 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1118 |   *) enable_dlopen_self=unknown ;;
1121 |   case $lt_cv_dlopen_self_static in
1122 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1123 |   *) enable_dlopen_self_static=unknown ;;
1126 | ])# AC_LIBTOOL_DLOPEN_SELF
2036 | # AC_LIBTOOL_DLOPEN
2038 | # enable checks for dlopen support
2039 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2041 | ])# AC_LIBTOOL_DLOPEN
2839 | AC_LIBTOOL_DLOPEN_SELF
4556 | # Whether dlopen is supported.
4557 | dlopen_support=$enable_dlopen
4559 | # Whether dlopen of programs is supported.
4560 | dlopen_self=$enable_dlopen_self
4562 | # Whether dlopen of statically linked programs is supported.
4563 | dlopen_self_static=$enable_dlopen_self_static
4571 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```