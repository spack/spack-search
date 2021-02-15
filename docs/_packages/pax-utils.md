---
name: "pax-utils"
layout: package
next_package: foundationdb
previous_package: py-quast
languages: ['bash', 'cpp', 'python']
---
## 1.2.2
8 / 385 files match

 - [elf.h](#elfh)
 - [lddtree.py](#lddtreepy)
 - [macho.h](#machoh)
 - [autotools/ltmain.sh](#autotoolsltmainsh)
 - [autotools/m4/libtool.m4](#autotoolsm4libtoolm4)
 - [autotools/m4/ltoptions.m4](#autotoolsm4ltoptionsm4)
 - [man/scanmacho.docbook](#manscanmachodocbook)
 - [man/scanmacho.1](#manscanmacho1)

### elf.h

```cpp

{% raw %}
1707 | 					   by rld on dlopen() calls.  */
{% endraw %}

```
### lddtree.py

```python

{% raw %}
606 |   # is copied over (since we know it can be dlopen-ed by NPTL at runtime).
609 |   # for known libs that get loaded (e.g. curl will dlopen(libresolv)).
{% endraw %}

```
### macho.h

```cpp

{% raw %}
61 | #define MH_BUNDLE   0x8     /* dlopen plugin (.bundle) */
{% endraw %}

```
### autotools/ltmain.sh

```bash

{% raw %}
2309 |     opt_dlopen=
2370 |         --dlopen|-dlopen)
2371 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2487 |       # Only execute mode is allowed to have -dlopen flags.
2488 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2489 |         func_error "unrecognized option '-dlopen'"
3715 |   -dlopen FILE      add the directory containing FILE to the library path
3717 | This mode sets the library path environment variable according to '-dlopen'
3772 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3781 |   -module           build a library that can dlopened
3889 |     # Handle -dlopen flags immediately.
3890 |     for file in $opt_dlopen; do
3909 | 	# Skip this library if it cannot be dlopened.
3936 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6630 | 	    dlopen_self=$dlopen_self_static
6636 | 	    dlopen_self=$dlopen_self_static
6642 | 	    dlopen_self=$dlopen_self_static
6700 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6790 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6957 |       -dlopen)
7395 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7463 | 	  # This library was specified with -dlopen.
7583 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7594 | 	passes="conv scan dlopen dlpreopen link"
7620 | 	dlopen) libs=$dlfiles ;;
7648 |       if test dlopen = "$pass"; then
7868 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7869 | 	      # If there is no dlopen support or we're linking statically,
7897 | 	dlopen=
7927 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7973 | 	# This library was specified with -dlopen.
7974 | 	if test dlopen = "$pass"; then
7976 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7978 | 	     test yes != "$dlopen_support" ||
7981 | 	    # If there is no dlname, no dlopen support or we're linking
7990 | 	fi # $pass = dlopen
8046 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8048 | 	      # We recover the dlopen module name by 'saving' the la file
8072 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8201 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8202 | 	  dlopenmodule=
8205 | 	      dlopenmodule=$dlpremoduletest
8209 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8306 | 		    # if the lib is a (non-dlopened) module then we cannot
8310 | 		      if test "X$dlopenmodule" != "X$lib"; then
8462 | 	      echo "*** a static module, that should work as long as the dlopening application"
8463 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8607 |       if test dlopen != "$pass"; then
8737 | 	func_warning "'-dlopen' is ignored for archives"
8804 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9498 | 	    echo "*** a static module, that should work as long as the dlopening"
9499 | 	    echo "*** application is linked with the -dlopen flag."
9517 | 	    echo "*** or is declared to -dlopen it."
10129 | 	func_warning "'-dlopen' is ignored for objects"
10249 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10250 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10932 | # The name that we can dlopen(3).
10961 | # Files to dlopen/dlpreopen
10962 | dlopen='$dlfiles'
{% endraw %}

```
### autotools/m4/libtool.m4

```

{% raw %}
1821 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1824 | m4_defun([_LT_TRY_DLOPEN_SELF],
1882 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1915 | ])# _LT_TRY_DLOPEN_SELF
1918 | # LT_SYS_DLOPEN_SELF
1920 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1922 | if test yes != "$enable_dlopen"; then
1923 |   enable_dlopen=unknown
1924 |   enable_dlopen_self=unknown
1925 |   enable_dlopen_self_static=unknown
1927 |   lt_cv_dlopen=no
1928 |   lt_cv_dlopen_libs=
1932 |     lt_cv_dlopen=load_add_on
1933 |     lt_cv_dlopen_libs=
1934 |     lt_cv_dlopen_self=yes
1938 |     lt_cv_dlopen=LoadLibrary
1939 |     lt_cv_dlopen_libs=
1943 |     lt_cv_dlopen=dlopen
1944 |     lt_cv_dlopen_libs=
1949 |     AC_CHECK_LIB([dl], [dlopen],
1950 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1951 |     lt_cv_dlopen=dyld
1952 |     lt_cv_dlopen_libs=
1953 |     lt_cv_dlopen_self=yes
1960 |     lt_cv_dlopen=dlopen
1961 |     lt_cv_dlopen_libs=
1962 |     lt_cv_dlopen_self=no
1967 | 	  [lt_cv_dlopen=shl_load],
1969 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1970 | 	[AC_CHECK_FUNC([dlopen],
1971 | 	      [lt_cv_dlopen=dlopen],
1972 | 	  [AC_CHECK_LIB([dl], [dlopen],
1973 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1974 | 	    [AC_CHECK_LIB([svld], [dlopen],
1975 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1977 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1986 |   if test no = "$lt_cv_dlopen"; then
1987 |     enable_dlopen=no
1989 |     enable_dlopen=yes
1992 |   case $lt_cv_dlopen in
1993 |   dlopen)
2001 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2003 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2004 | 	  lt_cv_dlopen_self, [dnl
2005 | 	  _LT_TRY_DLOPEN_SELF(
2006 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2007 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2010 |     if test yes = "$lt_cv_dlopen_self"; then
2012 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2013 | 	  lt_cv_dlopen_self_static, [dnl
2014 | 	  _LT_TRY_DLOPEN_SELF(
2015 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2016 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2026 |   case $lt_cv_dlopen_self in
2027 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2028 |   *) enable_dlopen_self=unknown ;;
2031 |   case $lt_cv_dlopen_self_static in
2032 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2033 |   *) enable_dlopen_self_static=unknown ;;
2036 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2037 | 	 [Whether dlopen is supported])
2038 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2039 | 	 [Whether dlopen of programs is supported])
2040 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2041 | 	 [Whether dlopen of statically linked programs is supported])
2042 | ])# LT_SYS_DLOPEN_SELF
2045 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2047 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6135 |     [Compiler flag to allow reflexive dlopens])
6248 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### autotools/m4/ltoptions.m4

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
### man/scanmacho.docbook

```

{% raw %}
222 |    <listitem><para><emphasis remap='B'>MH_BUNDLE</emphasis> - dlopen plugin (.bundle)</para></listitem>
{% endraw %}

```
### man/scanmacho.1

```

{% raw %}
298 | \- dlopen plugin (\&.bundle)
{% endraw %}

```