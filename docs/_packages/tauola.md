---
name: "tauola"
layout: package
next_package: openexr
previous_package: openslp
languages: ['bash']
---
## 1.1.8
8 / 926 files match

 - [config/ltmain.sh](#configltmainsh)
 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [autom4te.cache/output.1](#autom4tecacheoutput1)
 - [autom4te.cache/output.2](#autom4tecacheoutput2)
 - [autom4te.cache/traces.0](#autom4tecachetraces0)
 - [autom4te.cache/traces.1](#autom4tecachetraces1)
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
### autom4te.cache/output.0

```

{% raw %}
9335 |         enable_dlopen=no
12707 |   if test "x$enable_dlopen" != xyes; then
12708 |   enable_dlopen=unknown
12709 |   enable_dlopen_self=unknown
12710 |   enable_dlopen_self_static=unknown
12712 |   lt_cv_dlopen=no
12713 |   lt_cv_dlopen_libs=
12717 |     lt_cv_dlopen="load_add_on"
12718 |     lt_cv_dlopen_libs=
12719 |     lt_cv_dlopen_self=yes
12723 |     lt_cv_dlopen="LoadLibrary"
12724 |     lt_cv_dlopen_libs=
12728 |     lt_cv_dlopen="dlopen"
12729 |     lt_cv_dlopen_libs=
12734 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12735 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12736 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12750 | char dlopen ();
12754 | return dlopen ();
12760 |   ac_cv_lib_dl_dlopen=yes
12762 |   ac_cv_lib_dl_dlopen=no
12768 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12769 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12770 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12771 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12774 |     lt_cv_dlopen="dyld"
12775 |     lt_cv_dlopen_libs=
12776 |     lt_cv_dlopen_self=yes
12785 |   lt_cv_dlopen="shl_load"
12824 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
12826 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
12827 | if test "x$ac_cv_func_dlopen" = xyes; then :
12828 |   lt_cv_dlopen="dlopen"
12830 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12831 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12832 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12846 | char dlopen ();
12850 | return dlopen ();
12856 |   ac_cv_lib_dl_dlopen=yes
12858 |   ac_cv_lib_dl_dlopen=no
12864 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12865 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12866 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12867 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12869 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
12870 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
12871 | if ${ac_cv_lib_svld_dlopen+:} false; then :
12885 | char dlopen ();
12889 | return dlopen ();
12895 |   ac_cv_lib_svld_dlopen=yes
12897 |   ac_cv_lib_svld_dlopen=no
12903 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
12904 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
12905 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
12906 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12945 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
12966 |   if test "x$lt_cv_dlopen" != xno; then
12967 |     enable_dlopen=yes
12969 |     enable_dlopen=no
12972 |   case $lt_cv_dlopen in
12973 |   dlopen)
12981 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12983 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
12984 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12985 | if ${lt_cv_dlopen_self+:} false; then :
12989 |   lt_cv_dlopen_self=cross
13044 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13071 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
13072 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
13073 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
13077 |     lt_cv_dlopen_self=no
13084 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
13085 | $as_echo "$lt_cv_dlopen_self" >&6; }
13087 |     if test "x$lt_cv_dlopen_self" = xyes; then
13089 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
13090 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
13091 | if ${lt_cv_dlopen_self_static+:} false; then :
13095 |   lt_cv_dlopen_self_static=cross
13150 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13177 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
13178 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
13179 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
13183 |     lt_cv_dlopen_self_static=no
13190 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
13191 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
13200 |   case $lt_cv_dlopen_self in
13201 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
13202 |   *) enable_dlopen_self=unknown ;;
13205 |   case $lt_cv_dlopen_self_static in
13206 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
13207 |   *) enable_dlopen_self_static=unknown ;;
20349 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
20350 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
20351 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
21677 | # Whether dlopen is supported.
21678 | dlopen_support=$enable_dlopen
21680 | # Whether dlopen of programs is supported.
21681 | dlopen_self=$enable_dlopen_self
21683 | # Whether dlopen of statically linked programs is supported.
21684 | dlopen_self_static=$enable_dlopen_self_static
21728 | # Compiler flag to allow reflexive dlopens.
22070 | # Compiler flag to allow reflexive dlopens.
22223 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.1

```

{% raw %}
9335 |         enable_dlopen=no
12707 |   if test "x$enable_dlopen" != xyes; then
12708 |   enable_dlopen=unknown
12709 |   enable_dlopen_self=unknown
12710 |   enable_dlopen_self_static=unknown
12712 |   lt_cv_dlopen=no
12713 |   lt_cv_dlopen_libs=
12717 |     lt_cv_dlopen="load_add_on"
12718 |     lt_cv_dlopen_libs=
12719 |     lt_cv_dlopen_self=yes
12723 |     lt_cv_dlopen="LoadLibrary"
12724 |     lt_cv_dlopen_libs=
12728 |     lt_cv_dlopen="dlopen"
12729 |     lt_cv_dlopen_libs=
12734 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12735 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12736 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12750 | char dlopen ();
12754 | return dlopen ();
12760 |   ac_cv_lib_dl_dlopen=yes
12762 |   ac_cv_lib_dl_dlopen=no
12768 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12769 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12770 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12771 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12774 |     lt_cv_dlopen="dyld"
12775 |     lt_cv_dlopen_libs=
12776 |     lt_cv_dlopen_self=yes
12785 |   lt_cv_dlopen="shl_load"
12824 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
12826 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
12827 | if test "x$ac_cv_func_dlopen" = xyes; then :
12828 |   lt_cv_dlopen="dlopen"
12830 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12831 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12832 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12846 | char dlopen ();
12850 | return dlopen ();
12856 |   ac_cv_lib_dl_dlopen=yes
12858 |   ac_cv_lib_dl_dlopen=no
12864 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12865 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12866 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12867 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12869 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
12870 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
12871 | if ${ac_cv_lib_svld_dlopen+:} false; then :
12885 | char dlopen ();
12889 | return dlopen ();
12895 |   ac_cv_lib_svld_dlopen=yes
12897 |   ac_cv_lib_svld_dlopen=no
12903 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
12904 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
12905 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
12906 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12945 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
12966 |   if test "x$lt_cv_dlopen" != xno; then
12967 |     enable_dlopen=yes
12969 |     enable_dlopen=no
12972 |   case $lt_cv_dlopen in
12973 |   dlopen)
12981 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12983 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
12984 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12985 | if ${lt_cv_dlopen_self+:} false; then :
12989 |   lt_cv_dlopen_self=cross
13044 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13071 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
13072 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
13073 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
13077 |     lt_cv_dlopen_self=no
13084 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
13085 | $as_echo "$lt_cv_dlopen_self" >&6; }
13087 |     if test "x$lt_cv_dlopen_self" = xyes; then
13089 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
13090 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
13091 | if ${lt_cv_dlopen_self_static+:} false; then :
13095 |   lt_cv_dlopen_self_static=cross
13150 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13177 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
13178 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
13179 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
13183 |     lt_cv_dlopen_self_static=no
13190 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
13191 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
13200 |   case $lt_cv_dlopen_self in
13201 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
13202 |   *) enable_dlopen_self=unknown ;;
13205 |   case $lt_cv_dlopen_self_static in
13206 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
13207 |   *) enable_dlopen_self_static=unknown ;;
20349 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
20350 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
20351 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
21677 | # Whether dlopen is supported.
21678 | dlopen_support=$enable_dlopen
21680 | # Whether dlopen of programs is supported.
21681 | dlopen_self=$enable_dlopen_self
21683 | # Whether dlopen of statically linked programs is supported.
21684 | dlopen_self_static=$enable_dlopen_self_static
21728 | # Compiler flag to allow reflexive dlopens.
22070 | # Compiler flag to allow reflexive dlopens.
22223 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.2

```

{% raw %}
9335 |         enable_dlopen=no
12707 |   if test "x$enable_dlopen" != xyes; then
12708 |   enable_dlopen=unknown
12709 |   enable_dlopen_self=unknown
12710 |   enable_dlopen_self_static=unknown
12712 |   lt_cv_dlopen=no
12713 |   lt_cv_dlopen_libs=
12717 |     lt_cv_dlopen="load_add_on"
12718 |     lt_cv_dlopen_libs=
12719 |     lt_cv_dlopen_self=yes
12723 |     lt_cv_dlopen="LoadLibrary"
12724 |     lt_cv_dlopen_libs=
12728 |     lt_cv_dlopen="dlopen"
12729 |     lt_cv_dlopen_libs=
12734 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12735 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12736 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12750 | char dlopen ();
12754 | return dlopen ();
12760 |   ac_cv_lib_dl_dlopen=yes
12762 |   ac_cv_lib_dl_dlopen=no
12768 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12769 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12770 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12771 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12774 |     lt_cv_dlopen="dyld"
12775 |     lt_cv_dlopen_libs=
12776 |     lt_cv_dlopen_self=yes
12785 |   lt_cv_dlopen="shl_load"
12824 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
12826 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
12827 | if test "x$ac_cv_func_dlopen" = xyes; then :
12828 |   lt_cv_dlopen="dlopen"
12830 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12831 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12832 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12846 | char dlopen ();
12850 | return dlopen ();
12856 |   ac_cv_lib_dl_dlopen=yes
12858 |   ac_cv_lib_dl_dlopen=no
12864 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12865 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12866 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
12867 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12869 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
12870 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
12871 | if ${ac_cv_lib_svld_dlopen+:} false; then :
12885 | char dlopen ();
12889 | return dlopen ();
12895 |   ac_cv_lib_svld_dlopen=yes
12897 |   ac_cv_lib_svld_dlopen=no
12903 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
12904 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
12905 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
12906 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12945 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
12966 |   if test "x$lt_cv_dlopen" != xno; then
12967 |     enable_dlopen=yes
12969 |     enable_dlopen=no
12972 |   case $lt_cv_dlopen in
12973 |   dlopen)
12981 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12983 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
12984 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12985 | if ${lt_cv_dlopen_self+:} false; then :
12989 |   lt_cv_dlopen_self=cross
13044 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13071 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
13072 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
13073 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
13077 |     lt_cv_dlopen_self=no
13084 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
13085 | $as_echo "$lt_cv_dlopen_self" >&6; }
13087 |     if test "x$lt_cv_dlopen_self" = xyes; then
13089 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
13090 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
13091 | if ${lt_cv_dlopen_self_static+:} false; then :
13095 |   lt_cv_dlopen_self_static=cross
13150 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13177 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
13178 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
13179 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
13183 |     lt_cv_dlopen_self_static=no
13190 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
13191 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
13200 |   case $lt_cv_dlopen_self in
13201 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
13202 |   *) enable_dlopen_self=unknown ;;
13205 |   case $lt_cv_dlopen_self_static in
13206 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
13207 |   *) enable_dlopen_self_static=unknown ;;
20349 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
20350 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
20351 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
21677 | # Whether dlopen is supported.
21678 | dlopen_support=$enable_dlopen
21680 | # Whether dlopen of programs is supported.
21681 | dlopen_self=$enable_dlopen_self
21683 | # Whether dlopen of statically linked programs is supported.
21684 | dlopen_self_static=$enable_dlopen_self_static
21728 | # Compiler flag to allow reflexive dlopens.
22070 | # Compiler flag to allow reflexive dlopens.
22223 | # Compiler flag to allow reflexive dlopens.
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
2554 | m4trace:configure.ac:145: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### autom4te.cache/traces.1

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
1692 | m4trace:m4/libtool.m4:1844: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
1693 | if test "x$enable_dlopen" != xyes; then
1694 |   enable_dlopen=unknown
1695 |   enable_dlopen_self=unknown
1696 |   enable_dlopen_self_static=unknown
1698 |   lt_cv_dlopen=no
1699 |   lt_cv_dlopen_libs=
1703 |     lt_cv_dlopen="load_add_on"
1704 |     lt_cv_dlopen_libs=
1705 |     lt_cv_dlopen_self=yes
1709 |     lt_cv_dlopen="LoadLibrary"
1710 |     lt_cv_dlopen_libs=
1714 |     lt_cv_dlopen="dlopen"
1715 |     lt_cv_dlopen_libs=
1720 |     AC_CHECK_LIB([dl], [dlopen],
1721 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1722 |     lt_cv_dlopen="dyld"
1723 |     lt_cv_dlopen_libs=
1724 |     lt_cv_dlopen_self=yes
1730 | 	  [lt_cv_dlopen="shl_load"],
1732 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1733 | 	[AC_CHECK_FUNC([dlopen],
1734 | 	      [lt_cv_dlopen="dlopen"],
1735 | 	  [AC_CHECK_LIB([dl], [dlopen],
1736 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1737 | 	    [AC_CHECK_LIB([svld], [dlopen],
1738 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1740 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1749 |   if test "x$lt_cv_dlopen" != xno; then
1750 |     enable_dlopen=yes
1752 |     enable_dlopen=no
1755 |   case $lt_cv_dlopen in
1756 |   dlopen)
1764 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1766 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1767 | 	  lt_cv_dlopen_self, [dnl
1768 | 	  _LT_TRY_DLOPEN_SELF(
1769 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1770 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1773 |     if test "x$lt_cv_dlopen_self" = xyes; then
1775 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1776 | 	  lt_cv_dlopen_self_static, [dnl
1777 | 	  _LT_TRY_DLOPEN_SELF(
1778 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1779 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1789 |   case $lt_cv_dlopen_self in
1790 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1791 |   *) enable_dlopen_self=unknown ;;
1794 |   case $lt_cv_dlopen_self_static in
1795 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1796 |   *) enable_dlopen_self_static=unknown ;;
1799 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1800 | 	 [Whether dlopen is supported])
1801 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1802 | 	 [Whether dlopen of programs is supported])
1803 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1804 | 	 [Whether dlopen of statically linked programs is supported])
1806 | m4trace:m4/libtool.m4:1961: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1807 | m4trace:m4/libtool.m4:1961: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
1809 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2105 | m4trace:m4/ltoptions.m4:111: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2108 | put the `dlopen' option into LT_INIT's first parameter.])
2110 | m4trace:m4/ltoptions.m4:111: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2112 | _LT_SET_OPTION([LT_INIT], [dlopen])
2115 | put the `dlopen' option into LT_INIT's first parameter.])
2207 | m4trace:m4/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2554 | m4trace:configure.ac:145: -1- LT_SYS_DLOPEN_SELF
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