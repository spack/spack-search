---
name: "lumpy-sv"
layout: package
next_package: lvm2
previous_package: lua-luajit
languages: ['c']
---
## 0.2.13
1 / 275 files match, 1 filtered matches.

 - [src/utils/sqlite3/sqlite3.c](#srcutilssqlite3sqlite3c)

### src/utils/sqlite3/sqlite3.c

```c

{% raw %}
28160 | #include <dlfcn.h>
28161 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
28162 |   UNUSED_PARAMETER(NotUsed);
28163 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
28164 | }
28165 | 
{% endraw %}

```