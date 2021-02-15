---
name: "libidl"
layout: package
next_package: mysql
previous_package: openwsman
languages: ['bash']
---
## 0.8.14
2 / 34 files match

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
2667 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
2670 | m4_defun([_LT_TRY_DLOPEN_SELF],
2722 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
2751 | ])# _LT_TRY_DLOPEN_SELF
2754 | # LT_SYS_DLOPEN_SELF
2756 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
2758 | if test "x$enable_dlopen" != xyes; then
2759 |   enable_dlopen=unknown
2760 |   enable_dlopen_self=unknown
2761 |   enable_dlopen_self_static=unknown
2763 |   lt_cv_dlopen=no
2764 |   lt_cv_dlopen_libs=
2768 |     lt_cv_dlopen="load_add_on"
2769 |     lt_cv_dlopen_libs=
2770 |     lt_cv_dlopen_self=yes
2774 |     lt_cv_dlopen="LoadLibrary"
2775 |     lt_cv_dlopen_libs=
2779 |     lt_cv_dlopen="dlopen"
2780 |     lt_cv_dlopen_libs=
2785 |     AC_CHECK_LIB([dl], [dlopen],
2786 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
2787 |     lt_cv_dlopen="dyld"
2788 |     lt_cv_dlopen_libs=
2789 |     lt_cv_dlopen_self=yes
2795 | 	  [lt_cv_dlopen="shl_load"],
2797 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
2798 | 	[AC_CHECK_FUNC([dlopen],
2799 | 	      [lt_cv_dlopen="dlopen"],
2800 | 	  [AC_CHECK_LIB([dl], [dlopen],
2801 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2802 | 	    [AC_CHECK_LIB([svld], [dlopen],
2803 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2805 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
2814 |   if test "x$lt_cv_dlopen" != xno; then
2815 |     enable_dlopen=yes
2817 |     enable_dlopen=no
2820 |   case $lt_cv_dlopen in
2821 |   dlopen)
2829 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2831 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2832 | 	  lt_cv_dlopen_self, [dnl
2833 | 	  _LT_TRY_DLOPEN_SELF(
2834 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2835 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2838 |     if test "x$lt_cv_dlopen_self" = xyes; then
2840 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2841 | 	  lt_cv_dlopen_self_static, [dnl
2842 | 	  _LT_TRY_DLOPEN_SELF(
2843 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2844 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2854 |   case $lt_cv_dlopen_self in
2855 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2856 |   *) enable_dlopen_self=unknown ;;
2859 |   case $lt_cv_dlopen_self_static in
2860 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2861 |   *) enable_dlopen_self_static=unknown ;;
2864 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2865 | 	 [Whether dlopen is supported])
2866 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2867 | 	 [Whether dlopen of programs is supported])
2868 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2869 | 	 [Whether dlopen of statically linked programs is supported])
2870 | ])# LT_SYS_DLOPEN_SELF
2873 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2875 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6188 |     [Compiler flag to allow reflexive dlopens])
6300 |   LT_SYS_DLOPEN_SELF
8450 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8482 | # dlopen
8484 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8487 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8488 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8491 | put the `dlopen' option into LT_INIT's first parameter.])
8495 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8941 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```