---
name: "biobambam2"
layout: package
next_package: glfw
previous_package: kahip
languages: ['bash']
---
## 2.0.177
6 / 238 files match

 - [ltmain.sh](#ltmainsh)
 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [autom4te.cache/output.1](#autom4tecacheoutput1)
 - [autom4te.cache/traces.0](#autom4tecachetraces0)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)

### ltmain.sh

```bash

{% raw %}
2335 |     opt_dlopen=
2408 |         --dlopen|-dlopen)
2409 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2532 |       # Only execute mode is allowed to have -dlopen flags.
2533 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2534 |         func_error "unrecognized option '-dlopen'"
3760 |   -dlopen FILE      add the directory containing FILE to the library path
3762 | This mode sets the library path environment variable according to '-dlopen'
3817 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3826 |   -module           build a library that can dlopened
3934 |     # Handle -dlopen flags immediately.
3935 |     for file in $opt_dlopen; do
3954 | 	# Skip this library if it cannot be dlopened.
3981 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6674 | 	    dlopen_self=$dlopen_self_static
6680 | 	    dlopen_self=$dlopen_self_static
6686 | 	    dlopen_self=$dlopen_self_static
6744 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6834 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7001 |       -dlopen)
7441 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7509 | 	  # This library was specified with -dlopen.
7629 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7640 | 	passes="conv scan dlopen dlpreopen link"
7666 | 	dlopen) libs=$dlfiles ;;
7697 |       if test dlopen = "$pass"; then
7917 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7918 | 	      # If there is no dlopen support or we're linking statically,
7946 | 	dlopen=
7976 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8022 | 	# This library was specified with -dlopen.
8023 | 	if test dlopen = "$pass"; then
8025 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8027 | 	     test yes != "$dlopen_support" ||
8030 | 	    # If there is no dlname, no dlopen support or we're linking
8039 | 	fi # $pass = dlopen
8095 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8097 | 	      # We recover the dlopen module name by 'saving' the la file
8121 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8250 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8251 | 	  dlopenmodule=
8254 | 	      dlopenmodule=$dlpremoduletest
8258 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8355 | 		    # if the lib is a (non-dlopened) module then we cannot
8359 | 		      if test "X$dlopenmodule" != "X$lib"; then
8511 | 	      echo "*** a static module, that should work as long as the dlopening application"
8512 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8656 |       if test dlopen != "$pass"; then
8786 | 	func_warning "'-dlopen' is ignored for archives"
8853 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9550 | 	    echo "*** a static module, that should work as long as the dlopening"
9551 | 	    echo "*** application is linked with the -dlopen flag."
9569 | 	    echo "*** or is declared to -dlopen it."
10181 | 	func_warning "'-dlopen' is ignored for objects"
10301 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10302 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10983 | # The name that we can dlopen(3).
11012 | # Files to dlopen/dlpreopen
11013 | dlopen='$dlfiles'
{% endraw %}

```
### autom4te.cache/output.0

```

{% raw %}
7147 |         enable_dlopen=no
10817 |   if test yes != "$enable_dlopen"; then
10818 |   enable_dlopen=unknown
10819 |   enable_dlopen_self=unknown
10820 |   enable_dlopen_self_static=unknown
10822 |   lt_cv_dlopen=no
10823 |   lt_cv_dlopen_libs=
10827 |     lt_cv_dlopen=load_add_on
10828 |     lt_cv_dlopen_libs=
10829 |     lt_cv_dlopen_self=yes
10833 |     lt_cv_dlopen=LoadLibrary
10834 |     lt_cv_dlopen_libs=
10838 |     lt_cv_dlopen=dlopen
10839 |     lt_cv_dlopen_libs=
10844 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10845 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10846 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10860 | char dlopen ();
10864 | return dlopen ();
10870 |   ac_cv_lib_dl_dlopen=yes
10872 |   ac_cv_lib_dl_dlopen=no
10878 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10879 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10880 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
10881 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
10884 |     lt_cv_dlopen=dyld
10885 |     lt_cv_dlopen_libs=
10886 |     lt_cv_dlopen_self=yes
10895 |     lt_cv_dlopen=dlopen
10896 |     lt_cv_dlopen_libs=
10897 |     lt_cv_dlopen_self=no
10903 |   lt_cv_dlopen=shl_load
10942 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
10944 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
10945 | if test "x$ac_cv_func_dlopen" = xyes; then :
10946 |   lt_cv_dlopen=dlopen
10948 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10949 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10950 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10964 | char dlopen ();
10968 | return dlopen ();
10974 |   ac_cv_lib_dl_dlopen=yes
10976 |   ac_cv_lib_dl_dlopen=no
10982 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10983 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10984 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
10985 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
10987 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
10988 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
10989 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11003 | char dlopen ();
11007 | return dlopen ();
11013 |   ac_cv_lib_svld_dlopen=yes
11015 |   ac_cv_lib_svld_dlopen=no
11021 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11022 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11023 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11024 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
11063 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
11084 |   if test no = "$lt_cv_dlopen"; then
11085 |     enable_dlopen=no
11087 |     enable_dlopen=yes
11090 |   case $lt_cv_dlopen in
11091 |   dlopen)
11099 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11101 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11102 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11103 | if ${lt_cv_dlopen_self+:} false; then :
11107 |   lt_cv_dlopen_self=cross
11162 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11189 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
11190 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
11191 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
11195 |     lt_cv_dlopen_self=no
11202 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
11203 | $as_echo "$lt_cv_dlopen_self" >&6; }
11205 |     if test yes = "$lt_cv_dlopen_self"; then
11207 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
11208 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
11209 | if ${lt_cv_dlopen_self_static+:} false; then :
11213 |   lt_cv_dlopen_self_static=cross
11268 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11295 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
11296 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
11297 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
11301 |     lt_cv_dlopen_self_static=no
11308 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
11309 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
11318 |   case $lt_cv_dlopen_self in
11319 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
11320 |   *) enable_dlopen_self=unknown ;;
11323 |   case $lt_cv_dlopen_self_static in
11324 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
11325 |   *) enable_dlopen_self_static=unknown ;;
18729 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
18730 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
18731 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
19887 | # Whether dlopen is supported.
19888 | dlopen_support=$enable_dlopen
19890 | # Whether dlopen of programs is supported.
19891 | dlopen_self=$enable_dlopen_self
19893 | # Whether dlopen of statically linked programs is supported.
19894 | dlopen_self_static=$enable_dlopen_self_static
19938 | # Compiler flag to allow reflexive dlopens.
20180 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.1

```

{% raw %}
7147 |         enable_dlopen=no
10817 |   if test yes != "$enable_dlopen"; then
10818 |   enable_dlopen=unknown
10819 |   enable_dlopen_self=unknown
10820 |   enable_dlopen_self_static=unknown
10822 |   lt_cv_dlopen=no
10823 |   lt_cv_dlopen_libs=
10827 |     lt_cv_dlopen=load_add_on
10828 |     lt_cv_dlopen_libs=
10829 |     lt_cv_dlopen_self=yes
10833 |     lt_cv_dlopen=LoadLibrary
10834 |     lt_cv_dlopen_libs=
10838 |     lt_cv_dlopen=dlopen
10839 |     lt_cv_dlopen_libs=
10844 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10845 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10846 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10860 | char dlopen ();
10864 | return dlopen ();
10870 |   ac_cv_lib_dl_dlopen=yes
10872 |   ac_cv_lib_dl_dlopen=no
10878 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10879 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10880 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
10881 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
10884 |     lt_cv_dlopen=dyld
10885 |     lt_cv_dlopen_libs=
10886 |     lt_cv_dlopen_self=yes
10895 |     lt_cv_dlopen=dlopen
10896 |     lt_cv_dlopen_libs=
10897 |     lt_cv_dlopen_self=no
10903 |   lt_cv_dlopen=shl_load
10942 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
10944 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
10945 | if test "x$ac_cv_func_dlopen" = xyes; then :
10946 |   lt_cv_dlopen=dlopen
10948 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10949 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10950 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10964 | char dlopen ();
10968 | return dlopen ();
10974 |   ac_cv_lib_dl_dlopen=yes
10976 |   ac_cv_lib_dl_dlopen=no
10982 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10983 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10984 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
10985 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
10987 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
10988 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
10989 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11003 | char dlopen ();
11007 | return dlopen ();
11013 |   ac_cv_lib_svld_dlopen=yes
11015 |   ac_cv_lib_svld_dlopen=no
11021 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11022 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11023 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11024 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
11063 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
11084 |   if test no = "$lt_cv_dlopen"; then
11085 |     enable_dlopen=no
11087 |     enable_dlopen=yes
11090 |   case $lt_cv_dlopen in
11091 |   dlopen)
11099 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11101 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11102 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11103 | if ${lt_cv_dlopen_self+:} false; then :
11107 |   lt_cv_dlopen_self=cross
11162 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11189 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
11190 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
11191 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
11195 |     lt_cv_dlopen_self=no
11202 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
11203 | $as_echo "$lt_cv_dlopen_self" >&6; }
11205 |     if test yes = "$lt_cv_dlopen_self"; then
11207 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
11208 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
11209 | if ${lt_cv_dlopen_self_static+:} false; then :
11213 |   lt_cv_dlopen_self_static=cross
11268 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11295 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
11296 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
11297 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
11301 |     lt_cv_dlopen_self_static=no
11308 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
11309 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
11318 |   case $lt_cv_dlopen_self in
11319 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
11320 |   *) enable_dlopen_self=unknown ;;
11323 |   case $lt_cv_dlopen_self_static in
11324 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
11325 |   *) enable_dlopen_self_static=unknown ;;
18729 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
18730 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
18731 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
19887 | # Whether dlopen is supported.
19888 | dlopen_support=$enable_dlopen
19890 | # Whether dlopen of programs is supported.
19891 | dlopen_self=$enable_dlopen_self
19893 | # Whether dlopen of statically linked programs is supported.
19894 | dlopen_self_static=$enable_dlopen_self_static
19938 | # Compiler flag to allow reflexive dlopens.
20180 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.0

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
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
388 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
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
1984 | m4trace:m4/libtool.m4:1920: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
1985 | if test yes != "$enable_dlopen"; then
1986 |   enable_dlopen=unknown
1987 |   enable_dlopen_self=unknown
1988 |   enable_dlopen_self_static=unknown
1990 |   lt_cv_dlopen=no
1991 |   lt_cv_dlopen_libs=
1995 |     lt_cv_dlopen=load_add_on
1996 |     lt_cv_dlopen_libs=
1997 |     lt_cv_dlopen_self=yes
2001 |     lt_cv_dlopen=LoadLibrary
2002 |     lt_cv_dlopen_libs=
2006 |     lt_cv_dlopen=dlopen
2007 |     lt_cv_dlopen_libs=
2012 |     AC_CHECK_LIB([dl], [dlopen],
2013 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
2014 |     lt_cv_dlopen=dyld
2015 |     lt_cv_dlopen_libs=
2016 |     lt_cv_dlopen_self=yes
2023 |     lt_cv_dlopen=dlopen
2024 |     lt_cv_dlopen_libs=
2025 |     lt_cv_dlopen_self=no
2030 | 	  [lt_cv_dlopen=shl_load],
2032 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
2033 | 	[AC_CHECK_FUNC([dlopen],
2034 | 	      [lt_cv_dlopen=dlopen],
2035 | 	  [AC_CHECK_LIB([dl], [dlopen],
2036 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
2037 | 	    [AC_CHECK_LIB([svld], [dlopen],
2038 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
2040 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2049 |   if test no = "$lt_cv_dlopen"; then
2050 |     enable_dlopen=no
2052 |     enable_dlopen=yes
2055 |   case $lt_cv_dlopen in
2056 |   dlopen)
2064 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2066 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2067 | 	  lt_cv_dlopen_self, [dnl
2068 | 	  _LT_TRY_DLOPEN_SELF(
2069 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2070 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2073 |     if test yes = "$lt_cv_dlopen_self"; then
2075 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2076 | 	  lt_cv_dlopen_self_static, [dnl
2077 | 	  _LT_TRY_DLOPEN_SELF(
2078 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2079 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2089 |   case $lt_cv_dlopen_self in
2090 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2091 |   *) enable_dlopen_self=unknown ;;
2094 |   case $lt_cv_dlopen_self_static in
2095 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2096 |   *) enable_dlopen_self_static=unknown ;;
2099 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2100 | 	 [Whether dlopen is supported])
2101 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2102 | 	 [Whether dlopen of programs is supported])
2103 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2104 | 	 [Whether dlopen of statically linked programs is supported])
2106 | m4trace:m4/libtool.m4:2045: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2107 | m4trace:m4/libtool.m4:2045: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2109 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2418 | m4trace:m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2421 | put the 'dlopen' option into LT_INIT's first parameter.])
2423 | m4trace:m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2425 | _LT_SET_OPTION([LT_INIT], [dlopen])
2428 | put the 'dlopen' option into LT_INIT's first parameter.])
2520 | m4trace:m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2709 | m4trace:configure.ac:3: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1820 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1823 | m4_defun([_LT_TRY_DLOPEN_SELF],
1881 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1914 | ])# _LT_TRY_DLOPEN_SELF
1917 | # LT_SYS_DLOPEN_SELF
1919 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1921 | if test yes != "$enable_dlopen"; then
1922 |   enable_dlopen=unknown
1923 |   enable_dlopen_self=unknown
1924 |   enable_dlopen_self_static=unknown
1926 |   lt_cv_dlopen=no
1927 |   lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen=load_add_on
1932 |     lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen_self=yes
1937 |     lt_cv_dlopen=LoadLibrary
1938 |     lt_cv_dlopen_libs=
1942 |     lt_cv_dlopen=dlopen
1943 |     lt_cv_dlopen_libs=
1948 |     AC_CHECK_LIB([dl], [dlopen],
1949 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1950 |     lt_cv_dlopen=dyld
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1959 |     lt_cv_dlopen=dlopen
1960 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen_self=no
1966 | 	  [lt_cv_dlopen=shl_load],
1968 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1969 | 	[AC_CHECK_FUNC([dlopen],
1970 | 	      [lt_cv_dlopen=dlopen],
1971 | 	  [AC_CHECK_LIB([dl], [dlopen],
1972 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1973 | 	    [AC_CHECK_LIB([svld], [dlopen],
1974 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1976 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1985 |   if test no = "$lt_cv_dlopen"; then
1986 |     enable_dlopen=no
1988 |     enable_dlopen=yes
1991 |   case $lt_cv_dlopen in
1992 |   dlopen)
2000 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2002 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2003 | 	  lt_cv_dlopen_self, [dnl
2004 | 	  _LT_TRY_DLOPEN_SELF(
2005 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2006 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2009 |     if test yes = "$lt_cv_dlopen_self"; then
2011 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2012 | 	  lt_cv_dlopen_self_static, [dnl
2013 | 	  _LT_TRY_DLOPEN_SELF(
2014 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2015 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2025 |   case $lt_cv_dlopen_self in
2026 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2027 |   *) enable_dlopen_self=unknown ;;
2030 |   case $lt_cv_dlopen_self_static in
2031 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2032 |   *) enable_dlopen_self_static=unknown ;;
2035 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2036 | 	 [Whether dlopen is supported])
2037 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2038 | 	 [Whether dlopen of programs is supported])
2039 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2040 | 	 [Whether dlopen of statically linked programs is supported])
2041 | ])# LT_SYS_DLOPEN_SELF
2044 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2046 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6147 |     [Compiler flag to allow reflexive dlopens])
6260 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
107 | # dlopen
109 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
112 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
113 | [_LT_SET_OPTION([LT_INIT], [dlopen])
116 | put the 'dlopen' option into LT_INIT's first parameter.])
120 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```