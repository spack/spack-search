---
name: "exciting"
layout: package
next_package: libassuan
previous_package: tcl
languages: ['bash']
---
## 14
6 / 4135 files match

 - [src/libXC/config.status](#srclibxcconfigstatus)
 - [src/libXC/config.status.lineno](#srclibxcconfigstatuslineno)
 - [src/libXC/ltmain.sh](#srclibxcltmainsh)
 - [src/libXC/configure.lineno](#srclibxcconfigurelineno)
 - [src/libXC/m4/libtool.m4](#srclibxcm4libtoolm4)
 - [src/libXC/m4/ltoptions.m4](#srclibxcm4ltoptionsm4)

### src/libXC/config.status

```

{% raw %}
680 | enable_dlopen='unknown'
681 | enable_dlopen_self='unknown'
682 | enable_dlopen_self_static='unknown'
1810 | # Whether dlopen is supported.
1811 | dlopen_support=$enable_dlopen
1813 | # Whether dlopen of programs is supported.
1814 | dlopen_self=$enable_dlopen_self
1816 | # Whether dlopen of statically linked programs is supported.
1817 | dlopen_self_static=$enable_dlopen_self_static
1861 | # Compiler flag to allow reflexive dlopens.
2203 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/libXC/config.status.lineno

```

{% raw %}
599 | enable_dlopen='unknown'
600 | enable_dlopen_self='unknown'
601 | enable_dlopen_self_static='unknown'
1824 | # Whether dlopen is supported.
1825 | dlopen_support=$enable_dlopen
1827 | # Whether dlopen of programs is supported.
1828 | dlopen_self=$enable_dlopen_self
1830 | # Whether dlopen of statically linked programs is supported.
1831 | dlopen_self_static=$enable_dlopen_self_static
1875 | # Compiler flag to allow reflexive dlopens.
2217 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/libXC/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### src/libXC/configure.lineno

```

{% raw %}
7708 |         enable_dlopen=no
11173 |   if test "x$enable_dlopen" != xyes; then
11174 |   enable_dlopen=unknown
11175 |   enable_dlopen_self=unknown
11176 |   enable_dlopen_self_static=unknown
11178 |   lt_cv_dlopen=no
11179 |   lt_cv_dlopen_libs=
11183 |     lt_cv_dlopen="load_add_on"
11184 |     lt_cv_dlopen_libs=
11185 |     lt_cv_dlopen_self=yes
11189 |     lt_cv_dlopen="LoadLibrary"
11190 |     lt_cv_dlopen_libs=
11194 |     lt_cv_dlopen="dlopen"
11195 |     lt_cv_dlopen_libs=
11200 |     { $as_echo "$as_me:11201: checking for dlopen in -ldl" >&5
11201 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11202 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
11220 | char dlopen ();
11224 | return dlopen ();
11250 |   ac_cv_lib_dl_dlopen=yes
11255 | 	ac_cv_lib_dl_dlopen=no
11263 | { $as_echo "$as_me:11264: result: $ac_cv_lib_dl_dlopen" >&5
11264 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11265 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
11266 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11269 |     lt_cv_dlopen="dyld"
11270 |     lt_cv_dlopen_libs=
11271 |     lt_cv_dlopen_self=yes
11364 |   lt_cv_dlopen="shl_load"
11432 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
11434 |   { $as_echo "$as_me:11435: checking for dlopen" >&5
11435 | $as_echo_n "checking for dlopen... " >&6; }
11436 | if test "${ac_cv_func_dlopen+set}" = set; then
11445 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
11447 | #define dlopen innocuous_dlopen
11450 |     which can conflict with char dlopen (); below.
11460 | #undef dlopen
11468 | char dlopen ();
11472 | #if defined __stub_dlopen || defined __stub___dlopen
11479 | return dlopen ();
11505 |   ac_cv_func_dlopen=yes
11510 | 	ac_cv_func_dlopen=no
11517 | { $as_echo "$as_me:11518: result: $ac_cv_func_dlopen" >&5
11518 | $as_echo "$ac_cv_func_dlopen" >&6; }
11519 | if test "x$ac_cv_func_dlopen" = x""yes; then
11520 |   lt_cv_dlopen="dlopen"
11522 |   { $as_echo "$as_me:11523: checking for dlopen in -ldl" >&5
11523 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11524 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
11542 | char dlopen ();
11546 | return dlopen ();
11572 |   ac_cv_lib_dl_dlopen=yes
11577 | 	ac_cv_lib_dl_dlopen=no
11585 | { $as_echo "$as_me:11586: result: $ac_cv_lib_dl_dlopen" >&5
11586 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11587 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
11588 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11590 |   { $as_echo "$as_me:11591: checking for dlopen in -lsvld" >&5
11591 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11592 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
11610 | char dlopen ();
11614 | return dlopen ();
11640 |   ac_cv_lib_svld_dlopen=yes
11645 | 	ac_cv_lib_svld_dlopen=no
11653 | { $as_echo "$as_me:11654: result: $ac_cv_lib_svld_dlopen" >&5
11654 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11655 | if test "x$ac_cv_lib_svld_dlopen" = x""yes; then
11656 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
11724 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
11745 |   if test "x$lt_cv_dlopen" != xno; then
11746 |     enable_dlopen=yes
11748 |     enable_dlopen=no
11751 |   case $lt_cv_dlopen in
11752 |   dlopen)
11760 |     LIBS="$lt_cv_dlopen_libs $LIBS"
11762 |     { $as_echo "$as_me:11763: checking whether a program can dlopen itself" >&5
11763 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
11764 | if test "${lt_cv_dlopen_self+set}" = set; then
11768 |   lt_cv_dlopen_self=cross
11823 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11850 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
11851 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
11852 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
11856 |     lt_cv_dlopen_self=no
11863 | { $as_echo "$as_me:11864: result: $lt_cv_dlopen_self" >&5
11864 | $as_echo "$lt_cv_dlopen_self" >&6; }
11866 |     if test "x$lt_cv_dlopen_self" = xyes; then
11868 |       { $as_echo "$as_me:11869: checking whether a statically linked program can dlopen itself" >&5
11869 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
11870 | if test "${lt_cv_dlopen_self_static+set}" = set; then
11874 |   lt_cv_dlopen_self_static=cross
11929 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
11956 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
11957 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
11958 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
11962 |     lt_cv_dlopen_self_static=no
11969 | { $as_echo "$as_me:11970: result: $lt_cv_dlopen_self_static" >&5
11970 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
11979 |   case $lt_cv_dlopen_self in
11980 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
11981 |   *) enable_dlopen_self=unknown ;;
11984 |   case $lt_cv_dlopen_self_static in
11985 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
11986 |   *) enable_dlopen_self_static=unknown ;;
19857 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
19858 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
19859 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
21199 | # Whether dlopen is supported.
21200 | dlopen_support=$enable_dlopen
21202 | # Whether dlopen of programs is supported.
21203 | dlopen_self=$enable_dlopen_self
21205 | # Whether dlopen of statically linked programs is supported.
21206 | dlopen_self_static=$enable_dlopen_self_static
21250 | # Compiler flag to allow reflexive dlopens.
21592 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/libXC/m4/libtool.m4

```

{% raw %}
1744 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1747 | m4_defun([_LT_TRY_DLOPEN_SELF],
1805 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1838 | ])# _LT_TRY_DLOPEN_SELF
1841 | # LT_SYS_DLOPEN_SELF
1843 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1845 | if test "x$enable_dlopen" != xyes; then
1846 |   enable_dlopen=unknown
1847 |   enable_dlopen_self=unknown
1848 |   enable_dlopen_self_static=unknown
1850 |   lt_cv_dlopen=no
1851 |   lt_cv_dlopen_libs=
1855 |     lt_cv_dlopen="load_add_on"
1856 |     lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen_self=yes
1861 |     lt_cv_dlopen="LoadLibrary"
1862 |     lt_cv_dlopen_libs=
1866 |     lt_cv_dlopen="dlopen"
1867 |     lt_cv_dlopen_libs=
1872 |     AC_CHECK_LIB([dl], [dlopen],
1873 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1874 |     lt_cv_dlopen="dyld"
1875 |     lt_cv_dlopen_libs=
1876 |     lt_cv_dlopen_self=yes
1882 | 	  [lt_cv_dlopen="shl_load"],
1884 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1885 | 	[AC_CHECK_FUNC([dlopen],
1886 | 	      [lt_cv_dlopen="dlopen"],
1887 | 	  [AC_CHECK_LIB([dl], [dlopen],
1888 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1889 | 	    [AC_CHECK_LIB([svld], [dlopen],
1890 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1892 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1901 |   if test "x$lt_cv_dlopen" != xno; then
1902 |     enable_dlopen=yes
1904 |     enable_dlopen=no
1907 |   case $lt_cv_dlopen in
1908 |   dlopen)
1916 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1918 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1919 | 	  lt_cv_dlopen_self, [dnl
1920 | 	  _LT_TRY_DLOPEN_SELF(
1921 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1922 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1925 |     if test "x$lt_cv_dlopen_self" = xyes; then
1927 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1928 | 	  lt_cv_dlopen_self_static, [dnl
1929 | 	  _LT_TRY_DLOPEN_SELF(
1930 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1931 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1941 |   case $lt_cv_dlopen_self in
1942 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1943 |   *) enable_dlopen_self=unknown ;;
1946 |   case $lt_cv_dlopen_self_static in
1947 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1948 |   *) enable_dlopen_self_static=unknown ;;
1951 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1952 | 	 [Whether dlopen is supported])
1953 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1954 | 	 [Whether dlopen of programs is supported])
1955 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1956 | 	 [Whether dlopen of statically linked programs is supported])
1957 | ])# LT_SYS_DLOPEN_SELF
1960 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1962 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5662 |     [Compiler flag to allow reflexive dlopens])
5775 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### src/libXC/m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```