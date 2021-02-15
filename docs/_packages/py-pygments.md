---
name: "py-pygments"
layout: package
next_package: libcerf
previous_package: treelite
languages: ['bash']
---
## 2.4.2
2 / 1149 files match

 - [tests/examplefiles/ltmain.sh](#testsexamplefilesltmainsh)
 - [tests/examplefiles/output/ltmain.sh](#testsexamplefilesoutputltmainsh)

### tests/examplefiles/ltmain.sh

```bash

{% raw %}
570 |   -dlopen)
571 |     prevopt="-dlopen"
655 |   # Only execute mode is allowed to have -dlopen flags.
657 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1194 | 	    dlopen_self=$dlopen_self_static
1199 | 	    dlopen_self=$dlopen_self_static
1255 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1347 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1504 |       -dlopen)
1891 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1964 | 	  # This library was specified with -dlopen.
2105 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2117 | 	passes="conv scan dlopen dlpreopen link"
2130 | 	dlopen) libs="$dlfiles" ;;
2135 |       if test "$pass" = dlopen; then
2314 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2315 | 	      # If there is no dlopen support or we're linking statically,
2348 | 	dlopen=
2369 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2412 | 	# This library was specified with -dlopen.
2413 | 	if test "$pass" = dlopen; then
2415 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2419 | 	     test "$dlopen_support" != yes ||
2421 | 	    # If there is no dlname, no dlopen support or we're linking
2430 | 	fi # $pass = dlopen
2483 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
{% endraw %}

```
### tests/examplefiles/output/ltmain.sh

```bash

{% raw %}
14256 | V-dlopen
14274 | V"-dlopen"
15752 | V# Only execute mode is allowed to have -dlopen flags.\u000a
15862 | V: unrecognized option \u005c`-dlopen'
25715 | Vdlopen_self
25722 | V$dlopen_self_static
25840 | Vdlopen_self
25847 | V$dlopen_self_static
27042 | V$dlopen_self
28829 | V$dlopen_support
31778 | V-dlopen
39388 | V$dlopen_support
40788 | V# This library was specified with -dlopen.\u000a
43916 | V: libraries can \u005c`-dlopen' only libtool libraries: 
44074 | V"conv scan dlopen dlpreopen link"
44394 | Vdlopen
44571 | Vdlopen
49120 | V$dlopen_support
49197 | V# If there is no dlopen support or we're linking statically,\u000a
49947 | Vdlopen
50407 | V$dlopen
50441 | V$dlopen
51542 | V# This library was specified with -dlopen.\u000a
51582 | Vdlopen
51659 | V: cannot -dlopen a convenience library: \u005c`
51767 | V$dlopen_support
51845 | V# If there is no dlname, no dlopen support or we're linking\u000a
51971 | V# $pass = dlopen\u000a
53447 | V# Otherwise, use the dlname, so that lt_dlopen finds it.\u000a
{% endraw %}

```