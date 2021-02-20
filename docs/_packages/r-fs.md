---
name: "r-fs"
layout: package
next_package: r-httpuv
previous_package: r
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
24 | static int uv__dlerror(uv_lib_t* lib, const char* filename, DWORD errorno);
25 | 
26 | 
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
28 |   WCHAR filename_w[32768];
29 | 
{% endraw %}

```
### src/libuv/src/unix/darwin-proctitle.c

```c

{% raw %}
84 |   int err;
85 | 
86 |   err = -ENOENT;
87 |   application_services_handle = dlopen("/System/Library/Frameworks/"
88 |                                        "ApplicationServices.framework/"
89 |                                        "Versions/A/ApplicationServices",
90 |                                        RTLD_LAZY | RTLD_LOCAL);
91 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
92 |                                   "CoreFoundation.framework/"
93 |                                   "Versions/A/CoreFoundation",
{% endraw %}

```
### src/libuv/src/unix/fsevents.c

```c

{% raw %}
528 |    * per-event loop properties and have the dynamic linker keep track for us.
529 |    */
530 |   err = -ENOSYS;
531 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
532 |                                   "CoreFoundation.framework/"
533 |                                   "Versions/A/CoreFoundation",
535 |   if (core_foundation_handle == NULL)
536 |     goto out;
537 | 
538 |   core_services_handle = dlopen("/System/Library/Frameworks/"
539 |                                 "CoreServices.framework/"
540 |                                 "Versions/A/CoreServices",
{% endraw %}

```
### src/libuv/src/unix/dl.c

```c

{% raw %}
29 | static int uv__dlerror(uv_lib_t* lib);
30 | 
31 | 
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
33 |   dlerror(); /* Reset error status. */
34 |   lib->errmsg = NULL;
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
36 |   return lib->handle ? 0 : uv__dlerror(lib);
37 | }
{% endraw %}

```
### src/libuv/include/uv.h

```c

{% raw %}
1436 | 
1437 | UV_EXTERN void uv_disable_stdio_inheritance(void);
1438 | 
1439 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
1440 | UV_EXTERN void uv_dlclose(uv_lib_t* lib);
1441 | UV_EXTERN int uv_dlsym(uv_lib_t* lib, const char* name, void** ptr);
{% endraw %}

```