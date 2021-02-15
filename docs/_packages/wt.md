---
name: "wt"
layout: package
next_package: njet
previous_package: cbtf-krell
languages: ['cpp']
---
## 3.3.7
2 / 2020 files match

 - [src/Wt/Dbo/backend/amalgamation/sqlite3.c](#srcwtdbobackendamalgamationsqlite3c)
 - [src/3rdparty/glew-1.10.0/src/glew.c](#src3rdpartyglew-1100srcglewc)

### src/Wt/Dbo/backend/amalgamation/sqlite3.c

```cpp

{% raw %}
1521 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
13749 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
20253 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
20254 |   return pVfs->xDlOpen(pVfs, zPath);
35895 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
35897 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
35902 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
35945 |   #define unixDlOpen  0
37328 |     unixDlOpen,           /* xDlOpen */                     \
43154 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
43161 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
43166 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
43176 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
43191 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
43213 |   #define winDlOpen  0
43434 |     winDlOpen,             /* xDlOpen */
43459 |     winDlOpen,             /* xDlOpen */
43484 |     winDlOpen,             /* xDlOpen */
43509 |     winDlOpen,             /* xDlOpen */
111727 |   handle = sqlite3OsDlOpen(pVfs, zFile);
111732 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
172701 | static void *rbuVfsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
172703 |   return pRealVfs->xDlOpen(pRealVfs, zPath);
172804 |     rbuVfsDlOpen,                 /* xDlOpen */
{% endraw %}

```
### src/3rdparty/glew-1.10.0/src/glew.c

```cpp

{% raw %}
80 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
107 |     image = dlopen("libRegal.dylib", RTLD_LAZY);
109 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```