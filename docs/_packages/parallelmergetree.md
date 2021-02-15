---
name: "parallelmergetree"
layout: package
next_package: py-4suite-xml
previous_package: otf
languages: ['bash']
---
## develop
5 / 199 files match

 - [diy/src/bil-0.6.0/ltmain.sh](#diysrcbil-060ltmainsh)
 - [diy/src/bil-0.6.0/aclocal.m4](#diysrcbil-060aclocalm4)
 - [diy/src/bil-0.6.0/autom4te.cache/output.0](#diysrcbil-060autom4tecacheoutput0)
 - [diy/src/bil-0.6.0/autom4te.cache/output.1](#diysrcbil-060autom4tecacheoutput1)
 - [diy/src/bil-0.6.0/autom4te.cache/traces.0](#diysrcbil-060autom4tecachetraces0)

### diy/src/bil-0.6.0/ltmain.sh

```bash

{% raw %}
737 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
787 |       -dlopen=*|--mode=*|--tag=*)
876 |   # Only execute mode is allowed to have -dlopen flags.
878 |     func_error "unrecognized option \`-dlopen'"
1504 |   -dlopen FILE      add the directory containing FILE to the library path
1506 | This mode sets the library path environment variable according to \`-dlopen'
1559 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1568 |   -module           build a library that can dlopened
1643 |     # Handle -dlopen flags immediately.
1660 | 	# Skip this library if it cannot be dlopened.
1687 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
3603 | 	    dlopen_self=$dlopen_self_static
3609 | 	    dlopen_self=$dlopen_self_static
3615 | 	    dlopen_self=$dlopen_self_static
3668 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
3752 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3909 |       -dlopen)
4287 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4354 | 	  # This library was specified with -dlopen.
4469 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
4480 | 	passes="conv scan dlopen dlpreopen link"
4506 | 	dlopen) libs="$dlfiles" ;;
4532 |       if test "$pass" = dlopen; then
4744 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
4745 | 	      # If there is no dlopen support or we're linking statically,
4775 | 	dlopen=
4805 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
4845 | 	# This library was specified with -dlopen.
4846 | 	if test "$pass" = dlopen; then
4848 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
4851 | 	     test "$dlopen_support" != yes ||
4853 | 	    # If there is no dlname, no dlopen support or we're linking
4862 | 	fi # $pass = dlopen
4920 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5046 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5047 | 	  dlopenmodule=""
5050 | 	      dlopenmodule="$dlpremoduletest"
5054 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5151 | 		    # if the lib is a (non-dlopened) module then we can not
5155 | 		      if test "X$dlopenmodule" != "X$lib"; then
5307 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5308 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5443 |       if test "$pass" != dlopen; then
5542 | 	func_warning "\`-dlopen' is ignored for archives"
5609 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6271 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6272 | 	    $ECHO "*** application is linked with the -dlopen flag."
6290 | 	    $ECHO "*** or is declared to -dlopen it."
6857 | 	func_warning "\`-dlopen' is ignored for objects"
6972 |         && test "$dlopen_support" = unknown \
6973 | 	&& test "$dlopen_self" = unknown \
6974 | 	&& test "$dlopen_self_static" = unknown && \
6975 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
7602 | # The name that we can dlopen(3).
7631 | # Files to dlopen/dlpreopen
7632 | dlopen='$dlfiles'
{% endraw %}

```
### diy/src/bil-0.6.0/aclocal.m4

```

{% raw %}
1642 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1645 | m4_defun([_LT_TRY_DLOPEN_SELF],
1701 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1730 | ])# _LT_TRY_DLOPEN_SELF
1733 | # LT_SYS_DLOPEN_SELF
1735 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1737 | if test "x$enable_dlopen" != xyes; then
1738 |   enable_dlopen=unknown
1739 |   enable_dlopen_self=unknown
1740 |   enable_dlopen_self_static=unknown
1742 |   lt_cv_dlopen=no
1743 |   lt_cv_dlopen_libs=
1747 |     lt_cv_dlopen="load_add_on"
1748 |     lt_cv_dlopen_libs=
1749 |     lt_cv_dlopen_self=yes
1753 |     lt_cv_dlopen="LoadLibrary"
1754 |     lt_cv_dlopen_libs=
1758 |     lt_cv_dlopen="dlopen"
1759 |     lt_cv_dlopen_libs=
1764 |     AC_CHECK_LIB([dl], [dlopen],
1765 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1766 |     lt_cv_dlopen="dyld"
1767 |     lt_cv_dlopen_libs=
1768 |     lt_cv_dlopen_self=yes
1774 | 	  [lt_cv_dlopen="shl_load"],
1776 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1777 | 	[AC_CHECK_FUNC([dlopen],
1778 | 	      [lt_cv_dlopen="dlopen"],
1779 | 	  [AC_CHECK_LIB([dl], [dlopen],
1780 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1781 | 	    [AC_CHECK_LIB([svld], [dlopen],
1782 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1784 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1793 |   if test "x$lt_cv_dlopen" != xno; then
1794 |     enable_dlopen=yes
1796 |     enable_dlopen=no
1799 |   case $lt_cv_dlopen in
1800 |   dlopen)
1808 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1810 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1811 | 	  lt_cv_dlopen_self, [dnl
1812 | 	  _LT_TRY_DLOPEN_SELF(
1813 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1814 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1817 |     if test "x$lt_cv_dlopen_self" = xyes; then
1819 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1820 | 	  lt_cv_dlopen_self_static, [dnl
1821 | 	  _LT_TRY_DLOPEN_SELF(
1822 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1823 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1833 |   case $lt_cv_dlopen_self in
1834 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1835 |   *) enable_dlopen_self=unknown ;;
1838 |   case $lt_cv_dlopen_self_static in
1839 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1840 |   *) enable_dlopen_self_static=unknown ;;
1843 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1844 | 	 [Whether dlopen is supported])
1845 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1846 | 	 [Whether dlopen of programs is supported])
1847 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1848 | 	 [Whether dlopen of statically linked programs is supported])
1849 | ])# LT_SYS_DLOPEN_SELF
1852 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1854 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5132 |     [Compiler flag to allow reflexive dlopens])
5244 |   LT_SYS_DLOPEN_SELF
7381 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7413 | # dlopen
7415 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7418 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7419 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7422 | put the `dlopen' option into LT_INIT's first parameter.])
7426 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
7872 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### diy/src/bil-0.6.0/autom4te.cache/output.0

```

{% raw %}
6990 |         enable_dlopen=no
10082 |   if test "x$enable_dlopen" != xyes; then
10083 |   enable_dlopen=unknown
10084 |   enable_dlopen_self=unknown
10085 |   enable_dlopen_self_static=unknown
10087 |   lt_cv_dlopen=no
10088 |   lt_cv_dlopen_libs=
10092 |     lt_cv_dlopen="load_add_on"
10093 |     lt_cv_dlopen_libs=
10094 |     lt_cv_dlopen_self=yes
10098 |     lt_cv_dlopen="LoadLibrary"
10099 |     lt_cv_dlopen_libs=
10103 |     lt_cv_dlopen="dlopen"
10104 |     lt_cv_dlopen_libs=
10109 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10110 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10111 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then :
10125 | char dlopen ();
10129 | return dlopen ();
10135 |   ac_cv_lib_dl_dlopen=yes
10137 |   ac_cv_lib_dl_dlopen=no
10143 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10144 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10145 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then :
10146 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10149 |     lt_cv_dlopen="dyld"
10150 |     lt_cv_dlopen_libs=
10151 |     lt_cv_dlopen_self=yes
10160 |   lt_cv_dlopen="shl_load"
10199 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
10201 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
10202 | if test "x$ac_cv_func_dlopen" = x""yes; then :
10203 |   lt_cv_dlopen="dlopen"
10205 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
10206 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
10207 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then :
10221 | char dlopen ();
10225 | return dlopen ();
10231 |   ac_cv_lib_dl_dlopen=yes
10233 |   ac_cv_lib_dl_dlopen=no
10239 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
10240 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
10241 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then :
10242 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10244 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
10245 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
10246 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then :
10260 | char dlopen ();
10264 | return dlopen ();
10270 |   ac_cv_lib_svld_dlopen=yes
10272 |   ac_cv_lib_svld_dlopen=no
10278 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
10279 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
10280 | if test "x$ac_cv_lib_svld_dlopen" = x""yes; then :
10281 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
10320 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
10341 |   if test "x$lt_cv_dlopen" != xno; then
10342 |     enable_dlopen=yes
10344 |     enable_dlopen=no
10347 |   case $lt_cv_dlopen in
10348 |   dlopen)
10356 |     LIBS="$lt_cv_dlopen_libs $LIBS"
10358 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
10359 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
10360 | if test "${lt_cv_dlopen_self+set}" = set; then :
10364 |   lt_cv_dlopen_self=cross
10413 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10436 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
10437 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
10438 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
10442 |     lt_cv_dlopen_self=no
10449 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
10450 | $as_echo "$lt_cv_dlopen_self" >&6; }
10452 |     if test "x$lt_cv_dlopen_self" = xyes; then
10454 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
10455 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
10456 | if test "${lt_cv_dlopen_self_static+set}" = set; then :
10460 |   lt_cv_dlopen_self_static=cross
10509 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10532 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
10533 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
10534 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
10538 |     lt_cv_dlopen_self_static=no
10545 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
10546 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
10555 |   case $lt_cv_dlopen_self in
10556 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
10557 |   *) enable_dlopen_self=unknown ;;
10560 |   case $lt_cv_dlopen_self_static in
10561 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
10562 |   *) enable_dlopen_self_static=unknown ;;
12107 | enable_dlopen='`$ECHO "X$enable_dlopen" | $Xsed -e "$delay_single_quote_subst"`'
12108 | enable_dlopen_self='`$ECHO "X$enable_dlopen_self" | $Xsed -e "$delay_single_quote_subst"`'
12109 | enable_dlopen_self_static='`$ECHO "X$enable_dlopen_self_static" | $Xsed -e "$delay_single_quote_subst"`'
13186 | # Whether dlopen is supported.
13187 | dlopen_support=$enable_dlopen
13189 | # Whether dlopen of programs is supported.
13190 | dlopen_self=$enable_dlopen_self
13192 | # Whether dlopen of statically linked programs is supported.
13193 | dlopen_self_static=$enable_dlopen_self_static
13233 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### diy/src/bil-0.6.0/autom4te.cache/output.1

```

{% raw %}
6868 |         enable_dlopen=no
10020 |   if test "x$enable_dlopen" != xyes; then
10021 |   enable_dlopen=unknown
10022 |   enable_dlopen_self=unknown
10023 |   enable_dlopen_self_static=unknown
10025 |   lt_cv_dlopen=no
10026 |   lt_cv_dlopen_libs=
10030 |     lt_cv_dlopen="load_add_on"
10031 |     lt_cv_dlopen_libs=
10032 |     lt_cv_dlopen_self=yes
10036 |     lt_cv_dlopen="LoadLibrary"
10037 |     lt_cv_dlopen_libs=
10041 |     lt_cv_dlopen="dlopen"
10042 |     lt_cv_dlopen_libs=
10047 |     { echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
10048 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6; }
10049 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
10067 | char dlopen ();
10071 | return dlopen ();
10094 |   ac_cv_lib_dl_dlopen=yes
10099 | 	ac_cv_lib_dl_dlopen=no
10106 | { echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
10107 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6; }
10108 | if test $ac_cv_lib_dl_dlopen = yes; then
10109 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10112 |     lt_cv_dlopen="dyld"
10113 |     lt_cv_dlopen_libs=
10114 |     lt_cv_dlopen_self=yes
10203 |   lt_cv_dlopen="shl_load"
10267 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
10269 |   { echo "$as_me:$LINENO: checking for dlopen" >&5
10270 | echo $ECHO_N "checking for dlopen... $ECHO_C" >&6; }
10271 | if test "${ac_cv_func_dlopen+set}" = set; then
10280 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
10282 | #define dlopen innocuous_dlopen
10285 |     which can conflict with char dlopen (); below.
10295 | #undef dlopen
10303 | char dlopen ();
10307 | #if defined __stub_dlopen || defined __stub___dlopen
10314 | return dlopen ();
10337 |   ac_cv_func_dlopen=yes
10342 | 	ac_cv_func_dlopen=no
10348 | { echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
10349 | echo "${ECHO_T}$ac_cv_func_dlopen" >&6; }
10350 | if test $ac_cv_func_dlopen = yes; then
10351 |   lt_cv_dlopen="dlopen"
10353 |   { echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
10354 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6; }
10355 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
10373 | char dlopen ();
10377 | return dlopen ();
10400 |   ac_cv_lib_dl_dlopen=yes
10405 | 	ac_cv_lib_dl_dlopen=no
10412 | { echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
10413 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6; }
10414 | if test $ac_cv_lib_dl_dlopen = yes; then
10415 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
10417 |   { echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
10418 | echo $ECHO_N "checking for dlopen in -lsvld... $ECHO_C" >&6; }
10419 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
10437 | char dlopen ();
10441 | return dlopen ();
10464 |   ac_cv_lib_svld_dlopen=yes
10469 | 	ac_cv_lib_svld_dlopen=no
10476 | { echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
10477 | echo "${ECHO_T}$ac_cv_lib_svld_dlopen" >&6; }
10478 | if test $ac_cv_lib_svld_dlopen = yes; then
10479 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
10543 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
10564 |   if test "x$lt_cv_dlopen" != xno; then
10565 |     enable_dlopen=yes
10567 |     enable_dlopen=no
10570 |   case $lt_cv_dlopen in
10571 |   dlopen)
10579 |     LIBS="$lt_cv_dlopen_libs $LIBS"
10581 |     { echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
10582 | echo $ECHO_N "checking whether a program can dlopen itself... $ECHO_C" >&6; }
10583 | if test "${lt_cv_dlopen_self+set}" = set; then
10587 |   lt_cv_dlopen_self=cross
10640 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10663 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
10664 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
10665 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
10669 |     lt_cv_dlopen_self=no
10676 | { echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
10677 | echo "${ECHO_T}$lt_cv_dlopen_self" >&6; }
10679 |     if test "x$lt_cv_dlopen_self" = xyes; then
10681 |       { echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
10682 | echo $ECHO_N "checking whether a statically linked program can dlopen itself... $ECHO_C" >&6; }
10683 | if test "${lt_cv_dlopen_self_static+set}" = set; then
10687 |   lt_cv_dlopen_self_static=cross
10740 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
10763 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
10764 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
10765 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
10769 |     lt_cv_dlopen_self_static=no
10776 | { echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
10777 | echo "${ECHO_T}$lt_cv_dlopen_self_static" >&6; }
10786 |   case $lt_cv_dlopen_self in
10787 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
10788 |   *) enable_dlopen_self=unknown ;;
10791 |   case $lt_cv_dlopen_self_static in
10792 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
10793 |   *) enable_dlopen_self_static=unknown ;;
13029 | enable_dlopen='`$ECHO "X$enable_dlopen" | $Xsed -e "$delay_single_quote_subst"`'
13030 | enable_dlopen_self='`$ECHO "X$enable_dlopen_self" | $Xsed -e "$delay_single_quote_subst"`'
13031 | enable_dlopen_self_static='`$ECHO "X$enable_dlopen_self_static" | $Xsed -e "$delay_single_quote_subst"`'
14206 | # Whether dlopen is supported.
14207 | dlopen_support=$enable_dlopen
14209 | # Whether dlopen of programs is supported.
14210 | dlopen_self=$enable_dlopen_self
14212 | # Whether dlopen of statically linked programs is supported.
14213 | dlopen_self_static=$enable_dlopen_self_static
14253 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### diy/src/bil-0.6.0/autom4te.cache/traces.0

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
2335 | m4trace:configure.ac:63: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```