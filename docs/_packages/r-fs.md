---
name: "r-fs"
layout: package
next_package: xfsprogs
previous_package: rocprofiler-dev
languages: ['c']
---
## 1.3.1
11 / 242 files match, 5 filtered matches.

 - [src/libuv/src/win/dl.c](#srclibuvsrcwindlc)
 - [src/libuv/src/unix/darwin-proctitle.c](#srclibuvsrcunixdarwin-proctitlec)
 - [src/libuv/src/unix/fsevents.c](#srclibuvsrcunixfseventsc)
 - [src/libuv/src/unix/dl.c](#srclibuvsrcunixdlc)
 - [src/libuv/include/uv.h](#srclibuvincludeuvh)

### src/libuv/src/win/dl.c

```c

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### src/libuv/src/unix/darwin-proctitle.c

```c

{% raw %}
87 |   application_services_handle = dlopen("/System/Library/Frameworks/"
91 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### src/libuv/src/unix/fsevents.c

```c

{% raw %}
531 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
538 |   core_services_handle = dlopen("/System/Library/Frameworks/"
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
1439 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```