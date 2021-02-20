---
name: "mariadb-c-client"
layout: package
next_package: mc
previous_package: mariadb
languages: ['c']
---
## 2.3.1
4 / 200 files match, 1 filtered matches.

 - [libmariadb/client_plugin.c](#libmariadbclient_pluginc)

### libmariadb/client_plugin.c

```c

{% raw %}
127 | 
128 |   @param mysql          MYSQL structure (for error reporting)
129 |   @param plugin         plugin to install
130 |   @param dlhandle       a handle to the shared object (returned by dlopen)
131 |                         or 0 if the plugin was not dynamically loaded
132 |   @param argc           number of arguments in the 'va_list args'
371 |            name, SO_EXT, NullS);
372 |    
373 |   /* Open new dll handle */
374 |   if (!(dlhandle= dlopen((const char *)dlpath, RTLD_NOW)))
375 |   {
376 | #ifdef _WIN32
{% endraw %}

```