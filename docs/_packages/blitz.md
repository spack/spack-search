---
name: "blitz"
layout: package
next_package: iegenlib
previous_package: cmockery
languages: ['bash']
---
## 1.0.1
14 / 894 files match

 - [config/ltmain.sh](#configltmainsh)
 - [autom4te.cache/output.3](#autom4tecacheoutput3)
 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [autom4te.cache/traces.6](#autom4tecachetraces6)
 - [autom4te.cache/output.1](#autom4tecacheoutput1)
 - [autom4te.cache/output.2](#autom4tecacheoutput2)
 - [autom4te.cache/output.5](#autom4tecacheoutput5)
 - [autom4te.cache/traces.0](#autom4tecachetraces0)
 - [autom4te.cache/traces.5](#autom4tecachetraces5)
 - [autom4te.cache/output.6](#autom4tecacheoutput6)
 - [autom4te.cache/output.4](#autom4tecacheoutput4)
 - [autom4te.cache/traces.2](#autom4tecachetraces2)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)

### config/ltmain.sh

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
### autom4te.cache/output.3

```

{% raw %}
10537 |         enable_dlopen=no
13879 |   if test "x$enable_dlopen" != xyes; then
13880 |   enable_dlopen=unknown
13881 |   enable_dlopen_self=unknown
13882 |   enable_dlopen_self_static=unknown
13884 |   lt_cv_dlopen=no
13885 |   lt_cv_dlopen_libs=
13889 |     lt_cv_dlopen="load_add_on"
13890 |     lt_cv_dlopen_libs=
13891 |     lt_cv_dlopen_self=yes
13895 |     lt_cv_dlopen="LoadLibrary"
13896 |     lt_cv_dlopen_libs=
13900 |     lt_cv_dlopen="dlopen"
13901 |     lt_cv_dlopen_libs=
13906 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
13907 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
13908 | if ${ac_cv_lib_dl_dlopen+:} false; then :
13922 | char dlopen ();
13926 | return dlopen ();
13932 |   ac_cv_lib_dl_dlopen=yes
13934 |   ac_cv_lib_dl_dlopen=no
13940 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
13941 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
13942 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
13943 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
13946 |     lt_cv_dlopen="dyld"
13947 |     lt_cv_dlopen_libs=
13948 |     lt_cv_dlopen_self=yes
13957 |   lt_cv_dlopen="shl_load"
13996 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
13998 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
13999 | if test "x$ac_cv_func_dlopen" = xyes; then :
14000 |   lt_cv_dlopen="dlopen"
14002 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14003 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14004 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14018 | char dlopen ();
14022 | return dlopen ();
14028 |   ac_cv_lib_dl_dlopen=yes
14030 |   ac_cv_lib_dl_dlopen=no
14036 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14037 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14038 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14039 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14041 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14042 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14043 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14057 | char dlopen ();
14061 | return dlopen ();
14067 |   ac_cv_lib_svld_dlopen=yes
14069 |   ac_cv_lib_svld_dlopen=no
14075 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14076 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14077 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14078 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
14117 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
14138 |   if test "x$lt_cv_dlopen" != xno; then
14139 |     enable_dlopen=yes
14141 |     enable_dlopen=no
14144 |   case $lt_cv_dlopen in
14145 |   dlopen)
14153 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14155 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14156 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14157 | if ${lt_cv_dlopen_self+:} false; then :
14161 |   lt_cv_dlopen_self=cross
14216 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14243 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14244 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14245 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14249 |     lt_cv_dlopen_self=no
14256 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14257 | $as_echo "$lt_cv_dlopen_self" >&6; }
14259 |     if test "x$lt_cv_dlopen_self" = xyes; then
14261 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14262 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14263 | if ${lt_cv_dlopen_self_static+:} false; then :
14267 |   lt_cv_dlopen_self_static=cross
14322 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14349 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14350 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14351 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14355 |     lt_cv_dlopen_self_static=no
14362 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14363 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14372 |   case $lt_cv_dlopen_self in
14373 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14374 |   *) enable_dlopen_self=unknown ;;
14377 |   case $lt_cv_dlopen_self_static in
14378 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14379 |   *) enable_dlopen_self_static=unknown ;;
28141 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
28142 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
28143 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
30775 | # Whether dlopen is supported.
30776 | dlopen_support=$enable_dlopen
30778 | # Whether dlopen of programs is supported.
30779 | dlopen_self=$enable_dlopen_self
30781 | # Whether dlopen of statically linked programs is supported.
30782 | dlopen_self_static=$enable_dlopen_self_static
30826 | # Compiler flag to allow reflexive dlopens.
31168 | # Compiler flag to allow reflexive dlopens.
31321 | # Compiler flag to allow reflexive dlopens.
31474 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.0

```

{% raw %}
10537 |         enable_dlopen=no
13879 |   if test "x$enable_dlopen" != xyes; then
13880 |   enable_dlopen=unknown
13881 |   enable_dlopen_self=unknown
13882 |   enable_dlopen_self_static=unknown
13884 |   lt_cv_dlopen=no
13885 |   lt_cv_dlopen_libs=
13889 |     lt_cv_dlopen="load_add_on"
13890 |     lt_cv_dlopen_libs=
13891 |     lt_cv_dlopen_self=yes
13895 |     lt_cv_dlopen="LoadLibrary"
13896 |     lt_cv_dlopen_libs=
13900 |     lt_cv_dlopen="dlopen"
13901 |     lt_cv_dlopen_libs=
13906 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
13907 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
13908 | if ${ac_cv_lib_dl_dlopen+:} false; then :
13922 | char dlopen ();
13926 | return dlopen ();
13932 |   ac_cv_lib_dl_dlopen=yes
13934 |   ac_cv_lib_dl_dlopen=no
13940 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
13941 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
13942 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
13943 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
13946 |     lt_cv_dlopen="dyld"
13947 |     lt_cv_dlopen_libs=
13948 |     lt_cv_dlopen_self=yes
13957 |   lt_cv_dlopen="shl_load"
13996 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
13998 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
13999 | if test "x$ac_cv_func_dlopen" = xyes; then :
14000 |   lt_cv_dlopen="dlopen"
14002 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14003 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14004 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14018 | char dlopen ();
14022 | return dlopen ();
14028 |   ac_cv_lib_dl_dlopen=yes
14030 |   ac_cv_lib_dl_dlopen=no
14036 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14037 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14038 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14039 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14041 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14042 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14043 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14057 | char dlopen ();
14061 | return dlopen ();
14067 |   ac_cv_lib_svld_dlopen=yes
14069 |   ac_cv_lib_svld_dlopen=no
14075 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14076 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14077 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14078 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
14117 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
14138 |   if test "x$lt_cv_dlopen" != xno; then
14139 |     enable_dlopen=yes
14141 |     enable_dlopen=no
14144 |   case $lt_cv_dlopen in
14145 |   dlopen)
14153 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14155 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14156 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14157 | if ${lt_cv_dlopen_self+:} false; then :
14161 |   lt_cv_dlopen_self=cross
14216 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14243 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14244 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14245 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14249 |     lt_cv_dlopen_self=no
14256 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14257 | $as_echo "$lt_cv_dlopen_self" >&6; }
14259 |     if test "x$lt_cv_dlopen_self" = xyes; then
14261 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14262 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14263 | if ${lt_cv_dlopen_self_static+:} false; then :
14267 |   lt_cv_dlopen_self_static=cross
14322 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14349 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14350 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14351 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14355 |     lt_cv_dlopen_self_static=no
14362 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14363 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14372 |   case $lt_cv_dlopen_self in
14373 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14374 |   *) enable_dlopen_self=unknown ;;
14377 |   case $lt_cv_dlopen_self_static in
14378 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14379 |   *) enable_dlopen_self_static=unknown ;;
28141 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
28142 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
28143 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
30775 | # Whether dlopen is supported.
30776 | dlopen_support=$enable_dlopen
30778 | # Whether dlopen of programs is supported.
30779 | dlopen_self=$enable_dlopen_self
30781 | # Whether dlopen of statically linked programs is supported.
30782 | dlopen_self_static=$enable_dlopen_self_static
30826 | # Compiler flag to allow reflexive dlopens.
31168 | # Compiler flag to allow reflexive dlopens.
31321 | # Compiler flag to allow reflexive dlopens.
31474 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.6

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/Users/rpfische/macports/share/aclocal/ltdl.m4:542: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
290 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
291 |   [lt_cv_sys_dlopen_deplibs],
292 |   [# PORTME does your system automatically load deplibs for dlopen?
296 |   lt_cv_sys_dlopen_deplibs=unknown
301 |     lt_cv_sys_dlopen_deplibs=unknown
304 |     lt_cv_sys_dlopen_deplibs=yes
309 |       lt_cv_sys_dlopen_deplibs=no
314 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
326 |     lt_cv_sys_dlopen_deplibs=yes
329 |     lt_cv_sys_dlopen_deplibs=yes
332 |     lt_cv_sys_dlopen_deplibs=yes
337 |     lt_cv_sys_dlopen_deplibs=unknown
341 |     # at 6.2 and later dlopen does load deplibs.
342 |     lt_cv_sys_dlopen_deplibs=yes
345 |     lt_cv_sys_dlopen_deplibs=yes
348 |     lt_cv_sys_dlopen_deplibs=yes
351 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
354 |     lt_cv_sys_dlopen_deplibs=no
357 |     # dlopen *does* load deplibs and with the right loader patch applied
363 |     lt_cv_sys_dlopen_deplibs=unknown
370 |     lt_cv_sys_dlopen_deplibs=yes
373 |     lt_cv_sys_dlopen_deplibs=yes
376 |     lt_cv_sys_dlopen_deplibs=yes
379 |     libltdl_cv_sys_dlopen_deplibs=yes
383 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
384 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
385 |     [Define if the OS needs help to load dependent libraries for dlopen().])
388 | m4trace:/Users/rpfische/macports/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/Users/rpfische/macports/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
391 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
463 | LIBADD_DLOPEN=
464 | AC_SEARCH_LIBS([dlopen], [dl],
467 | 	if test "$ac_cv_search_dlopen" != "none required"; then
468 | 	  LIBADD_DLOPEN=-ldl
470 | 	libltdl_cv_lib_dl_dlopen=yes
471 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
475 |     ]], [[dlopen(0, 0);]])],
478 | 	    libltdl_cv_func_dlopen=yes
479 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
480 | 	[AC_CHECK_LIB([svld], [dlopen],
483 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
484 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
485 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
488 |   LIBS="$LIBS $LIBADD_DLOPEN"
492 | AC_SUBST([LIBADD_DLOPEN])
498 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
502 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
512 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
515 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
519 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
526 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
542 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
594 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
599 |       LIBS="$LIBS $LIBADD_DLOPEN"
657 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
4362 | m4trace:m4/libtool.m4:1958: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
4363 | if test "x$enable_dlopen" != xyes; then
4364 |   enable_dlopen=unknown
4365 |   enable_dlopen_self=unknown
4366 |   enable_dlopen_self_static=unknown
4368 |   lt_cv_dlopen=no
4369 |   lt_cv_dlopen_libs=
4373 |     lt_cv_dlopen="load_add_on"
4374 |     lt_cv_dlopen_libs=
4375 |     lt_cv_dlopen_self=yes
4379 |     lt_cv_dlopen="LoadLibrary"
4380 |     lt_cv_dlopen_libs=
4384 |     lt_cv_dlopen="dlopen"
4385 |     lt_cv_dlopen_libs=
4390 |     AC_CHECK_LIB([dl], [dlopen],
4391 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
4392 |     lt_cv_dlopen="dyld"
4393 |     lt_cv_dlopen_libs=
4394 |     lt_cv_dlopen_self=yes
4400 | 	  [lt_cv_dlopen="shl_load"],
4402 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
4403 | 	[AC_CHECK_FUNC([dlopen],
4404 | 	      [lt_cv_dlopen="dlopen"],
4405 | 	  [AC_CHECK_LIB([dl], [dlopen],
4406 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
4407 | 	    [AC_CHECK_LIB([svld], [dlopen],
4408 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
4410 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
4419 |   if test "x$lt_cv_dlopen" != xno; then
4420 |     enable_dlopen=yes
4422 |     enable_dlopen=no
4425 |   case $lt_cv_dlopen in
4426 |   dlopen)
4434 |     LIBS="$lt_cv_dlopen_libs $LIBS"
4436 |     AC_CACHE_CHECK([whether a program can dlopen itself],
4437 | 	  lt_cv_dlopen_self, [dnl
4438 | 	  _LT_TRY_DLOPEN_SELF(
4439 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
4440 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
4443 |     if test "x$lt_cv_dlopen_self" = xyes; then
4445 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
4446 | 	  lt_cv_dlopen_self_static, [dnl
4447 | 	  _LT_TRY_DLOPEN_SELF(
4448 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
4449 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
4459 |   case $lt_cv_dlopen_self in
4460 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
4461 |   *) enable_dlopen_self=unknown ;;
4464 |   case $lt_cv_dlopen_self_static in
4465 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
4466 |   *) enable_dlopen_self_static=unknown ;;
4469 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
4470 | 	 [Whether dlopen is supported])
4471 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
4472 | 	 [Whether dlopen of programs is supported])
4473 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
4474 | 	 [Whether dlopen of statically linked programs is supported])
4476 | m4trace:m4/libtool.m4:1961: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
4477 | m4trace:m4/libtool.m4:1961: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
4479 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
4775 | m4trace:m4/ltoptions.m4:116: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
4778 | put the `dlopen' option into LT_INIT's first parameter.])
4780 | m4trace:m4/ltoptions.m4:116: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
4782 | _LT_SET_OPTION([LT_INIT], [dlopen])
4785 | put the `dlopen' option into LT_INIT's first parameter.])
4877 | m4trace:m4/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
5284 | m4trace:configure.ac:85: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### autom4te.cache/output.1

```

{% raw %}
10537 |         enable_dlopen=no
13879 |   if test "x$enable_dlopen" != xyes; then
13880 |   enable_dlopen=unknown
13881 |   enable_dlopen_self=unknown
13882 |   enable_dlopen_self_static=unknown
13884 |   lt_cv_dlopen=no
13885 |   lt_cv_dlopen_libs=
13889 |     lt_cv_dlopen="load_add_on"
13890 |     lt_cv_dlopen_libs=
13891 |     lt_cv_dlopen_self=yes
13895 |     lt_cv_dlopen="LoadLibrary"
13896 |     lt_cv_dlopen_libs=
13900 |     lt_cv_dlopen="dlopen"
13901 |     lt_cv_dlopen_libs=
13906 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
13907 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
13908 | if ${ac_cv_lib_dl_dlopen+:} false; then :
13922 | char dlopen ();
13926 | return dlopen ();
13932 |   ac_cv_lib_dl_dlopen=yes
13934 |   ac_cv_lib_dl_dlopen=no
13940 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
13941 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
13942 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
13943 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
13946 |     lt_cv_dlopen="dyld"
13947 |     lt_cv_dlopen_libs=
13948 |     lt_cv_dlopen_self=yes
13957 |   lt_cv_dlopen="shl_load"
13996 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
13998 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
13999 | if test "x$ac_cv_func_dlopen" = xyes; then :
14000 |   lt_cv_dlopen="dlopen"
14002 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14003 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14004 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14018 | char dlopen ();
14022 | return dlopen ();
14028 |   ac_cv_lib_dl_dlopen=yes
14030 |   ac_cv_lib_dl_dlopen=no
14036 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14037 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14038 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14039 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14041 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14042 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14043 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14057 | char dlopen ();
14061 | return dlopen ();
14067 |   ac_cv_lib_svld_dlopen=yes
14069 |   ac_cv_lib_svld_dlopen=no
14075 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14076 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14077 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14078 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
14117 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
14138 |   if test "x$lt_cv_dlopen" != xno; then
14139 |     enable_dlopen=yes
14141 |     enable_dlopen=no
14144 |   case $lt_cv_dlopen in
14145 |   dlopen)
14153 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14155 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14156 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14157 | if ${lt_cv_dlopen_self+:} false; then :
14161 |   lt_cv_dlopen_self=cross
14216 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14243 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14244 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14245 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14249 |     lt_cv_dlopen_self=no
14256 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14257 | $as_echo "$lt_cv_dlopen_self" >&6; }
14259 |     if test "x$lt_cv_dlopen_self" = xyes; then
14261 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14262 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14263 | if ${lt_cv_dlopen_self_static+:} false; then :
14267 |   lt_cv_dlopen_self_static=cross
14322 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14349 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14350 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14351 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14355 |     lt_cv_dlopen_self_static=no
14362 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14363 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14372 |   case $lt_cv_dlopen_self in
14373 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14374 |   *) enable_dlopen_self=unknown ;;
14377 |   case $lt_cv_dlopen_self_static in
14378 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14379 |   *) enable_dlopen_self_static=unknown ;;
28141 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
28142 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
28143 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
30775 | # Whether dlopen is supported.
30776 | dlopen_support=$enable_dlopen
30778 | # Whether dlopen of programs is supported.
30779 | dlopen_self=$enable_dlopen_self
30781 | # Whether dlopen of statically linked programs is supported.
30782 | dlopen_self_static=$enable_dlopen_self_static
30826 | # Compiler flag to allow reflexive dlopens.
31168 | # Compiler flag to allow reflexive dlopens.
31321 | # Compiler flag to allow reflexive dlopens.
31474 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.2

```

{% raw %}
10537 |         enable_dlopen=no
13879 |   if test "x$enable_dlopen" != xyes; then
13880 |   enable_dlopen=unknown
13881 |   enable_dlopen_self=unknown
13882 |   enable_dlopen_self_static=unknown
13884 |   lt_cv_dlopen=no
13885 |   lt_cv_dlopen_libs=
13889 |     lt_cv_dlopen="load_add_on"
13890 |     lt_cv_dlopen_libs=
13891 |     lt_cv_dlopen_self=yes
13895 |     lt_cv_dlopen="LoadLibrary"
13896 |     lt_cv_dlopen_libs=
13900 |     lt_cv_dlopen="dlopen"
13901 |     lt_cv_dlopen_libs=
13906 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
13907 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
13908 | if ${ac_cv_lib_dl_dlopen+:} false; then :
13922 | char dlopen ();
13926 | return dlopen ();
13932 |   ac_cv_lib_dl_dlopen=yes
13934 |   ac_cv_lib_dl_dlopen=no
13940 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
13941 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
13942 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
13943 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
13946 |     lt_cv_dlopen="dyld"
13947 |     lt_cv_dlopen_libs=
13948 |     lt_cv_dlopen_self=yes
13957 |   lt_cv_dlopen="shl_load"
13996 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
13998 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
13999 | if test "x$ac_cv_func_dlopen" = xyes; then :
14000 |   lt_cv_dlopen="dlopen"
14002 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14003 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14004 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14018 | char dlopen ();
14022 | return dlopen ();
14028 |   ac_cv_lib_dl_dlopen=yes
14030 |   ac_cv_lib_dl_dlopen=no
14036 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14037 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14038 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14039 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14041 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14042 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14043 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14057 | char dlopen ();
14061 | return dlopen ();
14067 |   ac_cv_lib_svld_dlopen=yes
14069 |   ac_cv_lib_svld_dlopen=no
14075 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14076 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14077 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14078 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
14117 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
14138 |   if test "x$lt_cv_dlopen" != xno; then
14139 |     enable_dlopen=yes
14141 |     enable_dlopen=no
14144 |   case $lt_cv_dlopen in
14145 |   dlopen)
14153 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14155 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14156 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14157 | if ${lt_cv_dlopen_self+:} false; then :
14161 |   lt_cv_dlopen_self=cross
14216 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14243 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14244 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14245 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14249 |     lt_cv_dlopen_self=no
14256 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14257 | $as_echo "$lt_cv_dlopen_self" >&6; }
14259 |     if test "x$lt_cv_dlopen_self" = xyes; then
14261 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14262 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14263 | if ${lt_cv_dlopen_self_static+:} false; then :
14267 |   lt_cv_dlopen_self_static=cross
14322 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14349 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14350 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14351 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14355 |     lt_cv_dlopen_self_static=no
14362 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14363 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14372 |   case $lt_cv_dlopen_self in
14373 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14374 |   *) enable_dlopen_self=unknown ;;
14377 |   case $lt_cv_dlopen_self_static in
14378 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14379 |   *) enable_dlopen_self_static=unknown ;;
28141 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
28142 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
28143 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
30775 | # Whether dlopen is supported.
30776 | dlopen_support=$enable_dlopen
30778 | # Whether dlopen of programs is supported.
30779 | dlopen_self=$enable_dlopen_self
30781 | # Whether dlopen of statically linked programs is supported.
30782 | dlopen_self_static=$enable_dlopen_self_static
30826 | # Compiler flag to allow reflexive dlopens.
31168 | # Compiler flag to allow reflexive dlopens.
31321 | # Compiler flag to allow reflexive dlopens.
31474 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.5

```

{% raw %}
10001 |         enable_dlopen=no
13619 |   if test yes != "$enable_dlopen"; then
13620 |   enable_dlopen=unknown
13621 |   enable_dlopen_self=unknown
13622 |   enable_dlopen_self_static=unknown
13624 |   lt_cv_dlopen=no
13625 |   lt_cv_dlopen_libs=
13629 |     lt_cv_dlopen=load_add_on
13630 |     lt_cv_dlopen_libs=
13631 |     lt_cv_dlopen_self=yes
13635 |     lt_cv_dlopen=LoadLibrary
13636 |     lt_cv_dlopen_libs=
13640 |     lt_cv_dlopen=dlopen
13641 |     lt_cv_dlopen_libs=
13646 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
13647 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
13648 | if ${ac_cv_lib_dl_dlopen+:} false; then :
13662 | char dlopen ();
13666 | return dlopen ();
13672 |   ac_cv_lib_dl_dlopen=yes
13674 |   ac_cv_lib_dl_dlopen=no
13680 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
13681 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
13682 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
13683 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
13686 |     lt_cv_dlopen=dyld
13687 |     lt_cv_dlopen_libs=
13688 |     lt_cv_dlopen_self=yes
13697 |     lt_cv_dlopen=dlopen
13698 |     lt_cv_dlopen_libs=
13699 |     lt_cv_dlopen_self=no
13705 |   lt_cv_dlopen=shl_load
13744 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
13746 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
13747 | if test "x$ac_cv_func_dlopen" = xyes; then :
13748 |   lt_cv_dlopen=dlopen
13750 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
13751 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
13752 | if ${ac_cv_lib_dl_dlopen+:} false; then :
13766 | char dlopen ();
13770 | return dlopen ();
13776 |   ac_cv_lib_dl_dlopen=yes
13778 |   ac_cv_lib_dl_dlopen=no
13784 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
13785 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
13786 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
13787 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
13789 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
13790 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
13791 | if ${ac_cv_lib_svld_dlopen+:} false; then :
13805 | char dlopen ();
13809 | return dlopen ();
13815 |   ac_cv_lib_svld_dlopen=yes
13817 |   ac_cv_lib_svld_dlopen=no
13823 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
13824 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
13825 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
13826 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
13865 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
13886 |   if test no = "$lt_cv_dlopen"; then
13887 |     enable_dlopen=no
13889 |     enable_dlopen=yes
13892 |   case $lt_cv_dlopen in
13893 |   dlopen)
13901 |     LIBS="$lt_cv_dlopen_libs $LIBS"
13903 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
13904 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
13905 | if ${lt_cv_dlopen_self+:} false; then :
13909 |   lt_cv_dlopen_self=cross
13964 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13991 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
13992 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
13993 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
13997 |     lt_cv_dlopen_self=no
14004 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14005 | $as_echo "$lt_cv_dlopen_self" >&6; }
14007 |     if test yes = "$lt_cv_dlopen_self"; then
14009 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14010 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14011 | if ${lt_cv_dlopen_self_static+:} false; then :
14015 |   lt_cv_dlopen_self_static=cross
14070 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14097 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14098 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14099 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14103 |     lt_cv_dlopen_self_static=no
14110 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14111 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14120 |   case $lt_cv_dlopen_self in
14121 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14122 |   *) enable_dlopen_self=unknown ;;
14125 |   case $lt_cv_dlopen_self_static in
14126 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14127 |   *) enable_dlopen_self_static=unknown ;;
25502 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
25503 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
25504 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
26961 | # Whether dlopen is supported.
26962 | dlopen_support=$enable_dlopen
26964 | # Whether dlopen of programs is supported.
26965 | dlopen_self=$enable_dlopen_self
26967 | # Whether dlopen of statically linked programs is supported.
26968 | dlopen_self_static=$enable_dlopen_self_static
27012 | # Compiler flag to allow reflexive dlopens.
27254 | # Compiler flag to allow reflexive dlopens.
27407 | # Compiler flag to allow reflexive dlopens.
27560 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.0

```

{% raw %}
474 | m4trace:/usr/share/aclocal/libtool.m4:1844: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
475 | if test "x$enable_dlopen" != xyes; then
476 |   enable_dlopen=unknown
477 |   enable_dlopen_self=unknown
478 |   enable_dlopen_self_static=unknown
480 |   lt_cv_dlopen=no
481 |   lt_cv_dlopen_libs=
485 |     lt_cv_dlopen="load_add_on"
486 |     lt_cv_dlopen_libs=
487 |     lt_cv_dlopen_self=yes
491 |     lt_cv_dlopen="LoadLibrary"
492 |     lt_cv_dlopen_libs=
496 |     lt_cv_dlopen="dlopen"
497 |     lt_cv_dlopen_libs=
502 |     AC_CHECK_LIB([dl], [dlopen],
503 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
504 |     lt_cv_dlopen="dyld"
505 |     lt_cv_dlopen_libs=
506 |     lt_cv_dlopen_self=yes
512 | 	  [lt_cv_dlopen="shl_load"],
514 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
515 | 	[AC_CHECK_FUNC([dlopen],
516 | 	      [lt_cv_dlopen="dlopen"],
517 | 	  [AC_CHECK_LIB([dl], [dlopen],
518 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
519 | 	    [AC_CHECK_LIB([svld], [dlopen],
520 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
522 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
531 |   if test "x$lt_cv_dlopen" != xno; then
532 |     enable_dlopen=yes
534 |     enable_dlopen=no
537 |   case $lt_cv_dlopen in
538 |   dlopen)
546 |     LIBS="$lt_cv_dlopen_libs $LIBS"
548 |     AC_CACHE_CHECK([whether a program can dlopen itself],
549 | 	  lt_cv_dlopen_self, [dnl
550 | 	  _LT_TRY_DLOPEN_SELF(
551 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
552 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
555 |     if test "x$lt_cv_dlopen_self" = xyes; then
557 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
558 | 	  lt_cv_dlopen_self_static, [dnl
559 | 	  _LT_TRY_DLOPEN_SELF(
560 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
561 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
571 |   case $lt_cv_dlopen_self in
572 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
573 |   *) enable_dlopen_self=unknown ;;
576 |   case $lt_cv_dlopen_self_static in
577 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
578 |   *) enable_dlopen_self_static=unknown ;;
581 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
582 | 	 [Whether dlopen is supported])
583 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
584 | 	 [Whether dlopen of programs is supported])
585 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
586 | 	 [Whether dlopen of statically linked programs is supported])
588 | m4trace:/usr/share/aclocal/libtool.m4:1961: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
589 | m4trace:/usr/share/aclocal/libtool.m4:1961: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
591 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1065 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1109 | eval "LTDLOPEN=\"$libname_spec\""
1110 | AC_SUBST([LTDLOPEN])
1112 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1113 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1114 |   [lt_cv_sys_dlopen_deplibs],
1115 |   [# PORTME does your system automatically load deplibs for dlopen?
1119 |   lt_cv_sys_dlopen_deplibs=unknown
1124 |     lt_cv_sys_dlopen_deplibs=unknown
1127 |     lt_cv_sys_dlopen_deplibs=yes
1132 |       lt_cv_sys_dlopen_deplibs=no
1139 |     lt_cv_sys_dlopen_deplibs=yes
1142 |     lt_cv_sys_dlopen_deplibs=yes
1146 |     lt_cv_sys_dlopen_deplibs=yes
1149 |     lt_cv_sys_dlopen_deplibs=yes
1152 |     lt_cv_sys_dlopen_deplibs=yes
1157 |     lt_cv_sys_dlopen_deplibs=unknown
1161 |     # at 6.2 and later dlopen does load deplibs.
1162 |     lt_cv_sys_dlopen_deplibs=yes
1165 |     lt_cv_sys_dlopen_deplibs=yes
1168 |     lt_cv_sys_dlopen_deplibs=yes
1171 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1174 |     lt_cv_sys_dlopen_deplibs=no
1177 |     # dlopen *does* load deplibs and with the right loader patch applied
1183 |     lt_cv_sys_dlopen_deplibs=unknown
1190 |     lt_cv_sys_dlopen_deplibs=yes
1193 |     lt_cv_sys_dlopen_deplibs=yes
1196 |     lt_cv_sys_dlopen_deplibs=yes
1199 |     libltdl_cv_sys_dlopen_deplibs=yes
1203 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
1204 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1205 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1208 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1209 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1211 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1277 | LIBADD_DLOPEN=
1278 | AC_SEARCH_LIBS([dlopen], [dl],
1281 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
1282 | 	  LIBADD_DLOPEN="-ldl"
1284 | 	libltdl_cv_lib_dl_dlopen="yes"
1285 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1289 |     ]], [[dlopen(0, 0);]])],
1292 | 	    libltdl_cv_func_dlopen="yes"
1293 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1294 | 	[AC_CHECK_LIB([svld], [dlopen],
1297 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
1298 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1299 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
1302 |   LIBS="$LIBS $LIBADD_DLOPEN"
1306 | AC_SUBST([LIBADD_DLOPEN])
1312 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1316 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1326 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1329 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1333 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1340 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
1356 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
1405 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
1406 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
1411 |           LIBS="$LIBS $LIBADD_DLOPEN"
1412 | 	  _LT_TRY_DLOPEN_SELF(
1430 | m4trace:/usr/share/aclocal/ltoptions.m4:111: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1433 | put the `dlopen' option into LT_INIT's first parameter.])
1435 | m4trace:/usr/share/aclocal/ltoptions.m4:111: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1437 | _LT_SET_OPTION([LT_INIT], [dlopen])
1440 | put the `dlopen' option into LT_INIT's first parameter.])
1532 | m4trace:/usr/share/aclocal/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
5115 | m4trace:configure.ac:85: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### autom4te.cache/traces.5

```

{% raw %}
1030 | m4trace:/Users/rpfische/macports/share/aclocal/libtool.m4:2043: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
1031 | if test yes != "$enable_dlopen"; then
1032 |   enable_dlopen=unknown
1033 |   enable_dlopen_self=unknown
1034 |   enable_dlopen_self_static=unknown
1036 |   lt_cv_dlopen=no
1037 |   lt_cv_dlopen_libs=
1041 |     lt_cv_dlopen=load_add_on
1042 |     lt_cv_dlopen_libs=
1043 |     lt_cv_dlopen_self=yes
1047 |     lt_cv_dlopen=LoadLibrary
1048 |     lt_cv_dlopen_libs=
1052 |     lt_cv_dlopen=dlopen
1053 |     lt_cv_dlopen_libs=
1058 |     AC_CHECK_LIB([dl], [dlopen],
1059 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1060 |     lt_cv_dlopen=dyld
1061 |     lt_cv_dlopen_libs=
1062 |     lt_cv_dlopen_self=yes
1069 |     lt_cv_dlopen=dlopen
1070 |     lt_cv_dlopen_libs=
1071 |     lt_cv_dlopen_self=no
1076 | 	  [lt_cv_dlopen=shl_load],
1078 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1079 | 	[AC_CHECK_FUNC([dlopen],
1080 | 	      [lt_cv_dlopen=dlopen],
1081 | 	  [AC_CHECK_LIB([dl], [dlopen],
1082 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1083 | 	    [AC_CHECK_LIB([svld], [dlopen],
1084 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1086 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1095 |   if test no = "$lt_cv_dlopen"; then
1096 |     enable_dlopen=no
1098 |     enable_dlopen=yes
1101 |   case $lt_cv_dlopen in
1102 |   dlopen)
1110 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1112 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1113 | 	  lt_cv_dlopen_self, [dnl
1114 | 	  _LT_TRY_DLOPEN_SELF(
1115 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1116 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1119 |     if test yes = "$lt_cv_dlopen_self"; then
1121 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1122 | 	  lt_cv_dlopen_self_static, [dnl
1123 | 	  _LT_TRY_DLOPEN_SELF(
1124 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1125 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1135 |   case $lt_cv_dlopen_self in
1136 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1137 |   *) enable_dlopen_self=unknown ;;
1140 |   case $lt_cv_dlopen_self_static in
1141 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1142 |   *) enable_dlopen_self_static=unknown ;;
1145 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1146 | 	 [Whether dlopen is supported])
1147 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1148 | 	 [Whether dlopen of programs is supported])
1149 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1150 | 	 [Whether dlopen of statically linked programs is supported])
1152 | m4trace:/Users/rpfische/macports/share/aclocal/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1153 | m4trace:/Users/rpfische/macports/share/aclocal/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
1155 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1705 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1749 | eval "LTDLOPEN=\"$libname_spec\""
1750 | AC_SUBST([LTDLOPEN])
1752 | m4trace:/Users/rpfische/macports/share/aclocal/ltdl.m4:542: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1753 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1754 |   [lt_cv_sys_dlopen_deplibs],
1755 |   [# PORTME does your system automatically load deplibs for dlopen?
1759 |   lt_cv_sys_dlopen_deplibs=unknown
1764 |     lt_cv_sys_dlopen_deplibs=unknown
1767 |     lt_cv_sys_dlopen_deplibs=yes
1772 |       lt_cv_sys_dlopen_deplibs=no
1777 |     lt_cv_sys_dlopen_deplibs=yes
1782 |     lt_cv_sys_dlopen_deplibs=yes
1785 |     lt_cv_sys_dlopen_deplibs=yes
1789 |     lt_cv_sys_dlopen_deplibs=yes
1792 |     lt_cv_sys_dlopen_deplibs=yes
1795 |     lt_cv_sys_dlopen_deplibs=yes
1800 |     lt_cv_sys_dlopen_deplibs=unknown
1804 |     # at 6.2 and later dlopen does load deplibs.
1805 |     lt_cv_sys_dlopen_deplibs=yes
1808 |     lt_cv_sys_dlopen_deplibs=yes
1811 |     lt_cv_sys_dlopen_deplibs=yes
1814 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1817 |     lt_cv_sys_dlopen_deplibs=no
1820 |     # dlopen *does* load deplibs and with the right loader patch applied
1826 |     lt_cv_sys_dlopen_deplibs=unknown
1833 |     lt_cv_sys_dlopen_deplibs=yes
1836 |     lt_cv_sys_dlopen_deplibs=yes
1839 |     lt_cv_sys_dlopen_deplibs=yes
1842 |     libltdl_cv_sys_dlopen_deplibs=yes
1846 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
1847 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1848 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1851 | m4trace:/Users/rpfische/macports/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1852 | m4trace:/Users/rpfische/macports/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1854 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1926 | LIBADD_DLOPEN=
1927 | AC_SEARCH_LIBS([dlopen], [dl],
1930 | 	if test "$ac_cv_search_dlopen" != "none required"; then
1931 | 	  LIBADD_DLOPEN=-ldl
1933 | 	libltdl_cv_lib_dl_dlopen=yes
1934 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1938 |     ]], [[dlopen(0, 0);]])],
1941 | 	    libltdl_cv_func_dlopen=yes
1942 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1943 | 	[AC_CHECK_LIB([svld], [dlopen],
1946 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
1947 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1948 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
1951 |   LIBS="$LIBS $LIBADD_DLOPEN"
1955 | AC_SUBST([LIBADD_DLOPEN])
1961 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1965 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1975 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1978 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1982 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1989 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
2005 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
2057 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
2062 |       LIBS="$LIBS $LIBADD_DLOPEN"
2120 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
2162 | m4trace:/Users/rpfische/macports/share/aclocal/ltoptions.m4:118: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2165 | put the 'dlopen' option into LT_INIT's first parameter.])
2167 | m4trace:/Users/rpfische/macports/share/aclocal/ltoptions.m4:118: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2169 | _LT_SET_OPTION([LT_INIT], [dlopen])
2172 | put the 'dlopen' option into LT_INIT's first parameter.])
2264 | m4trace:/Users/rpfische/macports/share/aclocal/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
3399 | m4trace:configure.ac:85: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### autom4te.cache/output.6

```

{% raw %}
10638 |         enable_dlopen=no
13980 |   if test "x$enable_dlopen" != xyes; then
13981 |   enable_dlopen=unknown
13982 |   enable_dlopen_self=unknown
13983 |   enable_dlopen_self_static=unknown
13985 |   lt_cv_dlopen=no
13986 |   lt_cv_dlopen_libs=
13990 |     lt_cv_dlopen="load_add_on"
13991 |     lt_cv_dlopen_libs=
13992 |     lt_cv_dlopen_self=yes
13996 |     lt_cv_dlopen="LoadLibrary"
13997 |     lt_cv_dlopen_libs=
14001 |     lt_cv_dlopen="dlopen"
14002 |     lt_cv_dlopen_libs=
14007 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14008 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14009 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14023 | char dlopen ();
14027 | return dlopen ();
14033 |   ac_cv_lib_dl_dlopen=yes
14035 |   ac_cv_lib_dl_dlopen=no
14041 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14042 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14043 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14044 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14047 |     lt_cv_dlopen="dyld"
14048 |     lt_cv_dlopen_libs=
14049 |     lt_cv_dlopen_self=yes
14058 |   lt_cv_dlopen="shl_load"
14097 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
14099 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
14100 | if test "x$ac_cv_func_dlopen" = xyes; then :
14101 |   lt_cv_dlopen="dlopen"
14103 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14104 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14105 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14119 | char dlopen ();
14123 | return dlopen ();
14129 |   ac_cv_lib_dl_dlopen=yes
14131 |   ac_cv_lib_dl_dlopen=no
14137 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14138 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14139 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14140 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14142 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14143 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14144 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14158 | char dlopen ();
14162 | return dlopen ();
14168 |   ac_cv_lib_svld_dlopen=yes
14170 |   ac_cv_lib_svld_dlopen=no
14176 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14177 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14178 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14179 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
14218 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
14239 |   if test "x$lt_cv_dlopen" != xno; then
14240 |     enable_dlopen=yes
14242 |     enable_dlopen=no
14245 |   case $lt_cv_dlopen in
14246 |   dlopen)
14254 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14256 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14257 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14258 | if ${lt_cv_dlopen_self+:} false; then :
14262 |   lt_cv_dlopen_self=cross
14317 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14344 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14345 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14346 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14350 |     lt_cv_dlopen_self=no
14357 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14358 | $as_echo "$lt_cv_dlopen_self" >&6; }
14360 |     if test "x$lt_cv_dlopen_self" = xyes; then
14362 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14363 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14364 | if ${lt_cv_dlopen_self_static+:} false; then :
14368 |   lt_cv_dlopen_self_static=cross
14423 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14450 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14451 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14452 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14456 |     lt_cv_dlopen_self_static=no
14463 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14464 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14473 |   case $lt_cv_dlopen_self in
14474 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14475 |   *) enable_dlopen_self=unknown ;;
14478 |   case $lt_cv_dlopen_self_static in
14479 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14480 |   *) enable_dlopen_self_static=unknown ;;
28242 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
28243 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
28244 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
30876 | # Whether dlopen is supported.
30877 | dlopen_support=$enable_dlopen
30879 | # Whether dlopen of programs is supported.
30880 | dlopen_self=$enable_dlopen_self
30882 | # Whether dlopen of statically linked programs is supported.
30883 | dlopen_self_static=$enable_dlopen_self_static
30927 | # Compiler flag to allow reflexive dlopens.
31269 | # Compiler flag to allow reflexive dlopens.
31422 | # Compiler flag to allow reflexive dlopens.
31575 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.4

```

{% raw %}
10638 |         enable_dlopen=no
13980 |   if test "x$enable_dlopen" != xyes; then
13981 |   enable_dlopen=unknown
13982 |   enable_dlopen_self=unknown
13983 |   enable_dlopen_self_static=unknown
13985 |   lt_cv_dlopen=no
13986 |   lt_cv_dlopen_libs=
13990 |     lt_cv_dlopen="load_add_on"
13991 |     lt_cv_dlopen_libs=
13992 |     lt_cv_dlopen_self=yes
13996 |     lt_cv_dlopen="LoadLibrary"
13997 |     lt_cv_dlopen_libs=
14001 |     lt_cv_dlopen="dlopen"
14002 |     lt_cv_dlopen_libs=
14007 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14008 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14009 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14023 | char dlopen ();
14027 | return dlopen ();
14033 |   ac_cv_lib_dl_dlopen=yes
14035 |   ac_cv_lib_dl_dlopen=no
14041 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14042 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14043 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14044 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14047 |     lt_cv_dlopen="dyld"
14048 |     lt_cv_dlopen_libs=
14049 |     lt_cv_dlopen_self=yes
14058 |   lt_cv_dlopen="shl_load"
14097 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
14099 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
14100 | if test "x$ac_cv_func_dlopen" = xyes; then :
14101 |   lt_cv_dlopen="dlopen"
14103 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
14104 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14105 | if ${ac_cv_lib_dl_dlopen+:} false; then :
14119 | char dlopen ();
14123 | return dlopen ();
14129 |   ac_cv_lib_dl_dlopen=yes
14131 |   ac_cv_lib_dl_dlopen=no
14137 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
14138 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14139 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
14140 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14142 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
14143 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14144 | if ${ac_cv_lib_svld_dlopen+:} false; then :
14158 | char dlopen ();
14162 | return dlopen ();
14168 |   ac_cv_lib_svld_dlopen=yes
14170 |   ac_cv_lib_svld_dlopen=no
14176 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
14177 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14178 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
14179 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
14218 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
14239 |   if test "x$lt_cv_dlopen" != xno; then
14240 |     enable_dlopen=yes
14242 |     enable_dlopen=no
14245 |   case $lt_cv_dlopen in
14246 |   dlopen)
14254 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14256 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
14257 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14258 | if ${lt_cv_dlopen_self+:} false; then :
14262 |   lt_cv_dlopen_self=cross
14317 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14344 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14345 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14346 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14350 |     lt_cv_dlopen_self=no
14357 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
14358 | $as_echo "$lt_cv_dlopen_self" >&6; }
14360 |     if test "x$lt_cv_dlopen_self" = xyes; then
14362 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
14363 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14364 | if ${lt_cv_dlopen_self_static+:} false; then :
14368 |   lt_cv_dlopen_self_static=cross
14423 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14450 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14451 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14452 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14456 |     lt_cv_dlopen_self_static=no
14463 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
14464 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14473 |   case $lt_cv_dlopen_self in
14474 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14475 |   *) enable_dlopen_self=unknown ;;
14478 |   case $lt_cv_dlopen_self_static in
14479 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14480 |   *) enable_dlopen_self_static=unknown ;;
28242 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
28243 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
28244 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
30876 | # Whether dlopen is supported.
30877 | dlopen_support=$enable_dlopen
30879 | # Whether dlopen of programs is supported.
30880 | dlopen_self=$enable_dlopen_self
30882 | # Whether dlopen of statically linked programs is supported.
30883 | dlopen_self_static=$enable_dlopen_self_static
30927 | # Compiler flag to allow reflexive dlopens.
31269 | # Compiler flag to allow reflexive dlopens.
31422 | # Compiler flag to allow reflexive dlopens.
31575 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.2

```

{% raw %}
244 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
288 | eval "LTDLOPEN=\"$libname_spec\""
289 | AC_SUBST([LTDLOPEN])
291 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
292 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
293 |   [lt_cv_sys_dlopen_deplibs],
294 |   [# PORTME does your system automatically load deplibs for dlopen?
298 |   lt_cv_sys_dlopen_deplibs=unknown
303 |     lt_cv_sys_dlopen_deplibs=unknown
306 |     lt_cv_sys_dlopen_deplibs=yes
311 |       lt_cv_sys_dlopen_deplibs=no
318 |     lt_cv_sys_dlopen_deplibs=yes
321 |     lt_cv_sys_dlopen_deplibs=yes
325 |     lt_cv_sys_dlopen_deplibs=yes
328 |     lt_cv_sys_dlopen_deplibs=yes
331 |     lt_cv_sys_dlopen_deplibs=yes
336 |     lt_cv_sys_dlopen_deplibs=unknown
340 |     # at 6.2 and later dlopen does load deplibs.
341 |     lt_cv_sys_dlopen_deplibs=yes
344 |     lt_cv_sys_dlopen_deplibs=yes
347 |     lt_cv_sys_dlopen_deplibs=yes
350 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
353 |     lt_cv_sys_dlopen_deplibs=no
356 |     # dlopen *does* load deplibs and with the right loader patch applied
362 |     lt_cv_sys_dlopen_deplibs=unknown
369 |     lt_cv_sys_dlopen_deplibs=yes
372 |     lt_cv_sys_dlopen_deplibs=yes
375 |     lt_cv_sys_dlopen_deplibs=yes
378 |     libltdl_cv_sys_dlopen_deplibs=yes
382 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
383 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
384 |     [Define if the OS needs help to load dependent libraries for dlopen().])
387 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
388 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
390 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
456 | LIBADD_DLOPEN=
457 | AC_SEARCH_LIBS([dlopen], [dl],
460 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
461 | 	  LIBADD_DLOPEN="-ldl"
463 | 	libltdl_cv_lib_dl_dlopen="yes"
464 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
468 |     ]], [[dlopen(0, 0);]])],
471 | 	    libltdl_cv_func_dlopen="yes"
472 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
473 | 	[AC_CHECK_LIB([svld], [dlopen],
476 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
477 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
478 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
481 |   LIBS="$LIBS $LIBADD_DLOPEN"
485 | AC_SUBST([LIBADD_DLOPEN])
491 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
495 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
505 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
508 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
512 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
519 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
535 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
584 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
585 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
590 |           LIBS="$LIBS $LIBADD_DLOPEN"
591 | 	  _LT_TRY_DLOPEN_SELF(
4195 | m4trace:m4/libtool.m4:1844: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
4196 | if test "x$enable_dlopen" != xyes; then
4197 |   enable_dlopen=unknown
4198 |   enable_dlopen_self=unknown
4199 |   enable_dlopen_self_static=unknown
4201 |   lt_cv_dlopen=no
4202 |   lt_cv_dlopen_libs=
4206 |     lt_cv_dlopen="load_add_on"
4207 |     lt_cv_dlopen_libs=
4208 |     lt_cv_dlopen_self=yes
4212 |     lt_cv_dlopen="LoadLibrary"
4213 |     lt_cv_dlopen_libs=
4217 |     lt_cv_dlopen="dlopen"
4218 |     lt_cv_dlopen_libs=
4223 |     AC_CHECK_LIB([dl], [dlopen],
4224 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
4225 |     lt_cv_dlopen="dyld"
4226 |     lt_cv_dlopen_libs=
4227 |     lt_cv_dlopen_self=yes
4233 | 	  [lt_cv_dlopen="shl_load"],
4235 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
4236 | 	[AC_CHECK_FUNC([dlopen],
4237 | 	      [lt_cv_dlopen="dlopen"],
4238 | 	  [AC_CHECK_LIB([dl], [dlopen],
4239 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
4240 | 	    [AC_CHECK_LIB([svld], [dlopen],
4241 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
4243 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
4252 |   if test "x$lt_cv_dlopen" != xno; then
4253 |     enable_dlopen=yes
4255 |     enable_dlopen=no
4258 |   case $lt_cv_dlopen in
4259 |   dlopen)
4267 |     LIBS="$lt_cv_dlopen_libs $LIBS"
4269 |     AC_CACHE_CHECK([whether a program can dlopen itself],
4270 | 	  lt_cv_dlopen_self, [dnl
4271 | 	  _LT_TRY_DLOPEN_SELF(
4272 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
4273 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
4276 |     if test "x$lt_cv_dlopen_self" = xyes; then
4278 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
4279 | 	  lt_cv_dlopen_self_static, [dnl
4280 | 	  _LT_TRY_DLOPEN_SELF(
4281 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
4282 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
4292 |   case $lt_cv_dlopen_self in
4293 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
4294 |   *) enable_dlopen_self=unknown ;;
4297 |   case $lt_cv_dlopen_self_static in
4298 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
4299 |   *) enable_dlopen_self_static=unknown ;;
4302 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
4303 | 	 [Whether dlopen is supported])
4304 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
4305 | 	 [Whether dlopen of programs is supported])
4306 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
4307 | 	 [Whether dlopen of statically linked programs is supported])
4309 | m4trace:m4/libtool.m4:1961: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
4310 | m4trace:m4/libtool.m4:1961: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
4312 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
4608 | m4trace:m4/ltoptions.m4:111: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
4611 | put the `dlopen' option into LT_INIT's first parameter.])
4613 | m4trace:m4/ltoptions.m4:111: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
4615 | _LT_SET_OPTION([LT_INIT], [dlopen])
4618 | put the `dlopen' option into LT_INIT's first parameter.])
4710 | m4trace:m4/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
5115 | m4trace:configure.ac:85: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1744 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1747 | m4_defun([_LT_TRY_DLOPEN_SELF],
1805 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1838 | ])# _LT_TRY_DLOPEN_SELF
1841 | # LT_SYS_DLOPEN_SELF
1843 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1845 | if test "x$enable_dlopen" != xyes; then
1846 |   enable_dlopen=unknown
1847 |   enable_dlopen_self=unknown
1848 |   enable_dlopen_self_static=unknown
1850 |   lt_cv_dlopen=no
1851 |   lt_cv_dlopen_libs=
1855 |     lt_cv_dlopen="load_add_on"
1856 |     lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen_self=yes
1861 |     lt_cv_dlopen="LoadLibrary"
1862 |     lt_cv_dlopen_libs=
1866 |     lt_cv_dlopen="dlopen"
1867 |     lt_cv_dlopen_libs=
1872 |     AC_CHECK_LIB([dl], [dlopen],
1873 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1874 |     lt_cv_dlopen="dyld"
1875 |     lt_cv_dlopen_libs=
1876 |     lt_cv_dlopen_self=yes
1882 | 	  [lt_cv_dlopen="shl_load"],
1884 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1885 | 	[AC_CHECK_FUNC([dlopen],
1886 | 	      [lt_cv_dlopen="dlopen"],
1887 | 	  [AC_CHECK_LIB([dl], [dlopen],
1888 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1889 | 	    [AC_CHECK_LIB([svld], [dlopen],
1890 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1892 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1901 |   if test "x$lt_cv_dlopen" != xno; then
1902 |     enable_dlopen=yes
1904 |     enable_dlopen=no
1907 |   case $lt_cv_dlopen in
1908 |   dlopen)
1916 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1918 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1919 | 	  lt_cv_dlopen_self, [dnl
1920 | 	  _LT_TRY_DLOPEN_SELF(
1921 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1922 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1925 |     if test "x$lt_cv_dlopen_self" = xyes; then
1927 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1928 | 	  lt_cv_dlopen_self_static, [dnl
1929 | 	  _LT_TRY_DLOPEN_SELF(
1930 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1931 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1941 |   case $lt_cv_dlopen_self in
1942 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1943 |   *) enable_dlopen_self=unknown ;;
1946 |   case $lt_cv_dlopen_self_static in
1947 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1948 |   *) enable_dlopen_self_static=unknown ;;
1951 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1952 | 	 [Whether dlopen is supported])
1953 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1954 | 	 [Whether dlopen of programs is supported])
1955 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1956 | 	 [Whether dlopen of statically linked programs is supported])
1957 | ])# LT_SYS_DLOPEN_SELF
1960 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1962 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5662 |     [Compiler flag to allow reflexive dlopens])
5775 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```