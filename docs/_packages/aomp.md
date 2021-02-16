---
name: "aomp"
layout: package
next_package: meson
previous_package: ilmbase
languages: ['python', 'c']
---
## 3.10.0
139 / 99671 files match, 26 filtered matches.

 - [aomp-dir/amd-llvm-project/openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h](#aomp-diramd-llvm-projectopenmpruntimesrcthirdpartyittnotifyittnotify_configh)
 - [aomp-dir/amd-llvm-project/openmp/libompd/gdb-plugin/ompdModule.c](#aomp-diramd-llvm-projectopenmplibompdgdb-pluginompdmodulec)
 - [aomp-dir/amd-llvm-project/openmp/libompd/gdb-plugin/ompd/ompd.py](#aomp-diramd-llvm-projectopenmplibompdgdb-pluginompdompdpy)
 - [aomp-dir/amd-llvm-project/openmp/libomptarget/test/offloading/dynamic_module_load.c](#aomp-diramd-llvm-projectopenmplibomptargettestoffloadingdynamic_module_loadc)
 - [aomp-dir/amd-llvm-project/openmp/tools/multiplex/ompt-multiplex.h](#aomp-diramd-llvm-projectopenmptoolsmultiplexompt-multiplexh)
 - [aomp-dir/amd-llvm-project/lldb/include/lldb/Target/Process.h](#aomp-diramd-llvm-projectlldbincludelldbtargetprocessh)
 - [aomp-dir/amd-llvm-project/lldb/test/API/functionalities/load_using_paths/TestLoadUsingPaths.py](#aomp-diramd-llvm-projectlldbtestapifunctionalitiesload_using_pathstestloadusingpathspy)
 - [aomp-dir/amd-llvm-project/lldb/test/API/functionalities/load_unload/TestLoadUnload.py](#aomp-diramd-llvm-projectlldbtestapifunctionalitiesload_unloadtestloadunloadpy)
 - [aomp-dir/amd-llvm-project/lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c](#aomp-diramd-llvm-projectlldbtestapimacosxfind-dsymbundle-with-dot-in-filenamemainc)
 - [aomp-dir/amd-llvm-project/lldb/packages/Python/lldbsuite/test/make/dylib.h](#aomp-diramd-llvm-projectlldbpackagespythonlldbsuitetestmakedylibh)
 - [aomp-dir/amd-llvm-project/lld/ELF/Config.h](#aomp-diramd-llvm-projectlldelfconfigh)
 - [aomp-dir/amd-llvm-project/llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c](#aomp-diramd-llvm-projectllvmlibexecutionengineinteljiteventsjitprofilingc)
 - [aomp-dir/amd-llvm-project/libcxx/src/include/refstring.h](#aomp-diramd-llvm-projectlibcxxsrcincluderefstringh)
 - [aomp-dir/amd-llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.h](#aomp-diramd-llvm-projectcompiler-rtlibsanitizer_commonsanitizer_platform_limits_netbsdh)
 - [aomp-dir/amd-llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux.h](#aomp-diramd-llvm-projectcompiler-rtlibsanitizer_commonsanitizer_linuxh)
 - [aomp-dir/amd-llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.h](#aomp-diramd-llvm-projectcompiler-rtlibsanitizer_commonsanitizer_platform_limits_freebsdh)
 - [aomp-dir/amd-llvm-project/compiler-rt/test/msan/dtls_test.c](#aomp-diramd-llvm-projectcompiler-rttestmsandtls_testc)
 - [aomp-dir/amd-llvm-project/compiler-rt/test/asan/TestCases/Posix/global-registration.c](#aomp-diramd-llvm-projectcompiler-rttestasantestcasesposixglobal-registrationc)
 - [aomp-dir/amd-llvm-project/compiler-rt/test/asan/TestCases/Linux/stress_dtls.c](#aomp-diramd-llvm-projectcompiler-rttestasantestcaseslinuxstress_dtlsc)
 - [aomp-dir/amd-llvm-project/compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c](#aomp-diramd-llvm-projectcompiler-rttestasantestcaseslinuxdlopen-mixed-c-cxxc)
 - [aomp-dir/amd-llvm-project/compiler-rt/test/tsan/dtls.c](#aomp-diramd-llvm-projectcompiler-rttesttsandtlsc)
 - [aomp-dir/amd-llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c](#aomp-diramd-llvm-projectcompiler-rttestprofileinputsinstrprof-dlopen-mainc)
 - [aomp-dir/amd-llvm-project/compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c](#aomp-diramd-llvm-projectcompiler-rttestprofileinputsinstrprof-value-prof-visibilityc)
 - [aomp-dir/amd-llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c](#aomp-diramd-llvm-projectcompiler-rttestprofileinputsinstrprof-dlopen-dlclose-mainc)
 - [aomp-dir/amd-llvm-project/polly/tools/GPURuntime/GPUJIT.c](#aomp-diramd-llvm-projectpollytoolsgpuruntimegpujitc)
 - [aomp-dir/amd-llvm-project/libcxxabi/src/include/refstring.h](#aomp-diramd-llvm-projectlibcxxabisrcincluderefstringh)

### aomp-dir/amd-llvm-project/openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h

```c

{% raw %}
352 | void* dlopen(const char*, int) __attribute__((weak));
{% endraw %}

```
### aomp-dir/amd-llvm-project/openmp/libompd/gdb-plugin/ompdModule.c

```c

{% raw %}
321 | 	ompd_library = dlopen(name, RTLD_LAZY);
1168 | 	{"ompd_open", ompd_open, METH_VARARGS, "Execute dlopen, return OMPD version."},
{% endraw %}

```
### aomp-dir/amd-llvm-project/openmp/libompd/gdb-plugin/ompd/ompd.py

```python

{% raw %}
58 | 					pass # It's ok to fail on dlopen
{% endraw %}

```
### aomp-dir/amd-llvm-project/openmp/libomptarget/test/offloading/dynamic_module_load.c

```c

{% raw %}
17 |   void *Handle = dlopen(argv[1], RTLD_NOW);
21 |     printf("dlopen() failed: %s\n", dlerror());
{% endraw %}

```
### aomp-dir/amd-llvm-project/openmp/tools/multiplex/ompt-multiplex.h

```c

{% raw %}
1057 |       void *h = dlopen(tool_libs_buffer + progress, RTLD_LAZY);
{% endraw %}

```
### aomp-dir/amd-llvm-project/lldb/include/lldb/Target/Process.h

```c

{% raw %}
2834 |   std::unique_ptr<UtilityFunction> m_dlopen_utility_func_up;
2835 |   llvm::once_flag m_dlopen_utility_func_flag_once;
{% endraw %}

```
### aomp-dir/amd-llvm-project/lldb/test/API/functionalities/load_using_paths/TestLoadUsingPaths.py

```python

{% raw %}
40 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
{% endraw %}

```
### aomp-dir/amd-llvm-project/lldb/test/API/functionalities/load_unload/TestLoadUnload.py

```python

{% raw %}
95 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
152 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
309 |         """Test breakpoint by name works correctly with dlopen'ing."""
{% endraw %}

```
### aomp-dir/amd-llvm-project/lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c

```c

{% raw %}
9 |     void *handle = dlopen ("com.apple.sbd.xpc/com.apple.sbd", RTLD_NOW);
{% endraw %}

```
### aomp-dir/amd-llvm-project/lldb/packages/Python/lldbsuite/test/make/dylib.h

```c

{% raw %}
38 |   return dlopen(fullname, RTLD_NOW);
{% endraw %}

```
### aomp-dir/amd-llvm-project/lld/ELF/Config.h

```c

{% raw %}
226 |   bool zNodlopen;
{% endraw %}

```
### aomp-dir/amd-llvm-project/llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

```c

{% raw %}
347 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
356 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
{% endraw %}

```
### aomp-dir/amd-llvm-project/libcxx/src/include/refstring.h

```c

{% raw %}
46 |     void* handle = dlopen("/usr/lib/libstdc++.6.dylib", RTLD_NOLOAD);
{% endraw %}

```
### aomp-dir/amd-llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.h

```c

{% raw %}
22 | void *__sanitizer_get_link_map_by_dlopen_handle(void *handle);
24 |     (link_map *)__sanitizer_get_link_map_by_dlopen_handle(handle)
{% endraw %}

```
### aomp-dir/amd-llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux.h

```c

{% raw %}
26 | struct link_map;  // Opaque type returned by dlopen().
{% endraw %}

```
### aomp-dir/amd-llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.h

```c

{% raw %}
27 | void *__sanitizer_get_link_map_by_dlopen_handle(void *handle);
29 |   (link_map *)__sanitizer_get_link_map_by_dlopen_handle(handle)
{% endraw %}

```
### aomp-dir/amd-llvm-project/compiler-rt/test/msan/dtls_test.c

```c

{% raw %}
52 |   void *handle = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### aomp-dir/amd-llvm-project/compiler-rt/test/asan/TestCases/Posix/global-registration.c

```c

{% raw %}
39 |     void *handle = dlopen(libpath, RTLD_NOW);
41 |       fprintf(stderr, "dlopen: %s\n", dlerror());
{% endraw %}

```
### aomp-dir/amd-llvm-project/compiler-rt/test/asan/TestCases/Linux/stress_dtls.c

```c

{% raw %}
84 |     void *handle = dlopen(buf, RTLD_LAZY);
{% endraw %}

```
### aomp-dir/amd-llvm-project/compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c

```c

{% raw %}
36 |   void *handle = dlopen(argv[1], RTLD_LAZY);
{% endraw %}

```
### aomp-dir/amd-llvm-project/compiler-rt/test/tsan/dtls.c

```c

{% raw %}
37 |   void *handle = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### aomp-dir/amd-llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c

```c

{% raw %}
14 |   void *f1_handle = dlopen(DLOPEN_FUNC_DIR"/func.shared", DLOPEN_FLAGS);
27 |   void *f2_handle = dlopen(DLOPEN_FUNC_DIR"/func2.shared", DLOPEN_FLAGS);
{% endraw %}

```
### aomp-dir/amd-llvm-project/compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c

```c

{% raw %}
29 |   void *Handle = dlopen(DLOPEN_FUNC_DIR "/func.shared", RTLD_NOW);
{% endraw %}

```
### aomp-dir/amd-llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c

```c

{% raw %}
6 |   void *f1_handle = dlopen("func.shared", RTLD_LAZY | RTLD_GLOBAL);
19 |   void *f2_handle = dlopen("func2.shared", RTLD_LAZY | RTLD_GLOBAL);
33 |   void *f3_handle = dlopen("func3.shared", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### aomp-dir/amd-llvm-project/polly/tools/GPURuntime/GPUJIT.c

```c

{% raw %}
223 |   HandleOpenCLBeignet = dlopen("/usr/local/lib/beignet/libcl.so", RTLD_LAZY);
224 |   HandleOpenCL = dlopen("libOpenCL.so", RTLD_LAZY);
1047 |   HandleCuda = dlopen("libcuda.so", RTLD_LAZY);
1053 |   HandleCudaRT = dlopen("libcudart.so", RTLD_LAZY);
{% endraw %}

```
### aomp-dir/amd-llvm-project/libcxxabi/src/include/refstring.h

```c

{% raw %}
50 |     void* handle = dlopen("/usr/lib/libstdc++.6.dylib", RTLD_NOLOAD);
{% endraw %}

```