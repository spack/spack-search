---
name: "mcpp"
layout: package
next_package: powertop
previous_package: xcb-util
languages: ['bash']
---
## 2.7.2
2 / 826 files match

 - [aclocal.m4](#aclocalm4)
 - [config/ltmain.sh](#configltmainsh)

### aclocal.m4

```

{% raw %}
210 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
825 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
828 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
884 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
913 | ])# _LT_AC_TRY_DLOPEN_SELF
916 | # AC_LIBTOOL_DLOPEN_SELF
918 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
920 | if test "x$enable_dlopen" != xyes; then
921 |   enable_dlopen=unknown
922 |   enable_dlopen_self=unknown
923 |   enable_dlopen_self_static=unknown
925 |   lt_cv_dlopen=no
926 |   lt_cv_dlopen_libs=
930 |     lt_cv_dlopen="load_add_on"
931 |     lt_cv_dlopen_libs=
932 |     lt_cv_dlopen_self=yes
936 |     lt_cv_dlopen="LoadLibrary"
937 |     lt_cv_dlopen_libs=
941 |     lt_cv_dlopen="dlopen"
942 |     lt_cv_dlopen_libs=
947 |     AC_CHECK_LIB([dl], [dlopen],
948 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
949 |     lt_cv_dlopen="dyld"
950 |     lt_cv_dlopen_libs=
951 |     lt_cv_dlopen_self=yes
957 | 	  [lt_cv_dlopen="shl_load"],
959 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
960 | 	[AC_CHECK_FUNC([dlopen],
961 | 	      [lt_cv_dlopen="dlopen"],
962 | 	  [AC_CHECK_LIB([dl], [dlopen],
963 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
964 | 	    [AC_CHECK_LIB([svld], [dlopen],
965 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
967 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
976 |   if test "x$lt_cv_dlopen" != xno; then
977 |     enable_dlopen=yes
979 |     enable_dlopen=no
982 |   case $lt_cv_dlopen in
983 |   dlopen)
991 |     LIBS="$lt_cv_dlopen_libs $LIBS"
993 |     AC_CACHE_CHECK([whether a program can dlopen itself],
994 | 	  lt_cv_dlopen_self, [dnl
995 | 	  _LT_AC_TRY_DLOPEN_SELF(
996 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
997 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1000 |     if test "x$lt_cv_dlopen_self" = xyes; then
1002 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1003 |     	  lt_cv_dlopen_self_static, [dnl
1004 | 	  _LT_AC_TRY_DLOPEN_SELF(
1005 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1006 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1016 |   case $lt_cv_dlopen_self in
1017 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1018 |   *) enable_dlopen_self=unknown ;;
1021 |   case $lt_cv_dlopen_self_static in
1022 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1023 |   *) enable_dlopen_self_static=unknown ;;
1026 | ])# AC_LIBTOOL_DLOPEN_SELF
1887 | # AC_LIBTOOL_DLOPEN
1889 | # enable checks for dlopen support
1890 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1892 | ])# AC_LIBTOOL_DLOPEN
2680 | AC_LIBTOOL_DLOPEN_SELF
4351 | # Whether dlopen is supported.
4352 | dlopen_support=$enable_dlopen
4354 | # Whether dlopen of programs is supported.
4355 | dlopen_self=$enable_dlopen_self
4357 | # Whether dlopen of statically linked programs is supported.
4358 | dlopen_self_static=$enable_dlopen_self_static
4366 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### config/ltmain.sh

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
2090 |       if test "$pass" = dlopen; then
2269 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2270 | 	      # If there is no dlopen support or we're linking statically,
2303 | 	dlopen=
2324 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2367 | 	# This library was specified with -dlopen.
2368 | 	if test "$pass" = dlopen; then
2370 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2374 | 	     test "$dlopen_support" != yes ||
2376 | 	    # If there is no dlname, no dlopen support or we're linking
2385 | 	fi # $pass = dlopen
2438 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2813 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2814 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2965 |       if test "$pass" != dlopen; then
3066 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3133 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3776 | 	    $echo "*** a static module, that should work as long as the dlopening"
3777 | 	    $echo "*** application is linked with the -dlopen flag."
3795 | 	    $echo "*** or is declared to -dlopen it."
4205 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4337 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4338 | 	   test "$dlopen_self_static" = unknown; then
4339 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5677 | # The name that we can dlopen(3).
5700 | # Files to dlopen/dlpreopen
5701 | dlopen='$dlfiles'
6316 |     # Handle -dlopen flags immediately.
6345 | 	# Skip this library if it cannot be dlopened.
6370 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6730 |   -dlopen FILE      add the directory containing FILE to the library path
6732 | This mode sets the library path environment variable according to \`-dlopen'
6781 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6790 |   -module           build a library that can dlopened
{% endraw %}

```