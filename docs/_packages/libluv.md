---
name: "libluv"
layout: package
next_package: libmesh
previous_package: libkcapi
languages: ['c']
---
## 1.36.0-0
14 / 484 files match, 7 filtered matches.

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
78 |   int err;
79 | 
80 |   err = UV_ENOENT;
81 |   application_services_handle = dlopen("/System/Library/Frameworks/"
82 |                                        "ApplicationServices.framework/"
83 |                                        "Versions/A/ApplicationServices",
84 |                                        RTLD_LAZY | RTLD_LOCAL);
85 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
86 |                                   "CoreFoundation.framework/"
87 |                                   "Versions/A/CoreFoundation",
{% endraw %}

```
### deps/libuv/src/unix/fsevents.c

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
1671 | 
1672 | UV_EXTERN void uv_disable_stdio_inheritance(void);
1673 | 
1674 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
1675 | UV_EXTERN void uv_dlclose(uv_lib_t* lib);
1676 | UV_EXTERN int uv_dlsym(uv_lib_t* lib, const char* name, void** ptr);
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
### deps/libuv/docs/code/plugin/main.c

```c

{% raw %}
20 |     uv_lib_t *lib = (uv_lib_t*) malloc(sizeof(uv_lib_t));
21 |     while (--argc) {
22 |         fprintf(stderr, "Loading %s\n", argv[argc]);
23 |         if (uv_dlopen(argv[argc], lib)) {
24 |             fprintf(stderr, "Error: %s\n", uv_dlerror(lib));
25 |             continue;
{% endraw %}

```