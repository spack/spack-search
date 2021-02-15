---
name: "buddy"
layout: package
next_package: ibm-databroker
previous_package: brltty
languages: ['bash']
---
## 2.4
2 / 82 files match

 - [aclocal.m4](#aclocalm4)
 - [tools/ltmain.sh](#toolsltmainsh)

### aclocal.m4

```

{% raw %}
202 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
710 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
713 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
769 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
796 | ])# _LT_AC_TRY_DLOPEN_SELF
799 | # AC_LIBTOOL_DLOPEN_SELF
801 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
803 | if test "x$enable_dlopen" != xyes; then
804 |   enable_dlopen=unknown
805 |   enable_dlopen_self=unknown
806 |   enable_dlopen_self_static=unknown
808 |   lt_cv_dlopen=no
809 |   lt_cv_dlopen_libs=
813 |     lt_cv_dlopen="load_add_on"
814 |     lt_cv_dlopen_libs=
815 |     lt_cv_dlopen_self=yes
819 |     lt_cv_dlopen="LoadLibrary"
820 |     lt_cv_dlopen_libs=
824 |     lt_cv_dlopen="dlopen"
825 |     lt_cv_dlopen_libs=
830 |     AC_CHECK_LIB([dl], [dlopen],
831 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
832 |     lt_cv_dlopen="dyld"
833 |     lt_cv_dlopen_libs=
834 |     lt_cv_dlopen_self=yes
840 | 	  [lt_cv_dlopen="shl_load"],
842 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
843 | 	[AC_CHECK_FUNC([dlopen],
844 | 	      [lt_cv_dlopen="dlopen"],
845 | 	  [AC_CHECK_LIB([dl], [dlopen],
846 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
847 | 	    [AC_CHECK_LIB([svld], [dlopen],
848 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
850 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
859 |   if test "x$lt_cv_dlopen" != xno; then
860 |     enable_dlopen=yes
862 |     enable_dlopen=no
865 |   case $lt_cv_dlopen in
866 |   dlopen)
874 |     LIBS="$lt_cv_dlopen_libs $LIBS"
876 |     AC_CACHE_CHECK([whether a program can dlopen itself],
877 | 	  lt_cv_dlopen_self, [dnl
878 | 	  _LT_AC_TRY_DLOPEN_SELF(
879 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
880 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
883 |     if test "x$lt_cv_dlopen_self" = xyes; then
885 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
886 |     	  lt_cv_dlopen_self_static, [dnl
887 | 	  _LT_AC_TRY_DLOPEN_SELF(
888 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
889 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
899 |   case $lt_cv_dlopen_self in
900 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
901 |   *) enable_dlopen_self=unknown ;;
904 |   case $lt_cv_dlopen_self_static in
905 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
906 |   *) enable_dlopen_self_static=unknown ;;
909 | ])# AC_LIBTOOL_DLOPEN_SELF
1728 | # AC_LIBTOOL_DLOPEN
1730 | # enable checks for dlopen support
1731 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1733 | ])# AC_LIBTOOL_DLOPEN
2528 | AC_LIBTOOL_DLOPEN_SELF($1)
3478 | AC_LIBTOOL_DLOPEN_SELF($1)
3773 | AC_LIBTOOL_DLOPEN_SELF($1)
4078 | # Whether dlopen is supported.
4079 | dlopen_support=$enable_dlopen
4081 | # Whether dlopen of programs is supported.
4082 | dlopen_self=$enable_dlopen_self
4084 | # Whether dlopen of statically linked programs is supported.
4085 | dlopen_self_static=$enable_dlopen_self_static
4093 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### tools/ltmain.sh

```bash

{% raw %}
380 |   -dlopen)
381 |     prevopt="-dlopen"
453 |   # Only execute mode is allowed to have -dlopen flags.
455 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
975 | 	    dlopen_self=$dlopen_self_static
979 | 	    dlopen_self=$dlopen_self_static
1035 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1127 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1272 |       -dlopen)
1616 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1684 | 	  # This library was specified with -dlopen.
1826 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1838 | 	passes="conv scan dlopen dlpreopen link"
1851 | 	dlopen) libs="$dlfiles" ;;
1856 |       if test "$pass" = dlopen; then
2024 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2025 | 	      # If there is no dlopen support or we're linking statically,
2058 | 	dlopen=
2077 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2120 | 	# This library was specified with -dlopen.
2121 | 	if test "$pass" = dlopen; then
2123 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2127 | 	     test "$dlopen_support" != yes ||
2129 | 	    # If there is no dlname, no dlopen support or we're linking
2138 | 	fi # $pass = dlopen
2183 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2550 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2551 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2704 |       if test "$pass" != dlopen; then
2805 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
2872 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3505 | 	    $echo "*** a static module, that should work as long as the dlopening"
3506 | 	    $echo "*** application is linked with the -dlopen flag."
3524 | 	    $echo "*** or is declared to -dlopen it."
3944 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4130 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4131 | 	   test "$dlopen_self_static" = unknown; then
4132 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5257 | # The name that we can dlopen(3).
5280 | # Files to dlopen/dlpreopen
5281 | dlopen='$dlfiles'
5896 |     # Handle -dlopen flags immediately.
5925 | 	# Skip this library if it cannot be dlopened.
5950 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6301 |   -dlopen FILE      add the directory containing FILE to the library path
6303 | This mode sets the library path environment variable according to \`-dlopen'
6352 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6361 |   -module           build a library that can dlopened
{% endraw %}

```