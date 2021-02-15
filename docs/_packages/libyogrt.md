---
name: "libyogrt"
layout: package
next_package: ltrace
previous_package: mindthegap
languages: ['cpp', 'bash']
---
## 1.20-2
4 / 60 files match

 - [aclocal.m4](#aclocalm4)
 - [config/ltmain.sh](#configltmainsh)
 - [src/yogrt.c](#srcyogrtc)
 - [src/none/internal.c](#srcnoneinternalc)

### aclocal.m4

```

{% raw %}
210 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
846 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
849 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
905 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
934 | ])# _LT_AC_TRY_DLOPEN_SELF
937 | # AC_LIBTOOL_DLOPEN_SELF
939 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
941 | if test "x$enable_dlopen" != xyes; then
942 |   enable_dlopen=unknown
943 |   enable_dlopen_self=unknown
944 |   enable_dlopen_self_static=unknown
946 |   lt_cv_dlopen=no
947 |   lt_cv_dlopen_libs=
951 |     lt_cv_dlopen="load_add_on"
952 |     lt_cv_dlopen_libs=
953 |     lt_cv_dlopen_self=yes
957 |     lt_cv_dlopen="LoadLibrary"
958 |     lt_cv_dlopen_libs=
962 |     lt_cv_dlopen="dlopen"
963 |     lt_cv_dlopen_libs=
968 |     AC_CHECK_LIB([dl], [dlopen],
969 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
970 |     lt_cv_dlopen="dyld"
971 |     lt_cv_dlopen_libs=
972 |     lt_cv_dlopen_self=yes
978 | 	  [lt_cv_dlopen="shl_load"],
980 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
981 | 	[AC_CHECK_FUNC([dlopen],
982 | 	      [lt_cv_dlopen="dlopen"],
983 | 	  [AC_CHECK_LIB([dl], [dlopen],
984 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
985 | 	    [AC_CHECK_LIB([svld], [dlopen],
986 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
988 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
997 |   if test "x$lt_cv_dlopen" != xno; then
998 |     enable_dlopen=yes
1000 |     enable_dlopen=no
1003 |   case $lt_cv_dlopen in
1004 |   dlopen)
1012 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1014 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1015 | 	  lt_cv_dlopen_self, [dnl
1016 | 	  _LT_AC_TRY_DLOPEN_SELF(
1017 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1018 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1021 |     if test "x$lt_cv_dlopen_self" = xyes; then
1023 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1024 |     	  lt_cv_dlopen_self_static, [dnl
1025 | 	  _LT_AC_TRY_DLOPEN_SELF(
1026 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1027 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1037 |   case $lt_cv_dlopen_self in
1038 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1039 |   *) enable_dlopen_self=unknown ;;
1042 |   case $lt_cv_dlopen_self_static in
1043 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1044 |   *) enable_dlopen_self_static=unknown ;;
1047 | ])# AC_LIBTOOL_DLOPEN_SELF
1950 | # AC_LIBTOOL_DLOPEN
1952 | # enable checks for dlopen support
1953 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1955 | ])# AC_LIBTOOL_DLOPEN
2753 | AC_LIBTOOL_DLOPEN_SELF
4491 | # Whether dlopen is supported.
4492 | dlopen_support=$enable_dlopen
4494 | # Whether dlopen of programs is supported.
4495 | dlopen_self=$enable_dlopen_self
4497 | # Whether dlopen of statically linked programs is supported.
4498 | dlopen_self_static=$enable_dlopen_self_static
4506 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
551 |   -dlopen)
552 |     prevopt="-dlopen"
636 |   # Only execute mode is allowed to have -dlopen flags.
638 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1177 | 	    dlopen_self=$dlopen_self_static
1183 | 	    dlopen_self=$dlopen_self_static
1189 | 	    dlopen_self=$dlopen_self_static
1246 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1338 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1495 |       -dlopen)
1883 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1956 | 	  # This library was specified with -dlopen.
2097 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2109 | 	passes="conv scan dlopen dlpreopen link"
2122 | 	dlopen) libs="$dlfiles" ;;
2130 |       if test "$pass" = dlopen; then
2309 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2310 | 	      # If there is no dlopen support or we're linking statically,
2343 | 	dlopen=
2364 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2407 | 	# This library was specified with -dlopen.
2408 | 	if test "$pass" = dlopen; then
2410 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2414 | 	     test "$dlopen_support" != yes ||
2416 | 	    # If there is no dlname, no dlopen support or we're linking
2425 | 	fi # $pass = dlopen
2478 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2855 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2856 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
3007 |       if test "$pass" != dlopen; then
3108 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3175 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3820 | 	    $echo "*** a static module, that should work as long as the dlopening"
3821 | 	    $echo "*** application is linked with the -dlopen flag."
3839 | 	    $echo "*** or is declared to -dlopen it."
4252 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4386 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4387 | 	   test "$dlopen_self_static" = unknown; then
4388 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5740 | # The name that we can dlopen(3).
5763 | # Files to dlopen/dlpreopen
5764 | dlopen='$dlfiles'
6379 |     # Handle -dlopen flags immediately.
6408 | 	# Skip this library if it cannot be dlopened.
6435 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6795 |   -dlopen FILE      add the directory containing FILE to the library path
6797 | This mode sets the library path environment variable according to \`-dlopen'
6846 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6855 |   -module           build a library that can dlopened
{% endraw %}

```
### src/yogrt.c

```cpp

{% raw %}
270 | 	if ((backend_handle = dlopen(path, flags)) == NULL) {
271 | 		error("dlopen failed: %s\n", dlerror());
{% endraw %}

```
### src/none/internal.c

```cpp

{% raw %}
26 |  * libraries which are dlopen()ed by the main libyogrt library.
{% endraw %}

```