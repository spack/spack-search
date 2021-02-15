---
name: "liblbxutil"
layout: package
next_package: py-pyjnius
previous_package: libkcapi
languages: ['bash']
---
## 1.1.0
2 / 31 files match

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
1817 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
2528 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
2531 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
2587 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
2616 | ])# _LT_AC_TRY_DLOPEN_SELF
2619 | # AC_LIBTOOL_DLOPEN_SELF
2621 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
2623 | if test "x$enable_dlopen" != xyes; then
2624 |   enable_dlopen=unknown
2625 |   enable_dlopen_self=unknown
2626 |   enable_dlopen_self_static=unknown
2628 |   lt_cv_dlopen=no
2629 |   lt_cv_dlopen_libs=
2633 |     lt_cv_dlopen="load_add_on"
2634 |     lt_cv_dlopen_libs=
2635 |     lt_cv_dlopen_self=yes
2639 |     lt_cv_dlopen="LoadLibrary"
2640 |     lt_cv_dlopen_libs=
2644 |     lt_cv_dlopen="dlopen"
2645 |     lt_cv_dlopen_libs=
2650 |     AC_CHECK_LIB([dl], [dlopen],
2651 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
2652 |     lt_cv_dlopen="dyld"
2653 |     lt_cv_dlopen_libs=
2654 |     lt_cv_dlopen_self=yes
2660 | 	  [lt_cv_dlopen="shl_load"],
2662 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
2663 | 	[AC_CHECK_FUNC([dlopen],
2664 | 	      [lt_cv_dlopen="dlopen"],
2665 | 	  [AC_CHECK_LIB([dl], [dlopen],
2666 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2667 | 	    [AC_CHECK_LIB([svld], [dlopen],
2668 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2670 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
2679 |   if test "x$lt_cv_dlopen" != xno; then
2680 |     enable_dlopen=yes
2682 |     enable_dlopen=no
2685 |   case $lt_cv_dlopen in
2686 |   dlopen)
2694 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2696 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2697 | 	  lt_cv_dlopen_self, [dnl
2698 | 	  _LT_AC_TRY_DLOPEN_SELF(
2699 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2700 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2703 |     if test "x$lt_cv_dlopen_self" = xyes; then
2705 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2706 |     	  lt_cv_dlopen_self_static, [dnl
2707 | 	  _LT_AC_TRY_DLOPEN_SELF(
2708 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2709 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2719 |   case $lt_cv_dlopen_self in
2720 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2721 |   *) enable_dlopen_self=unknown ;;
2724 |   case $lt_cv_dlopen_self_static in
2725 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2726 |   *) enable_dlopen_self_static=unknown ;;
2729 | ])# AC_LIBTOOL_DLOPEN_SELF
3627 | # AC_LIBTOOL_DLOPEN
3629 | # enable checks for dlopen support
3630 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
3632 | ])# AC_LIBTOOL_DLOPEN
4430 | AC_LIBTOOL_DLOPEN_SELF
6147 | # Whether dlopen is supported.
6148 | dlopen_support=$enable_dlopen
6150 | # Whether dlopen of programs is supported.
6151 | dlopen_self=$enable_dlopen_self
6153 | # Whether dlopen of statically linked programs is supported.
6154 | dlopen_self_static=$enable_dlopen_self_static
6162 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```