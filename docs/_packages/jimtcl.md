---
name: "jimtcl"
layout: package
next_package: keepalived
previous_package: py-mypy
languages: ['cpp']
---
## 0.77
6 / 213 files match

 - [auto.def](#autodef)
 - [jim-win32compat.h](#jim-win32compath)
 - [jim-win32compat.c](#jim-win32compatc)
 - [jim-load.c](#jim-loadc)
 - [sqlite3/sqlite3.c](#sqlite3sqlite3c)
 - [autosetup/jimsh0.c](#autosetupjimsh0c)

### auto.def

```

{% raw %}
129 |         # We provide our own implementation of dlopen for mingw32
130 |         define-feature dlopen-compat
291 |     load     { check {[have-feature dlopen-compat] || [cc-check-function-in-lib dlopen dl]} libdep lib_dlopen }
{% endraw %}

```
### jim-win32compat.h

```cpp

{% raw %}
12 | #define HAVE_DLOPEN
13 | void *dlopen(const char *path, int mode);
{% endraw %}

```
### jim-win32compat.c

```cpp

{% raw %}
10 | #if defined(HAVE_DLOPEN_COMPAT)
11 | void *dlopen(const char *path, int mode)
{% endraw %}

```
### jim-load.c

```cpp

{% raw %}
9 | #if defined(HAVE_DLOPEN) || defined(HAVE_DLOPEN_COMPAT)
31 |     void *handle = dlopen(pathName, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### sqlite3/sqlite3.c

```cpp

{% raw %}
1488 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
13566 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
19935 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
19936 |   return pVfs->xDlOpen(pVfs, zPath);
35414 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
35416 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
35421 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
35464 |   #define unixDlOpen  0
36847 |     unixDlOpen,           /* xDlOpen */                     \
42667 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
42674 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
42679 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
42689 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
42704 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
42726 |   #define winDlOpen  0
42947 |     winDlOpen,             /* xDlOpen */
42972 |     winDlOpen,             /* xDlOpen */
42997 |     winDlOpen,             /* xDlOpen */
43022 |     winDlOpen,             /* xDlOpen */
109860 |   handle = sqlite3OsDlOpen(pVfs, zFile);
109865 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
169474 | static void *rbuVfsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
169476 |   return pRealVfs->xDlOpen(pRealVfs, zPath);
169577 |     rbuVfsDlOpen,                 /* xDlOpen */
{% endraw %}

```
### autosetup/jimsh0.c

```cpp

{% raw %}
61 | #define HAVE_DLOPEN
62 | void *dlopen(const char *path, int mode);
21832 | #if defined(HAVE_DLOPEN_COMPAT)
21833 | void *dlopen(const char *path, int mode)
{% endraw %}

```