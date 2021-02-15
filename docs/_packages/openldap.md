---
name: "openldap"
layout: package
next_package: stat
previous_package: fast-global-file-status
languages: ['cpp', 'bash']
---
## 2.4.48
9 / 1488 files match

 - [configure.in](#configurein)
 - [aclocal.m4](#aclocalm4)
 - [build/ltmain.sh](#buildltmainsh)
 - [servers/slapd/module.c](#serversslapdmodulec)
 - [servers/slapd/slapi/plugin.c](#serversslapdslapipluginc)
 - [servers/slapd/overlays/ppolicy.c](#serversslapdoverlaysppolicyc)
 - [contrib/ldapc++/ltmain.sh](#contribldapc++ltmainsh)
 - [contrib/ldapc++/aclocal.m4](#contribldapc++aclocalm4)
 - [doc/guide/admin/aspell.en.pws](#docguideadminaspellenpws)

### configure.in

```

{% raw %}
672 | AC_LIBTOOL_DLOPEN
2613 | 	SLAPD_MODULES_LDFLAGS="-dlopen self"
3074 | dnl For Windows build, we don't want to include -dlopen flags.
{% endraw %}

```
### aclocal.m4

```

{% raw %}
682 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
1261 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1264 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
1320 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1347 | ])# _LT_AC_TRY_DLOPEN_SELF
1350 | # AC_LIBTOOL_DLOPEN_SELF
1352 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1354 | if test "x$enable_dlopen" != xyes; then
1355 |   enable_dlopen=unknown
1356 |   enable_dlopen_self=unknown
1357 |   enable_dlopen_self_static=unknown
1359 |   lt_cv_dlopen=no
1360 |   lt_cv_dlopen_libs=
1364 |     lt_cv_dlopen="load_add_on"
1365 |     lt_cv_dlopen_libs=
1366 |     lt_cv_dlopen_self=yes
1370 |     lt_cv_dlopen="LoadLibrary"
1371 |     lt_cv_dlopen_libs=
1375 |     lt_cv_dlopen="dlopen"
1376 |     lt_cv_dlopen_libs=
1381 |     AC_CHECK_LIB([dl], [dlopen],
1382 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1383 |     lt_cv_dlopen="dyld"
1384 |     lt_cv_dlopen_libs=
1385 |     lt_cv_dlopen_self=yes
1391 | 	  [lt_cv_dlopen="shl_load"],
1393 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
1394 | 	[AC_CHECK_FUNC([dlopen],
1395 | 	      [lt_cv_dlopen="dlopen"],
1396 | 	  [AC_CHECK_LIB([dl], [dlopen],
1397 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1398 | 	    [AC_CHECK_LIB([svld], [dlopen],
1399 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1401 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
1410 |   if test "x$lt_cv_dlopen" != xno; then
1411 |     enable_dlopen=yes
1413 |     enable_dlopen=no
1416 |   case $lt_cv_dlopen in
1417 |   dlopen)
1425 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1427 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1428 | 	  lt_cv_dlopen_self, [dnl
1429 | 	  _LT_AC_TRY_DLOPEN_SELF(
1430 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1431 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1434 |     if test "x$lt_cv_dlopen_self" = xyes; then
1436 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1437 |     	  lt_cv_dlopen_self_static, [dnl
1438 | 	  _LT_AC_TRY_DLOPEN_SELF(
1439 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1440 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1450 |   case $lt_cv_dlopen_self in
1451 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1452 |   *) enable_dlopen_self=unknown ;;
1455 |   case $lt_cv_dlopen_self_static in
1456 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1457 |   *) enable_dlopen_self_static=unknown ;;
1460 | ])# AC_LIBTOOL_DLOPEN_SELF
2291 | # AC_LIBTOOL_DLOPEN
2293 | # enable checks for dlopen support
2294 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2296 | ])# AC_LIBTOOL_DLOPEN
3104 | AC_LIBTOOL_DLOPEN_SELF($1)
4073 | AC_LIBTOOL_DLOPEN_SELF($1)
4396 | AC_LIBTOOL_DLOPEN_SELF($1)
4712 | # Whether dlopen is supported.
4713 | dlopen_support=$enable_dlopen
4715 | # Whether dlopen of programs is supported.
4716 | dlopen_self=$enable_dlopen_self
4718 | # Whether dlopen of statically linked programs is supported.
4719 | dlopen_self_static=$enable_dlopen_self_static
4727 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### build/ltmain.sh

```bash

{% raw %}
566 |   -dlopen)
567 |     prevopt="-dlopen"
651 |   # Only execute mode is allowed to have -dlopen flags.
653 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1190 | 	    dlopen_self=$dlopen_self_static
1195 | 	    dlopen_self=$dlopen_self_static
1251 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1343 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1500 |       -dlopen)
1888 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1961 | 	  # This library was specified with -dlopen.
2102 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2114 | 	passes="conv scan dlopen dlpreopen link"
2127 | 	dlopen) libs="$dlfiles" ;;
2132 |       if test "$pass" = dlopen; then
2334 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2335 | 	      # If there is no dlopen support or we're linking statically,
2368 | 	dlopen=
2389 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2432 | 	# This library was specified with -dlopen.
2433 | 	if test "$pass" = dlopen; then
2435 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2439 | 	     test "$dlopen_support" != yes ||
2441 | 	    # If there is no dlname, no dlopen support or we're linking
2450 | 	fi # $pass = dlopen
2503 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2878 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2879 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
3030 |       if test "$pass" != dlopen; then
3131 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3198 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3836 | 	    $echo "*** a static module, that should work as long as the dlopening"
3837 | 	    $echo "*** application is linked with the -dlopen flag."
3855 | 	    $echo "*** or is declared to -dlopen it."
4265 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4397 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4398 | 	   test "$dlopen_self_static" = unknown; then
4399 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5740 | # The name that we can dlopen(3).
5763 | # Files to dlopen/dlpreopen
5764 | dlopen='$dlfiles'
6379 |     # Handle -dlopen flags immediately.
6408 | 	# Skip this library if it cannot be dlopened.
6433 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6793 |   -dlopen FILE      add the directory containing FILE to the library path
6795 | This mode sets the library path environment variable according to \`-dlopen'
6844 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6853 |   -module           build a library that can dlopened
{% endraw %}

```
### servers/slapd/module.c

```cpp

{% raw %}
182 | 	if ((module->lib = lt_dlopenext(file)) == NULL) {
189 | 		Debug(LDAP_DEBUG_ANY, "lt_dlopenext failed: (%s) %s\n", file_name,
{% endraw %}

```
### servers/slapd/slapi/plugin.c

```cpp

{% raw %}
527 |  *                     pLdHandle - handle returned by lt_dlopen()
553 | 	*pLdHandle = lt_dlopen( path );
{% endraw %}

```
### servers/slapd/overlays/ppolicy.c

```cpp

{% raw %}
684 | 		if ((mod = lt_dlopen( pp->pwdCheckModule )) == NULL) {
688 | 			"check_password_quality: lt_dlopen failed: (%s) %s.\n",
{% endraw %}

```
### contrib/ldapc++/ltmain.sh

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
2087 |       if test "$pass" = dlopen; then
2266 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2267 | 	      # If there is no dlopen support or we're linking statically,
2300 | 	dlopen=
2321 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2364 | 	# This library was specified with -dlopen.
2365 | 	if test "$pass" = dlopen; then
2367 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2371 | 	     test "$dlopen_support" != yes ||
2373 | 	    # If there is no dlname, no dlopen support or we're linking
2382 | 	fi # $pass = dlopen
2435 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2810 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2811 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2962 |       if test "$pass" != dlopen; then
3063 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3130 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3768 | 	    $echo "*** a static module, that should work as long as the dlopening"
3769 | 	    $echo "*** application is linked with the -dlopen flag."
3787 | 	    $echo "*** or is declared to -dlopen it."
4197 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4329 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4330 | 	   test "$dlopen_self_static" = unknown; then
4331 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5669 | # The name that we can dlopen(3).
5692 | # Files to dlopen/dlpreopen
5693 | dlopen='$dlfiles'
6308 |     # Handle -dlopen flags immediately.
6337 | 	# Skip this library if it cannot be dlopened.
6362 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6722 |   -dlopen FILE      add the directory containing FILE to the library path
6724 | This mode sets the library path environment variable according to \`-dlopen'
6773 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6782 |   -module           build a library that can dlopened
{% endraw %}

```
### contrib/ldapc++/aclocal.m4

```

{% raw %}
214 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
925 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
928 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
984 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1013 | ])# _LT_AC_TRY_DLOPEN_SELF
1016 | # AC_LIBTOOL_DLOPEN_SELF
1018 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1020 | if test "x$enable_dlopen" != xyes; then
1021 |   enable_dlopen=unknown
1022 |   enable_dlopen_self=unknown
1023 |   enable_dlopen_self_static=unknown
1025 |   lt_cv_dlopen=no
1026 |   lt_cv_dlopen_libs=
1030 |     lt_cv_dlopen="load_add_on"
1031 |     lt_cv_dlopen_libs=
1032 |     lt_cv_dlopen_self=yes
1036 |     lt_cv_dlopen="LoadLibrary"
1037 |     lt_cv_dlopen_libs=
1041 |     lt_cv_dlopen="dlopen"
1042 |     lt_cv_dlopen_libs=
1047 |     AC_CHECK_LIB([dl], [dlopen],
1048 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1049 |     lt_cv_dlopen="dyld"
1050 |     lt_cv_dlopen_libs=
1051 |     lt_cv_dlopen_self=yes
1057 | 	  [lt_cv_dlopen="shl_load"],
1059 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1060 | 	[AC_CHECK_FUNC([dlopen],
1061 | 	      [lt_cv_dlopen="dlopen"],
1062 | 	  [AC_CHECK_LIB([dl], [dlopen],
1063 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1064 | 	    [AC_CHECK_LIB([svld], [dlopen],
1065 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1067 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1076 |   if test "x$lt_cv_dlopen" != xno; then
1077 |     enable_dlopen=yes
1079 |     enable_dlopen=no
1082 |   case $lt_cv_dlopen in
1083 |   dlopen)
1091 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1093 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1094 | 	  lt_cv_dlopen_self, [dnl
1095 | 	  _LT_AC_TRY_DLOPEN_SELF(
1096 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1097 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1100 |     if test "x$lt_cv_dlopen_self" = xyes; then
1102 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1103 |     	  lt_cv_dlopen_self_static, [dnl
1104 | 	  _LT_AC_TRY_DLOPEN_SELF(
1105 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1106 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1116 |   case $lt_cv_dlopen_self in
1117 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1118 |   *) enable_dlopen_self=unknown ;;
1121 |   case $lt_cv_dlopen_self_static in
1122 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1123 |   *) enable_dlopen_self_static=unknown ;;
1126 | ])# AC_LIBTOOL_DLOPEN_SELF
2036 | # AC_LIBTOOL_DLOPEN
2038 | # enable checks for dlopen support
2039 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2041 | ])# AC_LIBTOOL_DLOPEN
2839 | AC_LIBTOOL_DLOPEN_SELF
4556 | # Whether dlopen is supported.
4557 | dlopen_support=$enable_dlopen
4559 | # Whether dlopen of programs is supported.
4560 | dlopen_self=$enable_dlopen_self
4562 | # Whether dlopen of statically linked programs is supported.
4563 | dlopen_self_static=$enable_dlopen_self_static
4571 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### doc/guide/admin/aspell.en.pws

```

{% raw %}
90 | dlopen
{% endraw %}

```