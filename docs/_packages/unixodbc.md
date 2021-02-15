---
name: "unixodbc"
layout: package
next_package: r-nloptr
previous_package: fastjar
languages: ['html', 'cpp', 'bash']
---
## 2.3.4
44 / 845 files match

 - [README.QNX](#readmeqnx)
 - [config.h.in](#confighin)
 - [configure.ac](#configureac)
 - [README.OSX](#readmeosx)
 - [README.VMS](#readmevms)
 - [README.AIX](#readmeaix)
 - [ltmain.sh](#ltmainsh)
 - [exe/dltest.c](#exedltestc)
 - [extras/vms.c](#extrasvmsc)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/ltdl.m4](#m4ltdlm4)
 - [m4/.svn/text-base/ltdl.m4.svn-base](#m4svntext-baseltdlm4svn-base)
 - [m4/.svn/text-base/libtool.m4.svn-base](#m4svntext-baselibtoolm4svn-base)
 - [m4/.svn/text-base/ltoptions.m4.svn-base](#m4svntext-baseltoptionsm4svn-base)
 - [odbcinst/SQLConfigDataSource.c](#odbcinstsqlconfigdatasourcec)
 - [odbcinst/SQLCreateDataSource.c](#odbcinstsqlcreatedatasourcec)
 - [odbcinst/ODBCINSTConstructProperties.c](#odbcinstodbcinstconstructpropertiesc)
 - [odbcinst/SQLConfigDriver.c](#odbcinstsqlconfigdriverc)
 - [odbcinst/_SQLDriverConnectPrompt.c](#odbcinst_sqldriverconnectpromptc)
 - [odbcinst/SQLManageDataSources.c](#odbcinstsqlmanagedatasourcesc)
 - [DriverManager/drivermanager.h](#drivermanagerdrivermanagerh)
 - [DriverManager/__info.c](#drivermanager__infoc)
 - [DriverManager/SQLGetConnectAttrW.c](#drivermanagersqlgetconnectattrwc)
 - [DriverManager/SQLRowCount.c](#drivermanagersqlrowcountc)
 - [DriverManager/SQLAllocHandle.c](#drivermanagersqlallochandlec)
 - [DriverManager/SQLConnect.c](#drivermanagersqlconnectc)
 - [DriverManager/__handles.c](#drivermanager__handlesc)
 - [DriverManager/SQLDisconnect.c](#drivermanagersqldisconnectc)
 - [libltdl/configure.ac](#libltdlconfigureac)
 - [libltdl/ltdl.h](#libltdlltdlh)
 - [libltdl/ltdl.c](#libltdlltdlc)
 - [libltdl/config-h.in](#libltdlconfig-hin)
 - [libltdl/Makefile.am](#libltdlmakefileam)
 - [libltdl/Makefile.in](#libltdlmakefilein)
 - [libltdl/config/ltmain.sh](#libltdlconfigltmainsh)
 - [libltdl/m4/libtool.m4](#libltdlm4libtoolm4)
 - [libltdl/m4/ltoptions.m4](#libltdlm4ltoptionsm4)
 - [libltdl/m4/ltdl.m4](#libltdlm4ltdlm4)
 - [libltdl/loaders/preopen.c](#libltdlloaderspreopenc)
 - [libltdl/loaders/dlopen.c](#libltdlloadersdlopenc)
 - [libltdl/libltdl/lt__private.h](#libltdllibltdllt__privateh)
 - [libltdl/libltdl/lt_error.h](#libltdllibltdllt_errorh)
 - [doc/AdministratorManual/odbcinst.html](#docadministratormanualodbcinsthtml)

### README.QNX

```

{% raw %}
20 | 5. We now need to alter the flags dlopen uses
{% endraw %}

```
### config.h.in

```

{% raw %}
342 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
343 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### configure.ac

```

{% raw %}
139 | LT_INIT([dlopen])
{% endraw %}

```
### README.OSX

```

{% raw %}
17 | 	dlopen type process that unixODBC requires. However help is
{% endraw %}

```
### README.VMS

```

{% raw %}
22 | [.EXTRAS]VMS.C  - Contains OpenVMS specific wrappers (dlopen, etc..)
{% endraw %}

```
### README.AIX

```

{% raw %}
35 | The drivers will be build as a .a, containing a .so, BUT dlopen only is 
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
6155 |       if test "$pass" = dlopen; then
6374 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6375 | 	      # If there is no dlopen support or we're linking statically,
6405 | 	dlopen=
6435 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6481 | 	# This library was specified with -dlopen.
6482 | 	if test "$pass" = dlopen; then
6484 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6487 | 	     test "$dlopen_support" != yes ||
6489 | 	    # If there is no dlname, no dlopen support or we're linking
6498 | 	fi # $pass = dlopen
6554 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6556 | 	      # We recover the dlopen module name by 'saving' the la file
6580 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6709 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6710 | 	  dlopenmodule=""
6713 | 	      dlopenmodule="$dlpremoduletest"
6717 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6814 | 		    # if the lib is a (non-dlopened) module then we can not
6818 | 		      if test "X$dlopenmodule" != "X$lib"; then
6970 | 	      echo "*** a static module, that should work as long as the dlopening application"
6971 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7115 |       if test "$pass" != dlopen; then
7214 | 	func_warning "\`-dlopen' is ignored for archives"
7281 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7960 | 	    echo "*** a static module, that should work as long as the dlopening"
7961 | 	    echo "*** application is linked with the -dlopen flag."
7979 | 	    echo "*** or is declared to -dlopen it."
8590 | 	func_warning "\`-dlopen' is ignored for objects"
8708 |         && test "$dlopen_support" = unknown \
8709 | 	&& test "$dlopen_self" = unknown \
8710 | 	&& test "$dlopen_self_static" = unknown && \
8711 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9392 | # The name that we can dlopen(3).
9421 | # Files to dlopen/dlpreopen
9422 | dlopen='$dlfiles'
{% endraw %}

```
### exe/dltest.c

```cpp

{% raw %}
42 | "*      man page for dlopen to create a       *\n" \
78 |     hDLL = lt_dlopen( argv[1] );
81 | 		printf( "[dltest] ERROR dlopen: %s\n", lt_dlerror() );
{% endraw %}

```
### extras/vms.c

```cpp

{% raw %}
48 | void * lt_dlopen (const char *filename)
246 |      * Adds a path to the list of paths where lt_dlopen will look for shareable images.
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
5677 |     [Compiler flag to allow reflexive dlopens])
5790 |   LT_SYS_DLOPEN_SELF
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
### m4/.svn/text-base/ltdl.m4.svn-base

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
### m4/.svn/text-base/libtool.m4.svn-base

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
5677 |     [Compiler flag to allow reflexive dlopens])
5790 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/.svn/text-base/ltoptions.m4.svn-base

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
### odbcinst/SQLConfigDataSource.c

```cpp

{% raw %}
104 | 		if ( (hDLL = lt_dlopen( szDriverSetup ))  )
{% endraw %}

```
### odbcinst/SQLCreateDataSource.c

```cpp

{% raw %}
203 |     hDLL = lt_dlopen( szNameAndExtension );
217 |         hDLL = lt_dlopen( szPathAndName );
{% endraw %}

```
### odbcinst/ODBCINSTConstructProperties.c

```cpp

{% raw %}
169 | 	if ( !(hDLL = lt_dlopen( szDriverSetup ))  )
{% endraw %}

```
### odbcinst/SQLConfigDriver.c

```cpp

{% raw %}
105 | 		if ( (hDLL = lt_dlopen( szDriverSetup ))  )
{% endraw %}

```
### odbcinst/_SQLDriverConnectPrompt.c

```cpp

{% raw %}
33 |     hDLL = lt_dlopen( szNameAndExtension );
58 |         hDLL = lt_dlopen( szPathAndName );
{% endraw %}

```
### odbcinst/SQLManageDataSources.c

```cpp

{% raw %}
150 |     hDLL = lt_dlopen( szNameAndExtension );
165 |         hDLL = lt_dlopen( szPathAndName );
{% endraw %}

```
### DriverManager/drivermanager.h

```cpp

{% raw %}
138 | 			                            /* some dlopen implemnations where dlsym */
{% endraw %}

```
### DriverManager/__info.c

```cpp

{% raw %}
167 |  * handles in the driver. usage counting in the driver means that dlopen is
{% endraw %}

```
### DriverManager/SQLGetConnectAttrW.c

```cpp

{% raw %}
67 |  * handles in the driver. usage counting in the driver means that dlopen is
{% endraw %}

```
### DriverManager/SQLRowCount.c

```cpp

{% raw %}
57 |  * handles in the driver. usage counting in the driver means that dlopen is
{% endraw %}

```
### DriverManager/SQLAllocHandle.c

```cpp

{% raw %}
74 |  * handles in the driver. usage counting in the driver means that dlopen is
{% endraw %}

```
### DriverManager/SQLConnect.c

```cpp

{% raw %}
232 |  * handles in the driver. usage counting in the driver means that dlopen is
514 |  * Fixed some unchanged dlopen,dlsym,dlclose functions
523 |  * Added support for libtld dlopen replace
810 | static void *odbc_dlopen( char *libname, char **err )
839 |         hand = lt_dlopen( libname );
1068 |      * if pooling then leave the dlopen
1129 |     if ( !(connection -> dl_handle = odbc_dlopen( driver_lib, &err )))
2333 |         if ( !(connection -> cl_handle = odbc_dlopen( name, &err )))
2363 |             if ( !(connection -> cl_handle = odbc_dlopen( name, &err )))
2659 |          * this is safe, because the dlopen function will reuse the handle if we 
2890 |              * this is safe, because the dlopen function will reuse the handle if we 
2947 |              * this is safe, because the dlopen function will reuse the handle if we 
{% endraw %}

```
### DriverManager/__handles.c

```cpp

{% raw %}
68 |  * handles in the driver. usage counting in the driver means that dlopen is
{% endraw %}

```
### DriverManager/SQLDisconnect.c

```cpp

{% raw %}
53 |  * handles in the driver. usage counting in the driver means that dlopen is
{% endraw %}

```
### libltdl/configure.ac

```

{% raw %}
66 | LT_INIT([dlopen win32-dll])
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
### libltdl/config-h.in

```

{% raw %}
117 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
118 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### libltdl/Makefile.am

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
### libltdl/Makefile.in

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
### libltdl/config/ltmain.sh

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
6155 |       if test "$pass" = dlopen; then
6374 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6375 | 	      # If there is no dlopen support or we're linking statically,
6405 | 	dlopen=
6435 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6481 | 	# This library was specified with -dlopen.
6482 | 	if test "$pass" = dlopen; then
6484 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6487 | 	     test "$dlopen_support" != yes ||
6489 | 	    # If there is no dlname, no dlopen support or we're linking
6498 | 	fi # $pass = dlopen
6554 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6556 | 	      # We recover the dlopen module name by 'saving' the la file
6580 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6709 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6710 | 	  dlopenmodule=""
6713 | 	      dlopenmodule="$dlpremoduletest"
6717 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6814 | 		    # if the lib is a (non-dlopened) module then we can not
6818 | 		      if test "X$dlopenmodule" != "X$lib"; then
6970 | 	      echo "*** a static module, that should work as long as the dlopening application"
6971 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7115 |       if test "$pass" != dlopen; then
7214 | 	func_warning "\`-dlopen' is ignored for archives"
7281 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7960 | 	    echo "*** a static module, that should work as long as the dlopening"
7961 | 	    echo "*** application is linked with the -dlopen flag."
7979 | 	    echo "*** or is declared to -dlopen it."
8590 | 	func_warning "\`-dlopen' is ignored for objects"
8708 |         && test "$dlopen_support" = unknown \
8709 | 	&& test "$dlopen_self" = unknown \
8710 | 	&& test "$dlopen_self_static" = unknown && \
8711 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9392 | # The name that we can dlopen(3).
9421 | # Files to dlopen/dlpreopen
9422 | dlopen='$dlfiles'
{% endraw %}

```
### libltdl/m4/libtool.m4

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
5677 |     [Compiler flag to allow reflexive dlopens])
5790 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### libltdl/m4/ltoptions.m4

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
### libltdl/m4/ltdl.m4

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
### libltdl/loaders/preopen.c

```cpp

{% raw %}
353 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
{% endraw %}

```
### libltdl/loaders/dlopen.c

```cpp

{% raw %}
0 | /* loader-dlopen.c --  dynamic linking with dlopen/dlsym
38 | #define get_vtable	dlopen_LTX_get_vtable
69 |       vtable->name		= "lt_dlopen";
193 |   module = dlopen (filename, module_flags);
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
45 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
{% endraw %}

```
### doc/AdministratorManual/odbcinst.html

```html

{% raw %}
98 | to the wrong place the DSN will not work. If the dlopen() fails the DSN will 
{% endraw %}

```