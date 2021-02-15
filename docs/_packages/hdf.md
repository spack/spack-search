---
name: "hdf"
layout: package
next_package: jags
previous_package: adol-c
languages: ['cmake', 'bash']
---
## 4.2.12
6 / 1070 files match

 - [configure.ac](#configureac)
 - [aclocal.m4](#aclocalm4)
 - [bin/ltmain.sh](#binltmainsh)
 - [config/cmake_ext_mod/ConfigureChecks.cmake](#configcmake_ext_modconfigurecheckscmake)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)

### configure.ac

```

{% raw %}
331 | LT_INIT([dlopen disable-shared])
{% endraw %}

```
### aclocal.m4

```

{% raw %}
2934 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
2937 | m4_defun([_LT_TRY_DLOPEN_SELF],
2995 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
3028 | ])# _LT_TRY_DLOPEN_SELF
3031 | # LT_SYS_DLOPEN_SELF
3033 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
3035 | if test "x$enable_dlopen" != xyes; then
3036 |   enable_dlopen=unknown
3037 |   enable_dlopen_self=unknown
3038 |   enable_dlopen_self_static=unknown
3040 |   lt_cv_dlopen=no
3041 |   lt_cv_dlopen_libs=
3045 |     lt_cv_dlopen="load_add_on"
3046 |     lt_cv_dlopen_libs=
3047 |     lt_cv_dlopen_self=yes
3051 |     lt_cv_dlopen="LoadLibrary"
3052 |     lt_cv_dlopen_libs=
3056 |     lt_cv_dlopen="dlopen"
3057 |     lt_cv_dlopen_libs=
3062 |     AC_CHECK_LIB([dl], [dlopen],
3063 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
3064 |     lt_cv_dlopen="dyld"
3065 |     lt_cv_dlopen_libs=
3066 |     lt_cv_dlopen_self=yes
3072 | 	  [lt_cv_dlopen="shl_load"],
3074 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
3075 | 	[AC_CHECK_FUNC([dlopen],
3076 | 	      [lt_cv_dlopen="dlopen"],
3077 | 	  [AC_CHECK_LIB([dl], [dlopen],
3078 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
3079 | 	    [AC_CHECK_LIB([svld], [dlopen],
3080 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
3082 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
3091 |   if test "x$lt_cv_dlopen" != xno; then
3092 |     enable_dlopen=yes
3094 |     enable_dlopen=no
3097 |   case $lt_cv_dlopen in
3098 |   dlopen)
3106 |     LIBS="$lt_cv_dlopen_libs $LIBS"
3108 |     AC_CACHE_CHECK([whether a program can dlopen itself],
3109 | 	  lt_cv_dlopen_self, [dnl
3110 | 	  _LT_TRY_DLOPEN_SELF(
3111 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
3112 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
3115 |     if test "x$lt_cv_dlopen_self" = xyes; then
3117 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
3118 | 	  lt_cv_dlopen_self_static, [dnl
3119 | 	  _LT_TRY_DLOPEN_SELF(
3120 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
3121 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
3131 |   case $lt_cv_dlopen_self in
3132 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
3133 |   *) enable_dlopen_self=unknown ;;
3136 |   case $lt_cv_dlopen_self_static in
3137 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
3138 |   *) enable_dlopen_self_static=unknown ;;
3141 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
3142 | 	 [Whether dlopen is supported])
3143 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
3144 | 	 [Whether dlopen of programs is supported])
3145 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
3146 | 	 [Whether dlopen of statically linked programs is supported])
3147 | ])# LT_SYS_DLOPEN_SELF
3150 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
3152 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6848 |     [Compiler flag to allow reflexive dlopens])
6957 |   LT_SYS_DLOPEN_SELF
9229 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
9261 | # dlopen
9263 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
9266 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
9267 | [_LT_SET_OPTION([LT_INIT], [dlopen])
9270 | put the `dlopen' option into LT_INIT's first parameter.])
9274 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
9735 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### bin/ltmain.sh

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
### config/cmake_ext_mod/ConfigureChecks.cmake

```cmake

{% raw %}
114 |   CHECK_LIBRARY_EXISTS_CONCAT ("dl" dlopen     ${HDF_PREFIX}_HAVE_LIBDL)
{% endraw %}

```
### m4/libtool.m4

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
5658 |     [Compiler flag to allow reflexive dlopens])
5771 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

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