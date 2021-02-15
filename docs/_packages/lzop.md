---
name: "lzop"
layout: package
next_package: grafana
previous_package: isc-dhcp
languages: ['bash']
---
## 1.01
1 / 86 files match

 - [acconfig/ltmain.sh](#acconfigltmainsh)

### acconfig/ltmain.sh

```bash

{% raw %}
194 |   -dlopen)
195 |     prevopt="-dlopen"
265 |   # Only execute mode is allowed to have -dlopen flags.
267 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
807 | 	    dlopen_self=$dlopen_self_static
811 | 	    dlopen_self=$dlopen_self_static
867 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
979 |       -dlopen)
1228 | 	  # This file was specified with -dlopen.
1229 | 	  if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1262 | 	  # This library was specified with -dlopen.
1374 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1386 | 	passes="conv scan dlopen dlpreopen link"
1395 | 	dlopen)
1513 | 	  if test $pass = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
1514 | 	    # If there is no dlopen support or we're linking statically,
1546 | 	dlopen=
1565 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
1607 | 	# This library was specified with -dlopen.
1608 | 	if test $pass = dlopen; then
1610 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
1613 | 	  if test -z "$dlname" || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
1614 | 	    # If there is no dlname, no dlopen support or we're linking
1621 | 	fi # $pass = dlopen
1666 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
1980 | 	      echo "*** a static module, that should work as long as the dlopening application"
1981 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2087 |       if test $pass != dlopen; then
2155 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
2220 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
2746 | 	    echo "*** a static module, that should work as long as the dlopening"
2747 | 	    echo "*** application is linked with the -dlopen flag."
2765 | 	    echo "*** or is declared to -dlopen it."
3018 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
3190 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
3191 | 	   test "$dlopen_self_static" = unknown; then
3192 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
4021 | # The name that we can dlopen(3).
4041 | # Files to dlopen/dlpreopen
4042 | dlopen='$dlfiles'
4620 |     # Handle -dlopen flags immediately.
4649 | 	# Skip this library if it cannot be dlopened.
4674 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
4988 |   -dlopen FILE      add the directory containing FILE to the library path
4990 | This mode sets the library path environment variable according to \`-dlopen'
5039 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
5048 |   -module           build a library that can dlopened
{% endraw %}

```