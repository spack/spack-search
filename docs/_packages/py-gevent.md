---
name: "py-gevent"
layout: package
next_package: gtkmm
previous_package: iproute2
languages: ['c']
---
## 1.3a2
13 / 1152 files match

 - [deps/libuv/src/win/dl.c](#depslibuvsrcwindlc)
 - [deps/libuv/src/unix/darwin-proctitle.c](#depslibuvsrcunixdarwin-proctitlec)
 - [deps/libuv/src/unix/fsevents.c](#depslibuvsrcunixfseventsc)
 - [deps/libuv/src/unix/dl.c](#depslibuvsrcunixdlc)
 - [deps/libuv/include/uv.h](#depslibuvincludeuvh)
 - [deps/libuv/test/test-dlerror.c](#depslibuvtesttest-dlerrorc)

### deps/libuv/src/win/dl.c

```c

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### deps/libuv/src/unix/darwin-proctitle.c

```c

{% raw %}
87 |   application_services_handle = dlopen("/System/Library/Frameworks/"
91 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### deps/libuv/src/unix/fsevents.c

```c

{% raw %}
531 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
538 |   core_services_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### deps/libuv/src/unix/dl.c

```c

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### deps/libuv/include/uv.h

```c

{% raw %}
1439 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```
### deps/libuv/test/test-dlerror.c

```c

{% raw %}
39 |   r = uv_dlopen(path, &lib);
{% endraw %}

```