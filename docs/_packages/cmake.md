---
name: "cmake"
layout: package
next_package: cntk
previous_package: charmpp
languages: ['c']
---
## 3.18.3
22 / 16369 files match, 5 filtered matches.

 - [Utilities/cmlibuv/src/win/dl.c](#utilitiescmlibuvsrcwindlc)
 - [Utilities/cmlibuv/src/unix/darwin-proctitle.c](#utilitiescmlibuvsrcunixdarwin-proctitlec)
 - [Utilities/cmlibuv/src/unix/fsevents.c](#utilitiescmlibuvsrcunixfseventsc)
 - [Utilities/cmlibuv/src/unix/dl.c](#utilitiescmlibuvsrcunixdlc)
 - [Utilities/cmlibuv/include/uv.h](#utilitiescmlibuvincludeuvh)

### Utilities/cmlibuv/src/win/dl.c

```c

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### Utilities/cmlibuv/src/unix/darwin-proctitle.c

```c

{% raw %}
80 |   application_services_handle = dlopen("/System/Library/Frameworks/"
84 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### Utilities/cmlibuv/src/unix/fsevents.c

```c

{% raw %}
532 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
539 |   core_services_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### Utilities/cmlibuv/src/unix/dl.c

```c

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### Utilities/cmlibuv/include/uv.h

```c

{% raw %}
1700 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```