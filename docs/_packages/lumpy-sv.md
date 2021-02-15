---
name: "lumpy-sv"
layout: package
next_package: r-rcmdcheck
previous_package: kea
languages: ['cpp']
---
## 0.2.13
1 / 275 files match

 - [src/utils/sqlite3/sqlite3.c](#srcutilssqlite3sqlite3c)

### src/utils/sqlite3/sqlite3.c

```cpp

{% raw %}
1623 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
9595 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
14995 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
14996 |   return pVfs->xDlOpen(pVfs, zPath);
28161 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
28163 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
28168 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
28211 |   #define unixDlOpen  0
29585 |     unixDlOpen,           /* xDlOpen */                     \
33985 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
34020 |   #define winDlOpen  0
34202 |     winDlOpen,           /* xDlOpen */
90835 |   handle = sqlite3OsDlOpen(pVfs, zFile);
{% endraw %}

```