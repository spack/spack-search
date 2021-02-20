---
name: "py-uvloop"
layout: package
next_package: py-uwsgi
previous_package: py-tables
languages: ['c']
---
## 0.14.0
15 / 449 files match, 6 filtered matches.

 - [vendor/libuv/src/win/dl.c](#vendorlibuvsrcwindlc)
 - [vendor/libuv/src/unix/darwin-proctitle.c](#vendorlibuvsrcunixdarwin-proctitlec)
 - [vendor/libuv/src/unix/fsevents.c](#vendorlibuvsrcunixfseventsc)
 - [vendor/libuv/src/unix/dl.c](#vendorlibuvsrcunixdlc)
 - [vendor/libuv/include/uv.h](#vendorlibuvincludeuvh)
 - [vendor/libuv/test/test-dlerror.c](#vendorlibuvtesttest-dlerrorc)

### vendor/libuv/src/win/dl.c

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
### vendor/libuv/src/unix/darwin-proctitle.c

```c

{% raw %}
79 | #if !TARGET_OS_IPHONE
80 |   OSStatus (*pSetApplicationIsDaemon)(int);
81 | 
82 |   application_services_handle = dlopen("/System/Library/Frameworks/"
83 |                                        "ApplicationServices.framework/"
84 |                                        "Versions/A/ApplicationServices",
85 |                                        RTLD_LAZY | RTLD_LOCAL);
86 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
87 |                                   "CoreFoundation.framework/"
88 |                                   "Versions/A/CoreFoundation",
{% endraw %}

```
### vendor/libuv/src/unix/fsevents.c

```c

{% raw %}
533 |    * per-event loop properties and have the dynamic linker keep track for us.
534 |    */
535 |   err = UV_ENOSYS;
536 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
537 |                                   "CoreFoundation.framework/"
538 |                                   "Versions/A/CoreFoundation",
540 |   if (core_foundation_handle == NULL)
541 |     goto out;
542 | 
543 |   core_services_handle = dlopen("/System/Library/Frameworks/"
544 |                                 "CoreServices.framework/"
545 |                                 "Versions/A/CoreServices",
{% endraw %}

```
### vendor/libuv/src/unix/dl.c

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
### vendor/libuv/include/uv.h

```c

{% raw %}
1643 | 
1644 | UV_EXTERN void uv_disable_stdio_inheritance(void);
1645 | 
1646 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
1647 | UV_EXTERN void uv_dlclose(uv_lib_t* lib);
1648 | UV_EXTERN int uv_dlsym(uv_lib_t* lib, const char* name, void** ptr);
{% endraw %}

```
### vendor/libuv/test/test-dlerror.c

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