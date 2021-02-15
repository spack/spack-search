---
name: "heppdt"
layout: package
next_package: npth
previous_package: py-vermin
languages: ['bash']
---
## 3.04.00
6 / 624 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)
 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [autom4te.cache/output.1](#autom4tecacheoutput1)
 - [autom4te.cache/traces.0](#autom4tecachetraces0)
 - [autom4te.cache/traces.1](#autom4tecachetraces1)

### ltmain.sh

```bash

{% raw %}
371 |   -dlopen)
372 |     prevopt="-dlopen"
444 |   # Only execute mode is allowed to have -dlopen flags.
446 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
966 | 	    dlopen_self=$dlopen_self_static
970 | 	    dlopen_self=$dlopen_self_static
1026 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1118 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1263 |       -dlopen)
1607 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1675 | 	  # This library was specified with -dlopen.
1817 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1829 | 	passes="conv scan dlopen dlpreopen link"
1842 | 	dlopen) libs="$dlfiles" ;;
1847 |       if test "$pass" = dlopen; then
2015 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2016 | 	      # If there is no dlopen support or we're linking statically,
2049 | 	dlopen=
2068 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2111 | 	# This library was specified with -dlopen.
2112 | 	if test "$pass" = dlopen; then
2114 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2118 | 	     test "$dlopen_support" != yes ||
2120 | 	    # If there is no dlname, no dlopen support or we're linking
2129 | 	fi # $pass = dlopen
2174 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2541 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2542 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2695 |       if test "$pass" != dlopen; then
2796 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
2863 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3496 | 	    $echo "*** a static module, that should work as long as the dlopening"
3497 | 	    $echo "*** application is linked with the -dlopen flag."
3515 | 	    $echo "*** or is declared to -dlopen it."
3927 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4113 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4114 | 	   test "$dlopen_self_static" = unknown; then
4115 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5240 | # The name that we can dlopen(3).
5263 | # Files to dlopen/dlpreopen
5264 | dlopen='$dlfiles'
5879 |     # Handle -dlopen flags immediately.
5908 | 	# Skip this library if it cannot be dlopened.
5933 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6284 |   -dlopen FILE      add the directory containing FILE to the library path
6286 | This mode sets the library path environment variable according to \`-dlopen'
6335 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6344 |   -module           build a library that can dlopened
{% endraw %}

```
### aclocal.m4

```

{% raw %}
202 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
705 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
708 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
764 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
791 | ])# _LT_AC_TRY_DLOPEN_SELF
794 | # AC_LIBTOOL_DLOPEN_SELF
796 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
798 | if test "x$enable_dlopen" != xyes; then
799 |   enable_dlopen=unknown
800 |   enable_dlopen_self=unknown
801 |   enable_dlopen_self_static=unknown
803 |   lt_cv_dlopen=no
804 |   lt_cv_dlopen_libs=
808 |     lt_cv_dlopen="load_add_on"
809 |     lt_cv_dlopen_libs=
810 |     lt_cv_dlopen_self=yes
814 |     lt_cv_dlopen="LoadLibrary"
815 |     lt_cv_dlopen_libs=
819 |     lt_cv_dlopen="dlopen"
820 |     lt_cv_dlopen_libs=
825 |     AC_CHECK_LIB([dl], [dlopen],
826 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
827 |     lt_cv_dlopen="dyld"
828 |     lt_cv_dlopen_libs=
829 |     lt_cv_dlopen_self=yes
835 | 	  [lt_cv_dlopen="shl_load"],
837 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
838 | 	[AC_CHECK_FUNC([dlopen],
839 | 	      [lt_cv_dlopen="dlopen"],
840 | 	  [AC_CHECK_LIB([dl], [dlopen],
841 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
842 | 	    [AC_CHECK_LIB([svld], [dlopen],
843 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
845 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
854 |   if test "x$lt_cv_dlopen" != xno; then
855 |     enable_dlopen=yes
857 |     enable_dlopen=no
860 |   case $lt_cv_dlopen in
861 |   dlopen)
869 |     LIBS="$lt_cv_dlopen_libs $LIBS"
871 |     AC_CACHE_CHECK([whether a program can dlopen itself],
872 | 	  lt_cv_dlopen_self, [dnl
873 | 	  _LT_AC_TRY_DLOPEN_SELF(
874 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
875 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
878 |     if test "x$lt_cv_dlopen_self" = xyes; then
880 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
881 |     	  lt_cv_dlopen_self_static, [dnl
882 | 	  _LT_AC_TRY_DLOPEN_SELF(
883 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
884 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
894 |   case $lt_cv_dlopen_self in
895 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
896 |   *) enable_dlopen_self=unknown ;;
899 |   case $lt_cv_dlopen_self_static in
900 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
901 |   *) enable_dlopen_self_static=unknown ;;
904 | ])# AC_LIBTOOL_DLOPEN_SELF
1734 | # AC_LIBTOOL_DLOPEN
1736 | # enable checks for dlopen support
1737 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1739 | ])# AC_LIBTOOL_DLOPEN
2534 | AC_LIBTOOL_DLOPEN_SELF($1)
3484 | AC_LIBTOOL_DLOPEN_SELF($1)
3779 | AC_LIBTOOL_DLOPEN_SELF($1)
4084 | # Whether dlopen is supported.
4085 | dlopen_support=$enable_dlopen
4087 | # Whether dlopen of programs is supported.
4088 | dlopen_self=$enable_dlopen_self
4090 | # Whether dlopen of statically linked programs is supported.
4091 | dlopen_self_static=$enable_dlopen_self_static
4099 | # Compiler flag to allow reflexive dlopens.
7180 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
7683 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
7686 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
7742 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
7769 | ])# _LT_AC_TRY_DLOPEN_SELF
7772 | # AC_LIBTOOL_DLOPEN_SELF
7774 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
7776 | if test "x$enable_dlopen" != xyes; then
7777 |   enable_dlopen=unknown
7778 |   enable_dlopen_self=unknown
7779 |   enable_dlopen_self_static=unknown
7781 |   lt_cv_dlopen=no
7782 |   lt_cv_dlopen_libs=
7786 |     lt_cv_dlopen="load_add_on"
7787 |     lt_cv_dlopen_libs=
7788 |     lt_cv_dlopen_self=yes
7792 |     lt_cv_dlopen="LoadLibrary"
7793 |     lt_cv_dlopen_libs=
7797 |     lt_cv_dlopen="dlopen"
7798 |     lt_cv_dlopen_libs=
7803 |     AC_CHECK_LIB([dl], [dlopen],
7804 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
7805 |     lt_cv_dlopen="dyld"
7806 |     lt_cv_dlopen_libs=
7807 |     lt_cv_dlopen_self=yes
7813 | 	  [lt_cv_dlopen="shl_load"],
7815 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
7816 | 	[AC_CHECK_FUNC([dlopen],
7817 | 	      [lt_cv_dlopen="dlopen"],
7818 | 	  [AC_CHECK_LIB([dl], [dlopen],
7819 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
7820 | 	    [AC_CHECK_LIB([svld], [dlopen],
7821 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
7823 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
7832 |   if test "x$lt_cv_dlopen" != xno; then
7833 |     enable_dlopen=yes
7835 |     enable_dlopen=no
7838 |   case $lt_cv_dlopen in
7839 |   dlopen)
7847 |     LIBS="$lt_cv_dlopen_libs $LIBS"
7849 |     AC_CACHE_CHECK([whether a program can dlopen itself],
7850 | 	  lt_cv_dlopen_self, [dnl
7851 | 	  _LT_AC_TRY_DLOPEN_SELF(
7852 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
7853 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
7856 |     if test "x$lt_cv_dlopen_self" = xyes; then
7858 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
7859 |     	  lt_cv_dlopen_self_static, [dnl
7860 | 	  _LT_AC_TRY_DLOPEN_SELF(
7861 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
7862 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
7872 |   case $lt_cv_dlopen_self in
7873 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
7874 |   *) enable_dlopen_self=unknown ;;
7877 |   case $lt_cv_dlopen_self_static in
7878 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
7879 |   *) enable_dlopen_self_static=unknown ;;
7882 | ])# AC_LIBTOOL_DLOPEN_SELF
8712 | # AC_LIBTOOL_DLOPEN
8714 | # enable checks for dlopen support
8715 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
8717 | ])# AC_LIBTOOL_DLOPEN
9516 | AC_LIBTOOL_DLOPEN_SELF($1)
10470 | AC_LIBTOOL_DLOPEN_SELF($1)
10769 | AC_LIBTOOL_DLOPEN_SELF($1)
11074 | # Whether dlopen is supported.
11075 | dlopen_support=$enable_dlopen
11077 | # Whether dlopen of programs is supported.
11078 | dlopen_self=$enable_dlopen_self
11080 | # Whether dlopen of statically linked programs is supported.
11081 | dlopen_self_static=$enable_dlopen_self_static
11089 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.0

```

{% raw %}
6483 | enable_dlopen=no
8516 | if test "x$enable_dlopen" != xyes; then
8517 |   enable_dlopen=unknown
8518 |   enable_dlopen_self=unknown
8519 |   enable_dlopen_self_static=unknown
8521 |   lt_cv_dlopen=no
8522 |   lt_cv_dlopen_libs=
8526 |     lt_cv_dlopen="load_add_on"
8527 |     lt_cv_dlopen_libs=
8528 |     lt_cv_dlopen_self=yes
8532 |     lt_cv_dlopen="LoadLibrary"
8533 |     lt_cv_dlopen_libs=
8537 |     lt_cv_dlopen="dlopen"
8538 |     lt_cv_dlopen_libs=
8543 |     echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
8544 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
8545 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
8563 | char dlopen ();
8567 | dlopen ();
8594 |   ac_cv_lib_dl_dlopen=yes
8599 | ac_cv_lib_dl_dlopen=no
8605 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
8606 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
8607 | if test $ac_cv_lib_dl_dlopen = yes; then
8608 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
8611 |     lt_cv_dlopen="dyld"
8612 |     lt_cv_dlopen_libs=
8613 |     lt_cv_dlopen_self=yes
8711 |   lt_cv_dlopen="shl_load"
8778 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"
8780 |   echo "$as_me:$LINENO: checking for dlopen" >&5
8781 | echo $ECHO_N "checking for dlopen... $ECHO_C" >&6
8782 | if test "${ac_cv_func_dlopen+set}" = set; then
8791 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
8793 | #define dlopen innocuous_dlopen
8796 |     which can conflict with char dlopen (); below.
8806 | #undef dlopen
8815 | char dlopen ();
8819 | #if defined (__stub_dlopen) || defined (__stub___dlopen)
8822 | char (*f) () = dlopen;
8831 | return f != dlopen;
8858 |   ac_cv_func_dlopen=yes
8863 | ac_cv_func_dlopen=no
8868 | echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
8869 | echo "${ECHO_T}$ac_cv_func_dlopen" >&6
8870 | if test $ac_cv_func_dlopen = yes; then
8871 |   lt_cv_dlopen="dlopen"
8873 |   echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
8874 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
8875 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
8893 | char dlopen ();
8897 | dlopen ();
8924 |   ac_cv_lib_dl_dlopen=yes
8929 | ac_cv_lib_dl_dlopen=no
8935 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
8936 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
8937 | if test $ac_cv_lib_dl_dlopen = yes; then
8938 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
8940 |   echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
8941 | echo $ECHO_N "checking for dlopen in -lsvld... $ECHO_C" >&6
8942 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
8960 | char dlopen ();
8964 | dlopen ();
8991 |   ac_cv_lib_svld_dlopen=yes
8996 | ac_cv_lib_svld_dlopen=no
9002 | echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
9003 | echo "${ECHO_T}$ac_cv_lib_svld_dlopen" >&6
9004 | if test $ac_cv_lib_svld_dlopen = yes; then
9005 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
9072 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"
9093 |   if test "x$lt_cv_dlopen" != xno; then
9094 |     enable_dlopen=yes
9096 |     enable_dlopen=no
9099 |   case $lt_cv_dlopen in
9100 |   dlopen)
9108 |     LIBS="$lt_cv_dlopen_libs $LIBS"
9110 |     echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
9111 | echo $ECHO_N "checking whether a program can dlopen itself... $ECHO_C" >&6
9112 | if test "${lt_cv_dlopen_self+set}" = set; then
9116 |   lt_cv_dlopen_self=cross
9169 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
9190 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
9191 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
9192 |       x$lt_unknown|x*) lt_cv_dlopen_self=no ;;
9196 |     lt_cv_dlopen_self=no
9203 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
9204 | echo "${ECHO_T}$lt_cv_dlopen_self" >&6
9206 |     if test "x$lt_cv_dlopen_self" = xyes; then
9208 |       echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
9209 | echo $ECHO_N "checking whether a statically linked program can dlopen itself... $ECHO_C" >&6
9210 | if test "${lt_cv_dlopen_self_static+set}" = set; then
9214 |   lt_cv_dlopen_self_static=cross
9267 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
9288 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
9289 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
9290 |       x$lt_unknown|x*) lt_cv_dlopen_self_static=no ;;
9294 |     lt_cv_dlopen_self_static=no
9301 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
9302 | echo "${ECHO_T}$lt_cv_dlopen_self_static" >&6
9311 |   case $lt_cv_dlopen_self in
9312 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
9313 |   *) enable_dlopen_self=unknown ;;
9316 |   case $lt_cv_dlopen_self_static in
9317 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
9318 |   *) enable_dlopen_self_static=unknown ;;
9644 | # Whether dlopen is supported.
9645 | dlopen_support=$enable_dlopen
9647 | # Whether dlopen of programs is supported.
9648 | dlopen_self=$enable_dlopen_self
9650 | # Whether dlopen of statically linked programs is supported.
9651 | dlopen_self_static=$enable_dlopen_self_static
9659 | # Compiler flag to allow reflexive dlopens.
12239 | if test "x$enable_dlopen" != xyes; then
12240 |   enable_dlopen=unknown
12241 |   enable_dlopen_self=unknown
12242 |   enable_dlopen_self_static=unknown
12244 |   lt_cv_dlopen=no
12245 |   lt_cv_dlopen_libs=
12249 |     lt_cv_dlopen="load_add_on"
12250 |     lt_cv_dlopen_libs=
12251 |     lt_cv_dlopen_self=yes
12255 |     lt_cv_dlopen="LoadLibrary"
12256 |     lt_cv_dlopen_libs=
12260 |     lt_cv_dlopen="dlopen"
12261 |     lt_cv_dlopen_libs=
12266 |     echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
12267 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
12268 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
12286 | char dlopen ();
12290 | dlopen ();
12317 |   ac_cv_lib_dl_dlopen=yes
12322 | ac_cv_lib_dl_dlopen=no
12328 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
12329 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
12330 | if test $ac_cv_lib_dl_dlopen = yes; then
12331 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12334 |     lt_cv_dlopen="dyld"
12335 |     lt_cv_dlopen_libs=
12336 |     lt_cv_dlopen_self=yes
12434 |   lt_cv_dlopen="shl_load"
12501 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"
12503 |   echo "$as_me:$LINENO: checking for dlopen" >&5
12504 | echo $ECHO_N "checking for dlopen... $ECHO_C" >&6
12505 | if test "${ac_cv_func_dlopen+set}" = set; then
12514 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
12516 | #define dlopen innocuous_dlopen
12519 |     which can conflict with char dlopen (); below.
12529 | #undef dlopen
12538 | char dlopen ();
12542 | #if defined (__stub_dlopen) || defined (__stub___dlopen)
12545 | char (*f) () = dlopen;
12554 | return f != dlopen;
12581 |   ac_cv_func_dlopen=yes
12586 | ac_cv_func_dlopen=no
12591 | echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
12592 | echo "${ECHO_T}$ac_cv_func_dlopen" >&6
12593 | if test $ac_cv_func_dlopen = yes; then
12594 |   lt_cv_dlopen="dlopen"
12596 |   echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
12597 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
12598 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
12616 | char dlopen ();
12620 | dlopen ();
12647 |   ac_cv_lib_dl_dlopen=yes
12652 | ac_cv_lib_dl_dlopen=no
12658 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
12659 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
12660 | if test $ac_cv_lib_dl_dlopen = yes; then
12661 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12663 |   echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
12664 | echo $ECHO_N "checking for dlopen in -lsvld... $ECHO_C" >&6
12665 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
12683 | char dlopen ();
12687 | dlopen ();
12714 |   ac_cv_lib_svld_dlopen=yes
12719 | ac_cv_lib_svld_dlopen=no
12725 | echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
12726 | echo "${ECHO_T}$ac_cv_lib_svld_dlopen" >&6
12727 | if test $ac_cv_lib_svld_dlopen = yes; then
12728 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12795 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"
12816 |   if test "x$lt_cv_dlopen" != xno; then
12817 |     enable_dlopen=yes
12819 |     enable_dlopen=no
12822 |   case $lt_cv_dlopen in
12823 |   dlopen)
12831 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12833 |     echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
12834 | echo $ECHO_N "checking whether a program can dlopen itself... $ECHO_C" >&6
12835 | if test "${lt_cv_dlopen_self+set}" = set; then
12839 |   lt_cv_dlopen_self=cross
12892 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12913 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12914 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12915 |       x$lt_unknown|x*) lt_cv_dlopen_self=no ;;
12919 |     lt_cv_dlopen_self=no
12926 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
12927 | echo "${ECHO_T}$lt_cv_dlopen_self" >&6
12929 |     if test "x$lt_cv_dlopen_self" = xyes; then
12931 |       echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
12932 | echo $ECHO_N "checking whether a statically linked program can dlopen itself... $ECHO_C" >&6
12933 | if test "${lt_cv_dlopen_self_static+set}" = set; then
12937 |   lt_cv_dlopen_self_static=cross
12990 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13011 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
13012 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
13013 |       x$lt_unknown|x*) lt_cv_dlopen_self_static=no ;;
13017 |     lt_cv_dlopen_self_static=no
13024 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
13025 | echo "${ECHO_T}$lt_cv_dlopen_self_static" >&6
13034 |   case $lt_cv_dlopen_self in
13035 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
13036 |   *) enable_dlopen_self=unknown ;;
13039 |   case $lt_cv_dlopen_self_static in
13040 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
13041 |   *) enable_dlopen_self_static=unknown ;;
13245 | # Whether dlopen is supported.
13246 | dlopen_support=$enable_dlopen
13248 | # Whether dlopen of programs is supported.
13249 | dlopen_self=$enable_dlopen_self
13251 | # Whether dlopen of statically linked programs is supported.
13252 | dlopen_self_static=$enable_dlopen_self_static
13260 | # Compiler flag to allow reflexive dlopens.
15610 | # Whether dlopen is supported.
15611 | dlopen_support=$enable_dlopen
15613 | # Whether dlopen of programs is supported.
15614 | dlopen_self=$enable_dlopen_self
15616 | # Whether dlopen of statically linked programs is supported.
15617 | dlopen_self_static=$enable_dlopen_self_static
15625 | # Compiler flag to allow reflexive dlopens.
17781 | if test "x$enable_dlopen" != xyes; then
17782 |   enable_dlopen=unknown
17783 |   enable_dlopen_self=unknown
17784 |   enable_dlopen_self_static=unknown
17786 |   lt_cv_dlopen=no
17787 |   lt_cv_dlopen_libs=
17791 |     lt_cv_dlopen="load_add_on"
17792 |     lt_cv_dlopen_libs=
17793 |     lt_cv_dlopen_self=yes
17797 |     lt_cv_dlopen="LoadLibrary"
17798 |     lt_cv_dlopen_libs=
17802 |     lt_cv_dlopen="dlopen"
17803 |     lt_cv_dlopen_libs=
17808 |     echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
17809 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
17810 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
17828 | char dlopen ();
17832 | dlopen ();
17859 |   ac_cv_lib_dl_dlopen=yes
17864 | ac_cv_lib_dl_dlopen=no
17870 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
17871 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
17872 | if test $ac_cv_lib_dl_dlopen = yes; then
17873 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
17876 |     lt_cv_dlopen="dyld"
17877 |     lt_cv_dlopen_libs=
17878 |     lt_cv_dlopen_self=yes
17976 |   lt_cv_dlopen="shl_load"
18043 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"
18045 |   echo "$as_me:$LINENO: checking for dlopen" >&5
18046 | echo $ECHO_N "checking for dlopen... $ECHO_C" >&6
18047 | if test "${ac_cv_func_dlopen+set}" = set; then
18056 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
18058 | #define dlopen innocuous_dlopen
18061 |     which can conflict with char dlopen (); below.
18071 | #undef dlopen
18080 | char dlopen ();
18084 | #if defined (__stub_dlopen) || defined (__stub___dlopen)
18087 | char (*f) () = dlopen;
18096 | return f != dlopen;
18123 |   ac_cv_func_dlopen=yes
18128 | ac_cv_func_dlopen=no
18133 | echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
18134 | echo "${ECHO_T}$ac_cv_func_dlopen" >&6
18135 | if test $ac_cv_func_dlopen = yes; then
18136 |   lt_cv_dlopen="dlopen"
18138 |   echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
18139 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
18140 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
18158 | char dlopen ();
18162 | dlopen ();
18189 |   ac_cv_lib_dl_dlopen=yes
18194 | ac_cv_lib_dl_dlopen=no
18200 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
18201 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
18202 | if test $ac_cv_lib_dl_dlopen = yes; then
18203 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
18205 |   echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
18206 | echo $ECHO_N "checking for dlopen in -lsvld... $ECHO_C" >&6
18207 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
18225 | char dlopen ();
18229 | dlopen ();
18256 |   ac_cv_lib_svld_dlopen=yes
18261 | ac_cv_lib_svld_dlopen=no
18267 | echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
18268 | echo "${ECHO_T}$ac_cv_lib_svld_dlopen" >&6
18269 | if test $ac_cv_lib_svld_dlopen = yes; then
18270 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
18337 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"
18358 |   if test "x$lt_cv_dlopen" != xno; then
18359 |     enable_dlopen=yes
18361 |     enable_dlopen=no
18364 |   case $lt_cv_dlopen in
18365 |   dlopen)
18373 |     LIBS="$lt_cv_dlopen_libs $LIBS"
18375 |     echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
18376 | echo $ECHO_N "checking whether a program can dlopen itself... $ECHO_C" >&6
18377 | if test "${lt_cv_dlopen_self+set}" = set; then
18381 |   lt_cv_dlopen_self=cross
18434 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
18455 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
18456 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
18457 |       x$lt_unknown|x*) lt_cv_dlopen_self=no ;;
18461 |     lt_cv_dlopen_self=no
18468 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
18469 | echo "${ECHO_T}$lt_cv_dlopen_self" >&6
18471 |     if test "x$lt_cv_dlopen_self" = xyes; then
18473 |       echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
18474 | echo $ECHO_N "checking whether a statically linked program can dlopen itself... $ECHO_C" >&6
18475 | if test "${lt_cv_dlopen_self_static+set}" = set; then
18479 |   lt_cv_dlopen_self_static=cross
18532 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
18553 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
18554 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
18555 |       x$lt_unknown|x*) lt_cv_dlopen_self_static=no ;;
18559 |     lt_cv_dlopen_self_static=no
18566 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
18567 | echo "${ECHO_T}$lt_cv_dlopen_self_static" >&6
18576 |   case $lt_cv_dlopen_self in
18577 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
18578 |   *) enable_dlopen_self=unknown ;;
18581 |   case $lt_cv_dlopen_self_static in
18582 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
18583 |   *) enable_dlopen_self_static=unknown ;;
18787 | # Whether dlopen is supported.
18788 | dlopen_support=$enable_dlopen
18790 | # Whether dlopen of programs is supported.
18791 | dlopen_self=$enable_dlopen_self
18793 | # Whether dlopen of statically linked programs is supported.
18794 | dlopen_self_static=$enable_dlopen_self_static
18802 | # Compiler flag to allow reflexive dlopens.
19232 | # Whether dlopen is supported.
19233 | dlopen_support=$enable_dlopen
19235 | # Whether dlopen of programs is supported.
19236 | dlopen_self=$enable_dlopen_self
19238 | # Whether dlopen of statically linked programs is supported.
19239 | dlopen_self_static=$enable_dlopen_self_static
19247 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.1

```

{% raw %}
6483 | enable_dlopen=no
8516 | if test "x$enable_dlopen" != xyes; then
8517 |   enable_dlopen=unknown
8518 |   enable_dlopen_self=unknown
8519 |   enable_dlopen_self_static=unknown
8521 |   lt_cv_dlopen=no
8522 |   lt_cv_dlopen_libs=
8526 |     lt_cv_dlopen="load_add_on"
8527 |     lt_cv_dlopen_libs=
8528 |     lt_cv_dlopen_self=yes
8532 |     lt_cv_dlopen="LoadLibrary"
8533 |     lt_cv_dlopen_libs=
8537 |     lt_cv_dlopen="dlopen"
8538 |     lt_cv_dlopen_libs=
8543 |     echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
8544 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
8545 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
8563 | char dlopen ();
8567 | dlopen ();
8594 |   ac_cv_lib_dl_dlopen=yes
8599 | ac_cv_lib_dl_dlopen=no
8605 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
8606 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
8607 | if test $ac_cv_lib_dl_dlopen = yes; then
8608 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
8611 |     lt_cv_dlopen="dyld"
8612 |     lt_cv_dlopen_libs=
8613 |     lt_cv_dlopen_self=yes
8711 |   lt_cv_dlopen="shl_load"
8778 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"
8780 |   echo "$as_me:$LINENO: checking for dlopen" >&5
8781 | echo $ECHO_N "checking for dlopen... $ECHO_C" >&6
8782 | if test "${ac_cv_func_dlopen+set}" = set; then
8791 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
8793 | #define dlopen innocuous_dlopen
8796 |     which can conflict with char dlopen (); below.
8806 | #undef dlopen
8815 | char dlopen ();
8819 | #if defined (__stub_dlopen) || defined (__stub___dlopen)
8822 | char (*f) () = dlopen;
8831 | return f != dlopen;
8858 |   ac_cv_func_dlopen=yes
8863 | ac_cv_func_dlopen=no
8868 | echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
8869 | echo "${ECHO_T}$ac_cv_func_dlopen" >&6
8870 | if test $ac_cv_func_dlopen = yes; then
8871 |   lt_cv_dlopen="dlopen"
8873 |   echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
8874 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
8875 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
8893 | char dlopen ();
8897 | dlopen ();
8924 |   ac_cv_lib_dl_dlopen=yes
8929 | ac_cv_lib_dl_dlopen=no
8935 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
8936 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
8937 | if test $ac_cv_lib_dl_dlopen = yes; then
8938 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
8940 |   echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
8941 | echo $ECHO_N "checking for dlopen in -lsvld... $ECHO_C" >&6
8942 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
8960 | char dlopen ();
8964 | dlopen ();
8991 |   ac_cv_lib_svld_dlopen=yes
8996 | ac_cv_lib_svld_dlopen=no
9002 | echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
9003 | echo "${ECHO_T}$ac_cv_lib_svld_dlopen" >&6
9004 | if test $ac_cv_lib_svld_dlopen = yes; then
9005 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
9072 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"
9093 |   if test "x$lt_cv_dlopen" != xno; then
9094 |     enable_dlopen=yes
9096 |     enable_dlopen=no
9099 |   case $lt_cv_dlopen in
9100 |   dlopen)
9108 |     LIBS="$lt_cv_dlopen_libs $LIBS"
9110 |     echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
9111 | echo $ECHO_N "checking whether a program can dlopen itself... $ECHO_C" >&6
9112 | if test "${lt_cv_dlopen_self+set}" = set; then
9116 |   lt_cv_dlopen_self=cross
9169 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
9190 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
9191 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
9192 |       x$lt_unknown|x*) lt_cv_dlopen_self=no ;;
9196 |     lt_cv_dlopen_self=no
9203 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
9204 | echo "${ECHO_T}$lt_cv_dlopen_self" >&6
9206 |     if test "x$lt_cv_dlopen_self" = xyes; then
9208 |       echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
9209 | echo $ECHO_N "checking whether a statically linked program can dlopen itself... $ECHO_C" >&6
9210 | if test "${lt_cv_dlopen_self_static+set}" = set; then
9214 |   lt_cv_dlopen_self_static=cross
9267 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
9288 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
9289 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
9290 |       x$lt_unknown|x*) lt_cv_dlopen_self_static=no ;;
9294 |     lt_cv_dlopen_self_static=no
9301 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
9302 | echo "${ECHO_T}$lt_cv_dlopen_self_static" >&6
9311 |   case $lt_cv_dlopen_self in
9312 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
9313 |   *) enable_dlopen_self=unknown ;;
9316 |   case $lt_cv_dlopen_self_static in
9317 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
9318 |   *) enable_dlopen_self_static=unknown ;;
9644 | # Whether dlopen is supported.
9645 | dlopen_support=$enable_dlopen
9647 | # Whether dlopen of programs is supported.
9648 | dlopen_self=$enable_dlopen_self
9650 | # Whether dlopen of statically linked programs is supported.
9651 | dlopen_self_static=$enable_dlopen_self_static
9659 | # Compiler flag to allow reflexive dlopens.
12239 | if test "x$enable_dlopen" != xyes; then
12240 |   enable_dlopen=unknown
12241 |   enable_dlopen_self=unknown
12242 |   enable_dlopen_self_static=unknown
12244 |   lt_cv_dlopen=no
12245 |   lt_cv_dlopen_libs=
12249 |     lt_cv_dlopen="load_add_on"
12250 |     lt_cv_dlopen_libs=
12251 |     lt_cv_dlopen_self=yes
12255 |     lt_cv_dlopen="LoadLibrary"
12256 |     lt_cv_dlopen_libs=
12260 |     lt_cv_dlopen="dlopen"
12261 |     lt_cv_dlopen_libs=
12266 |     echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
12267 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
12268 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
12286 | char dlopen ();
12290 | dlopen ();
12317 |   ac_cv_lib_dl_dlopen=yes
12322 | ac_cv_lib_dl_dlopen=no
12328 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
12329 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
12330 | if test $ac_cv_lib_dl_dlopen = yes; then
12331 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12334 |     lt_cv_dlopen="dyld"
12335 |     lt_cv_dlopen_libs=
12336 |     lt_cv_dlopen_self=yes
12434 |   lt_cv_dlopen="shl_load"
12501 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"
12503 |   echo "$as_me:$LINENO: checking for dlopen" >&5
12504 | echo $ECHO_N "checking for dlopen... $ECHO_C" >&6
12505 | if test "${ac_cv_func_dlopen+set}" = set; then
12514 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
12516 | #define dlopen innocuous_dlopen
12519 |     which can conflict with char dlopen (); below.
12529 | #undef dlopen
12538 | char dlopen ();
12542 | #if defined (__stub_dlopen) || defined (__stub___dlopen)
12545 | char (*f) () = dlopen;
12554 | return f != dlopen;
12581 |   ac_cv_func_dlopen=yes
12586 | ac_cv_func_dlopen=no
12591 | echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
12592 | echo "${ECHO_T}$ac_cv_func_dlopen" >&6
12593 | if test $ac_cv_func_dlopen = yes; then
12594 |   lt_cv_dlopen="dlopen"
12596 |   echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
12597 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
12598 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
12616 | char dlopen ();
12620 | dlopen ();
12647 |   ac_cv_lib_dl_dlopen=yes
12652 | ac_cv_lib_dl_dlopen=no
12658 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
12659 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
12660 | if test $ac_cv_lib_dl_dlopen = yes; then
12661 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12663 |   echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
12664 | echo $ECHO_N "checking for dlopen in -lsvld... $ECHO_C" >&6
12665 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
12683 | char dlopen ();
12687 | dlopen ();
12714 |   ac_cv_lib_svld_dlopen=yes
12719 | ac_cv_lib_svld_dlopen=no
12725 | echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
12726 | echo "${ECHO_T}$ac_cv_lib_svld_dlopen" >&6
12727 | if test $ac_cv_lib_svld_dlopen = yes; then
12728 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12795 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"
12816 |   if test "x$lt_cv_dlopen" != xno; then
12817 |     enable_dlopen=yes
12819 |     enable_dlopen=no
12822 |   case $lt_cv_dlopen in
12823 |   dlopen)
12831 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12833 |     echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
12834 | echo $ECHO_N "checking whether a program can dlopen itself... $ECHO_C" >&6
12835 | if test "${lt_cv_dlopen_self+set}" = set; then
12839 |   lt_cv_dlopen_self=cross
12892 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12913 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12914 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12915 |       x$lt_unknown|x*) lt_cv_dlopen_self=no ;;
12919 |     lt_cv_dlopen_self=no
12926 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
12927 | echo "${ECHO_T}$lt_cv_dlopen_self" >&6
12929 |     if test "x$lt_cv_dlopen_self" = xyes; then
12931 |       echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
12932 | echo $ECHO_N "checking whether a statically linked program can dlopen itself... $ECHO_C" >&6
12933 | if test "${lt_cv_dlopen_self_static+set}" = set; then
12937 |   lt_cv_dlopen_self_static=cross
12990 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
13011 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
13012 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
13013 |       x$lt_unknown|x*) lt_cv_dlopen_self_static=no ;;
13017 |     lt_cv_dlopen_self_static=no
13024 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
13025 | echo "${ECHO_T}$lt_cv_dlopen_self_static" >&6
13034 |   case $lt_cv_dlopen_self in
13035 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
13036 |   *) enable_dlopen_self=unknown ;;
13039 |   case $lt_cv_dlopen_self_static in
13040 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
13041 |   *) enable_dlopen_self_static=unknown ;;
13245 | # Whether dlopen is supported.
13246 | dlopen_support=$enable_dlopen
13248 | # Whether dlopen of programs is supported.
13249 | dlopen_self=$enable_dlopen_self
13251 | # Whether dlopen of statically linked programs is supported.
13252 | dlopen_self_static=$enable_dlopen_self_static
13260 | # Compiler flag to allow reflexive dlopens.
15610 | # Whether dlopen is supported.
15611 | dlopen_support=$enable_dlopen
15613 | # Whether dlopen of programs is supported.
15614 | dlopen_self=$enable_dlopen_self
15616 | # Whether dlopen of statically linked programs is supported.
15617 | dlopen_self_static=$enable_dlopen_self_static
15625 | # Compiler flag to allow reflexive dlopens.
17781 | if test "x$enable_dlopen" != xyes; then
17782 |   enable_dlopen=unknown
17783 |   enable_dlopen_self=unknown
17784 |   enable_dlopen_self_static=unknown
17786 |   lt_cv_dlopen=no
17787 |   lt_cv_dlopen_libs=
17791 |     lt_cv_dlopen="load_add_on"
17792 |     lt_cv_dlopen_libs=
17793 |     lt_cv_dlopen_self=yes
17797 |     lt_cv_dlopen="LoadLibrary"
17798 |     lt_cv_dlopen_libs=
17802 |     lt_cv_dlopen="dlopen"
17803 |     lt_cv_dlopen_libs=
17808 |     echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
17809 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
17810 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
17828 | char dlopen ();
17832 | dlopen ();
17859 |   ac_cv_lib_dl_dlopen=yes
17864 | ac_cv_lib_dl_dlopen=no
17870 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
17871 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
17872 | if test $ac_cv_lib_dl_dlopen = yes; then
17873 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
17876 |     lt_cv_dlopen="dyld"
17877 |     lt_cv_dlopen_libs=
17878 |     lt_cv_dlopen_self=yes
17976 |   lt_cv_dlopen="shl_load"
18043 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"
18045 |   echo "$as_me:$LINENO: checking for dlopen" >&5
18046 | echo $ECHO_N "checking for dlopen... $ECHO_C" >&6
18047 | if test "${ac_cv_func_dlopen+set}" = set; then
18056 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
18058 | #define dlopen innocuous_dlopen
18061 |     which can conflict with char dlopen (); below.
18071 | #undef dlopen
18080 | char dlopen ();
18084 | #if defined (__stub_dlopen) || defined (__stub___dlopen)
18087 | char (*f) () = dlopen;
18096 | return f != dlopen;
18123 |   ac_cv_func_dlopen=yes
18128 | ac_cv_func_dlopen=no
18133 | echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
18134 | echo "${ECHO_T}$ac_cv_func_dlopen" >&6
18135 | if test $ac_cv_func_dlopen = yes; then
18136 |   lt_cv_dlopen="dlopen"
18138 |   echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
18139 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6
18140 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
18158 | char dlopen ();
18162 | dlopen ();
18189 |   ac_cv_lib_dl_dlopen=yes
18194 | ac_cv_lib_dl_dlopen=no
18200 | echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
18201 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6
18202 | if test $ac_cv_lib_dl_dlopen = yes; then
18203 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
18205 |   echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
18206 | echo $ECHO_N "checking for dlopen in -lsvld... $ECHO_C" >&6
18207 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
18225 | char dlopen ();
18229 | dlopen ();
18256 |   ac_cv_lib_svld_dlopen=yes
18261 | ac_cv_lib_svld_dlopen=no
18267 | echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
18268 | echo "${ECHO_T}$ac_cv_lib_svld_dlopen" >&6
18269 | if test $ac_cv_lib_svld_dlopen = yes; then
18270 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
18337 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"
18358 |   if test "x$lt_cv_dlopen" != xno; then
18359 |     enable_dlopen=yes
18361 |     enable_dlopen=no
18364 |   case $lt_cv_dlopen in
18365 |   dlopen)
18373 |     LIBS="$lt_cv_dlopen_libs $LIBS"
18375 |     echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
18376 | echo $ECHO_N "checking whether a program can dlopen itself... $ECHO_C" >&6
18377 | if test "${lt_cv_dlopen_self+set}" = set; then
18381 |   lt_cv_dlopen_self=cross
18434 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
18455 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
18456 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
18457 |       x$lt_unknown|x*) lt_cv_dlopen_self=no ;;
18461 |     lt_cv_dlopen_self=no
18468 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
18469 | echo "${ECHO_T}$lt_cv_dlopen_self" >&6
18471 |     if test "x$lt_cv_dlopen_self" = xyes; then
18473 |       echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
18474 | echo $ECHO_N "checking whether a statically linked program can dlopen itself... $ECHO_C" >&6
18475 | if test "${lt_cv_dlopen_self_static+set}" = set; then
18479 |   lt_cv_dlopen_self_static=cross
18532 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
18553 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
18554 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
18555 |       x$lt_unknown|x*) lt_cv_dlopen_self_static=no ;;
18559 |     lt_cv_dlopen_self_static=no
18566 | echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
18567 | echo "${ECHO_T}$lt_cv_dlopen_self_static" >&6
18576 |   case $lt_cv_dlopen_self in
18577 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
18578 |   *) enable_dlopen_self=unknown ;;
18581 |   case $lt_cv_dlopen_self_static in
18582 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
18583 |   *) enable_dlopen_self_static=unknown ;;
18787 | # Whether dlopen is supported.
18788 | dlopen_support=$enable_dlopen
18790 | # Whether dlopen of programs is supported.
18791 | dlopen_self=$enable_dlopen_self
18793 | # Whether dlopen of statically linked programs is supported.
18794 | dlopen_self_static=$enable_dlopen_self_static
18802 | # Compiler flag to allow reflexive dlopens.
19232 | # Whether dlopen is supported.
19233 | dlopen_support=$enable_dlopen
19235 | # Whether dlopen of programs is supported.
19236 | dlopen_self=$enable_dlopen_self
19238 | # Whether dlopen of statically linked programs is supported.
19239 | dlopen_self_static=$enable_dlopen_self_static
19247 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.0

```

{% raw %}
161 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
605 | m4trace:/usr/share/aclocal/libtool.m4:801: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF], [AC_REQUIRE([_LT_AC_CHECK_DLFCN])dnl
660 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
688 | m4trace:/usr/share/aclocal/libtool.m4:914: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_REQUIRE([_LT_AC_CHECK_DLFCN])dnl
689 | if test "x$enable_dlopen" != xyes; then
690 |   enable_dlopen=unknown
691 |   enable_dlopen_self=unknown
692 |   enable_dlopen_self_static=unknown
694 |   lt_cv_dlopen=no
695 |   lt_cv_dlopen_libs=
699 |     lt_cv_dlopen="load_add_on"
700 |     lt_cv_dlopen_libs=
701 |     lt_cv_dlopen_self=yes
705 |     lt_cv_dlopen="LoadLibrary"
706 |     lt_cv_dlopen_libs=
710 |     lt_cv_dlopen="dlopen"
711 |     lt_cv_dlopen_libs=
716 |     AC_CHECK_LIB([dl], [dlopen],
717 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
718 |     lt_cv_dlopen="dyld"
719 |     lt_cv_dlopen_libs=
720 |     lt_cv_dlopen_self=yes
726 | 	  [lt_cv_dlopen="shl_load"],
728 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
729 | 	[AC_CHECK_FUNC([dlopen],
730 | 	      [lt_cv_dlopen="dlopen"],
731 | 	  [AC_CHECK_LIB([dl], [dlopen],
732 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
733 | 	    [AC_CHECK_LIB([svld], [dlopen],
734 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
736 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
745 |   if test "x$lt_cv_dlopen" != xno; then
746 |     enable_dlopen=yes
748 |     enable_dlopen=no
751 |   case $lt_cv_dlopen in
752 |   dlopen)
760 |     LIBS="$lt_cv_dlopen_libs $LIBS"
762 |     AC_CACHE_CHECK([whether a program can dlopen itself],
763 | 	  lt_cv_dlopen_self, [dnl
764 | 	  _LT_AC_TRY_DLOPEN_SELF(
765 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
766 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
769 |     if test "x$lt_cv_dlopen_self" = xyes; then
771 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
772 |     	  lt_cv_dlopen_self_static, [dnl
773 | 	  _LT_AC_TRY_DLOPEN_SELF(
774 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
775 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
785 |   case $lt_cv_dlopen_self in
786 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
787 |   *) enable_dlopen_self=unknown ;;
790 |   case $lt_cv_dlopen_self_static in
791 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
792 |   *) enable_dlopen_self_static=unknown ;;
1584 | m4trace:/usr/share/aclocal/libtool.m4:1749: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_BEFORE([$0],[AC_LIBTOOL_SETUP])
2192 | AC_LIBTOOL_DLOPEN_SELF($1)
3138 | AC_LIBTOOL_DLOPEN_SELF($1)
3415 | AC_LIBTOOL_DLOPEN_SELF($1)
3703 | # Whether dlopen is supported.
3704 | dlopen_support=$enable_dlopen
3706 | # Whether dlopen of programs is supported.
3707 | dlopen_self=$enable_dlopen_self
3709 | # Whether dlopen of statically linked programs is supported.
3710 | dlopen_self_static=$enable_dlopen_self_static
3718 | # Compiler flag to allow reflexive dlopens.
6843 | m4trace:configure.ac:60: -1- AC_LIBTOOL_DLOPEN_SELF([])
6876 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [
6877 |     lt_cv_dlopen="dyld"
6878 |     lt_cv_dlopen_libs=
6879 |     lt_cv_dlopen_self=yes
6881 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [shl_load], [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"], [AC_CHECK_FUNC([dlopen],
6882 | 	      [lt_cv_dlopen="dlopen"],
6883 | 	  [AC_CHECK_LIB([dl], [dlopen],
6884 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
6885 | 	    [AC_CHECK_LIB([svld], [dlopen],
6886 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
6888 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
6893 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [AC_CHECK_LIB([svld], [dlopen],
6894 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
6896 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
6899 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([svld], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"], [AC_CHECK_LIB([dld], [dld_link],
6900 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
6902 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [dld_link], [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
6903 | m4trace:configure.ac:60: -1- _LT_AC_TRY_DLOPEN_SELF([lt_cv_dlopen_self=yes], [lt_cv_dlopen_self=yes], [lt_cv_dlopen_self=no], [lt_cv_dlopen_self=cross])
6904 | m4trace:configure.ac:60: -1- _LT_AC_TRY_DLOPEN_SELF([lt_cv_dlopen_self_static=yes], [lt_cv_dlopen_self_static=yes], [lt_cv_dlopen_self_static=no], [lt_cv_dlopen_self_static=cross])
7384 | m4trace:configure.ac:60: -1- AC_LIBTOOL_DLOPEN_SELF([CXX])
7385 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [
7386 |     lt_cv_dlopen="dyld"
7387 |     lt_cv_dlopen_libs=
7388 |     lt_cv_dlopen_self=yes
7390 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [shl_load], [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"], [AC_CHECK_FUNC([dlopen],
7391 | 	      [lt_cv_dlopen="dlopen"],
7392 | 	  [AC_CHECK_LIB([dl], [dlopen],
7393 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
7394 | 	    [AC_CHECK_LIB([svld], [dlopen],
7395 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
7397 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
7402 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [AC_CHECK_LIB([svld], [dlopen],
7403 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
7405 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
7408 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([svld], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"], [AC_CHECK_LIB([dld], [dld_link],
7409 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
7411 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [dld_link], [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
7412 | m4trace:configure.ac:60: -1- _LT_AC_TRY_DLOPEN_SELF([lt_cv_dlopen_self=yes], [lt_cv_dlopen_self=yes], [lt_cv_dlopen_self=no], [lt_cv_dlopen_self=cross])
7413 | m4trace:configure.ac:60: -1- _LT_AC_TRY_DLOPEN_SELF([lt_cv_dlopen_self_static=yes], [lt_cv_dlopen_self_static=yes], [lt_cv_dlopen_self_static=no], [lt_cv_dlopen_self_static=cross])
8373 | m4trace:configure.ac:60: -1- AC_LIBTOOL_DLOPEN_SELF([GCJ])
8374 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [
8375 |     lt_cv_dlopen="dyld"
8376 |     lt_cv_dlopen_libs=
8377 |     lt_cv_dlopen_self=yes
8379 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [shl_load], [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"], [AC_CHECK_FUNC([dlopen],
8380 | 	      [lt_cv_dlopen="dlopen"],
8381 | 	  [AC_CHECK_LIB([dl], [dlopen],
8382 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
8383 | 	    [AC_CHECK_LIB([svld], [dlopen],
8384 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
8386 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
8391 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [AC_CHECK_LIB([svld], [dlopen],
8392 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
8394 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
8397 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([svld], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"], [AC_CHECK_LIB([dld], [dld_link],
8398 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
8400 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [dld_link], [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
8401 | m4trace:configure.ac:60: -1- _LT_AC_TRY_DLOPEN_SELF([lt_cv_dlopen_self=yes], [lt_cv_dlopen_self=yes], [lt_cv_dlopen_self=no], [lt_cv_dlopen_self=cross])
8402 | m4trace:configure.ac:60: -1- _LT_AC_TRY_DLOPEN_SELF([lt_cv_dlopen_self_static=yes], [lt_cv_dlopen_self_static=yes], [lt_cv_dlopen_self_static=no], [lt_cv_dlopen_self_static=cross])
{% endraw %}

```
### autom4te.cache/traces.1

```

{% raw %}
280 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [
281 |     lt_cv_dlopen="dyld"
282 |     lt_cv_dlopen_libs=
283 |     lt_cv_dlopen_self=yes
285 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [shl_load], [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"], [AC_CHECK_FUNC([dlopen],
286 | 	      [lt_cv_dlopen="dlopen"],
287 | 	  [AC_CHECK_LIB([dl], [dlopen],
288 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
289 | 	    [AC_CHECK_LIB([svld], [dlopen],
290 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
292 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
297 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [AC_CHECK_LIB([svld], [dlopen],
298 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
300 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
303 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([svld], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"], [AC_CHECK_LIB([dld], [dld_link],
304 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
306 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [dld_link], [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
335 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [
336 |     lt_cv_dlopen="dyld"
337 |     lt_cv_dlopen_libs=
338 |     lt_cv_dlopen_self=yes
340 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [shl_load], [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"], [AC_CHECK_FUNC([dlopen],
341 | 	      [lt_cv_dlopen="dlopen"],
342 | 	  [AC_CHECK_LIB([dl], [dlopen],
343 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
344 | 	    [AC_CHECK_LIB([svld], [dlopen],
345 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
347 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
352 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [AC_CHECK_LIB([svld], [dlopen],
353 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
355 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
358 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([svld], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"], [AC_CHECK_LIB([dld], [dld_link],
359 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
361 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [dld_link], [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
389 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [
390 |     lt_cv_dlopen="dyld"
391 |     lt_cv_dlopen_libs=
392 |     lt_cv_dlopen_self=yes
394 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [shl_load], [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"], [AC_CHECK_FUNC([dlopen],
395 | 	      [lt_cv_dlopen="dlopen"],
396 | 	  [AC_CHECK_LIB([dl], [dlopen],
397 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
398 | 	    [AC_CHECK_LIB([svld], [dlopen],
399 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
401 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
406 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dl], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"], [AC_CHECK_LIB([svld], [dlopen],
407 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
409 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
412 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([svld], [dlopen], [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"], [AC_CHECK_LIB([dld], [dld_link],
413 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
415 | m4trace:configure.ac:60: -1- AC_CHECK_LIB([dld], [dld_link], [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
{% endraw %}

```