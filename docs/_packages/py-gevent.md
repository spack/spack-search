---
name: "py-gevent"
layout: package
next_package: py-grpcio
previous_package: py-fenics-dolfinx
languages: ['c']
---
## 1.3a2
13 / 1152 files match, 6 filtered matches.

 - [deps/libuv/src/win/dl.c](#depslibuvsrcwindlc)
 - [deps/libuv/src/unix/darwin-proctitle.c](#depslibuvsrcunixdarwin-proctitlec)
 - [deps/libuv/src/unix/fsevents.c](#depslibuvsrcunixfseventsc)
 - [deps/libuv/src/unix/dl.c](#depslibuvsrcunixdlc)
 - [deps/libuv/include/uv.h](#depslibuvincludeuvh)
 - [deps/libuv/test/test-dlerror.c](#depslibuvtesttest-dlerrorc)

### deps/libuv/src/win/dl.c

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
### deps/libuv/src/unix/darwin-proctitle.c

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
### deps/libuv/src/unix/fsevents.c

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
### deps/libuv/src/unix/dl.c

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
### deps/libuv/include/uv.h

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
### deps/libuv/test/test-dlerror.c

```c

{% raw %}
36 |   ASSERT(msg != NULL);
37 |   ASSERT(strstr(msg, dlerror_no_error) != NULL);
38 | 
39 |   r = uv_dlopen(path, &lib);
40 |   ASSERT(r == -1);
41 | 
{% endraw %}

```