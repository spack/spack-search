---
name: "mysql"
layout: package
next_package: tau
previous_package: pulseaudio
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c', 'cpp']
---
## 8.0.19
26 / 39146 files match, 18 filtered matches.

 - [storage/ndb/memcache/extra/memcached/daemon/memcached.c](#storagendbmemcacheextramemcacheddaemonmemcachedc)
 - [storage/ndb/memcache/extra/memcached/utilities/engine_loader.c](#storagendbmemcacheextramemcachedutilitiesengine_loaderc)
 - [storage/ndb/memcache/extra/memcached/programs/engine_testapp.c](#storagendbmemcacheextramemcachedprogramsengine_testappc)
 - [storage/ndb/memcache/extra/memcached/win32/dlfcn.h](#storagendbmemcacheextramemcachedwin32dlfcnh)
 - [storage/ndb/memcache/extra/memcached/win32/dlfcn.c](#storagendbmemcacheextramemcachedwin32dlfcnc)
 - [router/src/plugin_info/src/library_file.cc](#routersrcplugin_infosrclibrary_filecc)
 - [router/src/harness/src/loader-posix.cc](#routersrcharnesssrcloader-posixcc)
 - [plugin/auth/dialog.cc](#pluginauthdialogcc)
 - [plugin/innodb_memcached/daemon_memcached/daemon/memcached.c](#plugininnodb_memcacheddaemon_memcacheddaemonmemcachedc)
 - [plugin/innodb_memcached/daemon_memcached/utilities/engine_loader.c](#plugininnodb_memcacheddaemon_memcachedutilitiesengine_loaderc)
 - [plugin/innodb_memcached/daemon_memcached/programs/engine_testapp.c](#plugininnodb_memcacheddaemon_memcachedprogramsengine_testappc)
 - [plugin/innodb_memcached/daemon_memcached/win32/dlfcn.h](#plugininnodb_memcacheddaemon_memcachedwin32dlfcnh)
 - [plugin/innodb_memcached/daemon_memcached/win32/dlfcn.c](#plugininnodb_memcacheddaemon_memcachedwin32dlfcnc)
 - [extra/icu/source/common/putilimp.h](#extraicusourcecommonputilimph)
 - [sql-common/client_plugin.cc](#sql-commonclient_plugincc)
 - [components/mysql_server/dynamic_loader_scheme_file.cc](#componentsmysql_serverdynamic_loader_scheme_filecc)
 - [sql/sql_udf.cc](#sqlsql_udfcc)
 - [sql/sql_plugin.cc](#sqlsql_plugincc)

### storage/ndb/memcache/extra/memcached/daemon/memcached.c

```c

{% raw %}
6863 |         return false;
6864 |     }
6865 | 
6866 |     void *symbol = dlsym(handle, "memcached_extensions_initialize");
6867 |     if (symbol == NULL) {
6868 |         const char *msg = dlerror();
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/utilities/engine_loader.c

```c

{% raw %}
38 |         return false;
39 |     }
40 | 
41 |     void *symbol = dlsym(handle, "create_instance");
42 |     if (symbol == NULL) {
43 |         logger->log(EXTENSION_LOG_WARNING, NULL,
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/programs/engine_testapp.c

```c

{% raw %}
837 |     }
838 | 
839 |     //get the test cases
840 |     void *symbol = dlsym(handle, "get_tests");
841 |     if (symbol == NULL) {
842 |         const char *msg = dlerror();
859 |                                     .waitfor_cookie = waitfor_mock_cookie,
860 |                                     .time_travel = mock_time_travel,
861 |                                     .get_current_testcase = get_current_testcase };
862 |     symbol = dlsym(handle, "setup_suite");
863 |     if (symbol != NULL) {
864 |         my_setup_suite.voidptr = symbol;
906 |     }
907 | 
908 |     //tear down the suite if needed
909 |     symbol = dlsym(handle, "teardown_suite");
910 |     if (symbol != NULL) {
911 |         my_teardown_suite.voidptr = symbol;
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/win32/dlfcn.h

```c

{% raw %}
1 | #define DLFCN_H
2 | void* dlopen(const char* path, int mode);
3 | void* dlsym(void* handle, const char* symbol);
4 | int dlclose(void* handle);
5 | const char *dlerror(void);
{% endraw %}

```
### storage/ndb/memcache/extra/memcached/win32/dlfcn.c

```c

{% raw %}
27 |     return handle;
28 | }
29 | 
30 | void* dlsym(void* handle, const char* symbol) {
31 |     return GetProcAddress(handle, symbol);
32 | }
{% endraw %}

```
### router/src/plugin_info/src/library_file.cc

```cpp

{% raw %}
132 |   T *result{nullptr};
133 | 
134 | #ifndef _WIN32
135 |   result = reinterpret_cast<T *>(dlsym(impl_->handle, symbol.c_str()));
136 |   const char *error = dlerror();
137 |   if (error) {
{% endraw %}

```
### router/src/harness/src/loader-posix.cc

```cpp

{% raw %}
119 |   dlerror();  // clear any previous errors
120 | 
121 |   std::string symbol = "harness_plugin_" + name;
122 |   Plugin *p = reinterpret_cast<Plugin *>(dlsym(impl_->handle, symbol.c_str()));
123 | 
124 |   const char *error = dlerror();
{% endraw %}

```
### plugin/auth/dialog.cc

```cpp

{% raw %}
342 |                        size_t unused2 MY_ATTRIBUTE((unused)),
343 |                        int unused3 MY_ATTRIBUTE((unused)),
344 |                        va_list unused4 MY_ATTRIBUTE((unused))) {
345 |   void *sym = dlsym(RTLD_DEFAULT, "mysql_authentication_dialog_ask");
346 |   ask = sym ? (mysql_authentication_dialog_ask_t)sym : builtin_ask;
347 |   return 0;
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/daemon/memcached.c

```c

{% raw %}
6957 |         return false;
6958 |     }
6959 | 
6960 |     void *symbol = dlsym(handle, "memcached_extensions_initialize");
6961 |     if (symbol == NULL) {
6962 |         const char *msg = dlerror();
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/utilities/engine_loader.c

```c

{% raw %}
39 |         return false;
40 |     }
41 | 
42 |     void *symbol = dlsym(handle, "create_instance");
43 |     if (symbol == NULL) {
44 |         logger->log(EXTENSION_LOG_WARNING, NULL,
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/programs/engine_testapp.c

```c

{% raw %}
812 |     }
813 | 
814 |     //get the test cases
815 |     void *symbol = dlsym(handle, "get_tests");
816 |     if (symbol == NULL) {
817 |         const char *msg = dlerror();
833 |                                     .unlock_cookie = unlock_mock_cookie,
834 |                                     .waitfor_cookie = waitfor_mock_cookie,
835 |                                     .time_travel = mock_time_travel };
836 |     symbol = dlsym(handle, "setup_suite");
837 |     if (symbol != NULL) {
838 |         my_setup_suite.voidptr = symbol;
880 |     }
881 | 
882 |     //tear down the suite if needed
883 |     symbol = dlsym(handle, "teardown_suite");
884 |     if (symbol != NULL) {
885 |         my_teardown_suite.voidptr = symbol;
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/win32/dlfcn.h

```c

{% raw %}
1 | #define DLFCN_H
2 | void* dlopen(const char* path, int mode);
3 | void* dlsym(void* handle, const char* symbol);
4 | int dlclose(void* handle);
5 | const char *dlerror(void);
{% endraw %}

```
### plugin/innodb_memcached/daemon_memcached/win32/dlfcn.c

```c

{% raw %}
27 |     return handle;
28 | }
29 | 
30 | void* dlsym(void* handle, const char* symbol) {
31 |     return GetProcAddress(handle, symbol);
32 | }
{% endraw %}

```
### extra/icu/source/common/putilimp.h

```c

{% raw %}
589 |  * Extract a symbol from a library (function)
590 |  * @internal (ICU 4.8)
591 |  */
592 | U_INTERNAL UVoidFunction* U_EXPORT2 uprv_dlsym_func( void *lib, const char *symbolName, UErrorCode *status);
593 | 
594 | /**
{% endraw %}

```
### sql-common/client_plugin.cc

```cpp

{% raw %}
491 | #if defined(__APPLE__)
492 | have_plugin:
493 | #endif
494 |   if (!(sym = dlsym(dlhandle, plugin_declarations_sym))) {
495 |     errmsg = "not a plugin";
496 |     dlclose(dlhandle);
{% endraw %}

```
### components/mysql_server/dynamic_loader_scheme_file.cc

```cpp

{% raw %}
122 | 
123 |     /* Look for "list_components" function. */
124 |     list_components_func list_func = reinterpret_cast<list_components_func>(
125 |         dlsym(handle, "list_components"));
126 |     if (list_func == NULL) {
127 |       return true;
183 | 
184 |     /* Delete entry from library entry points list. */
185 |     list_components_func list_func = reinterpret_cast<list_components_func>(
186 |         dlsym(it->second, "list_components"));
187 |     library_entry_set.erase(list_func);
188 | 
{% endraw %}

```
### sql/sql_udf.cc

```cpp

{% raw %}
112 | static char *init_syms(udf_func *tmp, char *nm) {
113 |   char *end;
114 | 
115 |   if (!((tmp->func = (Udf_func_any)dlsym(tmp->dlhandle, tmp->name.str))))
116 |     return tmp->name.str;
117 | 
119 | 
120 |   if (tmp->type == UDFTYPE_AGGREGATE) {
121 |     (void)my_stpcpy(end, "_clear");
122 |     if (!((tmp->func_clear = (Udf_func_clear)dlsym(tmp->dlhandle, nm))))
123 |       return nm;
124 |     (void)my_stpcpy(end, "_add");
125 |     if (!((tmp->func_add = (Udf_func_add)dlsym(tmp->dlhandle, nm)))) return nm;
126 |   }
127 | 
128 |   (void)my_stpcpy(end, "_deinit");
129 |   tmp->func_deinit = (Udf_func_deinit)dlsym(tmp->dlhandle, nm);
130 | 
131 |   (void)my_stpcpy(end, "_init");
132 |   tmp->func_init = (Udf_func_init)dlsym(tmp->dlhandle, nm);
133 | 
134 |   /*
{% endraw %}

```
### sql/sql_plugin.cc

```cpp

{% raw %}
704 |     return NULL;
705 |   }
706 |   /* Determine interface version */
707 |   if (!(sym = dlsym(plugin_dl.handle, plugin_interface_version_sym))) {
708 |     free_plugin_mem(&plugin_dl);
709 |     mysql_rwlock_unlock(&LOCK_system_variables_hash);
725 | 
726 |   /* link the services in */
727 |   for (i = 0; i < array_elements(list_of_services); i++) {
728 |     if ((sym = dlsym(plugin_dl.handle, list_of_services[i].name))) {
729 |       uint ver = (uint)(intptr) * (void **)sym;
730 |       if ((*(void **)sym) !=
744 |   }
745 | 
746 |   /* Find plugin declarations */
747 |   if (!(sym = dlsym(plugin_dl.handle, plugin_declarations_sym))) {
748 |     free_plugin_mem(&plugin_dl);
749 |     mysql_rwlock_unlock(&LOCK_system_variables_hash);
757 |     st_mysql_plugin *old, *cur;
758 |     char *ptr = (char *)sym;
759 | 
760 |     if ((sym = dlsym(plugin_dl.handle, sizeof_st_plugin_sym)))
761 |       sizeof_st_plugin = *(int *)sym;
762 |     else {
{% endraw %}

```