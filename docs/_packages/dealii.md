---
name: "dealii"
layout: package
next_package: xcb-util-keysyms
previous_package: ncbi-magicblast
languages: ['cmake', 'cpp']
---
## 9.1.0
8 / 10417 files match

 - [bundled/tbb-2018_U2/src/tbb/itt_notify.cpp](#bundledtbb-2018_u2srctbbitt_notifycpp)
 - [bundled/tbb-2018_U2/src/tbb/dynamic_link.cpp](#bundledtbb-2018_u2srctbbdynamic_linkcpp)
 - [bundled/tbb-2018_U2/src/tbb/tools_api/ittnotify_config.h](#bundledtbb-2018_u2srctbbtools_apiittnotify_configh)
 - [bundled/tbb-2018_U2/src/rml/server/rml_server.cpp](#bundledtbb-2018_u2srcrmlserverrml_servercpp)
 - [bundled/tbb-2018_U2/src/tbbproxy/tbbproxy.cpp](#bundledtbb-2018_u2srctbbproxytbbproxycpp)
 - [bundled/tbb-2018_U2/src/tbbmalloc/tbbmalloc.cpp](#bundledtbb-2018_u2srctbbmalloctbbmalloccpp)
 - [bundled/tbb-2018_U2/include/tbb/tbb_config.h](#bundledtbb-2018_u2includetbbtbb_configh)
 - [cmake/configure/configure_1_threads.cmake](#cmakeconfigureconfigure_1_threadscmake)

### bundled/tbb-2018_U2/src/tbb/itt_notify.cpp

```

{% raw %}
27 |     #pragma weak dlopen
52 |     // tool_api crashes without dlopen, check that it's present. Common case
53 |     // for lack of dlopen is static binaries, i.e. ones build with -static.
54 |     if (dlopen == NULL)
{% endraw %}

```
### bundled/tbb-2018_U2/src/tbb/dynamic_link.cpp

```

{% raw %}
34 |     #define dlopen( name, flags )   LoadLibrary( name )
51 |     #pragma weak dlopen
89 |     dlopen may fail to reopen the library in two cases:
444 |             library_handle = dlopen( info.dli_fname, RTLD_LAZY );
477 |         if ( !dlopen ) return 0;
479 |         library_handle = dlopen( NULL, RTLD_LAZY );
481 |         // On Android dlopen( NULL ) returns NULL if it is called during dynamic module initialization.
526 |         dynamic_link_handle library_handle = dlopen( path, RTLD_LAZY );
{% endraw %}

```
### bundled/tbb-2018_U2/src/tbb/tools_api/ittnotify_config.h

```cpp

{% raw %}
282 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
{% endraw %}

```
### bundled/tbb-2018_U2/src/rml/server/rml_server.cpp

```

{% raw %}
3200 |     // Hack to keep this library from being closed by causing the first client's dlopen to not have a corresponding dlclose.
{% endraw %}

```
### bundled/tbb-2018_U2/src/tbbproxy/tbbproxy.cpp

```

{% raw %}
42 |     #include <dlfcn.h>    // dlopen, dlsym, dlclose, dlerror.
235 |     Windows implementation of dlopen, dlclose, dlsym, dlerror.
242 |     // Implement Unix-like interface (dlopen, dlclose, dlsym, dlerror) via Win32 API functions.
244 |     // Type of dlopen result.
252 |     // Unix-like dlopen().
253 |     static handle_t dlopen( char const * name, rtld_flags_t ) {
255 |     } // dlopen
310 |     // Type of dlopen() result.
374 |     _handle = dlopen( dll_name, RTLD_NOW );
{% endraw %}

```
### bundled/tbb-2018_U2/src/tbbmalloc/tbbmalloc.cpp

```

{% raw %}
28 | #include <dlfcn.h> // dlopen
92 | // Work around non-reentrancy in dlopen() on Android
93 | #if !__TBB_USE_DLOPEN_REENTRANCY_WORKAROUND
96 |         dlopen(MALLOCLIB_NAME, RTLD_NOW);
98 | #endif /* !__TBB_USE_DLOPEN_REENTRANCY_WORKAROUND */
{% endraw %}

```
### bundled/tbb-2018_U2/include/tbb/tbb_config.h

```cpp

{% raw %}
751 | // Many OS versions (Android 4.0.[0-3] for example) need workaround for dlopen to avoid non-recursive loader lock hang
755 | #define __TBB_USE_DLOPEN_REENTRANCY_WORKAROUND  (__ANDROID_API__ < 19)
{% endraw %}

```
### cmake/configure/configure_1_threads.cmake

```cmake

{% raw %}
225 |   # tbb uses dlopen/dlclose, so link against libdl.so as well:
{% endraw %}

```