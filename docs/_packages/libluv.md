---
name: "libluv"
layout: package
next_package: lcms
previous_package: swipl
languages: ['cmake', 'cpp']
---
## 1.36.0-0
14 / 484 files match

 - [deps/lua.cmake](#depsluacmake)
 - [deps/luajit.cmake](#depsluajitcmake)
 - [deps/libuv/configure.ac](#depslibuvconfigureac)
 - [deps/libuv/src/win/dl.c](#depslibuvsrcwindlc)
 - [deps/libuv/src/unix/darwin-proctitle.c](#depslibuvsrcunixdarwin-proctitlec)
 - [deps/libuv/src/unix/fsevents.c](#depslibuvsrcunixfseventsc)
 - [deps/libuv/src/unix/dl.c](#depslibuvsrcunixdlc)
 - [deps/libuv/include/uv.h](#depslibuvincludeuvh)
 - [deps/libuv/include/uv/win.h](#depslibuvincludeuvwinh)
 - [deps/libuv/include/uv/unix.h](#depslibuvincludeuvunixh)
 - [deps/libuv/test/test-dlerror.c](#depslibuvtesttest-dlerrorc)
 - [deps/libuv/docs/src/dll.rst](#depslibuvdocssrcdllrst)
 - [deps/libuv/docs/src/guide/utilities.rst](#depslibuvdocssrcguideutilitiesrst)
 - [deps/libuv/docs/code/plugin/main.c](#depslibuvdocscodepluginmainc)

### deps/lua.cmake

```cmake

{% raw %}
41 |   CHECK_FUNCTION_EXISTS(dlopen LUA_USE_DLOPEN)
42 |   IF(NOT LUA_USE_DLOPEN)
44 | Function dlopen() seems not to be supported on your platform.
47 |   ENDIF(NOT LUA_USE_DLOPEN)
{% endraw %}

```
### deps/luajit.cmake

```cmake

{% raw %}
87 |   CHECK_FUNCTION_EXISTS(dlopen LUA_USE_DLOPEN)
88 |   IF(NOT LUA_USE_DLOPEN)
90 | Function dlopen() seems not to be supported on your platform.
93 |   ENDIF(NOT LUA_USE_DLOPEN)
{% endraw %}

```
### deps/libuv/configure.ac

```

{% raw %}
41 | AC_CHECK_LIB([dl], [dlopen])
{% endraw %}

```
### deps/libuv/src/win/dl.c

```cpp

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### deps/libuv/src/unix/darwin-proctitle.c

```cpp

{% raw %}
81 |   application_services_handle = dlopen("/System/Library/Frameworks/"
85 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### deps/libuv/src/unix/fsevents.c

```cpp

{% raw %}
536 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
543 |   core_services_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### deps/libuv/src/unix/dl.c

```cpp

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### deps/libuv/include/uv.h

```cpp

{% raw %}
1674 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```
### deps/libuv/include/uv/win.h

```cpp

{% raw %}
317 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### deps/libuv/include/uv/unix.h

```cpp

{% raw %}
212 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### deps/libuv/test/test-dlerror.c

```cpp

{% raw %}
39 |   r = uv_dlopen(path, &lib);
{% endraw %}

```
### deps/libuv/docs/src/dll.rst

```

{% raw %}
27 | .. c:function:: int uv_dlopen(const char* filename, uv_lib_t* lib)
43 |     Returns the last uv_dlopen() or uv_dlsym() error message.
{% endraw %}

```
### deps/libuv/docs/src/guide/utilities.rst

```

{% raw %}
336 | This is done by using ``uv_dlopen`` to first load the shared library
346 | ``uv_dlopen`` expects a path to the shared library and sets the opaque
{% endraw %}

```
### deps/libuv/docs/code/plugin/main.c

```cpp

{% raw %}
23 |         if (uv_dlopen(argv[argc], lib)) {
{% endraw %}

```