---
name: "mysql"
layout: package
next_package: pdsh
previous_package: libidl
languages: ['cpp', 'c']
---
## 8.0.19
28 / 39146 files match

 - [storage/ndb/memcache/extra/memcached/daemon/memcached.c](#storagendbmemcacheextramemcacheddaemonmemcachedc)
 - [storage/ndb/memcache/extra/memcached/utilities/engine_loader.c](#storagendbmemcacheextramemcachedutilitiesengine_loaderc)
 - [storage/ndb/memcache/extra/memcached/programs/engine_testapp.c](#storagendbmemcacheextramemcachedprogramsengine_testappc)
 - [storage/ndb/memcache/extra/memcached/win32/dlfcn.h](#storagendbmemcacheextramemcachedwin32dlfcnh)
 - [storage/ndb/memcache/extra/memcached/win32/dlfcn.c](#storagendbmemcacheextramemcachedwin32dlfcnc)
 - [router/src/plugin_info/src/library_file.cc](#routersrcplugin_infosrclibrary_filecc)
 - [router/src/harness/src/loader-posix.cc](#routersrcharnesssrcloader-posixcc)
 - [plugin/innodb_memcached/daemon_memcached/daemon/memcached.c](#plugininnodb_memcacheddaemon_memcacheddaemonmemcachedc)
 - [plugin/innodb_memcached/daemon_memcached/utilities/engine_loader.c](#plugininnodb_memcacheddaemon_memcachedutilitiesengine_loaderc)
 - [plugin/innodb_memcached/daemon_memcached/programs/engine_testapp.c](#plugininnodb_memcacheddaemon_memcachedprogramsengine_testappc)
 - [plugin/innodb_memcached/daemon_memcached/win32/dlfcn.h](#plugininnodb_memcacheddaemon_memcachedwin32dlfcnh)
 - [plugin/innodb_memcached/daemon_memcached/win32/dlfcn.c](#plugininnodb_memcacheddaemon_memcachedwin32dlfcnc)
 - [sql-common/client_plugin.cc](#sql-commonclient_plugincc)
 - [components/mysql_server/dynamic_loader_scheme_file.cc](#componentsmysql_serverdynamic_loader_scheme_filecc)
 - [sql/mysqld.cc](#sqlmysqldcc)
 - [sql/sys_vars.cc](#sqlsys_varscc)
 - [sql/set_var.h](#sqlset_varh)
 - [sql/sql_udf.cc](#sqlsql_udfcc)
 - [sql/sql_plugin.cc](#sqlsql_plugincc)

### storage/ndb/memcache/extra/memcached/daemon/memcached.c

```c

{% raw %}
6857 |     void *handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/utilities/engine_loader.c

```c

{% raw %}
31 |     handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/programs/engine_testapp.c

```c

{% raw %}
832 |     void* handle = dlopen(test_suite, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/win32/dlfcn.h

```c

{% raw %}
2 | void* dlopen(const char* path, int mode);
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/win32/dlfcn.c

```c

{% raw %}
12 | void* dlopen(const char* path, int mode) {
{% endraw %}

```
### router/src/plugin_info/src/library_file.cc

```cpp

{% raw %}
88 |   impl_->handle = dlopen(file_name.c_str(), RTLD_LOCAL | RTLD_LAZY);
{% endraw %}

```
### router/src/harness/src/loader-posix.cc

```cpp

{% raw %}
86 |       handle(dlopen(path.c_str(), RTLD_LOCAL | RTLD_NOW)) {
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/daemon/memcached.c

```c

{% raw %}
6951 |     void *handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/utilities/engine_loader.c

```c

{% raw %}
32 |     handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/programs/engine_testapp.c

```c

{% raw %}
807 |     void* handle = dlopen(test_suite, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/win32/dlfcn.h

```c

{% raw %}
2 | void* dlopen(const char* path, int mode);
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/win32/dlfcn.c

```c

{% raw %}
12 | void* dlopen(const char* path, int mode) {
{% endraw %}

```
### sql-common/client_plugin.cc

```cpp

{% raw %}
167 |   @param dlhandle       a handle to the shared object (returned by dlopen)
467 |   DBUG_PRINT("info", ("dlopeninig %s", dlpath));
469 |   if (!(dlhandle = dlopen(dlpath, RTLD_NOW))) {
473 |     if ((dlhandle = dlopen(dlpath, RTLD_NOW))) goto have_plugin;
487 |     DBUG_PRINT("info", ("failed to dlopen"));
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

```c

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