---
name: "saws"
layout: package
next_package: tengine
previous_package: libdaemon
languages: ['c']
---
## 0.1.0
1 / 39 files match, 1 filtered matches.

 - [src/mongoose.c](#srcmongoosec)

### src/mongoose.c

```c

{% raw %}
1241 | static HANDLE dlopen(const char *dll_name, int flags) {
4502 |   if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
{% endraw %}

```