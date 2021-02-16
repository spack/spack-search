---
name: "icarus"
layout: package
next_package: libxslt
previous_package: py-mpi4py
languages: ['cpp', 'c']
---
## v10_3
7 / 728 files match

 - [t-dll.cc](#t-dllcc)
 - [vvp/vpi_modules.cc](#vvpvpi_modulescc)
 - [vvp/ivl_dlfcn.h](#vvpivl_dlfcnh)
 - [cadpli/cadpli.c](#cadplicadplic)
 - [cadpli/ivl_dlfcn.h](#cadpliivl_dlfcnh)

### t-dll.cc

```cpp

{% raw %}
39 | inline ivl_dll_t ivl_dlopen(const char *name)
72 | inline ivl_dll_t ivl_dlopen(const char*name)
73 | { return dlopen(name,RTLD_LAZY); }
88 | inline ivl_dll_t ivl_dlopen(const char*name)
689 |       dll_ = ivl_dlopen(dll_path_);
695 | 	    dll_ = ivl_dlopen(tmp);
2808 |       dll_ = ivl_dlopen(target_name);
2814 | 	    dll_ = ivl_dlopen(tmp);
{% endraw %}

```
### vvp/vpi_modules.cc

```cpp

{% raw %}
137 |       dll = ivl_dlopen(buf, export_flag);
140 | 	fprintf(stderr,"%s:`%s' failed to open using dlopen() because:\n"
{% endraw %}

```
### vvp/ivl_dlfcn.h

```c

{% raw %}
34 | inline ivl_dll_t ivl_dlopen(const char *name, bool)
68 | inline ivl_dll_t ivl_dlopen(const char*name, bool global_flag)
69 | { return dlopen(name,RTLD_LAZY|(global_flag?RTLD_GLOBAL:0)); }
84 | inline ivl_dll_t ivl_dlopen(const char*name)
{% endraw %}

```
### cadpli/cadpli.c

```c

{% raw %}
55 | 	    mod = ivl_dlopen(module);
{% endraw %}

```
### cadpli/ivl_dlfcn.h

```c

{% raw %}
34 | static __inline__ ivl_dll_t ivl_dlopen(const char *name)
60 | static __inline__ ivl_dll_t ivl_dlopen(const char*name)
61 | { return dlopen(name,RTLD_LAZY); }
76 | static __inline__ ivl_dll_t ivl_dlopen(const char*name)
{% endraw %}

```