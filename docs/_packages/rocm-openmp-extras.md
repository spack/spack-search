---
name: "rocm-openmp-extras"
layout: package
next_package: py-notebook
previous_package: libtheora
languages: ['python', 'c']
---
## 4.0.0
136 / 100137 files match

 - [rocm-openmp-extras/llvm-project/openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h](#rocm-openmp-extrasllvm-projectopenmpruntimesrcthirdpartyittnotifyittnotify_configh)
 - [rocm-openmp-extras/llvm-project/openmp/libomptarget/test/offloading/dynamic_module_load.c](#rocm-openmp-extrasllvm-projectopenmplibomptargettestoffloadingdynamic_module_loadc)
 - [rocm-openmp-extras/llvm-project/openmp/tools/multiplex/ompt-multiplex.h](#rocm-openmp-extrasllvm-projectopenmptoolsmultiplexompt-multiplexh)
 - [rocm-openmp-extras/llvm-project/lldb/include/lldb/Target/Process.h](#rocm-openmp-extrasllvm-projectlldbincludelldbtargetprocessh)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/dlopen_other_executable/TestDlopenOtherExecutable.py](#rocm-openmp-extrasllvm-projectlldbtestapifunctionalitiesdlopen_other_executabletestdlopenotherexecutablepy)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/dlopen_other_executable/main.c](#rocm-openmp-extrasllvm-projectlldbtestapifunctionalitiesdlopen_other_executablemainc)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/load_using_paths/TestLoadUsingPaths.py](#rocm-openmp-extrasllvm-projectlldbtestapifunctionalitiesload_using_pathstestloadusingpathspy)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/load_unload/TestLoadUnload.py](#rocm-openmp-extrasllvm-projectlldbtestapifunctionalitiesload_unloadtestloadunloadpy)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c](#rocm-openmp-extrasllvm-projectlldbtestapimacosxfind-dsymbundle-with-dot-in-filenamemainc)
 - [rocm-openmp-extras/llvm-project/lldb/packages/Python/lldbsuite/test/make/dylib.h](#rocm-openmp-extrasllvm-projectlldbpackagespythonlldbsuitetestmakedylibh)
 - [rocm-openmp-extras/llvm-project/lld/ELF/Config.h](#rocm-openmp-extrasllvm-projectlldelfconfigh)
 - [rocm-openmp-extras/llvm-project/llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c](#rocm-openmp-extrasllvm-projectllvmlibexecutionengineinteljiteventsjitprofilingc)
 - [rocm-openmp-extras/llvm-project/libcxx/src/include/refstring.h](#rocm-openmp-extrasllvm-projectlibcxxsrcincluderefstringh)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.h](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_platform_limits_netbsdh)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux.h](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_linuxh)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.h](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_platform_limits_freebsdh)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/msan/dtls_test.c](#rocm-openmp-extrasllvm-projectcompiler-rttestmsandtls_testc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/global-registration.c](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcasesposixglobal-registrationc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/stress_dtls.c](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcaseslinuxstress_dtlsc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcaseslinuxdlopen-mixed-c-cxxc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/dtls.c](#rocm-openmp-extrasllvm-projectcompiler-rttesttsandtlsc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Posix/gcov-dlopen.c](#rocm-openmp-extrasllvm-projectcompiler-rttestprofileposixgcov-dlopenc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c](#rocm-openmp-extrasllvm-projectcompiler-rttestprofileinputsinstrprof-dlopen-mainc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c](#rocm-openmp-extrasllvm-projectcompiler-rttestprofileinputsinstrprof-value-prof-visibilityc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c](#rocm-openmp-extrasllvm-projectcompiler-rttestprofileinputsinstrprof-dlopen-dlclose-mainc)
 - [rocm-openmp-extras/llvm-project/polly/tools/GPURuntime/GPUJIT.c](#rocm-openmp-extrasllvm-projectpollytoolsgpuruntimegpujitc)
 - [rocm-openmp-extras/llvm-project/libcxxabi/src/include/refstring.h](#rocm-openmp-extrasllvm-projectlibcxxabisrcincluderefstringh)

### rocm-openmp-extras/llvm-project/openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h

```c

{% raw %}
352 | void* dlopen(const char*, int) __attribute__((weak));
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/libomptarget/test/offloading/dynamic_module_load.c

```c

{% raw %}
18 |   void *Handle = dlopen(argv[1], RTLD_NOW);
22 |     printf("dlopen() failed: %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/tools/multiplex/ompt-multiplex.h

```c

{% raw %}
1057 |       void *h = dlopen(tool_libs_buffer + progress, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/include/lldb/Target/Process.h

```c

{% raw %}
2834 |   std::unique_ptr<UtilityFunction> m_dlopen_utility_func_up;
2835 |   llvm::once_flag m_dlopen_utility_func_flag_once;
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/dlopen_other_executable/TestDlopenOtherExecutable.py

```python

{% raw %}
28 |             "// break after dlopen", lldb.SBFileSpec("main.c"))
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/dlopen_other_executable/main.c

```c

{% raw %}
6 |   int h = dlopen("other", RTLD_LAZY);
7 |   assert(h && "dlopen failed?");
8 |   return i; // break after dlopen
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/load_using_paths/TestLoadUsingPaths.py

```python

{% raw %}
40 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/load_unload/TestLoadUnload.py

```python

{% raw %}
95 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
152 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
309 |         """Test breakpoint by name works correctly with dlopen'ing."""
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c

```c

{% raw %}
9 |     void *handle = dlopen ("com.apple.sbd.xpc/com.apple.sbd", RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/packages/Python/lldbsuite/test/make/dylib.h

```c

{% raw %}
38 |   return dlopen(fullname, RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lld/ELF/Config.h

```c

{% raw %}
226 |   bool zNodlopen;
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

```c

{% raw %}
347 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
356 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/libcxx/src/include/refstring.h

```c

{% raw %}
46 |     void* handle = dlopen("/usr/lib/libstdc++.6.dylib", RTLD_NOLOAD);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.h

```c

{% raw %}
22 | void *__sanitizer_get_link_map_by_dlopen_handle(void *handle);
24 |     (link_map *)__sanitizer_get_link_map_by_dlopen_handle(handle)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux.h

```c

{% raw %}
26 | struct link_map;  // Opaque type returned by dlopen().
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.h

```c

{% raw %}
27 | void *__sanitizer_get_link_map_by_dlopen_handle(void *handle);
29 |   (link_map *)__sanitizer_get_link_map_by_dlopen_handle(handle)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/msan/dtls_test.c

```c

{% raw %}
52 |   void *handle = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/global-registration.c

```c

{% raw %}
39 |     void *handle = dlopen(libpath, RTLD_NOW);
41 |       fprintf(stderr, "dlopen: %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/stress_dtls.c

```c

{% raw %}
84 |     void *handle = dlopen(buf, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c

```c

{% raw %}
36 |   void *handle = dlopen(argv[1], RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/dtls.c

```c

{% raw %}
37 |   void *handle = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Posix/gcov-dlopen.c

```c

{% raw %}
39 |   void *f1_handle = dlopen("func1.so", RTLD_LAZY | RTLD_GLOBAL);
46 |   void *f2_handle = dlopen("func2.so", RTLD_LAZY | RTLD_GLOBAL);
57 |   void *f3_handle = dlopen("func3.so", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c

```c

{% raw %}
14 |   void *f1_handle = dlopen(DLOPEN_FUNC_DIR"/func.shared", DLOPEN_FLAGS);
27 |   void *f2_handle = dlopen(DLOPEN_FUNC_DIR"/func2.shared", DLOPEN_FLAGS);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c

```c

{% raw %}
29 |   void *Handle = dlopen(DLOPEN_FUNC_DIR "/func.shared", RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c

```c

{% raw %}
6 |   void *f1_handle = dlopen("func.shared", RTLD_LAZY | RTLD_GLOBAL);
19 |   void *f2_handle = dlopen("func2.shared", RTLD_LAZY | RTLD_GLOBAL);
33 |   void *f3_handle = dlopen("func3.shared", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/polly/tools/GPURuntime/GPUJIT.c

```c

{% raw %}
223 |   HandleOpenCLBeignet = dlopen("/usr/local/lib/beignet/libcl.so", RTLD_LAZY);
224 |   HandleOpenCL = dlopen("libOpenCL.so", RTLD_LAZY);
1047 |   HandleCuda = dlopen("libcuda.so", RTLD_LAZY);
1053 |   HandleCudaRT = dlopen("libcudart.so", RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/libcxxabi/src/include/refstring.h

```c

{% raw %}
50 |     void* handle = dlopen("/usr/lib/libstdc++.6.dylib", RTLD_NOLOAD);
{% endraw %}

```