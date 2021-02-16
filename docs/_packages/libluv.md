---
name: "libluv"
layout: package
next_package: lcms
previous_package: swipl
languages: ['c']
---
## 1.36.0-0
14 / 484 files match

 - [deps/libuv/src/win/dl.c](#depslibuvsrcwindlc)
 - [deps/libuv/src/unix/darwin-proctitle.c](#depslibuvsrcunixdarwin-proctitlec)
 - [deps/libuv/src/unix/fsevents.c](#depslibuvsrcunixfseventsc)
 - [deps/libuv/src/unix/dl.c](#depslibuvsrcunixdlc)
 - [deps/libuv/include/uv.h](#depslibuvincludeuvh)
 - [deps/libuv/test/test-dlerror.c](#depslibuvtesttest-dlerrorc)
 - [deps/libuv/docs/code/plugin/main.c](#depslibuvdocscodepluginmainc)

### deps/libuv/src/win/dl.c

```c

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### deps/libuv/src/unix/darwin-proctitle.c

```c

{% raw %}
81 |   application_services_handle = dlopen("/System/Library/Frameworks/"
85 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### deps/libuv/src/unix/fsevents.c

```c

{% raw %}
536 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
543 |   core_services_handle = dlopen("/System/Library/Frameworks/"
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
1674 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```
### deps/libuv/test/test-dlerror.c

```c

{% raw %}
39 |   r = uv_dlopen(path, &lib);
{% endraw %}

```
### deps/libuv/docs/code/plugin/main.c

```c

{% raw %}
23 |         if (uv_dlopen(argv[argc], lib)) {
{% endraw %}

```