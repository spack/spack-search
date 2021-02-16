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
130 |   @param dlhandle       a handle to the shared object (returned by dlopen)
374 |   if (!(dlhandle= dlopen((const char *)dlpath, RTLD_NOW)))
{% endraw %}

```