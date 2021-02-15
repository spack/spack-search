---
name: "sst-macro"
layout: package
next_package: cairomm
previous_package: pmdk
languages: ['cpp', 'bash']
---
## 10.1.0
55 / 2421 files match

 - [configure.ac](#configureac)
 - [aclocal.m4](#aclocalm4)
 - [Makefile.in](#makefilein)
 - [bin/ltmain.sh](#binltmainsh)
 - [bin/Makefile.in](#binmakefilein)
 - [sumi-mpi/Makefile.in](#sumi-mpimakefilein)
 - [include/Makefile.in](#includemakefilein)
 - [tests/Makefile.in](#testsmakefilein)
 - [tests/external/Makefile.in](#testsexternalmakefilein)
 - [tests/sumi/Makefile.in](#testssumimakefilein)
 - [tests/api/mpi/Makefile.in](#testsapimpimakefilein)
 - [tests/api/globals/Makefile.in](#testsapiglobalsmakefilein)
 - [sst-dumpi/bin/ltmain.sh](#sst-dumpibinltmainsh)
 - [sst-dumpi/acinclude/libtool.m4](#sst-dumpiacincludelibtoolm4)
 - [sst-dumpi/acinclude/ltoptions.m4](#sst-dumpiacincludeltoptionsm4)
 - [acinclude/libtool.m4](#acincludelibtoolm4)
 - [acinclude/ltoptions.m4](#acincludeltoptionsm4)
 - [acinclude/check_dlopen.m4](#acincludecheck_dlopenm4)
 - [python/Makefile.in](#pythonmakefilein)
 - [configurations/Makefile.in](#configurationsmakefilein)
 - [share/Makefile.in](#sharemakefilein)
 - [sumi/Makefile.in](#sumimakefilein)
 - [skeletons/sst_component_example/component.cc](#skeletonssst_component_examplecomponentcc)
 - [sprockit/Makefile.in](#sprockitmakefilein)
 - [sprockit/test/Makefile.in](#sprockittestmakefilein)
 - [sprockit/sprockit/Makefile.in](#sprockitsprockitmakefilein)
 - [docs/manual/manual.md](#docsmanualmanualmd)
 - [docs/manual/BasicMPITutorial.tex](#docsmanualbasicmpitutorialtex)
 - [sstmac/Makefile.in](#sstmacmakefilein)
 - [sstmac/common/Makefile.in](#sstmaccommonmakefilein)
 - [sstmac/main/loadlib.cc](#sstmacmainloadlibcc)
 - [sstmac/main/Makefile.in](#sstmacmainmakefilein)
 - [sstmac/dumpi_util/Makefile.in](#sstmacdumpi_utilmakefilein)
 - [sstmac/libraries/Makefile.in](#sstmaclibrariesmakefilein)
 - [sstmac/libraries/pthread/Makefile.in](#sstmaclibrariespthreadmakefilein)
 - [sstmac/libraries/omp/Makefile.in](#sstmaclibrariesompmakefilein)
 - [sstmac/libraries/machines/Makefile.in](#sstmaclibrariesmachinesmakefilein)
 - [sstmac/libraries/blas/Makefile.in](#sstmaclibrariesblasmakefilein)
 - [sstmac/software/Makefile.in](#sstmacsoftwaremakefilein)
 - [sstmac/software/launch/app_launcher.cc](#sstmacsoftwarelaunchapp_launchercc)
 - [sstmac/software/process/global.cc](#sstmacsoftwareprocessglobalcc)
 - [sstmac/software/process/app.h](#sstmacsoftwareprocessapph)
 - [sstmac/software/process/app.cc](#sstmacsoftwareprocessappcc)
 - [sstmac/sst_core/Makefile.in](#sstmacsst_coremakefilein)
 - [sstmac/skeletons/Makefile.in](#sstmacskeletonsmakefilein)
 - [sstmac/hardware/Makefile.in](#sstmachardwaremakefilein)
 - [sstmac/install/Makefile.in](#sstmacinstallmakefilein)
 - [sstmac/clang_replacements/Makefile.in](#sstmacclang_replacementsmakefilein)
 - [sstmac/replacements/dlfcn.h](#sstmacreplacementsdlfcnh)
 - [sstmac/replacements/Makefile.in](#sstmacreplacementsmakefilein)
 - [sstmac/test_skeletons/Makefile.in](#sstmactest_skeletonsmakefilein)
 - [sstmac/backends/Makefile.in](#sstmacbackendsmakefilein)
 - [sstmac/backends/common/Makefile.in](#sstmacbackendscommonmakefilein)
 - [sstmac/backends/native/Makefile.in](#sstmacbackendsnativemakefilein)
 - [sstmac/backends/mpi/Makefile.in](#sstmacbackendsmpimakefilein)

### configure.ac

```

{% raw %}
114 | LT_INIT([shared disable-static dlopen])
135 | CHECK_DLOPEN()
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1142 | m4_include([acinclude/check_dlopen.m4])
{% endraw %}

```
### Makefile.in

```

{% raw %}
120 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### bin/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### bin/Makefile.in

```

{% raw %}
141 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sumi-mpi/Makefile.in

```

{% raw %}
121 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### include/Makefile.in

```

{% raw %}
103 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### tests/Makefile.in

```

{% raw %}
281 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### tests/external/Makefile.in

```

{% raw %}
116 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### tests/sumi/Makefile.in

```

{% raw %}
96 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### tests/api/mpi/Makefile.in

```

{% raw %}
99 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### tests/api/globals/Makefile.in

```

{% raw %}
107 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sst-dumpi/bin/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### sst-dumpi/acinclude/libtool.m4

```

{% raw %}
1744 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1747 | m4_defun([_LT_TRY_DLOPEN_SELF],
1805 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1838 | ])# _LT_TRY_DLOPEN_SELF
1841 | # LT_SYS_DLOPEN_SELF
1843 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1845 | if test "x$enable_dlopen" != xyes; then
1846 |   enable_dlopen=unknown
1847 |   enable_dlopen_self=unknown
1848 |   enable_dlopen_self_static=unknown
1850 |   lt_cv_dlopen=no
1851 |   lt_cv_dlopen_libs=
1855 |     lt_cv_dlopen="load_add_on"
1856 |     lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen_self=yes
1861 |     lt_cv_dlopen="LoadLibrary"
1862 |     lt_cv_dlopen_libs=
1866 |     lt_cv_dlopen="dlopen"
1867 |     lt_cv_dlopen_libs=
1872 |     AC_CHECK_LIB([dl], [dlopen],
1873 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1874 |     lt_cv_dlopen="dyld"
1875 |     lt_cv_dlopen_libs=
1876 |     lt_cv_dlopen_self=yes
1882 | 	  [lt_cv_dlopen="shl_load"],
1884 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1885 | 	[AC_CHECK_FUNC([dlopen],
1886 | 	      [lt_cv_dlopen="dlopen"],
1887 | 	  [AC_CHECK_LIB([dl], [dlopen],
1888 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1889 | 	    [AC_CHECK_LIB([svld], [dlopen],
1890 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1892 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1901 |   if test "x$lt_cv_dlopen" != xno; then
1902 |     enable_dlopen=yes
1904 |     enable_dlopen=no
1907 |   case $lt_cv_dlopen in
1908 |   dlopen)
1916 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1918 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1919 | 	  lt_cv_dlopen_self, [dnl
1920 | 	  _LT_TRY_DLOPEN_SELF(
1921 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1922 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1925 |     if test "x$lt_cv_dlopen_self" = xyes; then
1927 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1928 | 	  lt_cv_dlopen_self_static, [dnl
1929 | 	  _LT_TRY_DLOPEN_SELF(
1930 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1931 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1941 |   case $lt_cv_dlopen_self in
1942 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1943 |   *) enable_dlopen_self=unknown ;;
1946 |   case $lt_cv_dlopen_self_static in
1947 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1948 |   *) enable_dlopen_self_static=unknown ;;
1951 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1952 | 	 [Whether dlopen is supported])
1953 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1954 | 	 [Whether dlopen of programs is supported])
1955 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1956 | 	 [Whether dlopen of statically linked programs is supported])
1957 | ])# LT_SYS_DLOPEN_SELF
1960 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1962 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5662 |     [Compiler flag to allow reflexive dlopens])
5775 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### sst-dumpi/acinclude/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### acinclude/libtool.m4

```

{% raw %}
1744 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1747 | m4_defun([_LT_TRY_DLOPEN_SELF],
1805 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1838 | ])# _LT_TRY_DLOPEN_SELF
1841 | # LT_SYS_DLOPEN_SELF
1843 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1845 | if test "x$enable_dlopen" != xyes; then
1846 |   enable_dlopen=unknown
1847 |   enable_dlopen_self=unknown
1848 |   enable_dlopen_self_static=unknown
1850 |   lt_cv_dlopen=no
1851 |   lt_cv_dlopen_libs=
1855 |     lt_cv_dlopen="load_add_on"
1856 |     lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen_self=yes
1861 |     lt_cv_dlopen="LoadLibrary"
1862 |     lt_cv_dlopen_libs=
1866 |     lt_cv_dlopen="dlopen"
1867 |     lt_cv_dlopen_libs=
1872 |     AC_CHECK_LIB([dl], [dlopen],
1873 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1874 |     lt_cv_dlopen="dyld"
1875 |     lt_cv_dlopen_libs=
1876 |     lt_cv_dlopen_self=yes
1882 | 	  [lt_cv_dlopen="shl_load"],
1884 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1885 | 	[AC_CHECK_FUNC([dlopen],
1886 | 	      [lt_cv_dlopen="dlopen"],
1887 | 	  [AC_CHECK_LIB([dl], [dlopen],
1888 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1889 | 	    [AC_CHECK_LIB([svld], [dlopen],
1890 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1892 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1901 |   if test "x$lt_cv_dlopen" != xno; then
1902 |     enable_dlopen=yes
1904 |     enable_dlopen=no
1907 |   case $lt_cv_dlopen in
1908 |   dlopen)
1916 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1918 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1919 | 	  lt_cv_dlopen_self, [dnl
1920 | 	  _LT_TRY_DLOPEN_SELF(
1921 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1922 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1925 |     if test "x$lt_cv_dlopen_self" = xyes; then
1927 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1928 | 	  lt_cv_dlopen_self_static, [dnl
1929 | 	  _LT_TRY_DLOPEN_SELF(
1930 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1931 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1941 |   case $lt_cv_dlopen_self in
1942 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1943 |   *) enable_dlopen_self=unknown ;;
1946 |   case $lt_cv_dlopen_self_static in
1947 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1948 |   *) enable_dlopen_self_static=unknown ;;
1951 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1952 | 	 [Whether dlopen is supported])
1953 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1954 | 	 [Whether dlopen of programs is supported])
1955 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1956 | 	 [Whether dlopen of statically linked programs is supported])
1957 | ])# LT_SYS_DLOPEN_SELF
1960 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1962 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5662 |     [Compiler flag to allow reflexive dlopens])
5775 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### acinclude/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### acinclude/check_dlopen.m4

```

{% raw %}
1 | AC_DEFUN([CHECK_DLOPEN], [
5 | AC_CHECK_LIB([dl], [dlopen], [],
{% endraw %}

```
### python/Makefile.in

```

{% raw %}
115 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### configurations/Makefile.in

```

{% raw %}
103 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### share/Makefile.in

```

{% raw %}
92 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sumi/Makefile.in

```

{% raw %}
116 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### skeletons/sst_component_example/component.cc

```cpp

{% raw %}
70 |  * SST will look for this module information after loading libtest.so using dlopen
71 |  * dlopen of libtest.so is triggered by running 'import sst.test'
{% endraw %}

```
### sprockit/Makefile.in

```

{% raw %}
101 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sprockit/test/Makefile.in

```

{% raw %}
115 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sprockit/sprockit/Makefile.in

```

{% raw %}
141 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### docs/manual/manual.md

```

{% raw %}
1481 | While MPI would have produced an executable, SST works by loading shared object files using `dlopen`.
1483 | Using `dlopen` tricks, SST finds the main function in the .so file and calls it to spawn the skeleton app.
{% endraw %}

```
### docs/manual/BasicMPITutorial.tex

```

{% raw %}
41 | While MPI would have produced an executable, SST works by loading shared object files using \inlinecode{dlopen}.
43 | Using \inlinecode{dlopen} tricks, SST finds the main function in the .so file and calls it to spawn the skeleton app.
{% endraw %}

```
### sstmac/Makefile.in

```

{% raw %}
103 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/common/Makefile.in

```

{% raw %}
123 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/main/loadlib.cc

```cpp

{% raw %}
105 |   // from dlopen, which is a useful error message for the user.
106 |   void* handle = dlopen(fullpath.c_str(), RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```
### sstmac/main/Makefile.in

```

{% raw %}
116 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/dumpi_util/Makefile.in

```

{% raw %}
116 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/libraries/Makefile.in

```

{% raw %}
103 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/libraries/pthread/Makefile.in

```

{% raw %}
117 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/libraries/omp/Makefile.in

```

{% raw %}
115 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/libraries/machines/Makefile.in

```

{% raw %}
116 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/libraries/blas/Makefile.in

```

{% raw %}
116 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/software/Makefile.in

```

{% raw %}
142 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/software/launch/app_launcher.cc

```cpp

{% raw %}
81 |     App::dlopenCheck(lreq->aid(), app_params);
{% endraw %}

```
### sstmac/software/process/global.cc

```cpp

{% raw %}
190 | extern "C" void *sstmac_dlopen(const char* filename, int flag)
192 |   void* ret = dlopen(filename, flag);
{% endraw %}

```
### sstmac/software/process/app.h

```cpp

{% raw %}
229 |   static void dlopenCheck(int aid, SST::Params& params, bool check_name = true);
233 |   static void lockDlopen(int aid);
235 |   static void unlockDlopen(int aid);
295 |   struct dlopen_entry {
300 |     dlopen_entry() : handle(nullptr), refcount(0), loaded(false) {}
303 |   static std::map<int, dlopen_entry> dlopens_;
{% endraw %}

```
### sstmac/software/process/app.cc

```cpp

{% raw %}
113 | std::map<int, App::dlopen_entry> App::dlopens_;
145 | static thread_lock dlopen_lock;
148 | App::lockDlopen(int aid)
150 |   dlopen_entry& entry = dlopens_[aid];
155 | App::unlockDlopen(int aid)
161 | App::dlopenCheck(int aid, SST::Params& params, bool check_name)
164 |     dlopen_lock.lock();
166 |     dlopen_entry& entry = dlopens_[aid];
194 |     dlopen_lock.unlock();
203 |   dlopen_lock.lock();
204 |   auto iter = dlopens_.find(aid);
205 |   if (iter != dlopens_.end()){
206 |     dlopen_entry& entry = iter->second;
210 |       dlopens_.erase(iter);
213 |   dlopen_lock.unlock();
{% endraw %}

```
### sstmac/sst_core/Makefile.in

```

{% raw %}
119 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/skeletons/Makefile.in

```

{% raw %}
134 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/hardware/Makefile.in

```

{% raw %}
139 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/install/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/clang_replacements/Makefile.in

```

{% raw %}
103 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/replacements/dlfcn.h

```cpp

{% raw %}
49 | #define dlopen sstmac_dlopen
55 | void *sstmac_dlopen(const char *filename, int flag);
{% endraw %}

```
### sstmac/replacements/Makefile.in

```

{% raw %}
159 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/test_skeletons/Makefile.in

```

{% raw %}
116 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/backends/Makefile.in

```

{% raw %}
114 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/backends/common/Makefile.in

```

{% raw %}
116 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/backends/native/Makefile.in

```

{% raw %}
125 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```
### sstmac/backends/mpi/Makefile.in

```

{% raw %}
123 | 	$(top_srcdir)/acinclude/check_dlopen.m4 \
{% endraw %}

```