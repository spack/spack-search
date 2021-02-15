---
name: "libsecret"
layout: package
next_package: protobuf
previous_package: py-notebook
languages: ['bash']
---
## 0.18.8
2 / 287 files match

 - [aclocal.m4](#aclocalm4)
 - [build/ltmain.sh](#buildltmainsh)

### aclocal.m4

```

{% raw %}
1621 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
4063 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
4066 | m4_defun([_LT_TRY_DLOPEN_SELF],
4124 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
4157 | ])# _LT_TRY_DLOPEN_SELF
4160 | # LT_SYS_DLOPEN_SELF
4162 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
4164 | if test yes != "$enable_dlopen"; then
4165 |   enable_dlopen=unknown
4166 |   enable_dlopen_self=unknown
4167 |   enable_dlopen_self_static=unknown
4169 |   lt_cv_dlopen=no
4170 |   lt_cv_dlopen_libs=
4174 |     lt_cv_dlopen=load_add_on
4175 |     lt_cv_dlopen_libs=
4176 |     lt_cv_dlopen_self=yes
4180 |     lt_cv_dlopen=LoadLibrary
4181 |     lt_cv_dlopen_libs=
4185 |     lt_cv_dlopen=dlopen
4186 |     lt_cv_dlopen_libs=
4191 |     AC_CHECK_LIB([dl], [dlopen],
4192 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
4193 |     lt_cv_dlopen=dyld
4194 |     lt_cv_dlopen_libs=
4195 |     lt_cv_dlopen_self=yes
4202 |     lt_cv_dlopen=dlopen
4203 |     lt_cv_dlopen_libs=
4204 |     lt_cv_dlopen_self=no
4209 | 	  [lt_cv_dlopen=shl_load],
4211 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
4212 | 	[AC_CHECK_FUNC([dlopen],
4213 | 	      [lt_cv_dlopen=dlopen],
4214 | 	  [AC_CHECK_LIB([dl], [dlopen],
4215 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
4216 | 	    [AC_CHECK_LIB([svld], [dlopen],
4217 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
4219 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
4228 |   if test no = "$lt_cv_dlopen"; then
4229 |     enable_dlopen=no
4231 |     enable_dlopen=yes
4234 |   case $lt_cv_dlopen in
4235 |   dlopen)
4243 |     LIBS="$lt_cv_dlopen_libs $LIBS"
4245 |     AC_CACHE_CHECK([whether a program can dlopen itself],
4246 | 	  lt_cv_dlopen_self, [dnl
4247 | 	  _LT_TRY_DLOPEN_SELF(
4248 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
4249 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
4252 |     if test yes = "$lt_cv_dlopen_self"; then
4254 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
4255 | 	  lt_cv_dlopen_self_static, [dnl
4256 | 	  _LT_TRY_DLOPEN_SELF(
4257 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
4258 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
4268 |   case $lt_cv_dlopen_self in
4269 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
4270 |   *) enable_dlopen_self=unknown ;;
4273 |   case $lt_cv_dlopen_self_static in
4274 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
4275 |   *) enable_dlopen_self_static=unknown ;;
4278 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
4279 | 	 [Whether dlopen is supported])
4280 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
4281 | 	 [Whether dlopen of programs is supported])
4282 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
4283 | 	 [Whether dlopen of statically linked programs is supported])
4284 | ])# LT_SYS_DLOPEN_SELF
4287 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
4289 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
8367 |     [Compiler flag to allow reflexive dlopens])
8476 |   LT_SYS_DLOPEN_SELF
10671 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
10705 | # dlopen
10707 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
10710 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
10711 | [_LT_SET_OPTION([LT_INIT], [dlopen])
10714 | put the 'dlopen' option into LT_INIT's first parameter.])
10718 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
11232 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### build/ltmain.sh

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
7345 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7413 | 	  # This library was specified with -dlopen.
7533 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7544 | 	passes="conv scan dlopen dlpreopen link"
7570 | 	dlopen) libs=$dlfiles ;;
7598 |       if test dlopen = "$pass"; then
7818 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7819 | 	      # If there is no dlopen support or we're linking statically,
7847 | 	dlopen=
7877 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7923 | 	# This library was specified with -dlopen.
7924 | 	if test dlopen = "$pass"; then
7926 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7928 | 	     test yes != "$dlopen_support" ||
7931 | 	    # If there is no dlname, no dlopen support or we're linking
7940 | 	fi # $pass = dlopen
7996 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7998 | 	      # We recover the dlopen module name by 'saving' the la file
8022 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8151 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8152 | 	  dlopenmodule=
8155 | 	      dlopenmodule=$dlpremoduletest
8159 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8256 | 		    # if the lib is a (non-dlopened) module then we cannot
8260 | 		      if test "X$dlopenmodule" != "X$lib"; then
8412 | 	      echo "*** a static module, that should work as long as the dlopening application"
8413 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8557 |       if test dlopen != "$pass"; then
8687 | 	func_warning "'-dlopen' is ignored for archives"
8754 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9448 | 	    echo "*** a static module, that should work as long as the dlopening"
9449 | 	    echo "*** application is linked with the -dlopen flag."
9467 | 	    echo "*** or is declared to -dlopen it."
10079 | 	func_warning "'-dlopen' is ignored for objects"
10199 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10200 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10881 | # The name that we can dlopen(3).
10910 | # Files to dlopen/dlpreopen
10911 | dlopen='$dlfiles'
{% endraw %}

```