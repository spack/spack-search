---
name: "openslp"
layout: package
next_package: tauola
previous_package: gtkorvo-enet
languages: ['bash']
---
## 2.0.0
3 / 445 files match

 - [openslp.contrib/kio_slp/admin/ltmain.sh](#openslpcontribkio_slpadminltmainsh)
 - [openslp.contrib/kio_slp/admin/libtool.m4.in](#openslpcontribkio_slpadminlibtoolm4in)
 - [openslp/configure.ac](#openslpconfigureac)

### openslp.contrib/kio_slp/admin/ltmain.sh

```bash

{% raw %}
215 |   -dlopen)
216 |     prevopt="-dlopen"
281 |   # Only execute mode is allowed to have -dlopen flags.
283 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
852 | 	    dlopen_self=$dlopen_self_static
856 | 	    dlopen_self=$dlopen_self_static
913 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1020 |       -dlopen)
1288 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1356 | 	  # This library was specified with -dlopen.
1516 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1528 | 	passes="conv scan dlopen dlpreopen link"
1541 | 	dlopen) libs="$dlfiles" ;;
1546 |       if test $pass = dlopen; then
1660 | 	    if test $pass = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
1661 | 	      # If there is no dlopen support or we're linking statically,
1694 | 	dlopen=
1712 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
1752 | 	# This library was specified with -dlopen.
1753 | 	if test $pass = dlopen; then
1755 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
1758 | 	  if test -z "$dlname" || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
1759 | 	    # If there is no dlname, no dlopen support or we're linking statically,
2195 |       if test $pass != dlopen; then
2262 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
2327 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
2775 | 	    echo "*** a static module, that should work as long as the dlopening"
2776 | 	    echo "*** application is linked with the -dlopen flag."
2794 | 	    echo "*** or is declared to -dlopen it."
3020 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
3189 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
3190 | 	   test "$dlopen_self_static" = unknown; then
3191 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
3980 | # The name that we can dlopen(3).
4000 | # Files to dlopen/dlpreopen
4001 | dlopen='$dlfiles'
4538 |     # Handle -dlopen flags immediately.
4567 | 	# Skip this library if it cannot be dlopened.
4592 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
4875 |   -dlopen FILE      add the directory containing FILE to the library path
4877 | This mode sets the library path environment variable according to \`-dlopen'
4926 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
4935 |   -module           build a library that can dlopened
{% endraw %}

```
### openslp.contrib/kio_slp/admin/libtool.m4.in

```

{% raw %}
117 | ifdef([AC_PROVIDE_AC_LIBTOOL_DLOPEN],
118 | [libtool_flags="$libtool_flags --enable-dlopen"])
202 | # AC_LIBTOOL_DLOPEN - enable checks for dlopen support
203 | AC_DEFUN(AC_LIBTOOL_DLOPEN, [AC_BEFORE([$0],[AC_LIBTOOL_SETUP])])
{% endraw %}

```
### openslp/configure.ac

```

{% raw %}
159 |   AC_CHECK_LIB([dl], [dlopen], [],
{% endraw %}

```