---
name: "genometools"
layout: package
next_package: proj
previous_package: g2o
languages: ['cpp']
---
## 1.6.1
3 / 4299 files match

 - [src/external/sqlite-3.8.7.1/sqlite3.c](#srcexternalsqlite-3871sqlite3c)
 - [src/external/lua-5.1.5/src/luaconf.h](#srcexternallua-515srcluaconfh)
 - [src/external/lua-5.1.5/src/loadlib.c](#srcexternallua-515srcloadlibc)

### src/external/sqlite-3.8.7.1/sqlite3.c

```cpp

{% raw %}
1280 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
10313 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
16121 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
16122 |   return pVfs->xDlOpen(pVfs, zPath);
30839 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
30841 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
30846 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
30889 |   #define unixDlOpen  0
32263 |     unixDlOpen,           /* xDlOpen */                     \
37775 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
37782 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
37787 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
37797 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
37812 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
37834 |   #define winDlOpen  0
38017 |     winDlOpen,           /* xDlOpen */
38042 |     winDlOpen,           /* xDlOpen */
100427 |   handle = sqlite3OsDlOpen(pVfs, zFile);
100432 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
{% endraw %}

```
### src/external/lua-5.1.5/src/luaconf.h

```cpp

{% raw %}
37 | #define LUA_USE_DLOPEN		/* needs an extra library: -ldl */
689 | ** dyld, or Unix's dlopen). If your system is some kind of Unix, there
690 | ** is a good chance that it has dlopen, so LUA_DL_DLOPEN will work for
691 | ** it.  To use dlopen you also need to adapt the src/Makefile (probably
694 | ** also add -DLUA_USE_DLOPEN.)
699 | #if defined(LUA_USE_DLOPEN)
700 | #define LUA_DL_DLOPEN
{% endraw %}

```
### src/external/lua-5.1.5/src/loadlib.c

```cpp

{% raw %}
50 | #if defined(LUA_DL_DLOPEN)
68 |   void *lib = dlopen(path, RTLD_NOW);
{% endraw %}

```