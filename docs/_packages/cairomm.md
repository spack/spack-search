---
name: "cairomm"
layout: package
next_package: at-spi2-core
previous_package: sst-macro
languages: ['bash']
---
## 1.6.2
2 / 343 files match

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
213 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
828 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
831 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
887 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
916 | ])# _LT_AC_TRY_DLOPEN_SELF
919 | # AC_LIBTOOL_DLOPEN_SELF
921 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
923 | if test "x$enable_dlopen" != xyes; then
924 |   enable_dlopen=unknown
925 |   enable_dlopen_self=unknown
926 |   enable_dlopen_self_static=unknown
928 |   lt_cv_dlopen=no
929 |   lt_cv_dlopen_libs=
933 |     lt_cv_dlopen="load_add_on"
934 |     lt_cv_dlopen_libs=
935 |     lt_cv_dlopen_self=yes
939 |     lt_cv_dlopen="LoadLibrary"
940 |     lt_cv_dlopen_libs=
944 |     lt_cv_dlopen="dlopen"
945 |     lt_cv_dlopen_libs=
950 |     AC_CHECK_LIB([dl], [dlopen],
951 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
952 |     lt_cv_dlopen="dyld"
953 |     lt_cv_dlopen_libs=
954 |     lt_cv_dlopen_self=yes
960 | 	  [lt_cv_dlopen="shl_load"],
962 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
963 | 	[AC_CHECK_FUNC([dlopen],
964 | 	      [lt_cv_dlopen="dlopen"],
965 | 	  [AC_CHECK_LIB([dl], [dlopen],
966 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
967 | 	    [AC_CHECK_LIB([svld], [dlopen],
968 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
970 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
979 |   if test "x$lt_cv_dlopen" != xno; then
980 |     enable_dlopen=yes
982 |     enable_dlopen=no
985 |   case $lt_cv_dlopen in
986 |   dlopen)
994 |     LIBS="$lt_cv_dlopen_libs $LIBS"
996 |     AC_CACHE_CHECK([whether a program can dlopen itself],
997 | 	  lt_cv_dlopen_self, [dnl
998 | 	  _LT_AC_TRY_DLOPEN_SELF(
999 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1000 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1003 |     if test "x$lt_cv_dlopen_self" = xyes; then
1005 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1006 |     	  lt_cv_dlopen_self_static, [dnl
1007 | 	  _LT_AC_TRY_DLOPEN_SELF(
1008 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1009 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1019 |   case $lt_cv_dlopen_self in
1020 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1021 |   *) enable_dlopen_self=unknown ;;
1024 |   case $lt_cv_dlopen_self_static in
1025 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1026 |   *) enable_dlopen_self_static=unknown ;;
1029 | ])# AC_LIBTOOL_DLOPEN_SELF
1919 | # AC_LIBTOOL_DLOPEN
1921 | # enable checks for dlopen support
1922 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1924 | ])# AC_LIBTOOL_DLOPEN
2712 | AC_LIBTOOL_DLOPEN_SELF
4383 | # Whether dlopen is supported.
4384 | dlopen_support=$enable_dlopen
4386 | # Whether dlopen of programs is supported.
4387 | dlopen_self=$enable_dlopen_self
4389 | # Whether dlopen of statically linked programs is supported.
4390 | dlopen_self_static=$enable_dlopen_self_static
4398 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```