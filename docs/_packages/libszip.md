---
name: "libszip"
layout: package
next_package: log4cplus
previous_package: openmc
languages: ['bash']
---
## 2.1.1
3 / 57 files match

 - [aclocal.m4](#aclocalm4)
 - [bin/ltmain.sh](#binltmainsh)
 - [config/commence.in](#configcommencein)

### aclocal.m4

```

{% raw %}
3001 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
3004 | m4_defun([_LT_TRY_DLOPEN_SELF],
3062 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
3095 | ])# _LT_TRY_DLOPEN_SELF
3098 | # LT_SYS_DLOPEN_SELF
3100 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
3102 | if test yes != "$enable_dlopen"; then
3103 |   enable_dlopen=unknown
3104 |   enable_dlopen_self=unknown
3105 |   enable_dlopen_self_static=unknown
3107 |   lt_cv_dlopen=no
3108 |   lt_cv_dlopen_libs=
3112 |     lt_cv_dlopen=load_add_on
3113 |     lt_cv_dlopen_libs=
3114 |     lt_cv_dlopen_self=yes
3118 |     lt_cv_dlopen=LoadLibrary
3119 |     lt_cv_dlopen_libs=
3123 |     lt_cv_dlopen=dlopen
3124 |     lt_cv_dlopen_libs=
3129 |     AC_CHECK_LIB([dl], [dlopen],
3130 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
3131 |     lt_cv_dlopen=dyld
3132 |     lt_cv_dlopen_libs=
3133 |     lt_cv_dlopen_self=yes
3140 |     lt_cv_dlopen=dlopen
3141 |     lt_cv_dlopen_libs=
3142 |     lt_cv_dlopen_self=no
3147 | 	  [lt_cv_dlopen=shl_load],
3149 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
3150 | 	[AC_CHECK_FUNC([dlopen],
3151 | 	      [lt_cv_dlopen=dlopen],
3152 | 	  [AC_CHECK_LIB([dl], [dlopen],
3153 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
3154 | 	    [AC_CHECK_LIB([svld], [dlopen],
3155 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
3157 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
3166 |   if test no = "$lt_cv_dlopen"; then
3167 |     enable_dlopen=no
3169 |     enable_dlopen=yes
3172 |   case $lt_cv_dlopen in
3173 |   dlopen)
3181 |     LIBS="$lt_cv_dlopen_libs $LIBS"
3183 |     AC_CACHE_CHECK([whether a program can dlopen itself],
3184 | 	  lt_cv_dlopen_self, [dnl
3185 | 	  _LT_TRY_DLOPEN_SELF(
3186 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
3187 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
3190 |     if test yes = "$lt_cv_dlopen_self"; then
3192 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
3193 | 	  lt_cv_dlopen_self_static, [dnl
3194 | 	  _LT_TRY_DLOPEN_SELF(
3195 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
3196 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
3206 |   case $lt_cv_dlopen_self in
3207 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
3208 |   *) enable_dlopen_self=unknown ;;
3211 |   case $lt_cv_dlopen_self_static in
3212 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
3213 |   *) enable_dlopen_self_static=unknown ;;
3216 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
3217 | 	 [Whether dlopen is supported])
3218 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
3219 | 	 [Whether dlopen of programs is supported])
3220 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
3221 | 	 [Whether dlopen of statically linked programs is supported])
3222 | ])# LT_SYS_DLOPEN_SELF
3225 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
3227 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
7305 |     [Compiler flag to allow reflexive dlopens])
7414 |   LT_SYS_DLOPEN_SELF
9609 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
9643 | # dlopen
9645 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
9648 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
9649 | [_LT_SET_OPTION([LT_INIT], [dlopen])
9652 | put the 'dlopen' option into LT_INIT's first parameter.])
9656 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
10170 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### bin/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### config/commence.in

```

{% raw %}
50 | LT_LINK_EXE=$(LT) --mode=link $(CC) $(LT_STATIC_EXEC) -dlopen self -rpath $(libdir) $(DYNAMIC_DIRS)
{% endraw %}

```