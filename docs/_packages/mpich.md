---
name: "mpich"
layout: package
next_package: py-petsc4py
previous_package: libgpuarray
languages: ['cpp', 'c']
---
## 3.4.1
142 / 13322 files match, 25 filtered matches.

 - [src/mpi/romio/mpl/src/gpu/mpl_gpu_cuda.c](#srcmpiromiomplsrcgpumpl_gpu_cudac)
 - [src/pm/hydra2/libhydra/topo/hwloc/hwloc/include/hwloc/plugins.h](#srcpmhydra2libhydratopohwlochwlocincludehwlocpluginsh)
 - [src/pm/hydra2/libhydra/topo/hwloc/hwloc/hwloc/components.c](#srcpmhydra2libhydratopohwlochwlochwloccomponentsc)
 - [src/pm/hydra2/mpl/src/gpu/mpl_gpu_cuda.c](#srcpmhydra2mplsrcgpumpl_gpu_cudac)
 - [src/pm/hydra/tools/topo/hwloc/hwloc/include/hwloc/plugins.h](#srcpmhydratoolstopohwlochwlocincludehwlocpluginsh)
 - [src/pm/hydra/tools/topo/hwloc/hwloc/hwloc/components.c](#srcpmhydratoolstopohwlochwlochwloccomponentsc)
 - [src/pm/hydra/mpl/src/gpu/mpl_gpu_cuda.c](#srcpmhydramplsrcgpumpl_gpu_cudac)
 - [src/mpl/src/gpu/mpl_gpu_cuda.c](#srcmplsrcgpumpl_gpu_cudac)
 - [modules/libfabric/src/fabric.c](#moduleslibfabricsrcfabricc)
 - [modules/libfabric/prov/util/src/util_mem_hooks.c](#moduleslibfabricprovutilsrcutil_mem_hooksc)
 - [modules/hwloc/include/hwloc/plugins.h](#moduleshwlocincludehwlocpluginsh)
 - [modules/hwloc/hwloc/components.c](#moduleshwlochwloccomponentsc)
 - [modules/ucx/src/ucm/util/sys.c](#modulesucxsrcucmutilsysc)
 - [modules/ucx/src/ucm/util/reloc.c](#modulesucxsrcucmutilrelocc)
 - [modules/ucx/src/ucm/api/ucm.h](#modulesucxsrcucmapiucmh)
 - [modules/ucx/src/ucs/config/ucm_opts.c](#modulesucxsrcucsconfigucm_optsc)
 - [modules/ucx/src/ucs/sys/module.c](#modulesucxsrcucssysmodulec)
 - [modules/ucx/test/mpi/test_memhooks.c](#modulesucxtestmpitest_memhooksc)
 - [modules/ucx/test/gtest/ucm/malloc_hook.cc](#modulesucxtestgtestucmmalloc_hookcc)
 - [modules/ucx/test/gtest/ucm/test_dlopen/dlopen_test_do_load.c](#modulesucxtestgtestucmtest_dlopendlopen_test_do_loadc)
 - [modules/ucx/test/apps/test_link_map.c](#modulesucxtestappstest_link_mapc)
 - [modules/ucx/test/apps/test_tcmalloc.c](#modulesucxtestappstest_tcmallocc)
 - [modules/ucx/test/apps/test_dlopen_cfg_print.c](#modulesucxtestappstest_dlopen_cfg_printc)
 - [modules/ucx/test/apps/test_ucs_dlopen.c](#modulesucxtestappstest_ucs_dlopenc)
 - [modules/ucx/test/apps/test_ucp_dlopen.c](#modulesucxtestappstest_ucp_dlopenc)

### src/mpi/romio/mpl/src/gpu/mpl_gpu_cuda.c

```c

{% raw %}
301 |     libcuda_handle = dlopen("libcuda.so", RTLD_LAZY | RTLD_GLOBAL);
303 |     libcudart_handle = dlopen("libcudart.so", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### src/pm/hydra2/libhydra/topo/hwloc/hwloc/include/hwloc/plugins.h

```c

{% raw %}
353 |   handle = lt_dlopen(NULL);
{% endraw %}

```
### src/pm/hydra2/libhydra/topo/hwloc/hwloc/hwloc/components.c

```c

{% raw %}
99 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### src/pm/hydra2/mpl/src/gpu/mpl_gpu_cuda.c

```c

{% raw %}
301 |     libcuda_handle = dlopen("libcuda.so", RTLD_LAZY | RTLD_GLOBAL);
303 |     libcudart_handle = dlopen("libcudart.so", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### src/pm/hydra/tools/topo/hwloc/hwloc/include/hwloc/plugins.h

```c

{% raw %}
353 |   handle = lt_dlopen(NULL);
{% endraw %}

```
### src/pm/hydra/tools/topo/hwloc/hwloc/hwloc/components.c

```c

{% raw %}
99 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### src/pm/hydra/mpl/src/gpu/mpl_gpu_cuda.c

```c

{% raw %}
301 |     libcuda_handle = dlopen("libcuda.so", RTLD_LAZY | RTLD_GLOBAL);
303 |     libcudart_handle = dlopen("libcudart.so", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### src/mpl/src/gpu/mpl_gpu_cuda.c

```c

{% raw %}
301 |     libcuda_handle = dlopen("libcuda.so", RTLD_LAZY | RTLD_GLOBAL);
303 |     libcudart_handle = dlopen("libcudart.so", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### modules/libfabric/src/fabric.c

```c

{% raw %}
567 | 		dlhandle = dlopen(lib, RTLD_NOW);
571 | 			       "dlopen(%s): %s\n", lib, dlerror());
635 | 	dlhandle = dlopen(NULL, RTLD_NOW);
{% endraw %}

```
### modules/libfabric/prov/util/src/util_mem_hooks.c

```c

{% raw %}
87 | static void *ofi_intercept_dlopen(const char *filename, int flag);
99 | 	[OFI_INTERCEPT_DLOPEN] = { .symbol = "dlopen",
100 | 				.our_func = ofi_intercept_dlopen},
118 | 	void *(*dlopen) (const char *, int);
245 | static void *ofi_intercept_dlopen(const char *filename, int flag)
250 | 	handle = real_calls.dlopen(filename, flag);
485 | 				   (void **) &real_calls.dlopen);
488 | 		       "intercept dlopen failed %d %s\n", ret, fi_strerror(ret));
{% endraw %}

```
### modules/hwloc/include/hwloc/plugins.h

```c

{% raw %}
353 |   handle = lt_dlopen(NULL);
{% endraw %}

```
### modules/hwloc/hwloc/components.c

```c

{% raw %}
99 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### modules/ucx/src/ucm/util/sys.c

```c

{% raw %}
43 |     .dlopen_process_rpath       = 1
303 |     dl = dlopen(info.dli_fname, RTLD_LOCAL|RTLD_LAZY|RTLD_NODELETE);
{% endraw %}

```
### modules/ucx/src/ucm/util/reloc.c

```c

{% raw %}
36 | typedef void * (*ucm_reloc_dlopen_func_t)(const char *, int);
67 | static ucm_reloc_dlopen_func_t  ucm_reloc_orig_dlopen  = NULL;
465 | static Dl_serinfo *ucm_dlopen_load_serinfo(const char *module_path)
472 |     module = ucm_reloc_orig_dlopen(module_path, RTLD_LAZY);
505 | void *ucm_dlopen(const char *filename, int flag)
520 |     if (!ucm_global_opts.dlopen_process_rpath) {
542 |     serinfo = ucm_dlopen_load_serinfo(dl_info.dli_fname);
560 |         handle = ucm_reloc_orig_dlopen(file_path, flag);
572 |     handle = ucm_reloc_orig_dlopen(filename, flag);
585 |     ucm_trace("dlopen(%s) = %p", filename, handle);
589 |         ucm_debug("in dlopen(%s), re-applying '%s' to %p", filename,
631 | static ucm_reloc_patch_t ucm_dlopen_reloc_patches[] = {
632 |     { .symbol = "dlopen",  .value  = ucm_dlopen  },
641 |     if (ucm_reloc_orig_dlopen == NULL) {
642 |         patch                 = &ucm_dlopen_reloc_patches[0];
643 |         ucm_reloc_orig_dlopen = (ucm_reloc_dlopen_func_t)
645 |         if (ucm_reloc_orig_dlopen == NULL) {
646 |             ucm_fatal("ucm_reloc_orig_dlopen is NULL");
652 |         patch                  = &ucm_dlopen_reloc_patches[1];
672 |     for (i = 0; i < ucs_array_size(ucm_dlopen_reloc_patches); ++i) {
673 |         status = ucm_reloc_apply_patch(&ucm_dlopen_reloc_patches[i], 0);
678 |         ucs_list_add_tail(&ucm_reloc_patch_list, &ucm_dlopen_reloc_patches[i].list);
{% endraw %}

```
### modules/ucx/src/ucm/api/ucm.h

```c

{% raw %}
196 |     int                  dlopen_process_rpath;        /* Process RPATH section in dlopen hook */
462 | void *ucm_dlopen(const char *filename, int flag);
{% endraw %}

```
### modules/ucx/src/ucs/config/ucm_opts.c

```c

{% raw %}
79 |    ucs_offsetof(ucm_global_config_t, dlopen_process_rpath),
{% endraw %}

```
### modules/ucx/src/ucs/sys/module.c

```c

{% raw %}
224 |         dl = dlopen(module_path, mode);
231 |             ucs_module_debug("dlopen('%s', mode=0x%x) failed: %s", module_path,
{% endraw %}

```
### modules/ucx/test/mpi/test_memhooks.c

```c

{% raw %}
107 |     void *dl = dlopen(lib_path, RTLD_LAZY);
{% endraw %}

```
### modules/ucx/test/gtest/ucm/malloc_hook.cc

```cpp

{% raw %}
1201 | class malloc_hook_dlopen : public malloc_hook {
1270 |         return get_lib_dir() + "/libdlopen_test_do_load.so";
1274 |         return get_lib_dir() + "/libdlopen_test_do_mmap.so";
1278 |         return get_lib_dir() + "/libdlopen_test_do_load_rpath.so";
1282 |         return "libdlopen_test_rpath.so"; // library should be located using rpath
1288 |     void test_indirect_dlopen(loader_t loader)
1324 |     void test_rpath_dlopen(loader_t loader)
1368 |     void test_dlopen_null(loader_t loader)
1377 | UCS_TEST_F(malloc_hook_dlopen, indirect_dlopen) {
1378 |     test_indirect_dlopen(dlopen);
1381 | UCS_TEST_F(malloc_hook_dlopen, indirect_ucm_dlopen) {
1382 |     test_indirect_dlopen(ucm_dlopen);
1385 | UCS_TEST_F(malloc_hook_dlopen, rpath_dlopen) {
1386 |     test_rpath_dlopen(dlopen);
1389 | UCS_TEST_F(malloc_hook_dlopen, rpath_ucm_dlopen) {
1390 |     test_rpath_dlopen(ucm_dlopen);
1393 | UCS_TEST_F(malloc_hook_dlopen, ucm_dlopen_null_dlopen) {
1394 |     test_dlopen_null(dlopen);
1397 | UCS_TEST_F(malloc_hook_dlopen, ucm_dlopen_null_ucm_dlopen) {
1398 |     test_dlopen_null(ucm_dlopen);
1401 | UCS_MT_TEST_F(malloc_hook_dlopen, dlopen_mt_with_memtype, 2) {
1421 |             void *lib1 = dlopen(get_lib_path_do_mmap().c_str(), RTLD_LAZY);
1425 |             void *lib2 = dlopen(get_lib_path_do_load().c_str(), RTLD_LAZY);
{% endraw %}

```
### modules/ucx/test/gtest/ucm/test_dlopen/dlopen_test_do_load.c

```c

{% raw %}
13 |     return (load_func ? load_func : dlopen)(path, RTLD_NOW);
{% endraw %}

```
### modules/ucx/test/apps/test_link_map.c

```c

{% raw %}
33 |     dlopen("libgcc_s.so.1", RTLD_LAZY);
{% endraw %}

```
### modules/ucx/test/apps/test_tcmalloc.c

```c

{% raw %}
25 |     dlopen("libselinux.so", RTLD_LAZY);
{% endraw %}

```
### modules/ucx/test/apps/test_dlopen_cfg_print.c

```c

{% raw %}
14 | static void* do_dlopen_or_exit(const char *filename)
20 |     handle = dlopen(filename, RTLD_LAZY);
41 |     ucs_handle = do_dlopen_or_exit(ucs_filename);
43 |         uct_handle = do_dlopen_or_exit(uct_filename);
{% endraw %}

```
### modules/ucx/test/apps/test_ucs_dlopen.c

```c

{% raw %}
90 |     handle = dlopen(filename, RTLD_NOW);
94 |         goto failed_dlopen;
103 | failed_dlopen:
{% endraw %}

```
### modules/ucx/test/apps/test_ucp_dlopen.c

```c

{% raw %}
97 |     handle = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
101 |         goto failed_dlopen;
110 | failed_dlopen:
{% endraw %}

```