---
name: "grafana"
layout: package
next_package: py-py2cairo
previous_package: lzop
languages: ['cpp']
---
## 6.7.3
1 / 7110 files match

 - [vendor/github.com/mattn/go-sqlite3/sqlite3-binding.c](#vendorgithubcommattngo-sqlite3sqlite3-bindingc)

### vendor/github.com/mattn/go-sqlite3/sqlite3-binding.c

```cpp

{% raw %}
2403 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
16032 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
22486 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
22487 |   return pVfs->xDlOpen(pVfs, zPath);
38940 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
38942 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
38947 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
38990 |   #define unixDlOpen  0
40373 |     unixDlOpen,           /* xDlOpen */                     \
46365 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
46372 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46377 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46387 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46402 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
46424 |   #define winDlOpen  0
46642 |     winDlOpen,             /* xDlOpen */
46667 |     winDlOpen,             /* xDlOpen */
46692 |     winDlOpen,             /* xDlOpen */
46717 |     winDlOpen,             /* xDlOpen */
46852 | static void *memdbDlOpen(sqlite3_vfs*, const char *zFilename);
46873 |   memdbDlOpen,                 /* xDlOpen */
47176 | static void *memdbDlOpen(sqlite3_vfs *pVfs, const char *zPath){
47177 |   return ORIGVFS(pVfs)->xDlOpen(ORIGVFS(pVfs), zPath);
120723 |   handle = sqlite3OsDlOpen(pVfs, zFile);
120728 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
194589 | static void *rbuVfsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
194591 |   return pRealVfs->xDlOpen(pRealVfs, zPath);
194692 |     rbuVfsDlOpen,                 /* xDlOpen */
{% endraw %}

```