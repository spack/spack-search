---
name: "fastdb"
layout: package
next_package: elfutils
previous_package: libevent
languages: ['bash']
---
## 3.75
5 / 716 files match

 - [aclocal.m4](#aclocalm4)
 - [config/ltmain.sh](#configltmainsh)
 - [config/.svn/text-base/ltmain.sh.svn-base](#configsvntext-baseltmainshsvn-base)
 - [.svn/text-base/configure.svn-base](#svntext-baseconfiguresvn-base)
 - [.svn/text-base/aclocal.m4.svn-base](#svntext-baseaclocalm4svn-base)

### aclocal.m4

```

{% raw %}
214 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
968 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
971 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
1027 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1056 | ])# _LT_AC_TRY_DLOPEN_SELF
1059 | # AC_LIBTOOL_DLOPEN_SELF
1061 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1063 | if test "x$enable_dlopen" != xyes; then
1064 |   enable_dlopen=unknown
1065 |   enable_dlopen_self=unknown
1066 |   enable_dlopen_self_static=unknown
1068 |   lt_cv_dlopen=no
1069 |   lt_cv_dlopen_libs=
1073 |     lt_cv_dlopen="load_add_on"
1074 |     lt_cv_dlopen_libs=
1075 |     lt_cv_dlopen_self=yes
1079 |     lt_cv_dlopen="LoadLibrary"
1080 |     lt_cv_dlopen_libs=
1084 |     lt_cv_dlopen="dlopen"
1085 |     lt_cv_dlopen_libs=
1090 |     AC_CHECK_LIB([dl], [dlopen],
1091 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1092 |     lt_cv_dlopen="dyld"
1093 |     lt_cv_dlopen_libs=
1094 |     lt_cv_dlopen_self=yes
1100 | 	  [lt_cv_dlopen="shl_load"],
1102 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1103 | 	[AC_CHECK_FUNC([dlopen],
1104 | 	      [lt_cv_dlopen="dlopen"],
1105 | 	  [AC_CHECK_LIB([dl], [dlopen],
1106 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1107 | 	    [AC_CHECK_LIB([svld], [dlopen],
1108 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1110 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1119 |   if test "x$lt_cv_dlopen" != xno; then
1120 |     enable_dlopen=yes
1122 |     enable_dlopen=no
1125 |   case $lt_cv_dlopen in
1126 |   dlopen)
1134 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1136 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1137 | 	  lt_cv_dlopen_self, [dnl
1138 | 	  _LT_AC_TRY_DLOPEN_SELF(
1139 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1140 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1143 |     if test "x$lt_cv_dlopen_self" = xyes; then
1145 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1146 |     	  lt_cv_dlopen_self_static, [dnl
1147 | 	  _LT_AC_TRY_DLOPEN_SELF(
1148 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1149 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1159 |   case $lt_cv_dlopen_self in
1160 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1161 |   *) enable_dlopen_self=unknown ;;
1164 |   case $lt_cv_dlopen_self_static in
1165 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1166 |   *) enable_dlopen_self_static=unknown ;;
1169 | ])# AC_LIBTOOL_DLOPEN_SELF
2080 | # AC_LIBTOOL_DLOPEN
2082 | # enable checks for dlopen support
2083 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2085 | ])# AC_LIBTOOL_DLOPEN
2883 | AC_LIBTOOL_DLOPEN_SELF
4600 | # Whether dlopen is supported.
4601 | dlopen_support=$enable_dlopen
4603 | # Whether dlopen of programs is supported.
4604 | dlopen_self=$enable_dlopen_self
4606 | # Whether dlopen of statically linked programs is supported.
4607 | dlopen_self_static=$enable_dlopen_self_static
4615 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
571 |   -dlopen)
572 |     prevopt="-dlopen"
656 |   # Only execute mode is allowed to have -dlopen flags.
658 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1199 | 	    dlopen_self=$dlopen_self_static
1205 | 	    dlopen_self=$dlopen_self_static
1211 | 	    dlopen_self=$dlopen_self_static
1268 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1360 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1517 |       -dlopen)
1910 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1983 | 	  # This library was specified with -dlopen.
2124 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2136 | 	passes="conv scan dlopen dlpreopen link"
2149 | 	dlopen) libs="$dlfiles" ;;
2154 |       if test "$pass" = dlopen; then
2338 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2339 | 	      # If there is no dlopen support or we're linking statically,
2372 | 	dlopen=
2393 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2436 | 	# This library was specified with -dlopen.
2437 | 	if test "$pass" = dlopen; then
2439 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2443 | 	     test "$dlopen_support" != yes ||
2445 | 	    # If there is no dlname, no dlopen support or we're linking
2454 | 	fi # $pass = dlopen
2507 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2884 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2885 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
3042 |       if test "$pass" != dlopen; then
3144 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3211 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3851 | 	    $echo "*** a static module, that should work as long as the dlopening"
3852 | 	    $echo "*** application is linked with the -dlopen flag."
3870 | 	    $echo "*** or is declared to -dlopen it."
4284 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4418 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4419 | 	   test "$dlopen_self_static" = unknown; then
4420 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5777 | # The name that we can dlopen(3).
5800 | # Files to dlopen/dlpreopen
5801 | dlopen='$dlfiles'
6416 |     # Handle -dlopen flags immediately.
6445 | 	# Skip this library if it cannot be dlopened.
6472 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6832 |   -dlopen FILE      add the directory containing FILE to the library path
6834 | This mode sets the library path environment variable according to \`-dlopen'
6883 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6892 |   -module           build a library that can dlopened
{% endraw %}

```
### config/.svn/text-base/ltmain.sh.svn-base

```

{% raw %}
571 |   -dlopen)
572 |     prevopt="-dlopen"
656 |   # Only execute mode is allowed to have -dlopen flags.
658 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1199 | 	    dlopen_self=$dlopen_self_static
1205 | 	    dlopen_self=$dlopen_self_static
1211 | 	    dlopen_self=$dlopen_self_static
1268 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1360 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1517 |       -dlopen)
1910 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1983 | 	  # This library was specified with -dlopen.
2124 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2136 | 	passes="conv scan dlopen dlpreopen link"
2149 | 	dlopen) libs="$dlfiles" ;;
2154 |       if test "$pass" = dlopen; then
2338 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2339 | 	      # If there is no dlopen support or we're linking statically,
2372 | 	dlopen=
2393 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2436 | 	# This library was specified with -dlopen.
2437 | 	if test "$pass" = dlopen; then
2439 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2443 | 	     test "$dlopen_support" != yes ||
2445 | 	    # If there is no dlname, no dlopen support or we're linking
2454 | 	fi # $pass = dlopen
2507 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2884 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2885 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
3042 |       if test "$pass" != dlopen; then
3144 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3211 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3851 | 	    $echo "*** a static module, that should work as long as the dlopening"
3852 | 	    $echo "*** application is linked with the -dlopen flag."
3870 | 	    $echo "*** or is declared to -dlopen it."
4284 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4418 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4419 | 	   test "$dlopen_self_static" = unknown; then
4420 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5777 | # The name that we can dlopen(3).
5800 | # Files to dlopen/dlpreopen
5801 | dlopen='$dlfiles'
6416 |     # Handle -dlopen flags immediately.
6445 | 	# Skip this library if it cannot be dlopened.
6472 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6832 |   -dlopen FILE      add the directory containing FILE to the library path
6834 | This mode sets the library path environment variable according to \`-dlopen'
6883 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6892 |   -module           build a library that can dlopened
{% endraw %}

```
### .svn/text-base/configure.svn-base

```

{% raw %}
7807 | enable_dlopen=no
10168 | if test "x$enable_dlopen" != xyes; then
10169 |   enable_dlopen=unknown
10170 |   enable_dlopen_self=unknown
10171 |   enable_dlopen_self_static=unknown
10173 |   lt_cv_dlopen=no
10174 |   lt_cv_dlopen_libs=
10178 |     lt_cv_dlopen="load_add_on"
10179 |     lt_cv_dlopen_libs=
10180 |     lt_cv_dlopen_self=yes
10184 |     lt_cv_dlopen="LoadLibrary"
10185 |     lt_cv_dlopen_libs=
10189 |     lt_cv_dlopen="dlopen"
10190 |     lt_cv_dlopen_libs=
10195 |     { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
10196 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10197 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
10215 | char dlopen ();
10219 | return dlopen ();
10245 |   ac_cv_lib_dl_dlopen=yes
10250 | 	ac_cv_lib_dl_dlopen=no
10258 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
10259 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10260 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
10261 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10264 |     lt_cv_dlopen="dyld"
10265 |     lt_cv_dlopen_libs=
10266 |     lt_cv_dlopen_self=yes
10359 |   lt_cv_dlopen="shl_load"
10427 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
10429 |   { $as_echo "$as_me:$LINENO: checking for dlopen" >&5
10430 | $as_echo_n "checking for dlopen... " >&6; }
10431 | if test "${ac_cv_func_dlopen+set}" = set; then
10440 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
10442 | #define dlopen innocuous_dlopen
10445 |     which can conflict with char dlopen (); below.
10455 | #undef dlopen
10463 | char dlopen ();
10467 | #if defined __stub_dlopen || defined __stub___dlopen
10474 | return dlopen ();
10500 |   ac_cv_func_dlopen=yes
10505 | 	ac_cv_func_dlopen=no
10512 | { $as_echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
10513 | $as_echo "$ac_cv_func_dlopen" >&6; }
10514 | if test "x$ac_cv_func_dlopen" = x""yes; then
10515 |   lt_cv_dlopen="dlopen"
10517 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
10518 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10519 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
10537 | char dlopen ();
10541 | return dlopen ();
10567 |   ac_cv_lib_dl_dlopen=yes
10572 | 	ac_cv_lib_dl_dlopen=no
10580 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
10581 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10582 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
10583 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10585 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
10586 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
10587 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
10605 | char dlopen ();
10609 | return dlopen ();
10635 |   ac_cv_lib_svld_dlopen=yes
10640 | 	ac_cv_lib_svld_dlopen=no
10648 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
10649 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
10650 | if test "x$ac_cv_lib_svld_dlopen" = x""yes; then
10651 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
10719 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
10740 |   if test "x$lt_cv_dlopen" != xno; then
10741 |     enable_dlopen=yes
10743 |     enable_dlopen=no
10746 |   case $lt_cv_dlopen in
10747 |   dlopen)
10755 |     LIBS="$lt_cv_dlopen_libs $LIBS"
10757 |     { $as_echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
10758 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
10759 | if test "${lt_cv_dlopen_self+set}" = set; then
10763 |   lt_cv_dlopen_self=cross
10816 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10839 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
10840 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
10841 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
10845 |     lt_cv_dlopen_self=no
10852 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
10853 | $as_echo "$lt_cv_dlopen_self" >&6; }
10855 |     if test "x$lt_cv_dlopen_self" = xyes; then
10857 |       { $as_echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
10858 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
10859 | if test "${lt_cv_dlopen_self_static+set}" = set; then
10863 |   lt_cv_dlopen_self_static=cross
10916 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10939 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
10940 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
10941 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
10945 |     lt_cv_dlopen_self_static=no
10952 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
10953 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
10962 |   case $lt_cv_dlopen_self in
10963 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
10964 |   *) enable_dlopen_self=unknown ;;
10967 |   case $lt_cv_dlopen_self_static in
10968 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
10969 |   *) enable_dlopen_self_static=unknown ;;
11269 | # Whether dlopen is supported.
11270 | dlopen_support=$enable_dlopen
11272 | # Whether dlopen of programs is supported.
11273 | dlopen_self=$enable_dlopen_self
11275 | # Whether dlopen of statically linked programs is supported.
11276 | dlopen_self_static=$enable_dlopen_self_static
11284 | # Compiler flag to allow reflexive dlopens.
14361 | # Whether dlopen is supported.
14362 | dlopen_support=$enable_dlopen
14364 | # Whether dlopen of programs is supported.
14365 | dlopen_self=$enable_dlopen_self
14367 | # Whether dlopen of statically linked programs is supported.
14368 | dlopen_self_static=$enable_dlopen_self_static
14376 | # Compiler flag to allow reflexive dlopens.
17003 | # Whether dlopen is supported.
17004 | dlopen_support=$enable_dlopen
17006 | # Whether dlopen of programs is supported.
17007 | dlopen_self=$enable_dlopen_self
17009 | # Whether dlopen of statically linked programs is supported.
17010 | dlopen_self_static=$enable_dlopen_self_static
17018 | # Compiler flag to allow reflexive dlopens.
19645 | # Whether dlopen is supported.
19646 | dlopen_support=$enable_dlopen
19648 | # Whether dlopen of programs is supported.
19649 | dlopen_self=$enable_dlopen_self
19651 | # Whether dlopen of statically linked programs is supported.
19652 | dlopen_self_static=$enable_dlopen_self_static
19660 | # Compiler flag to allow reflexive dlopens.
20131 | # Whether dlopen is supported.
20132 | dlopen_support=$enable_dlopen
20134 | # Whether dlopen of programs is supported.
20135 | dlopen_self=$enable_dlopen_self
20137 | # Whether dlopen of statically linked programs is supported.
20138 | dlopen_self_static=$enable_dlopen_self_static
20146 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### .svn/text-base/aclocal.m4.svn-base

```

{% raw %}
214 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
968 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
971 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
1027 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1056 | ])# _LT_AC_TRY_DLOPEN_SELF
1059 | # AC_LIBTOOL_DLOPEN_SELF
1061 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1063 | if test "x$enable_dlopen" != xyes; then
1064 |   enable_dlopen=unknown
1065 |   enable_dlopen_self=unknown
1066 |   enable_dlopen_self_static=unknown
1068 |   lt_cv_dlopen=no
1069 |   lt_cv_dlopen_libs=
1073 |     lt_cv_dlopen="load_add_on"
1074 |     lt_cv_dlopen_libs=
1075 |     lt_cv_dlopen_self=yes
1079 |     lt_cv_dlopen="LoadLibrary"
1080 |     lt_cv_dlopen_libs=
1084 |     lt_cv_dlopen="dlopen"
1085 |     lt_cv_dlopen_libs=
1090 |     AC_CHECK_LIB([dl], [dlopen],
1091 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1092 |     lt_cv_dlopen="dyld"
1093 |     lt_cv_dlopen_libs=
1094 |     lt_cv_dlopen_self=yes
1100 | 	  [lt_cv_dlopen="shl_load"],
1102 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1103 | 	[AC_CHECK_FUNC([dlopen],
1104 | 	      [lt_cv_dlopen="dlopen"],
1105 | 	  [AC_CHECK_LIB([dl], [dlopen],
1106 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1107 | 	    [AC_CHECK_LIB([svld], [dlopen],
1108 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1110 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1119 |   if test "x$lt_cv_dlopen" != xno; then
1120 |     enable_dlopen=yes
1122 |     enable_dlopen=no
1125 |   case $lt_cv_dlopen in
1126 |   dlopen)
1134 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1136 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1137 | 	  lt_cv_dlopen_self, [dnl
1138 | 	  _LT_AC_TRY_DLOPEN_SELF(
1139 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1140 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1143 |     if test "x$lt_cv_dlopen_self" = xyes; then
1145 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1146 |     	  lt_cv_dlopen_self_static, [dnl
1147 | 	  _LT_AC_TRY_DLOPEN_SELF(
1148 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1149 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1159 |   case $lt_cv_dlopen_self in
1160 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1161 |   *) enable_dlopen_self=unknown ;;
1164 |   case $lt_cv_dlopen_self_static in
1165 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1166 |   *) enable_dlopen_self_static=unknown ;;
1169 | ])# AC_LIBTOOL_DLOPEN_SELF
2080 | # AC_LIBTOOL_DLOPEN
2082 | # enable checks for dlopen support
2083 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2085 | ])# AC_LIBTOOL_DLOPEN
2883 | AC_LIBTOOL_DLOPEN_SELF
4600 | # Whether dlopen is supported.
4601 | dlopen_support=$enable_dlopen
4603 | # Whether dlopen of programs is supported.
4604 | dlopen_self=$enable_dlopen_self
4606 | # Whether dlopen of statically linked programs is supported.
4607 | dlopen_self_static=$enable_dlopen_self_static
4615 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```