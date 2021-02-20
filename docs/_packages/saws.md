---
name: "saws"
layout: package
next_package: sblim-sfcc
previous_package: sandbox
languages: ['c']
---
## 0.1.0
1 / 39 files match, 1 filtered matches.

 - [src/mongoose.c](#srcmongoosec)

### src/mongoose.c

```c

{% raw %}
1238 |   return _beginthread((void (__cdecl *)(void *)) f, 0, p) == -1L ? -1 : 0;
1239 | }
1240 | 
1241 | static HANDLE dlopen(const char *dll_name, int flags) {
1242 |   wchar_t wbuf[PATH_MAX];
1243 |   flags = 0; // Unused
4499 |   void  *dll_handle;
4500 |   struct ssl_func *fp;
4501 | 
4502 |   if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
4503 |     cry(fc(ctx), "%s: cannot load %s", __func__, dll_name);
4504 |     return 0;
{% endraw %}

```