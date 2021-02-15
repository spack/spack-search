---
name: "xhmm"
layout: package
next_package: draco
previous_package: pslib
languages: ['cpp']
---
## 20160104
1 / 158 files match

 - [sources/hmm++/sources/lib/sqlite3.c](#sourceshmm++sourceslibsqlite3c)

### sources/hmm++/sources/lib/sqlite3.c

```cpp

{% raw %}
1480 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
9160 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
14408 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
14409 |   return pVfs->xDlOpen(pVfs, zPath);
24017 | static void *os2DlOpen(sqlite3_vfs *pVfs, const char *zFilename){
24027 | ** os2Dlopen returns zero if DosLoadModule is not successful.
24050 |   #define os2DlOpen 0
24237 |     os2DlOpen,         /* xDlOpen */
29725 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
29727 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
29732 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
29775 |   #define unixDlOpen  0
31142 |     unixDlOpen,           /* xDlOpen */                     \
34022 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
34063 |   #define winDlOpen  0
34238 |     winDlOpen,           /* xDlOpen */
87846 |   handle = sqlite3OsDlOpen(pVfs, zFile);
{% endraw %}

```