---
name: "stinger"
layout: package
next_package: swftools
previous_package: stc
languages: ['c']
---
## master
2 / 862 files match, 2 filtered matches.

 - [lib/sqlite/src/sqlite3.c](#libsqlitesrcsqlite3c)
 - [lib/mongoose/src/mongoose.c](#libmongoosesrcmongoosec)

### lib/sqlite/src/sqlite3.c

```c

{% raw %}
31503 | #include <dlfcn.h>
31504 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
31505 |   UNUSED_PARAMETER(NotUsed);
31506 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
31507 | }
31508 | 
{% endraw %}

```
### lib/mongoose/src/mongoose.c

```c

{% raw %}
1276 |   return (long)_beginthread((void (__cdecl *)(void *)) f, 0, p) == -1L ? -1 : 0;
1277 | }
1278 | 
1279 | static HANDLE dlopen(const char *dll_name, int flags) {
1280 |   wchar_t wbuf[PATH_MAX];
1281 |   (void) flags;
4773 |   void  *dll_handle;
4774 |   struct ssl_func *fp;
4775 | 
4776 |   if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
4777 |     cry(fc(ctx), "%s: cannot load %s", __func__, dll_name);
4778 |     return 0;
{% endraw %}

```