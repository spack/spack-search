---
name: "id3lib"
layout: package
next_package: openfoam
previous_package: libbsd
languages: ['bash']
---
## 3.8.3
3 / 229 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)
 - [zlib/aclocal.m4](#zlibaclocalm4)

### ltmain.sh

```bash

{% raw %}
183 |   -dlopen)
184 |     prevopt="-dlopen"
254 |   # Only execute mode is allowed to have -dlopen flags.
256 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
795 | 	    dlopen_self=$dlopen_self_static
799 | 	    dlopen_self=$dlopen_self_static
855 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
962 |       -dlopen)
1206 | 	  # This file was specified with -dlopen.
1207 | 	  if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1240 | 	  # This library was specified with -dlopen.
1350 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1362 | 	passes="conv scan dlopen dlpreopen link"
1371 | 	dlopen)
1487 | 	  if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
1488 | 	    # If there is no dlopen support or we're linking statically,
1520 | 	dlopen=
1539 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
1579 | 	# This library was specified with -dlopen.
1580 | 	if test "$pass" = dlopen; then
1582 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
1585 | 	  if test -z "$dlname" || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
1586 | 	    # If there is no dlname, no dlopen support or we're linking
1593 | 	fi # $pass = dlopen
1638 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
1934 | 	      echo "*** as long as the dlopening application is linked with the -dlopen flag."
2038 |       if test "$pass" != dlopen; then
2106 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
2171 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
2680 | 	    echo "*** a static module, that should work as long as the dlopening"
2681 | 	    echo "*** application is linked with the -dlopen flag."
2699 | 	    echo "*** or is declared to -dlopen it."
2941 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
3113 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
3114 | 	   test "$dlopen_self_static" = unknown; then
3115 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
3931 | # The name that we can dlopen(3).
3951 | # Files to dlopen/dlpreopen
3952 | dlopen='$dlfiles'
4508 |     # Handle -dlopen flags immediately.
4537 | 	# Skip this library if it cannot be dlopened.
4562 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
4890 |   -dlopen FILE      add the directory containing FILE to the library path
4892 | This mode sets the library path environment variable according to \`-dlopen'
4941 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
4950 |   -module           build a library that can dlopened
{% endraw %}

```
### aclocal.m4

```

{% raw %}
884 | ifdef([AC_PROVIDE_AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
1348 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1351 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
1407 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1434 | ])# _LT_AC_TRY_DLOPEN_SELF
1436 | # AC_LIBTOOL_DLOPEN_SELF
1438 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1439 | [if test "x$enable_dlopen" != xyes; then
1440 |   enable_dlopen=unknown
1441 |   enable_dlopen_self=unknown
1442 |   enable_dlopen_self_static=unknown
1444 |   lt_cv_dlopen=no
1445 |   lt_cv_dlopen_libs=
1449 |     lt_cv_dlopen="load_add_on"
1450 |     lt_cv_dlopen_libs=
1451 |     lt_cv_dlopen_self=yes
1455 |     lt_cv_dlopen="LoadLibrary"
1456 |     lt_cv_dlopen_libs=
1461 |           [lt_cv_dlopen="shl_load"],
1463 |             [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
1464 | 	[AC_CHECK_FUNC([dlopen],
1465 | 	      [lt_cv_dlopen="dlopen"],
1466 | 	  [AC_CHECK_LIB([dl], [dlopen],
1467 | 	        [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1468 | 	    [AC_CHECK_LIB([svld], [dlopen],
1469 | 	          [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1471 | 	            [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
1480 |   if test "x$lt_cv_dlopen" != xno; then
1481 |     enable_dlopen=yes
1483 |     enable_dlopen=no
1486 |   case $lt_cv_dlopen in
1487 |   dlopen)
1496 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1498 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1499 | 	  lt_cv_dlopen_self, [dnl
1500 | 	  _LT_AC_TRY_DLOPEN_SELF(
1501 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1502 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1505 |     if test "x$lt_cv_dlopen_self" = xyes; then
1507 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1508 |     	  lt_cv_dlopen_self_static, [dnl
1509 | 	  _LT_AC_TRY_DLOPEN_SELF(
1510 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1511 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1521 |   case $lt_cv_dlopen_self in
1522 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1523 |   *) enable_dlopen_self=unknown ;;
1526 |   case $lt_cv_dlopen_self_static in
1527 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1528 |   *) enable_dlopen_self_static=unknown ;;
1531 | ])# AC_LIBTOOL_DLOPEN_SELF
3138 | AC_LIBTOOL_DLOPEN_SELF
3372 | # Whether dlopen is supported.
3373 | dlopen_support=$enable_dlopen
3375 | # Whether dlopen of programs is supported.
3376 | dlopen_self=$enable_dlopen_self
3378 | # Whether dlopen of statically linked programs is supported.
3379 | dlopen_self_static=$enable_dlopen_self_static
3387 | # Compiler flag to allow reflexive dlopens.
3735 | # AC_LIBTOOL_DLOPEN - enable checks for dlopen support
3736 | AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_BEFORE([$0],[AC_LIBTOOL_SETUP])])
{% endraw %}

```
### zlib/aclocal.m4

```

{% raw %}
608 | ifdef([AC_PROVIDE_AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
1072 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1075 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
1131 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1158 | ])# _LT_AC_TRY_DLOPEN_SELF
1160 | # AC_LIBTOOL_DLOPEN_SELF
1162 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1163 | [if test "x$enable_dlopen" != xyes; then
1164 |   enable_dlopen=unknown
1165 |   enable_dlopen_self=unknown
1166 |   enable_dlopen_self_static=unknown
1168 |   lt_cv_dlopen=no
1169 |   lt_cv_dlopen_libs=
1173 |     lt_cv_dlopen="load_add_on"
1174 |     lt_cv_dlopen_libs=
1175 |     lt_cv_dlopen_self=yes
1179 |     lt_cv_dlopen="LoadLibrary"
1180 |     lt_cv_dlopen_libs=
1185 |           [lt_cv_dlopen="shl_load"],
1187 |             [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
1188 | 	[AC_CHECK_FUNC([dlopen],
1189 | 	      [lt_cv_dlopen="dlopen"],
1190 | 	  [AC_CHECK_LIB([dl], [dlopen],
1191 | 	        [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1192 | 	    [AC_CHECK_LIB([svld], [dlopen],
1193 | 	          [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1195 | 	            [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
1204 |   if test "x$lt_cv_dlopen" != xno; then
1205 |     enable_dlopen=yes
1207 |     enable_dlopen=no
1210 |   case $lt_cv_dlopen in
1211 |   dlopen)
1220 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1222 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1223 | 	  lt_cv_dlopen_self, [dnl
1224 | 	  _LT_AC_TRY_DLOPEN_SELF(
1225 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1226 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1229 |     if test "x$lt_cv_dlopen_self" = xyes; then
1231 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1232 |     	  lt_cv_dlopen_self_static, [dnl
1233 | 	  _LT_AC_TRY_DLOPEN_SELF(
1234 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1235 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1245 |   case $lt_cv_dlopen_self in
1246 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1247 |   *) enable_dlopen_self=unknown ;;
1250 |   case $lt_cv_dlopen_self_static in
1251 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1252 |   *) enable_dlopen_self_static=unknown ;;
1255 | ])# AC_LIBTOOL_DLOPEN_SELF
2862 | AC_LIBTOOL_DLOPEN_SELF
3096 | # Whether dlopen is supported.
3097 | dlopen_support=$enable_dlopen
3099 | # Whether dlopen of programs is supported.
3100 | dlopen_self=$enable_dlopen_self
3102 | # Whether dlopen of statically linked programs is supported.
3103 | dlopen_self_static=$enable_dlopen_self_static
3111 | # Compiler flag to allow reflexive dlopens.
3459 | # AC_LIBTOOL_DLOPEN - enable checks for dlopen support
3460 | AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_BEFORE([$0],[AC_LIBTOOL_SETUP])])
{% endraw %}

```