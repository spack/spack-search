---
name: "libxfontcache"
layout: package
next_package: hdf-eos5
previous_package: gzip
languages: ['bash']
---
## 1.0.5
2 / 15 files match

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
### aclocal.m4

```

{% raw %}
1803 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
2514 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
2517 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
2573 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
2602 | ])# _LT_AC_TRY_DLOPEN_SELF
2605 | # AC_LIBTOOL_DLOPEN_SELF
2607 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
2609 | if test "x$enable_dlopen" != xyes; then
2610 |   enable_dlopen=unknown
2611 |   enable_dlopen_self=unknown
2612 |   enable_dlopen_self_static=unknown
2614 |   lt_cv_dlopen=no
2615 |   lt_cv_dlopen_libs=
2619 |     lt_cv_dlopen="load_add_on"
2620 |     lt_cv_dlopen_libs=
2621 |     lt_cv_dlopen_self=yes
2625 |     lt_cv_dlopen="LoadLibrary"
2626 |     lt_cv_dlopen_libs=
2630 |     lt_cv_dlopen="dlopen"
2631 |     lt_cv_dlopen_libs=
2636 |     AC_CHECK_LIB([dl], [dlopen],
2637 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
2638 |     lt_cv_dlopen="dyld"
2639 |     lt_cv_dlopen_libs=
2640 |     lt_cv_dlopen_self=yes
2646 | 	  [lt_cv_dlopen="shl_load"],
2648 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
2649 | 	[AC_CHECK_FUNC([dlopen],
2650 | 	      [lt_cv_dlopen="dlopen"],
2651 | 	  [AC_CHECK_LIB([dl], [dlopen],
2652 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2653 | 	    [AC_CHECK_LIB([svld], [dlopen],
2654 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2656 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
2665 |   if test "x$lt_cv_dlopen" != xno; then
2666 |     enable_dlopen=yes
2668 |     enable_dlopen=no
2671 |   case $lt_cv_dlopen in
2672 |   dlopen)
2680 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2682 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2683 | 	  lt_cv_dlopen_self, [dnl
2684 | 	  _LT_AC_TRY_DLOPEN_SELF(
2685 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2686 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2689 |     if test "x$lt_cv_dlopen_self" = xyes; then
2691 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2692 |     	  lt_cv_dlopen_self_static, [dnl
2693 | 	  _LT_AC_TRY_DLOPEN_SELF(
2694 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2695 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2705 |   case $lt_cv_dlopen_self in
2706 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2707 |   *) enable_dlopen_self=unknown ;;
2710 |   case $lt_cv_dlopen_self_static in
2711 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2712 |   *) enable_dlopen_self_static=unknown ;;
2715 | ])# AC_LIBTOOL_DLOPEN_SELF
3613 | # AC_LIBTOOL_DLOPEN
3615 | # enable checks for dlopen support
3616 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
3618 | ])# AC_LIBTOOL_DLOPEN
4416 | AC_LIBTOOL_DLOPEN_SELF
6133 | # Whether dlopen is supported.
6134 | dlopen_support=$enable_dlopen
6136 | # Whether dlopen of programs is supported.
6137 | dlopen_self=$enable_dlopen_self
6139 | # Whether dlopen of statically linked programs is supported.
6140 | dlopen_self_static=$enable_dlopen_self_static
6148 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```