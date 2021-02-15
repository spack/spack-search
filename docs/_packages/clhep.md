---
name: "clhep"
layout: package
next_package: motif
previous_package: hwloc
languages: ['bash']
---
## 2.2.0.4
12 / 922 files match

 - [CLHEP/Matrix/autotools/ltmain.sh](#clhepmatrixautotoolsltmainsh)
 - [CLHEP/GenericFunctions/autotools/ltmain.sh](#clhepgenericfunctionsautotoolsltmainsh)
 - [CLHEP/RefCount/autotools/ltmain.sh](#clheprefcountautotoolsltmainsh)
 - [CLHEP/Random/autotools/ltmain.sh](#clheprandomautotoolsltmainsh)
 - [CLHEP/Units/autotools/ltmain.sh](#clhepunitsautotoolsltmainsh)
 - [CLHEP/Exceptions/autotools/ltmain.sh](#clhepexceptionsautotoolsltmainsh)
 - [CLHEP/RandomObjects/autotools/ltmain.sh](#clheprandomobjectsautotoolsltmainsh)
 - [CLHEP/Evaluator/autotools/ltmain.sh](#clhepevaluatorautotoolsltmainsh)
 - [CLHEP/Cast/autotools/ltmain.sh](#clhepcastautotoolsltmainsh)
 - [CLHEP/Fields/autotools/ltmain.sh](#clhepfieldsautotoolsltmainsh)
 - [CLHEP/Vector/autotools/ltmain.sh](#clhepvectorautotoolsltmainsh)
 - [CLHEP/Geometry/autotools/ltmain.sh](#clhepgeometryautotoolsltmainsh)

### CLHEP/Matrix/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### CLHEP/GenericFunctions/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### CLHEP/RefCount/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### CLHEP/Random/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### CLHEP/Units/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### CLHEP/Exceptions/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### CLHEP/RandomObjects/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### CLHEP/Evaluator/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### CLHEP/Cast/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### CLHEP/Fields/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### CLHEP/Vector/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### CLHEP/Geometry/autotools/ltmain.sh

```bash

{% raw %}
439 |   -dlopen FILE      add the directory containing FILE to the library path
441 | This mode sets the library path environment variable according to \`-dlopen'
494 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
503 |   -module           build a library that can dlopened
612 |       --dlopen)		test $# -eq 0 && func_missing_arg "$opt" && break
656 |       --dlopen=*|--mode=*|--tag=*)
1601 |     # Handle -dlopen flags immediately.
1623 | 	# Skip this library if it cannot be dlopened.
1648 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2366 | 	    dlopen_self=$dlopen_self_static
2373 | 	    dlopen_self=$dlopen_self_static
2429 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2521 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2674 |       -dlopen)
3029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3096 | 	  # This library was specified with -dlopen.
3225 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3236 | 	passes="conv scan dlopen dlpreopen link"
3250 | 	dlopen) libs="$dlfiles" ;;
3277 |       if test "$pass" = dlopen; then
3483 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3484 | 	      # If there is no dlopen support or we're linking statically,
3516 | 	dlopen=
3546 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3586 | 	# This library was specified with -dlopen.
3587 | 	if test "$pass" = dlopen; then
3589 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3592 | 	     test "$dlopen_support" != yes ||
3594 | 	    # If there is no dlname, no dlopen support or we're linking
3603 | 	fi # $pass = dlopen
3658 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
3768 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
3769 | 	  dlopenmodule=""
3772 | 	      dlopenmodule="$dlpremoduletest"
3776 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
3882 | 		    # if the lib is a (non-dlopened) module then we can not
3886 | 		      if test "X$dlopenmodule" != "X$lib"; then
4036 | 	      $echo "*** a static module, that should work as long as the dlopening application"
4037 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
4162 |       if test "$pass" != dlopen; then
4261 | 	func_warning "\`-dlopen' is ignored for archives"
4324 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
4954 | 	    $echo "*** a static module, that should work as long as the dlopening"
4955 | 	    $echo "*** application is linked with the -dlopen flag."
4973 | 	    $echo "*** or is declared to -dlopen it."
5387 | 	func_warning "\`-dlopen' is ignored for objects"
5515 |         && test "$dlopen_support" = unknown \
5516 | 	&& test "$dlopen_self" = unknown \
5517 | 	&& test "$dlopen_self_static" = unknown && \
5518 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
6552 | # The name that we can dlopen(3).
6581 | # Files to dlopen/dlpreopen
6582 | dlopen='$dlfiles'
6802 |   # Only execute mode is allowed to have -dlopen flags.
6804 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```