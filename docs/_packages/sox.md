---
name: "sox"
layout: package
next_package: qscintilla
previous_package: kylin
languages: ['cpp', 'bash']
---
## 14.4.2
13 / 361 files match

 - [configure.ac](#configureac)
 - [ltmain.sh](#ltmainsh)
 - [src/formats.c](#srcformatsc)
 - [src/win32-ltdl.h](#srcwin32-ltdlh)
 - [src/mp3.c](#srcmp3c)
 - [src/ladspa.c](#srcladspac)
 - [src/soxconfig.h.in](#srcsoxconfighin)
 - [src/ladspa.h](#srcladspah)
 - [src/util.c](#srcutilc)
 - [src/win32-ltdl.c](#srcwin32-ltdlc)
 - [src/sox_i.h](#srcsox_ih)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)

### configure.ac

```

{% raw %}
47 | LT_INIT([dlopen win32-dll])
357 |     AC_MSG_CHECKING([whether to dlopen mad])
359 |       AS_HELP_STRING([--enable-dl-mad], [Dlopen mad instead of linking in.]),
363 |       AC_DEFINE(DL_MAD, 1, [Define to dlopen() mad.])
403 |     AC_MSG_CHECKING([whether to dlopen lame])
405 |       AS_HELP_STRING([--enable-dl-lame], [Dlopen lame instead of linking in.]),
409 |       AC_DEFINE(DL_LAME, 1, [Define to dlopen() lame.])
435 |     AC_MSG_CHECKING([whether to dlopen twolame])
437 |       AS_HELP_STRING([--enable-dl-twolame], [Dlopen twolame instead of linking in.]),
441 |       AC_DEFINE(DL_TWOLAME, 1, [Define to dlopen() libtwolame.])
512 | dnl since they will be dlopen()'ed instead.
524 | 			     [Dlopen amrbw instead of linking in.]),
527 |   AC_DEFINE(DL_AMRWB, 1, [Define to dlopen() amrwb.]) 
529 |   dnl to be linked in (since they will be dlopen()'ed instead).
539 | dnl since they will be dlopen()'ed instead.
551 | 			     [Dlopen amrnb instead of linking in.]),
554 |   AC_DEFINE(DL_AMRNB, 1, [Define to dlopen() amrnb.]) 
556 |   dnl to be linked in (since they will be dlopen()'ed instead).
592 | dnl to be linked in (since they will be dlopen()'ed instead).
597 | 			     [Dlopen sndfile instead of linking in.]),
601 |     AC_DEFINE(DL_SNDFILE, 1, [Define to dlopen() sndfile.]) 
603 |     dnl to be linked in (since they will be dlopen()'ed instead).
720 | echo " dlopen amrnb..............$enable_dl_amrnb"
724 | echo " dlopen amrwb..............$enable_dl_amrwb"
736 | echo " dlopen lame...............$enable_dl_lame"
740 | echo " dlopen mad................$enable_dl_mad"
744 | echo " dlopen twolame............$enable_dl_twolame"
750 | echo " dlopen sndfile............$enable_dl_sndfile"
{% endraw %}

```
### ltmain.sh

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
### src/formats.c

```cpp

{% raw %}
1193 |     lt_dlhandle lth = lt_dlopenext(file);
{% endraw %}

```
### src/win32-ltdl.h

```cpp

{% raw %}
47 | lt_dlopen(
51 | lt_dlopenext(
{% endraw %}

```
### src/mp3.c

```cpp

{% raw %}
66 |  * when using dlopen, but also true if linking directly against the DLL if the
{% endraw %}

```
### src/ladspa.c

```cpp

{% raw %}
133 |       || (l_st->lth = lt_dlopenext(l_st->name)) == NULL) {
{% endraw %}

```
### src/soxconfig.h.in

```

{% raw %}
5 | /* Define to dlopen() amrnb. */
8 | /* Define to dlopen() amrwb. */
11 | /* Define to dlopen() lame. */
14 | /* Define to dlopen() mad. */
17 | /* Define to dlopen() sndfile. */
20 | /* Define to dlopen() libtwolame. */
{% endraw %}

```
### src/ladspa.h

```cpp

{% raw %}
66 |    linking by dlopen() and family. The file will provide a number of
{% endraw %}

```
### src/util.c

```cpp

{% raw %}
180 |       dl = lt_dlopenext(*libname);
{% endraw %}

```
### src/win32-ltdl.c

```cpp

{% raw %}
322 | lt_dlopen(
331 | lt_dlopenext(
{% endraw %}

```
### src/sox_i.h

```cpp

{% raw %}
404 |      be used). If using DL_LAME, the func may be loaded via dlopen/dlsym, but
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1750 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1753 | m4_defun([_LT_TRY_DLOPEN_SELF],
1811 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1844 | ])# _LT_TRY_DLOPEN_SELF
1847 | # LT_SYS_DLOPEN_SELF
1849 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1851 | if test "x$enable_dlopen" != xyes; then
1852 |   enable_dlopen=unknown
1853 |   enable_dlopen_self=unknown
1854 |   enable_dlopen_self_static=unknown
1856 |   lt_cv_dlopen=no
1857 |   lt_cv_dlopen_libs=
1861 |     lt_cv_dlopen="load_add_on"
1862 |     lt_cv_dlopen_libs=
1863 |     lt_cv_dlopen_self=yes
1867 |     lt_cv_dlopen="LoadLibrary"
1868 |     lt_cv_dlopen_libs=
1872 |     lt_cv_dlopen="dlopen"
1873 |     lt_cv_dlopen_libs=
1878 |     AC_CHECK_LIB([dl], [dlopen],
1879 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1880 |     lt_cv_dlopen="dyld"
1881 |     lt_cv_dlopen_libs=
1882 |     lt_cv_dlopen_self=yes
1888 | 	  [lt_cv_dlopen="shl_load"],
1890 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1891 | 	[AC_CHECK_FUNC([dlopen],
1892 | 	      [lt_cv_dlopen="dlopen"],
1893 | 	  [AC_CHECK_LIB([dl], [dlopen],
1894 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1895 | 	    [AC_CHECK_LIB([svld], [dlopen],
1896 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1898 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1907 |   if test "x$lt_cv_dlopen" != xno; then
1908 |     enable_dlopen=yes
1910 |     enable_dlopen=no
1913 |   case $lt_cv_dlopen in
1914 |   dlopen)
1922 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1924 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1925 | 	  lt_cv_dlopen_self, [dnl
1926 | 	  _LT_TRY_DLOPEN_SELF(
1927 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1928 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1931 |     if test "x$lt_cv_dlopen_self" = xyes; then
1933 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1934 | 	  lt_cv_dlopen_self_static, [dnl
1935 | 	  _LT_TRY_DLOPEN_SELF(
1936 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1937 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1947 |   case $lt_cv_dlopen_self in
1948 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1949 |   *) enable_dlopen_self=unknown ;;
1952 |   case $lt_cv_dlopen_self_static in
1953 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1954 |   *) enable_dlopen_self_static=unknown ;;
1957 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1958 | 	 [Whether dlopen is supported])
1959 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1960 | 	 [Whether dlopen of programs is supported])
1961 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1962 | 	 [Whether dlopen of statically linked programs is supported])
1963 | ])# LT_SYS_DLOPEN_SELF
1966 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1968 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5668 |     [Compiler flag to allow reflexive dlopens])
5781 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

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