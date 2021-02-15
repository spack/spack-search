---
name: "libtheora"
layout: package
next_package: rocm-openmp-extras
previous_package: ferret
languages: ['bash']
---
## 1.1.1
2 / 291 files match

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
982 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
1014 | # dlopen
1016 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
1019 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
1020 | [_LT_SET_OPTION([LT_INIT], [dlopen])
1023 | put the `dlopen' option into LT_INIT's first parameter.])
1027 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
2904 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
2907 | m4_defun([_LT_TRY_DLOPEN_SELF],
2959 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
2988 | ])# _LT_TRY_DLOPEN_SELF
2991 | # LT_SYS_DLOPEN_SELF
2993 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
2995 | if test "x$enable_dlopen" != xyes; then
2996 |   enable_dlopen=unknown
2997 |   enable_dlopen_self=unknown
2998 |   enable_dlopen_self_static=unknown
3000 |   lt_cv_dlopen=no
3001 |   lt_cv_dlopen_libs=
3005 |     lt_cv_dlopen="load_add_on"
3006 |     lt_cv_dlopen_libs=
3007 |     lt_cv_dlopen_self=yes
3011 |     lt_cv_dlopen="LoadLibrary"
3012 |     lt_cv_dlopen_libs=
3016 |     lt_cv_dlopen="dlopen"
3017 |     lt_cv_dlopen_libs=
3022 |     AC_CHECK_LIB([dl], [dlopen],
3023 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
3024 |     lt_cv_dlopen="dyld"
3025 |     lt_cv_dlopen_libs=
3026 |     lt_cv_dlopen_self=yes
3032 | 	  [lt_cv_dlopen="shl_load"],
3034 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
3035 | 	[AC_CHECK_FUNC([dlopen],
3036 | 	      [lt_cv_dlopen="dlopen"],
3037 | 	  [AC_CHECK_LIB([dl], [dlopen],
3038 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
3039 | 	    [AC_CHECK_LIB([svld], [dlopen],
3040 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
3042 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
3051 |   if test "x$lt_cv_dlopen" != xno; then
3052 |     enable_dlopen=yes
3054 |     enable_dlopen=no
3057 |   case $lt_cv_dlopen in
3058 |   dlopen)
3066 |     LIBS="$lt_cv_dlopen_libs $LIBS"
3068 |     AC_CACHE_CHECK([whether a program can dlopen itself],
3069 | 	  lt_cv_dlopen_self, [dnl
3070 | 	  _LT_TRY_DLOPEN_SELF(
3071 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
3072 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
3075 |     if test "x$lt_cv_dlopen_self" = xyes; then
3077 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
3078 | 	  lt_cv_dlopen_self_static, [dnl
3079 | 	  _LT_TRY_DLOPEN_SELF(
3080 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
3081 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
3091 |   case $lt_cv_dlopen_self in
3092 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
3093 |   *) enable_dlopen_self=unknown ;;
3096 |   case $lt_cv_dlopen_self_static in
3097 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
3098 |   *) enable_dlopen_self_static=unknown ;;
3101 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
3102 | 	 [Whether dlopen is supported])
3103 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
3104 | 	 [Whether dlopen of programs is supported])
3105 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
3106 | 	 [Whether dlopen of statically linked programs is supported])
3107 | ])# LT_SYS_DLOPEN_SELF
3110 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
3112 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6428 |     [Compiler flag to allow reflexive dlopens])
6540 |   LT_SYS_DLOPEN_SELF
8820 | 			  _LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"])],
8821 | 	  [nonrecursive], [_LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"; lt_libobj_prefix="$lt_ltdl_dir/"])],
8995 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
9033 | LTDLOPEN=`eval "\\$ECHO \"$libname_spec\""`
9034 | AC_SUBST([LTDLOPEN])
9055 | # LT_SYS_DLOPEN_DEPLIBS
9057 | AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS],
9059 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
9060 |   [lt_cv_sys_dlopen_deplibs],
9061 |   [# PORTME does your system automatically load deplibs for dlopen?
9065 |   lt_cv_sys_dlopen_deplibs=unknown
9070 |     lt_cv_sys_dlopen_deplibs=unknown
9073 |     lt_cv_sys_dlopen_deplibs=yes
9078 |       lt_cv_sys_dlopen_deplibs=no
9085 |     lt_cv_sys_dlopen_deplibs=yes
9088 |     lt_cv_sys_dlopen_deplibs=yes
9092 |     lt_cv_sys_dlopen_deplibs=yes
9095 |     lt_cv_sys_dlopen_deplibs=yes
9098 |     lt_cv_sys_dlopen_deplibs=yes
9103 |     lt_cv_sys_dlopen_deplibs=unknown
9107 |     # at 6.2 and later dlopen does load deplibs.
9108 |     lt_cv_sys_dlopen_deplibs=yes
9111 |     lt_cv_sys_dlopen_deplibs=yes
9114 |     lt_cv_sys_dlopen_deplibs=yes
9117 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
9120 |     lt_cv_sys_dlopen_deplibs=no
9123 |     # dlopen *does* load deplibs and with the right loader patch applied
9129 |     lt_cv_sys_dlopen_deplibs=unknown
9136 |     lt_cv_sys_dlopen_deplibs=yes
9139 |     lt_cv_sys_dlopen_deplibs=yes
9142 |     lt_cv_sys_dlopen_deplibs=yes
9145 |     libltdl_cv_sys_dlopen_deplibs=yes
9149 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
9150 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
9151 |     [Define if the OS needs help to load dependent libraries for dlopen().])
9153 | ])# LT_SYS_DLOPEN_DEPLIBS
9156 | AU_ALIAS([AC_LTDL_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS])
9158 | dnl AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [])
9235 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
9259 | LIBADD_DLOPEN=
9260 | AC_SEARCH_LIBS([dlopen], [dl],
9263 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
9264 | 	  LIBADD_DLOPEN="-ldl"
9266 | 	libltdl_cv_lib_dl_dlopen="yes"
9267 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
9271 |     ]], [[dlopen(0, 0);]])],
9274 | 	    libltdl_cv_func_dlopen="yes"
9275 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
9276 | 	[AC_CHECK_LIB([svld], [dlopen],
9279 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
9280 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
9281 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
9284 |   LIBS="$LIBS $LIBADD_DLOPEN"
9288 | AC_SUBST([LIBADD_DLOPEN])
9294 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
9298 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
9308 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
9311 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
9315 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
9322 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
9338 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
9400 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
9401 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
9406 |           LIBS="$LIBS $LIBADD_DLOPEN"
9407 | 	  _LT_TRY_DLOPEN_SELF(
9703 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```