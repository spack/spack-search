---
name: "clamav"
layout: package
next_package: modern-wheel
previous_package: llvm-doe
languages: ['html', 'cmake', 'cpp', 'bash']
---
## 0.101.2
55 / 6766 files match

 - [configure.ac](#configureac)
 - [clamav-config.h.in](#clamav-confighin)
 - [config/ltmain.sh](#configltmainsh)
 - [libclamav/others.c](#libclamavothersc)
 - [libclamav/Makefile.am](#libclamavmakefileam)
 - [libclamav/Makefile.in](#libclamavmakefilein)
 - [libclamav/c++/config/ltmain.sh](#libclamavc++configltmainsh)
 - [libclamav/c++/llvm/lib/System/DynamicLibrary.cpp](#libclamavc++llvmlibsystemdynamiclibrarycpp)
 - [libclamav/c++/llvm/lib/ExecutionEngine/ExecutionEngine.cpp](#libclamavc++llvmlibexecutionengineexecutionenginecpp)
 - [libclamav/c++/llvm/lib/ExecutionEngine/JIT/JIT.cpp](#libclamavc++llvmlibexecutionenginejitjitcpp)
 - [libclamav/c++/llvm/include/llvm/Config/config.h.in](#libclamavc++llvmincludellvmconfigconfighin)
 - [libclamav/c++/llvm/include/llvm/Config/config.h.cmake](#libclamavc++llvmincludellvmconfigconfighcmake)
 - [libclamav/c++/llvm/include/llvm/Support/DynamicLinker.h](#libclamavc++llvmincludellvmsupportdynamiclinkerh)
 - [libclamav/c++/llvm/include/llvm-c/LinkTimeOptimizer.h](#libclamavc++llvmincludellvm-clinktimeoptimizerh)
 - [libclamav/c++/llvm/cmake/config-ix.cmake](#libclamavc++llvmcmakeconfig-ixcmake)
 - [libclamav/c++/llvm/autoconf/configure.ac](#libclamavc++llvmautoconfconfigureac)
 - [libclamav/c++/llvm/autoconf/ltmain.sh](#libclamavc++llvmautoconfltmainsh)
 - [libclamav/c++/llvm/autoconf/m4/libtool.m4](#libclamavc++llvmautoconfm4libtoolm4)
 - [libclamav/c++/llvm/autoconf/m4/ltdl.m4](#libclamavc++llvmautoconfm4ltdlm4)
 - [libclamav/c++/m4/libtool.m4](#libclamavc++m4libtoolm4)
 - [libclamav/c++/m4/ltoptions.m4](#libclamavc++m4ltoptionsm4)
 - [unit_tests/valgrind.supp](#unit_testsvalgrindsupp)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/lib-link.m4](#m4lib-linkm4)
 - [m4/ltdl.m4](#m4ltdlm4)
 - [libclammspack/ltmain.sh](#libclammspackltmainsh)
 - [libclammspack/m4/libtool.m4](#libclammspackm4libtoolm4)
 - [libclammspack/m4/ltoptions.m4](#libclammspackm4ltoptionsm4)
 - [libltdl/ltdl.h](#libltdlltdlh)
 - [libltdl/ltdl.c](#libltdlltdlc)
 - [libltdl/Makefile.am](#libltdlmakefileam)
 - [libltdl/Makefile.in](#libltdlmakefilein)
 - [libltdl/loaders/preopen.c](#libltdlloaderspreopenc)
 - [libltdl/loaders/dlopen.c](#libltdlloadersdlopenc)
 - [libltdl/libltdl/lt__private.h](#libltdllibltdllt__privateh)
 - [libltdl/libltdl/lt_error.h](#libltdllibltdllt_errorh)
 - [docs/UserManual/development.md](#docsusermanualdevelopmentmd)
 - [docs/html/UserManual/development.html](#docshtmlusermanualdevelopmenthtml)
 - [win32/clamav-config.h](#win32clamav-configh)
 - [win32/compat/ltdl.h](#win32compatltdlh)
 - [win32/compat/ltdl.c](#win32compatltdlc)
 - [win32/llvmbuild/include/llvm/Config/config.h](#win32llvmbuildincludellvmconfigconfigh)
 - [win32/3rdparty/libxml2/config.h.in](#win323rdpartylibxml2confighin)
 - [win32/3rdparty/libxml2/configure.ac](#win323rdpartylibxml2configureac)
 - [win32/3rdparty/libxml2/xmlmodule.c](#win323rdpartylibxml2xmlmodulec)
 - [win32/3rdparty/libxml2/ltmain.sh](#win323rdpartylibxml2ltmainsh)
 - [win32/3rdparty/libxml2/os400/wrappers.h](#win323rdpartylibxml2os400wrappersh)
 - [win32/3rdparty/libxml2/os400/wrappers.c](#win323rdpartylibxml2os400wrappersc)
 - [win32/3rdparty/libxml2/os400/config.h.in](#win323rdpartylibxml2os400confighin)
 - [win32/3rdparty/libxml2/os400/os400config.h.in](#win323rdpartylibxml2os400os400confighin)
 - [win32/3rdparty/libxml2/os400/dlfcn/dlfcn.h](#win323rdpartylibxml2os400dlfcndlfcnh)
 - [win32/3rdparty/libxml2/os400/dlfcn/dlfcn.c](#win323rdpartylibxml2os400dlfcndlfcnc)
 - [win32/3rdparty/libxml2/m4/libtool.m4](#win323rdpartylibxml2m4libtoolm4)
 - [win32/3rdparty/libxml2/m4/ltoptions.m4](#win323rdpartylibxml2m4ltoptionsm4)

### configure.ac

```

{% raw %}
54 | LT_INIT([dlopen disable-static])
{% endraw %}

```
### clamav-config.h.in

```

{% raw %}
476 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
477 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### libclamav/others.c

```cpp

{% raw %}
150 | 	rhandle = lt_dlopen(modulename);
159 | #ifdef WARN_DLOPEN_FAIL
160 |         cli_warnmsg("Cannot dlopen %s: %s - %s support unavailable\n", name, err, featurename);
162 |         cli_dbgmsg("Cannot dlopen %s: %s - %s support unavailable\n", name, err, featurename);
299 |     /* put dlopen() stuff here, etc. */
{% endraw %}

```
### libclamav/Makefile.am

```

{% raw %}
28 | AM_CPPFLAGS += -DWARN_DLOPEN_FAIL
106 | IFACELIBADD = -dlopen libclamunrar_iface.la
{% endraw %}

```
### libclamav/Makefile.in

```

{% raw %}
102 | @ENABLE_UNRAR_TRUE@am__append_1 = -DWARN_DLOPEN_FAIL
954 | LIBADD_DLOPEN = @LIBADD_DLOPEN@
980 | LTDLOPEN = @LTDLOPEN@
1176 | @ENABLE_UNRAR_TRUE@IFACELIBADD = -dlopen libclamunrar_iface.la
{% endraw %}

```
### libclamav/c++/config/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### libclamav/c++/llvm/lib/System/DynamicLibrary.cpp

```

{% raw %}
56 |     if (ErrMsg) *ErrMsg = "dlopen disabled";
76 |   void *H = dlopen(Filename, RTLD_LAZY|RTLD_GLOBAL);
83 |   // with the handle of dlopen(NULL, RTLD_GLOBAL).
98 |   if (ErrMsg) *ErrMsg = "dlopen() not supported on this platform";
{% endraw %}

```
### libclamav/c++/llvm/lib/ExecutionEngine/ExecutionEngine.cpp

```

{% raw %}
447 | /* CLAMAV LOCAL: allow for no dlopen */
{% endraw %}

```
### libclamav/c++/llvm/lib/ExecutionEngine/JIT/JIT.cpp

```

{% raw %}
223 | /* CLAMAV LOCAL: no dlopen */
{% endraw %}

```
### libclamav/c++/llvm/include/llvm/Config/config.h.in

```

{% raw %}
96 | /* Define if dlopen() is available on this platform. */
97 | #undef HAVE_DLOPEN
550 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
551 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### libclamav/c++/llvm/include/llvm/Config/config.h.cmake

```cmake

{% raw %}
8 | /* Define if dlopen(0) will open the symbols of the program */
9 | #undef CAN_DLOPEN_SELF
93 | /* Define if dlopen() is available on this platform. */
94 | #undef HAVE_DLOPEN
532 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
533 | #cmakedefine LTDL_DLOPEN_DEPLIBS ${LTDL_DLOPEN_DEPLIBS}
{% endraw %}

```
### libclamav/c++/llvm/include/llvm/Support/DynamicLinker.h

```cpp

{% raw %}
25 | /// if it is not NULL). Analogous to dlopen().
{% endraw %}

```
### libclamav/c++/llvm/include/llvm-c/LinkTimeOptimizer.h

```cpp

{% raw %}
43 |   /// linker to use dlopen() interface to dynamically load LinkTimeOptimizer.
44 |   /// extern "C" helps, because dlopen() interface uses name to find the symbol.
{% endraw %}

```
### libclamav/c++/llvm/cmake/config-ix.cmake

```cmake

{% raw %}
77 |   check_library_exists(dl dlopen "" HAVE_LIBDL)
235 |   set(LTDL_DLOPEN_DEPLIBS 1)
246 |   set(LTDL_DLOPEN_DEPLIBS 0)  # TODO
{% endraw %}

```
### libclamav/c++/llvm/autoconf/configure.ac

```

{% raw %}
1032 | dnl Check for libtool and the library that has dlopen function (which must come
1033 | dnl before the AC_PROG_LIBTOOL check in order to enable dlopening libraries with
1035 | AC_LIBTOOL_DLOPEN
1152 | dnl dlopen() is required for plugin support.
1153 | AC_SEARCH_LIBS(dlopen,dl,AC_DEFINE([HAVE_DLOPEN],[1],
1154 |                [Define if dlopen() is available on this platform.]),
1155 |                AC_MSG_WARN([dlopen() not found - disabling plugin support]))
{% endraw %}

```
### libclamav/c++/llvm/autoconf/ltmain.sh

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
### libclamav/c++/llvm/autoconf/m4/libtool.m4

```

{% raw %}
199 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
811 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
814 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
870 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
899 | ])# _LT_AC_TRY_DLOPEN_SELF
902 | # AC_LIBTOOL_DLOPEN_SELF
904 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
906 | if test "x$enable_dlopen" != xyes; then
907 |   enable_dlopen=unknown
908 |   enable_dlopen_self=unknown
909 |   enable_dlopen_self_static=unknown
911 |   lt_cv_dlopen=no
912 |   lt_cv_dlopen_libs=
916 |     lt_cv_dlopen="load_add_on"
917 |     lt_cv_dlopen_libs=
918 |     lt_cv_dlopen_self=yes
922 |     lt_cv_dlopen="LoadLibrary"
923 |     lt_cv_dlopen_libs=
927 |     lt_cv_dlopen="dlopen"
928 |     lt_cv_dlopen_libs=
933 |     AC_CHECK_LIB([dl], [dlopen],
934 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
935 |     lt_cv_dlopen="dyld"
936 |     lt_cv_dlopen_libs=
937 |     lt_cv_dlopen_self=yes
943 | 	  [lt_cv_dlopen="shl_load"],
945 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
946 | 	[AC_CHECK_FUNC([dlopen],
947 | 	      [lt_cv_dlopen="dlopen"],
948 | 	  [AC_CHECK_LIB([dl], [dlopen],
949 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
950 | 	    [AC_CHECK_LIB([svld], [dlopen],
951 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
953 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
962 |   if test "x$lt_cv_dlopen" != xno; then
963 |     enable_dlopen=yes
965 |     enable_dlopen=no
968 |   case $lt_cv_dlopen in
969 |   dlopen)
977 |     LIBS="$lt_cv_dlopen_libs $LIBS"
979 |     AC_CACHE_CHECK([whether a program can dlopen itself],
980 | 	  lt_cv_dlopen_self, [dnl
981 | 	  _LT_AC_TRY_DLOPEN_SELF(
982 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
983 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
986 |     if test "x$lt_cv_dlopen_self" = xyes; then
988 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
989 |     	  lt_cv_dlopen_self_static, [dnl
990 | 	  _LT_AC_TRY_DLOPEN_SELF(
991 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
992 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1002 |   case $lt_cv_dlopen_self in
1003 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1004 |   *) enable_dlopen_self=unknown ;;
1007 |   case $lt_cv_dlopen_self_static in
1008 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1009 |   *) enable_dlopen_self_static=unknown ;;
1012 | ])# AC_LIBTOOL_DLOPEN_SELF
1884 | # AC_LIBTOOL_DLOPEN
1886 | # enable checks for dlopen support
1887 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1889 | ])# AC_LIBTOOL_DLOPEN
2677 | AC_LIBTOOL_DLOPEN_SELF
4356 | # Whether dlopen is supported.
4357 | dlopen_support=$enable_dlopen
4359 | # Whether dlopen of programs is supported.
4360 | dlopen_self=$enable_dlopen_self
4362 | # Whether dlopen of statically linked programs is supported.
4363 | dlopen_self_static=$enable_dlopen_self_static
4371 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### libclamav/c++/llvm/autoconf/m4/ltdl.m4

```

{% raw %}
77 | AC_REQUIRE([AC_LTDL_SYS_DLOPEN_DEPLIBS])
104 | # AC_LTDL_SYS_DLOPEN_DEPLIBS
106 | AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS],
108 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
109 |   [libltdl_cv_sys_dlopen_deplibs],
110 |   [# PORTME does your system automatically load deplibs for dlopen?
114 |   libltdl_cv_sys_dlopen_deplibs=unknown
119 |     libltdl_cv_sys_dlopen_deplibs=unknown
122 |     libltdl_cv_sys_dlopen_deplibs=yes
127 |     libltdl_cv_sys_dlopen_deplibs=yes
131 |     libltdl_cv_sys_dlopen_deplibs=yes
134 |     libltdl_cv_sys_dlopen_deplibs=yes
137 |     libltdl_cv_sys_dlopen_deplibs=yes
142 |     libltdl_cv_sys_dlopen_deplibs=unknown
146 |     # at 6.2 and later dlopen does load deplibs.
147 |     libltdl_cv_sys_dlopen_deplibs=yes
150 |     libltdl_cv_sys_dlopen_deplibs=yes
153 |     libltdl_cv_sys_dlopen_deplibs=yes
156 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
159 |     libltdl_cv_sys_dlopen_deplibs=no
162 |     # dlopen *does* load deplibs and with the right loader patch applied
168 |     libltdl_cv_sys_dlopen_deplibs=unknown
175 |     libltdl_cv_sys_dlopen_deplibs=yes
178 |     libltdl_cv_sys_dlopen_deplibs=yes
181 |     libltdl_cv_sys_dlopen_deplibs=yes
185 | if test "$libltdl_cv_sys_dlopen_deplibs" != yes; then
186 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
187 |     [Define if the OS needs help to load dependent libraries for dlopen().])
189 | ])# AC_LTDL_SYS_DLOPEN_DEPLIBS
273 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
302 |     [AC_CHECK_LIB([dl], [dlopen],
305 | 	        LIBADD_DL="-ldl" libltdl_cv_lib_dl_dlopen="yes"],
309 |       ]], [[dlopen(0, 0);]])],[AC_DEFINE([HAVE_LIBDL], [1],
310 | 		             [Define if you have the libdl library or equivalent.]) libltdl_cv_func_dlopen="yes"],[AC_CHECK_LIB([svld], [dlopen],
313 | 	            LIBADD_DL="-lsvld" libltdl_cv_func_dlopen="yes"],
328 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
382 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
383 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
389 | 	  _LT_AC_TRY_DLOPEN_SELF(
{% endraw %}

```
### libclamav/c++/m4/libtool.m4

```

{% raw %}
1821 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1824 | m4_defun([_LT_TRY_DLOPEN_SELF],
1882 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1915 | ])# _LT_TRY_DLOPEN_SELF
1918 | # LT_SYS_DLOPEN_SELF
1920 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1922 | if test yes != "$enable_dlopen"; then
1923 |   enable_dlopen=unknown
1924 |   enable_dlopen_self=unknown
1925 |   enable_dlopen_self_static=unknown
1927 |   lt_cv_dlopen=no
1928 |   lt_cv_dlopen_libs=
1932 |     lt_cv_dlopen=load_add_on
1933 |     lt_cv_dlopen_libs=
1934 |     lt_cv_dlopen_self=yes
1938 |     lt_cv_dlopen=LoadLibrary
1939 |     lt_cv_dlopen_libs=
1943 |     lt_cv_dlopen=dlopen
1944 |     lt_cv_dlopen_libs=
1949 |     AC_CHECK_LIB([dl], [dlopen],
1950 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1951 |     lt_cv_dlopen=dyld
1952 |     lt_cv_dlopen_libs=
1953 |     lt_cv_dlopen_self=yes
1960 |     lt_cv_dlopen=dlopen
1961 |     lt_cv_dlopen_libs=
1962 |     lt_cv_dlopen_self=no
1967 | 	  [lt_cv_dlopen=shl_load],
1969 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1970 | 	[AC_CHECK_FUNC([dlopen],
1971 | 	      [lt_cv_dlopen=dlopen],
1972 | 	  [AC_CHECK_LIB([dl], [dlopen],
1973 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1974 | 	    [AC_CHECK_LIB([svld], [dlopen],
1975 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1977 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1986 |   if test no = "$lt_cv_dlopen"; then
1987 |     enable_dlopen=no
1989 |     enable_dlopen=yes
1992 |   case $lt_cv_dlopen in
1993 |   dlopen)
2001 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2003 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2004 | 	  lt_cv_dlopen_self, [dnl
2005 | 	  _LT_TRY_DLOPEN_SELF(
2006 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2007 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2010 |     if test yes = "$lt_cv_dlopen_self"; then
2012 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2013 | 	  lt_cv_dlopen_self_static, [dnl
2014 | 	  _LT_TRY_DLOPEN_SELF(
2015 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2016 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2026 |   case $lt_cv_dlopen_self in
2027 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2028 |   *) enable_dlopen_self=unknown ;;
2031 |   case $lt_cv_dlopen_self_static in
2032 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2033 |   *) enable_dlopen_self_static=unknown ;;
2036 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2037 | 	 [Whether dlopen is supported])
2038 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2039 | 	 [Whether dlopen of programs is supported])
2040 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2041 | 	 [Whether dlopen of statically linked programs is supported])
2042 | ])# LT_SYS_DLOPEN_SELF
2045 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2047 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6122 |     [Compiler flag to allow reflexive dlopens])
6235 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### libclamav/c++/m4/ltoptions.m4

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
### unit_tests/valgrind.supp

```

{% raw %}
102 |    dlopen-libcheck-overread4
106 |    fun:tryall_dlopen
112 |    dlopen-libcheck-overread8
116 |    fun:tryall_dlopen
127 |    fun:lt_dlopen
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1821 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1824 | m4_defun([_LT_TRY_DLOPEN_SELF],
1882 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1915 | ])# _LT_TRY_DLOPEN_SELF
1918 | # LT_SYS_DLOPEN_SELF
1920 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1922 | if test yes != "$enable_dlopen"; then
1923 |   enable_dlopen=unknown
1924 |   enable_dlopen_self=unknown
1925 |   enable_dlopen_self_static=unknown
1927 |   lt_cv_dlopen=no
1928 |   lt_cv_dlopen_libs=
1932 |     lt_cv_dlopen=load_add_on
1933 |     lt_cv_dlopen_libs=
1934 |     lt_cv_dlopen_self=yes
1938 |     lt_cv_dlopen=LoadLibrary
1939 |     lt_cv_dlopen_libs=
1943 |     lt_cv_dlopen=dlopen
1944 |     lt_cv_dlopen_libs=
1949 |     AC_CHECK_LIB([dl], [dlopen],
1950 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1951 |     lt_cv_dlopen=dyld
1952 |     lt_cv_dlopen_libs=
1953 |     lt_cv_dlopen_self=yes
1960 |     lt_cv_dlopen=dlopen
1961 |     lt_cv_dlopen_libs=
1962 |     lt_cv_dlopen_self=no
1967 | 	  [lt_cv_dlopen=shl_load],
1969 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1970 | 	[AC_CHECK_FUNC([dlopen],
1971 | 	      [lt_cv_dlopen=dlopen],
1972 | 	  [AC_CHECK_LIB([dl], [dlopen],
1973 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1974 | 	    [AC_CHECK_LIB([svld], [dlopen],
1975 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1977 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1986 |   if test no = "$lt_cv_dlopen"; then
1987 |     enable_dlopen=no
1989 |     enable_dlopen=yes
1992 |   case $lt_cv_dlopen in
1993 |   dlopen)
2001 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2003 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2004 | 	  lt_cv_dlopen_self, [dnl
2005 | 	  _LT_TRY_DLOPEN_SELF(
2006 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2007 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2010 |     if test yes = "$lt_cv_dlopen_self"; then
2012 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2013 | 	  lt_cv_dlopen_self_static, [dnl
2014 | 	  _LT_TRY_DLOPEN_SELF(
2015 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2016 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2026 |   case $lt_cv_dlopen_self in
2027 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2028 |   *) enable_dlopen_self=unknown ;;
2031 |   case $lt_cv_dlopen_self_static in
2032 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2033 |   *) enable_dlopen_self_static=unknown ;;
2036 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2037 | 	 [Whether dlopen is supported])
2038 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2039 | 	 [Whether dlopen of programs is supported])
2040 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2041 | 	 [Whether dlopen of statically linked programs is supported])
2042 | ])# LT_SYS_DLOPEN_SELF
2045 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2047 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6122 |     [Compiler flag to allow reflexive dlopens])
6235 |   LT_SYS_DLOPEN_SELF
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
### m4/lib-link.m4

```

{% raw %}
472 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### m4/ltdl.m4

```

{% raw %}
199 | 			  _LT_SHELL_INIT([lt_dlopen_dir=$lt_ltdl_dir])],
200 | 	  [nonrecursive], [_LT_SHELL_INIT([lt_dlopen_dir=$lt_ltdl_dir; lt_libobj_prefix=$lt_ltdl_dir/])],
374 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
418 | eval "LTDLOPEN=\"$libname_spec\""
419 | AC_SUBST([LTDLOPEN])
440 | # LT_SYS_DLOPEN_DEPLIBS
442 | AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS],
444 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
445 |   [lt_cv_sys_dlopen_deplibs],
446 |   [# PORTME does your system automatically load deplibs for dlopen?
450 |   lt_cv_sys_dlopen_deplibs=unknown
455 |     lt_cv_sys_dlopen_deplibs=unknown
458 |     lt_cv_sys_dlopen_deplibs=yes
463 |       lt_cv_sys_dlopen_deplibs=no
468 |     lt_cv_sys_dlopen_deplibs=yes
473 |     lt_cv_sys_dlopen_deplibs=yes
476 |     lt_cv_sys_dlopen_deplibs=yes
480 |     lt_cv_sys_dlopen_deplibs=yes
483 |     lt_cv_sys_dlopen_deplibs=yes
486 |     lt_cv_sys_dlopen_deplibs=yes
491 |     lt_cv_sys_dlopen_deplibs=unknown
495 |     # at 6.2 and later dlopen does load deplibs.
496 |     lt_cv_sys_dlopen_deplibs=yes
499 |     lt_cv_sys_dlopen_deplibs=yes
502 |     lt_cv_sys_dlopen_deplibs=yes
505 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
508 |     lt_cv_sys_dlopen_deplibs=no
511 |     # dlopen *does* load deplibs and with the right loader patch applied
517 |     lt_cv_sys_dlopen_deplibs=unknown
524 |     lt_cv_sys_dlopen_deplibs=yes
527 |     lt_cv_sys_dlopen_deplibs=yes
530 |     lt_cv_sys_dlopen_deplibs=yes
533 |     libltdl_cv_sys_dlopen_deplibs=yes
537 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
538 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
539 |     [Define if the OS needs help to load dependent libraries for dlopen().])
541 | ])# LT_SYS_DLOPEN_DEPLIBS
544 | AU_ALIAS([AC_LTDL_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS])
546 | dnl AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [])
635 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
660 | LIBADD_DLOPEN=
661 | AC_SEARCH_LIBS([dlopen], [dl],
664 | 	if test "$ac_cv_search_dlopen" != "none required"; then
665 | 	  LIBADD_DLOPEN=-ldl
667 | 	libltdl_cv_lib_dl_dlopen=yes
668 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
672 |     ]], [[dlopen(0, 0);]])],
675 | 	    libltdl_cv_func_dlopen=yes
676 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
677 | 	[AC_CHECK_LIB([svld], [dlopen],
680 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
681 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
682 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
685 |   LIBS="$LIBS $LIBADD_DLOPEN"
689 | AC_SUBST([LIBADD_DLOPEN])
695 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
699 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
709 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
712 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
716 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
723 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
739 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
804 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
809 |       LIBS="$LIBS $LIBADD_DLOPEN"
867 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
{% endraw %}

```
### libclammspack/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7346 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7414 | 	  # This library was specified with -dlopen.
7534 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7545 | 	passes="conv scan dlopen dlpreopen link"
7571 | 	dlopen) libs=$dlfiles ;;
7602 |       if test dlopen = "$pass"; then
7822 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7823 | 	      # If there is no dlopen support or we're linking statically,
7851 | 	dlopen=
7881 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7927 | 	# This library was specified with -dlopen.
7928 | 	if test dlopen = "$pass"; then
7930 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7932 | 	     test yes != "$dlopen_support" ||
7935 | 	    # If there is no dlname, no dlopen support or we're linking
7944 | 	fi # $pass = dlopen
8000 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8002 | 	      # We recover the dlopen module name by 'saving' the la file
8026 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8155 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8156 | 	  dlopenmodule=
8159 | 	      dlopenmodule=$dlpremoduletest
8163 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8260 | 		    # if the lib is a (non-dlopened) module then we cannot
8264 | 		      if test "X$dlopenmodule" != "X$lib"; then
8416 | 	      echo "*** a static module, that should work as long as the dlopening application"
8417 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8561 |       if test dlopen != "$pass"; then
8691 | 	func_warning "'-dlopen' is ignored for archives"
8758 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9455 | 	    echo "*** a static module, that should work as long as the dlopening"
9456 | 	    echo "*** application is linked with the -dlopen flag."
9474 | 	    echo "*** or is declared to -dlopen it."
10086 | 	func_warning "'-dlopen' is ignored for objects"
10206 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10207 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10888 | # The name that we can dlopen(3).
10917 | # Files to dlopen/dlpreopen
10918 | dlopen='$dlfiles'
{% endraw %}

```
### libclammspack/m4/libtool.m4

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
6140 |     [Compiler flag to allow reflexive dlopens])
6253 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### libclammspack/m4/ltoptions.m4

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
### libltdl/ltdl.h

```cpp

{% raw %}
0 | /* ltdl.h -- generic dlopen functions
75 | /* Portable libltdl versions of the system dlopen() API. */
76 | LT_SCOPE lt_dlhandle lt_dlopen		(const char *filename);
77 | LT_SCOPE lt_dlhandle lt_dlopenext	(const char *filename);
78 | LT_SCOPE lt_dlhandle lt_dlopenadvise	(const char *filename,
133 |   int		ref_count;	/* number of times lt_dlopened minus
{% endraw %}

```
### libltdl/ltdl.c

```cpp

{% raw %}
0 | /* ltdl.c -- system independent dlopen wrapper
132 | static	int	try_dlopen	      (lt_dlhandle *handle,
135 | static	int	tryall_dlopen	      (lt_dlhandle *handle,
175 |    dlopen an application module.  */
214 | #define preloaded_symbols	LT_CONC3(lt_, LTDLOPEN, _LTX_preloaded_symbols)
242 | 	 can use _them_ to lt_dlopen its own modules.  */
251 | 	  errors += lt_dlpreload_open (LT_STR(LTDLOPEN), loader_init_callback);
367 | tryall_dlopen (lt_dlhandle *phandle, const char *filename,
375 |   fprintf (stderr, "tryall_dlopen (%s, %s)\n",
385 |       if ((handle->info.filename == filename) /* dlopen self: 0 == 0 */
492 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
528 |       error += tryall_dlopen_module (handle, (const char *) 0,
531 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
546 |      we want the preopened version of it, even if a dlopenable
548 |   if (old_name && tryall_dlopen (handle, old_name,
560 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
568 | 	  if (tryall_dlopen_module (handle, dir, objdir,
575 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
791 |   /* Try to dlopen the file, but do not continue searching in any
793 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
815 | #if !defined LTDL_DLOPEN_DEPLIBS
823 | #else /* defined LTDL_DLOPEN_DEPLIBS */
952 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
978 | #endif /* defined LTDL_DLOPEN_DEPLIBS */
1158 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1175 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1182 |   /* dlopen self? */
1194 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1313 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1480 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1623 | lt_dlopen (const char *filename)
1625 |   return lt_dlopenadvise (filename, NULL);
1634 | lt_dlopenext (const char *filename)
1640 |     handle = lt_dlopenadvise (filename, advise);
1648 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1668 |       /* Just incase we missed a code path in try_dlopen() that reports
1670 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1679 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1692 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1703 |       errors = try_dlopen (&handle, filename, shared_ext, advise);
1898 |    passing to lt_dlopenext.  The extensions are stripped so that
1901 |    then the same directories that lt_dlopen would search are examined.  */
{% endraw %}

```
### libltdl/Makefile.am

```

{% raw %}
87 | libltdl_la_CPPFLAGS	= -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
93 | libltdlc_la_CPPFLAGS	= -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
102 | EXTRA_LTLIBRARIES	       += dlopen.la \
109 | dlopen_la_SOURCES	= loaders/dlopen.c
110 | dlopen_la_LDFLAGS	= -module -avoid-version
111 | dlopen_la_LIBADD	= $(LIBADD_DLOPEN)
{% endraw %}

```
### libltdl/Makefile.in

```

{% raw %}
217 | dlopen_la_DEPENDENCIES = $(am__DEPENDENCIES_1)
218 | am_dlopen_la_OBJECTS = dlopen.lo
219 | dlopen_la_OBJECTS = $(am_dlopen_la_OBJECTS)
220 | dlopen_la_LINK = $(LIBTOOL) $(AM_V_lt) --tag=CC $(AM_LIBTOOLFLAGS) \
222 | 	$(dlopen_la_LDFLAGS) $(LDFLAGS) -o $@
301 | SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
305 | DIST_SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
431 | LIBADD_DLOPEN = @LIBADD_DLOPEN@
457 | LTDLOPEN = @LTDLOPEN@
589 | EXTRA_LTLIBRARIES = dlopen.la dld_link.la dyld.la load_add_on.la \
619 | libltdl_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
624 | libltdlc_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
628 | dlopen_la_SOURCES = loaders/dlopen.c
629 | dlopen_la_LDFLAGS = -module -avoid-version
630 | dlopen_la_LIBADD = $(LIBADD_DLOPEN)
728 | dlopen.la: $(dlopen_la_OBJECTS) $(dlopen_la_DEPENDENCIES) $(EXTRA_dlopen_la_DEPENDENCIES) 
729 | 	$(AM_V_CCLD)$(dlopen_la_LINK)  $(dlopen_la_OBJECTS) $(dlopen_la_LIBADD) $(LIBS)
756 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/dlopen.Plo@am__quote@
802 | dlopen.lo: loaders/dlopen.c
803 | @am__fastdepCC_TRUE@	$(AM_V_CC)$(LIBTOOL) $(AM_V_lt) --tag=CC $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -MT dlopen.lo -MD -MP -MF $(DEPDIR)/dlopen.Tpo -c -o dlopen.lo `test -f 'loaders/dlopen.c' || echo '$(srcdir)/'`loaders/dlopen.c
804 | @am__fastdepCC_TRUE@	$(AM_V_at)$(am__mv) $(DEPDIR)/dlopen.Tpo $(DEPDIR)/dlopen.Plo
805 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	$(AM_V_CC)source='loaders/dlopen.c' object='dlopen.lo' libtool=yes @AMDEPBACKSLASH@
807 | @am__fastdepCC_FALSE@	$(AM_V_CC@am__nodep@)$(LIBTOOL) $(AM_V_lt) --tag=CC $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -c -o dlopen.lo `test -f 'loaders/dlopen.c' || echo '$(srcdir)/'`loaders/dlopen.c
{% endraw %}

```
### libltdl/loaders/preopen.c

```cpp

{% raw %}
365 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
{% endraw %}

```
### libltdl/loaders/dlopen.c

```cpp

{% raw %}
0 | /* loader-dlopen.c --  dynamic linking with dlopen/dlsym
38 | #define get_vtable	dlopen_LTX_get_vtable
69 |       vtable->name		= "lt_dlopen";
210 |   module = dlopen (filename, module_flags);
{% endraw %}

```
### libltdl/libltdl/lt__private.h

```cpp

{% raw %}
111 |   const lt_dlvtable *	vtable;		/* dlopening interface */
{% endraw %}

```
### libltdl/libltdl/lt_error.h

```cpp

{% raw %}
46 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
{% endraw %}

```
### docs/UserManual/development.md

```

{% raw %}
119 | - `clamscan`/`clamd` will not be able to extract files from RAR archives.  Based on the software license of the unrar library that ClamAV uses, the library can only be dynamically loaded.  ClamAV will attempt to dlopen the unrar library shared object and will continue on without RAR extraction support if the library can't be found (or if it doesn't get built, which is what happens if you indicate that shared libraries should not be built).
{% endraw %}

```
### docs/html/UserManual/development.html

```html

{% raw %}
129 | <li><p><code>clamscan</code>/<code>clamd</code> will not be able to extract files from RAR archives. Based on the software license of the unrar library that ClamAV uses, the library can only be dynamically loaded. ClamAV will attempt to dlopen the unrar library shared object and will continue on without RAR extraction support if the library can't be found (or if it doesn't get built, which is what happens if you indicate that shared libraries should not be built).</p></li>
{% endraw %}

```
### win32/clamav-config.h

```cpp

{% raw %}
432 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
433 | /* #undef LTDL_DLOPEN_DEPLIBS */
{% endraw %}

```
### win32/compat/ltdl.h

```cpp

{% raw %}
31 | lt_dlhandle lt_dlopen(const char *filename);
41 |   int		ref_count;	/* number of times lt_dlopened minus
{% endraw %}

```
### win32/compat/ltdl.c

```cpp

{% raw %}
30 | lt_dlhandle lt_dlopen(const char *filename) {
{% endraw %}

```
### win32/llvmbuild/include/llvm/Config/config.h

```cpp

{% raw %}
5 | /* Define if dlopen(0) will open the symbols of the program */
6 | #undef CAN_DLOPEN_SELF
90 | /* Define if dlopen() is available on this platform. */
91 | #undef HAVE_DLOPEN
520 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
521 | #define LTDL_DLOPEN_DEPLIBS 1
{% endraw %}

```
### win32/3rdparty/libxml2/config.h.in

```

{% raw %}
23 | /* Have dlopen based dso */
24 | #undef HAVE_DLOPEN
{% endraw %}

```
### win32/3rdparty/libxml2/configure.ac

```

{% raw %}
914 |   AC_CHECK_LIB(cygwin, dlopen, [
917 |     AC_DEFINE([HAVE_DLOPEN], [], [Have dlopen based dso])
929 |       AC_CHECK_FUNC(dlopen, libxml_have_dlopen=yes, [
930 |         AC_CHECK_LIB(dl, dlopen, [
932 |           libxml_have_dlopen=yes])])])])
940 |   if test "${libxml_have_dlopen}" = "yes"; then
951 |     AC_DEFINE([HAVE_DLOPEN], [], [Have dlopen based dso])
{% endraw %}

```
### win32/3rdparty/libxml2/xmlmodule.c

```cpp

{% raw %}
205 | #if defined(HAVE_DLOPEN) && !defined(_WIN32)
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
256 | #else /* ! HAVE_DLOPEN */
301 | #endif /* ! HAVE_DLOPEN */
{% endraw %}

```
### win32/3rdparty/libxml2/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### win32/3rdparty/libxml2/os400/wrappers.h

```cpp

{% raw %}
40 | extern void *   _lx_dlopen(const char * filename, int flag);
61 | #define dlopen          _lx_dlopen
{% endraw %}

```
### win32/3rdparty/libxml2/os400/wrappers.c

```cpp

{% raw %}
70 | _lx_dlopen(const char * filename, int flag)
76 |         result = dlopen(xmlTranscodeResult(filename, NULL, &d, NULL), flag);
{% endraw %}

```
### win32/3rdparty/libxml2/os400/config.h.in

```

{% raw %}
24 | /* Have dlopen based dso */
25 | #define HAVE_DLOPEN             1       /* Locally emulated. */
{% endraw %}

```
### win32/3rdparty/libxml2/os400/os400config.h.in

```

{% raw %}
26 | /* Have dlopen based dso */
27 | #define HAVE_DLOPEN             1       /* Locally emulated. */
{% endraw %}

```
### win32/3rdparty/libxml2/os400/dlfcn/dlfcn.h

```cpp

{% raw %}
1 | ***     dlopen(), dlclose() dlsym(), dlerror() emulation for OS/400.
13 | ***     Flags for dlopen().
26 | extern void *           dlopen(const char * filename, int flag);
{% endraw %}

```
### win32/3rdparty/libxml2/os400/dlfcn/dlfcn.c

```cpp

{% raw %}
1 | ***     dlopen(), dlclose() dlsym(), dlerror() emulation for OS/400.
1046 | dlopenqsys(const Qp0l_QSYS_Info_t * dllinfo)
1155 | dlopen(const char * filename, int flag)
1187 |                 dlhandle = dlopenqsys(&dllinfo);
1190 |                 dlhandle = dlopenqsys(&dllinfo);
1192 |                 dlhandle = dlopenqsys(&dllinfo);
1194 |                 dlhandle = dlopenqsys(&dllinfo);
1197 |                 dlhandle = dlopenqsys(&dllinfo);
1200 |                 dlhandle = dlopenqsys(&dllinfo);
1203 |                 dlhandle = dlopenqsys(&dllinfo);
{% endraw %}

```
### win32/3rdparty/libxml2/m4/libtool.m4

```

{% raw %}
1821 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1824 | m4_defun([_LT_TRY_DLOPEN_SELF],
1882 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1915 | ])# _LT_TRY_DLOPEN_SELF
1918 | # LT_SYS_DLOPEN_SELF
1920 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1922 | if test yes != "$enable_dlopen"; then
1923 |   enable_dlopen=unknown
1924 |   enable_dlopen_self=unknown
1925 |   enable_dlopen_self_static=unknown
1927 |   lt_cv_dlopen=no
1928 |   lt_cv_dlopen_libs=
1932 |     lt_cv_dlopen=load_add_on
1933 |     lt_cv_dlopen_libs=
1934 |     lt_cv_dlopen_self=yes
1938 |     lt_cv_dlopen=LoadLibrary
1939 |     lt_cv_dlopen_libs=
1943 |     lt_cv_dlopen=dlopen
1944 |     lt_cv_dlopen_libs=
1949 |     AC_CHECK_LIB([dl], [dlopen],
1950 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1951 |     lt_cv_dlopen=dyld
1952 |     lt_cv_dlopen_libs=
1953 |     lt_cv_dlopen_self=yes
1960 |     lt_cv_dlopen=dlopen
1961 |     lt_cv_dlopen_libs=
1962 |     lt_cv_dlopen_self=no
1967 | 	  [lt_cv_dlopen=shl_load],
1969 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1970 | 	[AC_CHECK_FUNC([dlopen],
1971 | 	      [lt_cv_dlopen=dlopen],
1972 | 	  [AC_CHECK_LIB([dl], [dlopen],
1973 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1974 | 	    [AC_CHECK_LIB([svld], [dlopen],
1975 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1977 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1986 |   if test no = "$lt_cv_dlopen"; then
1987 |     enable_dlopen=no
1989 |     enable_dlopen=yes
1992 |   case $lt_cv_dlopen in
1993 |   dlopen)
2001 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2003 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2004 | 	  lt_cv_dlopen_self, [dnl
2005 | 	  _LT_TRY_DLOPEN_SELF(
2006 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2007 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2010 |     if test yes = "$lt_cv_dlopen_self"; then
2012 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2013 | 	  lt_cv_dlopen_self_static, [dnl
2014 | 	  _LT_TRY_DLOPEN_SELF(
2015 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2016 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2026 |   case $lt_cv_dlopen_self in
2027 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2028 |   *) enable_dlopen_self=unknown ;;
2031 |   case $lt_cv_dlopen_self_static in
2032 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2033 |   *) enable_dlopen_self_static=unknown ;;
2036 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2037 | 	 [Whether dlopen is supported])
2038 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2039 | 	 [Whether dlopen of programs is supported])
2040 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2041 | 	 [Whether dlopen of statically linked programs is supported])
2042 | ])# LT_SYS_DLOPEN_SELF
2045 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2047 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6125 |     [Compiler flag to allow reflexive dlopens])
6238 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### win32/3rdparty/libxml2/m4/ltoptions.m4

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