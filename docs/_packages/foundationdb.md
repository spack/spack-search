---
name: "foundationdb"
layout: package
next_package: ufo-core
previous_package: pax-utils
languages: ['cpp']
---
## 6.2.24
8 / 1350 files match

 - [FDBLibTLS/plugin-test.cpp](#fdblibtlsplugin-testcpp)
 - [documentation/sphinx/source/api-c.rst](#documentationsphinxsourceapi-crst)
 - [documentation/sphinx/source/client-testing.rst](#documentationsphinxsourceclient-testingrst)
 - [flow/SignalSafeUnwind.h](#flowsignalsafeunwindh)
 - [flow/Platform.cpp](#flowplatformcpp)
 - [flow/stacktrace.amalgamation.cpp](#flowstacktraceamalgamationcpp)
 - [bindings/c/fdb_c.cpp](#bindingscfdb_ccpp)
 - [fdbserver/sqlite/sqlite3.amalgamation.c](#fdbserversqlitesqlite3amalgamationc)

### FDBLibTLS/plugin-test.cpp

```

{% raw %}
1150 | 	pluginSO = dlopen(argv[1], RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### documentation/sphinx/source/api-c.rst

```

{% raw %}
125 | When linking against ``libfdb_c.so``, you must also link against ``libm``, ``libpthread`` and ``librt``. These dependencies will be resolved by the dynamic linker when using this API via ``dlopen()`` or an FFI.
150 |    .. note:: This is actually implemented as a macro. If you are accessing this API via ``dlopen()`` or an FFI, you will need to use :func:`fdb_select_api_version_impl()`.
156 |    This is the actual entry point called by the :func:`fdb_select_api_version` macro. It should never be called directly from C, but if you are accessing this API via ``dlopen()`` or an FFI, you will need to use it. ``fdb_select_api_version(v)`` is equivalent to ``fdb_select_api_version_impl(v, FDB_API_VERSION)``.
{% endraw %}

```
### documentation/sphinx/source/client-testing.rst

```

{% raw %}
62 | dynamically. This is done through ``dlopen`` (on Unix like operating systems) or ``LoadLibrary`` (on Windows).
{% endraw %}

```
### flow/SignalSafeUnwind.h

```cpp

{% raw %}
35 | // (no further calls to dlopen() or dlclose() are permitted).
{% endraw %}

```
### flow/Platform.cpp

```

{% raw %}
2661 | 	dlobj = dlopen( lib_path, RTLD_NOLOAD | RTLD_LAZY );
2677 | 	dlobj = dlopen( lib_path, RTLD_LAZY | RTLD_LOCAL );
{% endraw %}

```
### flow/stacktrace.amalgamation.cpp

```

{% raw %}
2554 |       // "fake" dlopen()ed vdso library, the loader relocates some (but
{% endraw %}

```
### bindings/c/fdb_c.cpp

```

{% raw %}
705 | 	//OS X ld doesn't support -z nodelete, so we dlopen to increment the reference count of this module
711 | 	dlopen(info.dli_fname, RTLD_NOLOAD | RTLD_NODELETE);
{% endraw %}

```
### fdbserver/sqlite/sqlite3.amalgamation.c

```cpp

{% raw %}
2452 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
7622 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
7623 |   return pVfs->xDlOpen(pVfs, zPath);
16495 | static void *os2DlOpen(sqlite3_vfs *pVfs, const char *zFilename){
16506 | ** os2Dlopen returns zero if DosLoadModule is not successful.
16529 |   #define os2DlOpen 0
16697 |     os2DlOpen,         /* xDlOpen */
22132 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
22134 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
22139 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
22182 |   #define unixDlOpen  0
23548 |     unixDlOpen,           /* xDlOpen */                     \
26362 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
26403 |   #define winDlOpen  0
26578 |     winDlOpen,           /* xDlOpen */
71848 |   handle = sqlite3OsDlOpen(pVfs, zFile);
{% endraw %}

```