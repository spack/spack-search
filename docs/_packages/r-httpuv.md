---
name: "r-httpuv"
layout: package
next_package: r-igraph
previous_package: r-fs
languages: ['c']
---
## 1.3.5
6 / 254 files match, 4 filtered matches.

 - [src/libuv/src/win/dl.c](#srclibuvsrcwindlc)
 - [src/libuv/src/unix/dl.c](#srclibuvsrcunixdlc)
 - [src/libuv/include/uv.h](#srclibuvincludeuvh)
 - [src/libuv/test/test-dlerror.c](#srclibuvtesttest-dlerrorc)

### src/libuv/src/win/dl.c

```c

{% raw %}
24 | static int uv__dlerror(uv_lib_t* lib, int errorno);
25 | 
26 | 
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
28 |   WCHAR filename_w[32768];
29 | 
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
1846 |  * Opens a shared library. The filename is in utf-8. Returns 0 on success and
1847 |  * -1 on error. Call `uv_dlerror(uv_lib_t*)` to get the error message.
1848 |  */
1849 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
1850 | 
1851 | /*
{% endraw %}

```
### src/libuv/test/test-dlerror.c

```c

{% raw %}
39 |   const char* dlerror_desc = "";
40 | #endif
41 | 
42 |   r = uv_dlopen(path, &lib);
43 |   ASSERT(r == -1);
44 | 
{% endraw %}

```