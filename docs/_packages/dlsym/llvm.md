---
name: "llvm"
layout: package
next_package: lighttpd
previous_package: kcov
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 11.0.1
117 / 92993 files match, 21 filtered matches.

 - [clang/tools/scan-build-py/libear/ear.c](#clangtoolsscan-build-pylibearearc)
 - [openmp/runtime/src/kmp_ftn_entry.h](#openmpruntimesrckmp_ftn_entryh)
 - [openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h](#openmpruntimesrcthirdpartyittnotifyittnotify_configh)
 - [openmp/libomptarget/test/offloading/dynamic_module_load.c](#openmplibomptargettestoffloadingdynamic_module_loadc)
 - [openmp/tools/multiplex/ompt-multiplex.h](#openmptoolsmultiplexompt-multiplexh)
 - [lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c](#lldbtestapimacosxfind-dsymbundle-with-dot-in-filenamemainc)
 - [llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c](#llvmlibexecutionengineinteljiteventsjitprofilingc)
 - [libcxx/src/include/refstring.h](#libcxxsrcincluderefstringh)
 - [compiler-rt/lib/safestack/safestack_platform.h](#compiler-rtlibsafestacksafestack_platformh)
 - [compiler-rt/lib/builtins/os_version_check.c](#compiler-rtlibbuiltinsos_version_checkc)
 - [compiler-rt/test/msan/dtls_test.c](#compiler-rttestmsandtls_testc)
 - [compiler-rt/test/cfi/cross-dso/util/cfi_stubs.h](#compiler-rttestcficross-dsoutilcfi_stubsh)
 - [compiler-rt/test/asan/TestCases/Posix/global-registration.c](#compiler-rttestasantestcasesposixglobal-registrationc)
 - [compiler-rt/test/asan/TestCases/Linux/stress_dtls.c](#compiler-rttestasantestcaseslinuxstress_dtlsc)
 - [compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c](#compiler-rttestasantestcaseslinuxdlopen-mixed-c-cxxc)
 - [compiler-rt/test/tsan/dtls.c](#compiler-rttesttsandtlsc)
 - [compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c](#compiler-rttestprofileinputsinstrprof-dlopen-mainc)
 - [compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c](#compiler-rttestprofileinputsinstrprof-value-prof-visibilityc)
 - [compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c](#compiler-rttestprofileinputsinstrprof-dlopen-dlclose-mainc)
 - [polly/tools/GPURuntime/GPUJIT.c](#pollytoolsgpuruntimegpujitc)
 - [libcxxabi/src/include/refstring.h](#libcxxabisrcincluderefstringh)

### clang/tools/scan-build-py/libear/ear.c

```c

{% raw %}
53 |         void *from;                                                            \
54 |         TYPE_ to;                                                              \
55 |     } cast;                                                                    \
56 |     if (0 == (cast.from = dlsym(RTLD_NEXT, SYMBOL_))) {                        \
57 |         perror("bear: dlsym");                                                 \
58 |         exit(EXIT_FAILURE);                                                    \
59 |     }                                                                          \
{% endraw %}

```
### openmp/runtime/src/kmp_ftn_entry.h

```c

{% raw %}
944 |   return 0;
945 | #else
946 |   int (*fptr)();
947 |   if ((*(void **)(&fptr) = dlsym(RTLD_DEFAULT, "_Offload_number_of_devices"))) {
948 |     return (*fptr)();
949 |   } else if ((*(void **)(&fptr) = dlsym(RTLD_NEXT, "omp_get_num_devices"))) {
950 |     return (*fptr)();
951 |   } else { // liboffload & libomptarget don't exist
968 |   return KMP_HOST_DEVICE;
969 | #else
970 |   int (*fptr)();
971 |   if ((*(void **)(&fptr) = dlsym(RTLD_NEXT, "omp_get_initial_device"))) {
972 |     return (*fptr)();
973 |   } else { // liboffload & libomptarget don't exist
1330 |   else {
1331 | #if !KMP_OS_WINDOWS
1332 |     int (*fptr)(kmp_pause_status_t, int);
1333 |     if ((*(void **)(&fptr) = dlsym(RTLD_DEFAULT, "tgt_pause_resource")))
1334 |       return (*fptr)(kind, device_num);
1335 |     else
1347 |   int fails = 0;
1348 | #if !KMP_OS_WINDOWS
1349 |   int (*fptr)(kmp_pause_status_t, int);
1350 |   if ((*(void **)(&fptr) = dlsym(RTLD_DEFAULT, "tgt_pause_resource")))
1351 |     fails = (*fptr)(kind, KMP_DEVICE_ALL); // pause devices
1352 | #endif
{% endraw %}

```
### openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h

```c

{% raw %}
350 | #endif /* ITT_SIMPLE_INIT */
351 | 
352 | void* dlopen(const char*, int) __attribute__((weak));
353 | void* dlsym(void*, const char*) __attribute__((weak));
354 | int dlclose(void*) __attribute__((weak));
355 | #define DL_SYMBOLS (dlopen && dlsym && dlclose)
{% endraw %}

```
### openmp/libomptarget/test/offloading/dynamic_module_load.c

```c

{% raw %}
21 |     printf("dlopen() failed: %s\n", dlerror());
22 |     return 1;
23 |   }
24 |   Foo = (int (*)(void)) dlsym(Handle, "foo");
25 |   if (Handle == NULL) {
26 |     printf("dlsym() failed: %s\n", dlerror());
27 |     return 1;
28 |   }
{% endraw %}

```
### openmp/tools/multiplex/ompt-multiplex.h

```c

{% raw %}
1058 |       if (h) {
1059 |         client_start_tool =
1060 |             (ompt_start_tool_result_t * (*)(unsigned int, const char *))
1061 |                 dlsym(h, "ompt_start_tool");
1062 |         if (client_start_tool &&
1063 |             (ompt_multiplex_client_fns =
{% endraw %}

```
### lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c

```c

{% raw %}
9 |     void *handle = dlopen ("com.apple.sbd.xpc/com.apple.sbd", RTLD_NOW);
10 |     if (handle)
11 |     {
12 |         if (dlsym(handle, "foo"))
13 |         {
14 |             system ("/bin/rm -rf com.apple.sbd.xpc com.apple.sbd.xpc.dSYM");
{% endraw %}

```
### llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

```c

{% raw %}
369 | #if ITT_PLATFORM==ITT_PLATFORM_WIN
370 |     FUNC_NotifyEvent = (TPNotify)GetProcAddress(m_libHandle, "NotifyEvent");
371 | #else  /* ITT_PLATFORM==ITT_PLATFORM_WIN */
372 |     FUNC_NotifyEvent = (TPNotify)(intptr_t)dlsym(m_libHandle, "NotifyEvent");
373 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
374 |     if (!FUNC_NotifyEvent) 
380 | #if ITT_PLATFORM==ITT_PLATFORM_WIN
381 |     FUNC_Initialize = (TPInitialize)GetProcAddress(m_libHandle, "Initialize");
382 | #else  /* ITT_PLATFORM==ITT_PLATFORM_WIN */
383 |     FUNC_Initialize = (TPInitialize)(intptr_t)dlsym(m_libHandle, "Initialize");
384 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
385 |     if (!FUNC_Initialize) 
{% endraw %}

```
### libcxx/src/include/refstring.h

```c

{% raw %}
46 |     void* handle = dlopen("/usr/lib/libstdc++.6.dylib", RTLD_NOLOAD);
47 |     if (handle == nullptr)
48 |         return nullptr;
49 |     void* sym = dlsym(handle, "_ZNSs4_Rep20_S_empty_rep_storageE");
50 |     if (sym == nullptr)
51 |         return nullptr;
{% endraw %}

```
### compiler-rt/lib/safestack/safestack_platform.h

```c

{% raw %}
42 | 
43 | #if SANITIZER_NETBSD
44 | static void *GetRealLibcAddress(const char *symbol) {
45 |   void *real = dlsym(RTLD_NEXT, symbol);
46 |   if (!real)
47 |     real = dlsym(RTLD_DEFAULT, symbol);
48 |   if (!real) {
49 |     fprintf(stderr, "safestack GetRealLibcAddress failed for symbol=%s",
{% endraw %}

```
### compiler-rt/lib/builtins/os_version_check.c

```c

{% raw %}
75 | static void parseSystemVersionPList(void *Unused) {
76 |   (void)Unused;
77 |   // Load CoreFoundation dynamically
78 |   const void *NullAllocator = dlsym(RTLD_DEFAULT, "kCFAllocatorNull");
79 |   if (!NullAllocator)
80 |     return;
81 |   const CFAllocatorRef AllocatorNull = *(const CFAllocatorRef *)NullAllocator;
82 |   CFDataCreateWithBytesNoCopyFuncTy CFDataCreateWithBytesNoCopyFunc =
83 |       (CFDataCreateWithBytesNoCopyFuncTy)dlsym(RTLD_DEFAULT,
84 |                                                "CFDataCreateWithBytesNoCopy");
85 |   if (!CFDataCreateWithBytesNoCopyFunc)
86 |     return;
87 |   CFPropertyListCreateWithDataFuncTy CFPropertyListCreateWithDataFunc =
88 |       (CFPropertyListCreateWithDataFuncTy)dlsym(RTLD_DEFAULT,
89 |                                                 "CFPropertyListCreateWithData");
90 | // CFPropertyListCreateWithData was introduced only in macOS 10.6+, so it
92 | #pragma clang diagnostic push
93 | #pragma clang diagnostic ignored "-Wdeprecated-declarations"
94 |   CFPropertyListCreateFromXMLDataFuncTy CFPropertyListCreateFromXMLDataFunc =
95 |       (CFPropertyListCreateFromXMLDataFuncTy)dlsym(
96 |           RTLD_DEFAULT, "CFPropertyListCreateFromXMLData");
97 | #pragma clang diagnostic pop
100 |   if (!CFPropertyListCreateWithDataFunc && !CFPropertyListCreateFromXMLDataFunc)
101 |     return;
102 |   CFStringCreateWithCStringNoCopyFuncTy CFStringCreateWithCStringNoCopyFunc =
103 |       (CFStringCreateWithCStringNoCopyFuncTy)dlsym(
104 |           RTLD_DEFAULT, "CFStringCreateWithCStringNoCopy");
105 |   if (!CFStringCreateWithCStringNoCopyFunc)
106 |     return;
107 |   CFDictionaryGetValueFuncTy CFDictionaryGetValueFunc =
108 |       (CFDictionaryGetValueFuncTy)dlsym(RTLD_DEFAULT, "CFDictionaryGetValue");
109 |   if (!CFDictionaryGetValueFunc)
110 |     return;
111 |   CFGetTypeIDFuncTy CFGetTypeIDFunc =
112 |       (CFGetTypeIDFuncTy)dlsym(RTLD_DEFAULT, "CFGetTypeID");
113 |   if (!CFGetTypeIDFunc)
114 |     return;
115 |   CFStringGetTypeIDFuncTy CFStringGetTypeIDFunc =
116 |       (CFStringGetTypeIDFuncTy)dlsym(RTLD_DEFAULT, "CFStringGetTypeID");
117 |   if (!CFStringGetTypeIDFunc)
118 |     return;
119 |   CFStringGetCStringFuncTy CFStringGetCStringFunc =
120 |       (CFStringGetCStringFuncTy)dlsym(RTLD_DEFAULT, "CFStringGetCString");
121 |   if (!CFStringGetCStringFunc)
122 |     return;
123 |   CFReleaseFuncTy CFReleaseFunc =
124 |       (CFReleaseFuncTy)dlsym(RTLD_DEFAULT, "CFRelease");
125 |   if (!CFReleaseFunc)
126 |     return;
{% endraw %}

```
### compiler-rt/test/msan/dtls_test.c

```c

{% raw %}
52 |   void *handle = dlopen(path, RTLD_LAZY);
53 |   if (!handle) fprintf(stderr, "%s\n", dlerror());
54 |   assert(handle != 0);
55 |   GetTls = (get_t)dlsym(handle, "GetTls");
56 |   assert(dlerror() == 0);
57 | 
{% endraw %}

```
### compiler-rt/test/cfi/cross-dso/util/cfi_stubs.h

```c

{% raw %}
10 | static cfi_slowpath_diag_ty cfi_slowpath_diag;
11 | 
12 | __attribute__((constructor(0), no_sanitize("cfi"))) static void init() {
13 |   cfi_slowpath = (cfi_slowpath_ty)dlsym(RTLD_NEXT, "__cfi_slowpath");
14 |   cfi_slowpath_diag =
15 |       (cfi_slowpath_diag_ty)dlsym(RTLD_NEXT, "__cfi_slowpath_diag");
16 |   if (!cfi_slowpath || !cfi_slowpath_diag) abort();
17 | }
{% endraw %}

```
### compiler-rt/test/asan/TestCases/Posix/global-registration.c

```c

{% raw %}
42 |       return 1;
43 |     }
44 |     
45 |     char *buffer = (char *)dlsym(handle, "buffer3");
46 |     if (!buffer) {
47 |       fprintf(stderr, "dlsym: %s\n", dlerror());
48 |       return 1;
49 |     }
{% endraw %}

```
### compiler-rt/test/asan/TestCases/Linux/stress_dtls.c

```c

{% raw %}
87 |       exit(1);
88 |     }
89 |     snprintf(buf, sizeof(buf), "f%d", lib);
90 |     Functions[lib] = (f_t)dlsym(handle, buf);
91 |     if (!Functions[lib]) {
92 |       fprintf(stderr, "%s\n", dlerror());
{% endraw %}

```
### compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c

```c

{% raw %}
35 |   int (*bar)(void);
36 |   void *handle = dlopen(argv[1], RTLD_LAZY);
37 |   assert(handle);
38 |   bar = dlsym(handle, "bar");
39 |   assert(bar);
40 |   return bar();
{% endraw %}

```
### compiler-rt/test/tsan/dtls.c

```c

{% raw %}
37 |   void *handle = dlopen(path, RTLD_LAZY);
38 |   if (!handle) fprintf(stderr, "%s\n", dlerror());
39 |   assert(handle != 0);
40 |   GetTls = (get_t)dlsym(handle, "GetTls");
41 |   assert(dlerror() == 0);
42 | 
{% endraw %}

```
### compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c

```c

{% raw %}
18 |     return EXIT_FAILURE;
19 |   }
20 | 
21 |   void (*func)(int) = (void (*)(int))dlsym(f1_handle, "func");
22 |   if (func == NULL) {
23 |     fprintf(stderr, "unable to lookup symbol 'func': %s\n", dlerror());
31 |     return EXIT_FAILURE;
32 |   }
33 | 
34 |   void (*func2)(int) = (void (*)(int))dlsym(f2_handle, "func2");
35 |   if (func2 == NULL) {
36 |     fprintf(stderr, "unable to lookup symbol 'func2': %s\n", dlerror());
{% endraw %}

```
### compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c

```c

{% raw %}
36 |   // This tests that lprofMergeValueProfData is not accessed
37 |   // from outside a module
38 |   void (*SymHandle)(struct ValueProfData *, struct __llvm_profile_data *) =
39 |       (void (*)(struct ValueProfData *, struct __llvm_profile_data *))dlsym(
40 |           Handle, "lprofMergeValueProfData");
41 |   if (SymHandle) {
{% endraw %}

```
### compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c

```c

{% raw %}
9 |     return EXIT_FAILURE;
10 |   }
11 | 
12 |   void (*func)(void) = (void (*)(void))dlsym(f1_handle, "func");
13 |   if (func == NULL) {
14 |     fprintf(stderr, "unable to lookup symbol 'func': %s\n", dlerror());
22 |     return EXIT_FAILURE;
23 |   }
24 | 
25 |   void (*func2)(void) = (void (*)(void))dlsym(f2_handle, "func2");
26 |   if (func2 == NULL) {
27 |     fprintf(stderr, "unable to lookup symbol 'func2': %s\n", dlerror());
36 |     return EXIT_FAILURE;
37 |   }
38 | 
39 |   void (*func3)(void) = (void (*)(void))dlsym(f3_handle, "func3");
40 |   if (func3 == NULL) {
41 |     fprintf(stderr, "unable to lookup symbol 'func3': %s\n", dlerror());
45 | #endif
46 | 
47 |   dlerror();
48 |   void (*gcov_flush1)() = (void (*)())dlsym(f1_handle, "__gcov_flush");
49 |   if (gcov_flush1 == NULL) {
50 |     fprintf(stderr, "unable to find __gcov_flush in func.shared': %s\n", dlerror());
52 |   }
53 | 
54 |   dlerror();
55 |   void (*gcov_flush2)() = (void (*)())dlsym(f2_handle, "__gcov_flush");
56 |   if (gcov_flush2 == NULL) {
57 |     fprintf(stderr, "unable to find __gcov_flush in func2.shared': %s\n", dlerror());
{% endraw %}

```
### polly/tools/GPURuntime/GPUJIT.c

```c

{% raw %}
211 |   char *Err;
212 |   void *FuncPtr;
213 |   dlerror();
214 |   FuncPtr = dlsym(Handle, FuncName);
215 |   if ((Err = dlerror()) != 0) {
216 |     fprintf(stderr, "Load OpenCL Runtime API failed: %s. \n", Err);
1035 |   char *Err;
1036 |   void *FuncPtr;
1037 |   dlerror();
1038 |   FuncPtr = dlsym(Handle, FuncName);
1039 |   if ((Err = dlerror()) != 0) {
1040 |     fprintf(stderr, "Load CUDA driver API failed: %s. \n", Err);
{% endraw %}

```
### libcxxabi/src/include/refstring.h

```c

{% raw %}
50 |     void* handle = dlopen("/usr/lib/libstdc++.6.dylib", RTLD_NOLOAD);
51 |     if (handle == nullptr)
52 |         return nullptr;
53 |     void* sym = dlsym(handle, "_ZNSs4_Rep20_S_empty_rep_storageE");
54 |     if (sym == nullptr)
55 |         return nullptr;
{% endraw %}

```