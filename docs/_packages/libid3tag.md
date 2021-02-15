---
name: "libid3tag"
layout: package
next_package: comgr
previous_package: osqp
languages: ['bash']
---
## 0.15.1b
2 / 54 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
284 |   -dlopen)
285 |     prevopt="-dlopen"
357 |   # Only execute mode is allowed to have -dlopen flags.
359 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
957 | 	    dlopen_self=$dlopen_self_static
961 | 	    dlopen_self=$dlopen_self_static
1017 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1109 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1249 |       -dlopen)
1593 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1661 | 	  # This library was specified with -dlopen.
1803 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1815 | 	passes="conv scan dlopen dlpreopen link"
1828 | 	dlopen) libs="$dlfiles" ;;
1833 |       if test "$pass" = dlopen; then
2001 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2002 | 	      # If there is no dlopen support or we're linking statically,
2035 | 	dlopen=
2054 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2097 | 	# This library was specified with -dlopen.
2098 | 	if test "$pass" = dlopen; then
2100 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2103 | 	  if test -z "$dlname" || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2104 | 	    # If there is no dlname, no dlopen support or we're linking
2113 | 	fi # $pass = dlopen
2158 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2523 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2524 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2676 |       if test "$pass" != dlopen; then
2776 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
2843 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3474 | 	    $echo "*** a static module, that should work as long as the dlopening"
3475 | 	    $echo "*** application is linked with the -dlopen flag."
3493 | 	    $echo "*** or is declared to -dlopen it."
3906 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4092 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4093 | 	   test "$dlopen_self_static" = unknown; then
4094 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5217 | # The name that we can dlopen(3).
5240 | # Files to dlopen/dlpreopen
5241 | dlopen='$dlfiles'
5852 |     # Handle -dlopen flags immediately.
5881 | 	# Skip this library if it cannot be dlopened.
5906 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6257 |   -dlopen FILE      add the directory containing FILE to the library path
6259 | This mode sets the library path environment variable according to \`-dlopen'
6308 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6317 |   -module           build a library that can dlopened
{% endraw %}

```
### aclocal.m4

```

{% raw %}
203 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
706 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
709 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
765 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
792 | ])# _LT_AC_TRY_DLOPEN_SELF
795 | # AC_LIBTOOL_DLOPEN_SELF
797 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
799 | if test "x$enable_dlopen" != xyes; then
800 |   enable_dlopen=unknown
801 |   enable_dlopen_self=unknown
802 |   enable_dlopen_self_static=unknown
804 |   lt_cv_dlopen=no
805 |   lt_cv_dlopen_libs=
809 |     lt_cv_dlopen="load_add_on"
810 |     lt_cv_dlopen_libs=
811 |     lt_cv_dlopen_self=yes
815 |     lt_cv_dlopen="LoadLibrary"
816 |     lt_cv_dlopen_libs=
820 |     lt_cv_dlopen="dlopen"
821 |     lt_cv_dlopen_libs=
826 |     AC_CHECK_LIB([dl], [dlopen],
827 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
828 |     lt_cv_dlopen="dyld"
829 |     lt_cv_dlopen_libs=
830 |     lt_cv_dlopen_self=yes
836 | 	  [lt_cv_dlopen="shl_load"],
838 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
839 | 	[AC_CHECK_FUNC([dlopen],
840 | 	      [lt_cv_dlopen="dlopen"],
841 | 	  [AC_CHECK_LIB([dl], [dlopen],
842 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
843 | 	    [AC_CHECK_LIB([svld], [dlopen],
844 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
846 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
855 |   if test "x$lt_cv_dlopen" != xno; then
856 |     enable_dlopen=yes
858 |     enable_dlopen=no
861 |   case $lt_cv_dlopen in
862 |   dlopen)
870 |     LIBS="$lt_cv_dlopen_libs $LIBS"
872 |     AC_CACHE_CHECK([whether a program can dlopen itself],
873 | 	  lt_cv_dlopen_self, [dnl
874 | 	  _LT_AC_TRY_DLOPEN_SELF(
875 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
876 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
879 |     if test "x$lt_cv_dlopen_self" = xyes; then
881 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
882 |     	  lt_cv_dlopen_self_static, [dnl
883 | 	  _LT_AC_TRY_DLOPEN_SELF(
884 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
885 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
895 |   case $lt_cv_dlopen_self in
896 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
897 |   *) enable_dlopen_self=unknown ;;
900 |   case $lt_cv_dlopen_self_static in
901 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
902 |   *) enable_dlopen_self_static=unknown ;;
905 | ])# AC_LIBTOOL_DLOPEN_SELF
1718 | # AC_LIBTOOL_DLOPEN
1720 | # enable checks for dlopen support
1721 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1723 | ])# AC_LIBTOOL_DLOPEN
2509 | AC_LIBTOOL_DLOPEN_SELF($1)
3459 | AC_LIBTOOL_DLOPEN_SELF($1)
3754 | AC_LIBTOOL_DLOPEN_SELF($1)
4059 | # Whether dlopen is supported.
4060 | dlopen_support=$enable_dlopen
4062 | # Whether dlopen of programs is supported.
4063 | dlopen_self=$enable_dlopen_self
4065 | # Whether dlopen of statically linked programs is supported.
4066 | dlopen_self_static=$enable_dlopen_self_static
4074 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```