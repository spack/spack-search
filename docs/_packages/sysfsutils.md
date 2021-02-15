---
name: "sysfsutils"
layout: package
next_package: yoda
previous_package: openfst
languages: ['bash']
---
## 0_5
2 / 38 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
185 |   -dlopen)
186 |     prevopt="-dlopen"
256 |   # Only execute mode is allowed to have -dlopen flags.
258 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
798 | 	    dlopen_self=$dlopen_self_static
802 | 	    dlopen_self=$dlopen_self_static
858 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
970 |       -dlopen)
1219 | 	  # This file was specified with -dlopen.
1220 | 	  if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1253 | 	  # This library was specified with -dlopen.
1384 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1396 | 	passes="conv scan dlopen dlpreopen link"
1405 | 	dlopen)
1521 | 	  if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
1522 | 	    # If there is no dlopen support or we're linking statically,
1554 | 	dlopen=
1573 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
1615 | 	# This library was specified with -dlopen.
1616 | 	if test "$pass" = dlopen; then
1618 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
1621 | 	  if test -z "$dlname" || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
1622 | 	    # If there is no dlname, no dlopen support or we're linking
1629 | 	fi # $pass = dlopen
1674 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
1990 | 	      echo "*** as long as the dlopening application is linked with the -dlopen flag."
2096 |       if test "$pass" != dlopen; then
2164 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
2229 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
2731 | 	    echo "*** a static module, that should work as long as the dlopening"
2732 | 	    echo "*** application is linked with the -dlopen flag."
2750 | 	    echo "*** or is declared to -dlopen it."
2992 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
3164 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
3165 | 	   test "$dlopen_self_static" = unknown; then
3166 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
3982 | # The name that we can dlopen(3).
4002 | # Files to dlopen/dlpreopen
4003 | dlopen='$dlfiles'
4577 |     # Handle -dlopen flags immediately.
4606 | 	# Skip this library if it cannot be dlopened.
4631 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
4945 |   -dlopen FILE      add the directory containing FILE to the library path
4947 | This mode sets the library path environment variable according to \`-dlopen'
4996 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
5005 |   -module           build a library that can dlopened
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