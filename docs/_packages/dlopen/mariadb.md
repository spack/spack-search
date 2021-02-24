---
name: "mariadb"
layout: package
next_package: heaptrack
previous_package: wireshark
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c', 'cpp']
---
## 10.1.23
30 / 20399 files match, 12 filtered matches.

 - [storage/connect/ha_connect.cc](#storageconnectha_connectcc)
 - [storage/connect/mycat.cc](#storageconnectmycatcc)
 - [wsrep/wsrep_loader.c](#wsrepwsrep_loaderc)
 - [wsrep/wsrep_api.h](#wsrepwsrep_apih)
 - [sql-common/client_plugin.c](#sql-commonclient_pluginc)
 - [sql/mysqld.cc](#sqlmysqldcc)
 - [sql/sql_plugin.h](#sqlsql_pluginh)
 - [sql/sys_vars.cc](#sqlsys_varscc)
 - [sql/set_var.h](#sqlset_varh)
 - [sql/sql_udf.cc](#sqlsql_udfcc)
 - [sql/sql_plugin.cc](#sqlsql_plugincc)
 - [mysys/my_addr_resolve.c](#mysysmy_addr_resolvec)

### storage/connect/ha_connect.cc

```cpp

{% raw %}
649 |   Dl_info dl_info;
650 |   if (dladdr(&connect_hton, &dl_info))
651 |   {
652 |     if (dlopen(dl_info.dli_fname, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL) == 0)
653 |     {
654 |       sql_print_information("CONNECT: dlopen() failed, OEM table type is not supported");
655 |       sql_print_information("CONNECT: %s", dlerror());
656 |     }
{% endraw %}

```
### storage/connect/mycat.cc

```cpp

{% raw %}
410 |   const char *error = NULL;
411 | 
412 |   // Load the desired shared library
413 |   if (!(hdll = dlopen(soname, RTLD_LAZY))) {
414 |     error = dlerror();
415 |     sprintf(g->Message, MSG(SHARED_LIB_ERR), soname, SVP(error));
{% endraw %}

```
### wsrep/wsrep_loader.c

```c

{% raw %}
159 |         return ret;
160 |     }
161 | 
162 |     if (!(dlh = dlopen(spec, RTLD_NOW | RTLD_LOCAL))) {
163 |         snprintf(msg, sizeof(msg)-1, "wsrep_load(): dlopen(): %s", dlerror());
164 |         logger (WSREP_LOG_ERROR, msg);
165 |         ret = EINVAL;
{% endraw %}

```
### wsrep/wsrep_api.h

```c

{% raw %}
36 |   struct wsrep is the interface to wsrep provider. It contains all wsrep API
37 |   calls. It is a provider part of wsrep API contract.
38 | 
39 |   Finally, wsrep_load() method loads (dlopens) wsrep provider library. It is
40 |   defined in wsrep_loader.c unit and is part of libwsrep.a (which is not a
41 |   wsrep provider, but a convenience library).
{% endraw %}

```
### sql-common/client_plugin.c

```c

{% raw %}
118 | 
119 |   @param mysql          MYSQL structure (for error reporting)
120 |   @param plugin         plugin to install
121 |   @param dlhandle       a handle to the shared object (returned by dlopen)
122 |                         or 0 if the plugin was not dynamically loaded
123 |   @param argc           number of arguments in the 'va_list args'
362 |            mysql->options.extension->plugin_dir : PLUGINDIR, "/",
363 |            name, SO_EXT, NullS);
364 |    
365 |   DBUG_PRINT ("info", ("dlopeninig %s", dlpath));
366 |   /* Open new dll handle */
367 |   if (!(dlhandle= dlopen(dlpath, RTLD_NOW)))
368 |   {
369 |     DBUG_PRINT ("info", ("failed to dlopen"));
370 |     errmsg= dlerror();
371 |     goto err;
{% endraw %}

```
### sql/mysqld.cc

```cpp

{% raw %}
697 | MY_LOCALE *my_default_lc_messages;
698 | MY_LOCALE *my_default_lc_time_names;
699 | 
700 | SHOW_COMP_OPTION have_ssl, have_symlink, have_dlopen, have_query_cache;
701 | SHOW_COMP_OPTION have_geometry, have_rtree_keys;
702 | SHOW_COMP_OPTION have_crypt, have_compress;
8359 |   {"Open_table_definitions",   (char*) &show_table_definitions, SHOW_SIMPLE_FUNC},
8360 |   {"Open_tables",              (char*) &show_open_tables,       SHOW_SIMPLE_FUNC},
8361 |   {"Opened_files",             (char*) &my_file_total_opened, SHOW_LONG_NOFLUSH},
8362 |   {"Opened_plugin_libraries",  (char*) &dlopen_count, SHOW_LONG},
8363 |   {"Opened_table_definitions", (char*) offsetof(STATUS_VAR, opened_shares), SHOW_LONG_STATUS},
8364 |   {"Opened_tables",            (char*) offsetof(STATUS_VAR, opened_tables), SHOW_LONG_STATUS},
8738 |   have_symlink=SHOW_OPTION_YES;
8739 | #endif
8740 | #ifdef HAVE_DLOPEN
8741 |   have_dlopen=SHOW_OPTION_YES;
8742 | #else
8743 |   have_dlopen=SHOW_OPTION_NO;
8744 | #endif
8745 | #ifdef HAVE_QUERY_CACHE
{% endraw %}

```
### sql/sql_plugin.h

```c

{% raw %}
36 |   PLUGIN_FORCE_PLUS_PERMANENT };
37 | extern const char *global_plugin_typelib_names[];
38 | 
39 | extern ulong dlopen_count;
40 | 
41 | #include <my_sys.h>
{% endraw %}

```
### sql/sys_vars.cc

```cpp

{% raw %}
4068 |        "have_crypt", "have_crypt",
4069 |        READ_ONLY GLOBAL_VAR(have_crypt), NO_CMD_LINE);
4070 | 
4071 | static Sys_var_have Sys_have_dlopen(
4072 |        "have_dynamic_loading", "have_dynamic_loading",
4073 |        READ_ONLY GLOBAL_VAR(have_dlopen), NO_CMD_LINE);
4074 | 
4075 | static Sys_var_have Sys_have_geometry(
{% endraw %}

```
### sql/set_var.h

```c

{% raw %}
370 | extern SHOW_COMP_OPTION have_ndbcluster, have_partitioning;
371 | extern SHOW_COMP_OPTION have_profiling;
372 | 
373 | extern SHOW_COMP_OPTION have_ssl, have_symlink, have_dlopen;
374 | extern SHOW_COMP_OPTION have_query_cache;
375 | extern SHOW_COMP_OPTION have_geometry, have_rtree_keys;
{% endraw %}

```
### sql/sql_udf.cc

```cpp

{% raw %}
228 |       char dlpath[FN_REFLEN];
229 |       strxnmov(dlpath, sizeof(dlpath) - 1, opt_plugin_dir, "/", tmp->dl, NullS);
230 |       (void) unpack_filename(dlpath, dlpath);
231 |       if (!(dl= dlopen(dlpath, RTLD_NOW)))
232 |       {
233 | 	/* Print warning to log */
534 |     strxnmov(dlpath, sizeof(dlpath) - 1, opt_plugin_dir, "/", udf->dl, NullS);
535 |     (void) unpack_filename(dlpath, dlpath);
536 | 
537 |     if (!(dl = dlopen(dlpath, RTLD_NOW)))
538 |     {
539 |       my_error(ER_CANT_OPEN_LIBRARY, MYF(0),
540 |                udf->dl, errno, my_dlerror(dlpath));
541 |       DBUG_PRINT("error",("dlopen of %s failed, error: %d (%s)",
542 |                           udf->dl, errno, dlerror()));
543 |       goto err;
{% endraw %}

```
### sql/sql_plugin.cc

```cpp

{% raw %}
230 | static int plugin_array_version=0;
231 | 
232 | static bool initialized= 0;
233 | ulong dlopen_count;
234 | 
235 | 
756 |   (void) unpack_filename(dlpath, dlpath);
757 |   plugin_dl.ref_count= 1;
758 |   /* Open new dll handle */
759 |   if (!(plugin_dl.handle= dlopen(dlpath, RTLD_NOW)))
760 |   {
761 |     report_error(report, ER_CANT_OPEN_LIBRARY, dlpath, errno, my_dlerror(dlpath));
762 |     goto ret;
763 |   }
764 |   dlopen_count++;
765 | 
766 | #ifdef HAVE_LINK_H
1525 |   if (initialized)
1526 |     DBUG_RETURN(0);
1527 | 
1528 |   dlopen_count =0;
1529 | 
1530 |   init_alloc_root(&plugin_mem_root, 4096, 4096, MYF(0));
4145 | /*
4146 |   On dlclose() we need to restore values of all symbols that we've modified in
4147 |   the DSO. The reason is - the DSO might not actually be unloaded, so on the
4148 |   next dlopen() these symbols will have old values, they won't be
4149 |   reinitialized.
4150 | 
{% endraw %}

```
### mysys/my_addr_resolve.c

```c

{% raw %}
225 |     pid_t pid;
226 | 
227 | #if defined(HAVE_LINK_H) && defined(HAVE_DLOPEN)
228 |     struct link_map *lm = (struct link_map*) dlopen(0, RTLD_NOW);
229 |     if (lm)
230 |       offset= lm->l_addr;
{% endraw %}

```