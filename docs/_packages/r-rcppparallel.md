---
name: "r-rcppparallel"
layout: package
next_package: lhapdf5
previous_package: libxaw3d
languages: ['cpp']
---
## 4.4.3
9 / 506 files match

 - [src/tbb/build/android.inc](#srctbbbuildandroidinc)
 - [src/tbb/src/tbb/itt_notify.cpp](#srctbbsrctbbitt_notifycpp)
 - [src/tbb/src/tbb/dynamic_link.cpp](#srctbbsrctbbdynamic_linkcpp)
 - [src/tbb/src/tbb/tools_api/ittnotify_config.h](#srctbbsrctbbtools_apiittnotify_configh)
 - [src/tbb/src/rml/server/rml_server.cpp](#srctbbsrcrmlserverrml_servercpp)
 - [src/tbb/src/tbbproxy/tbbproxy.cpp](#srctbbsrctbbproxytbbproxycpp)
 - [src/tbb/src/tbbmalloc/tbbmalloc.cpp](#srctbbsrctbbmalloctbbmalloccpp)
 - [src/tbb/include/tbb/tbb_config.h](#srctbbincludetbbtbb_configh)
 - [inst/include/tbb/tbb_config.h](#instincludetbbtbb_configh)

### src/tbb/build/android.inc

```

{% raw %}
21 | #    dlopen_workaround:  Some OS versions need workaround for dlopen to avoid recursive calls.
{% endraw %}

```
### src/tbb/src/tbb/itt_notify.cpp

```

{% raw %}
27 |     #pragma weak dlopen
52 |     // tool_api crashes without dlopen, check that it's present. Common case
53 |     // for lack of dlopen is static binaries, i.e. ones build with -static.
54 |     if (dlopen == NULL)
{% endraw %}

```
### src/tbb/src/tbb/dynamic_link.cpp

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
### src/tbb/src/tbb/tools_api/ittnotify_config.h

```cpp

{% raw %}
282 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
{% endraw %}

```
### src/tbb/src/rml/server/rml_server.cpp

```

{% raw %}
3200 |     // Hack to keep this library from being closed by causing the first client's dlopen to not have a corresponding dlclose.
{% endraw %}

```
### src/tbb/src/tbbproxy/tbbproxy.cpp

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
### src/tbb/src/tbbmalloc/tbbmalloc.cpp

```

{% raw %}
28 | #include <dlfcn.h> // dlopen
92 | // Work around non-reentrancy in dlopen() on Android
93 | #if !__TBB_USE_DLOPEN_REENTRANCY_WORKAROUND
96 |         dlopen(MALLOCLIB_NAME, RTLD_NOW);
98 | #endif /* !__TBB_USE_DLOPEN_REENTRANCY_WORKAROUND */
{% endraw %}

```
### src/tbb/include/tbb/tbb_config.h

```cpp

{% raw %}
750 | // Many OS versions (Android 4.0.[0-3] for example) need workaround for dlopen to avoid non-recursive loader lock hang
754 | #define __TBB_USE_DLOPEN_REENTRANCY_WORKAROUND  (__ANDROID_API__ < 19)
{% endraw %}

```
### inst/include/tbb/tbb_config.h

```cpp

{% raw %}
755 | // Many OS versions (Android 4.0.[0-3] for example) need workaround for dlopen to avoid non-recursive loader lock hang
759 | #define __TBB_USE_DLOPEN_REENTRANCY_WORKAROUND  (__ANDROID_API__ < 19)
{% endraw %}

```