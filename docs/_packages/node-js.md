---
name: "node-js"
layout: package
next_package: sed
previous_package: wget
languages: ['cpp', 'c']
---
## 13.5.0
46 / 16565 files match

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
471 |   env->SetMethod(target, "dlopen", binding::DLOpen);
{% endraw %}

```
### src/node_constants.cc

```cpp

{% raw %}
1350 |   Local<Object> dlopen_constants = Object::New(isolate);
1351 |   CHECK(dlopen_constants->SetPrototype(env->context(),
1365 |   DefineDLOpenConstants(dlopen_constants);
1372 |                     OneByteString(isolate, "dlopen"),
1373 |                     dlopen_constants).Check();
{% endraw %}

```
### src/node_binding.cc

```cpp

{% raw %}
150 | void* wrapped_dlopen(const char* filename, int flags) {
151 |   CHECK_NOT_NULL(filename);  // This deviates from the 'real' dlopen().
175 |   void* real_handle = dlopen(filename, flags);
327 |   handle_ = dlopen(filename_.c_str(), flags_);
358 |   int ret = uv_dlopen(filename_.c_str(), &lib_);
422 |     env->ThrowError("process.dlopen needs at least 2 arguments.");
{% endraw %}

```
### test/addons/dlopen-ping-pong/binding.cc

```cpp

{% raw %}
7 | extern "C" const char* dlopen_pong(void) {
27 |   void* handle = dlopen(*filename, RTLD_LAZY);
30 |   ping_func = reinterpret_cast<ping>(dlsym(handle, "dlopen_ping"));
{% endraw %}

```
### test/addons/dlopen-ping-pong/ping.c

```c

{% raw %}
2 | const char* dlopen_pong(void);
4 | const char* dlopen_ping(void) {
5 |   return dlopen_pong();
{% endraw %}

```
### deps/openssl/openssl/crypto/dso/dso_dlfcn.c

```c

{% raw %}
115 |     ptr = dlopen(filename, flags);
446 |     void *ret = NULL, *handle = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### deps/v8/src/third_party/vtune/jitprofiling.cc

```cpp

{% raw %}
368 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
377 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
{% endraw %}

```
### deps/uv/src/win/dl.c

```c

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### deps/uv/src/unix/darwin-proctitle.c

```c

{% raw %}
82 |   application_services_handle = dlopen("/System/Library/Frameworks/"
86 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### deps/uv/src/unix/fsevents.c

```c

{% raw %}
536 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
543 |   core_services_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### deps/uv/src/unix/dl.c

```c

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### deps/uv/include/uv.h

```c

{% raw %}
1652 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```