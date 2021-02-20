---
name: "r-rsqlite"
layout: package
next_package: raft
previous_package: r-rmpi
languages: ['c']
---
## 2.1.0
1 / 115 files match, 1 filtered matches.

 - [src/vendor/sqlite3/sqlite3.c](#srcvendorsqlite3sqlite3c)

### src/vendor/sqlite3/sqlite3.c

```c

{% raw %}
36976 | #include <dlfcn.h>
36977 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
36978 |   UNUSED_PARAMETER(NotUsed);
36979 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
36980 | }
36981 | 
{% endraw %}

```