---
name: "grafana"
layout: package
next_package: graphicsmagick
previous_package: grads
languages: ['c']
---
## 6.7.3
1 / 7110 files match, 1 filtered matches.

 - [vendor/github.com/mattn/go-sqlite3/sqlite3-binding.c](#vendorgithubcommattngo-sqlite3sqlite3-bindingc)

### vendor/github.com/mattn/go-sqlite3/sqlite3-binding.c

```c

{% raw %}
38939 | #include <dlfcn.h>
38940 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
38941 |   UNUSED_PARAMETER(NotUsed);
38942 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
38943 | }
38944 | 
{% endraw %}

```