---
name: "py-uvloop"
layout: package
next_package: ocl-icd
previous_package: environment-modules
languages: ['cpp', 'bash']
---
## 0.14.0
15 / 449 files match

 - [vendor/libuv/configure.ac](#vendorlibuvconfigureac)
 - [vendor/libuv/ltmain.sh](#vendorlibuvltmainsh)
 - [vendor/libuv/src/win/dl.c](#vendorlibuvsrcwindlc)
 - [vendor/libuv/src/unix/darwin-proctitle.c](#vendorlibuvsrcunixdarwin-proctitlec)
 - [vendor/libuv/src/unix/fsevents.c](#vendorlibuvsrcunixfseventsc)
 - [vendor/libuv/src/unix/dl.c](#vendorlibuvsrcunixdlc)
 - [vendor/libuv/include/uv.h](#vendorlibuvincludeuvh)
 - [vendor/libuv/include/uv/win.h](#vendorlibuvincludeuvwinh)
 - [vendor/libuv/include/uv/unix.h](#vendorlibuvincludeuvunixh)
 - [vendor/libuv/autom4te.cache/output.0](#vendorlibuvautom4tecacheoutput0)
 - [vendor/libuv/autom4te.cache/output.1](#vendorlibuvautom4tecacheoutput1)
 - [vendor/libuv/autom4te.cache/traces.0](#vendorlibuvautom4tecachetraces0)
 - [vendor/libuv/m4/libtool.m4](#vendorlibuvm4libtoolm4)
 - [vendor/libuv/m4/ltoptions.m4](#vendorlibuvm4ltoptionsm4)
 - [vendor/libuv/test/test-dlerror.c](#vendorlibuvtesttest-dlerrorc)

### vendor/libuv/configure.ac

```

{% raw %}
44 | AC_CHECK_LIB([dl], [dlopen])
{% endraw %}

```
### vendor/libuv/ltmain.sh

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
6155 |       if test "$pass" = dlopen; then
6374 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6375 | 	      # If there is no dlopen support or we're linking statically,
6405 | 	dlopen=
6435 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6481 | 	# This library was specified with -dlopen.
6482 | 	if test "$pass" = dlopen; then
6484 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6487 | 	     test "$dlopen_support" != yes ||
6489 | 	    # If there is no dlname, no dlopen support or we're linking
6498 | 	fi # $pass = dlopen
6554 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6556 | 	      # We recover the dlopen module name by 'saving' the la file
6580 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6709 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6710 | 	  dlopenmodule=""
6713 | 	      dlopenmodule="$dlpremoduletest"
6717 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6814 | 		    # if the lib is a (non-dlopened) module then we can not
6818 | 		      if test "X$dlopenmodule" != "X$lib"; then
6970 | 	      echo "*** a static module, that should work as long as the dlopening application"
6971 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7115 |       if test "$pass" != dlopen; then
7214 | 	func_warning "\`-dlopen' is ignored for archives"
7281 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7960 | 	    echo "*** a static module, that should work as long as the dlopening"
7961 | 	    echo "*** application is linked with the -dlopen flag."
7979 | 	    echo "*** or is declared to -dlopen it."
8590 | 	func_warning "\`-dlopen' is ignored for objects"
8708 |         && test "$dlopen_support" = unknown \
8709 | 	&& test "$dlopen_self" = unknown \
8710 | 	&& test "$dlopen_self_static" = unknown && \
8711 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9392 | # The name that we can dlopen(3).
9421 | # Files to dlopen/dlpreopen
9422 | dlopen='$dlfiles'
{% endraw %}

```
### vendor/libuv/src/win/dl.c

```cpp

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### vendor/libuv/src/unix/darwin-proctitle.c

```cpp

{% raw %}
82 |   application_services_handle = dlopen("/System/Library/Frameworks/"
86 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### vendor/libuv/src/unix/fsevents.c

```cpp

{% raw %}
536 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
543 |   core_services_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### vendor/libuv/src/unix/dl.c

```cpp

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### vendor/libuv/include/uv.h

```cpp

{% raw %}
1646 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```
### vendor/libuv/include/uv/win.h

```cpp

{% raw %}
317 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### vendor/libuv/include/uv/unix.h

```cpp

{% raw %}
212 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### vendor/libuv/autom4te.cache/output.0

```

{% raw %}
8242 |         enable_dlopen=no
11555 |   if test "x$enable_dlopen" != xyes; then
11556 |   enable_dlopen=unknown
11557 |   enable_dlopen_self=unknown
11558 |   enable_dlopen_self_static=unknown
11560 |   lt_cv_dlopen=no
11561 |   lt_cv_dlopen_libs=
11565 |     lt_cv_dlopen="load_add_on"
11566 |     lt_cv_dlopen_libs=
11567 |     lt_cv_dlopen_self=yes
11571 |     lt_cv_dlopen="LoadLibrary"
11572 |     lt_cv_dlopen_libs=
11576 |     lt_cv_dlopen="dlopen"
11577 |     lt_cv_dlopen_libs=
11582 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11583 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11584 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11598 | char dlopen ();
11602 | return dlopen ();
11608 |   ac_cv_lib_dl_dlopen=yes
11610 |   ac_cv_lib_dl_dlopen=no
11616 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11617 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11618 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11619 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11622 |     lt_cv_dlopen="dyld"
11623 |     lt_cv_dlopen_libs=
11624 |     lt_cv_dlopen_self=yes
11633 |   lt_cv_dlopen="shl_load"
11672 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
11674 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
11675 | if test "x$ac_cv_func_dlopen" = xyes; then :
11676 |   lt_cv_dlopen="dlopen"
11678 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11679 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11680 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11694 | char dlopen ();
11698 | return dlopen ();
11704 |   ac_cv_lib_dl_dlopen=yes
11706 |   ac_cv_lib_dl_dlopen=no
11712 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11713 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11714 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11715 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11717 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
11718 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11719 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11733 | char dlopen ();
11737 | return dlopen ();
11743 |   ac_cv_lib_svld_dlopen=yes
11745 |   ac_cv_lib_svld_dlopen=no
11751 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11752 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11753 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11754 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
11793 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
11814 |   if test "x$lt_cv_dlopen" != xno; then
11815 |     enable_dlopen=yes
11817 |     enable_dlopen=no
11820 |   case $lt_cv_dlopen in
11821 |   dlopen)
11829 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11831 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11832 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11833 | if ${lt_cv_dlopen_self+:} false; then :
11837 |   lt_cv_dlopen_self=cross
11892 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11919 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
11920 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
11921 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
11925 |     lt_cv_dlopen_self=no
11932 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
11933 | $as_echo "$lt_cv_dlopen_self" >&6; }
11935 |     if test "x$lt_cv_dlopen_self" = xyes; then
11937 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
11938 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
11939 | if ${lt_cv_dlopen_self_static+:} false; then :
11943 |   lt_cv_dlopen_self_static=cross
11998 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12025 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12026 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12027 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12031 |     lt_cv_dlopen_self_static=no
12038 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
12039 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12048 |   case $lt_cv_dlopen_self in
12049 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12050 |   *) enable_dlopen_self=unknown ;;
12053 |   case $lt_cv_dlopen_self_static in
12054 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12055 |   *) enable_dlopen_self_static=unknown ;;
12228 | { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12229 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12230 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12244 | char dlopen ();
12248 | return dlopen ();
12254 |   ac_cv_lib_dl_dlopen=yes
12256 |   ac_cv_lib_dl_dlopen=no
12262 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12263 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12264 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
13977 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
13978 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
13979 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
14982 | # Whether dlopen is supported.
14983 | dlopen_support=$enable_dlopen
14985 | # Whether dlopen of programs is supported.
14986 | dlopen_self=$enable_dlopen_self
14988 | # Whether dlopen of statically linked programs is supported.
14989 | dlopen_self_static=$enable_dlopen_self_static
15033 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### vendor/libuv/autom4te.cache/output.1

```

{% raw %}
8242 |         enable_dlopen=no
11555 |   if test "x$enable_dlopen" != xyes; then
11556 |   enable_dlopen=unknown
11557 |   enable_dlopen_self=unknown
11558 |   enable_dlopen_self_static=unknown
11560 |   lt_cv_dlopen=no
11561 |   lt_cv_dlopen_libs=
11565 |     lt_cv_dlopen="load_add_on"
11566 |     lt_cv_dlopen_libs=
11567 |     lt_cv_dlopen_self=yes
11571 |     lt_cv_dlopen="LoadLibrary"
11572 |     lt_cv_dlopen_libs=
11576 |     lt_cv_dlopen="dlopen"
11577 |     lt_cv_dlopen_libs=
11582 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11583 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11584 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11598 | char dlopen ();
11602 | return dlopen ();
11608 |   ac_cv_lib_dl_dlopen=yes
11610 |   ac_cv_lib_dl_dlopen=no
11616 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11617 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11618 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11619 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11622 |     lt_cv_dlopen="dyld"
11623 |     lt_cv_dlopen_libs=
11624 |     lt_cv_dlopen_self=yes
11633 |   lt_cv_dlopen="shl_load"
11672 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
11674 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
11675 | if test "x$ac_cv_func_dlopen" = xyes; then :
11676 |   lt_cv_dlopen="dlopen"
11678 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11679 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11680 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11694 | char dlopen ();
11698 | return dlopen ();
11704 |   ac_cv_lib_dl_dlopen=yes
11706 |   ac_cv_lib_dl_dlopen=no
11712 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11713 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11714 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11715 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11717 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
11718 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11719 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11733 | char dlopen ();
11737 | return dlopen ();
11743 |   ac_cv_lib_svld_dlopen=yes
11745 |   ac_cv_lib_svld_dlopen=no
11751 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11752 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11753 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11754 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
11793 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
11814 |   if test "x$lt_cv_dlopen" != xno; then
11815 |     enable_dlopen=yes
11817 |     enable_dlopen=no
11820 |   case $lt_cv_dlopen in
11821 |   dlopen)
11829 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11831 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11832 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11833 | if ${lt_cv_dlopen_self+:} false; then :
11837 |   lt_cv_dlopen_self=cross
11892 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11919 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
11920 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
11921 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
11925 |     lt_cv_dlopen_self=no
11932 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
11933 | $as_echo "$lt_cv_dlopen_self" >&6; }
11935 |     if test "x$lt_cv_dlopen_self" = xyes; then
11937 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
11938 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
11939 | if ${lt_cv_dlopen_self_static+:} false; then :
11943 |   lt_cv_dlopen_self_static=cross
11998 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12025 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12026 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12027 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12031 |     lt_cv_dlopen_self_static=no
12038 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
12039 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12048 |   case $lt_cv_dlopen_self in
12049 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12050 |   *) enable_dlopen_self=unknown ;;
12053 |   case $lt_cv_dlopen_self_static in
12054 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12055 |   *) enable_dlopen_self_static=unknown ;;
12228 | { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
12229 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12230 | if ${ac_cv_lib_dl_dlopen+:} false; then :
12244 | char dlopen ();
12248 | return dlopen ();
12254 |   ac_cv_lib_dl_dlopen=yes
12256 |   ac_cv_lib_dl_dlopen=no
12262 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
12263 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12264 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
13977 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
13978 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
13979 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
14982 | # Whether dlopen is supported.
14983 | dlopen_support=$enable_dlopen
14985 | # Whether dlopen of programs is supported.
14986 | dlopen_self=$enable_dlopen_self
14988 | # Whether dlopen of statically linked programs is supported.
14989 | dlopen_self_static=$enable_dlopen_self_static
15033 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### vendor/libuv/autom4te.cache/traces.0

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
1814 | m4trace:m4/libtool.m4:1858: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
1815 | if test "x$enable_dlopen" != xyes; then
1816 |   enable_dlopen=unknown
1817 |   enable_dlopen_self=unknown
1818 |   enable_dlopen_self_static=unknown
1820 |   lt_cv_dlopen=no
1821 |   lt_cv_dlopen_libs=
1825 |     lt_cv_dlopen="load_add_on"
1826 |     lt_cv_dlopen_libs=
1827 |     lt_cv_dlopen_self=yes
1831 |     lt_cv_dlopen="LoadLibrary"
1832 |     lt_cv_dlopen_libs=
1836 |     lt_cv_dlopen="dlopen"
1837 |     lt_cv_dlopen_libs=
1842 |     AC_CHECK_LIB([dl], [dlopen],
1843 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1844 |     lt_cv_dlopen="dyld"
1845 |     lt_cv_dlopen_libs=
1846 |     lt_cv_dlopen_self=yes
1852 | 	  [lt_cv_dlopen="shl_load"],
1854 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1855 | 	[AC_CHECK_FUNC([dlopen],
1856 | 	      [lt_cv_dlopen="dlopen"],
1857 | 	  [AC_CHECK_LIB([dl], [dlopen],
1858 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1859 | 	    [AC_CHECK_LIB([svld], [dlopen],
1860 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1862 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1871 |   if test "x$lt_cv_dlopen" != xno; then
1872 |     enable_dlopen=yes
1874 |     enable_dlopen=no
1877 |   case $lt_cv_dlopen in
1878 |   dlopen)
1886 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1888 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1889 | 	  lt_cv_dlopen_self, [dnl
1890 | 	  _LT_TRY_DLOPEN_SELF(
1891 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1892 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1895 |     if test "x$lt_cv_dlopen_self" = xyes; then
1897 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1898 | 	  lt_cv_dlopen_self_static, [dnl
1899 | 	  _LT_TRY_DLOPEN_SELF(
1900 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1901 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1911 |   case $lt_cv_dlopen_self in
1912 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1913 |   *) enable_dlopen_self=unknown ;;
1916 |   case $lt_cv_dlopen_self_static in
1917 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1918 |   *) enable_dlopen_self_static=unknown ;;
1921 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1922 | 	 [Whether dlopen is supported])
1923 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1924 | 	 [Whether dlopen of programs is supported])
1925 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1926 | 	 [Whether dlopen of statically linked programs is supported])
1928 | m4trace:m4/libtool.m4:1975: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1929 | m4trace:m4/libtool.m4:1975: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
1931 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2227 | m4trace:m4/ltoptions.m4:111: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2230 | put the `dlopen' option into LT_INIT's first parameter.])
2232 | m4trace:m4/ltoptions.m4:111: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2234 | _LT_SET_OPTION([LT_INIT], [dlopen])
2237 | put the `dlopen' option into LT_INIT's first parameter.])
2329 | m4trace:m4/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2902 | m4trace:configure.ac:41: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### vendor/libuv/m4/libtool.m4

```

{% raw %}
1758 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1761 | m4_defun([_LT_TRY_DLOPEN_SELF],
1819 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1852 | ])# _LT_TRY_DLOPEN_SELF
1855 | # LT_SYS_DLOPEN_SELF
1857 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1859 | if test "x$enable_dlopen" != xyes; then
1860 |   enable_dlopen=unknown
1861 |   enable_dlopen_self=unknown
1862 |   enable_dlopen_self_static=unknown
1864 |   lt_cv_dlopen=no
1865 |   lt_cv_dlopen_libs=
1869 |     lt_cv_dlopen="load_add_on"
1870 |     lt_cv_dlopen_libs=
1871 |     lt_cv_dlopen_self=yes
1875 |     lt_cv_dlopen="LoadLibrary"
1876 |     lt_cv_dlopen_libs=
1880 |     lt_cv_dlopen="dlopen"
1881 |     lt_cv_dlopen_libs=
1886 |     AC_CHECK_LIB([dl], [dlopen],
1887 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1888 |     lt_cv_dlopen="dyld"
1889 |     lt_cv_dlopen_libs=
1890 |     lt_cv_dlopen_self=yes
1896 | 	  [lt_cv_dlopen="shl_load"],
1898 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1899 | 	[AC_CHECK_FUNC([dlopen],
1900 | 	      [lt_cv_dlopen="dlopen"],
1901 | 	  [AC_CHECK_LIB([dl], [dlopen],
1902 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1903 | 	    [AC_CHECK_LIB([svld], [dlopen],
1904 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1906 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1915 |   if test "x$lt_cv_dlopen" != xno; then
1916 |     enable_dlopen=yes
1918 |     enable_dlopen=no
1921 |   case $lt_cv_dlopen in
1922 |   dlopen)
1930 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1932 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1933 | 	  lt_cv_dlopen_self, [dnl
1934 | 	  _LT_TRY_DLOPEN_SELF(
1935 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1936 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1939 |     if test "x$lt_cv_dlopen_self" = xyes; then
1941 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1942 | 	  lt_cv_dlopen_self_static, [dnl
1943 | 	  _LT_TRY_DLOPEN_SELF(
1944 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1945 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1955 |   case $lt_cv_dlopen_self in
1956 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1957 |   *) enable_dlopen_self=unknown ;;
1960 |   case $lt_cv_dlopen_self_static in
1961 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1962 |   *) enable_dlopen_self_static=unknown ;;
1965 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1966 | 	 [Whether dlopen is supported])
1967 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1968 | 	 [Whether dlopen of programs is supported])
1969 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1970 | 	 [Whether dlopen of statically linked programs is supported])
1971 | ])# LT_SYS_DLOPEN_SELF
1974 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1976 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5676 |     [Compiler flag to allow reflexive dlopens])
5789 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### vendor/libuv/m4/ltoptions.m4

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
### vendor/libuv/test/test-dlerror.c

```cpp

{% raw %}
39 |   r = uv_dlopen(path, &lib);
{% endraw %}

```