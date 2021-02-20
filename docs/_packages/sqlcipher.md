---
name: "sqlcipher"
layout: package
next_package: sqlite
previous_package: spot
languages: ['c']
---
## 4.2.0
6 / 1840 files match, 1 filtered matches.

 - [src/os_unix.c](#srcos_unixc)

### src/os_unix.c

```c

{% raw %}
6364 | #include <dlfcn.h>
6365 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
6366 |   UNUSED_PARAMETER(NotUsed);
6367 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
6368 | }
6369 | 
{% endraw %}

```