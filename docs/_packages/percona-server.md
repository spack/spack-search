---
name: "percona-server"
layout: package
next_package: perl
previous_package: pdsh
languages: ['cpp', 'c']
---
## 8.0.20-11
33 / 44426 files match, 20 filtered matches.

 - [storage/ndb/memcache/extra/memcached/daemon/memcached.c](#storagendbmemcacheextramemcacheddaemonmemcachedc)
 - [storage/ndb/memcache/extra/memcached/utilities/engine_loader.c](#storagendbmemcacheextramemcachedutilitiesengine_loaderc)
 - [storage/ndb/memcache/extra/memcached/programs/engine_testapp.c](#storagendbmemcacheextramemcachedprogramsengine_testappc)
 - [storage/ndb/memcache/extra/memcached/win32/dlfcn.h](#storagendbmemcacheextramemcachedwin32dlfcnh)
 - [storage/ndb/memcache/extra/memcached/win32/dlfcn.c](#storagendbmemcacheextramemcachedwin32dlfcnc)
 - [router/src/plugin_info/src/library_file.cc](#routersrcplugin_infosrclibrary_filecc)
 - [router/src/harness/src/dynamic_loader.cc](#routersrcharnesssrcdynamic_loadercc)
 - [plugin/innodb_memcached/daemon_memcached/daemon/memcached.c](#plugininnodb_memcacheddaemon_memcacheddaemonmemcachedc)
 - [plugin/innodb_memcached/daemon_memcached/utilities/engine_loader.c](#plugininnodb_memcacheddaemon_memcachedutilitiesengine_loaderc)
 - [plugin/innodb_memcached/daemon_memcached/programs/engine_testapp.c](#plugininnodb_memcacheddaemon_memcachedprogramsengine_testappc)
 - [plugin/innodb_memcached/daemon_memcached/win32/dlfcn.h](#plugininnodb_memcacheddaemon_memcachedwin32dlfcnh)
 - [plugin/innodb_memcached/daemon_memcached/win32/dlfcn.c](#plugininnodb_memcacheddaemon_memcachedwin32dlfcnc)
 - [sql-common/client_plugin.cc](#sql-commonclient_plugincc)
 - [components/libminchassis/dynamic_loader_scheme_file.cc](#componentslibminchassisdynamic_loader_scheme_filecc)
 - [sql/mysqld.cc](#sqlmysqldcc)
 - [sql/sys_vars.cc](#sqlsys_varscc)
 - [sql/set_var.h](#sqlset_varh)
 - [sql/sql_udf.cc](#sqlsql_udfcc)
 - [sql/sql_plugin.cc](#sqlsql_plugincc)
 - [libmysql/authentication_ldap/auth_ldap_sasl_client.cc](#libmysqlauthentication_ldapauth_ldap_sasl_clientcc)

### storage/ndb/memcache/extra/memcached/daemon/memcached.c

```c

{% raw %}
6854 |         void* voidptr;
6855 |     } funky = {.initialize = NULL };
6856 | 
6857 |     void *handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
6858 |     if (handle == NULL) {
6859 |         const char *msg = dlerror();
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/utilities/engine_loader.c

```c

{% raw %}
28 |         void* voidptr;
29 |     } my_create = {.create = NULL };
30 | 
31 |     handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
32 |     if (handle == NULL) {
33 |         const char *msg = dlerror();
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/programs/engine_testapp.c

```c

{% raw %}
829 |     }
830 | 
831 |     //load test_suite
832 |     void* handle = dlopen(test_suite, RTLD_NOW | RTLD_LOCAL);
833 |     if (handle == NULL) {
834 |         const char *msg = dlerror();
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/win32/dlfcn.h

```c

{% raw %}
1 | #define DLFCN_H
2 | void* dlopen(const char* path, int mode);
3 | void* dlsym(void* handle, const char* symbol);
4 | int dlclose(void* handle);
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/win32/dlfcn.c

```c

{% raw %}
9 |  */
10 | static bool self = false;
11 | 
12 | void* dlopen(const char* path, int mode) {
13 |     if (path == NULL) {
14 |         // We don't support opening ourself
{% endraw %}

```
### router/src/plugin_info/src/library_file.cc

```cpp

{% raw %}
85 |       plugin_name_(plugin_name),
86 |       file_name_(file_name) {
87 | #ifndef _WIN32
88 |   impl_->handle = dlopen(file_name.c_str(), RTLD_LOCAL | RTLD_LAZY);
89 |   if (impl_->handle == nullptr) {
90 |     throw std::runtime_error("Could not load plugin file: " + file_name +
{% endraw %}

```
### router/src/harness/src/dynamic_loader.cc

```cpp

{% raw %}
138 |           .str();
139 | 
140 |   const DynamicLibrary::native_handle_type handle =
141 |       dlopen(filename.c_str(), RTLD_LOCAL | RTLD_NOW);
142 |   if (handle == nullptr) {
143 |     error_msg_ = dlerror();
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/daemon/memcached.c

```c

{% raw %}
6948 |         void* voidptr;
6949 |     } funky = {.initialize = NULL };
6950 | 
6951 |     void *handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
6952 |     if (handle == NULL) {
6953 |         const char *msg = dlerror();
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/utilities/engine_loader.c

```c

{% raw %}
29 |         void* voidptr;
30 |     } my_create = {.create = NULL };
31 | 
32 |     handle = dlopen(soname, RTLD_NOW | RTLD_LOCAL);
33 |     if (handle == NULL) {
34 |         const char *msg = dlerror();
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/programs/engine_testapp.c

```c

{% raw %}
804 |     }
805 | 
806 |     //load test_suite
807 |     void* handle = dlopen(test_suite, RTLD_NOW | RTLD_LOCAL);
808 |     if (handle == NULL) {
809 |         const char *msg = dlerror();
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/win32/dlfcn.h

```c

{% raw %}
1 | #define DLFCN_H
2 | void* dlopen(const char* path, int mode);
3 | void* dlsym(void* handle, const char* symbol);
4 | int dlclose(void* handle);
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/win32/dlfcn.c

```c

{% raw %}
9 |  */
10 | static bool self = false;
11 | 
12 | void* dlopen(const char* path, int mode) {
13 |     if (path == NULL) {
14 |         // We don't support opening ourself
{% endraw %}

```
### sql-common/client_plugin.cc

```cpp

{% raw %}
164 | 
165 |   @param mysql          MYSQL structure (for error reporting)
166 |   @param plugin         plugin to install
167 |   @param dlhandle       a handle to the shared object (returned by dlopen)
168 |                         or 0 if the plugin was not dynamically loaded
169 |   @param argc           number of arguments in the 'va_list args'
464 |   /* Compile dll path */
465 |   strxnmov(dlpath, sizeof(dlpath) - 1, plugindir, "/", name, SO_EXT, NullS);
466 | 
467 |   DBUG_PRINT("info", ("dlopeninig %s", dlpath));
468 |   /* Open new dll handle */
469 |   if (!(dlhandle = dlopen(dlpath, RTLD_NOW))) {
470 | #if defined(__APPLE__)
471 |     /* Apple supports plugins with .so also, so try this as well */
472 |     strxnmov(dlpath, sizeof(dlpath) - 1, plugindir, "/", name, ".so", NullS);
473 |     if ((dlhandle = dlopen(dlpath, RTLD_NOW))) goto have_plugin;
474 | #endif
475 | 
484 | #else
485 |     errmsg = dlerror();
486 | #endif
487 |     DBUG_PRINT("info", ("failed to dlopen"));
488 |     goto err;
489 |   }
{% endraw %}

```
### components/libminchassis/dynamic_loader_scheme_file.cc

```cpp

{% raw %}
124 | #endif
125 | 
126 |     /* Open library. */
127 |     void *handle = dlopen(file_name.c_str(), RTLD_NOW);
128 |     if (handle == NULL) {
129 |       const char *errmsg;
130 |       int error_number = dlopen_errno;
131 |       DLERROR_GENERATE(errmsg, error_number);
132 |       mysql_error_service_printf(ER_CANT_OPEN_LIBRARY, MYF(0),
{% endraw %}

```
### sql/mysqld.cc

```cpp

{% raw %}
1345 | MY_LOCALE *my_default_lc_messages;
1346 | MY_LOCALE *my_default_lc_time_names;
1347 | 
1348 | SHOW_COMP_OPTION have_symlink, have_dlopen, have_query_cache;
1349 | SHOW_COMP_OPTION have_geometry, have_rtree_keys;
1350 | SHOW_COMP_OPTION have_compress;
9595 | 
9596 |   have_symlink = SHOW_OPTION_YES;
9597 | 
9598 |   have_dlopen = SHOW_OPTION_YES;
9599 | 
9600 |   have_query_cache = SHOW_OPTION_NO;
{% endraw %}

```
### sql/sys_vars.cc

```cpp

{% raw %}
5630 |     "have_compress", "have_compress",
5631 |     READ_ONLY NON_PERSIST GLOBAL_VAR(have_compress), NO_CMD_LINE);
5632 | 
5633 | static Sys_var_have Sys_have_dlopen(
5634 |     "have_dynamic_loading", "have_dynamic_loading",
5635 |     READ_ONLY NON_PERSIST GLOBAL_VAR(have_dlopen), NO_CMD_LINE);
5636 | 
5637 | static Sys_var_have Sys_have_geometry(
{% endraw %}

```
### sql/set_var.h

```c

{% raw %}
491 | /* optional things, have_* variables */
492 | extern SHOW_COMP_OPTION have_profiling;
493 | 
494 | extern SHOW_COMP_OPTION have_symlink, have_dlopen;
495 | extern SHOW_COMP_OPTION have_query_cache;
496 | extern SHOW_COMP_OPTION have_geometry, have_rtree_keys;
{% endraw %}

```
### sql/sql_udf.cc

```cpp

{% raw %}
272 |       char dlpath[FN_REFLEN];
273 |       strxnmov(dlpath, sizeof(dlpath) - 1, opt_plugin_dir, "/", tmp->dl, NullS);
274 |       (void)unpack_filename(dlpath, dlpath);
275 |       if (!(dl = dlopen(dlpath, RTLD_NOW))) {
276 |         const char *errmsg;
277 |         int error_number = dlopen_errno;
278 |         DLERROR_GENERATE(errmsg, error_number);
279 | 
636 |     strxnmov(dlpath, sizeof(dlpath) - 1, opt_plugin_dir, "/", udf->dl, NullS);
637 |     (void)unpack_filename(dlpath, dlpath);
638 | 
639 |     if (!(dl = dlopen(dlpath, RTLD_NOW))) {
640 |       const char *errmsg;
641 |       int error_number = dlopen_errno;
642 |       DLERROR_GENERATE(errmsg, error_number);
643 | 
644 |       DBUG_PRINT("error", ("dlopen of %s failed, error: %d (%s)", udf->dl,
645 |                            error_number, errmsg));
646 |       my_error(ER_CANT_OPEN_LIBRARY, MYF(0), udf->dl, error_number, errmsg);
{% endraw %}

```
### sql/sql_plugin.cc

```cpp

{% raw %}
669 |   plugin_dl.ref_count = 1;
670 |   /* Open new dll handle */
671 |   mysql_mutex_assert_owner(&LOCK_plugin);
672 |   if (!(plugin_dl.handle = dlopen(dlpath, RTLD_NOW))) {
673 |     const char *errmsg;
674 |     int error_number = dlopen_errno;
675 |     /*
676 |       Conforming applications should use a critical section to retrieve
{% endraw %}

```
### libmysql/authentication_ldap/auth_ldap_sasl_client.cc

```cpp

{% raw %}
515 |    */
516 |   char sasl_plugin_dir[PATH_MAX]{};
517 |   // dlopen(NULL, ) should not fail ...
518 |   void *main_handle = dlopen(nullptr, RTLD_LAZY);
519 |   if (main_handle == nullptr) {
520 |     log_error(dlerror());
{% endraw %}

```