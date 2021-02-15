---
name: "sollya"
layout: package
next_package: r-rcppcctz
previous_package: cbtf
languages: ['cpp', 'bash']
---
## 7.0
9 / 1132 files match

 - [configure.ac](#configureac)
 - [library.c](#libraryc)
 - [help.h](#helph)
 - [external.c](#externalc)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)
 - [doc/libraryconstant.tex](#doclibraryconstanttex)
 - [doc/library.tex](#doclibrarytex)

### configure.ac

```

{% raw %}
46 | AC_LIBTOOL_DLOPEN
47 | LT_INIT([dlopen shared])   # AC_PROG_RANLIB is superseeded by LT_INIT
363 | dlopen_ok="yes"
364 | AC_CHECK_LIB([c], [dlopen], [], [dlopen_ok="no"])
365 | if test "x${dlopen_ok}y" = "xnoy" ; then
366 |   AC_CHECK_LIB([dl], [dlopen], [], AC_MSG_ERROR([libdl unusable]))
{% endraw %}

```
### library.c

```cpp

{% raw %}
524 |     dlfcnHandle = dlopen(libraryName, RTLD_LOCAL | RTLD_NOW);
{% endraw %}

```
### help.h

```cpp

{% raw %}
177 | #define HELP_LIBRARYCONSTANT_TEXT "Name: libraryconstant\n==> binds an external mathematical constant to a variable in Sollya\n\nLibrary names:\n   sollya_obj_t sollya_lib_libraryconstant(char *, void (*)(mpfr_t, mp_prec_t))\n   sollya_obj_t sollya_lib_build_function_libraryconstant(char *,\n                                                          void (*)(mpfr_t,\n                                                                   mp_prec_t))\n   sollya_obj_t sollya_lib_libraryconstant_with_data(char *,\n                                                     void (*)(mpfr_t,\n                                                              mp_prec_t,\n                                                              void *),\n                                                     void *,\n                                                     void (*)(void *))\n   sollya_obj_t sollya_lib_build_function_libraryconstant_with_data(\n                                                     char *,\n                                                     void (*)(mpfr_t,\n                                                              mp_prec_t,\n                                                              void *),\n                                                     void *,\n                                                     void (*)(void *))\n\nUsage: \n   libraryconstant({path}) : string -> function\n\nDescription: \n   * The command libraryconstant lets you extend the set of mathematical\n   constants known to Sollya.\n   By default, the only mathematical constant known by Sollya is pi.\n   For particular applications, one may want to\n   manipulate other constants, such as Euler's gamma constant, for instance.\n\n   * libraryconstant makes it possible to let Sollya know about new constants.\n   In order to let it know, you have to provide an implementation of the\n   constant you are interested in. This implementation is a C file containing\n   a function of the form:\n                 void my_ident(mpfr_t result, mp_prec_t prec) \n   The semantic of this function is the following: it is an implementation of\n   the constant in arbitrary precision.\n   my_ident(result, prec) shall set the\n   precision of the variable result to a suitable precision (the variable is\n   assumed to be already initialized) and store in result an approximate value\n   of the constant with a relative error not greater than 2^(1-prec).\n   More precisely, if c is the exact value of the constant, the value stored\n   in result should satisfy |result-c| <= 2^(1-prec)*|c|.\n\n   * You can include sollya.h in your implementation and use library \n   functionnalities of Sollya for your implementation. However, this requires to\n   have compiled Sollya with -fPIC in order to make the Sollya executable\n   code position independent and to use a system on with programs, using dlopen\n   to open dynamic routines can dynamically open themselves.\n\n   * To bind your constant into Sollya, you must use the same identifier as the\n   function name used in your implementation file (my_ident in the previous\n   example). Once the function code has been bound to an identifier, you can use\n   a simple assignment to assign the bound identifier to yet another identifier.\n   This way, you may use convenient names inside Sollya even if your\n   implementation environment requires you to use a less convenient name.\n\n   * Once your constant is bound, it is considered by Sollya as an infinitely\n   accurate constant (i.e. a 0-ary function, exactly like pi).\n\n   * The dynamic object file whose name is given to libraryconstant for binding of an\n   external library constant may also define a destructor function int sollya_external_lib_close(void).\n   If Sollya finds such a destructor function in the dynamic object file, it will call \n   that function when closing the dynamic object file again. This happens when Sollya\n   is terminated or when the current Sollya session is restarted using restart.\n   The purpose of the destructor function is to allow the dynamically bound code\n   to free any memory that it might have allocated before Sollya is terminated \n   or restarted. \n   The dynamic object file is not necessarily needed to define a destructor\n   function. This ensure backward compatibility with older Sollya external \n   library function object files.\n   When defined, the destructor function is supposed to return an integer\n   value indicating if an error has happened. Upon success, the destructor\n   functions is to return a zero value, upon error a non-zero value.\n\nExample 1: \n   > bashexecute(\"gcc -fPIC -Wall -c libraryconstantexample.c -I$HOME/.local/include\");\n   > bashexecute(\"gcc -shared -o libraryconstantexample libraryconstantexample.o -lgmp -lmpfr\");\n   > euler_gamma = libraryconstant(\"./libraryconstantexample\");\n   > prec = 20!;\n   > euler_gamma;\n   0.577215\n   > prec = 100!;\n   > euler_gamma;\n   0.577215664901532860606512090082\n   > midpointmode = on;\n   Midpoint mode has been activated.\n   > [euler_gamma];\n   0.57721566490153286060651209008~2/4~\n\nSee also: bashexecute, externalproc, externalplot, pi, library, evaluate, implementconstant\n"
178 | #define HELP_LIBRARY_TEXT "Name: library\n==> binds an external mathematical function to a variable in Sollya\n\nLibrary names:\n   sollya_obj_t sollya_lib_libraryfunction(sollya_obj_t, char *,\n                                           int (*)(mpfi_t, mpfi_t, int))\n   sollya_obj_t sollya_lib_build_function_libraryfunction(sollya_obj_t, char *,\n                                                          int (*)(mpfi_t,\n                                                                  mpfi_t, int))\n   sollya_obj_t sollya_lib_libraryfunction_with_data(\n                                           sollya_obj_t, char *,\n                                           int (*)(mpfi_t, mpfi_t, int, void *),\n                                           void *, void (*)(void *))\n   sollya_obj_t sollya_lib_build_function_libraryfunction_with_data(\n                                           sollya_obj_t, char *,\n                                           int (*)(mpfi_t,\n                                                   mpfi_t, int, void *),\n                                           void *, void (*)(void *))\n\nUsage: \n   library({path}) : string -> function\n\nDescription: \n   * The command library lets you extend the set of mathematical\n   functions known to Sollya.\n   By default, Sollya knows the most common mathematical functions such\n   as exp, sin, erf, etc. Within Sollya, these functions may be\n   composed. This way, Sollya should satisfy the needs of a lot of\n   users. However, for particular applications, one may want to\n   manipulate other functions such as Bessel functions, or functions\n   defined by an integral or even a particular solution of an ODE.\n\n   * library makes it possible to let Sollya know about new functions. In\n   order to let it know, you have to provide an implementation of the\n   function you are interested in. This implementation is a C file containing\n   a function of the form:\n                 int my_ident(sollya_mpfi_t result, sollya_mpfi_t op, int n) \n   The semantic of this function is the following: it is an implementation of\n   the function and its derivatives in interval arithmetic.\n   my_ident(result, I, n) shall store in result an enclosure \n   of the image set of the n-th derivative\n   of the function f over I: f^(n)(I) C result.\n\n   * The integer value returned by the function implementation currently has no\n   meaning.\n\n   * You do not need to provide a working implementation for any n. Most\n   functions of Sollya requires a relevant implementation only for f,\n   f' and f''. For higher derivatives, its is not so critical and the\n   implementation may just store [-Inf, +Inf] in result whenever n>2.\n\n   * Note that you should respect somehow interval-arithmetic standards in your\n   implementation: result has its own precision and you should perform the \n   intermediate computations so that result is as tight as possible.\n\n   * You can include sollya.h in your implementation and use library \n   functionnalities of Sollya for your implementation. However, this requires to\n   have compiled Sollya with -fPIC in order to make the Sollya executable code\n   position independent and to use a system on with programs, using dlopen to\n   open dynamic routines can dynamically open themselves. IMPORTANT NOTICE: as\n   the code will be run in a context where a sollya session is already opened,\n   the library functions must be used directly, without calling sollya_lib_init\n   and sollya_lib_close (calling these functions would conflict with the\n   current session, leading to weird and hard to debug behaviors).\n\n   * To bind your function into Sollya, you must use the same identifier as the\n   function name used in your implementation file (my_ident in the previous\n   example). Once the function code has been bound to an identifier, you can use\n   a simple assignment to assign the bound identifier to yet another identifier.\n   This way, you may use convenient names inside Sollya even if your\n   implementation environment requires you to use a less convenient name.\n\n   * The dynamic object file whose name is given to library for binding of an\n   external library function may also define a destructor function\n     int sollya_external_lib_close(void).\n   If Sollya finds such a destructor function in the dynamic object file, it\n   will call that function when closing the dynamic object file again.\n   This happens when Sollya is terminated or when the current Sollya session\n   is restarted using restart.\n   The purpose of the destructor function is to allow the dynamically bound code\n   to free any memory that it might have allocated before Sollya is terminated \n   or restarted. \n   The dynamic object file is not necessarily needed to define a destructor\n   function. This ensure backward compatibility with older Sollya external \n   library function object files.\n   When defined, the destructor function is supposed to return an integer\n   value indicating if an error has happened. Upon success, the destructor\n   functions is to return a zero value, upon error a non-zero value.\n\nExample 1: \n   > bashexecute(\"gcc -fPIC -Wall -c libraryexample.c -I$HOME/.local/include\");\n   > bashexecute(\"gcc -shared -o libraryexample libraryexample.o -lgmp -lmpfr\");\n   > myownlog = library(\"./libraryexample\");\n   > evaluate(log(x), 2);\n   0.69314718055994530941723212145817656807550013436025\n   > evaluate(myownlog(x), 2);\n   0.69314718055994530941723212145817656807550013436025\n\nSee also: function, bashexecute, externalproc, externalplot, diff, evaluate, libraryconstant\n"
{% endraw %}

```
### external.c

```cpp

{% raw %}
313 |   descr = dlopen(library, RTLD_NOW);
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1820 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1823 | m4_defun([_LT_TRY_DLOPEN_SELF],
1881 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1914 | ])# _LT_TRY_DLOPEN_SELF
1917 | # LT_SYS_DLOPEN_SELF
1919 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1921 | if test yes != "$enable_dlopen"; then
1922 |   enable_dlopen=unknown
1923 |   enable_dlopen_self=unknown
1924 |   enable_dlopen_self_static=unknown
1926 |   lt_cv_dlopen=no
1927 |   lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen=load_add_on
1932 |     lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen_self=yes
1937 |     lt_cv_dlopen=LoadLibrary
1938 |     lt_cv_dlopen_libs=
1942 |     lt_cv_dlopen=dlopen
1943 |     lt_cv_dlopen_libs=
1948 |     AC_CHECK_LIB([dl], [dlopen],
1949 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1950 |     lt_cv_dlopen=dyld
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1959 |     lt_cv_dlopen=dlopen
1960 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen_self=no
1966 | 	  [lt_cv_dlopen=shl_load],
1968 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1969 | 	[AC_CHECK_FUNC([dlopen],
1970 | 	      [lt_cv_dlopen=dlopen],
1971 | 	  [AC_CHECK_LIB([dl], [dlopen],
1972 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1973 | 	    [AC_CHECK_LIB([svld], [dlopen],
1974 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1976 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1985 |   if test no = "$lt_cv_dlopen"; then
1986 |     enable_dlopen=no
1988 |     enable_dlopen=yes
1991 |   case $lt_cv_dlopen in
1992 |   dlopen)
2000 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2002 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2003 | 	  lt_cv_dlopen_self, [dnl
2004 | 	  _LT_TRY_DLOPEN_SELF(
2005 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2006 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2009 |     if test yes = "$lt_cv_dlopen_self"; then
2011 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2012 | 	  lt_cv_dlopen_self_static, [dnl
2013 | 	  _LT_TRY_DLOPEN_SELF(
2014 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2015 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2025 |   case $lt_cv_dlopen_self in
2026 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2027 |   *) enable_dlopen_self=unknown ;;
2030 |   case $lt_cv_dlopen_self_static in
2031 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2032 |   *) enable_dlopen_self_static=unknown ;;
2035 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2036 | 	 [Whether dlopen is supported])
2037 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2038 | 	 [Whether dlopen of programs is supported])
2039 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2040 | 	 [Whether dlopen of statically linked programs is supported])
2041 | ])# LT_SYS_DLOPEN_SELF
2044 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2046 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6140 |     [Compiler flag to allow reflexive dlopens])
6253 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
107 | # dlopen
109 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
112 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
113 | [_LT_SET_OPTION([LT_INIT], [dlopen])
116 | put the 'dlopen' option into LT_INIT's first parameter.])
120 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### build-aux/ltmain.sh

```bash

{% raw %}
2431 |     opt_dlopen=
2504 |         --dlopen|-dlopen)
2505 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2628 |       # Only execute mode is allowed to have -dlopen flags.
2629 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2630 |         func_error "unrecognized option '-dlopen'"
3856 |   -dlopen FILE      add the directory containing FILE to the library path
3858 | This mode sets the library path environment variable according to '-dlopen'
3913 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3922 |   -module           build a library that can dlopened
4030 |     # Handle -dlopen flags immediately.
4031 |     for file in $opt_dlopen; do
4050 | 	# Skip this library if it cannot be dlopened.
4077 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6771 | 	    dlopen_self=$dlopen_self_static
6777 | 	    dlopen_self=$dlopen_self_static
6783 | 	    dlopen_self=$dlopen_self_static
6841 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6931 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7098 |       -dlopen)
7535 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7603 | 	  # This library was specified with -dlopen.
7723 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7734 | 	passes="conv scan dlopen dlpreopen link"
7760 | 	dlopen) libs=$dlfiles ;;
7791 |       if test dlopen = "$pass"; then
8011 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
8012 | 	      # If there is no dlopen support or we're linking statically,
8040 | 	dlopen=
8070 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8116 | 	# This library was specified with -dlopen.
8117 | 	if test dlopen = "$pass"; then
8119 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8121 | 	     test yes != "$dlopen_support" ||
8124 | 	    # If there is no dlname, no dlopen support or we're linking
8133 | 	fi # $pass = dlopen
8189 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8191 | 	      # We recover the dlopen module name by 'saving' the la file
8215 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8344 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8345 | 	  dlopenmodule=
8348 | 	      dlopenmodule=$dlpremoduletest
8352 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8449 | 		    # if the lib is a (non-dlopened) module then we cannot
8453 | 		      if test "X$dlopenmodule" != "X$lib"; then
8605 | 	      echo "*** a static module, that should work as long as the dlopening application"
8606 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8750 |       if test dlopen != "$pass"; then
8880 | 	func_warning "'-dlopen' is ignored for archives"
8947 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9644 | 	    echo "*** a static module, that should work as long as the dlopening"
9645 | 	    echo "*** application is linked with the -dlopen flag."
9663 | 	    echo "*** or is declared to -dlopen it."
10275 | 	func_warning "'-dlopen' is ignored for objects"
10395 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10396 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
11078 | # The name that we can dlopen(3).
11107 | # Files to dlopen/dlpreopen
11108 | dlopen='$dlfiles'
{% endraw %}

```
### doc/libraryconstant.tex

```

{% raw %}
51 |    code position independent and to use a system on with programs, using \texttt{dlopen}
{% endraw %}

```
### doc/library.tex

```

{% raw %}
60 |    position independent and to use a system on with programs, using \texttt{dlopen} to
{% endraw %}

```