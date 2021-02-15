---
name: "grib-api"
layout: package
next_package: global
previous_package: imagemagick
languages: ['cmake', 'bash']
---
## 1.24.0
9 / 6252 files match

 - [config.status](#configstatus)
 - [config/ltmain.sh](#configltmainsh)
 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [autom4te.cache/output.1](#autom4tecacheoutput1)
 - [autom4te.cache/output.2](#autom4tecacheoutput2)
 - [autom4te.cache/traces.0](#autom4tecachetraces0)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [cmake/ecbuild_add_library.cmake](#cmakeecbuild_add_librarycmake)

### config.status

```

{% raw %}
678 | enable_dlopen='unknown'
679 | enable_dlopen_self='unknown'
680 | enable_dlopen_self_static='unknown'
1869 | # Whether dlopen is supported.
1870 | dlopen_support=$enable_dlopen
1872 | # Whether dlopen of programs is supported.
1873 | dlopen_self=$enable_dlopen_self
1875 | # Whether dlopen of statically linked programs is supported.
1876 | dlopen_self_static=$enable_dlopen_self_static
1920 | # Compiler flag to allow reflexive dlopens.
2262 | # Compiler flag to allow reflexive dlopens.
2415 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
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
### autom4te.cache/output.0

```

{% raw %}
7096 |         enable_dlopen=no
10434 |   if test "x$enable_dlopen" != xyes; then
10435 |   enable_dlopen=unknown
10436 |   enable_dlopen_self=unknown
10437 |   enable_dlopen_self_static=unknown
10439 |   lt_cv_dlopen=no
10440 |   lt_cv_dlopen_libs=
10444 |     lt_cv_dlopen="load_add_on"
10445 |     lt_cv_dlopen_libs=
10446 |     lt_cv_dlopen_self=yes
10450 |     lt_cv_dlopen="LoadLibrary"
10451 |     lt_cv_dlopen_libs=
10455 |     lt_cv_dlopen="dlopen"
10456 |     lt_cv_dlopen_libs=
10461 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10462 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10463 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10477 | char dlopen ();
10481 | return dlopen ();
10487 |   ac_cv_lib_dl_dlopen=yes
10489 |   ac_cv_lib_dl_dlopen=no
10495 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10496 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10497 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
10498 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10501 |     lt_cv_dlopen="dyld"
10502 |     lt_cv_dlopen_libs=
10503 |     lt_cv_dlopen_self=yes
10512 |   lt_cv_dlopen="shl_load"
10551 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
10553 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
10554 | if test "x$ac_cv_func_dlopen" = xyes; then :
10555 |   lt_cv_dlopen="dlopen"
10557 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10558 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10559 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10573 | char dlopen ();
10577 | return dlopen ();
10583 |   ac_cv_lib_dl_dlopen=yes
10585 |   ac_cv_lib_dl_dlopen=no
10591 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10592 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10593 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
10594 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10596 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
10597 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
10598 | if ${ac_cv_lib_svld_dlopen+:} false; then :
10612 | char dlopen ();
10616 | return dlopen ();
10622 |   ac_cv_lib_svld_dlopen=yes
10624 |   ac_cv_lib_svld_dlopen=no
10630 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
10631 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
10632 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
10633 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
10672 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
10693 |   if test "x$lt_cv_dlopen" != xno; then
10694 |     enable_dlopen=yes
10696 |     enable_dlopen=no
10699 |   case $lt_cv_dlopen in
10700 |   dlopen)
10708 |     LIBS="$lt_cv_dlopen_libs $LIBS"
10710 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
10711 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
10712 | if ${lt_cv_dlopen_self+:} false; then :
10716 |   lt_cv_dlopen_self=cross
10771 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10798 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
10799 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
10800 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
10804 |     lt_cv_dlopen_self=no
10811 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
10812 | $as_echo "$lt_cv_dlopen_self" >&6; }
10814 |     if test "x$lt_cv_dlopen_self" = xyes; then
10816 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
10817 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
10818 | if ${lt_cv_dlopen_self_static+:} false; then :
10822 |   lt_cv_dlopen_self_static=cross
10877 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10904 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
10905 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
10906 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
10910 |     lt_cv_dlopen_self_static=no
10917 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
10918 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
10927 |   case $lt_cv_dlopen_self in
10928 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
10929 |   *) enable_dlopen_self=unknown ;;
10932 |   case $lt_cv_dlopen_self_static in
10933 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
10934 |   *) enable_dlopen_self_static=unknown ;;
22468 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
22469 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
22470 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
23717 | # Whether dlopen is supported.
23718 | dlopen_support=$enable_dlopen
23720 | # Whether dlopen of programs is supported.
23721 | dlopen_self=$enable_dlopen_self
23723 | # Whether dlopen of statically linked programs is supported.
23724 | dlopen_self_static=$enable_dlopen_self_static
23768 | # Compiler flag to allow reflexive dlopens.
24110 | # Compiler flag to allow reflexive dlopens.
24263 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.1

```

{% raw %}
7096 |         enable_dlopen=no
10434 |   if test "x$enable_dlopen" != xyes; then
10435 |   enable_dlopen=unknown
10436 |   enable_dlopen_self=unknown
10437 |   enable_dlopen_self_static=unknown
10439 |   lt_cv_dlopen=no
10440 |   lt_cv_dlopen_libs=
10444 |     lt_cv_dlopen="load_add_on"
10445 |     lt_cv_dlopen_libs=
10446 |     lt_cv_dlopen_self=yes
10450 |     lt_cv_dlopen="LoadLibrary"
10451 |     lt_cv_dlopen_libs=
10455 |     lt_cv_dlopen="dlopen"
10456 |     lt_cv_dlopen_libs=
10461 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10462 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10463 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10477 | char dlopen ();
10481 | return dlopen ();
10487 |   ac_cv_lib_dl_dlopen=yes
10489 |   ac_cv_lib_dl_dlopen=no
10495 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10496 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10497 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
10498 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10501 |     lt_cv_dlopen="dyld"
10502 |     lt_cv_dlopen_libs=
10503 |     lt_cv_dlopen_self=yes
10512 |   lt_cv_dlopen="shl_load"
10551 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
10553 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
10554 | if test "x$ac_cv_func_dlopen" = xyes; then :
10555 |   lt_cv_dlopen="dlopen"
10557 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10558 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10559 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10573 | char dlopen ();
10577 | return dlopen ();
10583 |   ac_cv_lib_dl_dlopen=yes
10585 |   ac_cv_lib_dl_dlopen=no
10591 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10592 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10593 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
10594 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10596 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
10597 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
10598 | if ${ac_cv_lib_svld_dlopen+:} false; then :
10612 | char dlopen ();
10616 | return dlopen ();
10622 |   ac_cv_lib_svld_dlopen=yes
10624 |   ac_cv_lib_svld_dlopen=no
10630 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
10631 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
10632 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
10633 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
10672 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
10693 |   if test "x$lt_cv_dlopen" != xno; then
10694 |     enable_dlopen=yes
10696 |     enable_dlopen=no
10699 |   case $lt_cv_dlopen in
10700 |   dlopen)
10708 |     LIBS="$lt_cv_dlopen_libs $LIBS"
10710 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
10711 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
10712 | if ${lt_cv_dlopen_self+:} false; then :
10716 |   lt_cv_dlopen_self=cross
10771 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10798 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
10799 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
10800 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
10804 |     lt_cv_dlopen_self=no
10811 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
10812 | $as_echo "$lt_cv_dlopen_self" >&6; }
10814 |     if test "x$lt_cv_dlopen_self" = xyes; then
10816 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
10817 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
10818 | if ${lt_cv_dlopen_self_static+:} false; then :
10822 |   lt_cv_dlopen_self_static=cross
10877 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10904 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
10905 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
10906 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
10910 |     lt_cv_dlopen_self_static=no
10917 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
10918 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
10927 |   case $lt_cv_dlopen_self in
10928 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
10929 |   *) enable_dlopen_self=unknown ;;
10932 |   case $lt_cv_dlopen_self_static in
10933 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
10934 |   *) enable_dlopen_self_static=unknown ;;
22468 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
22469 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
22470 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
23717 | # Whether dlopen is supported.
23718 | dlopen_support=$enable_dlopen
23720 | # Whether dlopen of programs is supported.
23721 | dlopen_self=$enable_dlopen_self
23723 | # Whether dlopen of statically linked programs is supported.
23724 | dlopen_self_static=$enable_dlopen_self_static
23768 | # Compiler flag to allow reflexive dlopens.
24110 | # Compiler flag to allow reflexive dlopens.
24263 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.2

```

{% raw %}
7096 |         enable_dlopen=no
10434 |   if test "x$enable_dlopen" != xyes; then
10435 |   enable_dlopen=unknown
10436 |   enable_dlopen_self=unknown
10437 |   enable_dlopen_self_static=unknown
10439 |   lt_cv_dlopen=no
10440 |   lt_cv_dlopen_libs=
10444 |     lt_cv_dlopen="load_add_on"
10445 |     lt_cv_dlopen_libs=
10446 |     lt_cv_dlopen_self=yes
10450 |     lt_cv_dlopen="LoadLibrary"
10451 |     lt_cv_dlopen_libs=
10455 |     lt_cv_dlopen="dlopen"
10456 |     lt_cv_dlopen_libs=
10461 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10462 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10463 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10477 | char dlopen ();
10481 | return dlopen ();
10487 |   ac_cv_lib_dl_dlopen=yes
10489 |   ac_cv_lib_dl_dlopen=no
10495 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10496 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10497 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
10498 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10501 |     lt_cv_dlopen="dyld"
10502 |     lt_cv_dlopen_libs=
10503 |     lt_cv_dlopen_self=yes
10512 |   lt_cv_dlopen="shl_load"
10551 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
10553 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
10554 | if test "x$ac_cv_func_dlopen" = xyes; then :
10555 |   lt_cv_dlopen="dlopen"
10557 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10558 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10559 | if ${ac_cv_lib_dl_dlopen+:} false; then :
10573 | char dlopen ();
10577 | return dlopen ();
10583 |   ac_cv_lib_dl_dlopen=yes
10585 |   ac_cv_lib_dl_dlopen=no
10591 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10592 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10593 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
10594 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10596 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
10597 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
10598 | if ${ac_cv_lib_svld_dlopen+:} false; then :
10612 | char dlopen ();
10616 | return dlopen ();
10622 |   ac_cv_lib_svld_dlopen=yes
10624 |   ac_cv_lib_svld_dlopen=no
10630 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
10631 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
10632 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
10633 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
10672 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
10693 |   if test "x$lt_cv_dlopen" != xno; then
10694 |     enable_dlopen=yes
10696 |     enable_dlopen=no
10699 |   case $lt_cv_dlopen in
10700 |   dlopen)
10708 |     LIBS="$lt_cv_dlopen_libs $LIBS"
10710 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
10711 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
10712 | if ${lt_cv_dlopen_self+:} false; then :
10716 |   lt_cv_dlopen_self=cross
10771 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10798 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
10799 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
10800 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
10804 |     lt_cv_dlopen_self=no
10811 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
10812 | $as_echo "$lt_cv_dlopen_self" >&6; }
10814 |     if test "x$lt_cv_dlopen_self" = xyes; then
10816 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
10817 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
10818 | if ${lt_cv_dlopen_self_static+:} false; then :
10822 |   lt_cv_dlopen_self_static=cross
10877 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10904 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
10905 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
10906 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
10910 |     lt_cv_dlopen_self_static=no
10917 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
10918 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
10927 |   case $lt_cv_dlopen_self in
10928 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
10929 |   *) enable_dlopen_self=unknown ;;
10932 |   case $lt_cv_dlopen_self_static in
10933 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
10934 |   *) enable_dlopen_self_static=unknown ;;
22468 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
22469 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
22470 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
23717 | # Whether dlopen is supported.
23718 | dlopen_support=$enable_dlopen
23720 | # Whether dlopen of programs is supported.
23721 | dlopen_self=$enable_dlopen_self
23723 | # Whether dlopen of statically linked programs is supported.
23724 | dlopen_self_static=$enable_dlopen_self_static
23768 | # Compiler flag to allow reflexive dlopens.
24110 | # Compiler flag to allow reflexive dlopens.
24263 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.0

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
1939 | m4trace:m4/libtool.m4:1850: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
1940 | if test "x$enable_dlopen" != xyes; then
1941 |   enable_dlopen=unknown
1942 |   enable_dlopen_self=unknown
1943 |   enable_dlopen_self_static=unknown
1945 |   lt_cv_dlopen=no
1946 |   lt_cv_dlopen_libs=
1950 |     lt_cv_dlopen="load_add_on"
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1956 |     lt_cv_dlopen="LoadLibrary"
1957 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen="dlopen"
1962 |     lt_cv_dlopen_libs=
1967 |     AC_CHECK_LIB([dl], [dlopen],
1968 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1969 |     lt_cv_dlopen="dyld"
1970 |     lt_cv_dlopen_libs=
1971 |     lt_cv_dlopen_self=yes
1977 | 	  [lt_cv_dlopen="shl_load"],
1979 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1980 | 	[AC_CHECK_FUNC([dlopen],
1981 | 	      [lt_cv_dlopen="dlopen"],
1982 | 	  [AC_CHECK_LIB([dl], [dlopen],
1983 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1984 | 	    [AC_CHECK_LIB([svld], [dlopen],
1985 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1987 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1996 |   if test "x$lt_cv_dlopen" != xno; then
1997 |     enable_dlopen=yes
1999 |     enable_dlopen=no
2002 |   case $lt_cv_dlopen in
2003 |   dlopen)
2011 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2013 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2014 | 	  lt_cv_dlopen_self, [dnl
2015 | 	  _LT_TRY_DLOPEN_SELF(
2016 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2017 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2020 |     if test "x$lt_cv_dlopen_self" = xyes; then
2022 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2023 | 	  lt_cv_dlopen_self_static, [dnl
2024 | 	  _LT_TRY_DLOPEN_SELF(
2025 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2026 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2036 |   case $lt_cv_dlopen_self in
2037 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2038 |   *) enable_dlopen_self=unknown ;;
2041 |   case $lt_cv_dlopen_self_static in
2042 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2043 |   *) enable_dlopen_self_static=unknown ;;
2046 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2047 | 	 [Whether dlopen is supported])
2048 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2049 | 	 [Whether dlopen of programs is supported])
2050 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2051 | 	 [Whether dlopen of statically linked programs is supported])
2053 | m4trace:m4/libtool.m4:1967: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2054 | m4trace:m4/libtool.m4:1967: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2056 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2352 | m4trace:m4/ltoptions.m4:111: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2355 | put the `dlopen' option into LT_INIT's first parameter.])
2357 | m4trace:m4/ltoptions.m4:111: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2359 | _LT_SET_OPTION([LT_INIT], [dlopen])
2362 | put the `dlopen' option into LT_INIT's first parameter.])
2454 | m4trace:m4/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
3027 | m4trace:configure.ac:10: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1750 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1753 | m4_defun([_LT_TRY_DLOPEN_SELF],
1811 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1844 | ])# _LT_TRY_DLOPEN_SELF
1847 | # LT_SYS_DLOPEN_SELF
1849 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1851 | if test "x$enable_dlopen" != xyes; then
1852 |   enable_dlopen=unknown
1853 |   enable_dlopen_self=unknown
1854 |   enable_dlopen_self_static=unknown
1856 |   lt_cv_dlopen=no
1857 |   lt_cv_dlopen_libs=
1861 |     lt_cv_dlopen="load_add_on"
1862 |     lt_cv_dlopen_libs=
1863 |     lt_cv_dlopen_self=yes
1867 |     lt_cv_dlopen="LoadLibrary"
1868 |     lt_cv_dlopen_libs=
1872 |     lt_cv_dlopen="dlopen"
1873 |     lt_cv_dlopen_libs=
1878 |     AC_CHECK_LIB([dl], [dlopen],
1879 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1880 |     lt_cv_dlopen="dyld"
1881 |     lt_cv_dlopen_libs=
1882 |     lt_cv_dlopen_self=yes
1888 | 	  [lt_cv_dlopen="shl_load"],
1890 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1891 | 	[AC_CHECK_FUNC([dlopen],
1892 | 	      [lt_cv_dlopen="dlopen"],
1893 | 	  [AC_CHECK_LIB([dl], [dlopen],
1894 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1895 | 	    [AC_CHECK_LIB([svld], [dlopen],
1896 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1898 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1907 |   if test "x$lt_cv_dlopen" != xno; then
1908 |     enable_dlopen=yes
1910 |     enable_dlopen=no
1913 |   case $lt_cv_dlopen in
1914 |   dlopen)
1922 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1924 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1925 | 	  lt_cv_dlopen_self, [dnl
1926 | 	  _LT_TRY_DLOPEN_SELF(
1927 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1928 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1931 |     if test "x$lt_cv_dlopen_self" = xyes; then
1933 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1934 | 	  lt_cv_dlopen_self_static, [dnl
1935 | 	  _LT_TRY_DLOPEN_SELF(
1936 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1937 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1947 |   case $lt_cv_dlopen_self in
1948 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1949 |   *) enable_dlopen_self=unknown ;;
1952 |   case $lt_cv_dlopen_self_static in
1953 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1954 |   *) enable_dlopen_self_static=unknown ;;
1957 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1958 | 	 [Whether dlopen is supported])
1959 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1960 | 	 [Whether dlopen of programs is supported])
1961 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1962 | 	 [Whether dlopen of statically linked programs is supported])
1963 | ])# LT_SYS_DLOPEN_SELF
1966 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1968 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5664 |     [Compiler flag to allow reflexive dlopens])
5777 |   LT_SYS_DLOPEN_SELF
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
### cmake/ecbuild_add_library.cmake

```cmake

{% raw %}
61 | #            dynamically at runtime using dlopen-like functionality
{% endraw %}

```