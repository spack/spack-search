---
name: "dia"
layout: package
next_package: babeltrace
previous_package: callflow
languages: ['bash']
---
## 0.97.3
3 / 3022 files match

 - [ltmain.sh](#ltmainsh)
 - [ChangeLog.pre-git](#changelogpre-git)
 - [aclocal.m4](#aclocalm4)

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
6155 |       if test "$pass" = dlopen; then
6374 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6375 | 	      # If there is no dlopen support or we're linking statically,
6405 | 	dlopen=
6435 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6481 | 	# This library was specified with -dlopen.
6482 | 	if test "$pass" = dlopen; then
6484 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6487 | 	     test "$dlopen_support" != yes ||
6489 | 	    # If there is no dlname, no dlopen support or we're linking
6498 | 	fi # $pass = dlopen
6554 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6556 | 	      # We recover the dlopen module name by 'saving' the la file
6580 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6709 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6710 | 	  dlopenmodule=""
6713 | 	      dlopenmodule="$dlpremoduletest"
6717 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6814 | 		    # if the lib is a (non-dlopened) module then we can not
6818 | 		      if test "X$dlopenmodule" != "X$lib"; then
6970 | 	      echo "*** a static module, that should work as long as the dlopening application"
6971 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7115 |       if test "$pass" != dlopen; then
7214 | 	func_warning "\`-dlopen' is ignored for archives"
7281 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7960 | 	    echo "*** a static module, that should work as long as the dlopening"
7961 | 	    echo "*** application is linked with the -dlopen flag."
7979 | 	    echo "*** or is declared to -dlopen it."
8590 | 	func_warning "\`-dlopen' is ignored for objects"
8708 |         && test "$dlopen_support" = unknown \
8709 | 	&& test "$dlopen_self" = unknown \
8710 | 	&& test "$dlopen_self_static" = unknown && \
8711 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9392 | # The name that we can dlopen(3).
9421 | # Files to dlopen/dlpreopen
9422 | dlopen='$dlfiles'
{% endraw %}

```
### ChangeLog.pre-git

```

{% raw %}
24025 | 	build a versioned library.  It will only ever be dlopen'd, so this
26408 | 	Detect dlopen better.
26409 | 	Detect wether dlopen needs an underscore in the identifier.
{% endraw %}

```
### aclocal.m4

```

{% raw %}
2423 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
2426 | m4_defun([_LT_TRY_DLOPEN_SELF],
2484 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
2517 | ])# _LT_TRY_DLOPEN_SELF
2520 | # LT_SYS_DLOPEN_SELF
2522 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
2524 | if test "x$enable_dlopen" != xyes; then
2525 |   enable_dlopen=unknown
2526 |   enable_dlopen_self=unknown
2527 |   enable_dlopen_self_static=unknown
2529 |   lt_cv_dlopen=no
2530 |   lt_cv_dlopen_libs=
2534 |     lt_cv_dlopen="load_add_on"
2535 |     lt_cv_dlopen_libs=
2536 |     lt_cv_dlopen_self=yes
2540 |     lt_cv_dlopen="LoadLibrary"
2541 |     lt_cv_dlopen_libs=
2545 |     lt_cv_dlopen="dlopen"
2546 |     lt_cv_dlopen_libs=
2551 |     AC_CHECK_LIB([dl], [dlopen],
2552 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
2553 |     lt_cv_dlopen="dyld"
2554 |     lt_cv_dlopen_libs=
2555 |     lt_cv_dlopen_self=yes
2561 | 	  [lt_cv_dlopen="shl_load"],
2563 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
2564 | 	[AC_CHECK_FUNC([dlopen],
2565 | 	      [lt_cv_dlopen="dlopen"],
2566 | 	  [AC_CHECK_LIB([dl], [dlopen],
2567 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2568 | 	    [AC_CHECK_LIB([svld], [dlopen],
2569 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2571 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
2580 |   if test "x$lt_cv_dlopen" != xno; then
2581 |     enable_dlopen=yes
2583 |     enable_dlopen=no
2586 |   case $lt_cv_dlopen in
2587 |   dlopen)
2595 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2597 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2598 | 	  lt_cv_dlopen_self, [dnl
2599 | 	  _LT_TRY_DLOPEN_SELF(
2600 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2601 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2604 |     if test "x$lt_cv_dlopen_self" = xyes; then
2606 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2607 | 	  lt_cv_dlopen_self_static, [dnl
2608 | 	  _LT_TRY_DLOPEN_SELF(
2609 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2610 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2620 |   case $lt_cv_dlopen_self in
2621 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2622 |   *) enable_dlopen_self=unknown ;;
2625 |   case $lt_cv_dlopen_self_static in
2626 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2627 |   *) enable_dlopen_self_static=unknown ;;
2630 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2631 | 	 [Whether dlopen is supported])
2632 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2633 | 	 [Whether dlopen of programs is supported])
2634 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2635 | 	 [Whether dlopen of statically linked programs is supported])
2636 | ])# LT_SYS_DLOPEN_SELF
2639 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2641 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6341 |     [Compiler flag to allow reflexive dlopens])
6450 |   LT_SYS_DLOPEN_SELF
8719 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8751 | # dlopen
8753 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8756 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8757 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8760 | put the `dlopen' option into LT_INIT's first parameter.])
8764 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
9225 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```