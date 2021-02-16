---
name: "libuv"
layout: package
next_package: py-rpy2
previous_package: libsndfile
languages: ['c']
---
## 1.38.1
12 / 422 files match

 - [src/win/dl.c](#srcwindlc)
 - [src/unix/darwin-proctitle.c](#srcunixdarwin-proctitlec)
 - [src/unix/fsevents.c](#srcunixfseventsc)
 - [src/unix/dl.c](#srcunixdlc)
 - [include/uv.h](#includeuvh)
 - [test/test-dlerror.c](#testtest-dlerrorc)
 - [docs/code/plugin/main.c](#docscodepluginmainc)

### src/win/dl.c

```c

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### src/unix/darwin-proctitle.c

```c

{% raw %}
80 |   application_services_handle = dlopen("/System/Library/Frameworks/"
84 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### src/unix/fsevents.c

```c

{% raw %}
532 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
539 |   core_services_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### src/unix/dl.c

```c

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### include/uv.h

```c

{% raw %}
1682 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```
### test/test-dlerror.c

```c

{% raw %}
39 |   r = uv_dlopen(path, &lib);
{% endraw %}

```
### docs/code/plugin/main.c

```c

{% raw %}
23 |         if (uv_dlopen(argv[argc], lib)) {
{% endraw %}

```