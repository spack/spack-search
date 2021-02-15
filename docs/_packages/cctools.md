---
name: "cctools"
layout: package
next_package: bazel
previous_package: libx11
languages: ['cpp']
---
## 7.1.0
2 / 1270 files match

 - [dttools/src/hdfs_library.c](#dttoolssrchdfs_libraryc)
 - [chirp/src/sqlite3.c](#chirpsrcsqlite3c)

### dttools/src/hdfs_library.c

```cpp

{% raw %}
121 | 		*handle = dlopen(path, RTLD_LAZY);
126 | 			debug(D_HDFS, "dlopen failed: %s", dlerror());
{% endraw %}

```
### chirp/src/sqlite3.c

```cpp

{% raw %}
1338 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
10562 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
16431 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
16432 |   return pVfs->xDlOpen(pVfs, zPath);
31210 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
31212 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
31217 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
31260 |   #define unixDlOpen  0
32634 |     unixDlOpen,           /* xDlOpen */                     \
38153 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
38160 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
38165 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
38175 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
38190 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
38212 |   #define winDlOpen  0
38395 |     winDlOpen,           /* xDlOpen */
38420 |     winDlOpen,           /* xDlOpen */
101715 |   handle = sqlite3OsDlOpen(pVfs, zFile);
101720 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
{% endraw %}

```