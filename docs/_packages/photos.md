---
name: "photos"
layout: package
next_package: gdb
previous_package: openmolcas
languages: ['bash']
---
## 3.61
5 / 168 files match

 - [aclocal.m4](#aclocalm4)
 - [config/ltmain.sh](#configltmainsh)
 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [autom4te.cache/output.1](#autom4tecacheoutput1)
 - [autom4te.cache/traces.0](#autom4tecachetraces0)

### aclocal.m4

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
7435 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7467 | # dlopen
7469 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7472 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7473 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7476 | put the `dlopen' option into LT_INIT's first parameter.])
7480 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
7926 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### config/ltmain.sh

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
### autom4te.cache/output.0

```

{% raw %}
10753 |         enable_dlopen=no
13951 |   if test "x$enable_dlopen" != xyes; then
13952 |   enable_dlopen=unknown
13953 |   enable_dlopen_self=unknown
13954 |   enable_dlopen_self_static=unknown
13956 |   lt_cv_dlopen=no
13957 |   lt_cv_dlopen_libs=
13961 |     lt_cv_dlopen="load_add_on"
13962 |     lt_cv_dlopen_libs=
13963 |     lt_cv_dlopen_self=yes
13967 |     lt_cv_dlopen="LoadLibrary"
13968 |     lt_cv_dlopen_libs=
13972 |     lt_cv_dlopen="dlopen"
13973 |     lt_cv_dlopen_libs=
13978 |     { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
13979 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
13980 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
13998 | char dlopen ();
14002 | return dlopen ();
14028 |   ac_cv_lib_dl_dlopen=yes
14033 | 	ac_cv_lib_dl_dlopen=no
14041 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
14042 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14043 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
14044 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14047 |     lt_cv_dlopen="dyld"
14048 |     lt_cv_dlopen_libs=
14049 |     lt_cv_dlopen_self=yes
14142 |   lt_cv_dlopen="shl_load"
14210 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
14212 |   { $as_echo "$as_me:$LINENO: checking for dlopen" >&5
14213 | $as_echo_n "checking for dlopen... " >&6; }
14214 | if test "${ac_cv_func_dlopen+set}" = set; then
14223 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
14225 | #define dlopen innocuous_dlopen
14228 |     which can conflict with char dlopen (); below.
14238 | #undef dlopen
14246 | char dlopen ();
14250 | #if defined __stub_dlopen || defined __stub___dlopen
14257 | return dlopen ();
14283 |   ac_cv_func_dlopen=yes
14288 | 	ac_cv_func_dlopen=no
14295 | { $as_echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
14296 | $as_echo "$ac_cv_func_dlopen" >&6; }
14297 | if test "x$ac_cv_func_dlopen" = x""yes; then
14298 |   lt_cv_dlopen="dlopen"
14300 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
14301 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14302 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
14320 | char dlopen ();
14324 | return dlopen ();
14350 |   ac_cv_lib_dl_dlopen=yes
14355 | 	ac_cv_lib_dl_dlopen=no
14363 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
14364 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14365 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
14366 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14368 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
14369 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14370 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
14388 | char dlopen ();
14392 | return dlopen ();
14418 |   ac_cv_lib_svld_dlopen=yes
14423 | 	ac_cv_lib_svld_dlopen=no
14431 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
14432 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14433 | if test "x$ac_cv_lib_svld_dlopen" = x""yes; then
14434 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
14502 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
14523 |   if test "x$lt_cv_dlopen" != xno; then
14524 |     enable_dlopen=yes
14526 |     enable_dlopen=no
14529 |   case $lt_cv_dlopen in
14530 |   dlopen)
14538 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14540 |     { $as_echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
14541 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14542 | if test "${lt_cv_dlopen_self+set}" = set; then
14546 |   lt_cv_dlopen_self=cross
14595 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14618 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14619 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14620 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14624 |     lt_cv_dlopen_self=no
14631 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
14632 | $as_echo "$lt_cv_dlopen_self" >&6; }
14634 |     if test "x$lt_cv_dlopen_self" = xyes; then
14636 |       { $as_echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
14637 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14638 | if test "${lt_cv_dlopen_self_static+set}" = set; then
14642 |   lt_cv_dlopen_self_static=cross
14691 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14714 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14715 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14716 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14720 |     lt_cv_dlopen_self_static=no
14727 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
14728 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14737 |   case $lt_cv_dlopen_self in
14738 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14739 |   *) enable_dlopen_self=unknown ;;
14742 |   case $lt_cv_dlopen_self_static in
14743 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14744 |   *) enable_dlopen_self_static=unknown ;;
21450 | enable_dlopen='`$ECHO "X$enable_dlopen" | $Xsed -e "$delay_single_quote_subst"`'
21451 | enable_dlopen_self='`$ECHO "X$enable_dlopen_self" | $Xsed -e "$delay_single_quote_subst"`'
21452 | enable_dlopen_self_static='`$ECHO "X$enable_dlopen_self_static" | $Xsed -e "$delay_single_quote_subst"`'
22823 | # Whether dlopen is supported.
22824 | dlopen_support=$enable_dlopen
22826 | # Whether dlopen of programs is supported.
22827 | dlopen_self=$enable_dlopen_self
22829 | # Whether dlopen of statically linked programs is supported.
22830 | dlopen_self_static=$enable_dlopen_self_static
22870 | # Compiler flag to allow reflexive dlopens.
23255 | # Compiler flag to allow reflexive dlopens.
23408 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.1

```

{% raw %}
10753 |         enable_dlopen=no
13947 |   if test "x$enable_dlopen" != xyes; then
13948 |   enable_dlopen=unknown
13949 |   enable_dlopen_self=unknown
13950 |   enable_dlopen_self_static=unknown
13952 |   lt_cv_dlopen=no
13953 |   lt_cv_dlopen_libs=
13957 |     lt_cv_dlopen="load_add_on"
13958 |     lt_cv_dlopen_libs=
13959 |     lt_cv_dlopen_self=yes
13963 |     lt_cv_dlopen="LoadLibrary"
13964 |     lt_cv_dlopen_libs=
13968 |     lt_cv_dlopen="dlopen"
13969 |     lt_cv_dlopen_libs=
13974 |     { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
13975 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
13976 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
13994 | char dlopen ();
13998 | return dlopen ();
14024 |   ac_cv_lib_dl_dlopen=yes
14029 | 	ac_cv_lib_dl_dlopen=no
14037 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
14038 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14039 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
14040 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14043 |     lt_cv_dlopen="dyld"
14044 |     lt_cv_dlopen_libs=
14045 |     lt_cv_dlopen_self=yes
14138 |   lt_cv_dlopen="shl_load"
14206 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
14208 |   { $as_echo "$as_me:$LINENO: checking for dlopen" >&5
14209 | $as_echo_n "checking for dlopen... " >&6; }
14210 | if test "${ac_cv_func_dlopen+set}" = set; then
14219 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
14221 | #define dlopen innocuous_dlopen
14224 |     which can conflict with char dlopen (); below.
14234 | #undef dlopen
14242 | char dlopen ();
14246 | #if defined __stub_dlopen || defined __stub___dlopen
14253 | return dlopen ();
14279 |   ac_cv_func_dlopen=yes
14284 | 	ac_cv_func_dlopen=no
14291 | { $as_echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
14292 | $as_echo "$ac_cv_func_dlopen" >&6; }
14293 | if test "x$ac_cv_func_dlopen" = x""yes; then
14294 |   lt_cv_dlopen="dlopen"
14296 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
14297 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
14298 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
14316 | char dlopen ();
14320 | return dlopen ();
14346 |   ac_cv_lib_dl_dlopen=yes
14351 | 	ac_cv_lib_dl_dlopen=no
14359 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
14360 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
14361 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
14362 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
14364 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
14365 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
14366 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
14384 | char dlopen ();
14388 | return dlopen ();
14414 |   ac_cv_lib_svld_dlopen=yes
14419 | 	ac_cv_lib_svld_dlopen=no
14427 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
14428 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
14429 | if test "x$ac_cv_lib_svld_dlopen" = x""yes; then
14430 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
14498 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
14519 |   if test "x$lt_cv_dlopen" != xno; then
14520 |     enable_dlopen=yes
14522 |     enable_dlopen=no
14525 |   case $lt_cv_dlopen in
14526 |   dlopen)
14534 |     LIBS="$lt_cv_dlopen_libs $LIBS"
14536 |     { $as_echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
14537 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
14538 | if test "${lt_cv_dlopen_self+set}" = set; then
14542 |   lt_cv_dlopen_self=cross
14591 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14614 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
14615 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
14616 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
14620 |     lt_cv_dlopen_self=no
14627 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
14628 | $as_echo "$lt_cv_dlopen_self" >&6; }
14630 |     if test "x$lt_cv_dlopen_self" = xyes; then
14632 |       { $as_echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
14633 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
14634 | if test "${lt_cv_dlopen_self_static+set}" = set; then
14638 |   lt_cv_dlopen_self_static=cross
14687 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
14710 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
14711 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
14712 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
14716 |     lt_cv_dlopen_self_static=no
14723 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
14724 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
14733 |   case $lt_cv_dlopen_self in
14734 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
14735 |   *) enable_dlopen_self=unknown ;;
14738 |   case $lt_cv_dlopen_self_static in
14739 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
14740 |   *) enable_dlopen_self_static=unknown ;;
21446 | enable_dlopen='`$ECHO "X$enable_dlopen" | $Xsed -e "$delay_single_quote_subst"`'
21447 | enable_dlopen_self='`$ECHO "X$enable_dlopen_self" | $Xsed -e "$delay_single_quote_subst"`'
21448 | enable_dlopen_self_static='`$ECHO "X$enable_dlopen_self_static" | $Xsed -e "$delay_single_quote_subst"`'
22819 | # Whether dlopen is supported.
22820 | dlopen_support=$enable_dlopen
22822 | # Whether dlopen of programs is supported.
22823 | dlopen_self=$enable_dlopen_self
22825 | # Whether dlopen of statically linked programs is supported.
22826 | dlopen_self_static=$enable_dlopen_self_static
22866 | # Compiler flag to allow reflexive dlopens.
23251 | # Compiler flag to allow reflexive dlopens.
23404 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.0

```

{% raw %}
438 | m4trace:/usr/share/aclocal/libtool.m4:1724: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
439 | if test "x$enable_dlopen" != xyes; then
440 |   enable_dlopen=unknown
441 |   enable_dlopen_self=unknown
442 |   enable_dlopen_self_static=unknown
444 |   lt_cv_dlopen=no
445 |   lt_cv_dlopen_libs=
449 |     lt_cv_dlopen="load_add_on"
450 |     lt_cv_dlopen_libs=
451 |     lt_cv_dlopen_self=yes
455 |     lt_cv_dlopen="LoadLibrary"
456 |     lt_cv_dlopen_libs=
460 |     lt_cv_dlopen="dlopen"
461 |     lt_cv_dlopen_libs=
466 |     AC_CHECK_LIB([dl], [dlopen],
467 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
468 |     lt_cv_dlopen="dyld"
469 |     lt_cv_dlopen_libs=
470 |     lt_cv_dlopen_self=yes
476 | 	  [lt_cv_dlopen="shl_load"],
478 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
479 | 	[AC_CHECK_FUNC([dlopen],
480 | 	      [lt_cv_dlopen="dlopen"],
481 | 	  [AC_CHECK_LIB([dl], [dlopen],
482 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
483 | 	    [AC_CHECK_LIB([svld], [dlopen],
484 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
486 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
495 |   if test "x$lt_cv_dlopen" != xno; then
496 |     enable_dlopen=yes
498 |     enable_dlopen=no
501 |   case $lt_cv_dlopen in
502 |   dlopen)
510 |     LIBS="$lt_cv_dlopen_libs $LIBS"
512 |     AC_CACHE_CHECK([whether a program can dlopen itself],
513 | 	  lt_cv_dlopen_self, [dnl
514 | 	  _LT_TRY_DLOPEN_SELF(
515 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
516 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
519 |     if test "x$lt_cv_dlopen_self" = xyes; then
521 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
522 | 	  lt_cv_dlopen_self_static, [dnl
523 | 	  _LT_TRY_DLOPEN_SELF(
524 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
525 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
535 |   case $lt_cv_dlopen_self in
536 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
537 |   *) enable_dlopen_self=unknown ;;
540 |   case $lt_cv_dlopen_self_static in
541 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
542 |   *) enable_dlopen_self_static=unknown ;;
545 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
546 | 	 [Whether dlopen is supported])
547 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
548 | 	 [Whether dlopen of programs is supported])
549 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
550 | 	 [Whether dlopen of statically linked programs is supported])
552 | m4trace:/usr/share/aclocal/libtool.m4:1841: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
553 | m4trace:/usr/share/aclocal/libtool.m4:1841: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
555 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1014 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1052 | LTDLOPEN=`eval "\\$ECHO \"$libname_spec\""`
1053 | AC_SUBST([LTDLOPEN])
1055 | m4trace:/usr/share/aclocal/ltdl.m4:437: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1056 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1057 |   [lt_cv_sys_dlopen_deplibs],
1058 |   [# PORTME does your system automatically load deplibs for dlopen?
1062 |   lt_cv_sys_dlopen_deplibs=unknown
1067 |     lt_cv_sys_dlopen_deplibs=unknown
1070 |     lt_cv_sys_dlopen_deplibs=yes
1075 |       lt_cv_sys_dlopen_deplibs=no
1082 |     lt_cv_sys_dlopen_deplibs=yes
1085 |     lt_cv_sys_dlopen_deplibs=yes
1089 |     lt_cv_sys_dlopen_deplibs=yes
1092 |     lt_cv_sys_dlopen_deplibs=yes
1095 |     lt_cv_sys_dlopen_deplibs=yes
1100 |     lt_cv_sys_dlopen_deplibs=unknown
1104 |     # at 6.2 and later dlopen does load deplibs.
1105 |     lt_cv_sys_dlopen_deplibs=yes
1108 |     lt_cv_sys_dlopen_deplibs=yes
1111 |     lt_cv_sys_dlopen_deplibs=yes
1114 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1117 |     lt_cv_sys_dlopen_deplibs=no
1120 |     # dlopen *does* load deplibs and with the right loader patch applied
1126 |     lt_cv_sys_dlopen_deplibs=unknown
1133 |     lt_cv_sys_dlopen_deplibs=yes
1136 |     lt_cv_sys_dlopen_deplibs=yes
1139 |     lt_cv_sys_dlopen_deplibs=yes
1142 |     libltdl_cv_sys_dlopen_deplibs=yes
1146 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
1147 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1148 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1151 | m4trace:/usr/share/aclocal/ltdl.m4:536: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1152 | m4trace:/usr/share/aclocal/ltdl.m4:536: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1154 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1213 | LIBADD_DLOPEN=
1214 | AC_SEARCH_LIBS([dlopen], [dl],
1217 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
1218 | 	  LIBADD_DLOPEN="-ldl"
1220 | 	libltdl_cv_lib_dl_dlopen="yes"
1221 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1225 |     ]], [[dlopen(0, 0);]])],
1228 | 	    libltdl_cv_func_dlopen="yes"
1229 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1230 | 	[AC_CHECK_LIB([svld], [dlopen],
1233 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
1234 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1235 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
1238 |   LIBS="$LIBS $LIBADD_DLOPEN"
1242 | AC_SUBST([LIBADD_DLOPEN])
1248 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1252 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1262 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1265 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1269 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1276 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
1292 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
1341 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
1342 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
1347 |           LIBS="$LIBS $LIBADD_DLOPEN"
1348 | 	  _LT_TRY_DLOPEN_SELF(
1366 | m4trace:/usr/share/aclocal/ltoptions.m4:110: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1369 | put the `dlopen' option into LT_INIT's first parameter.])
1371 | m4trace:/usr/share/aclocal/ltoptions.m4:110: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1373 | _LT_SET_OPTION([LT_INIT], [dlopen])
1376 | put the `dlopen' option into LT_INIT's first parameter.])
1468 | m4trace:/usr/share/aclocal/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2358 | m4trace:configure.ac:97: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```