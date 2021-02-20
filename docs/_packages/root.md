---
name: "root"
layout: package
next_package: rose
previous_package: roctracer-dev
languages: ['python', 'c']
---
## 6.22.06
26 / 18941 files match, 7 filtered matches.

 - [interpreter/llvm/src/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c](#interpreterllvmsrclibexecutionengineinteljiteventsjitprofilingc)
 - [bindings/pyroot/pythonizations/python/ROOT/_numbadeclare.py](#bindingspyrootpythonizationspythonroot_numbadeclarepy)
 - [bindings/pyroot_legacy/cppyy.py](#bindingspyroot_legacycppyypy)
 - [bindings/pyroot_legacy/JupyROOT/helpers/cppcompleter.py](#bindingspyroot_legacyjupyroothelperscppcompleterpy)
 - [bindings/jupyroot/python/JupyROOT/helpers/cppcompleter.py](#bindingsjupyrootpythonjupyroothelperscppcompleterpy)
 - [net/http/civetweb/civetweb.c](#nethttpcivetwebcivetwebc)
 - [builtins/glew/src/glew.c](#builtinsglewsrcglewc)

### interpreter/llvm/src/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

```c

{% raw %}
346 |     if (dllName)
347 |     {
348 |         /* Try to load the dll from the PATH... */
349 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
350 |     }
351 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
355 | #if ITT_PLATFORM==ITT_PLATFORM_WIN
356 |         m_libHandle = LoadLibraryA(DEFAULT_DLLNAME);
357 | #else  /* ITT_PLATFORM==ITT_PLATFORM_WIN */
358 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
359 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
360 |     }
{% endraw %}

```
### bindings/pyroot/pythonizations/python/ROOT/_numbadeclare.py

```python

{% raw %}
188 | 
189 |         ffi = cffi.FFI()
190 |         ffi.cdef('void* malloc(long size);')
191 |         C = ffi.dlopen(None)
192 |         glob['malloc'] = C.malloc
193 | 
{% endraw %}

```
### bindings/pyroot_legacy/cppyy.py

```python

{% raw %}
54 |                   ( 0 <= sys.platform.find( 'sunos' ) )
55 |    if needsGlobal:
56 |       # change dl flags to load dictionaries from pre-linked .so's
57 |       dlflags = sys.getdlopenflags()
58 |       sys.setdlopenflags( 0x100 | 0x2 )    # RTLD_GLOBAL | RTLD_NOW
59 | 
60 |    import libPyROOT as _backend
61 | 
62 |    # reset dl flags if needed
63 |    if needsGlobal:
64 |       sys.setdlopenflags( dlflags )
65 |    del needsGlobal
66 | 
{% endraw %}

```
### bindings/pyroot_legacy/JupyROOT/helpers/cppcompleter.py

```python

{% raw %}
108 |         self.active = True
109 |         if self.firstActivation:
110 |             utils.declareCppCode('#include "dlfcn.h"')
111 |             dlOpenRint = 'dlopen("libRint.so",RTLD_NOW);'
112 |             utils.processCppCode(dlOpenRint)
113 |             utils.declareCppCode(_TTabComHookCode)
{% endraw %}

```
### bindings/jupyroot/python/JupyROOT/helpers/cppcompleter.py

```python

{% raw %}
108 |         self.active = True
109 |         if self.firstActivation:
110 |             utils.declareCppCode('#include "dlfcn.h"')
111 |             dlOpenRint = 'dlopen("libRint.so",RTLD_NOW);'
112 |             utils.processCppCode(dlOpenRint)
113 |             utils.declareCppCode(_TTabComHookCode)
{% endraw %}

```
### net/http/civetweb/civetweb.c

```c

{% raw %}
5530 | 
5531 | FUNCTION_MAY_BE_UNUSED
5532 | static HANDLE
5533 | dlopen(const char *dll_name, int flags)
5534 | {
5535 | 	wchar_t wbuf[W_PATH_MAX];
15277 | 	int ok;
15278 | 	int truncated = 0;
15279 | 
15280 | 	if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
15281 | 		mg_snprintf(NULL,
15282 | 		            NULL, /* No truncation check for ebuf */
{% endraw %}

```
### builtins/glew/src/glew.c

```c

{% raw %}
85 | 
86 |   if (h == NULL)
87 |   {
88 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
89 |     gpa = dlsym(h, "glXGetProcAddress");
90 |   }
111 |   void* addr;
112 |   if (NULL == image)
113 |   {
114 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
115 |   }
116 |   if( !image ) return NULL;
{% endraw %}

```