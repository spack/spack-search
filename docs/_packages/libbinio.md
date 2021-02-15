---
name: "libbinio"
layout: package
next_package: h5hut
previous_package: gconf
languages: ['bash']
---
## 1.4
2 / 39 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
488 |   -dlopen)
489 |     prevopt="-dlopen"
561 |   # Only execute mode is allowed to have -dlopen flags.
563 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1083 | 	    dlopen_self=$dlopen_self_static
1087 | 	    dlopen_self=$dlopen_self_static
1143 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1235 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1380 |       -dlopen)
1724 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1792 | 	  # This library was specified with -dlopen.
1934 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1946 | 	passes="conv scan dlopen dlpreopen link"
1959 | 	dlopen) libs="$dlfiles" ;;
1964 |       if test "$pass" = dlopen; then
2147 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2148 | 	      # If there is no dlopen support or we're linking statically,
2181 | 	dlopen=
2200 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2243 | 	# This library was specified with -dlopen.
2244 | 	if test "$pass" = dlopen; then
2246 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2250 | 	     test "$dlopen_support" != yes ||
2252 | 	    # If there is no dlname, no dlopen support or we're linking
2261 | 	fi # $pass = dlopen
2313 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2680 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2681 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2834 |       if test "$pass" != dlopen; then
2935 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3002 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3635 | 	    $echo "*** a static module, that should work as long as the dlopening"
3636 | 	    $echo "*** application is linked with the -dlopen flag."
3654 | 	    $echo "*** or is declared to -dlopen it."
4012 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4144 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4145 | 	   test "$dlopen_self_static" = unknown; then
4146 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5216 | # The name that we can dlopen(3).
5239 | # Files to dlopen/dlpreopen
5240 | dlopen='$dlfiles'
5855 |     # Handle -dlopen flags immediately.
5884 | 	# Skip this library if it cannot be dlopened.
5909 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6260 |   -dlopen FILE      add the directory containing FILE to the library path
6262 | This mode sets the library path environment variable according to \`-dlopen'
6311 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6320 |   -module           build a library that can dlopened
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
1730 | # AC_LIBTOOL_DLOPEN
1732 | # enable checks for dlopen support
1733 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1735 | ])# AC_LIBTOOL_DLOPEN
2521 | AC_LIBTOOL_DLOPEN_SELF($1)
3471 | AC_LIBTOOL_DLOPEN_SELF($1)
3766 | AC_LIBTOOL_DLOPEN_SELF($1)
4071 | # Whether dlopen is supported.
4072 | dlopen_support=$enable_dlopen
4074 | # Whether dlopen of programs is supported.
4075 | dlopen_self=$enable_dlopen_self
4077 | # Whether dlopen of statically linked programs is supported.
4078 | dlopen_self_static=$enable_dlopen_self_static
4086 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```