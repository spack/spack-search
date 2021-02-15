---
name: "lzma"
layout: package
next_package: icedtea
previous_package: mpileaks
languages: ['bash']
---
## 4.32.7
2 / 128 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
522 |   -dlopen)
523 |     prevopt="-dlopen"
607 |   # Only execute mode is allowed to have -dlopen flags.
609 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1146 | 	    dlopen_self=$dlopen_self_static
1151 | 	    dlopen_self=$dlopen_self_static
1207 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1299 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1456 |       -dlopen)
1843 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1916 | 	  # This library was specified with -dlopen.
2057 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2069 | 	passes="conv scan dlopen dlpreopen link"
2082 | 	dlopen) libs="$dlfiles" ;;
2087 |       if test "$pass" = dlopen; then
2266 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2267 | 	      # If there is no dlopen support or we're linking statically,
2300 | 	dlopen=
2321 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2364 | 	# This library was specified with -dlopen.
2365 | 	if test "$pass" = dlopen; then
2367 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2371 | 	     test "$dlopen_support" != yes ||
2373 | 	    # If there is no dlname, no dlopen support or we're linking
2382 | 	fi # $pass = dlopen
2435 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2810 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2811 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2962 |       if test "$pass" != dlopen; then
3063 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3130 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3768 | 	    $echo "*** a static module, that should work as long as the dlopening"
3769 | 	    $echo "*** application is linked with the -dlopen flag."
3787 | 	    $echo "*** or is declared to -dlopen it."
4197 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4329 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4330 | 	   test "$dlopen_self_static" = unknown; then
4331 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5669 | # The name that we can dlopen(3).
5692 | # Files to dlopen/dlpreopen
5693 | dlopen='$dlfiles'
6308 |     # Handle -dlopen flags immediately.
6337 | 	# Skip this library if it cannot be dlopened.
6362 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6722 |   -dlopen FILE      add the directory containing FILE to the library path
6724 | This mode sets the library path environment variable according to \`-dlopen'
6773 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6782 |   -module           build a library that can dlopened
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
2024 | # AC_LIBTOOL_DLOPEN
2026 | # enable checks for dlopen support
2027 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2029 | ])# AC_LIBTOOL_DLOPEN
2827 | AC_LIBTOOL_DLOPEN_SELF
4544 | # Whether dlopen is supported.
4545 | dlopen_support=$enable_dlopen
4547 | # Whether dlopen of programs is supported.
4548 | dlopen_self=$enable_dlopen_self
4550 | # Whether dlopen of statically linked programs is supported.
4551 | dlopen_self_static=$enable_dlopen_self_static
4559 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```