---
name: "cistem"
layout: package
next_package: clamav
previous_package: charmpp
languages: ['c']
---
## 1.0.0-beta
3 / 344 files match, 1 filtered matches.

 - [src/core/sqlite/sqlite3.c](#srccoresqlitesqlite3c)

### src/core/sqlite/sqlite3.c

```c

{% raw %}
36532 | #include <dlfcn.h>
36533 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
36534 |   UNUSED_PARAMETER(NotUsed);
36535 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
36536 | }
36537 | 
{% endraw %}

```