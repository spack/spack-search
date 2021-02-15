---
name: "cmake"
layout: package
next_package: brltty
previous_package: cppad
languages: ['cmake', 'cpp']
---
## 3.18.3
22 / 16369 files match

 - [Help/variable/CMAKE_DL_LIBS.rst](#helpvariablecmake_dl_libsrst)
 - [Help/policy/CMP0065.rst](#helppolicycmp0065rst)
 - [Help/command/add_library.rst](#helpcommandadd_libraryrst)
 - [Help/command/file.rst](#helpcommandfilerst)
 - [Tests/Plugin/src/DynamicLoader.cxx](#testspluginsrcdynamicloadercxx)
 - [Tests/BundleUtilities/testbundleutils1.cpp](#testsbundleutilitiestestbundleutils1cpp)
 - [Tests/BundleUtilities/testbundleutils2.cpp](#testsbundleutilitiestestbundleutils2cpp)
 - [Tests/BundleUtilities/testbundleutils3.cpp](#testsbundleutilitiestestbundleutils3cpp)
 - [Utilities/cmlibuv/src/win/dl.c](#utilitiescmlibuvsrcwindlc)
 - [Utilities/cmlibuv/src/unix/darwin-proctitle.c](#utilitiescmlibuvsrcunixdarwin-proctitlec)
 - [Utilities/cmlibuv/src/unix/fsevents.c](#utilitiescmlibuvsrcunixfseventsc)
 - [Utilities/cmlibuv/src/unix/dl.c](#utilitiescmlibuvsrcunixdlc)
 - [Utilities/cmlibuv/include/uv.h](#utilitiescmlibuvincludeuvh)
 - [Utilities/cmlibuv/include/uv/win.h](#utilitiescmlibuvincludeuvwinh)
 - [Utilities/cmlibuv/include/uv/unix.h](#utilitiescmlibuvincludeuvunixh)
 - [Utilities/cmcurl/CMakeLists.txt](#utilitiescmcurlcmakeliststxt)
 - [Source/kwsys/DynamicLoader.cxx](#sourcekwsysdynamicloadercxx)
 - [Source/kwsys/DynamicLoader.hxx.in](#sourcekwsysdynamicloaderhxxin)
 - [Source/kwsys/testDynamicLoader.cxx](#sourcekwsystestdynamicloadercxx)
 - [Modules/KDE3Macros.cmake](#moduleskde3macroscmake)
 - [Modules/Platform/Linux-Intel.cmake](#modulesplatformlinux-intelcmake)
 - [Modules/Platform/Linux-GNU.cmake](#modulesplatformlinux-gnucmake)

### Help/variable/CMAKE_DL_LIBS.rst

```

{% raw %}
3 | Name of library containing ``dlopen`` and ``dlclose``.
5 | The name of the library that has ``dlopen`` and ``dlclose`` in it, usually
{% endraw %}

```
### Help/policy/CMP0065.rst

```

{% raw %}
8 | the executables for use by any plugins they may load via ``dlopen``.
{% endraw %}

```
### Help/command/add_library.rst

```

{% raw %}
31 | using dlopen-like functionality.  If no type is given explicitly the
{% endraw %}

```
### Help/command/file.rst

```

{% raw %}
209 |   ``dlopen()`` at runtime rather than linked at link time with ``ld -l``.
{% endraw %}

```
### Tests/Plugin/src/DynamicLoader.cxx

```

{% raw %}
236 |   return dlopen(libname.c_str(), RTLD_LAZY);
{% endraw %}

```
### Tests/BundleUtilities/testbundleutils1.cpp

```

{% raw %}
22 |   void* lib = dlopen("module1.so", RTLD_LAZY);
{% endraw %}

```
### Tests/BundleUtilities/testbundleutils2.cpp

```

{% raw %}
22 |   void* lib = dlopen("module2.so", RTLD_LAZY);
{% endraw %}

```
### Tests/BundleUtilities/testbundleutils3.cpp

```

{% raw %}
22 |   void* lib = dlopen("module3.so", RTLD_LAZY);
{% endraw %}

```
### Utilities/cmlibuv/src/win/dl.c

```cpp

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### Utilities/cmlibuv/src/unix/darwin-proctitle.c

```cpp

{% raw %}
80 |   application_services_handle = dlopen("/System/Library/Frameworks/"
84 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### Utilities/cmlibuv/src/unix/fsevents.c

```cpp

{% raw %}
532 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
539 |   core_services_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### Utilities/cmlibuv/src/unix/dl.c

```cpp

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### Utilities/cmlibuv/include/uv.h

```cpp

{% raw %}
1700 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```
### Utilities/cmlibuv/include/uv/win.h

```cpp

{% raw %}
328 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### Utilities/cmlibuv/include/uv/unix.h

```cpp

{% raw %}
229 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### Utilities/cmcurl/CMakeLists.txt

```

{% raw %}
386 | check_library_exists_concat("${CMAKE_DL_LIBS}" dlopen HAVE_LIBDL)
725 | # Check for symbol dlopen (same as HAVE_LIBDL)
726 | check_library_exists("${CURL_LIBS}" dlopen "" HAVE_DLOPEN)
{% endraw %}

```
### Source/kwsys/DynamicLoader.cxx

```

{% raw %}
27 | //   later) which use dlopen
430 | // later) which use dlopen
440 |   return dlopen(libname.c_str(), RTLD_LAZY);
{% endraw %}

```
### Source/kwsys/DynamicLoader.hxx.in

```

{% raw %}
32 |  * \warning dlopen on *nix system works the following way:
{% endraw %}

```
### Source/kwsys/testDynamicLoader.cxx

```

{% raw %}
96 | // dlopen() on Syllable before 11/22/2007 doesn't return 0 on error
106 |   // This one is actually fun to test, since dlopen is by default
108 |   res += TestDynamicLoader("foobar.lib", "dlopen", 0, 1, 0);
109 |   res += TestDynamicLoader("libdl.so", "dlopen", 1, 1, 1);
{% endraw %}

```
### Modules/KDE3Macros.cmake

```cmake

{% raw %}
310 |   file(APPEND ${_laname} "# The name that we can dlopen(3).\n")
326 |   file(APPEND ${_laname} "# Files to dlopen/dlpreopen\ndlopen=''\ndlpreopen=''\n")
{% endraw %}

```
### Modules/Platform/Linux-Intel.cmake

```cmake

{% raw %}
35 |   # executables that use dlopen but do not set ENABLE_EXPORTS.
{% endraw %}

```
### Modules/Platform/Linux-GNU.cmake

```cmake

{% raw %}
12 |   # executables that use dlopen but do not set ENABLE_EXPORTS.
{% endraw %}

```