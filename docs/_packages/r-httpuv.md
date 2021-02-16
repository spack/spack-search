---
name: "r-httpuv"
layout: package
next_package: r-igraph
previous_package: r-fs
languages: ['c']
---
## 1.3.5
6 / 254 files match, 4 filtered matches.

 - [src/libuv/src/win/dl.c](#srclibuvsrcwindlc)
 - [src/libuv/src/unix/dl.c](#srclibuvsrcunixdlc)
 - [src/libuv/include/uv.h](#srclibuvincludeuvh)
 - [src/libuv/test/test-dlerror.c](#srclibuvtesttest-dlerrorc)

### src/libuv/src/win/dl.c

```c

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### src/libuv/src/unix/dl.c

```c

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### src/libuv/include/uv.h

```c

{% raw %}
1849 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```
### src/libuv/test/test-dlerror.c

```c

{% raw %}
42 |   r = uv_dlopen(path, &lib);
{% endraw %}

```