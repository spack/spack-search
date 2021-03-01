---
name: "mariadb"
layout: package
next_package: mc
previous_package: lvm2
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp', 'c']
---
## 10.1.23
24 / 20399 files match, 13 filtered matches.

 - [storage/connect/mycat.cc](#storageconnectmycatcc)
 - [storage/tokudb/hatoku_hton.cc](#storagetokudbhatoku_htoncc)
 - [storage/tokudb/PerconaFT/portability/memory.cc](#storagetokudbperconaftportabilitymemorycc)
 - [storage/tokudb/PerconaFT/portability/toku_assert.cc](#storagetokudbperconaftportabilitytoku_assertcc)
 - [storage/tokudb/PerconaFT/portability/os_malloc.cc](#storagetokudbperconaftportabilityos_malloccc)
 - [storage/tokudb/PerconaFT/src/tests/loader-stress-del.cc](#storagetokudbperconaftsrctestsloader-stress-delcc)
 - [storage/tokudb/PerconaFT/src/tests/loader-stress-test.cc](#storagetokudbperconaftsrctestsloader-stress-testcc)
 - [wsrep/wsrep_loader.c](#wsrepwsrep_loaderc)
 - [plugin/auth_dialog/dialog.c](#pluginauth_dialogdialogc)
 - [plugin/server_audit/server_audit.c](#pluginserver_auditserver_auditc)
 - [sql-common/client_plugin.c](#sql-commonclient_pluginc)
 - [sql/sql_udf.cc](#sqlsql_udfcc)
 - [sql/sql_plugin.cc](#sqlsql_plugincc)

### storage/connect/mycat.cc

```cpp

{% raw %}
417 |     } // endif Hdll
418 | 
419 |   // Get the function returning an instance of the external DEF class
420 |   if (!(coldef = (XCOLDEF)dlsym(hdll, getname))) {
421 |     error = dlerror();
422 |     sprintf(g->Message, MSG(GET_FUNC_ERR), getname, SVP(error));
{% endraw %}

```
### storage/tokudb/hatoku_hton.cc

```cpp

{% raw %}
279 |             void*,
280 |             size_t);
281 |         mallctl_type mallctl_func;
282 |         mallctl_func= (mallctl_type)dlsym(RTLD_DEFAULT, "mallctl");
283 |         if (!mallctl_func) {
284 |             sql_print_error(
{% endraw %}

```
### storage/tokudb/PerconaFT/portability/memory.cc

```cpp

{% raw %}
95 |     // to get version and mmap threshold configuration.
96 |     typedef int (*mallctl_fun_t)(const char *, void *, size_t *, void *, size_t);
97 |     mallctl_fun_t mallctl_f;
98 |     mallctl_f = (mallctl_fun_t) dlsym(RTLD_DEFAULT, "mallctl");
99 |     if (mallctl_f) { // jemalloc is loaded
100 |         size_t version_length = sizeof status.mallocator_version;
{% endraw %}

```
### storage/tokudb/PerconaFT/portability/toku_assert.cc

```cpp

{% raw %}
62 | void
63 | toku_assert_init(void)
64 | {
65 |     malloc_stats_f = (malloc_stats_fun_t) dlsym(RTLD_DEFAULT, "malloc_stats");
66 | }
67 | 
{% endraw %}

```
### storage/tokudb/PerconaFT/portability/os_malloc.cc

```cpp

{% raw %}
280 | size_t os_malloc_usable_size(const void *p) {
281 |     if (p==NULL) return 0;
282 |     if (!malloc_usable_size_f) {
283 |         malloc_usable_size_f = (malloc_usable_size_fun_t) dlsym(RTLD_DEFAULT, "malloc_usable_size");
284 |         if (!malloc_usable_size_f) {
285 |             malloc_usable_size_f = (malloc_usable_size_fun_t) dlsym(RTLD_DEFAULT, "malloc_size"); // darwin
286 |             if (!malloc_usable_size_f) {
287 |                 abort(); // couldn't find a malloc size function
{% endraw %}

```
### storage/tokudb/PerconaFT/src/tests/loader-stress-del.cc

```cpp

{% raw %}
626 |     if (footprint_print) {
627 |         printf("%s:%d Hiwater=%ld water=%ld (extra hiwater=%ldM) mcount=%lld fcount=%lld\n", __FILE__, __LINE__, hiwater, water, (hiwater-hiwater_start)/(1024*1024), mcount, fcount);
628 |         typedef void (*malloc_stats_fun_t)(void);
629 |         malloc_stats_fun_t malloc_stats_f = (malloc_stats_fun_t) dlsym(RTLD_DEFAULT, "malloc_stats");
630 |         if (malloc_stats_f) {
631 |             malloc_stats_f();
{% endraw %}

```
### storage/tokudb/PerconaFT/src/tests/loader-stress-test.cc

```cpp

{% raw %}
585 |     if (footprint_print) {
586 |         printf("%s:%d Hiwater=%ld water=%ld (extra hiwater=%ldM) mcount=%lld fcount=%lld\n", __FILE__, __LINE__, hiwater, water, (hiwater-hiwater_start)/(1024*1024), mcount, fcount);
587 |         typedef void (*malloc_stats_fun_t)(void);
588 |         malloc_stats_fun_t malloc_stats_f = (malloc_stats_fun_t) dlsym(RTLD_DEFAULT, "malloc_stats");
589 |         if (malloc_stats_f) {
590 |             malloc_stats_f();
{% endraw %}

```
### wsrep/wsrep_loader.c

```c

{% raw %}
113 |         wsrep_loader_fun dlfun;
114 |         void *obj;
115 |     } alias;
116 |     alias.obj = dlsym(dlh, sym);
117 |     return alias.dlfun;
118 | }
120 | static int wsrep_check_version_symbol(void *dlh)
121 | {
122 |     char** dlversion = NULL;
123 |     dlversion = (char**) dlsym(dlh, "wsrep_interface_version");
124 |     if (dlversion == NULL)
125 |         return 0;
{% endraw %}

```
### plugin/auth_dialog/dialog.c

```c

{% raw %}
170 |                        int unused3     __attribute__((unused)), 
171 |                        va_list unused4 __attribute__((unused)))
172 | {
173 |   void *sym= dlsym(RTLD_DEFAULT, "mysql_authentication_dialog_ask");
174 |   ask= sym ? (mysql_authentication_dialog_ask_t) sym : builtin_ask;
175 |   return 0;
{% endraw %}

```
### plugin/server_audit/server_audit.c

```c

{% raw %}
2306 |   }
2307 |   if (!mysql_57_started)
2308 |   {
2309 |     const void *my_hash_init_ptr= dlsym(RTLD_DEFAULT, "_my_hash_init");
2310 |     if (!my_hash_init_ptr)
2311 |     {
2312 |       maria_above_5= 1;
2313 |       my_hash_init_ptr= dlsym(RTLD_DEFAULT, "my_hash_init2");
2314 |     }
2315 |     if (!my_hash_init_ptr)
2316 |       return 1;
2317 |   }
2318 | 
2319 |   if(!(int_mysql_data_home= dlsym(RTLD_DEFAULT, "mysql_data_home")))
2320 |   {
2321 |     if(!(int_mysql_data_home= dlsym(RTLD_DEFAULT, "?mysql_data_home@@3PADA")))
2322 |       int_mysql_data_home= &default_home;
2323 |   }
2374 |   /* so we warn users if both Query Cashe and TABLE events enabled.      */
2375 |   if (!started_mysql && FILTER(EVENT_TABLE))
2376 |   {
2377 |     ulonglong *qc_size= (ulonglong *) dlsym(RTLD_DEFAULT, "query_cache_size");
2378 |     if (qc_size == NULL || *qc_size != 0)
2379 |     {
2380 |       struct loc_system_variables *g_sys_var=
2381 |         (struct loc_system_variables *) dlsym(RTLD_DEFAULT,
2382 |                                           "global_system_variables");
2383 |       if (g_sys_var && g_sys_var->query_cache_type != 0)
{% endraw %}

```
### sql-common/client_plugin.c

```c

{% raw %}
371 |     goto err;
372 |   }
373 | 
374 |   if (!(sym= dlsym(dlhandle, plugin_declarations_sym)))
375 |   {
376 |     errmsg= "not a plugin";
{% endraw %}

```
### sql/sql_udf.cc

```cpp

{% raw %}
62 | {
63 |   char *end;
64 | 
65 |   if (!((tmp->func= (Udf_func_any) dlsym(tmp->dlhandle, tmp->name.str))))
66 |     return tmp->name.str;
67 | 
70 |   if (tmp->type == UDFTYPE_AGGREGATE)
71 |   {
72 |     (void)strmov(end, "_clear");
73 |     if (!((tmp->func_clear= (Udf_func_clear) dlsym(tmp->dlhandle, nm))))
74 |       return nm;
75 |     (void)strmov(end, "_add");
76 |     if (!((tmp->func_add= (Udf_func_add) dlsym(tmp->dlhandle, nm))))
77 |       return nm;
78 |   }
79 | 
80 |   (void) strmov(end,"_deinit");
81 |   tmp->func_deinit= (Udf_func_deinit) dlsym(tmp->dlhandle, nm);
82 | 
83 |   (void) strmov(end,"_init");
84 |   tmp->func_init= (Udf_func_init) dlsym(tmp->dlhandle, nm);
85 | 
86 |   /*
{% endraw %}

```
### sql/sql_plugin.cc

```cpp

{% raw %}
539 |     DBUG_RETURN(TRUE);
540 |   }
541 |   /* Find plugin declarations */
542 |   if (!(sym= dlsym(plugin_dl->handle, plugin_declarations_sym)))
543 |   {
544 |     report_error(report, ER_CANT_FIND_DL_ENTRY, plugin_declarations_sym);
553 |     struct st_maria_plugin *cur;
554 |     char *ptr= (char *)sym;
555 | 
556 |     if ((sym= dlsym(plugin_dl->handle, sizeof_st_plugin_sym)))
557 |       sizeof_st_plugin= *(int *)sym;
558 |     else
660 |     DBUG_RETURN(TRUE);
661 |   }
662 |   /* Find plugin declarations */
663 |   if (!(sym= dlsym(plugin_dl->handle, maria_plugin_declarations_sym)))
664 |   {
665 |     report_error(report, ER_CANT_FIND_DL_ENTRY, maria_plugin_declarations_sym);
671 |     struct st_maria_plugin *old, *cur;
672 |     char *ptr= (char *)sym;
673 | 
674 |     if ((sym= dlsym(plugin_dl->handle, maria_sizeof_st_plugin_sym)))
675 |       sizeof_st_plugin= *(int *)sym;
676 |     else
772 | #endif
773 | 
774 |   /* Checks which plugin interface present and reads info */
775 |   if (!(sym= dlsym(plugin_dl.handle, maria_plugin_interface_version_sym)))
776 |   {
777 |     if (read_mysql_plugin_info(&plugin_dl,
778 |                                dlsym(plugin_dl.handle,
779 |                                      plugin_interface_version_sym),
780 |                                dlpath,
790 |   /* link the services in */
791 |   for (i= 0; i < array_elements(list_of_services); i++)
792 |   {
793 |     if ((sym= dlsym(plugin_dl.handle, list_of_services[i].name)))
794 |     {
795 |       void **ptr= (void **)sym;
{% endraw %}

```