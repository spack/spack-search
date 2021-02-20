---
name: "rocm-openmp-extras"
layout: package
next_package: rocprofiler-dev
previous_package: rocm-opencl
languages: ['python', 'c']
---
## 4.0.0
136 / 100137 files match, 27 filtered matches.

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
349 | }
350 | #endif /* ITT_SIMPLE_INIT */
351 | 
352 | void* dlopen(const char*, int) __attribute__((weak));
353 | void* dlsym(void*, const char*) __attribute__((weak));
354 | int dlclose(void*) __attribute__((weak));
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/libomptarget/test/offloading/dynamic_module_load.c

```c

{% raw %}
15 | #include <dlfcn.h>
16 | #include <stdio.h>
17 | int main(int argc, char **argv) {
18 |   void *Handle = dlopen(argv[1], RTLD_NOW);
19 |   int (*Foo)(void);
20 | 
21 |   if (Handle == NULL) {
22 |     printf("dlopen() failed: %s\n", dlerror());
23 |     return 1;
24 |   }
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/tools/multiplex/ompt-multiplex.h

```c

{% raw %}
1054 |         tmp_progress++;
1055 |       if (tmp_progress < strlen(tool_libs))
1056 |         tool_libs_buffer[tmp_progress] = 0;
1057 |       void *h = dlopen(tool_libs_buffer + progress, RTLD_LAZY);
1058 |       if (h) {
1059 |         client_start_tool =
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/include/lldb/Target/Process.h

```c

{% raw %}
2831 | 
2832 |   enum { eCanJITDontKnow = 0, eCanJITYes, eCanJITNo } m_can_jit;
2833 | 
2834 |   std::unique_ptr<UtilityFunction> m_dlopen_utility_func_up;
2835 |   llvm::once_flag m_dlopen_utility_func_flag_once;
2836 | 
2837 |   size_t RemoveBreakpointOpcodesFromBuffer(lldb::addr_t addr, size_t size,
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/dlopen_other_executable/TestDlopenOtherExecutable.py

```python

{% raw %}
25 | 
26 |         # Continue so that dlopen is called.
27 |         breakpoint = self.target().BreakpointCreateBySourceRegex(
28 |             "// break after dlopen", lldb.SBFileSpec("main.c"))
29 |         self.assertNotEqual(breakpoint.GetNumResolvedLocations(), 0)
30 |         stopped_threads = lldbutil.continue_to_breakpoint(self.process(), breakpoint)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/dlopen_other_executable/main.c

```c

{% raw %}
3 | int main() {
4 |   int i = 0; // break here
5 |   // dlopen the 'other' test executable.
6 |   int h = dlopen("other", RTLD_LAZY);
7 |   assert(h && "dlopen failed?");
8 |   return i; // break after dlopen
9 | }
10 | 
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/load_using_paths/TestLoadUsingPaths.py

```python

{% raw %}
37 | 
38 |     @skipIfFreeBSD  # llvm.org/pr14424 - missing FreeBSD Makefiles/testcase support
39 |     @not_remote_testsuite_ready
40 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
41 |     @expectedFlakeyNetBSD
42 |     @expectedFailureAll(oslist=["linux"], archs=['arm'], bugnumber="llvm.org/pr45894")
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/load_unload/TestLoadUnload.py

```python

{% raw %}
92 |     @expectedFailureAll(oslist=["linux"])
93 |     @skipIfFreeBSD  # llvm.org/pr14424 - missing FreeBSD Makefiles/testcase support
94 |     @not_remote_testsuite_ready
95 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
96 |     @expectedFailureNetBSD
97 |     @skipIfReproducer # VFS is a snapshot.
149 |     @expectedFailureAll(oslist=["linux"])
150 |     @skipIfFreeBSD  # llvm.org/pr14424 - missing FreeBSD Makefiles/testcase support
151 |     @expectedFailureAndroid  # wrong source file shows up for hidden library
152 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
153 |     @skipIfDarwinEmbedded
154 |     @expectedFailureNetBSD
306 |         self.run_load_unload()
307 | 
308 |     def run_load_unload(self):
309 |         """Test breakpoint by name works correctly with dlopen'ing."""
310 |         self.copy_shlibs_to_remote()
311 | 
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c

```c

{% raw %}
6 | int main()
7 | {
8 | 
9 |     void *handle = dlopen ("com.apple.sbd.xpc/com.apple.sbd", RTLD_NOW);
10 |     if (handle)
11 |     {
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/packages/Python/lldbsuite/test/make/dylib.h

```c

{% raw %}
35 | #ifdef _WIN32
36 |   return LoadLibraryA(fullname);
37 | #else
38 |   return dlopen(fullname, RTLD_NOW);
39 | #endif
40 | }
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lld/ELF/Config.h

```c

{% raw %}
223 |   bool zKeepTextSectionPrefix;
224 |   bool zNodefaultlib;
225 |   bool zNodelete;
226 |   bool zNodlopen;
227 |   bool zNow;
228 |   bool zOrigin;
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

```c

{% raw %}
344 |     if (dllName)
345 |     {
346 |         /* Try to load the dll from the PATH... */
347 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
348 |     }
349 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
353 | #if ITT_PLATFORM==ITT_PLATFORM_WIN
354 |         m_libHandle = LoadLibraryA(DEFAULT_DLLNAME);
355 | #else  /* ITT_PLATFORM==ITT_PLATFORM_WIN */
356 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
357 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
358 |     }
{% endraw %}

```
### rocm-openmp-extras/llvm-project/libcxx/src/include/refstring.h

```c

{% raw %}
43 | inline
44 | const char* compute_gcc_empty_string_storage() _NOEXCEPT
45 | {
46 |     void* handle = dlopen("/usr/lib/libstdc++.6.dylib", RTLD_NOLOAD);
47 |     if (handle == nullptr)
48 |         return nullptr;
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.h

```c

{% raw %}
19 | #include "sanitizer_platform.h"
20 | 
21 | namespace __sanitizer {
22 | void *__sanitizer_get_link_map_by_dlopen_handle(void *handle);
23 | # define GET_LINK_MAP_BY_DLOPEN_HANDLE(handle) \
24 |     (link_map *)__sanitizer_get_link_map_by_dlopen_handle(handle)
25 | 
26 | extern unsigned struct_utsname_sz;
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux.h

```c

{% raw %}
23 | #include "sanitizer_platform_limits_solaris.h"
24 | #include "sanitizer_posix.h"
25 | 
26 | struct link_map;  // Opaque type returned by dlopen().
27 | struct utsname;
28 | 
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.h

```c

{% raw %}
24 | #include <sys/_types.h>
25 | 
26 | namespace __sanitizer {
27 | void *__sanitizer_get_link_map_by_dlopen_handle(void *handle);
28 | #define GET_LINK_MAP_BY_DLOPEN_HANDLE(handle) \
29 |   (link_map *)__sanitizer_get_link_map_by_dlopen_handle(handle)
30 | 
31 | extern unsigned struct_utsname_sz;
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/msan/dtls_test.c

```c

{% raw %}
49 |   snprintf(path, sizeof(path), "%s-so.so", argv[0]);
50 |   int i;
51 | 
52 |   void *handle = dlopen(path, RTLD_LAZY);
53 |   if (!handle) fprintf(stderr, "%s\n", dlerror());
54 |   assert(handle != 0);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/global-registration.c

```c

{% raw %}
36 |     char *libpath = malloc(strlen(argv[0]) + strlen(libsuffix) + 1);
37 |     sprintf(libpath, "%s%s", argv[0], libsuffix);
38 |     
39 |     void *handle = dlopen(libpath, RTLD_NOW);
40 |     if (!handle) {
41 |       fprintf(stderr, "dlopen: %s\n", dlerror());
42 |       return 1;
43 |     }
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/stress_dtls.c

```c

{% raw %}
81 |   for (lib = 0; lib < num_libs; lib++) {
82 |     char buf[4096];
83 |     snprintf(buf, sizeof(buf), "%s-f%d.so", argv[0], lib);
84 |     void *handle = dlopen(buf, RTLD_LAZY);
85 |     if (!handle) {
86 |       fprintf(stderr, "%s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c

```c

{% raw %}
33 | 
34 | int main(int argc, char **argv) {
35 |   int (*bar)(void);
36 |   void *handle = dlopen(argv[1], RTLD_LAZY);
37 |   assert(handle);
38 |   bar = dlsym(handle, "bar");
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/dtls.c

```c

{% raw %}
34 |   char path[4096];
35 |   snprintf(path, sizeof(path), "%s-so.so", argv[0]);
36 | 
37 |   void *handle = dlopen(path, RTLD_LAZY);
38 |   if (!handle) fprintf(stderr, "%s\n", dlerror());
39 |   assert(handle != 0);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Posix/gcov-dlopen.c

```c

{% raw %}
36 | #include <stdlib.h>
37 | 
38 | int main(int argc, char *argv[]) {
39 |   void *f1_handle = dlopen("func1.so", RTLD_LAZY | RTLD_GLOBAL);
40 |   if (f1_handle == NULL)
41 |     return fprintf(stderr, "unable to open 'func1.so': %s\n", dlerror());
43 |   if (func1 == NULL)
44 |     return fprintf(stderr, "unable to lookup symbol 'func1': %s\n", dlerror());
45 | 
46 |   void *f2_handle = dlopen("func2.so", RTLD_LAZY | RTLD_GLOBAL);
47 |   if (f2_handle == NULL)
48 |     return fprintf(stderr, "unable to open 'func2.so': %s\n", dlerror());
54 | #ifdef USE_LIB3
55 | // CHECK:          -: [[#@LINE+2]]:  void *f3_handle
56 | // LIB3:           1: [[#@LINE+1]]:  void *f3_handle
57 |   void *f3_handle = dlopen("func3.so", RTLD_LAZY | RTLD_GLOBAL);
58 |   if (f3_handle == NULL)
59 |     return fprintf(stderr, "unable to open 'func3.so': %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c

```c

{% raw %}
11 | int main(int argc, char *argv[]) {
12 | #ifdef DLOPEN_FUNC_DIR
13 |   dlerror();
14 |   void *f1_handle = dlopen(DLOPEN_FUNC_DIR"/func.shared", DLOPEN_FLAGS);
15 |   if (f1_handle == NULL) {
16 |     fprintf(stderr, "unable to open '" DLOPEN_FUNC_DIR "/func.shared': %s\n",
24 |     return EXIT_FAILURE;
25 |   }
26 | 
27 |   void *f2_handle = dlopen(DLOPEN_FUNC_DIR"/func2.shared", DLOPEN_FLAGS);
28 |   if (f2_handle == NULL) {
29 |     fprintf(stderr, "unable to open '" DLOPEN_FUNC_DIR "/func2.shared': %s\n",
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c

```c

{% raw %}
26 |   __llvm_profile_reset_counters();
27 | 
28 | #ifdef DLOPEN_FUNC_DIR
29 |   void *Handle = dlopen(DLOPEN_FUNC_DIR "/func.shared", RTLD_NOW);
30 |   if (!Handle) {
31 |     fprintf(stderr, "unable to open '" DLOPEN_FUNC_DIR "/func.shared': %s\n",
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c

```c

{% raw %}
3 | 
4 | int main(int argc, char *argv[]) {
5 |   dlerror();
6 |   void *f1_handle = dlopen("func.shared", RTLD_LAZY | RTLD_GLOBAL);
7 |   if (f1_handle == NULL) {
8 |     fprintf(stderr, "unable to open 'func.shared': %s\n", dlerror());
16 |   }
17 | 
18 |   dlerror();
19 |   void *f2_handle = dlopen("func2.shared", RTLD_LAZY | RTLD_GLOBAL);
20 |   if (f2_handle == NULL) {
21 |     fprintf(stderr, "unable to open 'func2.shared': %s\n", dlerror());
30 |   func2();
31 | 
32 | #ifdef USE_LIB3
33 |   void *f3_handle = dlopen("func3.shared", RTLD_LAZY | RTLD_GLOBAL);
34 |   if (f3_handle == NULL) {
35 |     fprintf(stderr, "unable to open 'func3.shared': %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/polly/tools/GPURuntime/GPUJIT.c

```c

{% raw %}
220 | }
221 | 
222 | static int initialDeviceAPILibrariesCL() {
223 |   HandleOpenCLBeignet = dlopen("/usr/local/lib/beignet/libcl.so", RTLD_LAZY);
224 |   HandleOpenCL = dlopen("libOpenCL.so", RTLD_LAZY);
225 |   if (!HandleOpenCL) {
226 |     fprintf(stderr, "Cannot open library: %s. \n", dlerror());
1044 | }
1045 | 
1046 | static int initialDeviceAPILibrariesCUDA() {
1047 |   HandleCuda = dlopen("libcuda.so", RTLD_LAZY);
1048 |   if (!HandleCuda) {
1049 |     fprintf(stderr, "Cannot open library: %s. \n", dlerror());
1050 |     return 0;
1051 |   }
1052 | 
1053 |   HandleCudaRT = dlopen("libcudart.so", RTLD_LAZY);
1054 |   if (!HandleCudaRT) {
1055 |     fprintf(stderr, "Cannot open library: %s. \n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/libcxxabi/src/include/refstring.h

```c

{% raw %}
47 | inline
48 | const char* compute_gcc_empty_string_storage() _NOEXCEPT
49 | {
50 |     void* handle = dlopen("/usr/lib/libstdc++.6.dylib", RTLD_NOLOAD);
51 |     if (handle == nullptr)
52 |         return nullptr;
{% endraw %}

```