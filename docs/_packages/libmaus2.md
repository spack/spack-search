---
name: "libmaus2"
layout: package
next_package: moosefs
previous_package: pandaseq
languages: ['bash']
---
## 2.0.767
10 / 1990 files match

 - [configure.ac](#configureac)
 - [ltmain.sh](#ltmainsh)
 - [src/libmaus2/util/DynamicLoading.cpp](#srclibmaus2utildynamicloadingcpp)
 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [autom4te.cache/output.1](#autom4tecacheoutput1)
 - [autom4te.cache/output.2](#autom4tecacheoutput2)
 - [autom4te.cache/traces.0](#autom4tecachetraces0)
 - [autom4te.cache/traces.2](#autom4tecachetraces2)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)

### configure.ac

```

{% raw %}
389 | 	AC_CHECK_FUNC(dlopen,dlopen_nolib=yes,dlopen_nolib=no)
396 | 	AC_CHECK_LIB([dl],[dlopen],[dlopen_lib_dl=yes],[dlopen_libdl=no])
402 |         AC_MSG_CHECKING([whether we found the dlopen function anywhere])
403 | 	if test "${dlopen_nolib}" = "yes" -o "${dlopen_lib_dl}" = "yes" ; then
404 | 		dlopen_any=yes
406 | 		dlopen_any=no
408 | 	AC_MSG_RESULT([$dlopen_any])
435 | 	if test "${dlopen_any}" = "yes" -a "${dlerror_any}" = "yes" -a "${dlsym_any}" = "yes" -a "${dlclose_any}" = "yes" ; then
444 | 		if test "${dlopen_nolib}" = "no" -o "${dlerror_nolib}" = "no" -o "${dlsym_nolib}" = "no" -o "${dlclose_nolib}" = "no" ; then
{% endraw %}

```
### ltmain.sh

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
7441 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7509 | 	  # This library was specified with -dlopen.
7629 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7640 | 	passes="conv scan dlopen dlpreopen link"
7666 | 	dlopen) libs=$dlfiles ;;
7697 |       if test dlopen = "$pass"; then
7917 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7918 | 	      # If there is no dlopen support or we're linking statically,
7946 | 	dlopen=
7976 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8022 | 	# This library was specified with -dlopen.
8023 | 	if test dlopen = "$pass"; then
8025 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8027 | 	     test yes != "$dlopen_support" ||
8030 | 	    # If there is no dlname, no dlopen support or we're linking
8039 | 	fi # $pass = dlopen
8095 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8097 | 	      # We recover the dlopen module name by 'saving' the la file
8121 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8250 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8251 | 	  dlopenmodule=
8254 | 	      dlopenmodule=$dlpremoduletest
8258 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8355 | 		    # if the lib is a (non-dlopened) module then we cannot
8359 | 		      if test "X$dlopenmodule" != "X$lib"; then
8511 | 	      echo "*** a static module, that should work as long as the dlopening application"
8512 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8656 |       if test dlopen != "$pass"; then
8786 | 	func_warning "'-dlopen' is ignored for archives"
8853 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9550 | 	    echo "*** a static module, that should work as long as the dlopening"
9551 | 	    echo "*** application is linked with the -dlopen flag."
9569 | 	    echo "*** or is declared to -dlopen it."
10181 | 	func_warning "'-dlopen' is ignored for objects"
10301 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10302 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10983 | # The name that we can dlopen(3).
11012 | # Files to dlopen/dlpreopen
11013 | dlopen='$dlfiles'
{% endraw %}

```
### src/libmaus2/util/DynamicLoading.cpp

```

{% raw %}
22 | 	void libmaus2_dlopen_dummy()
35 | 	int const r = dladdr(reinterpret_cast<void*>(libmaus2_dlopen_dummy), &libinfo);
58 | 	lib = dlopen(modname.c_str(),RTLD_LAZY | RTLD_NODELETE | addflags);
60 | 	lib = dlopen(modname.c_str(),RTLD_LAZY | addflags);
68 | 		lib = dlopen(instmodname.c_str(),RTLD_LAZY | RTLD_NODELETE | addflags);
70 | 		lib = dlopen(instmodname.c_str(),RTLD_LAZY | addflags);
77 | 		se.getStream() << "Failed to dlopen(\"" << modname << "\",RTLD_LAZY): " << dlerror() << std::endl;
{% endraw %}

```
### autom4te.cache/output.0

```

{% raw %}
7767 |         enable_dlopen=no
11437 |   if test yes != "$enable_dlopen"; then
11438 |   enable_dlopen=unknown
11439 |   enable_dlopen_self=unknown
11440 |   enable_dlopen_self_static=unknown
11442 |   lt_cv_dlopen=no
11443 |   lt_cv_dlopen_libs=
11447 |     lt_cv_dlopen=load_add_on
11448 |     lt_cv_dlopen_libs=
11449 |     lt_cv_dlopen_self=yes
11453 |     lt_cv_dlopen=LoadLibrary
11454 |     lt_cv_dlopen_libs=
11458 |     lt_cv_dlopen=dlopen
11459 |     lt_cv_dlopen_libs=
11464 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11465 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11466 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11480 | char dlopen ();
11484 | return dlopen ();
11490 |   ac_cv_lib_dl_dlopen=yes
11492 |   ac_cv_lib_dl_dlopen=no
11498 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11499 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11500 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11501 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11504 |     lt_cv_dlopen=dyld
11505 |     lt_cv_dlopen_libs=
11506 |     lt_cv_dlopen_self=yes
11515 |     lt_cv_dlopen=dlopen
11516 |     lt_cv_dlopen_libs=
11517 |     lt_cv_dlopen_self=no
11523 |   lt_cv_dlopen=shl_load
11562 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
11564 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
11565 | if test "x$ac_cv_func_dlopen" = xyes; then :
11566 |   lt_cv_dlopen=dlopen
11568 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11569 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11570 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11584 | char dlopen ();
11588 | return dlopen ();
11594 |   ac_cv_lib_dl_dlopen=yes
11596 |   ac_cv_lib_dl_dlopen=no
11602 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11603 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11604 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11605 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11607 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
11608 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11609 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11623 | char dlopen ();
11627 | return dlopen ();
11633 |   ac_cv_lib_svld_dlopen=yes
11635 |   ac_cv_lib_svld_dlopen=no
11641 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11642 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11643 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11644 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
11683 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
11704 |   if test no = "$lt_cv_dlopen"; then
11705 |     enable_dlopen=no
11707 |     enable_dlopen=yes
11710 |   case $lt_cv_dlopen in
11711 |   dlopen)
11719 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11721 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11722 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11723 | if ${lt_cv_dlopen_self+:} false; then :
11727 |   lt_cv_dlopen_self=cross
11782 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11809 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
11810 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
11811 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
11815 |     lt_cv_dlopen_self=no
11822 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
11823 | $as_echo "$lt_cv_dlopen_self" >&6; }
11825 |     if test yes = "$lt_cv_dlopen_self"; then
11827 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
11828 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
11829 | if ${lt_cv_dlopen_self_static+:} false; then :
11833 |   lt_cv_dlopen_self_static=cross
11888 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11915 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
11916 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
11917 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
11921 |     lt_cv_dlopen_self_static=no
11928 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
11929 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
11938 |   case $lt_cv_dlopen_self in
11939 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
11940 |   *) enable_dlopen_self=unknown ;;
11943 |   case $lt_cv_dlopen_self_static in
11944 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
11945 |   *) enable_dlopen_self_static=unknown ;;
18529 | 	ac_fn_cxx_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
18530 | if test "x$ac_cv_func_dlopen" = xyes; then :
18531 |   dlopen_nolib=yes
18533 |   dlopen_nolib=no
18570 | 	{ $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
18571 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
18572 | if ${ac_cv_lib_dl_dlopen+:} false; then :
18586 | char dlopen ();
18590 | return dlopen ();
18596 |   ac_cv_lib_dl_dlopen=yes
18598 |   ac_cv_lib_dl_dlopen=no
18604 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
18605 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
18606 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
18607 |   dlopen_lib_dl=yes
18609 |   dlopen_libdl=no
18745 |         { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether we found the dlopen function anywhere" >&5
18746 | $as_echo_n "checking whether we found the dlopen function anywhere... " >&6; }
18747 | 	if test "${dlopen_nolib}" = "yes" -o "${dlopen_lib_dl}" = "yes" ; then
18748 | 		dlopen_any=yes
18750 | 		dlopen_any=no
18752 | 	{ $as_echo "$as_me:${as_lineno-$LINENO}: result: $dlopen_any" >&5
18753 | $as_echo "$dlopen_any" >&6; }
18787 | 	if test "${dlopen_any}" = "yes" -a "${dlerror_any}" = "yes" -a "${dlsym_any}" = "yes" -a "${dlclose_any}" = "yes" ; then
18798 | 		if test "${dlopen_nolib}" = "no" -o "${dlerror_nolib}" = "no" -o "${dlsym_nolib}" = "no" -o "${dlclose_nolib}" = "no" ; then
26031 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
26032 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
26033 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
27191 | # Whether dlopen is supported.
27192 | dlopen_support=$enable_dlopen
27194 | # Whether dlopen of programs is supported.
27195 | dlopen_self=$enable_dlopen_self
27197 | # Whether dlopen of statically linked programs is supported.
27198 | dlopen_self_static=$enable_dlopen_self_static
27242 | # Compiler flag to allow reflexive dlopens.
27484 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.1

```

{% raw %}
7767 |         enable_dlopen=no
11437 |   if test yes != "$enable_dlopen"; then
11438 |   enable_dlopen=unknown
11439 |   enable_dlopen_self=unknown
11440 |   enable_dlopen_self_static=unknown
11442 |   lt_cv_dlopen=no
11443 |   lt_cv_dlopen_libs=
11447 |     lt_cv_dlopen=load_add_on
11448 |     lt_cv_dlopen_libs=
11449 |     lt_cv_dlopen_self=yes
11453 |     lt_cv_dlopen=LoadLibrary
11454 |     lt_cv_dlopen_libs=
11458 |     lt_cv_dlopen=dlopen
11459 |     lt_cv_dlopen_libs=
11464 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11465 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11466 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11480 | char dlopen ();
11484 | return dlopen ();
11490 |   ac_cv_lib_dl_dlopen=yes
11492 |   ac_cv_lib_dl_dlopen=no
11498 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11499 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11500 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11501 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11504 |     lt_cv_dlopen=dyld
11505 |     lt_cv_dlopen_libs=
11506 |     lt_cv_dlopen_self=yes
11515 |     lt_cv_dlopen=dlopen
11516 |     lt_cv_dlopen_libs=
11517 |     lt_cv_dlopen_self=no
11523 |   lt_cv_dlopen=shl_load
11562 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
11564 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
11565 | if test "x$ac_cv_func_dlopen" = xyes; then :
11566 |   lt_cv_dlopen=dlopen
11568 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11569 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11570 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11584 | char dlopen ();
11588 | return dlopen ();
11594 |   ac_cv_lib_dl_dlopen=yes
11596 |   ac_cv_lib_dl_dlopen=no
11602 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11603 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11604 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11605 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11607 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
11608 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11609 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11623 | char dlopen ();
11627 | return dlopen ();
11633 |   ac_cv_lib_svld_dlopen=yes
11635 |   ac_cv_lib_svld_dlopen=no
11641 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11642 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11643 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11644 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
11683 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
11704 |   if test no = "$lt_cv_dlopen"; then
11705 |     enable_dlopen=no
11707 |     enable_dlopen=yes
11710 |   case $lt_cv_dlopen in
11711 |   dlopen)
11719 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11721 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11722 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11723 | if ${lt_cv_dlopen_self+:} false; then :
11727 |   lt_cv_dlopen_self=cross
11782 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11809 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
11810 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
11811 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
11815 |     lt_cv_dlopen_self=no
11822 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
11823 | $as_echo "$lt_cv_dlopen_self" >&6; }
11825 |     if test yes = "$lt_cv_dlopen_self"; then
11827 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
11828 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
11829 | if ${lt_cv_dlopen_self_static+:} false; then :
11833 |   lt_cv_dlopen_self_static=cross
11888 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11915 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
11916 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
11917 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
11921 |     lt_cv_dlopen_self_static=no
11928 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
11929 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
11938 |   case $lt_cv_dlopen_self in
11939 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
11940 |   *) enable_dlopen_self=unknown ;;
11943 |   case $lt_cv_dlopen_self_static in
11944 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
11945 |   *) enable_dlopen_self_static=unknown ;;
18529 | 	ac_fn_cxx_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
18530 | if test "x$ac_cv_func_dlopen" = xyes; then :
18531 |   dlopen_nolib=yes
18533 |   dlopen_nolib=no
18570 | 	{ $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
18571 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
18572 | if ${ac_cv_lib_dl_dlopen+:} false; then :
18586 | char dlopen ();
18590 | return dlopen ();
18596 |   ac_cv_lib_dl_dlopen=yes
18598 |   ac_cv_lib_dl_dlopen=no
18604 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
18605 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
18606 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
18607 |   dlopen_lib_dl=yes
18609 |   dlopen_libdl=no
18745 |         { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether we found the dlopen function anywhere" >&5
18746 | $as_echo_n "checking whether we found the dlopen function anywhere... " >&6; }
18747 | 	if test "${dlopen_nolib}" = "yes" -o "${dlopen_lib_dl}" = "yes" ; then
18748 | 		dlopen_any=yes
18750 | 		dlopen_any=no
18752 | 	{ $as_echo "$as_me:${as_lineno-$LINENO}: result: $dlopen_any" >&5
18753 | $as_echo "$dlopen_any" >&6; }
18787 | 	if test "${dlopen_any}" = "yes" -a "${dlerror_any}" = "yes" -a "${dlsym_any}" = "yes" -a "${dlclose_any}" = "yes" ; then
18798 | 		if test "${dlopen_nolib}" = "no" -o "${dlerror_nolib}" = "no" -o "${dlsym_nolib}" = "no" -o "${dlclose_nolib}" = "no" ; then
26031 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
26032 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
26033 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
27191 | # Whether dlopen is supported.
27192 | dlopen_support=$enable_dlopen
27194 | # Whether dlopen of programs is supported.
27195 | dlopen_self=$enable_dlopen_self
27197 | # Whether dlopen of statically linked programs is supported.
27198 | dlopen_self_static=$enable_dlopen_self_static
27242 | # Compiler flag to allow reflexive dlopens.
27484 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.2

```

{% raw %}
7767 |         enable_dlopen=no
11437 |   if test yes != "$enable_dlopen"; then
11438 |   enable_dlopen=unknown
11439 |   enable_dlopen_self=unknown
11440 |   enable_dlopen_self_static=unknown
11442 |   lt_cv_dlopen=no
11443 |   lt_cv_dlopen_libs=
11447 |     lt_cv_dlopen=load_add_on
11448 |     lt_cv_dlopen_libs=
11449 |     lt_cv_dlopen_self=yes
11453 |     lt_cv_dlopen=LoadLibrary
11454 |     lt_cv_dlopen_libs=
11458 |     lt_cv_dlopen=dlopen
11459 |     lt_cv_dlopen_libs=
11464 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11465 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11466 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11480 | char dlopen ();
11484 | return dlopen ();
11490 |   ac_cv_lib_dl_dlopen=yes
11492 |   ac_cv_lib_dl_dlopen=no
11498 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11499 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11500 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11501 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11504 |     lt_cv_dlopen=dyld
11505 |     lt_cv_dlopen_libs=
11506 |     lt_cv_dlopen_self=yes
11515 |     lt_cv_dlopen=dlopen
11516 |     lt_cv_dlopen_libs=
11517 |     lt_cv_dlopen_self=no
11523 |   lt_cv_dlopen=shl_load
11562 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
11564 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
11565 | if test "x$ac_cv_func_dlopen" = xyes; then :
11566 |   lt_cv_dlopen=dlopen
11568 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
11569 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11570 | if ${ac_cv_lib_dl_dlopen+:} false; then :
11584 | char dlopen ();
11588 | return dlopen ();
11594 |   ac_cv_lib_dl_dlopen=yes
11596 |   ac_cv_lib_dl_dlopen=no
11602 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
11603 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11604 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
11605 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
11607 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
11608 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11609 | if ${ac_cv_lib_svld_dlopen+:} false; then :
11623 | char dlopen ();
11627 | return dlopen ();
11633 |   ac_cv_lib_svld_dlopen=yes
11635 |   ac_cv_lib_svld_dlopen=no
11641 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
11642 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11643 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
11644 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
11683 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
11704 |   if test no = "$lt_cv_dlopen"; then
11705 |     enable_dlopen=no
11707 |     enable_dlopen=yes
11710 |   case $lt_cv_dlopen in
11711 |   dlopen)
11719 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11721 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
11722 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11723 | if ${lt_cv_dlopen_self+:} false; then :
11727 |   lt_cv_dlopen_self=cross
11782 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11809 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
11810 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
11811 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
11815 |     lt_cv_dlopen_self=no
11822 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
11823 | $as_echo "$lt_cv_dlopen_self" >&6; }
11825 |     if test yes = "$lt_cv_dlopen_self"; then
11827 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
11828 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
11829 | if ${lt_cv_dlopen_self_static+:} false; then :
11833 |   lt_cv_dlopen_self_static=cross
11888 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11915 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
11916 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
11917 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
11921 |     lt_cv_dlopen_self_static=no
11928 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
11929 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
11938 |   case $lt_cv_dlopen_self in
11939 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
11940 |   *) enable_dlopen_self=unknown ;;
11943 |   case $lt_cv_dlopen_self_static in
11944 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
11945 |   *) enable_dlopen_self_static=unknown ;;
18529 | 	ac_fn_cxx_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
18530 | if test "x$ac_cv_func_dlopen" = xyes; then :
18531 |   dlopen_nolib=yes
18533 |   dlopen_nolib=no
18570 | 	{ $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
18571 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
18572 | if ${ac_cv_lib_dl_dlopen+:} false; then :
18586 | char dlopen ();
18590 | return dlopen ();
18596 |   ac_cv_lib_dl_dlopen=yes
18598 |   ac_cv_lib_dl_dlopen=no
18604 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
18605 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
18606 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
18607 |   dlopen_lib_dl=yes
18609 |   dlopen_libdl=no
18745 |         { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether we found the dlopen function anywhere" >&5
18746 | $as_echo_n "checking whether we found the dlopen function anywhere... " >&6; }
18747 | 	if test "${dlopen_nolib}" = "yes" -o "${dlopen_lib_dl}" = "yes" ; then
18748 | 		dlopen_any=yes
18750 | 		dlopen_any=no
18752 | 	{ $as_echo "$as_me:${as_lineno-$LINENO}: result: $dlopen_any" >&5
18753 | $as_echo "$dlopen_any" >&6; }
18787 | 	if test "${dlopen_any}" = "yes" -a "${dlerror_any}" = "yes" -a "${dlsym_any}" = "yes" -a "${dlclose_any}" = "yes" ; then
18798 | 		if test "${dlopen_nolib}" = "no" -o "${dlerror_nolib}" = "no" -o "${dlsym_nolib}" = "no" -o "${dlclose_nolib}" = "no" ; then
26031 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
26032 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
26033 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
27191 | # Whether dlopen is supported.
27192 | dlopen_support=$enable_dlopen
27194 | # Whether dlopen of programs is supported.
27195 | dlopen_self=$enable_dlopen_self
27197 | # Whether dlopen of statically linked programs is supported.
27198 | dlopen_self_static=$enable_dlopen_self_static
27242 | # Compiler flag to allow reflexive dlopens.
27484 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.0

```

{% raw %}
411 | m4trace:/usr/share/aclocal/libtool.m4:1920: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
412 | if test yes != "$enable_dlopen"; then
413 |   enable_dlopen=unknown
414 |   enable_dlopen_self=unknown
415 |   enable_dlopen_self_static=unknown
417 |   lt_cv_dlopen=no
418 |   lt_cv_dlopen_libs=
422 |     lt_cv_dlopen=load_add_on
423 |     lt_cv_dlopen_libs=
424 |     lt_cv_dlopen_self=yes
428 |     lt_cv_dlopen=LoadLibrary
429 |     lt_cv_dlopen_libs=
433 |     lt_cv_dlopen=dlopen
434 |     lt_cv_dlopen_libs=
439 |     AC_CHECK_LIB([dl], [dlopen],
440 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
441 |     lt_cv_dlopen=dyld
442 |     lt_cv_dlopen_libs=
443 |     lt_cv_dlopen_self=yes
450 |     lt_cv_dlopen=dlopen
451 |     lt_cv_dlopen_libs=
452 |     lt_cv_dlopen_self=no
457 | 	  [lt_cv_dlopen=shl_load],
459 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
460 | 	[AC_CHECK_FUNC([dlopen],
461 | 	      [lt_cv_dlopen=dlopen],
462 | 	  [AC_CHECK_LIB([dl], [dlopen],
463 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
464 | 	    [AC_CHECK_LIB([svld], [dlopen],
465 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
467 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
476 |   if test no = "$lt_cv_dlopen"; then
477 |     enable_dlopen=no
479 |     enable_dlopen=yes
482 |   case $lt_cv_dlopen in
483 |   dlopen)
491 |     LIBS="$lt_cv_dlopen_libs $LIBS"
493 |     AC_CACHE_CHECK([whether a program can dlopen itself],
494 | 	  lt_cv_dlopen_self, [dnl
495 | 	  _LT_TRY_DLOPEN_SELF(
496 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
497 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
500 |     if test yes = "$lt_cv_dlopen_self"; then
502 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
503 | 	  lt_cv_dlopen_self_static, [dnl
504 | 	  _LT_TRY_DLOPEN_SELF(
505 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
506 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
516 |   case $lt_cv_dlopen_self in
517 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
518 |   *) enable_dlopen_self=unknown ;;
521 |   case $lt_cv_dlopen_self_static in
522 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
523 |   *) enable_dlopen_self_static=unknown ;;
526 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
527 | 	 [Whether dlopen is supported])
528 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
529 | 	 [Whether dlopen of programs is supported])
530 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
531 | 	 [Whether dlopen of statically linked programs is supported])
533 | m4trace:/usr/share/aclocal/libtool.m4:2045: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
534 | m4trace:/usr/share/aclocal/libtool.m4:2045: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
536 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1086 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1130 | eval "LTDLOPEN=\"$libname_spec\""
1131 | AC_SUBST([LTDLOPEN])
1133 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1134 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1135 |   [lt_cv_sys_dlopen_deplibs],
1136 |   [# PORTME does your system automatically load deplibs for dlopen?
1140 |   lt_cv_sys_dlopen_deplibs=unknown
1145 |     lt_cv_sys_dlopen_deplibs=unknown
1148 |     lt_cv_sys_dlopen_deplibs=yes
1153 |       lt_cv_sys_dlopen_deplibs=no
1158 |     lt_cv_sys_dlopen_deplibs=yes
1163 |     lt_cv_sys_dlopen_deplibs=yes
1166 |     lt_cv_sys_dlopen_deplibs=yes
1170 |     lt_cv_sys_dlopen_deplibs=yes
1173 |     lt_cv_sys_dlopen_deplibs=yes
1176 |     lt_cv_sys_dlopen_deplibs=yes
1181 |     lt_cv_sys_dlopen_deplibs=unknown
1185 |     # at 6.2 and later dlopen does load deplibs.
1186 |     lt_cv_sys_dlopen_deplibs=yes
1189 |     lt_cv_sys_dlopen_deplibs=yes
1192 |     lt_cv_sys_dlopen_deplibs=yes
1195 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1198 |     lt_cv_sys_dlopen_deplibs=no
1201 |     # dlopen *does* load deplibs and with the right loader patch applied
1207 |     lt_cv_sys_dlopen_deplibs=unknown
1214 |     lt_cv_sys_dlopen_deplibs=yes
1217 |     lt_cv_sys_dlopen_deplibs=yes
1220 |     lt_cv_sys_dlopen_deplibs=yes
1223 |     libltdl_cv_sys_dlopen_deplibs=yes
1227 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
1228 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1229 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1232 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1233 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1235 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1307 | LIBADD_DLOPEN=
1308 | AC_SEARCH_LIBS([dlopen], [dl],
1311 | 	if test "$ac_cv_search_dlopen" != "none required"; then
1312 | 	  LIBADD_DLOPEN=-ldl
1314 | 	libltdl_cv_lib_dl_dlopen=yes
1315 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1319 |     ]], [[dlopen(0, 0);]])],
1322 | 	    libltdl_cv_func_dlopen=yes
1323 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1324 | 	[AC_CHECK_LIB([svld], [dlopen],
1327 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
1328 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1329 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
1332 |   LIBS="$LIBS $LIBADD_DLOPEN"
1336 | AC_SUBST([LIBADD_DLOPEN])
1342 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1346 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1356 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1359 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1363 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1370 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
1386 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
1438 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
1443 |       LIBS="$LIBS $LIBADD_DLOPEN"
1501 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
1543 | m4trace:/usr/share/aclocal/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1546 | put the 'dlopen' option into LT_INIT's first parameter.])
1548 | m4trace:/usr/share/aclocal/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1550 | _LT_SET_OPTION([LT_INIT], [dlopen])
1553 | put the 'dlopen' option into LT_INIT's first parameter.])
1645 | m4trace:/usr/share/aclocal/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2750 | m4trace:configure.ac:6: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### autom4te.cache/traces.2

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
290 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
291 |   [lt_cv_sys_dlopen_deplibs],
292 |   [# PORTME does your system automatically load deplibs for dlopen?
296 |   lt_cv_sys_dlopen_deplibs=unknown
301 |     lt_cv_sys_dlopen_deplibs=unknown
304 |     lt_cv_sys_dlopen_deplibs=yes
309 |       lt_cv_sys_dlopen_deplibs=no
314 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
326 |     lt_cv_sys_dlopen_deplibs=yes
329 |     lt_cv_sys_dlopen_deplibs=yes
332 |     lt_cv_sys_dlopen_deplibs=yes
337 |     lt_cv_sys_dlopen_deplibs=unknown
341 |     # at 6.2 and later dlopen does load deplibs.
342 |     lt_cv_sys_dlopen_deplibs=yes
345 |     lt_cv_sys_dlopen_deplibs=yes
348 |     lt_cv_sys_dlopen_deplibs=yes
351 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
354 |     lt_cv_sys_dlopen_deplibs=no
357 |     # dlopen *does* load deplibs and with the right loader patch applied
363 |     lt_cv_sys_dlopen_deplibs=unknown
370 |     lt_cv_sys_dlopen_deplibs=yes
373 |     lt_cv_sys_dlopen_deplibs=yes
376 |     lt_cv_sys_dlopen_deplibs=yes
379 |     libltdl_cv_sys_dlopen_deplibs=yes
383 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
384 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
385 |     [Define if the OS needs help to load dependent libraries for dlopen().])
388 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/usr/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
391 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
463 | LIBADD_DLOPEN=
464 | AC_SEARCH_LIBS([dlopen], [dl],
467 | 	if test "$ac_cv_search_dlopen" != "none required"; then
468 | 	  LIBADD_DLOPEN=-ldl
470 | 	libltdl_cv_lib_dl_dlopen=yes
471 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
475 |     ]], [[dlopen(0, 0);]])],
478 | 	    libltdl_cv_func_dlopen=yes
479 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
480 | 	[AC_CHECK_LIB([svld], [dlopen],
483 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
484 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
485 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
488 |   LIBS="$LIBS $LIBADD_DLOPEN"
492 | AC_SUBST([LIBADD_DLOPEN])
498 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
502 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
512 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
515 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
519 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
526 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
542 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
594 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
599 |       LIBS="$LIBS $LIBADD_DLOPEN"
657 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
2025 | m4trace:m4/libtool.m4:1920: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
2026 | if test yes != "$enable_dlopen"; then
2027 |   enable_dlopen=unknown
2028 |   enable_dlopen_self=unknown
2029 |   enable_dlopen_self_static=unknown
2031 |   lt_cv_dlopen=no
2032 |   lt_cv_dlopen_libs=
2036 |     lt_cv_dlopen=load_add_on
2037 |     lt_cv_dlopen_libs=
2038 |     lt_cv_dlopen_self=yes
2042 |     lt_cv_dlopen=LoadLibrary
2043 |     lt_cv_dlopen_libs=
2047 |     lt_cv_dlopen=dlopen
2048 |     lt_cv_dlopen_libs=
2053 |     AC_CHECK_LIB([dl], [dlopen],
2054 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
2055 |     lt_cv_dlopen=dyld
2056 |     lt_cv_dlopen_libs=
2057 |     lt_cv_dlopen_self=yes
2064 |     lt_cv_dlopen=dlopen
2065 |     lt_cv_dlopen_libs=
2066 |     lt_cv_dlopen_self=no
2071 | 	  [lt_cv_dlopen=shl_load],
2073 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
2074 | 	[AC_CHECK_FUNC([dlopen],
2075 | 	      [lt_cv_dlopen=dlopen],
2076 | 	  [AC_CHECK_LIB([dl], [dlopen],
2077 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
2078 | 	    [AC_CHECK_LIB([svld], [dlopen],
2079 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
2081 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2090 |   if test no = "$lt_cv_dlopen"; then
2091 |     enable_dlopen=no
2093 |     enable_dlopen=yes
2096 |   case $lt_cv_dlopen in
2097 |   dlopen)
2105 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2107 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2108 | 	  lt_cv_dlopen_self, [dnl
2109 | 	  _LT_TRY_DLOPEN_SELF(
2110 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2111 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2114 |     if test yes = "$lt_cv_dlopen_self"; then
2116 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2117 | 	  lt_cv_dlopen_self_static, [dnl
2118 | 	  _LT_TRY_DLOPEN_SELF(
2119 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2120 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2130 |   case $lt_cv_dlopen_self in
2131 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2132 |   *) enable_dlopen_self=unknown ;;
2135 |   case $lt_cv_dlopen_self_static in
2136 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2137 |   *) enable_dlopen_self_static=unknown ;;
2140 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2141 | 	 [Whether dlopen is supported])
2142 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2143 | 	 [Whether dlopen of programs is supported])
2144 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2145 | 	 [Whether dlopen of statically linked programs is supported])
2147 | m4trace:m4/libtool.m4:2045: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2148 | m4trace:m4/libtool.m4:2045: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2150 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2459 | m4trace:m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2462 | put the 'dlopen' option into LT_INIT's first parameter.])
2464 | m4trace:m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2466 | _LT_SET_OPTION([LT_INIT], [dlopen])
2469 | put the 'dlopen' option into LT_INIT's first parameter.])
2561 | m4trace:m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2750 | m4trace:configure.ac:6: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1820 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1823 | m4_defun([_LT_TRY_DLOPEN_SELF],
1881 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1914 | ])# _LT_TRY_DLOPEN_SELF
1917 | # LT_SYS_DLOPEN_SELF
1919 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1921 | if test yes != "$enable_dlopen"; then
1922 |   enable_dlopen=unknown
1923 |   enable_dlopen_self=unknown
1924 |   enable_dlopen_self_static=unknown
1926 |   lt_cv_dlopen=no
1927 |   lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen=load_add_on
1932 |     lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen_self=yes
1937 |     lt_cv_dlopen=LoadLibrary
1938 |     lt_cv_dlopen_libs=
1942 |     lt_cv_dlopen=dlopen
1943 |     lt_cv_dlopen_libs=
1948 |     AC_CHECK_LIB([dl], [dlopen],
1949 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1950 |     lt_cv_dlopen=dyld
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1959 |     lt_cv_dlopen=dlopen
1960 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen_self=no
1966 | 	  [lt_cv_dlopen=shl_load],
1968 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1969 | 	[AC_CHECK_FUNC([dlopen],
1970 | 	      [lt_cv_dlopen=dlopen],
1971 | 	  [AC_CHECK_LIB([dl], [dlopen],
1972 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1973 | 	    [AC_CHECK_LIB([svld], [dlopen],
1974 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1976 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1985 |   if test no = "$lt_cv_dlopen"; then
1986 |     enable_dlopen=no
1988 |     enable_dlopen=yes
1991 |   case $lt_cv_dlopen in
1992 |   dlopen)
2000 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2002 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2003 | 	  lt_cv_dlopen_self, [dnl
2004 | 	  _LT_TRY_DLOPEN_SELF(
2005 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2006 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2009 |     if test yes = "$lt_cv_dlopen_self"; then
2011 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2012 | 	  lt_cv_dlopen_self_static, [dnl
2013 | 	  _LT_TRY_DLOPEN_SELF(
2014 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2015 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2025 |   case $lt_cv_dlopen_self in
2026 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2027 |   *) enable_dlopen_self=unknown ;;
2030 |   case $lt_cv_dlopen_self_static in
2031 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2032 |   *) enable_dlopen_self_static=unknown ;;
2035 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2036 | 	 [Whether dlopen is supported])
2037 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2038 | 	 [Whether dlopen of programs is supported])
2039 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2040 | 	 [Whether dlopen of statically linked programs is supported])
2041 | ])# LT_SYS_DLOPEN_SELF
2044 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2046 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6147 |     [Compiler flag to allow reflexive dlopens])
6260 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
107 | # dlopen
109 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
112 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
113 | [_LT_SET_OPTION([LT_INIT], [dlopen])
116 | put the 'dlopen' option into LT_INIT's first parameter.])
120 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```