---
name: "percona-server"
layout: package
next_package: source-highlight
previous_package: libxrender
languages: ['cmake', 'cpp', 'bash']
---
## 8.0.20-11
33 / 44426 files match

 - [configure.cmake](#configurecmake)
 - [storage/ndb/src/common/portlib/NdbNuma.cpp](#storagendbsrccommonportlibndbnumacpp)
 - [storage/ndb/memcache/extra/memcached/daemon/memcached.c](#storagendbmemcacheextramemcacheddaemonmemcachedc)
 - [storage/ndb/memcache/extra/memcached/utilities/engine_loader.c](#storagendbmemcacheextramemcachedutilitiesengine_loaderc)
 - [storage/ndb/memcache/extra/memcached/programs/engine_testapp.c](#storagendbmemcacheextramemcachedprogramsengine_testappc)
 - [storage/ndb/memcache/extra/memcached/win32/dlfcn.h](#storagendbmemcacheextramemcachedwin32dlfcnh)
 - [storage/ndb/memcache/extra/memcached/win32/dlfcn.c](#storagendbmemcacheextramemcachedwin32dlfcnc)
 - [router/src/plugin_info/src/library_file.cc](#routersrcplugin_infosrclibrary_filecc)
 - [router/src/harness/src/dynamic_loader.cc](#routersrcharnesssrcdynamic_loadercc)
 - [router/src/harness/include/mysql/harness/loader.h](#routersrcharnessincludemysqlharnessloaderh)
 - [router/src/harness/tests/test_loader_lifecycle.cc](#routersrcharnessteststest_loader_lifecyclecc)
 - [include/my_sharedlib.h](#includemy_sharedlibh)
 - [plugin/innodb_memcached/daemon_memcached/daemon/memcached.c](#plugininnodb_memcacheddaemon_memcacheddaemonmemcachedc)
 - [plugin/innodb_memcached/daemon_memcached/utilities/engine_loader.c](#plugininnodb_memcacheddaemon_memcachedutilitiesengine_loaderc)
 - [plugin/innodb_memcached/daemon_memcached/programs/engine_testapp.c](#plugininnodb_memcacheddaemon_memcachedprogramsengine_testappc)
 - [plugin/innodb_memcached/daemon_memcached/win32/dlfcn.h](#plugininnodb_memcacheddaemon_memcachedwin32dlfcnh)
 - [plugin/innodb_memcached/daemon_memcached/win32/dlfcn.c](#plugininnodb_memcacheddaemon_memcachedwin32dlfcnc)
 - [extra/libedit/libedit-20190324-3.1/ltmain.sh](#extralibeditlibedit-20190324-31ltmainsh)
 - [extra/libedit/libedit-20190324-3.1/m4/libtool.m4](#extralibeditlibedit-20190324-31m4libtoolm4)
 - [extra/libedit/libedit-20190324-3.1/m4/ltoptions.m4](#extralibeditlibedit-20190324-31m4ltoptionsm4)
 - [extra/icu/source/common/putil.cpp](#extraicusourcecommonputilcpp)
 - [sql-common/client_plugin.cc](#sql-commonclient_plugincc)
 - [mysql-test/valgrind.supp](#mysql-testvalgrindsupp)
 - [mysql-test/t/sp-error.test](#mysql-testtsp-errortest)
 - [components/libminchassis/dynamic_loader_scheme_file_imp.h](#componentslibminchassisdynamic_loader_scheme_file_imph)
 - [components/libminchassis/dynamic_loader_scheme_file.cc](#componentslibminchassisdynamic_loader_scheme_filecc)
 - [sql/mysqld.cc](#sqlmysqldcc)
 - [sql/sys_vars.cc](#sqlsys_varscc)
 - [sql/set_var.h](#sqlset_varh)
 - [sql/sql_udf.cc](#sqlsql_udfcc)
 - [sql/sql_plugin.cc](#sqlsql_plugincc)
 - [cmake/os/SunOS.cmake](#cmakeossunoscmake)
 - [libmysql/authentication_ldap/auth_ldap_sasl_client.cc](#libmysqlauthentication_ldapauth_ldap_sasl_clientcc)

### configure.cmake

```cmake

{% raw %}
96 |   MY_SEARCH_LIBS(dlopen dl LIBDL)
97 |   # HAVE_dlopen_IN_LIBC
{% endraw %}

```
### storage/ndb/src/common/portlib/NdbNuma.cpp

```

{% raw %}
33 | #if defined HAVE_DLFCN_H && defined HAVE_DLOPEN
37 |  * Load libnuma using dlopen, not have to put link dependency on it...
80 | my_dlopen(const char * name)
82 |   void * p = dlopen(name, RTLD_LAZY);
115 |   handle = my_dlopen("libnuma.so");
118 |     handle = my_dlopen("libnuma.so.1");
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/daemon/memcached.c

```cpp

{% raw %}
6857 |     void *handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/utilities/engine_loader.c

```cpp

{% raw %}
31 |     handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/programs/engine_testapp.c

```cpp

{% raw %}
832 |     void* handle = dlopen(test_suite, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/win32/dlfcn.h

```cpp

{% raw %}
2 | void* dlopen(const char* path, int mode);
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/win32/dlfcn.c

```cpp

{% raw %}
7 |  * Keep track if the user tried to call dlopen(NULL, xx) to be able to give a sane
12 | void* dlopen(const char* path, int mode) {
{% endraw %}

```
### router/src/plugin_info/src/library_file.cc

```cpp

{% raw %}
56 | // dlopen/dlclose work differently on Alpine
88 |   impl_->handle = dlopen(file_name.c_str(), RTLD_LOCAL | RTLD_LAZY);
{% endraw %}

```
### router/src/harness/src/dynamic_loader.cc

```cpp

{% raw %}
29 | #include <dlfcn.h>  // dlopen
141 |       dlopen(filename.c_str(), RTLD_LOCAL | RTLD_NOW);
{% endraw %}

```
### router/src/harness/include/mysql/harness/loader.h

```cpp

{% raw %}
51 |  * lazily (for example, the `RTLD_LAZY` flag is used for `dlopen`) to
54 |  * loaded (flag `RTLD_GLOBAL` to `dlopen`).
{% endraw %}

```
### router/src/harness/tests/test_loader_lifecycle.cc

```cpp

{% raw %}
111 | // dlopen/dlclose work differently on Alpine
{% endraw %}

```
### include/my_sharedlib.h

```cpp

{% raw %}
34 | #define dlopen(libname, unused) LoadLibraryEx(libname, NULL, 0)
48 | #define dlopen_errno GetLastError()
58 | #define dlopen_errno errno
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/daemon/memcached.c

```cpp

{% raw %}
6951 |     void *handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/utilities/engine_loader.c

```cpp

{% raw %}
32 |     handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/programs/engine_testapp.c

```cpp

{% raw %}
807 |     void* handle = dlopen(test_suite, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/win32/dlfcn.h

```cpp

{% raw %}
2 | void* dlopen(const char* path, int mode);
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/win32/dlfcn.c

```cpp

{% raw %}
7 |  * Keep track if the user tried to call dlopen(NULL, xx) to be able to give a sane
12 | void* dlopen(const char* path, int mode) {
{% endraw %}

```
### extra/libedit/libedit-20190324-3.1/ltmain.sh

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
### extra/libedit/libedit-20190324-3.1/m4/libtool.m4

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
### extra/libedit/libedit-20190324-3.1/m4/ltoptions.m4

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
### extra/icu/source/common/putil.cpp

```

{% raw %}
154 | #    define HAVE_DLOPEN 0
159 | #   ifndef HAVE_DLOPEN
160 | #    define HAVE_DLOPEN 1
168 | #   define HAVE_DLOPEN 0
2330 | #if HAVE_DLOPEN && !U_PLATFORM_USES_ONLY_WIN32_API
2346 |   ret =  dlopen(libName, RTLD_NOW|RTLD_GLOBAL);
2349 |     printf("dlerror on dlopen(%s): %s\n", libName, dlerror());
{% endraw %}

```
### sql-common/client_plugin.cc

```cpp

{% raw %}
167 |   @param dlhandle       a handle to the shared object (returned by dlopen)
467 |   DBUG_PRINT("info", ("dlopeninig %s", dlpath));
469 |   if (!(dlhandle = dlopen(dlpath, RTLD_NOW))) {
473 |     if ((dlhandle = dlopen(dlpath, RTLD_NOW))) goto have_plugin;
477 |     /* There should be no win32 calls between failed dlopen() and GetLastError()
487 |     DBUG_PRINT("info", ("failed to dlopen"));
{% endraw %}

```
### mysql-test/valgrind.supp

```

{% raw %}
540 | # Warning caused by small memory leak in threaded dlopen
544 |    dlopen threaded memory leak
548 |    fun:dlopen*
552 |    dlopen memory leak
1175 |    fun:dlopen*
2006 |    fun:dlopen_doit
2139 |    fun:dlopen_doit
2278 |    fun:dlopen@@GLIBC_2.2.5
2305 |    fun:dlopen_doit
2320 |    fun:dlopen@@GLIBC_2.2.5
2396 |    fun:dlopen_doit
2399 |    fun:dlopen@@GLIBC_2.2.5
2443 |    fun:dlopen@@GLIBC_2.2.5
2502 |    fun:dlopen_doit
{% endraw %}

```
### mysql-test/t/sp-error.test

```

{% raw %}
23 | #    the actual failing dlopen()).
{% endraw %}

```
### components/libminchassis/dynamic_loader_scheme_file_imp.h

```cpp

{% raw %}
35 | #define dlopen(libname, unused) LoadLibraryEx(libname, NULL, 0)
50 | #define dlopen_errno GetLastError()
60 | #define dlopen_errno errno
{% endraw %}

```
### components/libminchassis/dynamic_loader_scheme_file.cc

```cpp

{% raw %}
127 |     void *handle = dlopen(file_name.c_str(), RTLD_NOW);
130 |       int error_number = dlopen_errno;
{% endraw %}

```
### sql/mysqld.cc

```cpp

{% raw %}
1348 | SHOW_COMP_OPTION have_symlink, have_dlopen, have_query_cache;
9598 |   have_dlopen = SHOW_OPTION_YES;
{% endraw %}

```
### sql/sys_vars.cc

```cpp

{% raw %}
5633 | static Sys_var_have Sys_have_dlopen(
5635 |     READ_ONLY NON_PERSIST GLOBAL_VAR(have_dlopen), NO_CMD_LINE);
{% endraw %}

```
### sql/set_var.h

```cpp

{% raw %}
494 | extern SHOW_COMP_OPTION have_symlink, have_dlopen;
{% endraw %}

```
### sql/sql_udf.cc

```cpp

{% raw %}
275 |       if (!(dl = dlopen(dlpath, RTLD_NOW))) {
277 |         int error_number = dlopen_errno;
639 |     if (!(dl = dlopen(dlpath, RTLD_NOW))) {
641 |       int error_number = dlopen_errno;
644 |       DBUG_PRINT("error", ("dlopen of %s failed, error: %d (%s)", udf->dl,
{% endraw %}

```
### sql/sql_plugin.cc

```cpp

{% raw %}
672 |   if (!(plugin_dl.handle = dlopen(dlpath, RTLD_NOW))) {
674 |     int error_number = dlopen_errno;
{% endraw %}

```
### cmake/os/SunOS.cmake

```cmake

{% raw %}
96 | # CMake defined -lthread as thread flag. This crashes in dlopen 
{% endraw %}

```
### libmysql/authentication_ldap/auth_ldap_sasl_client.cc

```cpp

{% raw %}
517 |   // dlopen(NULL, ) should not fail ...
518 |   void *main_handle = dlopen(nullptr, RTLD_LAZY);
{% endraw %}

```