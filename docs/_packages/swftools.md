---
name: "swftools"
layout: package
next_package: code-server
previous_package: silo
languages: ['cpp', 'bash']
---
## 0.9.2
2 / 480 files match

 - [ltmain.sh](#ltmainsh)
 - [lib/pdf/xpdf/GlobalParams.cc](#libpdfxpdfglobalparamscc)

### ltmain.sh

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
### lib/pdf/xpdf/GlobalParams.cc

```cpp

{% raw %}
511 |   if (!(dlA = dlopen(path->getCString(), RTLD_NOW))) {
{% endraw %}

```