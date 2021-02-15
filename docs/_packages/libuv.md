---
name: "libuv"
layout: package
next_package: py-rpy2
previous_package: libsndfile
languages: ['cpp']
---
## 1.38.1
12 / 422 files match

 - [configure.ac](#configureac)
 - [src/win/dl.c](#srcwindlc)
 - [src/unix/darwin-proctitle.c](#srcunixdarwin-proctitlec)
 - [src/unix/fsevents.c](#srcunixfseventsc)
 - [src/unix/dl.c](#srcunixdlc)
 - [include/uv.h](#includeuvh)
 - [include/uv/win.h](#includeuvwinh)
 - [include/uv/unix.h](#includeuvunixh)
 - [test/test-dlerror.c](#testtest-dlerrorc)
 - [docs/src/dll.rst](#docssrcdllrst)
 - [docs/src/guide/utilities.rst](#docssrcguideutilitiesrst)
 - [docs/code/plugin/main.c](#docscodepluginmainc)

### configure.ac

```

{% raw %}
44 | AC_CHECK_LIB([dl], [dlopen])
{% endraw %}

```
### src/win/dl.c

```cpp

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### src/unix/darwin-proctitle.c

```cpp

{% raw %}
80 |   application_services_handle = dlopen("/System/Library/Frameworks/"
84 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### src/unix/fsevents.c

```cpp

{% raw %}
532 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
539 |   core_services_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### src/unix/dl.c

```cpp

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### include/uv.h

```cpp

{% raw %}
1682 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```
### include/uv/win.h

```cpp

{% raw %}
317 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### include/uv/unix.h

```cpp

{% raw %}
212 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### test/test-dlerror.c

```cpp

{% raw %}
39 |   r = uv_dlopen(path, &lib);
{% endraw %}

```
### docs/src/dll.rst

```

{% raw %}
27 | .. c:function:: int uv_dlopen(const char* filename, uv_lib_t* lib)
43 |     Returns the last uv_dlopen() or uv_dlsym() error message.
{% endraw %}

```
### docs/src/guide/utilities.rst

```

{% raw %}
336 | This is done by using ``uv_dlopen`` to first load the shared library
346 | ``uv_dlopen`` expects a path to the shared library and sets the opaque
{% endraw %}

```
### docs/code/plugin/main.c

```cpp

{% raw %}
23 |         if (uv_dlopen(argv[argc], lib)) {
{% endraw %}

```