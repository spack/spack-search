---
name: "charmpp"
layout: package
next_package: cistem
previous_package: chapel
languages: ['c']
---
## 6.9.0
15 / 4475 files match, 4 filtered matches.

 - [src/util/ckdll_dlopen.C](#srcutilckdll_dlopenc)
 - [tests/ampi/privatization/test-cxx.C](#testsampiprivatizationtest-cxxc)
 - [contrib/hwloc/src/components.c](#contribhwlocsrccomponentsc)
 - [contrib/hwloc/include/hwloc/plugins.h](#contribhwlocincludehwlocpluginsh)

### src/util/ckdll_dlopen.C

```c

{% raw %}
1 |  dlopen version of CkDll class.  
2 |  This file can be #included whole by the configure script or ckdll.C.
3 | 
8 | #include <dlfcn.h> //for dlopen, etc.
9 | 
10 | CkDll::CkDll(const char *name) {
11 | 	handle=dlopen(name,RTLD_NOW);
12 | }
13 | void *CkDll::lookup(const char *name) {
{% endraw %}

```
### tests/ampi/privatization/test-cxx.C

```c

{% raw %}
58 |   int_ptr_accessor get_static_global_sharedlibrary_dynamic_ptr = nullptr;
59 |   int_ptr_accessor get_static_local_sharedlibrary_dynamic_ptr = nullptr;
60 | #endif
61 |   void * dynamiclib = dlopen("libcxx-" privatization_method_str "-shared-library-dynamic.so", RTLD_NOW);
62 |   if (!dynamiclib)
63 |   {
64 |     fprintf(stderr, "dlopen failed: %s\n", dlerror());
65 |   }
66 |   else
{% endraw %}

```
### contrib/hwloc/src/components.c

```c

{% raw %}
97 |   }
98 | 
99 |   /* dlopen and get the component structure */
100 |   handle = lt_dlopenext(filename);
101 |   if (!handle) {
102 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### contrib/hwloc/include/hwloc/plugins.h

```c

{% raw %}
367 | #ifdef HWLOC_INSIDE_PLUGIN
368 |   lt_dlhandle handle;
369 |   void *sym;
370 |   handle = lt_dlopen(NULL);
371 |   if (!handle)
372 |     /* cannot check, assume things will work */
{% endraw %}

```