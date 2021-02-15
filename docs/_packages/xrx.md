---
name: "xrx"
layout: package
next_package: rt-tests
previous_package: yoda
languages: ['bash']
---
## 1.0.4
2 / 73 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
885 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
946 |       -dlopen=*|--mode=*|--tag=*)
1036 |   # Only execute mode is allowed to have -dlopen flags.
1038 |     func_error "unrecognized option \`-dlopen'"
1672 |   -dlopen FILE      add the directory containing FILE to the library path
1674 | This mode sets the library path environment variable according to \`-dlopen'
1729 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1738 |   -module           build a library that can dlopened
1844 |     # Handle -dlopen flags immediately.
1861 | 	# Skip this library if it cannot be dlopened.
1888 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4436 | 	    dlopen_self=$dlopen_self_static
4442 | 	    dlopen_self=$dlopen_self_static
4448 | 	    dlopen_self=$dlopen_self_static
4506 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4590 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4752 |       -dlopen)
5140 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5207 | 	  # This library was specified with -dlopen.
5322 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5333 | 	passes="conv scan dlopen dlpreopen link"
5359 | 	dlopen) libs="$dlfiles" ;;
5386 |       if test "$pass" = dlopen; then
5598 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5599 | 	      # If there is no dlopen support or we're linking statically,
5629 | 	dlopen=
5659 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5699 | 	# This library was specified with -dlopen.
5700 | 	if test "$pass" = dlopen; then
5702 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5705 | 	     test "$dlopen_support" != yes ||
5707 | 	    # If there is no dlname, no dlopen support or we're linking
5716 | 	fi # $pass = dlopen
5774 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5900 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5901 | 	  dlopenmodule=""
5904 | 	      dlopenmodule="$dlpremoduletest"
5908 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6005 | 		    # if the lib is a (non-dlopened) module then we can not
6009 | 		      if test "X$dlopenmodule" != "X$lib"; then
6161 | 	      echo "*** a static module, that should work as long as the dlopening application"
6162 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
6298 |       if test "$pass" != dlopen; then
6397 | 	func_warning "\`-dlopen' is ignored for archives"
6464 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7126 | 	    echo "*** a static module, that should work as long as the dlopening"
7127 | 	    echo "*** application is linked with the -dlopen flag."
7145 | 	    echo "*** or is declared to -dlopen it."
7716 | 	func_warning "\`-dlopen' is ignored for objects"
7831 |         && test "$dlopen_support" = unknown \
7832 | 	&& test "$dlopen_self" = unknown \
7833 | 	&& test "$dlopen_self_static" = unknown && \
7834 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8473 | # The name that we can dlopen(3).
8502 | # Files to dlopen/dlpreopen
8503 | dlopen='$dlfiles'
{% endraw %}

```
### aclocal.m4

```

{% raw %}
4121 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
4124 | m4_defun([_LT_TRY_DLOPEN_SELF],
4182 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
4215 | ])# _LT_TRY_DLOPEN_SELF
4218 | # LT_SYS_DLOPEN_SELF
4220 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
4222 | if test "x$enable_dlopen" != xyes; then
4223 |   enable_dlopen=unknown
4224 |   enable_dlopen_self=unknown
4225 |   enable_dlopen_self_static=unknown
4227 |   lt_cv_dlopen=no
4228 |   lt_cv_dlopen_libs=
4232 |     lt_cv_dlopen="load_add_on"
4233 |     lt_cv_dlopen_libs=
4234 |     lt_cv_dlopen_self=yes
4238 |     lt_cv_dlopen="LoadLibrary"
4239 |     lt_cv_dlopen_libs=
4243 |     lt_cv_dlopen="dlopen"
4244 |     lt_cv_dlopen_libs=
4249 |     AC_CHECK_LIB([dl], [dlopen],
4250 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
4251 |     lt_cv_dlopen="dyld"
4252 |     lt_cv_dlopen_libs=
4253 |     lt_cv_dlopen_self=yes
4259 | 	  [lt_cv_dlopen="shl_load"],
4261 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
4262 | 	[AC_CHECK_FUNC([dlopen],
4263 | 	      [lt_cv_dlopen="dlopen"],
4264 | 	  [AC_CHECK_LIB([dl], [dlopen],
4265 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
4266 | 	    [AC_CHECK_LIB([svld], [dlopen],
4267 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
4269 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
4278 |   if test "x$lt_cv_dlopen" != xno; then
4279 |     enable_dlopen=yes
4281 |     enable_dlopen=no
4284 |   case $lt_cv_dlopen in
4285 |   dlopen)
4293 |     LIBS="$lt_cv_dlopen_libs $LIBS"
4295 |     AC_CACHE_CHECK([whether a program can dlopen itself],
4296 | 	  lt_cv_dlopen_self, [dnl
4297 | 	  _LT_TRY_DLOPEN_SELF(
4298 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
4299 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
4302 |     if test "x$lt_cv_dlopen_self" = xyes; then
4304 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
4305 | 	  lt_cv_dlopen_self_static, [dnl
4306 | 	  _LT_TRY_DLOPEN_SELF(
4307 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
4308 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
4318 |   case $lt_cv_dlopen_self in
4319 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
4320 |   *) enable_dlopen_self=unknown ;;
4323 |   case $lt_cv_dlopen_self_static in
4324 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
4325 |   *) enable_dlopen_self_static=unknown ;;
4328 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
4329 | 	 [Whether dlopen is supported])
4330 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
4331 | 	 [Whether dlopen of programs is supported])
4332 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
4333 | 	 [Whether dlopen of statically linked programs is supported])
4334 | ])# LT_SYS_DLOPEN_SELF
4337 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
4339 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
7777 |     [Compiler flag to allow reflexive dlopens])
7889 |   LT_SYS_DLOPEN_SELF
10014 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
10046 | # dlopen
10048 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
10051 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
10052 | [_LT_SET_OPTION([LT_INIT], [dlopen])
10055 | put the `dlopen' option into LT_INIT's first parameter.])
10059 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
10505 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```