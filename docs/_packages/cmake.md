---
name: "cmake"
layout: package
next_package: code-server
previous_package: clfft
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
24 | static int uv__dlerror(uv_lib_t* lib, const char* filename, DWORD errorno);
25 | 
26 | 
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
28 |   WCHAR filename_w[32768];
29 | 
{% endraw %}

```
### Utilities/cmlibuv/src/unix/darwin-proctitle.c

```c

{% raw %}
77 |   int err;
78 | 
79 |   err = UV_ENOENT;
80 |   application_services_handle = dlopen("/System/Library/Frameworks/"
81 |                                        "ApplicationServices.framework/"
82 |                                        "Versions/A/ApplicationServices",
83 |                                        RTLD_LAZY | RTLD_LOCAL);
84 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
85 |                                   "CoreFoundation.framework/"
86 |                                   "Versions/A/CoreFoundation",
{% endraw %}

```
### Utilities/cmlibuv/src/unix/fsevents.c

```c

{% raw %}
529 |    * per-event loop properties and have the dynamic linker keep track for us.
530 |    */
531 |   err = UV_ENOSYS;
532 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
533 |                                   "CoreFoundation.framework/"
534 |                                   "Versions/A/CoreFoundation",
536 |   if (core_foundation_handle == NULL)
537 |     goto out;
538 | 
539 |   core_services_handle = dlopen("/System/Library/Frameworks/"
540 |                                 "CoreServices.framework/"
541 |                                 "Versions/A/CoreServices",
{% endraw %}

```
### Utilities/cmlibuv/src/unix/dl.c

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
### Utilities/cmlibuv/include/uv.h

```c

{% raw %}
1697 | 
1698 | UV_EXTERN void uv_disable_stdio_inheritance(void);
1699 | 
1700 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
1701 | UV_EXTERN void uv_dlclose(uv_lib_t* lib);
1702 | UV_EXTERN int uv_dlsym(uv_lib_t* lib, const char* name, void** ptr);
{% endraw %}

```