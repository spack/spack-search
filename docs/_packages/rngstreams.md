---
name: "rngstreams"
layout: package
next_package: ddd
previous_package: neovim
languages: ['bash']
---
## 1.0.1
2 / 32 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
571 |   -dlopen)
572 |     prevopt="-dlopen"
656 |   # Only execute mode is allowed to have -dlopen flags.
658 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1199 | 	    dlopen_self=$dlopen_self_static
1205 | 	    dlopen_self=$dlopen_self_static
1211 | 	    dlopen_self=$dlopen_self_static
1268 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1360 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1517 |       -dlopen)
1910 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1983 | 	  # This library was specified with -dlopen.
2124 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2136 | 	passes="conv scan dlopen dlpreopen link"
2149 | 	dlopen) libs="$dlfiles" ;;
2154 |       if test "$pass" = dlopen; then
2338 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2339 | 	      # If there is no dlopen support or we're linking statically,
2372 | 	dlopen=
2393 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2436 | 	# This library was specified with -dlopen.
2437 | 	if test "$pass" = dlopen; then
2439 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2443 | 	     test "$dlopen_support" != yes ||
2445 | 	    # If there is no dlname, no dlopen support or we're linking
2454 | 	fi # $pass = dlopen
2507 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2884 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2885 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
3042 |       if test "$pass" != dlopen; then
3144 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3211 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3851 | 	    $echo "*** a static module, that should work as long as the dlopening"
3852 | 	    $echo "*** application is linked with the -dlopen flag."
3870 | 	    $echo "*** or is declared to -dlopen it."
4284 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4418 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4419 | 	   test "$dlopen_self_static" = unknown; then
4420 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5777 | # The name that we can dlopen(3).
5800 | # Files to dlopen/dlpreopen
5801 | dlopen='$dlfiles'
6416 |     # Handle -dlopen flags immediately.
6445 | 	# Skip this library if it cannot be dlopened.
6472 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6832 |   -dlopen FILE      add the directory containing FILE to the library path
6834 | This mode sets the library path environment variable according to \`-dlopen'
6883 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6892 |   -module           build a library that can dlopened
{% endraw %}

```
### aclocal.m4

```

{% raw %}
214 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
968 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
971 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
1027 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1056 | ])# _LT_AC_TRY_DLOPEN_SELF
1059 | # AC_LIBTOOL_DLOPEN_SELF
1061 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1063 | if test "x$enable_dlopen" != xyes; then
1064 |   enable_dlopen=unknown
1065 |   enable_dlopen_self=unknown
1066 |   enable_dlopen_self_static=unknown
1068 |   lt_cv_dlopen=no
1069 |   lt_cv_dlopen_libs=
1073 |     lt_cv_dlopen="load_add_on"
1074 |     lt_cv_dlopen_libs=
1075 |     lt_cv_dlopen_self=yes
1079 |     lt_cv_dlopen="LoadLibrary"
1080 |     lt_cv_dlopen_libs=
1084 |     lt_cv_dlopen="dlopen"
1085 |     lt_cv_dlopen_libs=
1090 |     AC_CHECK_LIB([dl], [dlopen],
1091 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1092 |     lt_cv_dlopen="dyld"
1093 |     lt_cv_dlopen_libs=
1094 |     lt_cv_dlopen_self=yes
1100 | 	  [lt_cv_dlopen="shl_load"],
1102 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1103 | 	[AC_CHECK_FUNC([dlopen],
1104 | 	      [lt_cv_dlopen="dlopen"],
1105 | 	  [AC_CHECK_LIB([dl], [dlopen],
1106 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1107 | 	    [AC_CHECK_LIB([svld], [dlopen],
1108 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1110 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1119 |   if test "x$lt_cv_dlopen" != xno; then
1120 |     enable_dlopen=yes
1122 |     enable_dlopen=no
1125 |   case $lt_cv_dlopen in
1126 |   dlopen)
1134 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1136 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1137 | 	  lt_cv_dlopen_self, [dnl
1138 | 	  _LT_AC_TRY_DLOPEN_SELF(
1139 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1140 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1143 |     if test "x$lt_cv_dlopen_self" = xyes; then
1145 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1146 |     	  lt_cv_dlopen_self_static, [dnl
1147 | 	  _LT_AC_TRY_DLOPEN_SELF(
1148 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1149 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1159 |   case $lt_cv_dlopen_self in
1160 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1161 |   *) enable_dlopen_self=unknown ;;
1164 |   case $lt_cv_dlopen_self_static in
1165 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1166 |   *) enable_dlopen_self_static=unknown ;;
1169 | ])# AC_LIBTOOL_DLOPEN_SELF
2080 | # AC_LIBTOOL_DLOPEN
2082 | # enable checks for dlopen support
2083 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2085 | ])# AC_LIBTOOL_DLOPEN
2883 | AC_LIBTOOL_DLOPEN_SELF
4600 | # Whether dlopen is supported.
4601 | dlopen_support=$enable_dlopen
4603 | # Whether dlopen of programs is supported.
4604 | dlopen_self=$enable_dlopen_self
4606 | # Whether dlopen of statically linked programs is supported.
4607 | dlopen_self_static=$enable_dlopen_self_static
4615 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```