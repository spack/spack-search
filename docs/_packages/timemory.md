---
name: "timemory"
layout: package
next_package: fermisciencetools
previous_package: binutils
languages: ['cmake', 'cpp']
---
## master
29 / 2657 files match

 - [source/tools/timemory-jump/README.md](#sourcetoolstimemory-jumpreadmemd)
 - [source/tools/timemory-jump/library.cpp](#sourcetoolstimemory-jumplibrarycpp)
 - [external/llvm-ompt/runtime/src/z_Linux_util.cpp](#externalllvm-omptruntimesrcz_linux_utilcpp)
 - [external/llvm-ompt/runtime/src/ompt-general.cpp](#externalllvm-omptruntimesrcompt-generalcpp)
 - [external/llvm-ompt/runtime/src/thirdparty/ittnotify/ittnotify_config.h](#externalllvm-omptruntimesrcthirdpartyittnotifyittnotify_configh)
 - [external/llvm-ompt/libomptarget/src/rtl.cpp](#externalllvm-omptlibomptargetsrcrtlcpp)
 - [external/llvm-ompt/libomptarget/plugins/generic-elf-64bit/src/rtl.cpp](#externalllvm-omptlibomptargetpluginsgeneric-elf-64bitsrcrtlcpp)
 - [external/line-profiler/cmake/Modules/targetLinkLibrariesWithDynamicLookup.cmake](#externalline-profilercmakemodulestargetlinklibrarieswithdynamiclookupcmake)
 - [external/gotcha/src/gotcha_dl.h](#externalgotchasrcgotcha_dlh)
 - [external/gotcha/src/gotcha_dl.c](#externalgotchasrcgotcha_dlc)
 - [external/gotcha/src/hash.c](#externalgotchasrchashc)
 - [external/gotcha/src/gotcha.c](#externalgotchasrcgotchac)
 - [external/gotcha/test/CMakeLists.txt](#externalgotchatestcmakeliststxt)
 - [external/gotcha/test/dlopen/test_dlopen.c](#externalgotchatestdlopentest_dlopenc)
 - [external/gotcha/test/dlopen/CMakeLists.txt](#externalgotchatestdlopencmakeliststxt)
 - [external/gotcha/test/multi_agent_dlopen/dlsym.c](#externalgotchatestmulti_agent_dlopendlsymc)
 - [external/gotcha/test/multi_agent_dlopen/monitor.c](#externalgotchatestmulti_agent_dlopenmonitorc)
 - [external/gotcha/test/multi_agent_dlopen/main.c](#externalgotchatestmulti_agent_dlopenmainc)
 - [external/gotcha/test/multi_agent_dlopen/CMakeLists.txt](#externalgotchatestmulti_agent_dlopencmakeliststxt)
 - [external/google-test/googletest/cmake/libgtest.la.in](#externalgoogle-testgoogletestcmakelibgtestlain)
 - [external/pybind11/include/pybind11/detail/internals.h](#externalpybind11includepybind11detailinternalsh)
 - [external/pybind11/docs/faq.rst](#externalpybind11docsfaqrst)
 - [external/caliper/ext/gotcha/src/gotcha_dl.h](#externalcaliperextgotchasrcgotcha_dlh)
 - [external/caliper/ext/gotcha/src/gotcha_dl.c](#externalcaliperextgotchasrcgotcha_dlc)
 - [external/caliper/ext/gotcha/src/hash.c](#externalcaliperextgotchasrchashc)
 - [external/caliper/ext/gotcha/src/gotcha.c](#externalcaliperextgotchasrcgotchac)
 - [cmake/Modules/BuildSettings.cmake](#cmakemodulesbuildsettingscmake)
 - [docs/tools.md](#docstoolsmd)
 - [docs/tools/timemory-jump/README.md](#docstoolstimemory-jumpreadmemd)

### source/tools/timemory-jump/README.md

```

{% raw %}
4 | `TIMEMORY_JUMP_LIBRARY` on libraries which provide `dlsym` and `dlopen`.
{% endraw %}

```
### source/tools/timemory-jump/library.cpp

```

{% raw %}
76 |         auto libhandle = dlopen(libpath.c_str(), RTLD_LAZY);
{% endraw %}

```
### external/llvm-ompt/runtime/src/z_Linux_util.cpp

```

{% raw %}
1348 |      handler. Mathworks: dlsym() is unsafe. We call dlsym and dlopen
{% endraw %}

```
### external/llvm-ompt/runtime/src/ompt-general.cpp

```

{% raw %}
254 |       void *h = dlopen(fname, RTLD_LAZY);
{% endraw %}

```
### external/llvm-ompt/runtime/src/thirdparty/ittnotify/ittnotify_config.h

```cpp

{% raw %}
280 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
{% endraw %}

```
### external/llvm-ompt/libomptarget/src/rtl.cpp

```

{% raw %}
60 |     void *dynlib_handle = dlopen(Name, RTLD_NOW);
{% endraw %}

```
### external/llvm-ompt/libomptarget/plugins/generic-elf-64bit/src/rtl.cpp

```

{% raw %}
214 |   // 2) Use dlopen to load the file and dlsym to retrieve the symbols.
233 |   DynLibTy Lib = {tmp_name, dlopen(tmp_name, RTLD_LAZY)};
{% endraw %}

```
### external/line-profiler/cmake/Modules/targetLinkLibrariesWithDynamicLookup.cmake

```cmake

{% raw %}
342 |         counter_module = dlopen(\"./counter.so\", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### external/gotcha/src/gotcha_dl.h

```cpp

{% raw %}
10 | extern gotcha_wrappee_handle_t orig_dlopen_handle;
{% endraw %}

```
### external/gotcha/src/gotcha_dl.c

```cpp

{% raw %}
9 | gotcha_wrappee_handle_t orig_dlopen_handle;
17 |    debug_printf(3, "Trying to re-bind %s from tool %s after dlopen\n",
28 |       debug_printf(3, "Still could not prepare binding %s after dlopen\n", binding->user_binding->name);
36 | static void* dlopen_wrapper(const char* filename, int flags) {
37 |    typeof(&dlopen_wrapper) orig_dlopen = gotcha_get_wrappee(orig_dlopen_handle);
39 |    debug_printf(1, "User called dlopen(%s, 0x%x)\n", filename, (unsigned int) flags);
40 |    handle = orig_dlopen(filename,flags);
42 |    debug_printf(2, "Searching new dlopened libraries for previously-not-found exports\n");
45 |    debug_printf(2, "Updating GOT entries for new dlopened libraries\n");
72 |   {"dlopen", dlopen_wrapper, &orig_dlopen_handle},
{% endraw %}

```
### external/gotcha/src/hash.c

```cpp

{% raw %}
216 |    //idiom used under dlopen_wrapper.
{% endraw %}

```
### external/gotcha/src/gotcha.c

```cpp

{% raw %}
317 |            debug_printf(2, "Stashing %s in notfound_binding table to re-lookup on dlopens\n",
{% endraw %}

```
### external/gotcha/test/CMakeLists.txt

```

{% raw %}
2 | add_subdirectory(dlopen)
5 | add_subdirectory(multi_agent_dlopen)
{% endraw %}

```
### external/gotcha/test/dlopen/test_dlopen.c

```cpp

{% raw %}
59 |    result = gotcha_wrap(funcs, 2, "dlopen_test");
65 |    libnum = dlopen(LIB_NAME, RTLD_NOW);
67 |       fprintf(stderr, "ERROR: Test failed to dlopen libnum.so\n");
78 |    /* Test 2: Does a call in a dlopen'd library get rerouted by gotcha */
{% endraw %}

```
### external/gotcha/test/dlopen/CMakeLists.txt

```

{% raw %}
1 | add_executable(test_dlopen test_dlopen.c)
2 | set_target_properties(test_dlopen
5 | target_link_libraries(test_dlopen gotcha dl)
6 | gotcha_add_test(dlopen_test test_dlopen)
7 | environment_add(dlopen_test TEST "GOTCHA_DEBUG=3 LIBNUM_DIR=${CMAKE_CURRENT_BINARY_DIR}")
8 | set_tests_properties(dlopen_test PROPERTIES
{% endraw %}

```
### external/gotcha/test/multi_agent_dlopen/dlsym.c

```cpp

{% raw %}
16 | typedef void * dlopen_mode_fcn_t(const char *, int);
19 | dlopen_mode_fcn_t __libc_dlopen_mode;
26 |     void * dl_handle = __libc_dlopen_mode("libdl.so", RTLD_LAZY);
29 | 	err(1, "__libc_dlopen_mode failed");
{% endraw %}

```
### external/gotcha/test/multi_agent_dlopen/monitor.c

```cpp

{% raw %}
3 |  *  Override dlopen() use dlsym(RTLD_NEXT).
16 | typedef void *dlopen_fcn_t(const char *, int);
18 | gotcha_wrappee_handle_t reel_dlopen_handle;
21 | wrap_dlopen(const char *file, int flag)
23 |     typeof(&wrap_dlopen) reel_dlopen = gotcha_get_wrappee(reel_dlopen_handle);
24 |     fprintf(stderr, "ENTER WRAP: %p\n", reel_dlopen);
25 |     fprintf(stderr, "%s:  enter dlopen:  file = %s\n", MYNAME, file);
27 |     void *ans = reel_dlopen ? (reel_dlopen)(file, flag) : NULL;
29 |       fprintf(stderr, "Real dlopen not found\n");
31 |     fprintf(stderr, "%s:  exit  dlopen:  handle = %p\n", MYNAME, ans);
37 |   { "dlopen", wrap_dlopen, &reel_dlopen_handle}
40 |   reel_dlopen_handle = NULL;
42 |   typeof(&wrap_dlopen) reel_dlopen = gotcha_get_wrappee(reel_dlopen_handle);
43 |   fprintf(stderr, "IMMEDIATE WRITE: %p\n", reel_dlopen);
{% endraw %}

```
### external/gotcha/test/multi_agent_dlopen/main.c

```cpp

{% raw %}
1 |  *  Try dlopen(libm.so, ...) and call sin().
23 |     void *handle = dlopen("libm.so", RTLD_NOW);
25 | 	err(1, "dlopen failed");
{% endraw %}

```
### external/gotcha/test/multi_agent_dlopen/CMakeLists.txt

```

{% raw %}
6 | gotcha_add_test(multi_agent_dlopen multi_agent_main)
7 | environment_add(multi_agent_dlopen TEST "LD_PRELOAD=${CMAKE_CURRENT_BINARY_DIR}/libmulti_agent_sym.so:${CMAKE_CURRENT_BINARY_DIR}/libmulti_agent_mon.so GOTCHA_DEBUG=3 LIBNUM_DIR=${CMAKE_CURRENT_BINARY_DIR}")
{% endraw %}

```
### external/google-test/googletest/cmake/libgtest.la.in

```

{% raw %}
15 | # Files to dlopen/dlpreopen
16 | dlopen=''
{% endraw %}

```
### external/pybind11/include/pybind11/detail/internals.h

```cpp

{% raw %}
49 | // Python loads modules by default with dlopen with the RTLD_LOCAL flag; under libc++ and possibly
{% endraw %}

```
### external/pybind11/docs/faq.rst

```

{% raw %}
178 | typically using ``dlopen`` with the ``RTLD_LOCAL`` flag), this Python default
{% endraw %}

```
### external/caliper/ext/gotcha/src/gotcha_dl.h

```cpp

{% raw %}
10 | extern gotcha_wrappee_handle_t orig_dlopen_handle;
{% endraw %}

```
### external/caliper/ext/gotcha/src/gotcha_dl.c

```cpp

{% raw %}
9 | gotcha_wrappee_handle_t orig_dlopen_handle;
17 |    debug_printf(3, "Trying to re-bind %s from tool %s after dlopen\n",
28 |       debug_printf(3, "Still could not prepare binding %s after dlopen\n", binding->user_binding->name);
36 | static void* dlopen_wrapper(const char* filename, int flags) {
37 |    typeof(&dlopen_wrapper) orig_dlopen = gotcha_get_wrappee(orig_dlopen_handle);
39 |    debug_printf(1, "User called dlopen(%s, 0x%x)\n", filename, (unsigned int) flags);
40 |    handle = orig_dlopen(filename,flags);
42 |    debug_printf(2, "Searching new dlopened libraries for previously-not-found exports\n");
45 |    debug_printf(2, "Updating GOT entries for new dlopened libraries\n");
68 |   {"dlopen", dlopen_wrapper, &orig_dlopen_handle},
{% endraw %}

```
### external/caliper/ext/gotcha/src/hash.c

```cpp

{% raw %}
216 |    //idiom used under dlopen_wrapper.
{% endraw %}

```
### external/caliper/ext/gotcha/src/gotcha.c

```cpp

{% raw %}
317 |            debug_printf(2, "Stashing %s in notfound_binding table to re-lookup on dlopens\n",
{% endraw %}

```
### cmake/Modules/BuildSettings.cmake

```cmake

{% raw %}
155 |     # symbol table. This option is needed for some uses of dlopen or to allow obtaining
{% endraw %}

```
### docs/tools.md

```

{% raw %}
31 |         - Provides timemory instrumentation via `dlopen` and `dlsym`
{% endraw %}

```
### docs/tools/timemory-jump/README.md

```

{% raw %}
2 | The timemory jump library implements the **jump** instrumentation mode for `timemory-run` tool. Additionally, this library can be linked to in lieu of the traditional timemory library and provide instrumentation via setting the environment variable `TIMEMORY_JUMP_LIBRARY` on libraries which provide `dlsym` and `dlopen`.
{% endraw %}

```