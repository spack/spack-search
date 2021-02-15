---
name: "r-httpuv"
layout: package
next_package: py-matplotlib
previous_package: ncbi-toolkit
languages: ['cpp']
---
## 1.3.5
6 / 254 files match

 - [src/libuv/src/win/dl.c](#srclibuvsrcwindlc)
 - [src/libuv/src/unix/dl.c](#srclibuvsrcunixdlc)
 - [src/libuv/include/uv.h](#srclibuvincludeuvh)
 - [src/libuv/include/uv-private/uv-win.h](#srclibuvincludeuv-privateuv-winh)
 - [src/libuv/include/uv-private/uv-unix.h](#srclibuvincludeuv-privateuv-unixh)
 - [src/libuv/test/test-dlerror.c](#srclibuvtesttest-dlerrorc)

### src/libuv/src/win/dl.c

```cpp

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### src/libuv/src/unix/dl.c

```cpp

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### src/libuv/include/uv.h

```cpp

{% raw %}
1849 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
1863 |  * Returns the last uv_dlopen() or uv_dlsym() error message.
{% endraw %}

```
### src/libuv/include/uv-private/uv-win.h

```cpp

{% raw %}
266 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### src/libuv/include/uv-private/uv-unix.h

```cpp

{% raw %}
155 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### src/libuv/test/test-dlerror.c

```cpp

{% raw %}
42 |   r = uv_dlopen(path, &lib);
{% endraw %}

```