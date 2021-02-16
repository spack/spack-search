---
name: "stinger"
layout: package
next_package: openfst
previous_package: multiverso
languages: ['c']
---
## master
2 / 862 files match

 - [lib/sqlite/src/sqlite3.c](#libsqlitesrcsqlite3c)
 - [lib/mongoose/src/mongoose.c](#libmongoosesrcmongoosec)

### lib/sqlite/src/sqlite3.c

```c

{% raw %}
31506 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### lib/mongoose/src/mongoose.c

```c

{% raw %}
1279 | static HANDLE dlopen(const char *dll_name, int flags) {
4776 |   if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
{% endraw %}

```