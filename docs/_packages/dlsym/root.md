---
name: "root"
layout: package
next_package: rose
previous_package: rocksdb
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 6.22.06
27 / 18941 files match, 5 filtered matches.

 - [interpreter/llvm/src/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c](#interpreterllvmsrclibexecutionengineinteljiteventsjitprofilingc)
 - [interpreter/llvm/src/tools/clang/tools/scan-build-py/libear/ear.c](#interpreterllvmsrctoolsclangtoolsscan-build-pylibearearc)
 - [interpreter/cling/lib/Interpreter/IncrementalExecutor.h](#interpreterclinglibinterpreterincrementalexecutorh)
 - [net/http/civetweb/civetweb.c](#nethttpcivetwebcivetwebc)
 - [builtins/glew/src/glew.c](#builtinsglewsrcglewc)

### interpreter/llvm/src/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

```c

{% raw %}
371 | #if ITT_PLATFORM==ITT_PLATFORM_WIN
372 |     FUNC_NotifyEvent = (TPNotify)GetProcAddress(m_libHandle, "NotifyEvent");
373 | #else  /* ITT_PLATFORM==ITT_PLATFORM_WIN */
374 |     FUNC_NotifyEvent = (TPNotify)(intptr_t)dlsym(m_libHandle, "NotifyEvent");
375 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
376 |     if (!FUNC_NotifyEvent) 
382 | #if ITT_PLATFORM==ITT_PLATFORM_WIN
383 |     FUNC_Initialize = (TPInitialize)GetProcAddress(m_libHandle, "Initialize");
384 | #else  /* ITT_PLATFORM==ITT_PLATFORM_WIN */
385 |     FUNC_Initialize = (TPInitialize)(intptr_t)dlsym(m_libHandle, "Initialize");
386 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
387 |     if (!FUNC_Initialize) 
{% endraw %}

```
### interpreter/llvm/src/tools/clang/tools/scan-build-py/libear/ear.c

```c

{% raw %}
54 |         void *from;                                                            \
55 |         TYPE_ to;                                                              \
56 |     } cast;                                                                    \
57 |     if (0 == (cast.from = dlsym(RTLD_NEXT, SYMBOL_))) {                        \
58 |         perror("bear: dlsym");                                                 \
59 |         exit(EXIT_FAILURE);                                                    \
60 |     }                                                                          \
{% endraw %}

```
### interpreter/cling/lib/Interpreter/IncrementalExecutor.h

```c

{% raw %}
272 |     template <class T>
273 |     ExecutionResult jitInitOrWrapper(llvm::StringRef funcname, T& fun) const {
274 |       fun = utils::UIntToFunctionPtr<T>(m_JIT->getSymbolAddress(funcname,
275 |                                                               false /*dlsym*/));
276 | 
277 |       // check if there is any unresolved symbol in the list
{% endraw %}

```
### net/http/civetweb/civetweb.c

```c

{% raw %}
15292 | 	for (fp = sw; fp->name != NULL; fp++) {
15293 | #if defined(_WIN32)
15294 | 		/* GetProcAddress() returns pointer to function */
15295 | 		u.fp = (void (*)(void))dlsym(dll_handle, fp->name);
15296 | #else
15297 | 		/* dlsym() on UNIX returns void *. ISO C forbids casts of data
15298 | 		 * pointers to function pointers. We need to use a union to make a
15299 | 		 * cast. */
15300 | 		u.p = dlsym(dll_handle, fp->name);
15301 | #endif /* _WIN32 */
15302 | 		if (u.fp == NULL) {
{% endraw %}

```
### builtins/glew/src/glew.c

```c

{% raw %}
86 |   if (h == NULL)
87 |   {
88 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
89 |     gpa = dlsym(h, "glXGetProcAddress");
90 |   }
91 | 
92 |   if (gpa != NULL)
93 |     return ((void*(*)(const GLubyte*))gpa)(name);
94 |   else
95 |     return dlsym(h, (const char*)name);
96 | }
97 | #endif /* __sgi || __sun || GLEW_APPLE_GLX */
114 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
115 |   }
116 |   if( !image ) return NULL;
117 |   addr = dlsym(image, (const char*)name);
118 |   if( addr ) return addr;
119 | #ifdef GLEW_APPLE_GLX
{% endraw %}

```