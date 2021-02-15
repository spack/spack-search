---
name: "mysql"
layout: package
next_package: pdsh
previous_package: libidl
languages: ['cmake', 'cpp']
---
## 8.0.19
28 / 39146 files match

 - [configure.cmake](#configurecmake)
 - [storage/ndb/src/common/portlib/NdbNuma.cpp](#storagendbsrccommonportlibndbnumacpp)
 - [storage/ndb/memcache/extra/memcached/daemon/memcached.c](#storagendbmemcacheextramemcacheddaemonmemcachedc)
 - [storage/ndb/memcache/extra/memcached/utilities/engine_loader.c](#storagendbmemcacheextramemcachedutilitiesengine_loaderc)
 - [storage/ndb/memcache/extra/memcached/programs/engine_testapp.c](#storagendbmemcacheextramemcachedprogramsengine_testappc)
 - [storage/ndb/memcache/extra/memcached/win32/dlfcn.h](#storagendbmemcacheextramemcachedwin32dlfcnh)
 - [storage/ndb/memcache/extra/memcached/win32/dlfcn.c](#storagendbmemcacheextramemcachedwin32dlfcnc)
 - [router/src/plugin_info/src/library_file.cc](#routersrcplugin_infosrclibrary_filecc)
 - [router/src/harness/src/loader-posix.cc](#routersrcharnesssrcloader-posixcc)
 - [router/src/harness/include/mysql/harness/loader.h](#routersrcharnessincludemysqlharnessloaderh)
 - [router/src/harness/tests/test_loader_lifecycle.cc](#routersrcharnessteststest_loader_lifecyclecc)
 - [include/my_sharedlib.h](#includemy_sharedlibh)
 - [plugin/innodb_memcached/daemon_memcached/daemon/memcached.c](#plugininnodb_memcacheddaemon_memcacheddaemonmemcachedc)
 - [plugin/innodb_memcached/daemon_memcached/utilities/engine_loader.c](#plugininnodb_memcacheddaemon_memcachedutilitiesengine_loaderc)
 - [plugin/innodb_memcached/daemon_memcached/programs/engine_testapp.c](#plugininnodb_memcacheddaemon_memcachedprogramsengine_testappc)
 - [plugin/innodb_memcached/daemon_memcached/win32/dlfcn.h](#plugininnodb_memcacheddaemon_memcachedwin32dlfcnh)
 - [plugin/innodb_memcached/daemon_memcached/win32/dlfcn.c](#plugininnodb_memcacheddaemon_memcachedwin32dlfcnc)
 - [extra/icu/source/common/putil.cpp](#extraicusourcecommonputilcpp)
 - [sql-common/client_plugin.cc](#sql-commonclient_plugincc)
 - [mysql-test/valgrind.supp](#mysql-testvalgrindsupp)
 - [mysql-test/t/sp-error.test](#mysql-testtsp-errortest)
 - [components/mysql_server/dynamic_loader_scheme_file.cc](#componentsmysql_serverdynamic_loader_scheme_filecc)
 - [sql/mysqld.cc](#sqlmysqldcc)
 - [sql/sys_vars.cc](#sqlsys_varscc)
 - [sql/set_var.h](#sqlset_varh)
 - [sql/sql_udf.cc](#sqlsql_udfcc)
 - [sql/sql_plugin.cc](#sqlsql_plugincc)
 - [cmake/os/SunOS.cmake](#cmakeossunoscmake)

### configure.cmake

```cmake

{% raw %}
109 |   MY_SEARCH_LIBS(dlopen dl LIBDL)
110 |   # HAVE_dlopen_IN_LIBC
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
### router/src/harness/src/loader-posix.cc

```cpp

{% raw %}
56 | // dlopen/dlclose work differently on Alpine
86 |       handle(dlopen(path.c_str(), RTLD_LOCAL | RTLD_NOW)) {
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
110 | // dlopen/dlclose work differently on Alpine
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
542 | # Warning caused by small memory leak in threaded dlopen
546 |    dlopen threaded memory leak
550 |    fun:dlopen*
554 |    dlopen memory leak
1058 |    fun:dlopen*
1882 |    fun:dlopen_doit
2000 |    fun:dlopen_doit
2139 |    fun:dlopen@@GLIBC_2.2.5
2166 |    fun:dlopen_doit
2181 |    fun:dlopen@@GLIBC_2.2.5
2257 |    fun:dlopen_doit
2260 |    fun:dlopen@@GLIBC_2.2.5
2304 |    fun:dlopen@@GLIBC_2.2.5
2363 |    fun:dlopen_doit
{% endraw %}

```
### mysql-test/t/sp-error.test

```

{% raw %}
23 | #    the actual failing dlopen()).
{% endraw %}

```
### components/mysql_server/dynamic_loader_scheme_file.cc

```cpp

{% raw %}
114 |     void *handle = dlopen(file_name.c_str(), RTLD_NOW);
{% endraw %}

```
### sql/mysqld.cc

```cpp

{% raw %}
1322 | SHOW_COMP_OPTION have_symlink, have_dlopen, have_query_cache;
9032 |   have_dlopen = SHOW_OPTION_YES;
{% endraw %}

```
### sql/sys_vars.cc

```cpp

{% raw %}
5350 | static Sys_var_have Sys_have_dlopen(
5352 |     READ_ONLY NON_PERSIST GLOBAL_VAR(have_dlopen), NO_CMD_LINE);
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
92 | # CMake defined -lthread as thread flag. This crashes in dlopen 
{% endraw %}

```