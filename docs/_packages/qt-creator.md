---
name: "qt-creator"
layout: package
next_package: r-rhtslib
previous_package: geos
languages: ['cpp']
---
## 4.8.0
3 / 13797 files match

 - [src/libs/3rdparty/botan/src/lib/utils/dyn_load/dyn_load.cpp](#srclibs3rdpartybotansrclibutilsdyn_loaddyn_loadcpp)
 - [src/libs/3rdparty/sqlite/sqlite3.c](#srclibs3rdpartysqlitesqlite3c)
 - [src/shared/qbs/tests/auto/blackbox/testdata/loadablemodule/main.cpp](#srcsharedqbstestsautoblackboxtestdataloadablemodulemaincpp)

### src/libs/3rdparty/botan/src/lib/utils/dyn_load/dyn_load.cpp

```

{% raw %}
36 |    m_lib = ::dlopen(m_lib_name.c_str(), RTLD_LAZY);
{% endraw %}

```
### src/libs/3rdparty/sqlite/sqlite3.c

```cpp

{% raw %}
2320 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
14803 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
20935 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
20936 |   return pVfs->xDlOpen(pVfs, zPath);
36538 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
36540 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
36545 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
36588 |   #define unixDlOpen  0
37971 |     unixDlOpen,           /* xDlOpen */                     \
43866 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
43873 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
43878 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
43888 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
43903 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
43925 |   #define winDlOpen  0
44143 |     winDlOpen,             /* xDlOpen */
44168 |     winDlOpen,             /* xDlOpen */
44193 |     winDlOpen,             /* xDlOpen */
44218 |     winDlOpen,             /* xDlOpen */
113339 |   handle = sqlite3OsDlOpen(pVfs, zFile);
113344 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
175524 | static void *rbuVfsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
175526 |   return pRealVfs->xDlOpen(pRealVfs, zPath);
175627 |     rbuVfsDlOpen,                 /* xDlOpen */
{% endraw %}

```
### src/shared/qbs/tests/auto/blackbox/testdata/loadablemodule/main.cpp

```

{% raw %}
57 | #define dlopen(path, mode) LoadLibraryA(path)
73 |     auto lib = dlopen(PREFIX "CoolPlugIn" SUFFIX, RTLD_LAZY);
{% endraw %}

```