---
name: "libuv"
layout: package
next_package: libverto
previous_package: libtool
languages: ['c']
---
## 1.38.1
12 / 422 files match, 7 filtered matches.

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
24 | static int uv__dlerror(uv_lib_t* lib, const char* filename, DWORD errorno);
25 | 
26 | 
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
28 |   WCHAR filename_w[32768];
29 | 
{% endraw %}

```
### src/unix/darwin-proctitle.c

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
### src/unix/fsevents.c

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
### src/unix/dl.c

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
### include/uv.h

```c

{% raw %}
1679 | 
1680 | UV_EXTERN void uv_disable_stdio_inheritance(void);
1681 | 
1682 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
1683 | UV_EXTERN void uv_dlclose(uv_lib_t* lib);
1684 | UV_EXTERN int uv_dlsym(uv_lib_t* lib, const char* name, void** ptr);
{% endraw %}

```
### test/test-dlerror.c

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
### docs/code/plugin/main.c

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