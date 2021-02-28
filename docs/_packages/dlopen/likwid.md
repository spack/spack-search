---
name: "likwid"
layout: package
next_package: openssl
previous_package: libpng
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.0.2
14 / 1422 files match, 13 filtered matches.

 - [src/topology_gpu.c](#srctopology_gpuc)
 - [src/includes/likwid.h](#srcincludeslikwidh)
 - [src/includes/nvmon_cupti.h](#srcincludesnvmon_cuptih)
 - [src/includes/nvmon_perfworks.h](#srcincludesnvmon_perfworksh)
 - [src/pthread-overload/pthread-overload.c](#srcpthread-overloadpthread-overloadc)
 - [ext/GOTCHA/src/gotcha_dl.h](#extgotchasrcgotcha_dlh)
 - [ext/GOTCHA/src/gotcha_dl.c](#extgotchasrcgotcha_dlc)
 - [ext/GOTCHA/src/gotcha.c](#extgotchasrcgotchac)
 - [ext/hwloc/include/hwloc/plugins.h](#exthwlocincludehwlocpluginsh)
 - [ext/hwloc/hwloc/components.c](#exthwlochwloccomponentsc)
 - [ext/lua/src/loadlib.c](#extluasrcloadlibc)
 - [bench/src/ptt2asm.c](#benchsrcptt2asmc)
 - [bench/includes/likwid.h](#benchincludeslikwidh)

### src/topology_gpu.c

```c

{% raw %}
107 |         return -1;
108 |     }
109 |     /* Need to link in the cuda libraries, if not found disable the component */
110 |     topo_dl_libcuda = dlopen("libcuda.so", RTLD_NOW | RTLD_GLOBAL);
111 |     if (!topo_dl_libcuda)
112 |     {
113 |         fprintf(stderr, "CUDA library libcuda.so not found.\n");
114 |         return -1;
115 |     }
116 |     topo_dl_libcudart = dlopen("libcudart.so", RTLD_NOW | RTLD_GLOBAL | RTLD_NODELETE);
117 |     if (!topo_dl_libcudart)
118 |     {
{% endraw %}

```
### src/includes/likwid.h

```c

{% raw %}
2078 | /*! \brief Initialize the Nvidia GPU performance monitoring facility (Nvmon)
2079 | 
2080 | Initialize the Nvidia GPU performance monitoring feature by creating basic data structures.
2081 | The CUDA and CUPTI library paths need to be in LD_LIBRARY_PATH to be found by dlopen.
2082 | 
2083 | @param [in] nrGpus Amount of GPUs
{% endraw %}

```
### src/includes/nvmon_cupti.h

```c

{% raw %}
123 |         return -1;
124 |     }
125 |     /* Need to link in the cuda libraries, if not found disable the component */
126 |     dl_libcuda = dlopen("libcuda.so", RTLD_NOW | RTLD_GLOBAL);
127 |     if (!dl_libcuda)
128 |     {
140 |     cuCtxSynchronizePtr = DLSYM_AND_CHECK(dl_libcuda, "cuCtxSynchronize");
141 |     cuCtxDestroyPtr = DLSYM_AND_CHECK(dl_libcuda, "cuCtxDestroy");
142 | 
143 |     dl_libcudart = dlopen("libcudart.so", RTLD_NOW | RTLD_GLOBAL | RTLD_NODELETE);
144 |     if (!dl_libcudart)
145 |     {
150 |     cudaSetDevicePtr = DLSYM_AND_CHECK(dl_libcudart, "cudaSetDevice");
151 |     cudaFreePtr = DLSYM_AND_CHECK(dl_libcudart, "cudaFree");
152 | 
153 |     dl_libcupti = dlopen("libcupti.so", RTLD_NOW | RTLD_GLOBAL);
154 |     if (!dl_libcupti)
155 |     {
{% endraw %}

```
### src/includes/nvmon_perfworks.h

```c

{% raw %}
92 |     if(_dl_non_dynamic_init != NULL) {
93 |         return -1;
94 |     }
95 |     perfw_dl_libcuda = dlopen("libcuda.so", RTLD_NOW | RTLD_GLOBAL);
96 |     if (!perfw_dl_libcuda)
97 |     {
98 |         fprintf(stderr, "CUDA library libcuda.so not found.\n");
99 |         return -1;
100 |     }
101 |     perfw_dl_libnvperf = dlopen("libnvperf_host.so", RTLD_NOW | RTLD_GLOBAL);
102 |     if (!perfw_dl_libnvperf)
103 |     {
104 |         fprintf(stderr, "CUDA library libnvperf_host.so not found.\n");
105 |         return -1;
106 |     }
107 |     perfw_dl_libnvperf_t = dlopen("libnvperf_target.so", RTLD_NOW | RTLD_GLOBAL);
108 |     if (!perfw_dl_libnvperf_t)
109 |     {
110 |         fprintf(stderr, "CUDA library libnvperf_target.so not found.\n");
111 |         return -1;
112 |     }
113 |     perfw_dl_libcupti = dlopen("libcupti.so", RTLD_NOW | RTLD_GLOBAL);
114 |     if (!perfw_dl_libcupti)
115 |     {
{% endraw %}

```
### src/pthread-overload/pthread-overload.c

```c

{% raw %}
221 |     /* Handle dll related stuff */
222 |     do
223 |     {
224 |         handle = dlopen(sosearchpaths[reallpthrindex], RTLD_LAZY);
225 |         if (handle)
226 |         {
{% endraw %}

```
### ext/GOTCHA/src/gotcha_dl.h

```c

{% raw %}
7 | extern void update_all_library_gots(hash_table_t *bindings);
8 | extern int prepare_symbol(struct internal_binding_t *binding);
9 | 
10 | extern gotcha_wrappee_handle_t orig_dlopen_handle;
11 | extern gotcha_wrappee_handle_t orig_dlsym_handle;
12 | 
{% endraw %}

```
### ext/GOTCHA/src/gotcha_dl.c

```c

{% raw %}
6 | 
7 | void* _dl_sym(void* handle, const char* name, void* where);
8 | 
9 | gotcha_wrappee_handle_t orig_dlopen_handle;
10 | gotcha_wrappee_handle_t orig_dlsym_handle;
11 | 
14 |    int result;
15 |    struct internal_binding_t *binding = (struct internal_binding_t *) data;
16 | 
17 |    debug_printf(3, "Trying to re-bind %s from tool %s after dlopen\n",
18 |                 binding->user_binding->name, binding->associated_binding_table->tool->tool_name);
19 |    
25 |    
26 |    result = prepare_symbol(binding);
27 |    if (result == -1) {
28 |       debug_printf(3, "Still could not prepare binding %s after dlopen\n", binding->user_binding->name);
29 |       return 0;
30 |    }
33 |    return 0;
34 | }
35 | 
36 | static void* dlopen_wrapper(const char* filename, int flags) {
37 |    typeof(&dlopen_wrapper) orig_dlopen = gotcha_get_wrappee(orig_dlopen_handle);
38 |    void *handle;
39 |    debug_printf(1, "User called dlopen(%s, 0x%x)\n", filename, (unsigned int) flags);
40 |    handle = orig_dlopen(filename,flags);
41 | 
42 |    debug_printf(2, "Searching new dlopened libraries for previously-not-found exports\n");
43 |    foreach_hash_entry(&notfound_binding_table, NULL, per_binding);
44 | 
45 |    debug_printf(2, "Updating GOT entries for new dlopened libraries\n");
46 |    update_all_library_gots(&function_hash_table);
47 |   
65 | }
66 | 
67 | struct gotcha_binding_t dl_binds[] = {
68 |   {"dlopen", dlopen_wrapper, &orig_dlopen_handle},
69 |   {"dlsym", dlsym_wrapper, &orig_dlsym_handle}
70 | };     
{% endraw %}

```
### ext/GOTCHA/src/gotcha.c

```c

{% raw %}
314 |         debug_printf(2, "Symbol %s needs lookup operation\n", binding->user_binding->name);
315 |         int presult = prepare_symbol(binding);
316 |         if (presult == -1) {
317 |            debug_printf(2, "Stashing %s in notfound_binding table to re-lookup on dlopens\n",
318 |                         binding->user_binding->name);
319 |            addto_hashtable(&notfound_binding_table, (hash_key_t) binding->user_binding->name, (hash_data_t) binding);
{% endraw %}

```
### ext/hwloc/include/hwloc/plugins.h

```c

{% raw %}
419 | #ifdef HWLOC_INSIDE_PLUGIN
420 |   lt_dlhandle handle;
421 |   void *sym;
422 |   handle = lt_dlopen(NULL);
423 |   if (!handle)
424 |     /* cannot check, assume things will work */
{% endraw %}

```
### ext/hwloc/hwloc/components.c

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
### ext/lua/src/loadlib.c

```c

{% raw %}
153 | 
154 | 
155 | static void *lsys_load (lua_State *L, const char *path, int seeglb) {
156 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
157 |   if (lib == NULL) lua_pushstring(L, dlerror());
158 |   return lib;
{% endraw %}

```
### bench/src/ptt2asm.c

```c

{% raw %}
558 |     void* (*owndlsym)(void*, const char*) = dlsym;
559 | 
560 |     dlerror();
561 |     testcase->dlhandle = dlopen(bdata(location), RTLD_LAZY);
562 |     if (!testcase->dlhandle) {
563 |         fprintf(stderr, "Error opening location %s: %s\n", bdata(location), dlerror());
{% endraw %}

```
### bench/includes/likwid.h

```c

{% raw %}
2078 | /*! \brief Initialize the Nvidia GPU performance monitoring facility (Nvmon)
2079 | 
2080 | Initialize the Nvidia GPU performance monitoring feature by creating basic data structures.
2081 | The CUDA and CUPTI library paths need to be in LD_LIBRARY_PATH to be found by dlopen.
2082 | 
2083 | @param [in] nrGpus Amount of GPUs
{% endraw %}

```