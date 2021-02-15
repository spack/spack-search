---
name: "orbit2"
layout: package
next_package: py-wxpython
previous_package: freexl
languages: ['bash']
---
## 2.14.19
2 / 376 files match

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
5059 |       if test "$pass" = dlopen; then
5271 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5272 | 	      # If there is no dlopen support or we're linking statically,
5302 | 	dlopen=
5332 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5372 | 	# This library was specified with -dlopen.
5373 | 	if test "$pass" = dlopen; then
5375 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5378 | 	     test "$dlopen_support" != yes ||
5380 | 	    # If there is no dlname, no dlopen support or we're linking
5389 | 	fi # $pass = dlopen
5447 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5573 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5574 | 	  dlopenmodule=""
5577 | 	      dlopenmodule="$dlpremoduletest"
5581 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5678 | 		    # if the lib is a (non-dlopened) module then we can not
5682 | 		      if test "X$dlopenmodule" != "X$lib"; then
5834 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5835 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5970 |       if test "$pass" != dlopen; then
6069 | 	func_warning "\`-dlopen' is ignored for archives"
6136 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6798 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6799 | 	    $ECHO "*** application is linked with the -dlopen flag."
6817 | 	    $ECHO "*** or is declared to -dlopen it."
7384 | 	func_warning "\`-dlopen' is ignored for objects"
7499 |         && test "$dlopen_support" = unknown \
7500 | 	&& test "$dlopen_self" = unknown \
7501 | 	&& test "$dlopen_self_static" = unknown && \
7502 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8134 | # The name that we can dlopen(3).
8163 | # Files to dlopen/dlpreopen
8164 | dlopen='$dlfiles'
{% endraw %}

```
### aclocal.m4

```

{% raw %}
2618 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
2621 | m4_defun([_LT_TRY_DLOPEN_SELF],
2673 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
2702 | ])# _LT_TRY_DLOPEN_SELF
2705 | # LT_SYS_DLOPEN_SELF
2707 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
2709 | if test "x$enable_dlopen" != xyes; then
2710 |   enable_dlopen=unknown
2711 |   enable_dlopen_self=unknown
2712 |   enable_dlopen_self_static=unknown
2714 |   lt_cv_dlopen=no
2715 |   lt_cv_dlopen_libs=
2719 |     lt_cv_dlopen="load_add_on"
2720 |     lt_cv_dlopen_libs=
2721 |     lt_cv_dlopen_self=yes
2725 |     lt_cv_dlopen="LoadLibrary"
2726 |     lt_cv_dlopen_libs=
2730 |     lt_cv_dlopen="dlopen"
2731 |     lt_cv_dlopen_libs=
2736 |     AC_CHECK_LIB([dl], [dlopen],
2737 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
2738 |     lt_cv_dlopen="dyld"
2739 |     lt_cv_dlopen_libs=
2740 |     lt_cv_dlopen_self=yes
2746 | 	  [lt_cv_dlopen="shl_load"],
2748 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
2749 | 	[AC_CHECK_FUNC([dlopen],
2750 | 	      [lt_cv_dlopen="dlopen"],
2751 | 	  [AC_CHECK_LIB([dl], [dlopen],
2752 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2753 | 	    [AC_CHECK_LIB([svld], [dlopen],
2754 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2756 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
2765 |   if test "x$lt_cv_dlopen" != xno; then
2766 |     enable_dlopen=yes
2768 |     enable_dlopen=no
2771 |   case $lt_cv_dlopen in
2772 |   dlopen)
2780 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2782 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2783 | 	  lt_cv_dlopen_self, [dnl
2784 | 	  _LT_TRY_DLOPEN_SELF(
2785 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2786 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2789 |     if test "x$lt_cv_dlopen_self" = xyes; then
2791 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2792 | 	  lt_cv_dlopen_self_static, [dnl
2793 | 	  _LT_TRY_DLOPEN_SELF(
2794 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2795 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2805 |   case $lt_cv_dlopen_self in
2806 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2807 |   *) enable_dlopen_self=unknown ;;
2810 |   case $lt_cv_dlopen_self_static in
2811 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2812 |   *) enable_dlopen_self_static=unknown ;;
2815 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2816 | 	 [Whether dlopen is supported])
2817 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2818 | 	 [Whether dlopen of programs is supported])
2819 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2820 | 	 [Whether dlopen of statically linked programs is supported])
2821 | ])# LT_SYS_DLOPEN_SELF
2824 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2826 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6139 |     [Compiler flag to allow reflexive dlopens])
6251 |   LT_SYS_DLOPEN_SELF
8401 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8433 | # dlopen
8435 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8438 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8439 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8442 | put the `dlopen' option into LT_INIT's first parameter.])
8446 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8892 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```