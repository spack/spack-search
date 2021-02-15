---
name: "r-rsqlite"
layout: package
next_package: procps-ng
previous_package: libmad
languages: ['cpp']
---
## 2.1.0
1 / 115 files match

 - [src/vendor/sqlite3/sqlite3.c](#srcvendorsqlite3sqlite3c)

### src/vendor/sqlite3/sqlite3.c

```cpp

{% raw %}
2330 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
14908 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
21053 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
21054 |   return pVfs->xDlOpen(pVfs, zPath);
36977 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
36979 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
36984 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
37027 |   #define unixDlOpen  0
38410 |     unixDlOpen,           /* xDlOpen */                     \
44354 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
44361 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
44366 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
44376 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
44391 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
44413 |   #define winDlOpen  0
44631 |     winDlOpen,             /* xDlOpen */
44656 |     winDlOpen,             /* xDlOpen */
44681 |     winDlOpen,             /* xDlOpen */
44706 |     winDlOpen,             /* xDlOpen */
114332 |   handle = sqlite3OsDlOpen(pVfs, zFile);
114339 |     if( bExists )  handle = sqlite3OsDlOpen(pVfs, zAltFile);
177405 | static void *rbuVfsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
177407 |   return pRealVfs->xDlOpen(pRealVfs, zPath);
177508 |     rbuVfsDlOpen,                 /* xDlOpen */
{% endraw %}

```