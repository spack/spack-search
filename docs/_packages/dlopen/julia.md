---
name: "julia"
layout: package
next_package: stat
previous_package: elfutils
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.5.2
19 / 1327 files match, 3 filtered matches.

 - [src/dlload.c](#srcdlloadc)
 - [src/init.c](#srcinitc)
 - [src/julia.h](#srcjuliah)

### src/dlload.c

```c

{% raw %}
90 | }
91 | #endif
92 | 
93 | JL_DLLEXPORT void *jl_dlopen(const char *filename, unsigned flags)
94 | {
95 | #if defined(_OS_WINDOWS_)
101 |     return LoadLibraryExW(wfilename, NULL, LOAD_WITH_ALTERED_SEARCH_PATH);
102 | #else
103 |     dlerror(); /* Reset error status. */
104 |     return dlopen(filename,
105 |                   (flags & JL_RTLD_NOW ? RTLD_NOW : RTLD_LAZY)
106 |                   | JL_RTLD(flags, LOCAL)
161 |         Dl_info info;
162 |         if (!dladdr((void*)(uintptr_t)&jl_load_dynamic_library, &info) || !info.dli_fname)
163 |             jl_error("could not load base module");
164 |         handle = dlopen(info.dli_fname, RTLD_NOW);
165 | #endif
166 |         goto done;
192 | #ifdef _OS_WINDOWS_
193 |                     if (i == 0) { // LoadLibrary already tested the extensions, we just need to check the `stat` result
194 | #endif
195 |                         handle = jl_dlopen(path, flags);
196 |                         if (handle)
197 |                             goto done;
212 |         const char *ext = extensions[i];
213 |         path[0] = '\0';
214 |         snprintf(path, PATHBUF, "%s%s", modname, ext);
215 |         handle = jl_dlopen(path, flags);
216 |         if (handle)
217 |             goto done;
{% endraw %}

```
### src/init.c

```c

{% raw %}
651 |     jl_init_stack_limits(1, &stack_lo, &stack_hi);
652 |     jl_dl_handle = jl_load_dynamic_library(NULL, JL_RTLD_DEFAULT, 1);
653 | #ifdef _OS_WINDOWS_
654 |     jl_ntdll_handle = jl_dlopen("ntdll.dll", 0); // bypass julia's pathchecking for system dlls
655 |     jl_kernel32_handle = jl_dlopen("kernel32.dll", 0);
656 | #if defined(_MSC_VER) && _MSC_VER == 1800
657 |     jl_crtdll_handle = jl_dlopen("msvcr120.dll", 0);
658 | #else
659 |     jl_crtdll_handle = jl_dlopen("msvcrt.dll", 0);
660 | #endif
661 |     jl_winsock_handle = jl_dlopen("ws2_32.dll", 0);
662 |     jl_exe_handle = GetModuleHandleA(NULL);
663 |     SymSetOptions(SYMOPT_UNDNAME | SYMOPT_DEFERRED_LOADS | SYMOPT_LOAD_LINES);
665 |         jl_printf(JL_STDERR, "WARNING: failed to initialize stack walk info\n");
666 |     }
667 |     needsSymRefreshModuleList = 0;
668 |     HMODULE jl_dbghelp = (HMODULE) jl_dlopen("dbghelp.dll", 0);
669 |     if (jl_dbghelp)
670 |         jl_dlsym(jl_dbghelp, "SymRefreshModuleList", (void **)&hSymRefreshModuleList, 1);
671 | #else
672 |     jl_exe_handle = jl_dlopen(NULL, JL_RTLD_NOW);
673 | #ifdef RTLD_DEFAULT
674 |     jl_RTLD_DEFAULT_handle = RTLD_DEFAULT;
{% endraw %}

```
### src/julia.h

```c

{% raw %}
1632 | };
1633 | #define JL_RTLD_DEFAULT (JL_RTLD_LAZY | JL_RTLD_DEEPBIND)
1634 | 
1635 | typedef void *jl_uv_libhandle; // compatible with dlopen (void*) / LoadLibrary (HMODULE)
1636 | JL_DLLEXPORT jl_uv_libhandle jl_load_dynamic_library(const char *fname, unsigned flags, int throw_err);
1637 | JL_DLLEXPORT jl_uv_libhandle jl_dlopen(const char *filename, unsigned flags);
1638 | JL_DLLEXPORT int jl_dlclose(jl_uv_libhandle handle);
1639 | JL_DLLEXPORT int jl_dlsym(jl_uv_libhandle handle, const char *symbol, void ** value, int throw_err);
{% endraw %}

```