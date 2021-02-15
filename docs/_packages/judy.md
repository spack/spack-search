---
name: "judy"
layout: package
next_package: steps
previous_package: z3
languages: ['bash']
---
## 1.0.5
5 / 101 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)
 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [autom4te.cache/output.1](#autom4tecacheoutput1)
 - [autom4te.cache/traces.0](#autom4tecachetraces0)

### ltmain.sh

```bash

{% raw %}
522 |   -dlopen)
523 |     prevopt="-dlopen"
607 |   # Only execute mode is allowed to have -dlopen flags.
609 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1146 | 	    dlopen_self=$dlopen_self_static
1151 | 	    dlopen_self=$dlopen_self_static
1207 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1299 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1456 |       -dlopen)
1843 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1916 | 	  # This library was specified with -dlopen.
2057 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2069 | 	passes="conv scan dlopen dlpreopen link"
2082 | 	dlopen) libs="$dlfiles" ;;
2090 |       if test "$pass" = dlopen; then
2269 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2270 | 	      # If there is no dlopen support or we're linking statically,
2303 | 	dlopen=
2324 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2367 | 	# This library was specified with -dlopen.
2368 | 	if test "$pass" = dlopen; then
2370 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2374 | 	     test "$dlopen_support" != yes ||
2376 | 	    # If there is no dlname, no dlopen support or we're linking
2385 | 	fi # $pass = dlopen
2438 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2813 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2814 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2965 |       if test "$pass" != dlopen; then
3066 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3133 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3776 | 	    $echo "*** a static module, that should work as long as the dlopening"
3777 | 	    $echo "*** application is linked with the -dlopen flag."
3795 | 	    $echo "*** or is declared to -dlopen it."
4205 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4337 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4338 | 	   test "$dlopen_self_static" = unknown; then
4339 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5677 | # The name that we can dlopen(3).
5700 | # Files to dlopen/dlpreopen
5701 | dlopen='$dlfiles'
6316 |     # Handle -dlopen flags immediately.
6345 | 	# Skip this library if it cannot be dlopened.
6370 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6730 |   -dlopen FILE      add the directory containing FILE to the library path
6732 | This mode sets the library path environment variable according to \`-dlopen'
6781 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6790 |   -module           build a library that can dlopened
{% endraw %}

```
### aclocal.m4

```

{% raw %}
205 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
820 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
823 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
879 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
908 | ])# _LT_AC_TRY_DLOPEN_SELF
911 | # AC_LIBTOOL_DLOPEN_SELF
913 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
915 | if test "x$enable_dlopen" != xyes; then
916 |   enable_dlopen=unknown
917 |   enable_dlopen_self=unknown
918 |   enable_dlopen_self_static=unknown
920 |   lt_cv_dlopen=no
921 |   lt_cv_dlopen_libs=
925 |     lt_cv_dlopen="load_add_on"
926 |     lt_cv_dlopen_libs=
927 |     lt_cv_dlopen_self=yes
931 |     lt_cv_dlopen="LoadLibrary"
932 |     lt_cv_dlopen_libs=
936 |     lt_cv_dlopen="dlopen"
937 |     lt_cv_dlopen_libs=
942 |     AC_CHECK_LIB([dl], [dlopen],
943 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
944 |     lt_cv_dlopen="dyld"
945 |     lt_cv_dlopen_libs=
946 |     lt_cv_dlopen_self=yes
952 | 	  [lt_cv_dlopen="shl_load"],
954 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
955 | 	[AC_CHECK_FUNC([dlopen],
956 | 	      [lt_cv_dlopen="dlopen"],
957 | 	  [AC_CHECK_LIB([dl], [dlopen],
958 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
959 | 	    [AC_CHECK_LIB([svld], [dlopen],
960 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
962 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
971 |   if test "x$lt_cv_dlopen" != xno; then
972 |     enable_dlopen=yes
974 |     enable_dlopen=no
977 |   case $lt_cv_dlopen in
978 |   dlopen)
986 |     LIBS="$lt_cv_dlopen_libs $LIBS"
988 |     AC_CACHE_CHECK([whether a program can dlopen itself],
989 | 	  lt_cv_dlopen_self, [dnl
990 | 	  _LT_AC_TRY_DLOPEN_SELF(
991 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
992 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
995 |     if test "x$lt_cv_dlopen_self" = xyes; then
997 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
998 |     	  lt_cv_dlopen_self_static, [dnl
999 | 	  _LT_AC_TRY_DLOPEN_SELF(
1000 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1001 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1011 |   case $lt_cv_dlopen_self in
1012 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1013 |   *) enable_dlopen_self=unknown ;;
1016 |   case $lt_cv_dlopen_self_static in
1017 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1018 |   *) enable_dlopen_self_static=unknown ;;
1021 | ])# AC_LIBTOOL_DLOPEN_SELF
1882 | # AC_LIBTOOL_DLOPEN
1884 | # enable checks for dlopen support
1885 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1887 | ])# AC_LIBTOOL_DLOPEN
2675 | AC_LIBTOOL_DLOPEN_SELF
4346 | # Whether dlopen is supported.
4347 | dlopen_support=$enable_dlopen
4349 | # Whether dlopen of programs is supported.
4350 | dlopen_self=$enable_dlopen_self
4352 | # Whether dlopen of statically linked programs is supported.
4353 | dlopen_self_static=$enable_dlopen_self_static
4361 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.0

```

{% raw %}
10211 | enable_dlopen=no
12405 | if test "x$enable_dlopen" != xyes; then
12406 |   enable_dlopen=unknown
12407 |   enable_dlopen_self=unknown
12408 |   enable_dlopen_self_static=unknown
12410 |   lt_cv_dlopen=no
12411 |   lt_cv_dlopen_libs=
12415 |     lt_cv_dlopen="load_add_on"
12416 |     lt_cv_dlopen_libs=
12417 |     lt_cv_dlopen_self=yes
12421 |     lt_cv_dlopen="LoadLibrary"
12422 |     lt_cv_dlopen_libs=
12426 |     lt_cv_dlopen="dlopen"
12427 |     lt_cv_dlopen_libs=
12432 |     { echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
12433 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6; }
12434 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
12452 | char dlopen ();
12456 | return dlopen ();
12479 |   ac_cv_lib_dl_dlopen=yes
12484 | 	ac_cv_lib_dl_dlopen=no
12491 | { echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
12492 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6; }
12493 | if test $ac_cv_lib_dl_dlopen = yes; then
12494 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12497 |     lt_cv_dlopen="dyld"
12498 |     lt_cv_dlopen_libs=
12499 |     lt_cv_dlopen_self=yes
12588 |   lt_cv_dlopen="shl_load"
12652 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"
12654 |   { echo "$as_me:$LINENO: checking for dlopen" >&5
12655 | echo $ECHO_N "checking for dlopen... $ECHO_C" >&6; }
12656 | if test "${ac_cv_func_dlopen+set}" = set; then
12665 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
12667 | #define dlopen innocuous_dlopen
12670 |     which can conflict with char dlopen (); below.
12680 | #undef dlopen
12688 | char dlopen ();
12692 | #if defined __stub_dlopen || defined __stub___dlopen
12699 | return dlopen ();
12722 |   ac_cv_func_dlopen=yes
12727 | 	ac_cv_func_dlopen=no
12733 | { echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
12734 | echo "${ECHO_T}$ac_cv_func_dlopen" >&6; }
12735 | if test $ac_cv_func_dlopen = yes; then
12736 |   lt_cv_dlopen="dlopen"
12738 |   { echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
12739 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6; }
12740 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
12758 | char dlopen ();
12762 | return dlopen ();
12785 |   ac_cv_lib_dl_dlopen=yes
12790 | 	ac_cv_lib_dl_dlopen=no
12797 | { echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
12798 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6; }
12799 | if test $ac_cv_lib_dl_dlopen = yes; then
12800 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12802 |   { echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
12803 | echo $ECHO_N "checking for dlopen in -lsvld... $ECHO_C" >&6; }
12804 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
12822 | char dlopen ();
12826 | return dlopen ();
12849 |   ac_cv_lib_svld_dlopen=yes
12854 | 	ac_cv_lib_svld_dlopen=no
12861 | { echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
12862 | echo "${ECHO_T}$ac_cv_lib_svld_dlopen" >&6; }
12863 | if test $ac_cv_lib_svld_dlopen = yes; then
12864 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12928 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"
12949 |   if test "x$lt_cv_dlopen" != xno; then
12950 |     enable_dlopen=yes
12952 |     enable_dlopen=no
12955 |   case $lt_cv_dlopen in
12956 |   dlopen)
12964 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12966 |     { echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
12967 | echo $ECHO_N "checking whether a program can dlopen itself... $ECHO_C" >&6; }
12968 | if test "${lt_cv_dlopen_self+set}" = set; then
12972 |   lt_cv_dlopen_self=cross
13025 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13048 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
13049 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
13050 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
13054 |     lt_cv_dlopen_self=no
13061 | { echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
13062 | echo "${ECHO_T}$lt_cv_dlopen_self" >&6; }
13064 |     if test "x$lt_cv_dlopen_self" = xyes; then
13066 |       { echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
13067 | echo $ECHO_N "checking whether a statically linked program can dlopen itself... $ECHO_C" >&6; }
13068 | if test "${lt_cv_dlopen_self_static+set}" = set; then
13072 |   lt_cv_dlopen_self_static=cross
13125 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13148 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
13149 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
13150 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
13154 |     lt_cv_dlopen_self_static=no
13161 | { echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
13162 | echo "${ECHO_T}$lt_cv_dlopen_self_static" >&6; }
13171 |   case $lt_cv_dlopen_self in
13172 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
13173 |   *) enable_dlopen_self=unknown ;;
13176 |   case $lt_cv_dlopen_self_static in
13177 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
13178 |   *) enable_dlopen_self_static=unknown ;;
13476 | # Whether dlopen is supported.
13477 | dlopen_support=$enable_dlopen
13479 | # Whether dlopen of programs is supported.
13480 | dlopen_self=$enable_dlopen_self
13482 | # Whether dlopen of statically linked programs is supported.
13483 | dlopen_self_static=$enable_dlopen_self_static
13491 | # Compiler flag to allow reflexive dlopens.
16499 | # Whether dlopen is supported.
16500 | dlopen_support=$enable_dlopen
16502 | # Whether dlopen of programs is supported.
16503 | dlopen_self=$enable_dlopen_self
16505 | # Whether dlopen of statically linked programs is supported.
16506 | dlopen_self_static=$enable_dlopen_self_static
16514 | # Compiler flag to allow reflexive dlopens.
19071 | # Whether dlopen is supported.
19072 | dlopen_support=$enable_dlopen
19074 | # Whether dlopen of programs is supported.
19075 | dlopen_self=$enable_dlopen_self
19077 | # Whether dlopen of statically linked programs is supported.
19078 | dlopen_self_static=$enable_dlopen_self_static
19086 | # Compiler flag to allow reflexive dlopens.
21654 | # Whether dlopen is supported.
21655 | dlopen_support=$enable_dlopen
21657 | # Whether dlopen of programs is supported.
21658 | dlopen_self=$enable_dlopen_self
21660 | # Whether dlopen of statically linked programs is supported.
21661 | dlopen_self_static=$enable_dlopen_self_static
21669 | # Compiler flag to allow reflexive dlopens.
22134 | # Whether dlopen is supported.
22135 | dlopen_support=$enable_dlopen
22137 | # Whether dlopen of programs is supported.
22138 | dlopen_self=$enable_dlopen_self
22140 | # Whether dlopen of statically linked programs is supported.
22141 | dlopen_self_static=$enable_dlopen_self_static
22149 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.1

```

{% raw %}
10211 | enable_dlopen=no
12401 | if test "x$enable_dlopen" != xyes; then
12402 |   enable_dlopen=unknown
12403 |   enable_dlopen_self=unknown
12404 |   enable_dlopen_self_static=unknown
12406 |   lt_cv_dlopen=no
12407 |   lt_cv_dlopen_libs=
12411 |     lt_cv_dlopen="load_add_on"
12412 |     lt_cv_dlopen_libs=
12413 |     lt_cv_dlopen_self=yes
12417 |     lt_cv_dlopen="LoadLibrary"
12418 |     lt_cv_dlopen_libs=
12422 |     lt_cv_dlopen="dlopen"
12423 |     lt_cv_dlopen_libs=
12428 |     { echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
12429 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6; }
12430 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
12448 | char dlopen ();
12452 | return dlopen ();
12475 |   ac_cv_lib_dl_dlopen=yes
12480 | 	ac_cv_lib_dl_dlopen=no
12487 | { echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
12488 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6; }
12489 | if test $ac_cv_lib_dl_dlopen = yes; then
12490 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12493 |     lt_cv_dlopen="dyld"
12494 |     lt_cv_dlopen_libs=
12495 |     lt_cv_dlopen_self=yes
12584 |   lt_cv_dlopen="shl_load"
12648 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"
12650 |   { echo "$as_me:$LINENO: checking for dlopen" >&5
12651 | echo $ECHO_N "checking for dlopen... $ECHO_C" >&6; }
12652 | if test "${ac_cv_func_dlopen+set}" = set; then
12661 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
12663 | #define dlopen innocuous_dlopen
12666 |     which can conflict with char dlopen (); below.
12676 | #undef dlopen
12684 | char dlopen ();
12688 | #if defined __stub_dlopen || defined __stub___dlopen
12695 | return dlopen ();
12718 |   ac_cv_func_dlopen=yes
12723 | 	ac_cv_func_dlopen=no
12729 | { echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
12730 | echo "${ECHO_T}$ac_cv_func_dlopen" >&6; }
12731 | if test $ac_cv_func_dlopen = yes; then
12732 |   lt_cv_dlopen="dlopen"
12734 |   { echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
12735 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6; }
12736 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
12754 | char dlopen ();
12758 | return dlopen ();
12781 |   ac_cv_lib_dl_dlopen=yes
12786 | 	ac_cv_lib_dl_dlopen=no
12793 | { echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
12794 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6; }
12795 | if test $ac_cv_lib_dl_dlopen = yes; then
12796 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12798 |   { echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
12799 | echo $ECHO_N "checking for dlopen in -lsvld... $ECHO_C" >&6; }
12800 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
12818 | char dlopen ();
12822 | return dlopen ();
12845 |   ac_cv_lib_svld_dlopen=yes
12850 | 	ac_cv_lib_svld_dlopen=no
12857 | { echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
12858 | echo "${ECHO_T}$ac_cv_lib_svld_dlopen" >&6; }
12859 | if test $ac_cv_lib_svld_dlopen = yes; then
12860 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12924 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"
12945 |   if test "x$lt_cv_dlopen" != xno; then
12946 |     enable_dlopen=yes
12948 |     enable_dlopen=no
12951 |   case $lt_cv_dlopen in
12952 |   dlopen)
12960 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12962 |     { echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
12963 | echo $ECHO_N "checking whether a program can dlopen itself... $ECHO_C" >&6; }
12964 | if test "${lt_cv_dlopen_self+set}" = set; then
12968 |   lt_cv_dlopen_self=cross
13021 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13044 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
13045 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
13046 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
13050 |     lt_cv_dlopen_self=no
13057 | { echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
13058 | echo "${ECHO_T}$lt_cv_dlopen_self" >&6; }
13060 |     if test "x$lt_cv_dlopen_self" = xyes; then
13062 |       { echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
13063 | echo $ECHO_N "checking whether a statically linked program can dlopen itself... $ECHO_C" >&6; }
13064 | if test "${lt_cv_dlopen_self_static+set}" = set; then
13068 |   lt_cv_dlopen_self_static=cross
13121 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13144 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
13145 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
13146 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
13150 |     lt_cv_dlopen_self_static=no
13157 | { echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
13158 | echo "${ECHO_T}$lt_cv_dlopen_self_static" >&6; }
13167 |   case $lt_cv_dlopen_self in
13168 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
13169 |   *) enable_dlopen_self=unknown ;;
13172 |   case $lt_cv_dlopen_self_static in
13173 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
13174 |   *) enable_dlopen_self_static=unknown ;;
13472 | # Whether dlopen is supported.
13473 | dlopen_support=$enable_dlopen
13475 | # Whether dlopen of programs is supported.
13476 | dlopen_self=$enable_dlopen_self
13478 | # Whether dlopen of statically linked programs is supported.
13479 | dlopen_self_static=$enable_dlopen_self_static
13487 | # Compiler flag to allow reflexive dlopens.
16491 | # Whether dlopen is supported.
16492 | dlopen_support=$enable_dlopen
16494 | # Whether dlopen of programs is supported.
16495 | dlopen_self=$enable_dlopen_self
16497 | # Whether dlopen of statically linked programs is supported.
16498 | dlopen_self_static=$enable_dlopen_self_static
16506 | # Compiler flag to allow reflexive dlopens.
19063 | # Whether dlopen is supported.
19064 | dlopen_support=$enable_dlopen
19066 | # Whether dlopen of programs is supported.
19067 | dlopen_self=$enable_dlopen_self
19069 | # Whether dlopen of statically linked programs is supported.
19070 | dlopen_self_static=$enable_dlopen_self_static
19078 | # Compiler flag to allow reflexive dlopens.
21642 | # Whether dlopen is supported.
21643 | dlopen_support=$enable_dlopen
21645 | # Whether dlopen of programs is supported.
21646 | dlopen_self=$enable_dlopen_self
21648 | # Whether dlopen of statically linked programs is supported.
21649 | dlopen_self_static=$enable_dlopen_self_static
21657 | # Compiler flag to allow reflexive dlopens.
22122 | # Whether dlopen is supported.
22123 | dlopen_support=$enable_dlopen
22125 | # Whether dlopen of programs is supported.
22126 | dlopen_self=$enable_dlopen_self
22128 | # Whether dlopen of statically linked programs is supported.
22129 | dlopen_self_static=$enable_dlopen_self_static
22137 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.0

```

{% raw %}
164 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
700 | m4trace:/usr/share/aclocal/libtool.m4:818: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF], [AC_REQUIRE([_LT_AC_CHECK_DLFCN])dnl
755 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
785 | m4trace:/usr/share/aclocal/libtool.m4:908: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_REQUIRE([_LT_AC_CHECK_DLFCN])dnl
786 | if test "x$enable_dlopen" != xyes; then
787 |   enable_dlopen=unknown
788 |   enable_dlopen_self=unknown
789 |   enable_dlopen_self_static=unknown
791 |   lt_cv_dlopen=no
792 |   lt_cv_dlopen_libs=
796 |     lt_cv_dlopen="load_add_on"
797 |     lt_cv_dlopen_libs=
798 |     lt_cv_dlopen_self=yes
802 |     lt_cv_dlopen="LoadLibrary"
803 |     lt_cv_dlopen_libs=
807 |     lt_cv_dlopen="dlopen"
808 |     lt_cv_dlopen_libs=
813 |     AC_CHECK_LIB([dl], [dlopen],
814 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
815 |     lt_cv_dlopen="dyld"
816 |     lt_cv_dlopen_libs=
817 |     lt_cv_dlopen_self=yes
823 | 	  [lt_cv_dlopen="shl_load"],
825 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
826 | 	[AC_CHECK_FUNC([dlopen],
827 | 	      [lt_cv_dlopen="dlopen"],
828 | 	  [AC_CHECK_LIB([dl], [dlopen],
829 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
830 | 	    [AC_CHECK_LIB([svld], [dlopen],
831 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
833 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
842 |   if test "x$lt_cv_dlopen" != xno; then
843 |     enable_dlopen=yes
845 |     enable_dlopen=no
848 |   case $lt_cv_dlopen in
849 |   dlopen)
857 |     LIBS="$lt_cv_dlopen_libs $LIBS"
859 |     AC_CACHE_CHECK([whether a program can dlopen itself],
860 | 	  lt_cv_dlopen_self, [dnl
861 | 	  _LT_AC_TRY_DLOPEN_SELF(
862 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
863 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
866 |     if test "x$lt_cv_dlopen_self" = xyes; then
868 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
869 |     	  lt_cv_dlopen_self_static, [dnl
870 | 	  _LT_AC_TRY_DLOPEN_SELF(
871 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
872 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
882 |   case $lt_cv_dlopen_self in
883 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
884 |   *) enable_dlopen_self=unknown ;;
887 |   case $lt_cv_dlopen_self_static in
888 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
889 |   *) enable_dlopen_self_static=unknown ;;
1712 | m4trace:/usr/share/aclocal/libtool.m4:1880: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_BEFORE([$0],[AC_LIBTOOL_SETUP])
2310 | AC_LIBTOOL_DLOPEN_SELF
3942 | # Whether dlopen is supported.
3943 | dlopen_support=$enable_dlopen
3945 | # Whether dlopen of programs is supported.
3946 | dlopen_self=$enable_dlopen_self
3948 | # Whether dlopen of statically linked programs is supported.
3949 | dlopen_self_static=$enable_dlopen_self_static
3957 | # Compiler flag to allow reflexive dlopens.
7295 | m4trace:configure.ac:244: -1- AC_LIBTOOL_DLOPEN_SELF
7297 | m4trace:configure.ac:244: -1- _LT_AC_TRY_DLOPEN_SELF([lt_cv_dlopen_self=yes], [lt_cv_dlopen_self=yes], [lt_cv_dlopen_self=no], [lt_cv_dlopen_self=cross])
7298 | m4trace:configure.ac:244: -1- _LT_AC_TRY_DLOPEN_SELF([lt_cv_dlopen_self_static=yes], [lt_cv_dlopen_self_static=yes], [lt_cv_dlopen_self_static=no], [lt_cv_dlopen_self_static=cross])
{% endraw %}

```