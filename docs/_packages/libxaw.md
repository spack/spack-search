---
name: "libxaw"
layout: package
next_package: optipng
previous_package: podio
languages: ['bash']
---
## 1.0.12
2 / 185 files match

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
2921 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
2924 | m4_defun([_LT_TRY_DLOPEN_SELF],
2982 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
3015 | ])# _LT_TRY_DLOPEN_SELF
3018 | # LT_SYS_DLOPEN_SELF
3020 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
3022 | if test "x$enable_dlopen" != xyes; then
3023 |   enable_dlopen=unknown
3024 |   enable_dlopen_self=unknown
3025 |   enable_dlopen_self_static=unknown
3027 |   lt_cv_dlopen=no
3028 |   lt_cv_dlopen_libs=
3032 |     lt_cv_dlopen="load_add_on"
3033 |     lt_cv_dlopen_libs=
3034 |     lt_cv_dlopen_self=yes
3038 |     lt_cv_dlopen="LoadLibrary"
3039 |     lt_cv_dlopen_libs=
3043 |     lt_cv_dlopen="dlopen"
3044 |     lt_cv_dlopen_libs=
3049 |     AC_CHECK_LIB([dl], [dlopen],
3050 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
3051 |     lt_cv_dlopen="dyld"
3052 |     lt_cv_dlopen_libs=
3053 |     lt_cv_dlopen_self=yes
3059 | 	  [lt_cv_dlopen="shl_load"],
3061 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
3062 | 	[AC_CHECK_FUNC([dlopen],
3063 | 	      [lt_cv_dlopen="dlopen"],
3064 | 	  [AC_CHECK_LIB([dl], [dlopen],
3065 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
3066 | 	    [AC_CHECK_LIB([svld], [dlopen],
3067 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
3069 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
3078 |   if test "x$lt_cv_dlopen" != xno; then
3079 |     enable_dlopen=yes
3081 |     enable_dlopen=no
3084 |   case $lt_cv_dlopen in
3085 |   dlopen)
3093 |     LIBS="$lt_cv_dlopen_libs $LIBS"
3095 |     AC_CACHE_CHECK([whether a program can dlopen itself],
3096 | 	  lt_cv_dlopen_self, [dnl
3097 | 	  _LT_TRY_DLOPEN_SELF(
3098 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
3099 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
3102 |     if test "x$lt_cv_dlopen_self" = xyes; then
3104 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
3105 | 	  lt_cv_dlopen_self_static, [dnl
3106 | 	  _LT_TRY_DLOPEN_SELF(
3107 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
3108 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
3118 |   case $lt_cv_dlopen_self in
3119 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
3120 |   *) enable_dlopen_self=unknown ;;
3123 |   case $lt_cv_dlopen_self_static in
3124 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
3125 |   *) enable_dlopen_self_static=unknown ;;
3128 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
3129 | 	 [Whether dlopen is supported])
3130 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
3131 | 	 [Whether dlopen of programs is supported])
3132 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
3133 | 	 [Whether dlopen of statically linked programs is supported])
3134 | ])# LT_SYS_DLOPEN_SELF
3137 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
3139 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6835 |     [Compiler flag to allow reflexive dlopens])
6944 |   LT_SYS_DLOPEN_SELF
9216 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
9248 | # dlopen
9250 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
9253 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
9254 | [_LT_SET_OPTION([LT_INIT], [dlopen])
9257 | put the `dlopen' option into LT_INIT's first parameter.])
9261 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
9722 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```