---
name: "sbml"
layout: package
next_package: tcl-tclxml
previous_package: flux-sched
languages: ['bash']
---
## 5.18.0
5 / 12299 files match

 - [config/libtool.m4](#configlibtoolm4)
 - [config/makefile-common-actions.mk](#configmakefile-common-actionsmk)
 - [config/ltmain.sh](#configltmainsh)
 - [src/bindings/matlab/Makefile.in](#srcbindingsmatlabmakefilein)
 - [src/bindings/matlab/test/Makefile.in](#srcbindingsmatlabtestmakefilein)

### config/libtool.m4

```

{% raw %}
200 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
915 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
918 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
974 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1003 | ])# _LT_AC_TRY_DLOPEN_SELF
1006 | # AC_LIBTOOL_DLOPEN_SELF
1008 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1010 | if test "x$enable_dlopen" != xyes; then
1011 |   enable_dlopen=unknown
1012 |   enable_dlopen_self=unknown
1013 |   enable_dlopen_self_static=unknown
1015 |   lt_cv_dlopen=no
1016 |   lt_cv_dlopen_libs=
1020 |     lt_cv_dlopen="load_add_on"
1021 |     lt_cv_dlopen_libs=
1022 |     lt_cv_dlopen_self=yes
1026 |     lt_cv_dlopen="LoadLibrary"
1027 |     lt_cv_dlopen_libs=
1031 |     lt_cv_dlopen="dlopen"
1032 |     lt_cv_dlopen_libs=
1037 |     AC_CHECK_LIB([dl], [dlopen],
1038 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1039 |     lt_cv_dlopen="dyld"
1040 |     lt_cv_dlopen_libs=
1041 |     lt_cv_dlopen_self=yes
1047 | 	  [lt_cv_dlopen="shl_load"],
1049 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1050 | 	[AC_CHECK_FUNC([dlopen],
1051 | 	      [lt_cv_dlopen="dlopen"],
1052 | 	  [AC_CHECK_LIB([dl], [dlopen],
1053 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1054 | 	    [AC_CHECK_LIB([svld], [dlopen],
1055 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1057 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1066 |   if test "x$lt_cv_dlopen" != xno; then
1067 |     enable_dlopen=yes
1069 |     enable_dlopen=no
1072 |   case $lt_cv_dlopen in
1073 |   dlopen)
1081 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1083 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1084 | 	  lt_cv_dlopen_self, [dnl
1085 | 	  _LT_AC_TRY_DLOPEN_SELF(
1086 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1087 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1090 |     if test "x$lt_cv_dlopen_self" = xyes; then
1092 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1093 |     	  lt_cv_dlopen_self_static, [dnl
1094 | 	  _LT_AC_TRY_DLOPEN_SELF(
1095 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1096 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1106 |   case $lt_cv_dlopen_self in
1107 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1108 |   *) enable_dlopen_self=unknown ;;
1111 |   case $lt_cv_dlopen_self_static in
1112 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1113 |   *) enable_dlopen_self_static=unknown ;;
1116 | ])# AC_LIBTOOL_DLOPEN_SELF
2014 | # AC_LIBTOOL_DLOPEN
2016 | # enable checks for dlopen support
2017 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2019 | ])# AC_LIBTOOL_DLOPEN
2821 | AC_LIBTOOL_DLOPEN_SELF
4546 | # Whether dlopen is supported.
4547 | dlopen_support=$enable_dlopen
4549 | # Whether dlopen of programs is supported.
4550 | dlopen_self=$enable_dlopen_self
4552 | # Whether dlopen of statically linked programs is supported.
4553 | dlopen_self_static=$enable_dlopen_self_static
4561 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### config/makefile-common-actions.mk

```

{% raw %}
763 | 	env DYLD_LIBRARY_PATH=".:$(RUN_LDPATH):$(DYLD_LIBRARY_PATH)" srcdir=$(realpath .) $(LIBTOOL) -dlopen $(TOP_BUILDDIR)/src/libsbml.la --mode=execute $(1)
769 | 	env LD_LIBRARY_PATH=".:$(RUN_LDPATH):$(LD_LIBRARY_PATH)" srcdir=$(realpath .) $(LIBTOOL) -dlopen $(TOP_BUILDDIR)/src/libsbml.la --mode=execute $(1)
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
557 |   -dlopen)
558 |     prevopt="-dlopen"
642 |   # Only execute mode is allowed to have -dlopen flags.
644 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1185 | 	    dlopen_self=$dlopen_self_static
1191 | 	    dlopen_self=$dlopen_self_static
1197 | 	    dlopen_self=$dlopen_self_static
1254 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1346 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1503 |       -dlopen)
1896 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1969 | 	  # This library was specified with -dlopen.
2110 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2122 | 	passes="conv scan dlopen dlpreopen link"
2135 | 	dlopen) libs="$dlfiles" ;;
2140 |       if test "$pass" = dlopen; then
2324 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2325 | 	      # If there is no dlopen support or we're linking statically,
2358 | 	dlopen=
2379 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2422 | 	# This library was specified with -dlopen.
2423 | 	if test "$pass" = dlopen; then
2425 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2429 | 	     test "$dlopen_support" != yes ||
2431 | 	    # If there is no dlname, no dlopen support or we're linking
2440 | 	fi # $pass = dlopen
2493 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2870 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2871 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
3028 |       if test "$pass" != dlopen; then
3130 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3197 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3837 | 	    $echo "*** a static module, that should work as long as the dlopening"
3838 | 	    $echo "*** application is linked with the -dlopen flag."
3856 | 	    $echo "*** or is declared to -dlopen it."
4270 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4404 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4405 | 	   test "$dlopen_self_static" = unknown; then
4406 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5758 | # The name that we can dlopen(3).
5781 | # Files to dlopen/dlpreopen
5782 | dlopen='$dlfiles'
6397 |     # Handle -dlopen flags immediately.
6426 | 	# Skip this library if it cannot be dlopened.
6453 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6813 |   -dlopen FILE      add the directory containing FILE to the library path
6815 | This mode sets the library path environment variable according to \`-dlopen'
6864 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6873 |   -module           build a library that can dlopened
{% endraw %}

```
### src/bindings/matlab/Makefile.in

```

{% raw %}
153 |     $(LIBTOOL) -dlopen $(TOP_BUILDDIR)/src/libsbml.la --mode=execute $(1)
{% endraw %}

```
### src/bindings/matlab/test/Makefile.in

```

{% raw %}
131 |     $(LIBTOOL) -dlopen $(TOP_BUILDDIR)/src/libsbml.la --mode=execute $(1)
{% endraw %}

```