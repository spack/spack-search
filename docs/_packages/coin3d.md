---
name: "coin3d"
layout: package
next_package: adios2
previous_package: kaldi
languages: ['bash']
---
## 3.1.0
9 / 3835 files match

 - [configure.ac](#configureac)
 - [src/glue/dl.cpp](#srcgluedlcpp)
 - [src/misc/SoType.cpp](#srcmiscsotypecpp)
 - [cfg/ltmain.sh](#cfgltmainsh)
 - [docs/ChangeLog.2003](#docschangelog2003)
 - [docs/ChangeLog.2006](#docschangelog2006)
 - [docs/plan.txt](#docsplantxt)
 - [docs/ChangeLog.2005](#docschangelog2005)
 - [docs/ChangeLog.2004](#docschangelog2004)

### configure.ac

```

{% raw %}
1298 | # On Mac OS X < 10.4, dlopen() is missing and has to be emulated; from
1299 | # 10.4 on, we can use dlopen() directly. Note that the latter does not 
1309 |     # Do *not* pick up dlopen() support when building on 10.4 for earlier
1310 |     # Mac OS X versions (< 10.4 did not support dlopen(), so we have to use 
{% endraw %}

```
### src/glue/dl.cpp

```

{% raw %}
434 |        are not meant to be dlopen'ed -- but we need this for
597 |       h->nativehnd = dlopen(cc_string_get_text(path), 
606 |     h->nativehnd = dlopen(filename, RTLD_LAZY);
610 |     If dlopen() fails for any reason than not being able to find the
627 |       cc_debugerror_post("cc_dl_open", "dlopen(\"%s\") failed with: '%s'", 
637 |        Simulate the behaviour of dlopen(NULL) by returning a handle to
643 |        the "classic" dlopen() style (where a NULL return value would
660 |         cc_debugerror_postinfo("cc_dlopen", "opening: %s", 
673 |         cc_debugerror_post("cc_dlopen", "%s", errstr);
716 |      then dlopen() on HP-UX: according to a discussion on the libtool
717 |      mailinglist, dlopen() for HP-UX was buggy in an official release,
820 |   /* Note: The dlopen() version returns NULL here if handle or
{% endraw %}

```
### src/misc/SoType.cpp

```

{% raw %}
549 |       // symbol first?  dlopen(NULL) might not be portable enough, but it
{% endraw %}

```
### cfg/ltmain.sh

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
### docs/ChangeLog.2003

```

{% raw %}
12959 | 	patches/dynload-extensions-dlopen+gcc.diff, src/misc/SoType.cpp:
{% endraw %}

```
### docs/ChangeLog.2006

```

{% raw %}
2702 | 	Rewrote string handling in Mac OS X dlopen workaround code to
2706 | 	process (the entry for framework dlopen hack was only created for
{% endraw %}

```
### docs/plan.txt

```

{% raw %}
259 |   nodes, nodekits, etc (through dlopen() on UNIX systems and
{% endraw %}

```
### docs/ChangeLog.2005

```

{% raw %}
1265 | 	Mac OS X runtime binding update: use dlopen() on Mac OS 10.4 ff.
{% endraw %}

```
### docs/ChangeLog.2004

```

{% raw %}
553 | 	Mac OS X fix: Simulate the behaviour of dlopen(NULL) to return a
623 | 	    error in dlopen() earlier)
1434 | 	Bugfix: HP-UX 11 would complain on dlclose() on handles from dlopen(NULL).
{% endraw %}

```