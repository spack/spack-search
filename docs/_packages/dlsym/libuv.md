---
name: "libuv"
layout: package
next_package: libxsmm
previous_package: libunwind
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.38.1
12 / 422 files match, 9 filtered matches.

 - [src/win/dl.c](#srcwindlc)
 - [src/unix/darwin-proctitle.c](#srcunixdarwin-proctitlec)
 - [src/unix/fs.c](#srcunixfsc)
 - [src/unix/random-getentropy.c](#srcunixrandom-getentropyc)
 - [src/unix/dl.c](#srcunixdlc)
 - [src/unix/random-getrandom.c](#srcunixrandom-getrandomc)
 - [src/unix/darwin.c](#srcunixdarwinc)
 - [include/uv.h](#includeuvh)
 - [docs/code/plugin/main.c](#docscodepluginmainc)

### src/win/dl.c

```c

{% raw %}
62 | }
63 | 
64 | 
65 | int uv_dlsym(uv_lib_t* lib, const char* name, void** ptr) {
66 |   /* Cast though integer to suppress pedantic warning about forbidden cast. */
67 |   *ptr = (void*)(uintptr_t) GetProcAddress(lib->handle, name);
{% endraw %}

```
### src/unix/darwin-proctitle.c

```c

{% raw %}
90 |     goto out;
91 | 
92 |   *(void **)(&pCFStringCreateWithCString) =
93 |       dlsym(core_foundation_handle, "CFStringCreateWithCString");
94 |   *(void **)(&pCFBundleGetBundleWithIdentifier) =
95 |       dlsym(core_foundation_handle, "CFBundleGetBundleWithIdentifier");
96 |   *(void **)(&pCFBundleGetDataPointerForName) =
97 |       dlsym(core_foundation_handle, "CFBundleGetDataPointerForName");
98 |   *(void **)(&pCFBundleGetFunctionPointerForName) =
99 |       dlsym(core_foundation_handle, "CFBundleGetFunctionPointerForName");
100 | 
101 |   if (pCFStringCreateWithCString == NULL ||
{% endraw %}

```
### src/unix/fs.c

```c

{% raw %}
272 |    * because it doesn't have mkostemp(O_CLOEXEC) either.
273 |    */
274 | #ifdef RTLD_DEFAULT
275 |   uv__mkostemp = (int (*)(char*, int)) dlsym(RTLD_DEFAULT, "mkostemp");
276 | 
277 |   /* We don't care about errors, but we do want to clean them up.
{% endraw %}

```
### src/unix/random-getentropy.c

```c

{% raw %}
31 | 
32 | 
33 | static void uv__random_getentropy_init(void) {
34 |   uv__getentropy = (uv__getentropy_cb) dlsym(RTLD_DEFAULT, "getentropy");
35 | }
36 | 
{% endraw %}

```
### src/unix/dl.c

```c

{% raw %}
49 | }
50 | 
51 | 
52 | int uv_dlsym(uv_lib_t* lib, const char* name, void** ptr) {
53 |   dlerror(); /* Reset error status. */
54 |   *ptr = dlsym(lib->handle, name);
{% endraw %}

```
### src/unix/random-getrandom.c

```c

{% raw %}
38 | static uv_once_t once = UV_ONCE_INIT;
39 | 
40 | static void uv__random_getrandom_init_once(void) {
41 |   uv__getrandom = (uv__getrandom_cb) dlsym(RTLD_DEFAULT, "getrandom");
42 | }
43 | 
{% endraw %}

```
### src/unix/darwin.c

```c

{% raw %}
56 |   if (KERN_SUCCESS != mach_timebase_info(&timebase))
57 |     abort();
58 | 
59 |   time_func = (uint64_t (*)(void)) dlsym(RTLD_DEFAULT, "mach_continuous_time");
60 |   if (time_func == NULL)
61 |     time_func = mach_absolute_time;
{% endraw %}

```
### include/uv.h

```c

{% raw %}
1681 | 
1682 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
1683 | UV_EXTERN void uv_dlclose(uv_lib_t* lib);
1684 | UV_EXTERN int uv_dlsym(uv_lib_t* lib, const char* name, void** ptr);
1685 | UV_EXTERN const char* uv_dlerror(const uv_lib_t* lib);
1686 | 
{% endraw %}

```
### docs/code/plugin/main.c

```c

{% raw %}
26 |         }
27 | 
28 |         init_plugin_function init_plugin;
29 |         if (uv_dlsym(lib, "initialize", (void **) &init_plugin)) {
30 |             fprintf(stderr, "dlsym error: %s\n", uv_dlerror(lib));
31 |             continue;
32 |         }
{% endraw %}

```