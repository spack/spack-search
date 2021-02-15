---
name: "steps"
layout: package
next_package: nginx
previous_package: judy
languages: ['bash']
---
## develop
2 / 1497 files match

 - [src/third_party/cvode-2.6.0/config/ltmain.sh](#srcthird_partycvode-260configltmainsh)
 - [test/ci/valgrind/mkl.supp](#testcivalgrindmklsupp)

### src/third_party/cvode-2.6.0/config/ltmain.sh

```bash

{% raw %}
527 |   -dlopen)
528 |     prevopt="-dlopen"
612 |   # Only execute mode is allowed to have -dlopen flags.
614 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1151 | 	    dlopen_self=$dlopen_self_static
1156 | 	    dlopen_self=$dlopen_self_static
1212 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1304 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1461 |       -dlopen)
1848 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1921 | 	  # This library was specified with -dlopen.
2062 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2074 | 	passes="conv scan dlopen dlpreopen link"
2087 | 	dlopen) libs="$dlfiles" ;;
2092 |       if test "$pass" = dlopen; then
2271 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2272 | 	      # If there is no dlopen support or we're linking statically,
2305 | 	dlopen=
2326 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2369 | 	# This library was specified with -dlopen.
2370 | 	if test "$pass" = dlopen; then
2372 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2376 | 	     test "$dlopen_support" != yes ||
2378 | 	    # If there is no dlname, no dlopen support or we're linking
2387 | 	fi # $pass = dlopen
2440 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2815 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2816 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2967 |       if test "$pass" != dlopen; then
3068 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3135 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3773 | 	    $echo "*** a static module, that should work as long as the dlopening"
3774 | 	    $echo "*** application is linked with the -dlopen flag."
3792 | 	    $echo "*** or is declared to -dlopen it."
4202 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4334 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4335 | 	   test "$dlopen_self_static" = unknown; then
4336 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5674 | # The name that we can dlopen(3).
5697 | # Files to dlopen/dlpreopen
5698 | dlopen='$dlfiles'
6313 |     # Handle -dlopen flags immediately.
6342 | 	# Skip this library if it cannot be dlopened.
6367 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6727 |   -dlopen FILE      add the directory containing FILE to the library path
6729 | This mode sets the library path environment variable according to \`-dlopen'
6778 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6787 |   -module           build a library that can dlopened
{% endraw %}

```
### test/ci/valgrind/mkl.supp

```

{% raw %}
6 |    fun:dlopen@@GLIBC_2.2.5
{% endraw %}

```