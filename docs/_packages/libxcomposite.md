---
name: "libxcomposite"
layout: package
next_package: speex
previous_package: libyaml
languages: ['bash']
---
## 0.4.4
2 / 29 files match

 - [ltmain.sh](#ltmainsh)
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
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### aclocal.m4

```

{% raw %}
2773 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
2776 | m4_defun([_LT_TRY_DLOPEN_SELF],
2834 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
2867 | ])# _LT_TRY_DLOPEN_SELF
2870 | # LT_SYS_DLOPEN_SELF
2872 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
2874 | if test "x$enable_dlopen" != xyes; then
2875 |   enable_dlopen=unknown
2876 |   enable_dlopen_self=unknown
2877 |   enable_dlopen_self_static=unknown
2879 |   lt_cv_dlopen=no
2880 |   lt_cv_dlopen_libs=
2884 |     lt_cv_dlopen="load_add_on"
2885 |     lt_cv_dlopen_libs=
2886 |     lt_cv_dlopen_self=yes
2890 |     lt_cv_dlopen="LoadLibrary"
2891 |     lt_cv_dlopen_libs=
2895 |     lt_cv_dlopen="dlopen"
2896 |     lt_cv_dlopen_libs=
2901 |     AC_CHECK_LIB([dl], [dlopen],
2902 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
2903 |     lt_cv_dlopen="dyld"
2904 |     lt_cv_dlopen_libs=
2905 |     lt_cv_dlopen_self=yes
2911 | 	  [lt_cv_dlopen="shl_load"],
2913 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
2914 | 	[AC_CHECK_FUNC([dlopen],
2915 | 	      [lt_cv_dlopen="dlopen"],
2916 | 	  [AC_CHECK_LIB([dl], [dlopen],
2917 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2918 | 	    [AC_CHECK_LIB([svld], [dlopen],
2919 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2921 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
2930 |   if test "x$lt_cv_dlopen" != xno; then
2931 |     enable_dlopen=yes
2933 |     enable_dlopen=no
2936 |   case $lt_cv_dlopen in
2937 |   dlopen)
2945 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2947 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2948 | 	  lt_cv_dlopen_self, [dnl
2949 | 	  _LT_TRY_DLOPEN_SELF(
2950 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2951 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2954 |     if test "x$lt_cv_dlopen_self" = xyes; then
2956 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2957 | 	  lt_cv_dlopen_self_static, [dnl
2958 | 	  _LT_TRY_DLOPEN_SELF(
2959 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2960 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2970 |   case $lt_cv_dlopen_self in
2971 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2972 |   *) enable_dlopen_self=unknown ;;
2975 |   case $lt_cv_dlopen_self_static in
2976 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2977 |   *) enable_dlopen_self_static=unknown ;;
2980 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2981 | 	 [Whether dlopen is supported])
2982 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2983 | 	 [Whether dlopen of programs is supported])
2984 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2985 | 	 [Whether dlopen of statically linked programs is supported])
2986 | ])# LT_SYS_DLOPEN_SELF
2989 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2991 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6687 |     [Compiler flag to allow reflexive dlopens])
6796 |   LT_SYS_DLOPEN_SELF
9068 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
9100 | # dlopen
9102 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
9105 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
9106 | [_LT_SET_OPTION([LT_INIT], [dlopen])
9109 | put the `dlopen' option into LT_INIT's first parameter.])
9113 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
9574 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```