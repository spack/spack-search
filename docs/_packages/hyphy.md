---
name: "hyphy"
layout: package
next_package: ibm-databroker
previous_package: hydra
languages: ['c']
---
## 2.3.14
4 / 936 files match, 1 filtered matches.

 - [contrib/SQLite-3.8.2/sqlite3.c](#contribsqlite-382sqlite3c)

### contrib/SQLite-3.8.2/sqlite3.c

```c

{% raw %}
29259 | #include <dlfcn.h>
29260 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
29261 |   UNUSED_PARAMETER(NotUsed);
29262 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
29263 | }
29264 | 
{% endraw %}

```