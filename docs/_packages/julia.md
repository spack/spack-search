---
name: "julia"
layout: package
next_package: aspect
previous_package: moosefs
languages: ['c']
---
## 1.5.2
19 / 1327 files match

 - [src/dlload.c](#srcdlloadc)
 - [src/init.c](#srcinitc)
 - [src/julia.h](#srcjuliah)

### src/dlload.c

```c

{% raw %}
93 | JL_DLLEXPORT void *jl_dlopen(const char *filename, unsigned flags)
104 |     return dlopen(filename,
164 |         handle = dlopen(info.dli_fname, RTLD_NOW);
195 |                         handle = jl_dlopen(path, flags);
215 |         handle = jl_dlopen(path, flags);
{% endraw %}

```
### src/init.c

```c

{% raw %}
654 |     jl_ntdll_handle = jl_dlopen("ntdll.dll", 0); // bypass julia's pathchecking for system dlls
655 |     jl_kernel32_handle = jl_dlopen("kernel32.dll", 0);
657 |     jl_crtdll_handle = jl_dlopen("msvcr120.dll", 0);
659 |     jl_crtdll_handle = jl_dlopen("msvcrt.dll", 0);
661 |     jl_winsock_handle = jl_dlopen("ws2_32.dll", 0);
668 |     HMODULE jl_dbghelp = (HMODULE) jl_dlopen("dbghelp.dll", 0);
672 |     jl_exe_handle = jl_dlopen(NULL, JL_RTLD_NOW);
{% endraw %}

```
### src/julia.h

```c

{% raw %}
1635 | typedef void *jl_uv_libhandle; // compatible with dlopen (void*) / LoadLibrary (HMODULE)
1637 | JL_DLLEXPORT jl_uv_libhandle jl_dlopen(const char *filename, unsigned flags);
{% endraw %}

```