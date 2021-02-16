---
name: "mariadb"
layout: package
next_package: ipcalc
previous_package: cubew
languages: ['cpp', 'c']
---
## 10.1.23
30 / 20399 files match

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
652 |     if (dlopen(dl_info.dli_fname, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL) == 0)
654 |       sql_print_information("CONNECT: dlopen() failed, OEM table type is not supported");
{% endraw %}

```
### storage/connect/mycat.cc

```cpp

{% raw %}
413 |   if (!(hdll = dlopen(soname, RTLD_LAZY))) {
{% endraw %}

```
### wsrep/wsrep_loader.c

```c

{% raw %}
162 |     if (!(dlh = dlopen(spec, RTLD_NOW | RTLD_LOCAL))) {
163 |         snprintf(msg, sizeof(msg)-1, "wsrep_load(): dlopen(): %s", dlerror());
{% endraw %}

```
### wsrep/wsrep_api.h

```c

{% raw %}
39 |   Finally, wsrep_load() method loads (dlopens) wsrep provider library. It is
{% endraw %}

```
### sql-common/client_plugin.c

```c

{% raw %}
121 |   @param dlhandle       a handle to the shared object (returned by dlopen)
365 |   DBUG_PRINT ("info", ("dlopeninig %s", dlpath));
367 |   if (!(dlhandle= dlopen(dlpath, RTLD_NOW)))
369 |     DBUG_PRINT ("info", ("failed to dlopen"));
{% endraw %}

```
### sql/mysqld.cc

```cpp

{% raw %}
700 | SHOW_COMP_OPTION have_ssl, have_symlink, have_dlopen, have_query_cache;
8362 |   {"Opened_plugin_libraries",  (char*) &dlopen_count, SHOW_LONG},
8741 |   have_dlopen=SHOW_OPTION_YES;
8743 |   have_dlopen=SHOW_OPTION_NO;
{% endraw %}

```
### sql/sql_plugin.h

```c

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

```c

{% raw %}
373 | extern SHOW_COMP_OPTION have_ssl, have_symlink, have_dlopen;
{% endraw %}

```
### sql/sql_udf.cc

```cpp

{% raw %}
231 |       if (!(dl= dlopen(dlpath, RTLD_NOW)))
537 |     if (!(dl = dlopen(dlpath, RTLD_NOW)))
541 |       DBUG_PRINT("error",("dlopen of %s failed, error: %d (%s)",
{% endraw %}

```
### sql/sql_plugin.cc

```cpp

{% raw %}
233 | ulong dlopen_count;
759 |   if (!(plugin_dl.handle= dlopen(dlpath, RTLD_NOW)))
764 |   dlopen_count++;
1528 |   dlopen_count =0;
4148 |   next dlopen() these symbols will have old values, they won't be
{% endraw %}

```
### mysys/my_addr_resolve.c

```c

{% raw %}
228 |     struct link_map *lm = (struct link_map*) dlopen(0, RTLD_NOW);
{% endraw %}

```