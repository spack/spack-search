---
name: "qt-creator"
layout: package
next_package: quantum-espresso
previous_package: qt
languages: ['c']
---
## 4.8.0
3 / 13797 files match, 1 filtered matches.

 - [src/libs/3rdparty/sqlite/sqlite3.c](#srclibs3rdpartysqlitesqlite3c)

### src/libs/3rdparty/sqlite/sqlite3.c

```c

{% raw %}
36537 | #include <dlfcn.h>
36538 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
36539 |   UNUSED_PARAMETER(NotUsed);
36540 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
36541 | }
36542 | 
{% endraw %}

```