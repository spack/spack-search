---
name: "casacore"
layout: package
next_package: libunwind
previous_package: gmake
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 3.3.0
3 / 3213 files match, 2 filtered matches.

 - [casa/OS/MemoryTrace.cc](#casaosmemorytracecc)
 - [casa/OS/DynLib.cc](#casaosdynlibcc)

### casa/OS/MemoryTrace.cc

```cpp

{% raw %}
279 |   ptrCastUnion ptrCast;
280 | 
281 |   void* handle = RTLD_NEXT;
282 |   ptrCast.ptr = dlsym(handle, "malloc");
283 |   if (ptrCast.ptr == NULL) {
284 |     printf("libcasa_malloclog cannot find malloc\n");
303 | 
304 |   printf("free %p\n", addr);
305 |   void* handle = RTLD_NEXT;
306 |   ptrCast.ptr = dlsym(handle, "free");
307 |   if (ptrCast.ptr == NULL) {
308 |     exit(1);
{% endraw %}

```
### casa/OS/DynLib.cc

```cpp

{% raw %}
93 |     itsError.clear();
94 | #ifdef HAVE_DLOPEN
95 |     if (itsHandle ) {
96 |       void* fptr = dlsym (itsHandle, funcName.c_str());
97 |       if (fptr == 0) {
98 |         itsError = dlerror();
{% endraw %}

```