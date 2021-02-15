---
name: "intel-tbb"
layout: package
next_package: libuuid
previous_package: vtk
languages: ['cpp']
---
## 2018.2
11 / 1460 files match

 - [build/android.inc](#buildandroidinc)
 - [src/tbb/itt_notify.cpp](#srctbbitt_notifycpp)
 - [src/tbb/dynamic_link.cpp](#srctbbdynamic_linkcpp)
 - [src/tbb/tools_api/ittnotify_config.h](#srctbbtools_apiittnotify_configh)
 - [src/rml/server/rml_server.cpp](#srcrmlserverrml_servercpp)
 - [src/tbbproxy/tbbproxy.cpp](#srctbbproxytbbproxycpp)
 - [src/tbbmalloc/tbbmalloc.cpp](#srctbbmalloctbbmalloccpp)
 - [src/test/harness_dynamic_libs.h](#srctestharness_dynamic_libsh)
 - [src/test/test_model_plugin.cpp](#srctesttest_model_plugincpp)
 - [src/test/test_cilk_dynamic_load.cpp](#srctesttest_cilk_dynamic_loadcpp)
 - [include/tbb/tbb_config.h](#includetbbtbb_configh)

### build/android.inc

```

{% raw %}
21 | #    dlopen_workaround:  Some OS versions need workaround for dlopen to avoid recursive calls.
{% endraw %}

```
### src/tbb/itt_notify.cpp

```

{% raw %}
27 |     #pragma weak dlopen
52 |     // tool_api crashes without dlopen, check that it's present. Common case
53 |     // for lack of dlopen is static binaries, i.e. ones build with -static.
54 |     if (dlopen == NULL)
{% endraw %}

```
### src/tbb/dynamic_link.cpp

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
### src/tbb/tools_api/ittnotify_config.h

```cpp

{% raw %}
282 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
{% endraw %}

```
### src/rml/server/rml_server.cpp

```

{% raw %}
3200 |     // Hack to keep this library from being closed by causing the first client's dlopen to not have a corresponding dlclose.
{% endraw %}

```
### src/tbbproxy/tbbproxy.cpp

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
### src/tbbmalloc/tbbmalloc.cpp

```

{% raw %}
28 | #include <dlfcn.h> // dlopen
92 | // Work around non-reentrancy in dlopen() on Android
93 | #if !__TBB_USE_DLOPEN_REENTRANCY_WORKAROUND
96 |         dlopen(MALLOCLIB_NAME, RTLD_NOW);
98 | #endif /* !__TBB_USE_DLOPEN_REENTRANCY_WORKAROUND */
{% endraw %}

```
### src/test/harness_dynamic_libs.h

```cpp

{% raw %}
90 |     return dlopen(name, RTLD_NOW|RTLD_GLOBAL);
{% endraw %}

```
### src/test/test_model_plugin.cpp

```

{% raw %}
171 |     hLib = dlopen(RML_LIBRARY_NAME("libirml"), RTLD_LAZY);
173 |         hLib = dlopen(RML_LIBRARY_NAME("libirml_debug"), RTLD_LAZY);
187 |             report_error_in("dlopen");
{% endraw %}

```
### src/test/test_cilk_dynamic_load.cpp

```

{% raw %}
24 | // Skip the test when cilkrts did not have dlopen()/dlclose() start up feature
30 | //2)   Intel(R) Cilk(TM) Plus, and it should be dynamically loaded with dlopen/LoadLibrary (possibly via a 3rd party module);
{% endraw %}

```
### include/tbb/tbb_config.h

```cpp

{% raw %}
751 | // Many OS versions (Android 4.0.[0-3] for example) need workaround for dlopen to avoid non-recursive loader lock hang
755 | #define __TBB_USE_DLOPEN_REENTRANCY_WORKAROUND  (__ANDROID_API__ < 19)
{% endraw %}

```