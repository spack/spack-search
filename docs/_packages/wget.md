---
name: "wget"
layout: package
next_package: node-js
previous_package: libestr
languages: ['bash']
---
## 1.19.1
3 / 1089 files match

 - [configure.ac](#configureac)
 - [m4/lib-link.m4](#m4lib-linkm4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)

### configure.ac

```

{% raw %}
354 |     dnl dlopen(), but HP-UX uses shl_load().
355 |     AC_CHECK_LIB(dl, dlopen, [], [
{% endraw %}

```
### m4/lib-link.m4

```

{% raw %}
518 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### build-aux/ltmain.sh

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