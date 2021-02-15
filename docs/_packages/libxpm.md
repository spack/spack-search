---
name: "libxpm"
layout: package
next_package: freetype
previous_package: healpix-cxx
languages: ['bash']
---
## 3.5.7
2 / 63 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

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
### aclocal.m4

```

{% raw %}
1583 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
2198 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
2201 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
2257 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
2286 | ])# _LT_AC_TRY_DLOPEN_SELF
2289 | # AC_LIBTOOL_DLOPEN_SELF
2291 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
2293 | if test "x$enable_dlopen" != xyes; then
2294 |   enable_dlopen=unknown
2295 |   enable_dlopen_self=unknown
2296 |   enable_dlopen_self_static=unknown
2298 |   lt_cv_dlopen=no
2299 |   lt_cv_dlopen_libs=
2303 |     lt_cv_dlopen="load_add_on"
2304 |     lt_cv_dlopen_libs=
2305 |     lt_cv_dlopen_self=yes
2309 |     lt_cv_dlopen="LoadLibrary"
2310 |     lt_cv_dlopen_libs=
2314 |     lt_cv_dlopen="dlopen"
2315 |     lt_cv_dlopen_libs=
2320 |     AC_CHECK_LIB([dl], [dlopen],
2321 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
2322 |     lt_cv_dlopen="dyld"
2323 |     lt_cv_dlopen_libs=
2324 |     lt_cv_dlopen_self=yes
2330 | 	  [lt_cv_dlopen="shl_load"],
2332 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
2333 | 	[AC_CHECK_FUNC([dlopen],
2334 | 	      [lt_cv_dlopen="dlopen"],
2335 | 	  [AC_CHECK_LIB([dl], [dlopen],
2336 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2337 | 	    [AC_CHECK_LIB([svld], [dlopen],
2338 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2340 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
2349 |   if test "x$lt_cv_dlopen" != xno; then
2350 |     enable_dlopen=yes
2352 |     enable_dlopen=no
2355 |   case $lt_cv_dlopen in
2356 |   dlopen)
2364 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2366 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2367 | 	  lt_cv_dlopen_self, [dnl
2368 | 	  _LT_AC_TRY_DLOPEN_SELF(
2369 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2370 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2373 |     if test "x$lt_cv_dlopen_self" = xyes; then
2375 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2376 |     	  lt_cv_dlopen_self_static, [dnl
2377 | 	  _LT_AC_TRY_DLOPEN_SELF(
2378 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2379 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2389 |   case $lt_cv_dlopen_self in
2390 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2391 |   *) enable_dlopen_self=unknown ;;
2394 |   case $lt_cv_dlopen_self_static in
2395 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2396 |   *) enable_dlopen_self_static=unknown ;;
2399 | ])# AC_LIBTOOL_DLOPEN_SELF
3272 | # AC_LIBTOOL_DLOPEN
3274 | # enable checks for dlopen support
3275 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
3277 | ])# AC_LIBTOOL_DLOPEN
4065 | AC_LIBTOOL_DLOPEN_SELF
5736 | # Whether dlopen is supported.
5737 | dlopen_support=$enable_dlopen
5739 | # Whether dlopen of programs is supported.
5740 | dlopen_self=$enable_dlopen_self
5742 | # Whether dlopen of statically linked programs is supported.
5743 | dlopen_self_static=$enable_dlopen_self_static
5751 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```