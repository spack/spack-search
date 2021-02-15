---
name: "spot"
layout: package
next_package: flex
previous_package: ding-libs
languages: ['cpp', 'bash']
---
## 1.2.6
23 / 4036 files match

 - [config.h.in](#confighin)
 - [iface/dve2/dve2.cc](#ifacedve2dve2cc)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/ltdl.m4](#m4ltdlm4)
 - [buddy/m4/libtool.m4](#buddym4libtoolm4)
 - [buddy/m4/ltoptions.m4](#buddym4ltoptionsm4)
 - [buddy/tools/ltmain.sh](#buddytoolsltmainsh)
 - [tools/ltmain.sh](#toolsltmainsh)
 - [ltdl/configure.ac](#ltdlconfigureac)
 - [ltdl/ltdl.h](#ltdlltdlh)
 - [ltdl/ltdl.c](#ltdlltdlc)
 - [ltdl/config-h.in](#ltdlconfig-hin)
 - [ltdl/Makefile.am](#ltdlmakefileam)
 - [ltdl/Makefile.in](#ltdlmakefilein)
 - [ltdl/config/ltmain.sh](#ltdlconfigltmainsh)
 - [ltdl/m4/libtool.m4](#ltdlm4libtoolm4)
 - [ltdl/m4/ltoptions.m4](#ltdlm4ltoptionsm4)
 - [ltdl/m4/ltdl.m4](#ltdlm4ltdlm4)
 - [ltdl/loaders/preopen.c](#ltdlloaderspreopenc)
 - [ltdl/loaders/dlopen.c](#ltdlloadersdlopenc)
 - [ltdl/libltdl/lt__private.h](#ltdllibltdllt__privateh)
 - [ltdl/libltdl/lt_error.h](#ltdllibltdllt_errorh)

### config.h.in

```

{% raw %}
1177 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
1178 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### iface/dve2/dve2.cc

```cpp

{% raw %}
1020 |     lt_dlhandle h = lt_dlopen(file.c_str());
{% endraw %}

```
### m4/libtool.m4

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
5658 |     [Compiler flag to allow reflexive dlopens])
5771 |   LT_SYS_DLOPEN_SELF
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
### m4/ltdl.m4

```

{% raw %}
199 | 			  _LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"])],
200 | 	  [nonrecursive], [_LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"; lt_libobj_prefix="$lt_ltdl_dir/"])],
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
470 |     lt_cv_sys_dlopen_deplibs=yes
473 |     lt_cv_sys_dlopen_deplibs=yes
477 |     lt_cv_sys_dlopen_deplibs=yes
480 |     lt_cv_sys_dlopen_deplibs=yes
483 |     lt_cv_sys_dlopen_deplibs=yes
488 |     lt_cv_sys_dlopen_deplibs=unknown
492 |     # at 6.2 and later dlopen does load deplibs.
493 |     lt_cv_sys_dlopen_deplibs=yes
496 |     lt_cv_sys_dlopen_deplibs=yes
499 |     lt_cv_sys_dlopen_deplibs=yes
502 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
505 |     lt_cv_sys_dlopen_deplibs=no
508 |     # dlopen *does* load deplibs and with the right loader patch applied
514 |     lt_cv_sys_dlopen_deplibs=unknown
521 |     lt_cv_sys_dlopen_deplibs=yes
524 |     lt_cv_sys_dlopen_deplibs=yes
527 |     lt_cv_sys_dlopen_deplibs=yes
530 |     libltdl_cv_sys_dlopen_deplibs=yes
534 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
535 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
536 |     [Define if the OS needs help to load dependent libraries for dlopen().])
538 | ])# LT_SYS_DLOPEN_DEPLIBS
541 | AU_ALIAS([AC_LTDL_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS])
543 | dnl AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [])
627 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
651 | LIBADD_DLOPEN=
652 | AC_SEARCH_LIBS([dlopen], [dl],
655 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
656 | 	  LIBADD_DLOPEN="-ldl"
658 | 	libltdl_cv_lib_dl_dlopen="yes"
659 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
663 |     ]], [[dlopen(0, 0);]])],
666 | 	    libltdl_cv_func_dlopen="yes"
667 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
668 | 	[AC_CHECK_LIB([svld], [dlopen],
671 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
672 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
673 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
676 |   LIBS="$LIBS $LIBADD_DLOPEN"
680 | AC_SUBST([LIBADD_DLOPEN])
686 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
690 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
700 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
703 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
707 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
714 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
730 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
792 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
793 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
798 |           LIBS="$LIBS $LIBADD_DLOPEN"
799 | 	  _LT_TRY_DLOPEN_SELF(
{% endraw %}

```
### buddy/m4/libtool.m4

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
5658 |     [Compiler flag to allow reflexive dlopens])
5771 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### buddy/m4/ltoptions.m4

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
### buddy/tools/ltmain.sh

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
### tools/ltmain.sh

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
### ltdl/configure.ac

```

{% raw %}
66 | LT_INIT([dlopen win32-dll])
{% endraw %}

```
### ltdl/ltdl.h

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
### ltdl/ltdl.c

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
485 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
521 |       error += tryall_dlopen_module (handle, (const char *) 0,
524 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
539 |      we want the preopened version of it, even if a dlopenable
541 |   if (old_name && tryall_dlopen (handle, old_name,
553 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
561 | 	  if (tryall_dlopen_module (handle, dir, objdir,
568 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
784 |   /* Try to dlopen the file, but do not continue searching in any
786 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
808 | #if !defined(LTDL_DLOPEN_DEPLIBS)
816 | #else /* defined(LTDL_DLOPEN_DEPLIBS) */
945 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
971 | #endif /* defined(LTDL_DLOPEN_DEPLIBS) */
1151 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1168 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1175 |   /* dlopen self? */
1187 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1306 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1473 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1616 | lt_dlopen (const char *filename)
1618 |   return lt_dlopenadvise (filename, NULL);
1627 | lt_dlopenext (const char *filename)
1633 |     handle = lt_dlopenadvise (filename, advise);
1641 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1661 |       /* Just incase we missed a code path in try_dlopen() that reports
1663 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1672 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1685 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1696 |       errors = try_dlopen (&handle, filename, shared_ext, advise);
1891 |    passing to lt_dlopenext.  The extensions are stripped so that
1894 |    then the same directories that lt_dlopen would search are examined.  */
{% endraw %}

```
### ltdl/config-h.in

```

{% raw %}
117 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
118 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### ltdl/Makefile.am

```

{% raw %}
86 | libltdl_la_CPPFLAGS	= -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
92 | libltdlc_la_CPPFLAGS	= -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
101 | EXTRA_LTLIBRARIES	       += dlopen.la \
108 | dlopen_la_SOURCES	= loaders/dlopen.c
109 | dlopen_la_LDFLAGS	= -module -avoid-version
110 | dlopen_la_LIBADD 	= $(LIBADD_DLOPEN)
{% endraw %}

```
### ltdl/Makefile.in

```

{% raw %}
95 | dlopen_la_DEPENDENCIES = $(am__DEPENDENCIES_1)
96 | am_dlopen_la_OBJECTS = dlopen.lo
97 | dlopen_la_OBJECTS = $(am_dlopen_la_OBJECTS)
98 | dlopen_la_LINK = $(LIBTOOL) --tag=CC $(AM_LIBTOOLFLAGS) \
100 | 	$(dlopen_la_LDFLAGS) $(LDFLAGS) -o $@
155 | SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
159 | DIST_SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
216 | LIBADD_DLOPEN = @LIBADD_DLOPEN@
223 | LTDLOPEN = @LTDLOPEN@
316 | EXTRA_LTLIBRARIES = dlopen.la dld_link.la dyld.la load_add_on.la \
347 | libltdl_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
352 | libltdlc_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
356 | dlopen_la_SOURCES = loaders/dlopen.c
357 | dlopen_la_LDFLAGS = -module -avoid-version
358 | dlopen_la_LIBADD = $(LIBADD_DLOPEN)
469 | dlopen.la: $(dlopen_la_OBJECTS) $(dlopen_la_DEPENDENCIES) 
470 | 	$(dlopen_la_LINK)  $(dlopen_la_OBJECTS) $(dlopen_la_LIBADD) $(LIBS)
494 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/dlopen.Plo@am__quote@
540 | dlopen.lo: loaders/dlopen.c
541 | @am__fastdepCC_TRUE@	$(LIBTOOL)  --tag=CC $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -MT dlopen.lo -MD -MP -MF $(DEPDIR)/dlopen.Tpo -c -o dlopen.lo `test -f 'loaders/dlopen.c' || echo '$(srcdir)/'`loaders/dlopen.c
542 | @am__fastdepCC_TRUE@	$(am__mv) $(DEPDIR)/dlopen.Tpo $(DEPDIR)/dlopen.Plo
543 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	source='loaders/dlopen.c' object='dlopen.lo' libtool=yes @AMDEPBACKSLASH@
545 | @am__fastdepCC_FALSE@	$(LIBTOOL)  --tag=CC $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -c -o dlopen.lo `test -f 'loaders/dlopen.c' || echo '$(srcdir)/'`loaders/dlopen.c
{% endraw %}

```
### ltdl/config/ltmain.sh

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
### ltdl/m4/libtool.m4

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
5658 |     [Compiler flag to allow reflexive dlopens])
5771 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### ltdl/m4/ltoptions.m4

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
### ltdl/m4/ltdl.m4

```

{% raw %}
199 | 			  _LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"])],
200 | 	  [nonrecursive], [_LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"; lt_libobj_prefix="$lt_ltdl_dir/"])],
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
470 |     lt_cv_sys_dlopen_deplibs=yes
473 |     lt_cv_sys_dlopen_deplibs=yes
477 |     lt_cv_sys_dlopen_deplibs=yes
480 |     lt_cv_sys_dlopen_deplibs=yes
483 |     lt_cv_sys_dlopen_deplibs=yes
488 |     lt_cv_sys_dlopen_deplibs=unknown
492 |     # at 6.2 and later dlopen does load deplibs.
493 |     lt_cv_sys_dlopen_deplibs=yes
496 |     lt_cv_sys_dlopen_deplibs=yes
499 |     lt_cv_sys_dlopen_deplibs=yes
502 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
505 |     lt_cv_sys_dlopen_deplibs=no
508 |     # dlopen *does* load deplibs and with the right loader patch applied
514 |     lt_cv_sys_dlopen_deplibs=unknown
521 |     lt_cv_sys_dlopen_deplibs=yes
524 |     lt_cv_sys_dlopen_deplibs=yes
527 |     lt_cv_sys_dlopen_deplibs=yes
530 |     libltdl_cv_sys_dlopen_deplibs=yes
534 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
535 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
536 |     [Define if the OS needs help to load dependent libraries for dlopen().])
538 | ])# LT_SYS_DLOPEN_DEPLIBS
541 | AU_ALIAS([AC_LTDL_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS])
543 | dnl AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [])
627 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
651 | LIBADD_DLOPEN=
652 | AC_SEARCH_LIBS([dlopen], [dl],
655 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
656 | 	  LIBADD_DLOPEN="-ldl"
658 | 	libltdl_cv_lib_dl_dlopen="yes"
659 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
663 |     ]], [[dlopen(0, 0);]])],
666 | 	    libltdl_cv_func_dlopen="yes"
667 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
668 | 	[AC_CHECK_LIB([svld], [dlopen],
671 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
672 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
673 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
676 |   LIBS="$LIBS $LIBADD_DLOPEN"
680 | AC_SUBST([LIBADD_DLOPEN])
686 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
690 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
700 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
703 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
707 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
714 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
730 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
792 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
793 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
798 |           LIBS="$LIBS $LIBADD_DLOPEN"
799 | 	  _LT_TRY_DLOPEN_SELF(
{% endraw %}

```
### ltdl/loaders/preopen.c

```cpp

{% raw %}
353 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
{% endraw %}

```
### ltdl/loaders/dlopen.c

```cpp

{% raw %}
0 | /* loader-dlopen.c --  dynamic linking with dlopen/dlsym
38 | #define get_vtable	dlopen_LTX_get_vtable
69 |       vtable->name		= "lt_dlopen";
193 |   module = dlopen (filename, module_flags);
{% endraw %}

```
### ltdl/libltdl/lt__private.h

```cpp

{% raw %}
111 |   const lt_dlvtable *	vtable;		/* dlopening interface */
{% endraw %}

```
### ltdl/libltdl/lt_error.h

```cpp

{% raw %}
45 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
{% endraw %}

```