---
name: "fakechroot"
layout: package
next_package: canal
previous_package: mc
languages: ['cpp', 'bash']
---
## 2.20.1
9 / 293 files match

 - [config.h.in](#confighin)
 - [configure.ac](#configureac)
 - [NEWS.md](#newsmd)
 - [src/Makefile.am](#srcmakefileam)
 - [src/dlopen.c](#srcdlopenc)
 - [src/Makefile.in](#srcmakefilein)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)

### config.h.in

```

{% raw %}
185 | /* Define to 1 if you have the `dlopen' function. */
186 | #undef HAVE_DLOPEN
{% endraw %}

```
### configure.ac

```

{% raw %}
181 |     dlopen
{% endraw %}

```
### NEWS.md

```

{% raw %}
64 |   `dlopen`(3) function was fixed. The `java`(1) command should work correctly.
{% endraw %}

```
### src/Makefile.am

```

{% raw %}
47 |     dlopen.c \
{% endraw %}

```
### src/dlopen.c

```cpp

{% raw %}
27 | wrapper(dlopen, void *, (const char * filename, int flag))
31 |     debug("dlopen(\"%s\", %d)", filename, flag);
34 |         debug("dlopen(\"%s\", %d)", filename, flag);
36 |     return nextcall(dlopen)(filename, flag);
{% endraw %}

```
### src/Makefile.in

```

{% raw %}
151 | 	dedotdot.lo dl_iterate_phdr.lo dladdr.lo dlmopen.lo dlopen.lo \
221 | 	./$(DEPDIR)/dlmopen.Plo ./$(DEPDIR)/dlopen.Plo \
518 |     dlopen.c \
766 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/dlopen.Plo@am__quote@ # am--include-marker
1080 | 	-rm -f ./$(DEPDIR)/dlopen.Plo
1277 | 	-rm -f ./$(DEPDIR)/dlopen.Plo
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
6141 |     [Compiler flag to allow reflexive dlopens])
6254 |   LT_SYS_DLOPEN_SELF
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
2335 |     opt_dlopen=
2408 |         --dlopen|-dlopen)
2409 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2532 |       # Only execute mode is allowed to have -dlopen flags.
2533 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2534 |         func_error "unrecognized option '-dlopen'"
3760 |   -dlopen FILE      add the directory containing FILE to the library path
3762 | This mode sets the library path environment variable according to '-dlopen'
3817 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3826 |   -module           build a library that can dlopened
3934 |     # Handle -dlopen flags immediately.
3935 |     for file in $opt_dlopen; do
3954 | 	# Skip this library if it cannot be dlopened.
3981 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6674 | 	    dlopen_self=$dlopen_self_static
6680 | 	    dlopen_self=$dlopen_self_static
6686 | 	    dlopen_self=$dlopen_self_static
6744 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6834 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7001 |       -dlopen)
7439 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7507 | 	  # This library was specified with -dlopen.
7627 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7638 | 	passes="conv scan dlopen dlpreopen link"
7664 | 	dlopen) libs=$dlfiles ;;
7695 |       if test dlopen = "$pass"; then
7915 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7916 | 	      # If there is no dlopen support or we're linking statically,
7944 | 	dlopen=
7974 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8020 | 	# This library was specified with -dlopen.
8021 | 	if test dlopen = "$pass"; then
8023 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8025 | 	     test yes != "$dlopen_support" ||
8028 | 	    # If there is no dlname, no dlopen support or we're linking
8037 | 	fi # $pass = dlopen
8093 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8095 | 	      # We recover the dlopen module name by 'saving' the la file
8119 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8248 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8249 | 	  dlopenmodule=
8252 | 	      dlopenmodule=$dlpremoduletest
8256 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8353 | 		    # if the lib is a (non-dlopened) module then we cannot
8357 | 		      if test "X$dlopenmodule" != "X$lib"; then
8509 | 	      echo "*** a static module, that should work as long as the dlopening application"
8510 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8654 |       if test dlopen != "$pass"; then
8784 | 	func_warning "'-dlopen' is ignored for archives"
8851 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9548 | 	    echo "*** a static module, that should work as long as the dlopening"
9549 | 	    echo "*** application is linked with the -dlopen flag."
9567 | 	    echo "*** or is declared to -dlopen it."
10179 | 	func_warning "'-dlopen' is ignored for objects"
10299 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10300 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10981 | # The name that we can dlopen(3).
11010 | # Files to dlopen/dlpreopen
11011 | dlopen='$dlfiles'
{% endraw %}

```