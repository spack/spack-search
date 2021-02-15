---
name: "hdf-eos2"
layout: package
next_package: tk
previous_package: ginac
languages: ['bash']
---
## 2.20v1.00
2 / 257 files match

 - [aclocal.m4](#aclocalm4)
 - [config/ltmain.sh](#configltmainsh)

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
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
522 |   -dlopen)
523 |     prevopt="-dlopen"
607 |   # Only execute mode is allowed to have -dlopen flags.
609 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1146 | 	    dlopen_self=$dlopen_self_static
1151 | 	    dlopen_self=$dlopen_self_static
1207 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1299 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1456 |       -dlopen)
1843 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1916 | 	  # This library was specified with -dlopen.
2057 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2069 | 	passes="conv scan dlopen dlpreopen link"
2082 | 	dlopen) libs="$dlfiles" ;;
2087 |       if test "$pass" = dlopen; then
2266 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2267 | 	      # If there is no dlopen support or we're linking statically,
2300 | 	dlopen=
2321 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2364 | 	# This library was specified with -dlopen.
2365 | 	if test "$pass" = dlopen; then
2367 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2371 | 	     test "$dlopen_support" != yes ||
2373 | 	    # If there is no dlname, no dlopen support or we're linking
2382 | 	fi # $pass = dlopen
2435 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2810 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2811 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2962 |       if test "$pass" != dlopen; then
3063 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3130 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3768 | 	    $echo "*** a static module, that should work as long as the dlopening"
3769 | 	    $echo "*** application is linked with the -dlopen flag."
3787 | 	    $echo "*** or is declared to -dlopen it."
4197 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4329 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4330 | 	   test "$dlopen_self_static" = unknown; then
4331 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5669 | # The name that we can dlopen(3).
5692 | # Files to dlopen/dlpreopen
5693 | dlopen='$dlfiles'
6308 |     # Handle -dlopen flags immediately.
6337 | 	# Skip this library if it cannot be dlopened.
6362 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6722 |   -dlopen FILE      add the directory containing FILE to the library path
6724 | This mode sets the library path environment variable according to \`-dlopen'
6773 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6782 |   -module           build a library that can dlopened
{% endraw %}

```