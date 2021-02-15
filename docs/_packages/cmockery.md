---
name: "cmockery"
layout: package
next_package: blitz
previous_package: libevpath
languages: ['bash']
---
## 0.1.0
2 / 43 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
527 |   -dlopen)
528 |     prevopt="-dlopen"
612 |   # Only execute mode is allowed to have -dlopen flags.
614 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1151 | 	    dlopen_self=$dlopen_self_static
1156 | 	    dlopen_self=$dlopen_self_static
1212 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1304 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1461 |       -dlopen)
1855 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1928 | 	  # This library was specified with -dlopen.
2069 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2081 | 	passes="conv scan dlopen dlpreopen link"
2094 | 	dlopen) libs="$dlfiles" ;;
2099 |       if test "$pass" = dlopen; then
2301 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2302 | 	      # If there is no dlopen support or we're linking statically,
2335 | 	dlopen=
2356 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2399 | 	# This library was specified with -dlopen.
2400 | 	if test "$pass" = dlopen; then
2402 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2406 | 	     test "$dlopen_support" != yes ||
2408 | 	    # If there is no dlname, no dlopen support or we're linking
2417 | 	fi # $pass = dlopen
2470 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2845 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2846 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2997 |       if test "$pass" != dlopen; then
3098 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3165 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3803 | 	    $echo "*** a static module, that should work as long as the dlopening"
3804 | 	    $echo "*** application is linked with the -dlopen flag."
3822 | 	    $echo "*** or is declared to -dlopen it."
4232 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4364 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4365 | 	   test "$dlopen_self_static" = unknown; then
4366 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5707 | # The name that we can dlopen(3).
5730 | # Files to dlopen/dlpreopen
5731 | dlopen='$dlfiles'
6353 |     # Handle -dlopen flags immediately.
6382 | 	# Skip this library if it cannot be dlopened.
6407 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6767 |   -dlopen FILE      add the directory containing FILE to the library path
6769 | This mode sets the library path environment variable according to \`-dlopen'
6818 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6827 |   -module           build a library that can dlopened
{% endraw %}

```
### aclocal.m4

```

{% raw %}
205 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
820 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
823 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
879 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
908 | ])# _LT_AC_TRY_DLOPEN_SELF
911 | # AC_LIBTOOL_DLOPEN_SELF
913 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
915 | if test "x$enable_dlopen" != xyes; then
916 |   enable_dlopen=unknown
917 |   enable_dlopen_self=unknown
918 |   enable_dlopen_self_static=unknown
920 |   lt_cv_dlopen=no
921 |   lt_cv_dlopen_libs=
925 |     lt_cv_dlopen="load_add_on"
926 |     lt_cv_dlopen_libs=
927 |     lt_cv_dlopen_self=yes
931 |     lt_cv_dlopen="LoadLibrary"
932 |     lt_cv_dlopen_libs=
936 |     lt_cv_dlopen="dlopen"
937 |     lt_cv_dlopen_libs=
942 |     AC_CHECK_LIB([dl], [dlopen],
943 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
944 |     lt_cv_dlopen="dyld"
945 |     lt_cv_dlopen_libs=
946 |     lt_cv_dlopen_self=yes
952 | 	  [lt_cv_dlopen="shl_load"],
954 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
955 | 	[AC_CHECK_FUNC([dlopen],
956 | 	      [lt_cv_dlopen="dlopen"],
957 | 	  [AC_CHECK_LIB([dl], [dlopen],
958 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
959 | 	    [AC_CHECK_LIB([svld], [dlopen],
960 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
962 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
971 |   if test "x$lt_cv_dlopen" != xno; then
972 |     enable_dlopen=yes
974 |     enable_dlopen=no
977 |   case $lt_cv_dlopen in
978 |   dlopen)
986 |     LIBS="$lt_cv_dlopen_libs $LIBS"
988 |     AC_CACHE_CHECK([whether a program can dlopen itself],
989 | 	  lt_cv_dlopen_self, [dnl
990 | 	  _LT_AC_TRY_DLOPEN_SELF(
991 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
992 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
995 |     if test "x$lt_cv_dlopen_self" = xyes; then
997 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
998 |     	  lt_cv_dlopen_self_static, [dnl
999 | 	  _LT_AC_TRY_DLOPEN_SELF(
1000 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1001 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1011 |   case $lt_cv_dlopen_self in
1012 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1013 |   *) enable_dlopen_self=unknown ;;
1016 |   case $lt_cv_dlopen_self_static in
1017 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1018 |   *) enable_dlopen_self_static=unknown ;;
1021 | ])# AC_LIBTOOL_DLOPEN_SELF
1906 | # AC_LIBTOOL_DLOPEN
1908 | # enable checks for dlopen support
1909 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1911 | ])# AC_LIBTOOL_DLOPEN
2699 | AC_LIBTOOL_DLOPEN_SELF
4370 | # Whether dlopen is supported.
4371 | dlopen_support=$enable_dlopen
4373 | # Whether dlopen of programs is supported.
4374 | dlopen_self=$enable_dlopen_self
4376 | # Whether dlopen of statically linked programs is supported.
4377 | dlopen_self_static=$enable_dlopen_self_static
4385 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```