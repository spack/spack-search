---
name: "gettext"
layout: package
next_package: rsyslog
previous_package: kcov
languages: ['cpp', 'bash']
---
## 0.20.1
22 / 5109 files match

 - [gettext-runtime/intl/libgnuintl.in.h](#gettext-runtimeintllibgnuintlinh)
 - [gettext-runtime/gnulib-m4/lib-link.m4](#gettext-runtimegnulib-m4lib-linkm4)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [gettext-tools/config.h.in](#gettext-toolsconfighin)
 - [gettext-tools/tests/mm-viet.comp.po](#gettext-toolstestsmm-vietcomppo)
 - [gettext-tools/gnulib-lib/libxml/xmlmodule.c](#gettext-toolsgnulib-liblibxmlxmlmodulec)
 - [gettext-tools/gnulib-m4/libxml.m4](#gettext-toolsgnulib-m4libxmlm4)
 - [gettext-tools/gnulib-m4/lib-link.m4](#gettext-toolsgnulib-m4lib-linkm4)
 - [gettext-tools/examples/hello-c++-kde/admin/acinclude.m4.in](#gettext-toolsexampleshello-c++-kdeadminacincludem4in)
 - [gettext-tools/examples/hello-c++-kde/admin/ltmain.sh](#gettext-toolsexampleshello-c++-kdeadminltmainsh)
 - [gettext-tools/examples/hello-c++-kde/admin/libtool.m4.in](#gettext-toolsexampleshello-c++-kdeadminlibtoolm4in)
 - [gnulib-local/lib/libxml/xmlmodule.c](#gnulib-localliblibxmlxmlmodulec)
 - [gnulib-local/m4/libxml.m4](#gnulib-localm4libxmlm4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)
 - [libtextstyle/config.h.in](#libtextstyleconfighin)
 - [libtextstyle/lib/libxml/xmlmodule.c](#libtextstyleliblibxmlxmlmodulec)
 - [libtextstyle/m4/libtool.m4](#libtextstylem4libtoolm4)
 - [libtextstyle/m4/ltoptions.m4](#libtextstylem4ltoptionsm4)
 - [libtextstyle/gnulib-m4/libxml.m4](#libtextstylegnulib-m4libxmlm4)
 - [libtextstyle/gnulib-m4/lib-link.m4](#libtextstylegnulib-m4lib-linkm4)
 - [libtextstyle/build-aux/ltmain.sh](#libtextstylebuild-auxltmainsh)

### gettext-runtime/intl/libgnuintl.in.h

```cpp

{% raw %}
71 |      4. in the dlopen()ed shared libraries, in the order in which they were
72 |         dlopen()ed.
77 |      * libintl.so is a dependency of a dlopen()ed shared library but not
{% endraw %}

```
### gettext-runtime/gnulib-m4/lib-link.m4

```

{% raw %}
516 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### m4/libtool.m4

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
6122 |     [Compiler flag to allow reflexive dlopens])
6235 |   LT_SYS_DLOPEN_SELF
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
### gettext-tools/config.h.in

```

{% raw %}
938 | /* Define to 1 if you have the `dlopen' function. */
939 | #undef HAVE_DLOPEN
{% endraw %}

```
### gettext-tools/tests/mm-viet.comp.po

```

{% raw %}
49477 | msgid "dlopen returned \"%return:1\"."
49478 | msgstr "lệnh dlopen đã gọi « %return:1 »."
{% endraw %}

```
### gettext-tools/gnulib-lib/libxml/xmlmodule.c

```cpp

{% raw %}
205 | #if defined(HAVE_DLOPEN) && !defined(_WIN32)
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
256 | #else /* ! HAVE_DLOPEN */
301 | #endif /* ! HAVE_DLOPEN */
{% endraw %}

```
### gettext-tools/gnulib-m4/libxml.m4

```

{% raw %}
204 |     AC_CHECK_FUNCS([dlopen getaddrinfo localtime shlload stat strftime])
{% endraw %}

```
### gettext-tools/gnulib-m4/lib-link.m4

```

{% raw %}
516 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### gettext-tools/examples/hello-c++-kde/admin/acinclude.m4.in

```

{% raw %}
2940 | AC_REQUIRE([AC_LIBTOOL_DLOPEN])
3676 | AC_CHECK_LIB(dl, dlopen, [
3689 | AC_DEFUN(KDE_CHECK_DLOPEN,
3701 | dnl XXX why change enable_dlopen? its already set by autoconf's AC_ARG_ENABLE
3703 | AC_ARG_ENABLE(dlopen,
3704 | [  --disable-dlopen        link statically [default=no]] ,
3705 | enable_dlopen=$enableval,
3706 | enable_dlopen=yes)
3710 |   enable_dlopen=no
3721 | if test "$enable_dlopen" = no ; then
3731 | KDE_CHECK_DLOPEN(libtool_enable_shared=yes, libtool_enable_static=no)
3735 | if test "$build_libtool_libs" = "yes" && test "$enable_dlopen" = "yes"; then
{% endraw %}

```
### gettext-tools/examples/hello-c++-kde/admin/ltmain.sh

```bash

{% raw %}
227 |   -dlopen)
228 |     prevopt="-dlopen"
298 |   # Only execute mode is allowed to have -dlopen flags.
300 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
871 | 	    dlopen_self=$dlopen_self_static
875 | 	    dlopen_self=$dlopen_self_static
932 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1014 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1146 |       -dlopen)
1438 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1506 | 	  # This library was specified with -dlopen.
1683 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
1695 | 	passes="conv scan dlopen dlpreopen link"
1708 | 	dlopen) libs="$dlfiles" ;;
1713 |       if test "$pass" = dlopen; then
1830 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
1831 | 	      # If there is no dlopen support or we're linking statically,
1864 | 	dlopen=
1882 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
1925 | 	# This library was specified with -dlopen.
1926 | 	if test "$pass" = dlopen; then
1928 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
1931 | 	  if test -z "$dlname" || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
1932 | 	    # If there is no dlname, no dlopen support or we're linking
1941 | 	fi # $pass = dlopen
1986 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2299 | 	      echo "*** a static module, that should work as long as the dlopening application"
2300 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2404 |       if test "$pass" != dlopen; then
2496 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
2561 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3104 | 	    echo "*** a static module, that should work as long as the dlopening"
3105 | 	    echo "*** application is linked with the -dlopen flag."
3123 | 	    echo "*** or is declared to -dlopen it."
3463 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
3621 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
3622 | 	   test "$dlopen_self_static" = unknown; then
3623 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
4467 | # The name that we can dlopen(3).
4487 | # Files to dlopen/dlpreopen
4488 | dlopen='$dlfiles'
5048 |     # Handle -dlopen flags immediately.
5077 | 	# Skip this library if it cannot be dlopened.
5102 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
5431 |   -dlopen FILE      add the directory containing FILE to the library path
5433 | This mode sets the library path environment variable according to \`-dlopen'
5482 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
5491 |   -module           build a library that can dlopened
{% endraw %}

```
### gettext-tools/examples/hello-c++-kde/admin/libtool.m4.in

```

{% raw %}
193 | ifdef([AC_PROVIDE_AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
646 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
649 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
705 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
732 | ])# _LT_AC_TRY_DLOPEN_SELF
735 | # AC_LIBTOOL_DLOPEN_SELF
737 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
739 | if test "x$enable_dlopen" != xyes; then
740 |   enable_dlopen=unknown
741 |   enable_dlopen_self=unknown
742 |   enable_dlopen_self_static=unknown
744 |   lt_cv_dlopen=no
745 |   lt_cv_dlopen_libs=
749 |     lt_cv_dlopen="load_add_on"
750 |     lt_cv_dlopen_libs=
751 |     lt_cv_dlopen_self=yes
755 |     lt_cv_dlopen="LoadLibrary"
756 |     lt_cv_dlopen_libs=
761 | 	  [lt_cv_dlopen="shl_load"],
763 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
764 | 	[AC_CHECK_FUNC([dlopen],
765 | 	      [lt_cv_dlopen="dlopen"],
766 | 	  [AC_CHECK_LIB([dl], [dlopen],
767 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
768 | 	    [AC_CHECK_LIB([svld], [dlopen],
769 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
771 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
780 |   if test "x$lt_cv_dlopen" != xno; then
781 |     enable_dlopen=yes
783 |     enable_dlopen=no
786 |   case $lt_cv_dlopen in
787 |   dlopen)
795 |     LIBS="$lt_cv_dlopen_libs $LIBS"
797 |     AC_CACHE_CHECK([whether a program can dlopen itself],
798 | 	  lt_cv_dlopen_self, [dnl
799 | 	  _LT_AC_TRY_DLOPEN_SELF(
800 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
801 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
804 |     if test "x$lt_cv_dlopen_self" = xyes; then
806 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
807 |     	  lt_cv_dlopen_self_static, [dnl
808 | 	  _LT_AC_TRY_DLOPEN_SELF(
809 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
810 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
820 |   case $lt_cv_dlopen_self in
821 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
822 |   *) enable_dlopen_self=unknown ;;
825 |   case $lt_cv_dlopen_self_static in
826 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
827 |   *) enable_dlopen_self_static=unknown ;;
830 | ])# AC_LIBTOOL_DLOPEN_SELF
1528 | # AC_LIBTOOL_DLOPEN
1530 | # enable checks for dlopen support
1531 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1533 | ])# AC_LIBTOOL_DLOPEN
2297 | AC_LIBTOOL_DLOPEN_SELF($1)
3146 | AC_LIBTOOL_DLOPEN_SELF($1)
3202 | AC_LIBTOOL_DLOPEN_SELF($1)
3486 | # Whether dlopen is supported.
3487 | dlopen_support=$enable_dlopen
3489 | # Whether dlopen of programs is supported.
3490 | dlopen_self=$enable_dlopen_self
3492 | # Whether dlopen of statically linked programs is supported.
3493 | dlopen_self_static=$enable_dlopen_self_static
3501 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### gnulib-local/lib/libxml/xmlmodule.c

```cpp

{% raw %}
205 | #if defined(HAVE_DLOPEN) && !defined(_WIN32)
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
256 | #else /* ! HAVE_DLOPEN */
301 | #endif /* ! HAVE_DLOPEN */
{% endraw %}

```
### gnulib-local/m4/libxml.m4

```

{% raw %}
204 |     AC_CHECK_FUNCS([dlopen getaddrinfo localtime shlload stat strftime])
{% endraw %}

```
### build-aux/ltmain.sh

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
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### libtextstyle/config.h.in

```

{% raw %}
232 | /* Define to 1 if you have the `dlopen' function. */
233 | #undef HAVE_DLOPEN
{% endraw %}

```
### libtextstyle/lib/libxml/xmlmodule.c

```cpp

{% raw %}
205 | #if defined(HAVE_DLOPEN) && !defined(_WIN32)
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
256 | #else /* ! HAVE_DLOPEN */
301 | #endif /* ! HAVE_DLOPEN */
{% endraw %}

```
### libtextstyle/m4/libtool.m4

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
6122 |     [Compiler flag to allow reflexive dlopens])
6235 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### libtextstyle/m4/ltoptions.m4

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
### libtextstyle/gnulib-m4/libxml.m4

```

{% raw %}
204 |     AC_CHECK_FUNCS([dlopen getaddrinfo localtime shlload stat strftime])
{% endraw %}

```
### libtextstyle/gnulib-m4/lib-link.m4

```

{% raw %}
516 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### libtextstyle/build-aux/ltmain.sh

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
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```