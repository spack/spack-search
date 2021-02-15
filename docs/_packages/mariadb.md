---
name: "mariadb"
layout: package
next_package: ipcalc
previous_package: cubew
languages: ['cmake', 'cpp', 'bash']
---
## 10.1.23
30 / 20399 files match

 - [configure.cmake](#configurecmake)
 - [storage/mroonga/vendor/groonga/configure.ac](#storagemroongavendorgroongaconfigureac)
 - [storage/mroonga/vendor/groonga/CMakeLists.txt](#storagemroongavendorgroongacmakeliststxt)
 - [storage/mroonga/vendor/groonga/lib/plugin.c](#storagemroongavendorgroongalibpluginc)
 - [storage/connect/ha_connect.cc](#storageconnectha_connectcc)
 - [storage/connect/jdbconn.cpp](#storageconnectjdbconncpp)
 - [storage/connect/mycat.cc](#storageconnectmycatcc)
 - [storage/connect/reldef.cpp](#storageconnectreldefcpp)
 - [storage/tokudb/PerconaFT/third_party/snappy-1.1.2/ltmain.sh](#storagetokudbperconaftthird_partysnappy-112ltmainsh)
 - [storage/tokudb/PerconaFT/third_party/snappy-1.1.2/aclocal.m4](#storagetokudbperconaftthird_partysnappy-112aclocalm4)
 - [storage/tokudb/PerconaFT/third_party/xz-4.999.9beta/m4/libtool.m4](#storagetokudbperconaftthird_partyxz-49999betam4libtoolm4)
 - [storage/tokudb/PerconaFT/third_party/xz-4.999.9beta/m4/ltoptions.m4](#storagetokudbperconaftthird_partyxz-49999betam4ltoptionsm4)
 - [storage/tokudb/PerconaFT/third_party/xz-4.999.9beta/m4/lib-link.m4](#storagetokudbperconaftthird_partyxz-49999betam4lib-linkm4)
 - [storage/tokudb/PerconaFT/third_party/xz-4.999.9beta/build-aux/ltmain.sh](#storagetokudbperconaftthird_partyxz-49999betabuild-auxltmainsh)
 - [storage/tokudb/PerconaFT/ftcxx/malloc_utils.hpp](#storagetokudbperconaftftcxxmalloc_utilshpp)
 - [wsrep/wsrep_loader.c](#wsrepwsrep_loaderc)
 - [wsrep/wsrep_api.h](#wsrepwsrep_apih)
 - [include/my_global.h](#includemy_globalh)
 - [sql-common/client_plugin.c](#sql-commonclient_pluginc)
 - [mysql-test/valgrind.supp](#mysql-testvalgrindsupp)
 - [mysql-test/t/sp-error.test](#mysql-testtsp-errortest)
 - [sql/mysqld.cc](#sqlmysqldcc)
 - [sql/sql_plugin.h](#sqlsql_pluginh)
 - [sql/sys_vars.cc](#sqlsys_varscc)
 - [sql/set_var.h](#sqlset_varh)
 - [sql/sql_udf.cc](#sqlsql_udfcc)
 - [sql/sql_plugin.cc](#sqlsql_plugincc)
 - [mysys/my_addr_resolve.c](#mysysmy_addr_resolvec)
 - [cmake/dtrace.cmake](#cmakedtracecmake)
 - [cmake/os/SunOS.cmake](#cmakeossunoscmake)

### configure.cmake

```cmake

{% raw %}
62 |      SET(HAVE_DLOPEN FALSE CACHE "Disable dlopen due to -static flag" FORCE)
123 |   MY_SEARCH_LIBS(dlopen dl LIBDL)
347 | CHECK_FUNCTION_EXISTS (dlopen HAVE_DLOPEN)
{% endraw %}

```
### storage/mroonga/vendor/groonga/configure.ac

```

{% raw %}
490 | AC_SEARCH_LIBS(dlopen, dl)
{% endraw %}

```
### storage/mroonga/vendor/groonga/CMakeLists.txt

```

{% raw %}
239 | ac_check_lib(dl dlopen)
{% endraw %}

```
### storage/mroonga/vendor/groonga/lib/plugin.c

```cpp

{% raw %}
49 | #  define grn_dl_open(filename)      dlopen(filename, RTLD_LAZY | RTLD_LOCAL)
{% endraw %}

```
### storage/connect/ha_connect.cc

```cpp

{% raw %}
652 |     if (dlopen(dl_info.dli_fname, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL) == 0)
654 |       sql_print_information("CONNECT: dlopen() failed, OEM table type is not supported");
{% endraw %}

```
### storage/connect/jdbconn.cpp

```

{% raw %}
743 | 			LibJvm = dlopen(soname, RTLD_LAZY);
{% endraw %}

```
### storage/connect/mycat.cc

```cpp

{% raw %}
413 |   if (!(hdll = dlopen(soname, RTLD_LAZY))) {
{% endraw %}

```
### storage/connect/reldef.cpp

```

{% raw %}
22 | #include <dlfcn.h>          // dlopen(), dlclose(), dlsym() ...
528 |     if (dlopen(dl_info.dli_fname, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL) == 0) {
530 |       sprintf(g->Message, "dlopen failed: %s, OEM not supported", SVP(error));
532 |       } // endif dlopen
542 |   if (!Hdll && !(Hdll = dlopen(soname, RTLD_NOLOAD)))
544 |     if (!(Hdll = dlopen(soname, RTLD_LAZY))) {
{% endraw %}

```
### storage/tokudb/PerconaFT/third_party/snappy-1.1.2/ltmain.sh

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
### storage/tokudb/PerconaFT/third_party/snappy-1.1.2/aclocal.m4

```

{% raw %}
1758 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1761 | m4_defun([_LT_TRY_DLOPEN_SELF],
1819 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1852 | ])# _LT_TRY_DLOPEN_SELF
1855 | # LT_SYS_DLOPEN_SELF
1857 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1859 | if test "x$enable_dlopen" != xyes; then
1860 |   enable_dlopen=unknown
1861 |   enable_dlopen_self=unknown
1862 |   enable_dlopen_self_static=unknown
1864 |   lt_cv_dlopen=no
1865 |   lt_cv_dlopen_libs=
1869 |     lt_cv_dlopen="load_add_on"
1870 |     lt_cv_dlopen_libs=
1871 |     lt_cv_dlopen_self=yes
1875 |     lt_cv_dlopen="LoadLibrary"
1876 |     lt_cv_dlopen_libs=
1880 |     lt_cv_dlopen="dlopen"
1881 |     lt_cv_dlopen_libs=
1886 |     AC_CHECK_LIB([dl], [dlopen],
1887 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1888 |     lt_cv_dlopen="dyld"
1889 |     lt_cv_dlopen_libs=
1890 |     lt_cv_dlopen_self=yes
1896 | 	  [lt_cv_dlopen="shl_load"],
1898 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1899 | 	[AC_CHECK_FUNC([dlopen],
1900 | 	      [lt_cv_dlopen="dlopen"],
1901 | 	  [AC_CHECK_LIB([dl], [dlopen],
1902 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1903 | 	    [AC_CHECK_LIB([svld], [dlopen],
1904 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1906 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1915 |   if test "x$lt_cv_dlopen" != xno; then
1916 |     enable_dlopen=yes
1918 |     enable_dlopen=no
1921 |   case $lt_cv_dlopen in
1922 |   dlopen)
1930 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1932 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1933 | 	  lt_cv_dlopen_self, [dnl
1934 | 	  _LT_TRY_DLOPEN_SELF(
1935 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1936 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1939 |     if test "x$lt_cv_dlopen_self" = xyes; then
1941 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1942 | 	  lt_cv_dlopen_self_static, [dnl
1943 | 	  _LT_TRY_DLOPEN_SELF(
1944 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1945 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1955 |   case $lt_cv_dlopen_self in
1956 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1957 |   *) enable_dlopen_self=unknown ;;
1960 |   case $lt_cv_dlopen_self_static in
1961 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1962 |   *) enable_dlopen_self_static=unknown ;;
1965 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1966 | 	 [Whether dlopen is supported])
1967 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1968 | 	 [Whether dlopen of programs is supported])
1969 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1970 | 	 [Whether dlopen of statically linked programs is supported])
1971 | ])# LT_SYS_DLOPEN_SELF
1974 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1976 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5691 |     [Compiler flag to allow reflexive dlopens])
5800 |   LT_SYS_DLOPEN_SELF
8072 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8104 | # dlopen
8106 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8109 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8110 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8113 | put the `dlopen' option into LT_INIT's first parameter.])
8117 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8578 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### storage/tokudb/PerconaFT/third_party/xz-4.999.9beta/m4/libtool.m4

```

{% raw %}
1634 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1637 | m4_defun([_LT_TRY_DLOPEN_SELF],
1689 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1718 | ])# _LT_TRY_DLOPEN_SELF
1721 | # LT_SYS_DLOPEN_SELF
1723 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1725 | if test "x$enable_dlopen" != xyes; then
1726 |   enable_dlopen=unknown
1727 |   enable_dlopen_self=unknown
1728 |   enable_dlopen_self_static=unknown
1730 |   lt_cv_dlopen=no
1731 |   lt_cv_dlopen_libs=
1735 |     lt_cv_dlopen="load_add_on"
1736 |     lt_cv_dlopen_libs=
1737 |     lt_cv_dlopen_self=yes
1741 |     lt_cv_dlopen="LoadLibrary"
1742 |     lt_cv_dlopen_libs=
1746 |     lt_cv_dlopen="dlopen"
1747 |     lt_cv_dlopen_libs=
1752 |     AC_CHECK_LIB([dl], [dlopen],
1753 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1754 |     lt_cv_dlopen="dyld"
1755 |     lt_cv_dlopen_libs=
1756 |     lt_cv_dlopen_self=yes
1762 | 	  [lt_cv_dlopen="shl_load"],
1764 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1765 | 	[AC_CHECK_FUNC([dlopen],
1766 | 	      [lt_cv_dlopen="dlopen"],
1767 | 	  [AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1769 | 	    [AC_CHECK_LIB([svld], [dlopen],
1770 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1772 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1781 |   if test "x$lt_cv_dlopen" != xno; then
1782 |     enable_dlopen=yes
1784 |     enable_dlopen=no
1787 |   case $lt_cv_dlopen in
1788 |   dlopen)
1796 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1798 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1799 | 	  lt_cv_dlopen_self, [dnl
1800 | 	  _LT_TRY_DLOPEN_SELF(
1801 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1802 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1805 |     if test "x$lt_cv_dlopen_self" = xyes; then
1807 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1808 | 	  lt_cv_dlopen_self_static, [dnl
1809 | 	  _LT_TRY_DLOPEN_SELF(
1810 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1811 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1821 |   case $lt_cv_dlopen_self in
1822 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1823 |   *) enable_dlopen_self=unknown ;;
1826 |   case $lt_cv_dlopen_self_static in
1827 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1828 |   *) enable_dlopen_self_static=unknown ;;
1831 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1832 | 	 [Whether dlopen is supported])
1833 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1834 | 	 [Whether dlopen of programs is supported])
1835 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1836 | 	 [Whether dlopen of statically linked programs is supported])
1837 | ])# LT_SYS_DLOPEN_SELF
1840 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1842 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5155 |     [Compiler flag to allow reflexive dlopens])
5271 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### storage/tokudb/PerconaFT/third_party/xz-4.999.9beta/m4/ltoptions.m4

```

{% raw %}
69 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
104 | # dlopen
106 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
109 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
110 | [_LT_SET_OPTION([LT_INIT], [dlopen])
113 | put the `dlopen' option into LT_INIT's first parameter.])
117 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### storage/tokudb/PerconaFT/third_party/xz-4.999.9beta/m4/lib-link.m4

```

{% raw %}
394 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### storage/tokudb/PerconaFT/third_party/xz-4.999.9beta/build-aux/ltmain.sh

```bash

{% raw %}
737 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
787 |       -dlopen=*|--mode=*|--tag=*)
876 |   # Only execute mode is allowed to have -dlopen flags.
878 |     func_error "unrecognized option \`-dlopen'"
1505 |   -dlopen FILE      add the directory containing FILE to the library path
1507 | This mode sets the library path environment variable according to \`-dlopen'
1560 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1569 |   -module           build a library that can dlopened
1644 |     # Handle -dlopen flags immediately.
1661 | 	# Skip this library if it cannot be dlopened.
1688 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4121 | 	    dlopen_self=$dlopen_self_static
4127 | 	    dlopen_self=$dlopen_self_static
4133 | 	    dlopen_self=$dlopen_self_static
4186 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4270 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4427 |       -dlopen)
4814 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4881 | 	  # This library was specified with -dlopen.
4996 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5007 | 	passes="conv scan dlopen dlpreopen link"
5033 | 	dlopen) libs="$dlfiles" ;;
5059 |       if test "$pass" = dlopen; then
5271 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5272 | 	      # If there is no dlopen support or we're linking statically,
5302 | 	dlopen=
5332 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5372 | 	# This library was specified with -dlopen.
5373 | 	if test "$pass" = dlopen; then
5375 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5378 | 	     test "$dlopen_support" != yes ||
5380 | 	    # If there is no dlname, no dlopen support or we're linking
5389 | 	fi # $pass = dlopen
5447 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5573 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5574 | 	  dlopenmodule=""
5577 | 	      dlopenmodule="$dlpremoduletest"
5581 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5678 | 		    # if the lib is a (non-dlopened) module then we can not
5682 | 		      if test "X$dlopenmodule" != "X$lib"; then
5834 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5835 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5970 |       if test "$pass" != dlopen; then
6069 | 	func_warning "\`-dlopen' is ignored for archives"
6136 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6798 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6799 | 	    $ECHO "*** application is linked with the -dlopen flag."
6817 | 	    $ECHO "*** or is declared to -dlopen it."
7384 | 	func_warning "\`-dlopen' is ignored for objects"
7499 |         && test "$dlopen_support" = unknown \
7500 | 	&& test "$dlopen_self" = unknown \
7501 | 	&& test "$dlopen_self_static" = unknown && \
7502 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8134 | # The name that we can dlopen(3).
8163 | # Files to dlopen/dlpreopen
8164 | dlopen='$dlfiles'
{% endraw %}

```
### storage/tokudb/PerconaFT/ftcxx/malloc_utils.hpp

```

{% raw %}
94 |         // dlopen()ed module that depends on libjemalloc, so rallocx is
{% endraw %}

```
### wsrep/wsrep_loader.c

```cpp

{% raw %}
162 |     if (!(dlh = dlopen(spec, RTLD_NOW | RTLD_LOCAL))) {
163 |         snprintf(msg, sizeof(msg)-1, "wsrep_load(): dlopen(): %s", dlerror());
{% endraw %}

```
### wsrep/wsrep_api.h

```cpp

{% raw %}
39 |   Finally, wsrep_load() method loads (dlopens) wsrep provider library. It is
{% endraw %}

```
### include/my_global.h

```cpp

{% raw %}
1073 | #define dlopen(libname, unused) LoadLibraryEx(libname, NULL, 0)
1082 | #define HAVE_DLOPEN 1
1090 | #ifdef HAVE_DLOPEN
1096 | #define dlopen(A,B) 0
{% endraw %}

```
### sql-common/client_plugin.c

```cpp

{% raw %}
121 |   @param dlhandle       a handle to the shared object (returned by dlopen)
365 |   DBUG_PRINT ("info", ("dlopeninig %s", dlpath));
367 |   if (!(dlhandle= dlopen(dlpath, RTLD_NOW)))
369 |     DBUG_PRINT ("info", ("failed to dlopen"));
{% endraw %}

```
### mysql-test/valgrind.supp

```

{% raw %}
399 |    dlopen / ptread_cancel_init memory loss on Suse Linux 10.3 32/64 bit ver 1
411 |    fun:__libc_dlopen_mode
417 |    dlopen / ptread_cancel_init memory loss on Suse Linux 10.3 32/64 bit ver 2
428 |    fun:__libc_dlopen_mode
434 |    dlopen / ptread_cancel_init memory loss on Suse Linux 10.3 32/64 bit
444 |    fun:__libc_dlopen_mode
455 |    Reading wrong data in libc_dlopen
466 |    fun:__libc_dlopen_mode
619 | # Warning caused by small memory leak in threaded dlopen
623 |    dlopen threaded memory leak
627 |    fun:dlopen*
732 |    fun:__libc_dlopen_mode
752 |    fun:__libc_dlopen_mode
772 |    fun:__libc_dlopen_mode
794 |    fun:__libc_dlopen_mode
815 |    fun:__libc_dlopen_mode
853 |    fun:__libc_dlopen_mode
872 |    fun:__libc_dlopen_mode
893 |    fun:__libc_dlopen_mode
916 |    fun:__libc_dlopen_mode
937 |    fun:__libc_dlopen_mode
1223 |   ConnectSE: unixODBC dlopen leaves some "still reachable"
1242 |   Mroonga: dlopen leaves some "still reachable"
1249 |   fun:dlopen_doit
1252 |   fun:dlopen@@GLIBC_2.2.5
1402 |    fun:dlopen_doit
1423 |    fun:dlopen_doit
1437 |    fun:dlopen_doit
1440 |    fun:dlopen@@GLIBC_2.2.5
{% endraw %}

```
### mysql-test/t/sp-error.test

```

{% raw %}
31 | #    the actual failing dlopen()).
{% endraw %}

```
### sql/mysqld.cc

```cpp

{% raw %}
700 | SHOW_COMP_OPTION have_ssl, have_symlink, have_dlopen, have_query_cache;
8362 |   {"Opened_plugin_libraries",  (char*) &dlopen_count, SHOW_LONG},
8740 | #ifdef HAVE_DLOPEN
8741 |   have_dlopen=SHOW_OPTION_YES;
8743 |   have_dlopen=SHOW_OPTION_NO;
{% endraw %}

```
### sql/sql_plugin.h

```cpp

{% raw %}
39 | extern ulong dlopen_count;
{% endraw %}

```
### sql/sys_vars.cc

```cpp

{% raw %}
4071 | static Sys_var_have Sys_have_dlopen(
4073 |        READ_ONLY GLOBAL_VAR(have_dlopen), NO_CMD_LINE);
{% endraw %}

```
### sql/set_var.h

```cpp

{% raw %}
373 | extern SHOW_COMP_OPTION have_ssl, have_symlink, have_dlopen;
{% endraw %}

```
### sql/sql_udf.cc

```cpp

{% raw %}
43 | #ifdef HAVE_DLOPEN
231 |       if (!(dl= dlopen(dlpath, RTLD_NOW)))
537 |     if (!(dl = dlopen(dlpath, RTLD_NOW)))
541 |       DBUG_PRINT("error",("dlopen of %s failed, error: %d (%s)",
664 | #endif /* HAVE_DLOPEN */
{% endraw %}

```
### sql/sql_plugin.cc

```cpp

{% raw %}
141 | #ifdef HAVE_DLOPEN
233 | ulong dlopen_count;
443 | #ifdef HAVE_DLOPEN
485 | #endif /* HAVE_DLOPEN */
490 | #ifdef HAVE_DLOPEN
519 | #ifdef HAVE_DLOPEN
719 | #endif /* HAVE_DLOPEN */
723 | #ifdef HAVE_DLOPEN
759 |   if (!(plugin_dl.handle= dlopen(dlpath, RTLD_NOW)))
764 |   dlopen_count++;
853 |   report_error(report, ER_FEATURE_DISABLED, "plugin", "HAVE_DLOPEN");
1528 |   dlopen_count =0;
4148 |   next dlopen() these symbols will have old values, they won't be
{% endraw %}

```
### mysys/my_addr_resolve.c

```cpp

{% raw %}
135 | #if defined(HAVE_LINK_H) && defined(HAVE_DLOPEN)
227 | #if defined(HAVE_LINK_H) && defined(HAVE_DLOPEN)
228 |     struct link_map *lm = (struct link_map*) dlopen(0, RTLD_NOW);
{% endraw %}

```
### cmake/dtrace.cmake

```cmake

{% raw %}
22 |      # This gcc causes crashes in dlopen() for dtraced shared libs,
{% endraw %}

```
### cmake/os/SunOS.cmake

```cmake

{% raw %}
29 | # CMake defined -lthread as thread flag. This crashes in dlopen 
{% endraw %}

```