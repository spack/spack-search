---
name: "pslib"
layout: package
next_package: xhmm
previous_package: cloog
languages: ['bash']
---
## 0.4.5
2 / 171 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
737 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
787 |       -dlopen=*|--mode=*|--tag=*)
876 |   # Only execute mode is allowed to have -dlopen flags.
878 |     func_error "unrecognized option \`-dlopen'"
1505 |   -dlopen FILE      add the directory containing FILE to the library path
1507 | This mode sets the library path environment variable according to \`-dlopen'
1560 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1569 |   -module           build a library that can dlopened
1644 |     # Handle -dlopen flags immediately.
1661 | 	# Skip this library if it cannot be dlopened.
1688 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4121 | 	    dlopen_self=$dlopen_self_static
4127 | 	    dlopen_self=$dlopen_self_static
4133 | 	    dlopen_self=$dlopen_self_static
4186 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4270 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4427 |       -dlopen)
4814 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4881 | 	  # This library was specified with -dlopen.
4996 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5007 | 	passes="conv scan dlopen dlpreopen link"
5033 | 	dlopen) libs="$dlfiles" ;;
5062 |       if test "$pass" = dlopen; then
5274 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5275 | 	      # If there is no dlopen support or we're linking statically,
5305 | 	dlopen=
5335 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5375 | 	# This library was specified with -dlopen.
5376 | 	if test "$pass" = dlopen; then
5378 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5381 | 	     test "$dlopen_support" != yes ||
5383 | 	    # If there is no dlname, no dlopen support or we're linking
5392 | 	fi # $pass = dlopen
5450 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5576 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5577 | 	  dlopenmodule=""
5580 | 	      dlopenmodule="$dlpremoduletest"
5584 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5681 | 		    # if the lib is a (non-dlopened) module then we can not
5685 | 		      if test "X$dlopenmodule" != "X$lib"; then
5837 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5838 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5974 |       if test "$pass" != dlopen; then
6073 | 	func_warning "\`-dlopen' is ignored for archives"
6140 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6805 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6806 | 	    $ECHO "*** application is linked with the -dlopen flag."
6824 | 	    $ECHO "*** or is declared to -dlopen it."
7391 | 	func_warning "\`-dlopen' is ignored for objects"
7506 |         && test "$dlopen_support" = unknown \
7507 | 	&& test "$dlopen_self" = unknown \
7508 | 	&& test "$dlopen_self_static" = unknown && \
7509 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8141 | # The name that we can dlopen(3).
8170 | # Files to dlopen/dlpreopen
8171 | dlopen='$dlfiles'
{% endraw %}

```
### aclocal.m4

```

{% raw %}
2276 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
2279 | m4_defun([_LT_TRY_DLOPEN_SELF],
2331 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
2360 | ])# _LT_TRY_DLOPEN_SELF
2363 | # LT_SYS_DLOPEN_SELF
2365 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
2367 | if test "x$enable_dlopen" != xyes; then
2368 |   enable_dlopen=unknown
2369 |   enable_dlopen_self=unknown
2370 |   enable_dlopen_self_static=unknown
2372 |   lt_cv_dlopen=no
2373 |   lt_cv_dlopen_libs=
2377 |     lt_cv_dlopen="load_add_on"
2378 |     lt_cv_dlopen_libs=
2379 |     lt_cv_dlopen_self=yes
2383 |     lt_cv_dlopen="LoadLibrary"
2384 |     lt_cv_dlopen_libs=
2388 |     lt_cv_dlopen="dlopen"
2389 |     lt_cv_dlopen_libs=
2394 |     AC_CHECK_LIB([dl], [dlopen],
2395 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
2396 |     lt_cv_dlopen="dyld"
2397 |     lt_cv_dlopen_libs=
2398 |     lt_cv_dlopen_self=yes
2404 | 	  [lt_cv_dlopen="shl_load"],
2406 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
2407 | 	[AC_CHECK_FUNC([dlopen],
2408 | 	      [lt_cv_dlopen="dlopen"],
2409 | 	  [AC_CHECK_LIB([dl], [dlopen],
2410 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2411 | 	    [AC_CHECK_LIB([svld], [dlopen],
2412 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2414 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
2423 |   if test "x$lt_cv_dlopen" != xno; then
2424 |     enable_dlopen=yes
2426 |     enable_dlopen=no
2429 |   case $lt_cv_dlopen in
2430 |   dlopen)
2438 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2440 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2441 | 	  lt_cv_dlopen_self, [dnl
2442 | 	  _LT_TRY_DLOPEN_SELF(
2443 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2444 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2447 |     if test "x$lt_cv_dlopen_self" = xyes; then
2449 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2450 | 	  lt_cv_dlopen_self_static, [dnl
2451 | 	  _LT_TRY_DLOPEN_SELF(
2452 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2453 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2463 |   case $lt_cv_dlopen_self in
2464 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2465 |   *) enable_dlopen_self=unknown ;;
2468 |   case $lt_cv_dlopen_self_static in
2469 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2470 |   *) enable_dlopen_self_static=unknown ;;
2473 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2474 | 	 [Whether dlopen is supported])
2475 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2476 | 	 [Whether dlopen of programs is supported])
2477 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2478 | 	 [Whether dlopen of statically linked programs is supported])
2479 | ])# LT_SYS_DLOPEN_SELF
2482 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2484 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5817 |     [Compiler flag to allow reflexive dlopens])
5929 |   LT_SYS_DLOPEN_SELF
8079 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8111 | # dlopen
8113 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8116 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8117 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8120 | put the `dlopen' option into LT_INIT's first parameter.])
8124 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8570 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```