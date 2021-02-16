---
name: "py-uvloop"
layout: package
next_package: ocl-icd
previous_package: environment-modules
languages: ['c']
---
## 0.14.0
15 / 449 files match

 - [vendor/libuv/src/win/dl.c](#vendorlibuvsrcwindlc)
 - [vendor/libuv/src/unix/darwin-proctitle.c](#vendorlibuvsrcunixdarwin-proctitlec)
 - [vendor/libuv/src/unix/fsevents.c](#vendorlibuvsrcunixfseventsc)
 - [vendor/libuv/src/unix/dl.c](#vendorlibuvsrcunixdlc)
 - [vendor/libuv/include/uv.h](#vendorlibuvincludeuvh)
 - [vendor/libuv/test/test-dlerror.c](#vendorlibuvtesttest-dlerrorc)

### vendor/libuv/src/win/dl.c

```c

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### vendor/libuv/src/unix/darwin-proctitle.c

```c

{% raw %}
82 |   application_services_handle = dlopen("/System/Library/Frameworks/"
86 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### vendor/libuv/src/unix/fsevents.c

```c

{% raw %}
536 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
543 |   core_services_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### vendor/libuv/src/unix/dl.c

```c

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### vendor/libuv/include/uv.h

```c

{% raw %}
1646 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```
### vendor/libuv/test/test-dlerror.c

```c

{% raw %}
39 |   r = uv_dlopen(path, &lib);
{% endraw %}

```