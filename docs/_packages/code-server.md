---
name: "code-server"
layout: package
next_package: prism
previous_package: swftools
languages: ['cpp', 'bash']
---
## 3.1.0
7 / 4773 files match

 - [lib/vscode/node_modules/vscode-sqlite3/build/Release/obj/gen/sqlite-autoconf-3280000/configure.ac](#libvscodenode_modulesvscode-sqlite3buildreleaseobjgensqlite-autoconf-3280000configureac)
 - [lib/vscode/node_modules/vscode-sqlite3/build/Release/obj/gen/sqlite-autoconf-3280000/ltmain.sh](#libvscodenode_modulesvscode-sqlite3buildreleaseobjgensqlite-autoconf-3280000ltmainsh)
 - [lib/vscode/node_modules/vscode-sqlite3/build/Release/obj/gen/sqlite-autoconf-3280000/aclocal.m4](#libvscodenode_modulesvscode-sqlite3buildreleaseobjgensqlite-autoconf-3280000aclocalm4)
 - [lib/vscode/node_modules/vscode-sqlite3/build/Release/obj/gen/sqlite-autoconf-3280000/sqlite3.c](#libvscodenode_modulesvscode-sqlite3buildreleaseobjgensqlite-autoconf-3280000sqlite3c)
 - [lib/vscode/node_modules/oniguruma/deps/onig/ltmain.sh](#libvscodenode_modulesonigurumadepsonigltmainsh)
 - [lib/vscode/node_modules/oniguruma/deps/onig/m4/libtool.m4](#libvscodenode_modulesonigurumadepsonigm4libtoolm4)
 - [lib/vscode/node_modules/oniguruma/deps/onig/m4/ltoptions.m4](#libvscodenode_modulesonigurumadepsonigm4ltoptionsm4)

### lib/vscode/node_modules/vscode-sqlite3/build/Release/obj/gen/sqlite-autoconf-3280000/configure.ac

```

{% raw %}
103 |   AC_SEARCH_LIBS(dlopen, dl)
{% endraw %}

```
### lib/vscode/node_modules/vscode-sqlite3/build/Release/obj/gen/sqlite-autoconf-3280000/ltmain.sh

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
### lib/vscode/node_modules/vscode-sqlite3/build/Release/obj/gen/sqlite-autoconf-3280000/aclocal.m4

```

{% raw %}
1834 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1837 | m4_defun([_LT_TRY_DLOPEN_SELF],
1895 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1928 | ])# _LT_TRY_DLOPEN_SELF
1931 | # LT_SYS_DLOPEN_SELF
1933 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1935 | if test yes != "$enable_dlopen"; then
1936 |   enable_dlopen=unknown
1937 |   enable_dlopen_self=unknown
1938 |   enable_dlopen_self_static=unknown
1940 |   lt_cv_dlopen=no
1941 |   lt_cv_dlopen_libs=
1945 |     lt_cv_dlopen=load_add_on
1946 |     lt_cv_dlopen_libs=
1947 |     lt_cv_dlopen_self=yes
1951 |     lt_cv_dlopen=LoadLibrary
1952 |     lt_cv_dlopen_libs=
1956 |     lt_cv_dlopen=dlopen
1957 |     lt_cv_dlopen_libs=
1962 |     AC_CHECK_LIB([dl], [dlopen],
1963 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1964 |     lt_cv_dlopen=dyld
1965 |     lt_cv_dlopen_libs=
1966 |     lt_cv_dlopen_self=yes
1973 |     lt_cv_dlopen=dlopen
1974 |     lt_cv_dlopen_libs=
1975 |     lt_cv_dlopen_self=no
1980 | 	  [lt_cv_dlopen=shl_load],
1982 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1983 | 	[AC_CHECK_FUNC([dlopen],
1984 | 	      [lt_cv_dlopen=dlopen],
1985 | 	  [AC_CHECK_LIB([dl], [dlopen],
1986 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1987 | 	    [AC_CHECK_LIB([svld], [dlopen],
1988 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1990 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1999 |   if test no = "$lt_cv_dlopen"; then
2000 |     enable_dlopen=no
2002 |     enable_dlopen=yes
2005 |   case $lt_cv_dlopen in
2006 |   dlopen)
2014 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2016 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2017 | 	  lt_cv_dlopen_self, [dnl
2018 | 	  _LT_TRY_DLOPEN_SELF(
2019 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2020 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2023 |     if test yes = "$lt_cv_dlopen_self"; then
2025 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2026 | 	  lt_cv_dlopen_self_static, [dnl
2027 | 	  _LT_TRY_DLOPEN_SELF(
2028 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2029 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2039 |   case $lt_cv_dlopen_self in
2040 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2041 |   *) enable_dlopen_self=unknown ;;
2044 |   case $lt_cv_dlopen_self_static in
2045 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2046 |   *) enable_dlopen_self_static=unknown ;;
2049 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2050 | 	 [Whether dlopen is supported])
2051 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2052 | 	 [Whether dlopen of programs is supported])
2053 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2054 | 	 [Whether dlopen of statically linked programs is supported])
2055 | ])# LT_SYS_DLOPEN_SELF
2058 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2060 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6154 |     [Compiler flag to allow reflexive dlopens])
6263 |   LT_SYS_DLOPEN_SELF
8458 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8492 | # dlopen
8494 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8497 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8498 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8501 | put the 'dlopen' option into LT_INIT's first parameter.])
8505 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
9019 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### lib/vscode/node_modules/vscode-sqlite3/build/Release/obj/gen/sqlite-autoconf-3280000/sqlite3.c

```cpp

{% raw %}
2391 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
15986 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
22415 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
22416 |   return pVfs->xDlOpen(pVfs, zPath);
38875 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
38877 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
38882 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
38925 |   #define unixDlOpen  0
40308 |     unixDlOpen,           /* xDlOpen */                     \
46300 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
46307 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46312 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46322 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46337 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
46359 |   #define winDlOpen  0
46577 |     winDlOpen,             /* xDlOpen */
46602 |     winDlOpen,             /* xDlOpen */
46627 |     winDlOpen,             /* xDlOpen */
46652 |     winDlOpen,             /* xDlOpen */
46787 | static void *memdbDlOpen(sqlite3_vfs*, const char *zFilename);
46808 |   memdbDlOpen,                 /* xDlOpen */
47111 | static void *memdbDlOpen(sqlite3_vfs *pVfs, const char *zPath){
47112 |   return ORIGVFS(pVfs)->xDlOpen(ORIGVFS(pVfs), zPath);
120211 |   handle = sqlite3OsDlOpen(pVfs, zFile);
120216 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
193698 | static void *rbuVfsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
193700 |   return pRealVfs->xDlOpen(pRealVfs, zPath);
193801 |     rbuVfsDlOpen,                 /* xDlOpen */
{% endraw %}

```
### lib/vscode/node_modules/oniguruma/deps/onig/ltmain.sh

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
6155 |       if test "$pass" = dlopen; then
6374 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6375 | 	      # If there is no dlopen support or we're linking statically,
6405 | 	dlopen=
6435 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6481 | 	# This library was specified with -dlopen.
6482 | 	if test "$pass" = dlopen; then
6484 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6487 | 	     test "$dlopen_support" != yes ||
6489 | 	    # If there is no dlname, no dlopen support or we're linking
6498 | 	fi # $pass = dlopen
6554 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6556 | 	      # We recover the dlopen module name by 'saving' the la file
6580 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6709 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6710 | 	  dlopenmodule=""
6713 | 	      dlopenmodule="$dlpremoduletest"
6717 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6814 | 		    # if the lib is a (non-dlopened) module then we can not
6818 | 		      if test "X$dlopenmodule" != "X$lib"; then
6970 | 	      echo "*** a static module, that should work as long as the dlopening application"
6971 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7115 |       if test "$pass" != dlopen; then
7214 | 	func_warning "\`-dlopen' is ignored for archives"
7281 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7960 | 	    echo "*** a static module, that should work as long as the dlopening"
7961 | 	    echo "*** application is linked with the -dlopen flag."
7979 | 	    echo "*** or is declared to -dlopen it."
8590 | 	func_warning "\`-dlopen' is ignored for objects"
8708 |         && test "$dlopen_support" = unknown \
8709 | 	&& test "$dlopen_self" = unknown \
8710 | 	&& test "$dlopen_self_static" = unknown && \
8711 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9392 | # The name that we can dlopen(3).
9421 | # Files to dlopen/dlpreopen
9422 | dlopen='$dlfiles'
{% endraw %}

```
### lib/vscode/node_modules/oniguruma/deps/onig/m4/libtool.m4

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
5677 |     [Compiler flag to allow reflexive dlopens])
5790 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### lib/vscode/node_modules/oniguruma/deps/onig/m4/ltoptions.m4

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