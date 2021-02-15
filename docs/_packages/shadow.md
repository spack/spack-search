---
name: "shadow"
layout: package
next_package: clamr
previous_package: hsakmt-roct
languages: ['bash']
---
## 4.7
2 / 907 files match

 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)

### ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7346 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7414 | 	  # This library was specified with -dlopen.
7534 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7545 | 	passes="conv scan dlopen dlpreopen link"
7571 | 	dlopen) libs=$dlfiles ;;
7602 |       if test dlopen = "$pass"; then
7822 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7823 | 	      # If there is no dlopen support or we're linking statically,
7851 | 	dlopen=
7881 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7927 | 	# This library was specified with -dlopen.
7928 | 	if test dlopen = "$pass"; then
7930 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7932 | 	     test yes != "$dlopen_support" ||
7935 | 	    # If there is no dlname, no dlopen support or we're linking
7944 | 	fi # $pass = dlopen
8000 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8002 | 	      # We recover the dlopen module name by 'saving' the la file
8026 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8155 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8156 | 	  dlopenmodule=
8159 | 	      dlopenmodule=$dlpremoduletest
8163 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8260 | 		    # if the lib is a (non-dlopened) module then we cannot
8264 | 		      if test "X$dlopenmodule" != "X$lib"; then
8416 | 	      echo "*** a static module, that should work as long as the dlopening application"
8417 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8561 |       if test dlopen != "$pass"; then
8691 | 	func_warning "'-dlopen' is ignored for archives"
8758 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9455 | 	    echo "*** a static module, that should work as long as the dlopening"
9456 | 	    echo "*** application is linked with the -dlopen flag."
9474 | 	    echo "*** or is declared to -dlopen it."
10086 | 	func_warning "'-dlopen' is ignored for objects"
10206 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10207 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10888 | # The name that we can dlopen(3).
10917 | # Files to dlopen/dlpreopen
10918 | dlopen='$dlfiles'
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1410 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
3707 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
3710 | m4_defun([_LT_TRY_DLOPEN_SELF],
3768 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
3801 | ])# _LT_TRY_DLOPEN_SELF
3804 | # LT_SYS_DLOPEN_SELF
3806 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
3808 | if test yes != "$enable_dlopen"; then
3809 |   enable_dlopen=unknown
3810 |   enable_dlopen_self=unknown
3811 |   enable_dlopen_self_static=unknown
3813 |   lt_cv_dlopen=no
3814 |   lt_cv_dlopen_libs=
3818 |     lt_cv_dlopen=load_add_on
3819 |     lt_cv_dlopen_libs=
3820 |     lt_cv_dlopen_self=yes
3824 |     lt_cv_dlopen=LoadLibrary
3825 |     lt_cv_dlopen_libs=
3829 |     lt_cv_dlopen=dlopen
3830 |     lt_cv_dlopen_libs=
3835 |     AC_CHECK_LIB([dl], [dlopen],
3836 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
3837 |     lt_cv_dlopen=dyld
3838 |     lt_cv_dlopen_libs=
3839 |     lt_cv_dlopen_self=yes
3846 |     lt_cv_dlopen=dlopen
3847 |     lt_cv_dlopen_libs=
3848 |     lt_cv_dlopen_self=no
3853 | 	  [lt_cv_dlopen=shl_load],
3855 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
3856 | 	[AC_CHECK_FUNC([dlopen],
3857 | 	      [lt_cv_dlopen=dlopen],
3858 | 	  [AC_CHECK_LIB([dl], [dlopen],
3859 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
3860 | 	    [AC_CHECK_LIB([svld], [dlopen],
3861 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
3863 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
3872 |   if test no = "$lt_cv_dlopen"; then
3873 |     enable_dlopen=no
3875 |     enable_dlopen=yes
3878 |   case $lt_cv_dlopen in
3879 |   dlopen)
3887 |     LIBS="$lt_cv_dlopen_libs $LIBS"
3889 |     AC_CACHE_CHECK([whether a program can dlopen itself],
3890 | 	  lt_cv_dlopen_self, [dnl
3891 | 	  _LT_TRY_DLOPEN_SELF(
3892 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
3893 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
3896 |     if test yes = "$lt_cv_dlopen_self"; then
3898 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
3899 | 	  lt_cv_dlopen_self_static, [dnl
3900 | 	  _LT_TRY_DLOPEN_SELF(
3901 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
3902 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
3912 |   case $lt_cv_dlopen_self in
3913 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
3914 |   *) enable_dlopen_self=unknown ;;
3917 |   case $lt_cv_dlopen_self_static in
3918 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
3919 |   *) enable_dlopen_self_static=unknown ;;
3922 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
3923 | 	 [Whether dlopen is supported])
3924 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
3925 | 	 [Whether dlopen of programs is supported])
3926 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
3927 | 	 [Whether dlopen of statically linked programs is supported])
3928 | ])# LT_SYS_DLOPEN_SELF
3931 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
3933 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
8027 |     [Compiler flag to allow reflexive dlopens])
8136 |   LT_SYS_DLOPEN_SELF
10331 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
10365 | # dlopen
10367 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
10370 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
10371 | [_LT_SET_OPTION([LT_INIT], [dlopen])
10374 | put the 'dlopen' option into LT_INIT's first parameter.])
10378 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
10892 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```