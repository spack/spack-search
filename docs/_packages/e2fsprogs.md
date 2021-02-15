---
name: "e2fsprogs"
layout: package
next_package: herwigpp
previous_package: blast-plus
languages: ['cpp', 'bash']
---
## 1.45.5
8 / 1500 files match

 - [configure.ac](#configureac)
 - [aclocal.m4](#aclocalm4)
 - [config/ltmain.sh](#configltmainsh)
 - [lib/config.h.in](#libconfighin)
 - [lib/ss/get_readline.c](#libssget_readlinec)
 - [lib/support/plausible.c](#libsupportplausiblec)
 - [intl/libgnuintl.h.in](#intllibgnuintlhin)
 - [doc/RelNotes/v1.07.txt](#docrelnotesv107txt)

### configure.ac

```

{% raw %}
84 | dnl Check to see if libdl exists for the sake of dlopen
86 | DLOPEN_LIB=''
87 | AC_CHECK_LIB(dl, dlopen,DLOPEN_LIB=-ldl)
88 | AC_SUBST(DLOPEN_LIB)
1128 | if test -n "$DLOPEN_LIB" ; then
1129 |    ac_cv_func_dlopen=yes
1136 | 	dlopen
1207 | if test "$ac_cv_func_dlopen" = yes ; then
1208 |    MAGIC_LIB=$DLOPEN_LIB
{% endraw %}

```
### aclocal.m4

```

{% raw %}
2184 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
2335 |     opt_dlopen=
2408 |         --dlopen|-dlopen)
2409 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2532 |       # Only execute mode is allowed to have -dlopen flags.
2533 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2534 |         func_error "unrecognized option '-dlopen'"
3760 |   -dlopen FILE      add the directory containing FILE to the library path
3762 | This mode sets the library path environment variable according to '-dlopen'
3817 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3826 |   -module           build a library that can dlopened
3934 |     # Handle -dlopen flags immediately.
3935 |     for file in $opt_dlopen; do
3954 | 	# Skip this library if it cannot be dlopened.
3981 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6674 | 	    dlopen_self=$dlopen_self_static
6680 | 	    dlopen_self=$dlopen_self_static
6686 | 	    dlopen_self=$dlopen_self_static
6744 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6834 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7001 |       -dlopen)
7439 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7507 | 	  # This library was specified with -dlopen.
7627 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7638 | 	passes="conv scan dlopen dlpreopen link"
7664 | 	dlopen) libs=$dlfiles ;;
7695 |       if test dlopen = "$pass"; then
7915 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7916 | 	      # If there is no dlopen support or we're linking statically,
7944 | 	dlopen=
7974 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8020 | 	# This library was specified with -dlopen.
8021 | 	if test dlopen = "$pass"; then
8023 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8025 | 	     test yes != "$dlopen_support" ||
8028 | 	    # If there is no dlname, no dlopen support or we're linking
8037 | 	fi # $pass = dlopen
8093 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8095 | 	      # We recover the dlopen module name by 'saving' the la file
8119 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8248 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8249 | 	  dlopenmodule=
8252 | 	      dlopenmodule=$dlpremoduletest
8256 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8353 | 		    # if the lib is a (non-dlopened) module then we cannot
8357 | 		      if test "X$dlopenmodule" != "X$lib"; then
8509 | 	      echo "*** a static module, that should work as long as the dlopening application"
8510 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8654 |       if test dlopen != "$pass"; then
8784 | 	func_warning "'-dlopen' is ignored for archives"
8851 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9548 | 	    echo "*** a static module, that should work as long as the dlopening"
9549 | 	    echo "*** application is linked with the -dlopen flag."
9567 | 	    echo "*** or is declared to -dlopen it."
10179 | 	func_warning "'-dlopen' is ignored for objects"
10299 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10300 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10981 | # The name that we can dlopen(3).
11010 | # Files to dlopen/dlpreopen
11011 | dlopen='$dlfiles'
{% endraw %}

```
### lib/config.h.in

```

{% raw %}
122 | /* Define to 1 if you have the `dlopen' function. */
123 | #undef HAVE_DLOPEN
{% endraw %}

```
### lib/ss/get_readline.c

```cpp

{% raw %}
19 | #ifdef HAVE_DLOPEN
23 | #ifdef HAVE_DLOPEN
41 | #ifdef HAVE_DLOPEN
69 | 		if ((handle = dlopen(cp, RTLD_NOW))) {
{% endraw %}

```
### lib/support/plausible.c

```cpp

{% raw %}
56 | #ifdef HAVE_DLOPEN
64 | 		magic_handle = dlopen("libmagic.so.1", RTLD_NOW);
{% endraw %}

```
### intl/libgnuintl.h.in

```

{% raw %}
65 |      4. in the dlopen()ed shared libraries, in the order in which they were
66 |         dlopen()ed.
71 |      * libintl.so is a dependency of a dlopen()ed shared library but not
{% endraw %}

```
### doc/RelNotes/v1.07.txt

```

{% raw %}
71 | library files to be used with dlopen(); it also makes the transition
{% endraw %}

```