---
name: "genometools"
layout: package
next_package: geopm
previous_package: gdb
languages: ['c']
---
## 1.6.1
3 / 4299 files match, 2 filtered matches.

 - [src/external/sqlite-3.8.7.1/sqlite3.c](#srcexternalsqlite-3871sqlite3c)
 - [src/external/lua-5.1.5/src/loadlib.c](#srcexternallua-515srcloadlibc)

### src/external/sqlite-3.8.7.1/sqlite3.c

```c

{% raw %}
30838 | #include <dlfcn.h>
30839 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
30840 |   UNUSED_PARAMETER(NotUsed);
30841 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
30842 | }
30843 | 
{% endraw %}

```
### src/external/lua-5.1.5/src/loadlib.c

```c

{% raw %}
65 | 
66 | 
67 | static void *ll_load (lua_State *L, const char *path) {
68 |   void *lib = dlopen(path, RTLD_NOW);
69 |   if (lib == NULL) lua_pushstring(L, dlerror());
70 |   return lib;
{% endraw %}

```