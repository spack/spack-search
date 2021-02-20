---
name: "code-server"
layout: package
next_package: coin3d
previous_package: cmake
languages: ['c']
---
## 3.1.0
7 / 4773 files match, 1 filtered matches.

 - [lib/vscode/node_modules/vscode-sqlite3/build/Release/obj/gen/sqlite-autoconf-3280000/sqlite3.c](#libvscodenode_modulesvscode-sqlite3buildreleaseobjgensqlite-autoconf-3280000sqlite3c)

### lib/vscode/node_modules/vscode-sqlite3/build/Release/obj/gen/sqlite-autoconf-3280000/sqlite3.c

```c

{% raw %}
38874 | #include <dlfcn.h>
38875 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
38876 |   UNUSED_PARAMETER(NotUsed);
38877 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
38878 | }
38879 | 
{% endraw %}

```