---
name: "intel-llvm"
layout: package
next_package: nicstat
previous_package: r-reticulate
languages: ['python', 'c']
---
## ycl
144 / 102229 files match

 - [openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h](#openmpruntimesrcthirdpartyittnotifyittnotify_configh)
 - [openmp/libomptarget/test/offloading/dynamic_module_load.c](#openmplibomptargettestoffloadingdynamic_module_loadc)
 - [openmp/tools/multiplex/ompt-multiplex.h](#openmptoolsmultiplexompt-multiplexh)
 - [lldb/include/lldb/Target/Process.h](#lldbincludelldbtargetprocessh)
 - [lldb/test/API/functionalities/dlopen_other_executable/TestDlopenOtherExecutable.py](#lldbtestapifunctionalitiesdlopen_other_executabletestdlopenotherexecutablepy)
 - [lldb/test/API/functionalities/dlopen_other_executable/main.c](#lldbtestapifunctionalitiesdlopen_other_executablemainc)
 - [lldb/test/API/functionalities/load_using_paths/TestLoadUsingPaths.py](#lldbtestapifunctionalitiesload_using_pathstestloadusingpathspy)
 - [lldb/test/API/functionalities/load_unload/TestLoadUnload.py](#lldbtestapifunctionalitiesload_unloadtestloadunloadpy)
 - [lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c](#lldbtestapimacosxfind-dsymbundle-with-dot-in-filenamemainc)
 - [lldb/packages/Python/lldbsuite/test/make/dylib.h](#lldbpackagespythonlldbsuitetestmakedylibh)
 - [lld/ELF/Config.h](#lldelfconfigh)
 - [llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c](#llvmlibexecutionengineinteljiteventsjitprofilingc)
 - [libcxx/src/include/refstring.h](#libcxxsrcincluderefstringh)
 - [compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.h](#compiler-rtlibsanitizer_commonsanitizer_platform_limits_netbsdh)
 - [compiler-rt/lib/sanitizer_common/sanitizer_linux.h](#compiler-rtlibsanitizer_commonsanitizer_linuxh)
 - [compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.h](#compiler-rtlibsanitizer_commonsanitizer_platform_limits_freebsdh)
 - [compiler-rt/test/msan/dtls_test.c](#compiler-rttestmsandtls_testc)
 - [compiler-rt/test/asan/TestCases/Posix/global-registration.c](#compiler-rttestasantestcasesposixglobal-registrationc)
 - [compiler-rt/test/asan/TestCases/Linux/stress_dtls.c](#compiler-rttestasantestcaseslinuxstress_dtlsc)
 - [compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c](#compiler-rttestasantestcaseslinuxdlopen-mixed-c-cxxc)
 - [compiler-rt/test/memprof/TestCases/stress_dtls.c](#compiler-rttestmemproftestcasesstress_dtlsc)
 - [compiler-rt/test/tsan/dtls.c](#compiler-rttesttsandtlsc)
 - [compiler-rt/test/profile/Posix/gcov-dlopen.c](#compiler-rttestprofileposixgcov-dlopenc)
 - [compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c](#compiler-rttestprofileinputsinstrprof-dlopen-mainc)
 - [compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c](#compiler-rttestprofileinputsinstrprof-value-prof-visibilityc)
 - [compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c](#compiler-rttestprofileinputsinstrprof-dlopen-dlclose-mainc)
 - [polly/tools/GPURuntime/GPUJIT.c](#pollytoolsgpuruntimegpujitc)

### openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h

```c

{% raw %}
352 | void* dlopen(const char*, int) __attribute__((weak));
{% endraw %}

```
### openmp/libomptarget/test/offloading/dynamic_module_load.c

```c

{% raw %}
18 |   void *Handle = dlopen(argv[1], RTLD_NOW);
22 |     printf("dlopen() failed: %s\n", dlerror());
{% endraw %}

```
### openmp/tools/multiplex/ompt-multiplex.h

```c

{% raw %}
1057 |       void *h = dlopen(tool_libs_buffer + progress, RTLD_LAZY);
{% endraw %}

```
### lldb/include/lldb/Target/Process.h

```c

{% raw %}
2846 |   std::unique_ptr<UtilityFunction> m_dlopen_utility_func_up;
2847 |   llvm::once_flag m_dlopen_utility_func_flag_once;
{% endraw %}

```
### lldb/test/API/functionalities/dlopen_other_executable/TestDlopenOtherExecutable.py

```python

{% raw %}
31 |             "// break after dlopen", lldb.SBFileSpec("main.c"))
{% endraw %}

```
### lldb/test/API/functionalities/dlopen_other_executable/main.c

```c

{% raw %}
6 |   int h = dlopen("other", RTLD_LAZY);
7 |   assert(h && "dlopen failed?");
8 |   return i; // break after dlopen
{% endraw %}

```
### lldb/test/API/functionalities/load_using_paths/TestLoadUsingPaths.py

```python

{% raw %}
39 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
{% endraw %}

```
### lldb/test/API/functionalities/load_unload/TestLoadUnload.py

```python

{% raw %}
94 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
149 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
301 |         """Test breakpoint by name works correctly with dlopen'ing."""
{% endraw %}

```
### lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c

```c

{% raw %}
10 |     void *handle = dlopen ("com.apple.sbd.xpc/com.apple.sbd", RTLD_NOW);
{% endraw %}

```
### lldb/packages/Python/lldbsuite/test/make/dylib.h

```c

{% raw %}
38 |   return dlopen(fullname, RTLD_NOW);
{% endraw %}

```
### lld/ELF/Config.h

```c

{% raw %}
233 |   bool zNodlopen;
{% endraw %}

```
### llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

```c

{% raw %}
347 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
356 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
{% endraw %}

```
### libcxx/src/include/refstring.h

```c

{% raw %}
59 |     void* handle = dlopen("/usr/lib/libstdc++.6.dylib", RTLD_NOLOAD);
{% endraw %}

```
### compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.h

```c

{% raw %}
22 | void *__sanitizer_get_link_map_by_dlopen_handle(void *handle);
24 |   (link_map *)__sanitizer_get_link_map_by_dlopen_handle(handle)
{% endraw %}

```
### compiler-rt/lib/sanitizer_common/sanitizer_linux.h

```c

{% raw %}
25 | struct link_map;  // Opaque type returned by dlopen().
{% endraw %}

```
### compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.h

```c

{% raw %}
27 | void *__sanitizer_get_link_map_by_dlopen_handle(void *handle);
29 |   (link_map *)__sanitizer_get_link_map_by_dlopen_handle(handle)
{% endraw %}

```
### compiler-rt/test/msan/dtls_test.c

```c

{% raw %}
52 |   void *handle = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### compiler-rt/test/asan/TestCases/Posix/global-registration.c

```c

{% raw %}
39 |     void *handle = dlopen(libpath, RTLD_NOW);
41 |       fprintf(stderr, "dlopen: %s\n", dlerror());
{% endraw %}

```
### compiler-rt/test/asan/TestCases/Linux/stress_dtls.c

```c

{% raw %}
84 |     void *handle = dlopen(buf, RTLD_LAZY);
{% endraw %}

```
### compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c

```c

{% raw %}
36 |   void *handle = dlopen(argv[1], RTLD_LAZY);
{% endraw %}

```
### compiler-rt/test/memprof/TestCases/stress_dtls.c

```c

{% raw %}
79 |     void *handle = dlopen(buf, RTLD_LAZY);
{% endraw %}

```
### compiler-rt/test/tsan/dtls.c

```c

{% raw %}
37 |   void *handle = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### compiler-rt/test/profile/Posix/gcov-dlopen.c

```c

{% raw %}
39 |   void *f1_handle = dlopen("func1.so", RTLD_LAZY | RTLD_GLOBAL);
46 |   void *f2_handle = dlopen("func2.so", RTLD_LAZY | RTLD_GLOBAL);
57 |   void *f3_handle = dlopen("func3.so", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c

```c

{% raw %}
14 |   void *f1_handle = dlopen(DLOPEN_FUNC_DIR"/func.shared", DLOPEN_FLAGS);
27 |   void *f2_handle = dlopen(DLOPEN_FUNC_DIR"/func2.shared", DLOPEN_FLAGS);
{% endraw %}

```
### compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c

```c

{% raw %}
29 |   void *Handle = dlopen(DLOPEN_FUNC_DIR "/func.shared", RTLD_NOW);
{% endraw %}

```
### compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c

```c

{% raw %}
6 |   void *f1_handle = dlopen("func.shared", RTLD_LAZY | RTLD_GLOBAL);
19 |   void *f2_handle = dlopen("func2.shared", RTLD_LAZY | RTLD_GLOBAL);
33 |   void *f3_handle = dlopen("func3.shared", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### polly/tools/GPURuntime/GPUJIT.c

```c

{% raw %}
223 |   HandleOpenCLBeignet = dlopen("/usr/local/lib/beignet/libcl.so", RTLD_LAZY);
224 |   HandleOpenCL = dlopen("libOpenCL.so", RTLD_LAZY);
1047 |   HandleCuda = dlopen("libcuda.so", RTLD_LAZY);
1053 |   HandleCudaRT = dlopen("libcudart.so", RTLD_LAZY);
{% endraw %}

```