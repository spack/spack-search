---
name: "node-js"
layout: package
next_package: ns-3-dev
previous_package: nnvm
languages: ['cpp', 'c']
---
## 13.5.0
46 / 16565 files match, 12 filtered matches.

 - [src/node_process_methods.cc](#srcnode_process_methodscc)
 - [src/node_constants.cc](#srcnode_constantscc)
 - [src/node_binding.cc](#srcnode_bindingcc)
 - [test/addons/dlopen-ping-pong/binding.cc](#testaddonsdlopen-ping-pongbindingcc)
 - [test/addons/dlopen-ping-pong/ping.c](#testaddonsdlopen-ping-pongpingc)
 - [deps/openssl/openssl/crypto/dso/dso_dlfcn.c](#depsopensslopensslcryptodsodso_dlfcnc)
 - [deps/v8/src/third_party/vtune/jitprofiling.cc](#depsv8srcthird_partyvtunejitprofilingcc)
 - [deps/uv/src/win/dl.c](#depsuvsrcwindlc)
 - [deps/uv/src/unix/darwin-proctitle.c](#depsuvsrcunixdarwin-proctitlec)
 - [deps/uv/src/unix/fsevents.c](#depsuvsrcunixfseventsc)
 - [deps/uv/src/unix/dl.c](#depsuvsrcunixdlc)
 - [deps/uv/include/uv.h](#depsuvincludeuvh)

### src/node_process_methods.cc

```cpp

{% raw %}
468 |   env->SetMethod(target, "_kill", Kill);
469 | 
470 |   env->SetMethodNoSideEffect(target, "cwd", Cwd);
471 |   env->SetMethod(target, "dlopen", binding::DLOpen);
472 |   env->SetMethod(target, "reallyExit", ReallyExit);
473 |   env->SetMethodNoSideEffect(target, "uptime", Uptime);
{% endraw %}

```
### src/node_constants.cc

```cpp

{% raw %}
1347 |   CHECK(zlib_constants->SetPrototype(env->context(),
1348 |                                      Null(env->isolate())).FromJust());
1349 | 
1350 |   Local<Object> dlopen_constants = Object::New(isolate);
1351 |   CHECK(dlopen_constants->SetPrototype(env->context(),
1352 |                                        Null(env->isolate())).FromJust());
1353 | 
1362 |   DefineSystemConstants(fs_constants);
1363 |   DefineCryptoConstants(crypto_constants);
1364 |   DefineZlibConstants(zlib_constants);
1365 |   DefineDLOpenConstants(dlopen_constants);
1366 |   DefineTraceConstants(trace_constants);
1367 | 
1369 |   NODE_DEFINE_CONSTANT(os_constants, UV_UDP_REUSEADDR);
1370 | 
1371 |   os_constants->Set(env->context(),
1372 |                     OneByteString(isolate, "dlopen"),
1373 |                     dlopen_constants).Check();
1374 |   os_constants->Set(env->context(),
1375 |                     OneByteString(isolate, "errno"),
{% endraw %}

```
### src/node_binding.cc

```cpp

{% raw %}
147 |   return &dlerror_storage[0];
148 | }
149 | 
150 | void* wrapped_dlopen(const char* filename, int flags) {
151 |   CHECK_NOT_NULL(filename);  // This deviates from the 'real' dlopen().
152 |   Mutex::ScopedLock lock(dlhandles_mutex);
153 | 
172 |     return *it;
173 |   }
174 | 
175 |   void* real_handle = dlopen(filename, flags);
176 |   if (real_handle == nullptr) {
177 |     dlerror_storage = dlerror();
324 | 
325 | #ifdef __POSIX__
326 | bool DLib::Open() {
327 |   handle_ = dlopen(filename_.c_str(), flags_);
328 |   if (handle_ != nullptr) return true;
329 |   errmsg_ = dlerror();
355 | }
356 | #else   // !__POSIX__
357 | bool DLib::Open() {
358 |   int ret = uv_dlopen(filename_.c_str(), &lib_);
359 |   if (ret == 0) {
360 |     handle_ = static_cast<void*>(lib_.handle);
419 |   CHECK_NULL(thread_local_modpending);
420 | 
421 |   if (args.Length() < 2) {
422 |     env->ThrowError("process.dlopen needs at least 2 arguments.");
423 |     return;
424 |   }
{% endraw %}

```
### test/addons/dlopen-ping-pong/binding.cc

```cpp

{% raw %}
4 | 
5 | #include <dlfcn.h>
6 | 
7 | extern "C" const char* dlopen_pong(void) {
8 |   return "pong";
9 | }
24 | 
25 | void LoadLibrary(const FunctionCallbackInfo<Value>& args) {
26 |   const String::Utf8Value filename(args.GetIsolate(), args[0]);
27 |   void* handle = dlopen(*filename, RTLD_LAZY);
28 |   if (handle == nullptr) fprintf(stderr, "%s\n", dlerror());
29 |   assert(handle != nullptr);
30 |   ping_func = reinterpret_cast<ping>(dlsym(handle, "dlopen_ping"));
31 |   assert(ping_func != nullptr);
32 | }
{% endraw %}

```
### test/addons/dlopen-ping-pong/ping.c

```c

{% raw %}
1 | 
2 | const char* dlopen_pong(void);
3 | 
4 | const char* dlopen_ping(void) {
5 |   return dlopen_pong();
6 | }
7 | 
{% endraw %}

```
### deps/openssl/openssl/crypto/dso/dso_dlfcn.c

```c

{% raw %}
112 |     if (filename[strlen(filename) - 1] == ')')
113 |         flags |= RTLD_MEMBER;
114 | # endif
115 |     ptr = dlopen(filename, flags);
116 |     if (ptr == NULL) {
117 |         DSOerr(DSO_F_DLFCN_LOAD, DSO_R_LOAD_FAILED);
443 | 
444 | static void *dlfcn_globallookup(const char *name)
445 | {
446 |     void *ret = NULL, *handle = dlopen(NULL, RTLD_LAZY);
447 | 
448 |     if (handle) {
{% endraw %}

```
### deps/v8/src/third_party/vtune/jitprofiling.cc

```cpp

{% raw %}
365 |     if (dllName)
366 |     {
367 |         // Try to load the dll from the PATH...
368 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
369 |     }
370 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
374 | #if ITT_PLATFORM==ITT_PLATFORM_WIN
375 |         m_libHandle = LoadLibraryA(DEFAULT_DLLNAME);
376 | #else  /* ITT_PLATFORM==ITT_PLATFORM_WIN */
377 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
378 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
379 |     }
{% endraw %}

```
### deps/uv/src/win/dl.c

```c

{% raw %}
24 | static int uv__dlerror(uv_lib_t* lib, const char* filename, DWORD errorno);
25 | 
26 | 
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
28 |   WCHAR filename_w[32768];
29 | 
{% endraw %}

```
### deps/uv/src/unix/darwin-proctitle.c

```c

{% raw %}
79 | #if !TARGET_OS_IPHONE
80 |   OSStatus (*pSetApplicationIsDaemon)(int);
81 | 
82 |   application_services_handle = dlopen("/System/Library/Frameworks/"
83 |                                        "ApplicationServices.framework/"
84 |                                        "Versions/A/ApplicationServices",
85 |                                        RTLD_LAZY | RTLD_LOCAL);
86 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
87 |                                   "CoreFoundation.framework/"
88 |                                   "Versions/A/CoreFoundation",
{% endraw %}

```
### deps/uv/src/unix/fsevents.c

```c

{% raw %}
533 |    * per-event loop properties and have the dynamic linker keep track for us.
534 |    */
535 |   err = UV_ENOSYS;
536 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
537 |                                   "CoreFoundation.framework/"
538 |                                   "Versions/A/CoreFoundation",
540 |   if (core_foundation_handle == NULL)
541 |     goto out;
542 | 
543 |   core_services_handle = dlopen("/System/Library/Frameworks/"
544 |                                 "CoreServices.framework/"
545 |                                 "Versions/A/CoreServices",
{% endraw %}

```
### deps/uv/src/unix/dl.c

```c

{% raw %}
29 | static int uv__dlerror(uv_lib_t* lib);
30 | 
31 | 
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
33 |   dlerror(); /* Reset error status. */
34 |   lib->errmsg = NULL;
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
36 |   return lib->handle ? 0 : uv__dlerror(lib);
37 | }
{% endraw %}

```
### deps/uv/include/uv.h

```c

{% raw %}
1649 | 
1650 | UV_EXTERN void uv_disable_stdio_inheritance(void);
1651 | 
1652 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
1653 | UV_EXTERN void uv_dlclose(uv_lib_t* lib);
1654 | UV_EXTERN int uv_dlsym(uv_lib_t* lib, const char* name, void** ptr);
{% endraw %}

```