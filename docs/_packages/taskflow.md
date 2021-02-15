---
name: "taskflow"
layout: package
next_package: dyninst
previous_package: pmix
languages: ['cpp']
---
## 2.7.0
11 / 3426 files match

 - [3rd-party/tbb/build/android.inc](#3rd-partytbbbuildandroidinc)
 - [3rd-party/tbb/src/tbb/itt_notify.cpp](#3rd-partytbbsrctbbitt_notifycpp)
 - [3rd-party/tbb/src/tbb/dynamic_link.cpp](#3rd-partytbbsrctbbdynamic_linkcpp)
 - [3rd-party/tbb/src/tbb/tools_api/ittnotify_config.h](#3rd-partytbbsrctbbtools_apiittnotify_configh)
 - [3rd-party/tbb/src/rml/server/rml_server.cpp](#3rd-partytbbsrcrmlserverrml_servercpp)
 - [3rd-party/tbb/src/tbbproxy/tbbproxy.cpp](#3rd-partytbbsrctbbproxytbbproxycpp)
 - [3rd-party/tbb/src/tbbmalloc/tbbmalloc.cpp](#3rd-partytbbsrctbbmalloctbbmalloccpp)
 - [3rd-party/tbb/src/test/harness_dynamic_libs.h](#3rd-partytbbsrctestharness_dynamic_libsh)
 - [3rd-party/tbb/src/test/test_model_plugin.cpp](#3rd-partytbbsrctesttest_model_plugincpp)
 - [3rd-party/tbb/src/test/test_cilk_dynamic_load.cpp](#3rd-partytbbsrctesttest_cilk_dynamic_loadcpp)
 - [3rd-party/tbb/include/tbb/tbb_config.h](#3rd-partytbbincludetbbtbb_configh)

### 3rd-party/tbb/build/android.inc

```

{% raw %}
17 | #    dlopen_workaround:  Some OS versions need workaround for dlopen to avoid recursive calls.
{% endraw %}

```
### 3rd-party/tbb/src/tbb/itt_notify.cpp

```

{% raw %}
23 |     #pragma weak dlopen
48 |     // tool_api crashes without dlopen, check that it's present. Common case
49 |     // for lack of dlopen is static binaries, i.e. ones build with -static.
50 |     if (dlopen == NULL)
{% endraw %}

```
### 3rd-party/tbb/src/tbb/dynamic_link.cpp

```

{% raw %}
30 |     #define dlopen( name, flags )   LoadLibrary( name )
47 |     #pragma weak dlopen
85 |     dlopen may fail to reopen the library in two cases:
439 |             library_handle = dlopen( info.dli_fname, RTLD_LAZY );
472 |         if ( !dlopen ) return 0;
474 |         library_handle = dlopen( NULL, RTLD_LAZY );
476 |         // On Android dlopen( NULL ) returns NULL if it is called during dynamic module initialization.
521 |             dynamic_link_handle library_handle = dlopen( path, RTLD_LAZY );
{% endraw %}

```
### 3rd-party/tbb/src/tbb/tools_api/ittnotify_config.h

```cpp

{% raw %}
282 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
341 | void* dlopen(const char*, int) __attribute__((weak));
344 | #define DL_SYMBOLS (dlopen && dlsym && dlclose)
{% endraw %}

```
### 3rd-party/tbb/src/rml/server/rml_server.cpp

```

{% raw %}
3196 |     // Hack to keep this library from being closed by causing the first client's dlopen to not have a corresponding dlclose.
{% endraw %}

```
### 3rd-party/tbb/src/tbbproxy/tbbproxy.cpp

```

{% raw %}
39 |     #include <dlfcn.h>    // dlopen, dlsym, dlclose, dlerror.
231 |     Windows implementation of dlopen, dlclose, dlsym, dlerror.
238 |     // Implement Unix-like interface (dlopen, dlclose, dlsym, dlerror) via Win32 API functions.
240 |     // Type of dlopen result.
248 |     // Unix-like dlopen().
249 |     static handle_t dlopen( char const * name, rtld_flags_t ) {
251 |     } // dlopen
306 |     // Type of dlopen() result.
370 |     _handle = dlopen( dll_name, RTLD_NOW );
{% endraw %}

```
### 3rd-party/tbb/src/tbbmalloc/tbbmalloc.cpp

```

{% raw %}
24 | #include <dlfcn.h> // dlopen
87 | // Work around non-reentrancy in dlopen() on Android
88 | #if !__TBB_USE_DLOPEN_REENTRANCY_WORKAROUND
91 |         dlopen(MALLOCLIB_NAME, RTLD_NOW);
93 | #endif /* !__TBB_USE_DLOPEN_REENTRANCY_WORKAROUND */
{% endraw %}

```
### 3rd-party/tbb/src/test/harness_dynamic_libs.h

```cpp

{% raw %}
86 |     return dlopen(name, RTLD_NOW|RTLD_GLOBAL);
{% endraw %}

```
### 3rd-party/tbb/src/test/test_model_plugin.cpp

```

{% raw %}
167 |     hLib = dlopen(RML_LIBRARY_NAME("libirml"), RTLD_LAZY);
169 |         hLib = dlopen(RML_LIBRARY_NAME("libirml_debug"), RTLD_LAZY);
183 |             report_error_in("dlopen");
{% endraw %}

```
### 3rd-party/tbb/src/test/test_cilk_dynamic_load.cpp

```

{% raw %}
20 | // Skip the test when cilkrts did not have dlopen()/dlclose() start up feature
26 | //2)   Intel(R) Cilk(TM) Plus, and it should be dynamically loaded with dlopen/LoadLibrary (possibly via a 3rd party module);
{% endraw %}

```
### 3rd-party/tbb/include/tbb/tbb_config.h

```cpp

{% raw %}
834 | // Many OS versions (Android 4.0.[0-3] for example) need workaround for dlopen to avoid non-recursive loader lock hang
838 | #define __TBB_USE_DLOPEN_REENTRANCY_WORKAROUND  (__ANDROID_API__ < 19)
{% endraw %}

```