---
name: "llvm-doe"
layout: package
next_package: llvm-openmp
previous_package: llvm-amdgpu
languages: ['python', 'c']
---
## pragma-omp-tile
134 / 92269 files match, 24 filtered matches.

 - [openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h](#openmpruntimesrcthirdpartyittnotifyittnotify_configh)
 - [openmp/libomptarget/test/offloading/dynamic_module_load.c](#openmplibomptargettestoffloadingdynamic_module_loadc)
 - [openmp/tools/multiplex/ompt-multiplex.h](#openmptoolsmultiplexompt-multiplexh)
 - [lldb/include/lldb/Target/Process.h](#lldbincludelldbtargetprocessh)
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
 - [compiler-rt/test/tsan/dtls.c](#compiler-rttesttsandtlsc)
 - [compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c](#compiler-rttestprofileinputsinstrprof-dlopen-mainc)
 - [compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c](#compiler-rttestprofileinputsinstrprof-value-prof-visibilityc)
 - [compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c](#compiler-rttestprofileinputsinstrprof-dlopen-dlclose-mainc)
 - [polly/tools/GPURuntime/GPUJIT.c](#pollytoolsgpuruntimegpujitc)
 - [libcxxabi/src/include/refstring.h](#libcxxabisrcincluderefstringh)

### openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h

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
### openmp/libomptarget/test/offloading/dynamic_module_load.c

```c

{% raw %}
14 | #include <dlfcn.h>
15 | #include <stdio.h>
16 | int main(int argc, char **argv) {
17 |   void *Handle = dlopen(argv[1], RTLD_NOW);
18 |   int (*Foo)(void);
19 | 
20 |   if (Handle == NULL) {
21 |     printf("dlopen() failed: %s\n", dlerror());
22 |     return 1;
23 |   }
{% endraw %}

```
### openmp/tools/multiplex/ompt-multiplex.h

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
### lldb/include/lldb/Target/Process.h

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
### lldb/test/API/functionalities/load_using_paths/TestLoadUsingPaths.py

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
### lldb/test/API/functionalities/load_unload/TestLoadUnload.py

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
### lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c

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
### lldb/packages/Python/lldbsuite/test/make/dylib.h

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
### lld/ELF/Config.h

```c

{% raw %}
222 |   bool zKeepTextSectionPrefix;
223 |   bool zNodefaultlib;
224 |   bool zNodelete;
225 |   bool zNodlopen;
226 |   bool zNow;
227 |   bool zOrigin;
{% endraw %}

```
### llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

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
### libcxx/src/include/refstring.h

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
### compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.h

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
### compiler-rt/lib/sanitizer_common/sanitizer_linux.h

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
### compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.h

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
### compiler-rt/test/msan/dtls_test.c

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
### compiler-rt/test/asan/TestCases/Posix/global-registration.c

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
### compiler-rt/test/asan/TestCases/Linux/stress_dtls.c

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
### compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c

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
### compiler-rt/test/tsan/dtls.c

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
### compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c

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
### compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c

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
### compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c

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
### polly/tools/GPURuntime/GPUJIT.c

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
### libcxxabi/src/include/refstring.h

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