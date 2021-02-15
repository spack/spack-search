---
name: "mozjs"
layout: package
next_package: libpeas
previous_package: ompt-openmp
languages: ['bash']
---
## 24.2.0
9 / 15846 files match

 - [intl/icu/source/configure.in](#intlicusourceconfigurein)
 - [intl/icu/source/common/putil.cpp](#intlicusourcecommonputilcpp)
 - [js/src/configure.in](#jssrcconfigurein)
 - [js/src/devtools/Instruments.cpp](#jssrcdevtoolsinstrumentscpp)
 - [js/src/ctypes/patches-libffi/03-bug-712594.patch](#jssrcctypespatches-libffi03-bug-712594patch)
 - [js/src/ctypes/libffi/ltmain.sh](#jssrcctypeslibffiltmainsh)
 - [js/src/ctypes/libffi/aclocal.m4](#jssrcctypeslibffiaclocalm4)
 - [js/src/ctypes/libffi/m4/libtool.m4](#jssrcctypeslibffim4libtoolm4)
 - [js/src/ctypes/libffi/m4/ltoptions.m4](#jssrcctypeslibffim4ltoptionsm4)

### intl/icu/source/configure.in

```

{% raw %}
417 |    AC_SEARCH_LIBS([dlopen], [dl])
418 |    AC_CHECK_FUNCS([dlopen])
420 |    if test "x$ac_cv_func_dlopen" != xyes; then
421 |       CONFIG_CPPFLAGS="$CONFIG_CPPFLAGS -DHAVE_DLOPEN=0"
{% endraw %}

```
### intl/icu/source/common/putil.cpp

```

{% raw %}
141 | #    define HAVE_DLOPEN 0
146 | #   ifndef HAVE_DLOPEN
147 | #    define HAVE_DLOPEN 1
155 | #   define HAVE_DLOPEN 0
2111 | #if HAVE_DLOPEN && !U_PLATFORM_USES_ONLY_WIN32_API
2127 |   ret =  dlopen(libName, RTLD_NOW|RTLD_GLOBAL);
2130 |     printf("dlerror on dlopen(%s): %s\n", libName, dlerror());
{% endraw %}

```
### js/src/configure.in

```

{% raw %}
2541 |     AC_SEARCH_LIBS(dlopen, dl,
2543 |         AC_DEFINE(HAVE_DLOPEN)))
{% endraw %}

```
### js/src/devtools/Instruments.cpp

```

{% raw %}
86 |   void *DTPerformanceLibrary = dlopen(DTPerformanceLibraryPath, flags);
88 |     DTPerformanceLibrary = dlopen(OldDTPerformanceLibraryPath, flags);
{% endraw %}

```
### js/src/ctypes/patches-libffi/03-bug-712594.patch

```

{% raw %}
217 | +			  _LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"])],
218 | +	  [nonrecursive], [_LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"; lt_libobj_prefix="$lt_ltdl_dir/"])],
392 | +AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
430 | +LTDLOPEN=`eval "\\$ECHO \"$libname_spec\""`
431 | +AC_SUBST([LTDLOPEN])
452 | +# LT_SYS_DLOPEN_DEPLIBS
454 | +AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS],
456 | +AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
457 | +  [lt_cv_sys_dlopen_deplibs],
458 | +  [# PORTME does your system automatically load deplibs for dlopen?
462 | +  lt_cv_sys_dlopen_deplibs=unknown
467 | +    lt_cv_sys_dlopen_deplibs=unknown
470 | +    lt_cv_sys_dlopen_deplibs=yes
475 | +      lt_cv_sys_dlopen_deplibs=no
482 | +    lt_cv_sys_dlopen_deplibs=yes
485 | +    lt_cv_sys_dlopen_deplibs=yes
489 | +    lt_cv_sys_dlopen_deplibs=yes
492 | +    lt_cv_sys_dlopen_deplibs=yes
495 | +    lt_cv_sys_dlopen_deplibs=yes
500 | +    lt_cv_sys_dlopen_deplibs=unknown
504 | +    # at 6.2 and later dlopen does load deplibs.
505 | +    lt_cv_sys_dlopen_deplibs=yes
508 | +    lt_cv_sys_dlopen_deplibs=yes
511 | +    lt_cv_sys_dlopen_deplibs=yes
514 | +    # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
517 | +    lt_cv_sys_dlopen_deplibs=no
520 | +    # dlopen *does* load deplibs and with the right loader patch applied
526 | +    lt_cv_sys_dlopen_deplibs=unknown
533 | +    lt_cv_sys_dlopen_deplibs=yes
536 | +    lt_cv_sys_dlopen_deplibs=yes
539 | +    lt_cv_sys_dlopen_deplibs=yes
542 | +    libltdl_cv_sys_dlopen_deplibs=yes
546 | +if test "$lt_cv_sys_dlopen_deplibs" != yes; then
547 | + AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
548 | +    [Define if the OS needs help to load dependent libraries for dlopen().])
550 | +])# LT_SYS_DLOPEN_DEPLIBS
553 | +AU_ALIAS([AC_LTDL_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS])
555 | +dnl AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [])
632 | +AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
656 | +LIBADD_DLOPEN=
657 | +AC_SEARCH_LIBS([dlopen], [dl],
660 | +	if test "$ac_cv_search_dlopen" != "none required" ; then
661 | +	  LIBADD_DLOPEN="-ldl"
663 | +	libltdl_cv_lib_dl_dlopen="yes"
664 | +	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
668 | +    ]], [[dlopen(0, 0);]])],
671 | +	    libltdl_cv_func_dlopen="yes"
672 | +	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
673 | +	[AC_CHECK_LIB([svld], [dlopen],
676 | +	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
677 | +		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
678 | +if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
681 | +  LIBS="$LIBS $LIBADD_DLOPEN"
685 | +AC_SUBST([LIBADD_DLOPEN])
691 | +	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
695 | +	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
705 | +	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
708 | +  LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
712 | +  LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
719 | +		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
735 | +LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
797 | +  if test x"$libltdl_cv_func_dlopen" = xyes ||
798 | +     test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
803 | +          LIBS="$LIBS $LIBADD_DLOPEN"
804 | +	  _LT_TRY_DLOPEN_SELF(
994 | @@ -10652,17 +10653,17 @@ if test "${lt_cv_dlopen_self+set}" = set
998 |    lt_cv_dlopen_self=cross
1013 | @@ -10748,17 +10749,17 @@ if test "${lt_cv_dlopen_self_static+set}
1017 |    lt_cv_dlopen_self_static=cross
{% endraw %}

```
### js/src/ctypes/libffi/ltmain.sh

```bash

{% raw %}
737 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
787 |       -dlopen=*|--mode=*|--tag=*)
876 |   # Only execute mode is allowed to have -dlopen flags.
878 |     func_error "unrecognized option \`-dlopen'"
1505 |   -dlopen FILE      add the directory containing FILE to the library path
1507 | This mode sets the library path environment variable according to \`-dlopen'
1560 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1569 |   -module           build a library that can dlopened
1644 |     # Handle -dlopen flags immediately.
1661 | 	# Skip this library if it cannot be dlopened.
1688 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4121 | 	    dlopen_self=$dlopen_self_static
4127 | 	    dlopen_self=$dlopen_self_static
4133 | 	    dlopen_self=$dlopen_self_static
4186 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4270 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4427 |       -dlopen)
4814 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4881 | 	  # This library was specified with -dlopen.
4996 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5007 | 	passes="conv scan dlopen dlpreopen link"
5033 | 	dlopen) libs="$dlfiles" ;;
5059 |       if test "$pass" = dlopen; then
5271 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5272 | 	      # If there is no dlopen support or we're linking statically,
5302 | 	dlopen=
5332 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5372 | 	# This library was specified with -dlopen.
5373 | 	if test "$pass" = dlopen; then
5375 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5378 | 	     test "$dlopen_support" != yes ||
5380 | 	    # If there is no dlname, no dlopen support or we're linking
5389 | 	fi # $pass = dlopen
5447 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5573 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5574 | 	  dlopenmodule=""
5577 | 	      dlopenmodule="$dlpremoduletest"
5581 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5678 | 		    # if the lib is a (non-dlopened) module then we can not
5682 | 		      if test "X$dlopenmodule" != "X$lib"; then
5834 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5835 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5970 |       if test "$pass" != dlopen; then
6069 | 	func_warning "\`-dlopen' is ignored for archives"
6136 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6798 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6799 | 	    $ECHO "*** application is linked with the -dlopen flag."
6817 | 	    $ECHO "*** or is declared to -dlopen it."
7384 | 	func_warning "\`-dlopen' is ignored for objects"
7499 |         && test "$dlopen_support" = unknown \
7500 | 	&& test "$dlopen_self" = unknown \
7501 | 	&& test "$dlopen_self_static" = unknown && \
7502 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8134 | # The name that we can dlopen(3).
8163 | # Files to dlopen/dlpreopen
8164 | dlopen='$dlfiles'
{% endraw %}

```
### js/src/ctypes/libffi/aclocal.m4

```

{% raw %}
1649 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1652 | m4_defun([_LT_TRY_DLOPEN_SELF],
1704 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1733 | ])# _LT_TRY_DLOPEN_SELF
1736 | # LT_SYS_DLOPEN_SELF
1738 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1740 | if test "x$enable_dlopen" != xyes; then
1741 |   enable_dlopen=unknown
1742 |   enable_dlopen_self=unknown
1743 |   enable_dlopen_self_static=unknown
1745 |   lt_cv_dlopen=no
1746 |   lt_cv_dlopen_libs=
1750 |     lt_cv_dlopen="load_add_on"
1751 |     lt_cv_dlopen_libs=
1752 |     lt_cv_dlopen_self=yes
1756 |     lt_cv_dlopen="LoadLibrary"
1757 |     lt_cv_dlopen_libs=
1761 |     lt_cv_dlopen="dlopen"
1762 |     lt_cv_dlopen_libs=
1767 |     AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1769 |     lt_cv_dlopen="dyld"
1770 |     lt_cv_dlopen_libs=
1771 |     lt_cv_dlopen_self=yes
1777 | 	  [lt_cv_dlopen="shl_load"],
1779 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1780 | 	[AC_CHECK_FUNC([dlopen],
1781 | 	      [lt_cv_dlopen="dlopen"],
1782 | 	  [AC_CHECK_LIB([dl], [dlopen],
1783 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1784 | 	    [AC_CHECK_LIB([svld], [dlopen],
1785 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1787 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1796 |   if test "x$lt_cv_dlopen" != xno; then
1797 |     enable_dlopen=yes
1799 |     enable_dlopen=no
1802 |   case $lt_cv_dlopen in
1803 |   dlopen)
1811 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1813 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1814 | 	  lt_cv_dlopen_self, [dnl
1815 | 	  _LT_TRY_DLOPEN_SELF(
1816 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1817 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1820 |     if test "x$lt_cv_dlopen_self" = xyes; then
1822 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1823 | 	  lt_cv_dlopen_self_static, [dnl
1824 | 	  _LT_TRY_DLOPEN_SELF(
1825 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1826 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1836 |   case $lt_cv_dlopen_self in
1837 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1838 |   *) enable_dlopen_self=unknown ;;
1841 |   case $lt_cv_dlopen_self_static in
1842 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1843 |   *) enable_dlopen_self_static=unknown ;;
1846 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1847 | 	 [Whether dlopen is supported])
1848 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1849 | 	 [Whether dlopen of programs is supported])
1850 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1851 | 	 [Whether dlopen of statically linked programs is supported])
1852 | ])# LT_SYS_DLOPEN_SELF
1855 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1857 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5173 |     [Compiler flag to allow reflexive dlopens])
5285 |   LT_SYS_DLOPEN_SELF
7565 | 			  _LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"])],
7566 | 	  [nonrecursive], [_LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"; lt_libobj_prefix="$lt_ltdl_dir/"])],
7740 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
7778 | LTDLOPEN=`eval "\\$ECHO \"$libname_spec\""`
7779 | AC_SUBST([LTDLOPEN])
7800 | # LT_SYS_DLOPEN_DEPLIBS
7802 | AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS],
7804 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
7805 |   [lt_cv_sys_dlopen_deplibs],
7806 |   [# PORTME does your system automatically load deplibs for dlopen?
7810 |   lt_cv_sys_dlopen_deplibs=unknown
7815 |     lt_cv_sys_dlopen_deplibs=unknown
7818 |     lt_cv_sys_dlopen_deplibs=yes
7823 |       lt_cv_sys_dlopen_deplibs=no
7830 |     lt_cv_sys_dlopen_deplibs=yes
7833 |     lt_cv_sys_dlopen_deplibs=yes
7837 |     lt_cv_sys_dlopen_deplibs=yes
7840 |     lt_cv_sys_dlopen_deplibs=yes
7843 |     lt_cv_sys_dlopen_deplibs=yes
7848 |     lt_cv_sys_dlopen_deplibs=unknown
7852 |     # at 6.2 and later dlopen does load deplibs.
7853 |     lt_cv_sys_dlopen_deplibs=yes
7856 |     lt_cv_sys_dlopen_deplibs=yes
7859 |     lt_cv_sys_dlopen_deplibs=yes
7862 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
7865 |     lt_cv_sys_dlopen_deplibs=no
7868 |     # dlopen *does* load deplibs and with the right loader patch applied
7874 |     lt_cv_sys_dlopen_deplibs=unknown
7881 |     lt_cv_sys_dlopen_deplibs=yes
7884 |     lt_cv_sys_dlopen_deplibs=yes
7887 |     lt_cv_sys_dlopen_deplibs=yes
7890 |     libltdl_cv_sys_dlopen_deplibs=yes
7894 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
7895 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
7896 |     [Define if the OS needs help to load dependent libraries for dlopen().])
7898 | ])# LT_SYS_DLOPEN_DEPLIBS
7901 | AU_ALIAS([AC_LTDL_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS])
7903 | dnl AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [])
7980 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
8004 | LIBADD_DLOPEN=
8005 | AC_SEARCH_LIBS([dlopen], [dl],
8008 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
8009 | 	  LIBADD_DLOPEN="-ldl"
8011 | 	libltdl_cv_lib_dl_dlopen="yes"
8012 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
8016 |     ]], [[dlopen(0, 0);]])],
8019 | 	    libltdl_cv_func_dlopen="yes"
8020 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
8021 | 	[AC_CHECK_LIB([svld], [dlopen],
8024 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
8025 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
8026 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
8029 |   LIBS="$LIBS $LIBADD_DLOPEN"
8033 | AC_SUBST([LIBADD_DLOPEN])
8039 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
8043 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
8053 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
8056 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
8060 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
8067 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
8083 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
8145 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
8146 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
8151 |           LIBS="$LIBS $LIBADD_DLOPEN"
8152 | 	  _LT_TRY_DLOPEN_SELF(
8240 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8272 | # dlopen
8274 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8277 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8278 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8281 | put the `dlopen' option into LT_INIT's first parameter.])
8285 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8731 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### js/src/ctypes/libffi/m4/libtool.m4

```

{% raw %}
1634 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1637 | m4_defun([_LT_TRY_DLOPEN_SELF],
1689 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1718 | ])# _LT_TRY_DLOPEN_SELF
1721 | # LT_SYS_DLOPEN_SELF
1723 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1725 | if test "x$enable_dlopen" != xyes; then
1726 |   enable_dlopen=unknown
1727 |   enable_dlopen_self=unknown
1728 |   enable_dlopen_self_static=unknown
1730 |   lt_cv_dlopen=no
1731 |   lt_cv_dlopen_libs=
1735 |     lt_cv_dlopen="load_add_on"
1736 |     lt_cv_dlopen_libs=
1737 |     lt_cv_dlopen_self=yes
1741 |     lt_cv_dlopen="LoadLibrary"
1742 |     lt_cv_dlopen_libs=
1746 |     lt_cv_dlopen="dlopen"
1747 |     lt_cv_dlopen_libs=
1752 |     AC_CHECK_LIB([dl], [dlopen],
1753 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1754 |     lt_cv_dlopen="dyld"
1755 |     lt_cv_dlopen_libs=
1756 |     lt_cv_dlopen_self=yes
1762 | 	  [lt_cv_dlopen="shl_load"],
1764 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1765 | 	[AC_CHECK_FUNC([dlopen],
1766 | 	      [lt_cv_dlopen="dlopen"],
1767 | 	  [AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1769 | 	    [AC_CHECK_LIB([svld], [dlopen],
1770 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1772 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1781 |   if test "x$lt_cv_dlopen" != xno; then
1782 |     enable_dlopen=yes
1784 |     enable_dlopen=no
1787 |   case $lt_cv_dlopen in
1788 |   dlopen)
1796 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1798 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1799 | 	  lt_cv_dlopen_self, [dnl
1800 | 	  _LT_TRY_DLOPEN_SELF(
1801 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1802 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1805 |     if test "x$lt_cv_dlopen_self" = xyes; then
1807 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1808 | 	  lt_cv_dlopen_self_static, [dnl
1809 | 	  _LT_TRY_DLOPEN_SELF(
1810 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1811 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1821 |   case $lt_cv_dlopen_self in
1822 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1823 |   *) enable_dlopen_self=unknown ;;
1826 |   case $lt_cv_dlopen_self_static in
1827 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1828 |   *) enable_dlopen_self_static=unknown ;;
1831 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1832 | 	 [Whether dlopen is supported])
1833 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1834 | 	 [Whether dlopen of programs is supported])
1835 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1836 | 	 [Whether dlopen of statically linked programs is supported])
1837 | ])# LT_SYS_DLOPEN_SELF
1840 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1842 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5158 |     [Compiler flag to allow reflexive dlopens])
5274 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### js/src/ctypes/libffi/m4/ltoptions.m4

```

{% raw %}
69 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
104 | # dlopen
106 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
109 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
110 | [_LT_SET_OPTION([LT_INIT], [dlopen])
113 | put the `dlopen' option into LT_INIT's first parameter.])
117 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```