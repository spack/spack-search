---
name: "zookeeper"
layout: package
next_package: pcre
previous_package: botan
languages: ['cpp', 'bash']
---
## 3.4.11
6 / 1552 files match

 - [src/c/ltmain.sh](#srccltmainsh)
 - [src/c/aclocal.m4](#srccaclocalm4)
 - [src/c/tests/LibCSymTable.cc](#srcctestslibcsymtablecc)
 - [src/c/autom4te.cache/output.0](#srccautom4tecacheoutput0)
 - [src/c/autom4te.cache/output.1](#srccautom4tecacheoutput1)
 - [src/c/autom4te.cache/traces.0](#srccautom4tecachetraces0)

### src/c/ltmain.sh

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
7346 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7414 | 	  # This library was specified with -dlopen.
7534 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7545 | 	passes="conv scan dlopen dlpreopen link"
7571 | 	dlopen) libs=$dlfiles ;;
7602 |       if test dlopen = "$pass"; then
7822 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7823 | 	      # If there is no dlopen support or we're linking statically,
7851 | 	dlopen=
7881 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7927 | 	# This library was specified with -dlopen.
7928 | 	if test dlopen = "$pass"; then
7930 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7932 | 	     test yes != "$dlopen_support" ||
7935 | 	    # If there is no dlname, no dlopen support or we're linking
7944 | 	fi # $pass = dlopen
8000 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8002 | 	      # We recover the dlopen module name by 'saving' the la file
8026 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8155 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8156 | 	  dlopenmodule=
8159 | 	      dlopenmodule=$dlpremoduletest
8163 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8260 | 		    # if the lib is a (non-dlopened) module then we cannot
8264 | 		      if test "X$dlopenmodule" != "X$lib"; then
8416 | 	      echo "*** a static module, that should work as long as the dlopening application"
8417 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8561 |       if test dlopen != "$pass"; then
8691 | 	func_warning "'-dlopen' is ignored for archives"
8758 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9455 | 	    echo "*** a static module, that should work as long as the dlopening"
9456 | 	    echo "*** application is linked with the -dlopen flag."
9474 | 	    echo "*** or is declared to -dlopen it."
10086 | 	func_warning "'-dlopen' is ignored for objects"
10206 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10207 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10888 | # The name that we can dlopen(3).
10917 | # Files to dlopen/dlpreopen
10918 | dlopen='$dlfiles'
{% endraw %}

```
### src/c/aclocal.m4

```

{% raw %}
3058 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
3061 | m4_defun([_LT_TRY_DLOPEN_SELF],
3119 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
3152 | ])# _LT_TRY_DLOPEN_SELF
3155 | # LT_SYS_DLOPEN_SELF
3157 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
3159 | if test yes != "$enable_dlopen"; then
3160 |   enable_dlopen=unknown
3161 |   enable_dlopen_self=unknown
3162 |   enable_dlopen_self_static=unknown
3164 |   lt_cv_dlopen=no
3165 |   lt_cv_dlopen_libs=
3169 |     lt_cv_dlopen=load_add_on
3170 |     lt_cv_dlopen_libs=
3171 |     lt_cv_dlopen_self=yes
3175 |     lt_cv_dlopen=LoadLibrary
3176 |     lt_cv_dlopen_libs=
3180 |     lt_cv_dlopen=dlopen
3181 |     lt_cv_dlopen_libs=
3186 |     AC_CHECK_LIB([dl], [dlopen],
3187 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
3188 |     lt_cv_dlopen=dyld
3189 |     lt_cv_dlopen_libs=
3190 |     lt_cv_dlopen_self=yes
3197 |     lt_cv_dlopen=dlopen
3198 |     lt_cv_dlopen_libs=
3199 |     lt_cv_dlopen_self=no
3204 | 	  [lt_cv_dlopen=shl_load],
3206 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
3207 | 	[AC_CHECK_FUNC([dlopen],
3208 | 	      [lt_cv_dlopen=dlopen],
3209 | 	  [AC_CHECK_LIB([dl], [dlopen],
3210 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
3211 | 	    [AC_CHECK_LIB([svld], [dlopen],
3212 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
3214 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
3223 |   if test no = "$lt_cv_dlopen"; then
3224 |     enable_dlopen=no
3226 |     enable_dlopen=yes
3229 |   case $lt_cv_dlopen in
3230 |   dlopen)
3238 |     LIBS="$lt_cv_dlopen_libs $LIBS"
3240 |     AC_CACHE_CHECK([whether a program can dlopen itself],
3241 | 	  lt_cv_dlopen_self, [dnl
3242 | 	  _LT_TRY_DLOPEN_SELF(
3243 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
3244 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
3247 |     if test yes = "$lt_cv_dlopen_self"; then
3249 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
3250 | 	  lt_cv_dlopen_self_static, [dnl
3251 | 	  _LT_TRY_DLOPEN_SELF(
3252 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
3253 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
3263 |   case $lt_cv_dlopen_self in
3264 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
3265 |   *) enable_dlopen_self=unknown ;;
3268 |   case $lt_cv_dlopen_self_static in
3269 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
3270 |   *) enable_dlopen_self_static=unknown ;;
3273 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
3274 | 	 [Whether dlopen is supported])
3275 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
3276 | 	 [Whether dlopen of programs is supported])
3277 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
3278 | 	 [Whether dlopen of statically linked programs is supported])
3279 | ])# LT_SYS_DLOPEN_SELF
3282 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
3284 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
7378 |     [Compiler flag to allow reflexive dlopens])
7487 |   LT_SYS_DLOPEN_SELF
9682 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
9716 | # dlopen
9718 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
9721 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
9722 | [_LT_SET_OPTION([LT_INIT], [dlopen])
9725 | put the 'dlopen' option into LT_INIT's first parameter.])
9729 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
10243 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### src/c/tests/LibCSymTable.cc

```cpp

{% raw %}
75 |         handle=dlopen("cygwin1.dll",RTLD_LAZY);
76 |         assert("Unable to dlopen global sym table"&&handle);
{% endraw %}

```
### src/c/autom4te.cache/output.0

```

{% raw %}
10476 |         enable_dlopen=no
14140 |   if test yes != "$enable_dlopen"; then
14141 |   enable_dlopen=unknown
14142 |   enable_dlopen_self=unknown
14143 |   enable_dlopen_self_static=unknown
14145 |   lt_cv_dlopen=no
14146 |   lt_cv_dlopen_libs=
14150 |     lt_cv_dlopen=load_add_on
14151 |     lt_cv_dlopen_libs=
14152 |     lt_cv_dlopen_self=yes
14156 |     lt_cv_dlopen=LoadLibrary
14157 |     lt_cv_dlopen_libs=
14161 |     lt_cv_dlopen=dlopen
14162 |     lt_cv_dlopen_libs=
14167 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14168 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14169 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14183 | char dlopen ();
14187 | return dlopen ();
14193 |   ac_cv_lib_dl_dlopen=yes
14195 |   ac_cv_lib_dl_dlopen=no
14201 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14202 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14203 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14204 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14207 |     lt_cv_dlopen=dyld
14208 |     lt_cv_dlopen_libs=
14209 |     lt_cv_dlopen_self=yes
14218 |     lt_cv_dlopen=dlopen
14219 |     lt_cv_dlopen_libs=
14220 |     lt_cv_dlopen_self=no
14226 |   lt_cv_dlopen=shl_load
14265 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
14267 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
14268 | if test "x$ac_cv_func_dlopen" = xyes; then :
14269 |   lt_cv_dlopen=dlopen
14271 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14272 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14273 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14287 | char dlopen ();
14291 | return dlopen ();
14297 |   ac_cv_lib_dl_dlopen=yes
14299 |   ac_cv_lib_dl_dlopen=no
14305 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14306 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14307 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14308 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14310 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14311 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14312 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14326 | char dlopen ();
14330 | return dlopen ();
14336 |   ac_cv_lib_svld_dlopen=yes
14338 |   ac_cv_lib_svld_dlopen=no
14344 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14345 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14346 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14347 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
14386 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
14407 |   if test no = "$lt_cv_dlopen"; then
14408 |     enable_dlopen=no
14410 |     enable_dlopen=yes
14413 |   case $lt_cv_dlopen in
14414 |   dlopen)
14422 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14424 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14425 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14426 | if ${lt_cv_dlopen_self+:} false; then :
14430 |   lt_cv_dlopen_self=cross
14485 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14512 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14513 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14514 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14518 |     lt_cv_dlopen_self=no
14525 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14526 | $as_echo "$lt_cv_dlopen_self" >&6; }
14528 |     if test yes = "$lt_cv_dlopen_self"; then
14530 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14531 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14532 | if ${lt_cv_dlopen_self_static+:} false; then :
14536 |   lt_cv_dlopen_self_static=cross
14591 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14618 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14619 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14620 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14624 |     lt_cv_dlopen_self_static=no
14631 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14632 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14641 |   case $lt_cv_dlopen_self in
14642 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14643 |   *) enable_dlopen_self=unknown ;;
14646 |   case $lt_cv_dlopen_self_static in
14647 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14648 |   *) enable_dlopen_self_static=unknown ;;
19541 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
19542 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
19543 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
20789 | # Whether dlopen is supported.
20790 | dlopen_support=$enable_dlopen
20792 | # Whether dlopen of programs is supported.
20793 | dlopen_self=$enable_dlopen_self
20795 | # Whether dlopen of statically linked programs is supported.
20796 | dlopen_self_static=$enable_dlopen_self_static
20840 | # Compiler flag to allow reflexive dlopens.
21082 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/c/autom4te.cache/output.1

```

{% raw %}
10476 |         enable_dlopen=no
14136 |   if test yes != "$enable_dlopen"; then
14137 |   enable_dlopen=unknown
14138 |   enable_dlopen_self=unknown
14139 |   enable_dlopen_self_static=unknown
14141 |   lt_cv_dlopen=no
14142 |   lt_cv_dlopen_libs=
14146 |     lt_cv_dlopen=load_add_on
14147 |     lt_cv_dlopen_libs=
14148 |     lt_cv_dlopen_self=yes
14152 |     lt_cv_dlopen=LoadLibrary
14153 |     lt_cv_dlopen_libs=
14157 |     lt_cv_dlopen=dlopen
14158 |     lt_cv_dlopen_libs=
14163 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14164 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14165 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14179 | char dlopen ();
14183 | return dlopen ();
14189 |   ac_cv_lib_dl_dlopen=yes
14191 |   ac_cv_lib_dl_dlopen=no
14197 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14198 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14199 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14200 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14203 |     lt_cv_dlopen=dyld
14204 |     lt_cv_dlopen_libs=
14205 |     lt_cv_dlopen_self=yes
14214 |     lt_cv_dlopen=dlopen
14215 |     lt_cv_dlopen_libs=
14216 |     lt_cv_dlopen_self=no
14222 |   lt_cv_dlopen=shl_load
14261 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
14263 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
14264 | if test "x$ac_cv_func_dlopen" = xyes; then :
14265 |   lt_cv_dlopen=dlopen
14267 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14268 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14269 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14283 | char dlopen ();
14287 | return dlopen ();
14293 |   ac_cv_lib_dl_dlopen=yes
14295 |   ac_cv_lib_dl_dlopen=no
14301 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14302 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14303 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14304 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
14306 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14307 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14308 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14322 | char dlopen ();
14326 | return dlopen ();
14332 |   ac_cv_lib_svld_dlopen=yes
14334 |   ac_cv_lib_svld_dlopen=no
14340 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14341 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14342 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14343 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
14382 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
14403 |   if test no = "$lt_cv_dlopen"; then
14404 |     enable_dlopen=no
14406 |     enable_dlopen=yes
14409 |   case $lt_cv_dlopen in
14410 |   dlopen)
14418 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14420 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14421 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14422 | if ${lt_cv_dlopen_self+:} false; then :
14426 |   lt_cv_dlopen_self=cross
14481 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14508 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14509 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14510 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14514 |     lt_cv_dlopen_self=no
14521 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14522 | $as_echo "$lt_cv_dlopen_self" >&6; }
14524 |     if test yes = "$lt_cv_dlopen_self"; then
14526 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14527 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14528 | if ${lt_cv_dlopen_self_static+:} false; then :
14532 |   lt_cv_dlopen_self_static=cross
14587 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14614 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14615 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14616 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14620 |     lt_cv_dlopen_self_static=no
14627 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14628 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14637 |   case $lt_cv_dlopen_self in
14638 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14639 |   *) enable_dlopen_self=unknown ;;
14642 |   case $lt_cv_dlopen_self_static in
14643 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14644 |   *) enable_dlopen_self_static=unknown ;;
19537 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
19538 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
19539 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
20785 | # Whether dlopen is supported.
20786 | dlopen_support=$enable_dlopen
20788 | # Whether dlopen of programs is supported.
20789 | dlopen_self=$enable_dlopen_self
20791 | # Whether dlopen of statically linked programs is supported.
20792 | dlopen_self_static=$enable_dlopen_self_static
20836 | # Compiler flag to allow reflexive dlopens.
21078 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/c/autom4te.cache/traces.0

```

{% raw %}
1248 | m4trace:/usr/share/aclocal/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
1249 | if test yes != "$enable_dlopen"; then
1250 |   enable_dlopen=unknown
1251 |   enable_dlopen_self=unknown
1252 |   enable_dlopen_self_static=unknown
1254 |   lt_cv_dlopen=no
1255 |   lt_cv_dlopen_libs=
1259 |     lt_cv_dlopen=load_add_on
1260 |     lt_cv_dlopen_libs=
1261 |     lt_cv_dlopen_self=yes
1265 |     lt_cv_dlopen=LoadLibrary
1266 |     lt_cv_dlopen_libs=
1270 |     lt_cv_dlopen=dlopen
1271 |     lt_cv_dlopen_libs=
1276 |     AC_CHECK_LIB([dl], [dlopen],
1277 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1278 |     lt_cv_dlopen=dyld
1279 |     lt_cv_dlopen_libs=
1280 |     lt_cv_dlopen_self=yes
1287 |     lt_cv_dlopen=dlopen
1288 |     lt_cv_dlopen_libs=
1289 |     lt_cv_dlopen_self=no
1294 | 	  [lt_cv_dlopen=shl_load],
1296 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1297 | 	[AC_CHECK_FUNC([dlopen],
1298 | 	      [lt_cv_dlopen=dlopen],
1299 | 	  [AC_CHECK_LIB([dl], [dlopen],
1300 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1301 | 	    [AC_CHECK_LIB([svld], [dlopen],
1302 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1304 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1313 |   if test no = "$lt_cv_dlopen"; then
1314 |     enable_dlopen=no
1316 |     enable_dlopen=yes
1319 |   case $lt_cv_dlopen in
1320 |   dlopen)
1328 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1330 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1331 | 	  lt_cv_dlopen_self, [dnl
1332 | 	  _LT_TRY_DLOPEN_SELF(
1333 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1334 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1337 |     if test yes = "$lt_cv_dlopen_self"; then
1339 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1340 | 	  lt_cv_dlopen_self_static, [dnl
1341 | 	  _LT_TRY_DLOPEN_SELF(
1342 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1343 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1353 |   case $lt_cv_dlopen_self in
1354 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1355 |   *) enable_dlopen_self=unknown ;;
1358 |   case $lt_cv_dlopen_self_static in
1359 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1360 |   *) enable_dlopen_self_static=unknown ;;
1363 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1364 | 	 [Whether dlopen is supported])
1365 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1366 | 	 [Whether dlopen of programs is supported])
1367 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1368 | 	 [Whether dlopen of statically linked programs is supported])
1370 | m4trace:/usr/share/aclocal/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1371 | m4trace:/usr/share/aclocal/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
1373 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1923 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1967 | eval "LTDLOPEN=\"$libname_spec\""
1968 | AC_SUBST([LTDLOPEN])
1970 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1971 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1972 |   [lt_cv_sys_dlopen_deplibs],
1973 |   [# PORTME does your system automatically load deplibs for dlopen?
1977 |   lt_cv_sys_dlopen_deplibs=unknown
1982 |     lt_cv_sys_dlopen_deplibs=unknown
1985 |     lt_cv_sys_dlopen_deplibs=yes
1990 |       lt_cv_sys_dlopen_deplibs=no
1995 |     lt_cv_sys_dlopen_deplibs=yes
2000 |     lt_cv_sys_dlopen_deplibs=yes
2003 |     lt_cv_sys_dlopen_deplibs=yes
2007 |     lt_cv_sys_dlopen_deplibs=yes
2010 |     lt_cv_sys_dlopen_deplibs=yes
2013 |     lt_cv_sys_dlopen_deplibs=yes
2018 |     lt_cv_sys_dlopen_deplibs=unknown
2022 |     # at 6.2 and later dlopen does load deplibs.
2023 |     lt_cv_sys_dlopen_deplibs=yes
2026 |     lt_cv_sys_dlopen_deplibs=yes
2029 |     lt_cv_sys_dlopen_deplibs=yes
2032 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
2035 |     lt_cv_sys_dlopen_deplibs=no
2038 |     # dlopen *does* load deplibs and with the right loader patch applied
2044 |     lt_cv_sys_dlopen_deplibs=unknown
2051 |     lt_cv_sys_dlopen_deplibs=yes
2054 |     lt_cv_sys_dlopen_deplibs=yes
2057 |     lt_cv_sys_dlopen_deplibs=yes
2060 |     libltdl_cv_sys_dlopen_deplibs=yes
2064 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
2065 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
2066 |     [Define if the OS needs help to load dependent libraries for dlopen().])
2069 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
2070 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
2072 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
2144 | LIBADD_DLOPEN=
2145 | AC_SEARCH_LIBS([dlopen], [dl],
2148 | 	if test "$ac_cv_search_dlopen" != "none required"; then
2149 | 	  LIBADD_DLOPEN=-ldl
2151 | 	libltdl_cv_lib_dl_dlopen=yes
2152 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
2156 |     ]], [[dlopen(0, 0);]])],
2159 | 	    libltdl_cv_func_dlopen=yes
2160 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
2161 | 	[AC_CHECK_LIB([svld], [dlopen],
2164 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
2165 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
2166 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
2169 |   LIBS="$LIBS $LIBADD_DLOPEN"
2173 | AC_SUBST([LIBADD_DLOPEN])
2179 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
2183 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
2193 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
2196 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
2200 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
2207 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
2223 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
2275 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
2280 |       LIBS="$LIBS $LIBADD_DLOPEN"
2338 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
2380 | m4trace:/usr/share/aclocal/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2383 | put the 'dlopen' option into LT_INIT's first parameter.])
2385 | m4trace:/usr/share/aclocal/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2387 | _LT_SET_OPTION([LT_INIT], [dlopen])
2390 | put the 'dlopen' option into LT_INIT's first parameter.])
2482 | m4trace:/usr/share/aclocal/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
3475 | m4trace:configure.ac:57: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```