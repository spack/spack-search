---
name: "stinger"
layout: package
next_package: openfst
previous_package: multiverso
languages: ['cpp']
---
## master
2 / 862 files match

 - [lib/sqlite/src/sqlite3.c](#libsqlitesrcsqlite3c)
 - [lib/mongoose/src/mongoose.c](#libmongoosesrcmongoosec)

### lib/sqlite/src/sqlite3.c

```cpp

{% raw %}
1387 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
10758 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
16688 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
16689 |   return pVfs->xDlOpen(pVfs, zPath);
31504 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
31506 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
31511 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
31554 |   #define unixDlOpen  0
32937 |     unixDlOpen,           /* xDlOpen */                     \
38510 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
38517 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
38522 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
38532 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
38547 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
38569 |   #define winDlOpen  0
38768 |     winDlOpen,           /* xDlOpen */
38793 |     winDlOpen,           /* xDlOpen */
102819 |   handle = sqlite3OsDlOpen(pVfs, zFile);
102824 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
{% endraw %}

```
### lib/mongoose/src/mongoose.c

```cpp

{% raw %}
1279 | static HANDLE dlopen(const char *dll_name, int flags) {
4776 |   if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
{% endraw %}

```