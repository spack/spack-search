---
name: "likwid"
layout: package
next_package: llvm-openmp
previous_package: libdmx
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
110 |     topo_dl_libcuda = dlopen("libcuda.so", RTLD_NOW | RTLD_GLOBAL);
116 |     topo_dl_libcudart = dlopen("libcudart.so", RTLD_NOW | RTLD_GLOBAL | RTLD_NODELETE);
{% endraw %}

```
### src/includes/likwid.h

```c

{% raw %}
2081 | The CUDA and CUPTI library paths need to be in LD_LIBRARY_PATH to be found by dlopen.
{% endraw %}

```
### src/includes/nvmon_cupti.h

```c

{% raw %}
126 |     dl_libcuda = dlopen("libcuda.so", RTLD_NOW | RTLD_GLOBAL);
143 |     dl_libcudart = dlopen("libcudart.so", RTLD_NOW | RTLD_GLOBAL | RTLD_NODELETE);
153 |     dl_libcupti = dlopen("libcupti.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/includes/nvmon_perfworks.h

```c

{% raw %}
95 |     perfw_dl_libcuda = dlopen("libcuda.so", RTLD_NOW | RTLD_GLOBAL);
101 |     perfw_dl_libnvperf = dlopen("libnvperf_host.so", RTLD_NOW | RTLD_GLOBAL);
107 |     perfw_dl_libnvperf_t = dlopen("libnvperf_target.so", RTLD_NOW | RTLD_GLOBAL);
113 |     perfw_dl_libcupti = dlopen("libcupti.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/pthread-overload/pthread-overload.c

```c

{% raw %}
224 |         handle = dlopen(sosearchpaths[reallpthrindex], RTLD_LAZY);
{% endraw %}

```
### ext/GOTCHA/src/gotcha_dl.h

```c

{% raw %}
10 | extern gotcha_wrappee_handle_t orig_dlopen_handle;
{% endraw %}

```
### ext/GOTCHA/src/gotcha_dl.c

```c

{% raw %}
9 | gotcha_wrappee_handle_t orig_dlopen_handle;
17 |    debug_printf(3, "Trying to re-bind %s from tool %s after dlopen\n",
28 |       debug_printf(3, "Still could not prepare binding %s after dlopen\n", binding->user_binding->name);
36 | static void* dlopen_wrapper(const char* filename, int flags) {
37 |    typeof(&dlopen_wrapper) orig_dlopen = gotcha_get_wrappee(orig_dlopen_handle);
39 |    debug_printf(1, "User called dlopen(%s, 0x%x)\n", filename, (unsigned int) flags);
40 |    handle = orig_dlopen(filename,flags);
42 |    debug_printf(2, "Searching new dlopened libraries for previously-not-found exports\n");
45 |    debug_printf(2, "Updating GOT entries for new dlopened libraries\n");
68 |   {"dlopen", dlopen_wrapper, &orig_dlopen_handle},
{% endraw %}

```
### ext/GOTCHA/src/gotcha.c

```c

{% raw %}
317 |            debug_printf(2, "Stashing %s in notfound_binding table to re-lookup on dlopens\n",
{% endraw %}

```
### ext/hwloc/include/hwloc/plugins.h

```c

{% raw %}
422 |   handle = lt_dlopen(NULL);
{% endraw %}

```
### ext/hwloc/hwloc/components.c

```c

{% raw %}
100 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### ext/lua/src/loadlib.c

```c

{% raw %}
156 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```
### bench/src/ptt2asm.c

```c

{% raw %}
561 |     testcase->dlhandle = dlopen(bdata(location), RTLD_LAZY);
{% endraw %}

```
### bench/includes/likwid.h

```c

{% raw %}
2081 | The CUDA and CUPTI library paths need to be in LD_LIBRARY_PATH to be found by dlopen.
{% endraw %}

```