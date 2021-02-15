---
name: "gnutls"
layout: package
next_package: hip-rocclr
previous_package: libxscrnsaver
languages: ['cpp', 'bash']
---
## 3.6.7.1
12 / 4928 files match

 - [lib/tpm.c](#libtpmc)
 - [lib/fips.c](#libfipsc)
 - [tests/pkcs11/pkcs11-privkey-safenet-always-auth.c](#testspkcs11pkcs11-privkey-safenet-always-authc)
 - [tests/pkcs11/pkcs11-privkey-always-auth.c](#testspkcs11pkcs11-privkey-always-authc)
 - [tests/pkcs11/pkcs11-import-url-privkey.c](#testspkcs11pkcs11-import-url-privkeyc)
 - [guile/pre-inst-guile.in](#guilepre-inst-guilein)
 - [guile/src/Makefile.am](#guilesrcmakefileam)
 - [guile/src/Makefile.in](#guilesrcmakefilein)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/lib-link.m4](#m4lib-linkm4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)

### lib/tpm.c

```cpp

{% raw %}
123 | 		tpm_dl = dlopen(TROUSERS_LIB, RTLD_LAZY);
{% endraw %}

```
### lib/fips.c

```cpp

{% raw %}
152 | 	dl = dlopen(lib, RTLD_LAZY);
{% endraw %}

```
### tests/pkcs11/pkcs11-privkey-safenet-always-auth.c

```cpp

{% raw %}
94 | 		dl = dlopen(lib, RTLD_NOW);
96 | 			fail("could not dlopen %s\n", lib);
{% endraw %}

```
### tests/pkcs11/pkcs11-privkey-always-auth.c

```cpp

{% raw %}
95 | 		dl = dlopen(lib, RTLD_NOW);
97 | 			fail("could not dlopen %s\n", lib);
{% endraw %}

```
### tests/pkcs11/pkcs11-import-url-privkey.c

```cpp

{% raw %}
100 | 		dl = dlopen(lib, RTLD_NOW);
102 | 			fail("could not dlopen %s\n", lib);
{% endraw %}

```
### guile/pre-inst-guile.in

```

{% raw %}
30 |        -dlopen "@abs_top_builddir@/guile/src/guile-gnutls-v-2.la"        \
{% endraw %}

```
### guile/src/Makefile.am

```

{% raw %}
38 | # Use '-module' to build a "dlopenable module", in Libtool terms.
{% endraw %}

```
### guile/src/Makefile.in

```

{% raw %}
1471 | # Use '-module' to build a "dlopenable module", in Libtool terms.
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
### m4/lib-link.m4

```

{% raw %}
516 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
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
7438 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7506 | 	  # This library was specified with -dlopen.
7626 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7637 | 	passes="conv scan dlopen dlpreopen link"
7663 | 	dlopen) libs=$dlfiles ;;
7694 |       if test dlopen = "$pass"; then
7914 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7915 | 	      # If there is no dlopen support or we're linking statically,
7943 | 	dlopen=
7973 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8019 | 	# This library was specified with -dlopen.
8020 | 	if test dlopen = "$pass"; then
8022 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8024 | 	     test yes != "$dlopen_support" ||
8027 | 	    # If there is no dlname, no dlopen support or we're linking
8036 | 	fi # $pass = dlopen
8092 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8094 | 	      # We recover the dlopen module name by 'saving' the la file
8118 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8247 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8248 | 	  dlopenmodule=
8251 | 	      dlopenmodule=$dlpremoduletest
8255 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8352 | 		    # if the lib is a (non-dlopened) module then we cannot
8356 | 		      if test "X$dlopenmodule" != "X$lib"; then
8508 | 	      echo "*** a static module, that should work as long as the dlopening application"
8509 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8653 |       if test dlopen != "$pass"; then
8783 | 	func_warning "'-dlopen' is ignored for archives"
8850 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9547 | 	    echo "*** a static module, that should work as long as the dlopening"
9548 | 	    echo "*** application is linked with the -dlopen flag."
9566 | 	    echo "*** or is declared to -dlopen it."
10178 | 	func_warning "'-dlopen' is ignored for objects"
10298 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10299 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10980 | # The name that we can dlopen(3).
11009 | # Files to dlopen/dlpreopen
11010 | dlopen='$dlfiles'
{% endraw %}

```