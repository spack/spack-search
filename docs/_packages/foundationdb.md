---
name: "foundationdb"
layout: package
next_package: freebayes
previous_package: foam-extend
languages: ['c']
---
## 6.2.24
8 / 1350 files match, 1 filtered matches.

 - [fdbserver/sqlite/sqlite3.amalgamation.c](#fdbserversqlitesqlite3amalgamationc)

### fdbserver/sqlite/sqlite3.amalgamation.c

```c

{% raw %}
22131 | #include <dlfcn.h>
22132 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
22133 |   UNUSED_PARAMETER(NotUsed);
22134 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
22135 | }
22136 | 
{% endraw %}

```