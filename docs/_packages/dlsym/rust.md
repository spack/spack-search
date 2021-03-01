---
name: "rust"
layout: package
next_package: sandbox
previous_package: ruby
library_name: dlsym
matches: ['dlsym', 'dlmopen']
languages: ['cpp', 'c']
---
## 1.44.0
140 / 112209 files match, 50 filtered matches.

 - [src/llvm-project/clang/tools/scan-build-py/libear/ear.c](#srcllvm-projectclangtoolsscan-build-pylibearearc)
 - [src/llvm-project/lldb/packages/Python/lldbsuite/test/macosx/find-dsym/bundle-with-dot-in-filename/main.c](#srcllvm-projectlldbpackagespythonlldbsuitetestmacosxfind-dsymbundle-with-dot-in-filenamemainc)
 - [src/llvm-project/llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c](#srcllvm-projectllvmlibexecutionengineinteljiteventsjitprofilingc)
 - [src/llvm-project/compiler-rt/lib/msan/msan_interceptors.cc](#srcllvm-projectcompiler-rtlibmsanmsan_interceptorscc)
 - [src/llvm-project/compiler-rt/lib/msan/tests/msan_test.cc](#srcllvm-projectcompiler-rtlibmsantestsmsan_testcc)
 - [src/llvm-project/compiler-rt/lib/asan/asan_linux.cc](#srcllvm-projectcompiler-rtlibasanasan_linuxcc)
 - [src/llvm-project/compiler-rt/lib/asan/asan_malloc_linux.cc](#srcllvm-projectcompiler-rtlibasanasan_malloc_linuxcc)
 - [src/llvm-project/compiler-rt/lib/interception/interception_linux.cc](#srcllvm-projectcompiler-rtlibinterceptioninterception_linuxcc)
 - [src/llvm-project/compiler-rt/lib/safestack/safestack_platform.h](#srcllvm-projectcompiler-rtlibsafestacksafestack_platformh)
 - [src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_mac.cc](#srcllvm-projectcompiler-rtlibsanitizer_commonsanitizer_maccc)
 - [src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_symbolizer_posix_libcdep.cc](#srcllvm-projectcompiler-rtlibsanitizer_commonsanitizer_symbolizer_posix_libcdepcc)
 - [src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_netbsd.cc](#srcllvm-projectcompiler-rtlibsanitizer_commonsanitizer_netbsdcc)
 - [src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_unwind_linux_libcdep.cc](#srcllvm-projectcompiler-rtlibsanitizer_commonsanitizer_unwind_linux_libcdepcc)
 - [src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux_libcdep.cc](#srcllvm-projectcompiler-rtlibsanitizer_commonsanitizer_linux_libcdepcc)
 - [src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux.cc](#srcllvm-projectcompiler-rtlibsanitizer_commonsanitizer_linuxcc)
 - [src/llvm-project/compiler-rt/lib/sanitizer_common/symbolizer/sanitizer_wrappers.cc](#srcllvm-projectcompiler-rtlibsanitizer_commonsymbolizersanitizer_wrapperscc)
 - [src/llvm-project/compiler-rt/lib/lsan/lsan_interceptors.cc](#srcllvm-projectcompiler-rtliblsanlsan_interceptorscc)
 - [src/llvm-project/compiler-rt/lib/stats/stats_client.cc](#srcllvm-projectcompiler-rtlibstatsstats_clientcc)
 - [src/llvm-project/compiler-rt/lib/builtins/os_version_check.c](#srcllvm-projectcompiler-rtlibbuiltinsos_version_checkc)
 - [src/llvm-project/compiler-rt/test/msan/dtls_test.c](#srcllvm-projectcompiler-rttestmsandtls_testc)
 - [src/llvm-project/compiler-rt/test/msan/Linux/process_vm_readv.cc](#srcllvm-projectcompiler-rttestmsanlinuxprocess_vm_readvcc)
 - [src/llvm-project/compiler-rt/test/cfi/cross-dso/util/cfi_stubs.h](#srcllvm-projectcompiler-rttestcficross-dsoutilcfi_stubsh)
 - [src/llvm-project/compiler-rt/test/asan/TestCases/Posix/start-deactivated.cc](#srcllvm-projectcompiler-rttestasantestcasesposixstart-deactivatedcc)
 - [src/llvm-project/compiler-rt/test/asan/TestCases/Posix/coverage-module-unloaded.cc](#srcllvm-projectcompiler-rttestasantestcasesposixcoverage-module-unloadedcc)
 - [src/llvm-project/compiler-rt/test/asan/TestCases/Posix/dlclose-test.cc](#srcllvm-projectcompiler-rttestasantestcasesposixdlclose-testcc)
 - [src/llvm-project/compiler-rt/test/asan/TestCases/Posix/global-registration.c](#srcllvm-projectcompiler-rttestasantestcasesposixglobal-registrationc)
 - [src/llvm-project/compiler-rt/test/asan/TestCases/Posix/asan-symbolize-sanity-test.cc](#srcllvm-projectcompiler-rttestasantestcasesposixasan-symbolize-sanity-testcc)
 - [src/llvm-project/compiler-rt/test/asan/TestCases/Posix/shared-lib-test.cc](#srcllvm-projectcompiler-rttestasantestcasesposixshared-lib-testcc)
 - [src/llvm-project/compiler-rt/test/asan/TestCases/Linux/stack-trace-dlclose.cc](#srcllvm-projectcompiler-rttestasantestcaseslinuxstack-trace-dlclosecc)
 - [src/llvm-project/compiler-rt/test/asan/TestCases/Linux/stress_dtls.c](#srcllvm-projectcompiler-rttestasantestcaseslinuxstress_dtlsc)
 - [src/llvm-project/compiler-rt/test/asan/TestCases/Linux/function-sections-are-bad.cc](#srcllvm-projectcompiler-rttestasantestcaseslinuxfunction-sections-are-badcc)
 - [src/llvm-project/compiler-rt/test/asan/TestCases/Darwin/init_for_dlopen.cc](#srcllvm-projectcompiler-rttestasantestcasesdarwininit_for_dlopencc)
 - [src/llvm-project/compiler-rt/test/hwasan/TestCases/Posix/system-allocator-fallback.cc](#srcllvm-projectcompiler-rttesthwasantestcasesposixsystem-allocator-fallbackcc)
 - [src/llvm-project/compiler-rt/test/sanitizer_common/TestCases/get_module_and_offset_for_pc.cc](#srcllvm-projectcompiler-rttestsanitizer_commontestcasesget_module_and_offset_for_pccc)
 - [src/llvm-project/compiler-rt/test/lsan/TestCases/Linux/use_tls_dynamic.cc](#srcllvm-projectcompiler-rttestlsantestcaseslinuxuse_tls_dynamiccc)
 - [src/llvm-project/compiler-rt/test/tsan/ignore_lib1.cc](#srcllvm-projectcompiler-rttesttsanignore_lib1cc)
 - [src/llvm-project/compiler-rt/test/tsan/ignore_lib4.cc](#srcllvm-projectcompiler-rttesttsanignore_lib4cc)
 - [src/llvm-project/compiler-rt/test/tsan/dtls.c](#srcllvm-projectcompiler-rttesttsandtlsc)
 - [src/llvm-project/compiler-rt/test/tsan/ignore_lib5.cc](#srcllvm-projectcompiler-rttesttsanignore_lib5cc)
 - [src/llvm-project/compiler-rt/test/tsan/dlclose.cc](#srcllvm-projectcompiler-rttesttsandlclosecc)
 - [src/llvm-project/compiler-rt/test/tsan/Darwin/dlopen.cc](#srcllvm-projectcompiler-rttesttsandarwindlopencc)
 - [src/llvm-project/compiler-rt/test/tsan/Darwin/external-lib.cc](#srcllvm-projectcompiler-rttesttsandarwinexternal-libcc)
 - [src/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c](#srcllvm-projectcompiler-rttestprofileinputsinstrprof-dlopen-mainc)
 - [src/llvm-project/compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c](#srcllvm-projectcompiler-rttestprofileinputsinstrprof-value-prof-visibilityc)
 - [src/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c](#srcllvm-projectcompiler-rttestprofileinputsinstrprof-dlopen-dlclose-mainc)
 - [vendor/openssl-src/openssl/crypto/rand/rand_vms.c](#vendoropenssl-srcopensslcryptorandrand_vmsc)
 - [vendor/openssl-src/openssl/crypto/dso/dso_dlfcn.c](#vendoropenssl-srcopensslcryptodsodso_dlfcnc)
 - [vendor/jemalloc-sys/jemalloc/src/background_thread.c](#vendorjemalloc-sysjemallocsrcbackground_threadc)
 - [vendor/jemalloc-sys/jemalloc/src/ctl.c](#vendorjemalloc-sysjemallocsrcctlc)
 - [vendor/curl-sys/curl/packages/vms/report_openssl_version.c](#vendorcurl-syscurlpackagesvmsreport_openssl_versionc)

### src/llvm-project/clang/tools/scan-build-py/libear/ear.c

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
### src/llvm-project/lldb/packages/Python/lldbsuite/test/macosx/find-dsym/bundle-with-dot-in-filename/main.c

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
### src/llvm-project/llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

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
### src/llvm-project/compiler-rt/lib/msan/msan_interceptors.cc

```cpp

{% raw %}
72 |   return in_interceptor_scope;
73 | }
74 | 
75 | static uptr allocated_for_dlsym;
76 | static const uptr kDlsymAllocPoolSize = 1024;
77 | static uptr alloc_memory_for_dlsym[kDlsymAllocPoolSize];
78 | 
79 | static bool IsInDlsymAllocPool(const void *ptr) {
80 |   uptr off = (uptr)ptr - (uptr)alloc_memory_for_dlsym;
81 |   return off < sizeof(alloc_memory_for_dlsym);
82 | }
83 | 
84 | static void *AllocateFromLocalPool(uptr size_in_bytes) {
85 |   uptr size_in_words = RoundUpTo(size_in_bytes, kWordSize) / kWordSize;
86 |   void *mem = (void *)&alloc_memory_for_dlsym[allocated_for_dlsym];
87 |   allocated_for_dlsym += size_in_words;
88 |   CHECK_LT(allocated_for_dlsym, kDlsymAllocPoolSize);
89 |   return mem;
90 | }
891 | INTERCEPTOR(void *, realloc, void *ptr, SIZE_T size) {
892 |   GET_MALLOC_STACK_TRACE;
893 |   if (UNLIKELY(IsInDlsymAllocPool(ptr))) {
894 |     uptr offset = (uptr)ptr - (uptr)alloc_memory_for_dlsym;
895 |     uptr copy_size = Min(size, kDlsymAllocPoolSize - offset);
896 |     void *new_ptr;
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/msan/tests/msan_test.cc

```cpp

{% raw %}
3206 |       printf("dlerror: %s\n", dlerror());
3207 |       ASSERT_TRUE(lib != NULL);
3208 |     }
3209 |     void **(*get_dso_global)() = (void **(*)())dlsym(lib, "get_dso_global");
3210 |     ASSERT_TRUE(get_dso_global != NULL);
3211 |     void **dso_global = get_dso_global();
4623 |   free(p);
4624 | 
4625 |   typedef void *(*mmap_fn)(void *, size_t, int, int, int, off_t);
4626 |   mmap_fn real_mmap = (mmap_fn)dlsym(RTLD_NEXT, "mmap");
4627 | 
4628 |   // Allocate the page that was released to the OS in free() with the real mmap,
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/asan/asan_linux.cc

```cpp

{% raw %}
243 | #endif
244 | 
245 | void *AsanDlSymNext(const char *sym) {
246 |   return dlsym(RTLD_NEXT, sym);
247 | }
248 | 
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/asan/asan_malloc_linux.cc

```cpp

{% raw %}
28 | // ---------------------- Replacement functions ---------------- {{{1
29 | using namespace __asan;  // NOLINT
30 | 
31 | static uptr allocated_for_dlsym;
32 | static uptr last_dlsym_alloc_size_in_words;
33 | static const uptr kDlsymAllocPoolSize = SANITIZER_RTEMS ? 4096 : 1024;
34 | static uptr alloc_memory_for_dlsym[kDlsymAllocPoolSize];
35 | 
36 | static INLINE bool IsInDlsymAllocPool(const void *ptr) {
37 |   uptr off = (uptr)ptr - (uptr)alloc_memory_for_dlsym;
38 |   return off < allocated_for_dlsym * sizeof(alloc_memory_for_dlsym[0]);
39 | }
40 | 
41 | static void *AllocateFromLocalPool(uptr size_in_bytes) {
42 |   uptr size_in_words = RoundUpTo(size_in_bytes, kWordSize) / kWordSize;
43 |   void *mem = (void*)&alloc_memory_for_dlsym[allocated_for_dlsym];
44 |   last_dlsym_alloc_size_in_words = size_in_words;
45 |   allocated_for_dlsym += size_in_words;
46 |   CHECK_LT(allocated_for_dlsym, kDlsymAllocPoolSize);
47 |   return mem;
48 | }
51 |   // Hack: since glibc 2.27 dlsym no longer uses stack-allocated memory to store
52 |   // error messages and instead uses malloc followed by free. To avoid pool
53 |   // exhaustion due to long object filenames, handle that special case here.
54 |   uptr prev_offset = allocated_for_dlsym - last_dlsym_alloc_size_in_words;
55 |   void *prev_mem = (void*)&alloc_memory_for_dlsym[prev_offset];
56 |   if (prev_mem == ptr) {
57 |     REAL(memset)(prev_mem, 0, last_dlsym_alloc_size_in_words * kWordSize);
58 |     allocated_for_dlsym = prev_offset;
59 |     last_dlsym_alloc_size_in_words = 0;
60 |   }
61 | }
67 | 
68 |   CHECK(alignment >= kWordSize);
69 | 
70 |   uptr addr = (uptr)&alloc_memory_for_dlsym[allocated_for_dlsym];
71 |   uptr aligned_addr = RoundUpTo(addr, alignment);
72 |   uptr aligned_size = RoundUpTo(size_in_bytes, kWordSize);
73 | 
74 |   uptr *end_mem = (uptr*)(aligned_addr + aligned_size);
75 |   uptr allocated = end_mem - alloc_memory_for_dlsym;
76 |   if (allocated >= kDlsymAllocPoolSize)
77 |     return errno_ENOMEM;
78 | 
79 |   allocated_for_dlsym = allocated;
80 |   *memptr = (void*)aligned_addr;
81 |   return 0;
104 | }
105 | 
106 | static void *ReallocFromLocalPool(void *ptr, uptr size) {
107 |   const uptr offset = (uptr)ptr - (uptr)alloc_memory_for_dlsym;
108 |   const uptr copy_size = Min(size, kDlsymAllocPoolSize - offset);
109 |   void *new_ptr;
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/interception/interception_linux.cc

```cpp

{% raw %}
38 |   if (StrCmp(name, "sigaction"))
39 |     name = "__sigaction14";
40 | #endif
41 |   void *addr = dlsym(RTLD_NEXT, name);
42 |   if (!addr) {
43 |     // If the lookup using RTLD_NEXT failed, the sanitizer runtime library is
45 |     // intercept, which means that we cannot intercept this function. We still
46 |     // want the address of the real definition, though, so look it up using
47 |     // RTLD_DEFAULT.
48 |     addr = dlsym(RTLD_DEFAULT, name);
49 |   }
50 |   return addr;
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/safestack/safestack_platform.h

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
### src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_mac.cc

```cpp

{% raw %}
830 |   // "pthread_create", if interceptors are working, it should really point to
831 |   // "wrap_pthread_create" within our own dylib.
832 |   Dl_info info_pthread_create;
833 |   void *dlopen_addr = dlsym(RTLD_DEFAULT, "pthread_create");
834 |   RAW_CHECK(dladdr(dlopen_addr, &info_pthread_create));
835 |   if (internal_strcmp(info.dli_fname, info_pthread_create.dli_fname) != 0) {
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_symbolizer_posix_libcdep.cc

```cpp

{% raw %}
74 | // malloc and thread-local storage, which is not a good thing to do during
75 | // symbolication.
76 | static void InitializeSwiftDemangler() {
77 |   swift_demangle_f = (swift_demangle_ft)dlsym(RTLD_DEFAULT, "swift_demangle");
78 |   (void)dlerror(); // Cleanup error message in case of failure
79 | }
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_netbsd.cc

```cpp

{% raw %}
74 | namespace __sanitizer {
75 | 
76 | static void *GetRealLibcAddress(const char *symbol) {
77 |   void *real = dlsym(RTLD_NEXT, symbol);
78 |   if (!real)
79 |     real = dlsym(RTLD_DEFAULT, symbol);
80 |   if (!real) {
81 |     Printf("GetRealLibcAddress failed for symbol=%s", symbol);
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_unwind_linux_libcdep.cc

```cpp

{% raw %}
60 |     return;
61 |   }
62 |   acquire_my_map_info_list =
63 |       (acquire_my_map_info_list_func)(uptr)dlsym(p, "acquire_my_map_info_list");
64 |   release_my_map_info_list =
65 |       (release_my_map_info_list_func)(uptr)dlsym(p, "release_my_map_info_list");
66 |   unwind_backtrace_signal_arch = (unwind_backtrace_signal_arch_func)(uptr)dlsym(
67 |       p, "unwind_backtrace_signal_arch");
68 |   if (!acquire_my_map_info_list || !release_my_map_info_list ||
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux_libcdep.cc

```cpp

{% raw %}
150 | 
151 | #if !SANITIZER_GO
152 | bool SetEnv(const char *name, const char *value) {
153 |   void *f = dlsym(RTLD_NEXT, "setenv");
154 |   if (!f)
155 |     return false;
241 | void InitTlsSize() {
242 |   // all current supported platforms have 16 bytes stack alignment
243 |   const size_t kStackAlign = 16;
244 |   void *get_tls_static_info_ptr = dlsym(RTLD_NEXT, "_dl_get_tls_static_info");
245 |   size_t tls_size = 0;
246 |   size_t tls_align = 0;
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux.cc

```cpp

{% raw %}
780 |                           const void *newp, uptr newlen) {
781 |   static decltype(sysctlbyname) *real = nullptr;
782 |   if (!real)
783 |     real = (decltype(sysctlbyname) *)dlsym(RTLD_NEXT, "sysctlbyname");
784 |   CHECK(real);
785 |   return real(sname, oldp, (size_t *)oldlenp, newp, (size_t)newlen);
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/sanitizer_common/symbolizer/sanitizer_wrappers.cc

```cpp

{% raw %}
57 | #define LLVM_SYMBOLIZER_GET_FUNC(Function) \
58 |   ((__interceptor_##Function)              \
59 |        ? (__interceptor_##Function)        \
60 |        : reinterpret_cast<decltype(&Function)>(dlsym(RTLD_NEXT, #Function)))
61 | 
62 | #define LLVM_SYMBOLIZER_INTERCEPTOR1(Function, ...)               \
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/lsan/lsan_interceptors.cc

```cpp

{% raw %}
63 |   if (lsan_init_is_running) {
64 |     // Hack: dlsym calls calloc before REAL(calloc) is retrieved from dlsym.
65 |     const uptr kCallocPoolSize = 1024;
66 |     static uptr calloc_memory_for_dlsym[kCallocPoolSize];
67 |     static uptr allocated;
68 |     uptr size_in_words = ((nmemb * size) + kWordSize - 1) / kWordSize;
69 |     void *mem = (void*)&calloc_memory_for_dlsym[allocated];
70 |     allocated += size_in_words;
71 |     CHECK(allocated < kCallocPoolSize);
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/stats/stats_client.cc

```cpp

{% raw %}
33 | #ifdef _WIN32
34 |   return reinterpret_cast<void *>(GetProcAddress(GetModuleHandle(0), name));
35 | #else
36 |   return dlsym(RTLD_DEFAULT, name);
37 | #endif
38 | }
{% endraw %}

```
### src/llvm-project/compiler-rt/lib/builtins/os_version_check.c

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
### src/llvm-project/compiler-rt/test/msan/dtls_test.c

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
### src/llvm-project/compiler-rt/test/msan/Linux/process_vm_readv.cc

```cpp

{% raw %}
30 | int main(void) {
31 |   // This requires glibc 2.15.
32 |   process_vm_readwritev_fn libc_process_vm_readv =
33 |       (process_vm_readwritev_fn)dlsym(RTLD_NEXT, "process_vm_readv");
34 |   if (!libc_process_vm_readv)
35 |     return exit_dummy();
36 | 
37 |   process_vm_readwritev_fn process_vm_readv =
38 |       (process_vm_readwritev_fn)dlsym(RTLD_DEFAULT, "process_vm_readv");
39 |   process_vm_readwritev_fn process_vm_writev =
40 |       (process_vm_readwritev_fn)dlsym(RTLD_DEFAULT, "process_vm_writev");
41 | 
42 |   char a[100];
{% endraw %}

```
### src/llvm-project/compiler-rt/test/cfi/cross-dso/util/cfi_stubs.h

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
### src/llvm-project/compiler-rt/test/asan/TestCases/Posix/start-deactivated.cc

```cpp

{% raw %}
78 |   }
79 | 
80 |   // After this line ASan is activated and starts detecting errors.
81 |   void *fn = dlsym(dso, "do_another_bad_thing");
82 |   if (!fn) {
83 |     fprintf(stderr, "dlsym failed: %s\n", dlerror());
84 |     return 1;
85 |   }
{% endraw %}

```
### src/llvm-project/compiler-rt/test/asan/TestCases/Posix/coverage-module-unloaded.cc

```cpp

{% raw %}
26 |   assert(argc > 2);
27 |   void *handle1 = dlopen(argv[1], RTLD_LAZY);  // %dynamiclib1
28 |   assert(handle1);
29 |   void (*bar1)() = (void (*)())dlsym(handle1, "bar");
30 |   assert(bar1);
31 |   bar1();
32 |   void *handle2 = dlopen(argv[2], RTLD_LAZY);  // %dynamiclib2
33 |   assert(handle2);
34 |   void (*bar2)() = (void (*)())dlsym(handle2, "bar");
35 |   assert(bar2);
36 |   bar2();
{% endraw %}

```
### src/llvm-project/compiler-rt/test/asan/TestCases/Posix/dlclose-test.cc

```cpp

{% raw %}
54 |     printf("error in dlopen(): %s\n", dlerror());
55 |     return 1;
56 |   }
57 |   fun_t *get = (fun_t*)dlsym(lib, "get_address_of_static_var");
58 |   if (!get) {
59 |     printf("failed dlsym\n");
60 |     return 1;
61 |   }
{% endraw %}

```
### src/llvm-project/compiler-rt/test/asan/TestCases/Posix/global-registration.c

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
### src/llvm-project/compiler-rt/test/asan/TestCases/Posix/asan-symbolize-sanity-test.cc

```cpp

{% raw %}
29 |     printf("error in dlopen(): %s\n", dlerror());
30 |     return 1;
31 |   }
32 |   fun_t *inc2 = (fun_t*)dlsym(lib, "inc2");
33 |   if (!inc2) return 1;
34 |   printf("ok\n");
{% endraw %}

```
### src/llvm-project/compiler-rt/test/asan/TestCases/Posix/shared-lib-test.cc

```cpp

{% raw %}
25 |     printf("error in dlopen(): %s\n", dlerror());
26 |     return 1;
27 |   }
28 |   fun_t *inc = (fun_t*)dlsym(lib, "inc");
29 |   if (!inc) return 1;
30 |   printf("ok\n");
{% endraw %}

```
### src/llvm-project/compiler-rt/test/asan/TestCases/Linux/stack-trace-dlclose.cc

```cpp

{% raw %}
27 | int main(int argc, char **argv) {
28 |   void *handle = dlopen(SO_DIR "/stack_trace_dlclose.so", RTLD_LAZY);
29 |   assert(handle);
30 |   void *(*foo)() = (void *(*)())dlsym(handle, "foo");
31 |   assert(foo);
32 |   void *p = foo();
{% endraw %}

```
### src/llvm-project/compiler-rt/test/asan/TestCases/Linux/stress_dtls.c

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
### src/llvm-project/compiler-rt/test/asan/TestCases/Linux/function-sections-are-bad.cc

```cpp

{% raw %}
20 |   assert(handle != 0);
21 | 
22 |   typedef void (*F)();
23 |   F f = (F)dlsym(handle, "call_rtl_from_dso");
24 |   printf("%s\n", dlerror());
25 |   assert(dlerror() == 0);
{% endraw %}

```
### src/llvm-project/compiler-rt/test/asan/TestCases/Darwin/init_for_dlopen.cc

```cpp

{% raw %}
33 |     return 1;
34 |   }
35 |   // Make sure we can find a function we expect to be in the dylib.
36 |   void *fn = dlsym(handle, "__sanitizer_mz_size");
37 |   if (!fn) {
38 |     fprintf(stderr, "Failed to get symbol: %s\n", dlerror());
{% endraw %}

```
### src/llvm-project/compiler-rt/test/hwasan/TestCases/Posix/system-allocator-fallback.cc

```cpp

{% raw %}
41 |     return 1;
42 |   }
43 | 
44 |   auto run_test = reinterpret_cast<run_test_fn *>(dlsym(lib, "run_test"));
45 |   if (!run_test) {
46 |     printf("failed dlsym\n");
47 |     return 1;
48 |   }
{% endraw %}

```
### src/llvm-project/compiler-rt/test/sanitizer_common/TestCases/get_module_and_offset_for_pc.cc

```cpp

{% raw %}
35 | void TestDlsym() {
36 |   void *handle = dlopen(SO_DIR "/get_module_and_offset_for_pc.so", RTLD_LAZY);
37 |   assert(handle);
38 |   void *foo = dlsym(handle, "foo");
39 |   assert(foo);
40 |   Test(foo, "foo");
{% endraw %}

```
### src/llvm-project/compiler-rt/test/lsan/TestCases/Linux/use_tls_dynamic.cc

```cpp

{% raw %}
25 |   void *handle = dlopen(path.c_str(), RTLD_LAZY);
26 |   assert(handle != 0);
27 |   typedef void **(* store_t)(void *p);
28 |   store_t StoreToTLS = (store_t)dlsym(handle, "StoreToTLS");
29 |   assert(dlerror() == 0);
30 | 
{% endraw %}

```
### src/llvm-project/compiler-rt/test/tsan/ignore_lib1.cc

```cpp

{% raw %}
29 |   void *h = dlopen(lib.c_str(), RTLD_GLOBAL | RTLD_NOW);
30 |   if (h == 0)
31 |     exit(printf("failed to load the library (%d)\n", errno));
32 |   void (*f)() = (void(*)())dlsym(h, "libfunc");
33 |   if (f == 0)
34 |     exit(printf("failed to find the func (%d)\n", errno));
{% endraw %}

```
### src/llvm-project/compiler-rt/test/tsan/ignore_lib4.cc

```cpp

{% raw %}
37 | int main(int argc, char **argv) {
38 |   std::string lib = std::string(dirname(argv[0])) + "/libignore_lib4.so";
39 |   void *h = dlopen(lib.c_str(), RTLD_GLOBAL | RTLD_NOW);
40 |   void (*func)() = (void(*)())dlsym(h, "myfunc");
41 |   func();
42 |   fprintf(stderr, "DONE\n");
{% endraw %}

```
### src/llvm-project/compiler-rt/test/tsan/dtls.c

```c

{% raw %}
36 |   void *handle = dlopen(path, RTLD_LAZY);
37 |   if (!handle) fprintf(stderr, "%s\n", dlerror());
38 |   assert(handle != 0);
39 |   GetTls = (get_t)dlsym(handle, "GetTls");
40 |   assert(dlerror() == 0);
41 | 
{% endraw %}

```
### src/llvm-project/compiler-rt/test/tsan/ignore_lib5.cc

```cpp

{% raw %}
62 |   void *h = dlopen(lib.c_str(), RTLD_GLOBAL | RTLD_NOW);
63 |   if (h == 0)
64 |     exit(printf("failed to load the library (%d)\n", errno));
65 |   void (*f)() = (void(*)())dlsym(h, "libfunc");
66 |   if (f == 0)
67 |     exit(printf("failed to find the func (%d)\n", errno));
{% endraw %}

```
### src/llvm-project/compiler-rt/test/tsan/dlclose.cc

```cpp

{% raw %}
38 |     printf("error in dlopen: %s\n", dlerror());
39 |     return 1;
40 |   }
41 |   void *f = dlsym(lib, "sofunc");
42 |   if (f == 0) {
43 |     printf("error in dlsym: %s\n", dlerror());
44 |     return 1;
45 |   }
{% endraw %}

```
### src/llvm-project/compiler-rt/test/tsan/Darwin/dlopen.cc

```cpp

{% raw %}
29 | int main(int argc, char *argv[]) {
30 |   void *handle = dlopen(argv[1], RTLD_NOW);
31 |   fprintf(stderr, "handle = %p\n", handle);
32 |   void (*foo)() = (void (*)())dlsym(handle, "foo");
33 |   fprintf(stderr, "foo = %p\n", foo);
34 |   foo();
{% endraw %}

```
### src/llvm-project/compiler-rt/test/tsan/Darwin/external-lib.cc

```cpp

{% raw %}
29 | 
30 | void InitializeLibrary() {
31 | #if defined(USE_TSAN_CALLBACKS)
32 |   callback_register_tag = (decltype(callback_register_tag))dlsym(RTLD_DEFAULT, "__tsan_external_register_tag");
33 |   callback_assign_tag = (decltype(callback_assign_tag))dlsym(RTLD_DEFAULT, "__tsan_external_assign_tag");
34 |   callback_read = (decltype(callback_read))dlsym(RTLD_DEFAULT, "__tsan_external_read");
35 |   callback_write = (decltype(callback_write))dlsym(RTLD_DEFAULT, "__tsan_external_write");
36 |   tag = callback_register_tag("MyLibrary::MyObject");
37 | #endif
{% endraw %}

```
### src/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c

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
### src/llvm-project/compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c

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
### src/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c

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
### vendor/openssl-src/openssl/crypto/rand/rand_vms.c

```c

{% raw %}
521 | static int init_get_entropy_address(void)
522 | {
523 |     if (get_entropy_address_flag == 0)
524 |         get_entropy_address = dlsym(dlopen(PUBLIC_VECTORS, 0), GET_ENTROPY);
525 |     get_entropy_address_flag = 1;
526 |     return get_entropy_address != NULL;
{% endraw %}

```
### vendor/openssl-src/openssl/crypto/dso/dso_dlfcn.c

```c

{% raw %}
182 |         DSOerr(DSO_F_DLFCN_BIND_FUNC, DSO_R_NULL_HANDLE);
183 |         return NULL;
184 |     }
185 |     u.dlret = dlsym(ptr, symname);
186 |     if (u.dlret == NULL) {
187 |         DSOerr(DSO_F_DLFCN_BIND_FUNC, DSO_R_SYM_FAILURE);
446 |     void *ret = NULL, *handle = dlopen(NULL, RTLD_LAZY);
447 | 
448 |     if (handle) {
449 |         ret = dlsym(handle, name);
450 |         dlclose(handle);
451 |     }
{% endraw %}

```
### vendor/jemalloc-sys/jemalloc/src/background_thread.c

```c

{% raw %}
811 | 	if (pthread_create_fptr != NULL) {
812 | 		return false;
813 | 	}
814 | 	pthread_create_fptr = dlsym(RTLD_NEXT, "pthread_create");
815 | 	if (pthread_create_fptr == NULL) {
816 | 		can_enable_background_thread = false;
817 | 		if (config_lazy_lock || opt_background_thread) {
818 | 			malloc_write("<jemalloc>: Error in dlsym(RTLD_NEXT, "
819 | 			    "\"pthread_create\")\n");
820 | 			abort();
{% endraw %}

```
### vendor/jemalloc-sys/jemalloc/src/ctl.c

```c

{% raw %}
1544 | 		background_thread_enabled_set(tsd_tsdn(tsd), newval);
1545 | 		if (newval) {
1546 | 			if (!can_enable_background_thread) {
1547 | 				malloc_printf("<jemalloc>: Error in dlsym("
1548 | 			            "RTLD_NEXT, \"pthread_create\"). Cannot "
1549 | 				    "enable background_thread\n");
1605 | 
1606 | 		if (background_thread_enabled()) {
1607 | 			if (!can_enable_background_thread) {
1608 | 				malloc_printf("<jemalloc>: Error in dlsym("
1609 | 			            "RTLD_NEXT, \"pthread_create\"). Cannot "
1610 | 				    "enable background_thread\n");
{% endraw %}

```
### vendor/curl-sys/curl/packages/vms/report_openssl_version.c

```c

{% raw %}
53 | 
54 |    libptr = dlopen(argv[1], 0);
55 | 
56 |    ssl_version = (const char * (*)(int))dlsym(libptr, "SSLeay_version");
57 |    if ((void *)ssl_version == NULL) {
58 |       ssl_version = (const char * (*)(int))dlsym(libptr, "ssleay_version");
59 |       if ((void *)ssl_version == NULL) {
60 |          ssl_version = (const char * (*)(int))dlsym(libptr, "SSLEAY_VERSION");
61 |       }
62 |    }
{% endraw %}

```