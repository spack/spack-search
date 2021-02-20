---
name: "mpich"
layout: package
next_package: multiverso
previous_package: mono
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
298 |     void *libcuda_handle;
299 |     void *libcudart_handle;
300 | 
301 |     libcuda_handle = dlopen("libcuda.so", RTLD_LAZY | RTLD_GLOBAL);
302 |     assert(libcuda_handle);
303 |     libcudart_handle = dlopen("libcudart.so", RTLD_LAZY | RTLD_GLOBAL);
304 |     assert(libcudart_handle);
305 | 
{% endraw %}

```
### src/pm/hydra2/libhydra/topo/hwloc/hwloc/include/hwloc/plugins.h

```c

{% raw %}
350 | #ifdef HWLOC_INSIDE_PLUGIN
351 |   lt_dlhandle handle;
352 |   void *sym;
353 |   handle = lt_dlopen(NULL);
354 |   if (!handle)
355 |     /* cannot check, assume things will work */
{% endraw %}

```
### src/pm/hydra2/libhydra/topo/hwloc/hwloc/hwloc/components.c

```c

{% raw %}
96 |   }
97 | 
98 |   /* dlopen and get the component structure */
99 |   handle = lt_dlopenext(filename);
100 |   if (!handle) {
101 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### src/pm/hydra2/mpl/src/gpu/mpl_gpu_cuda.c

```c

{% raw %}
298 |     void *libcuda_handle;
299 |     void *libcudart_handle;
300 | 
301 |     libcuda_handle = dlopen("libcuda.so", RTLD_LAZY | RTLD_GLOBAL);
302 |     assert(libcuda_handle);
303 |     libcudart_handle = dlopen("libcudart.so", RTLD_LAZY | RTLD_GLOBAL);
304 |     assert(libcudart_handle);
305 | 
{% endraw %}

```
### src/pm/hydra/tools/topo/hwloc/hwloc/include/hwloc/plugins.h

```c

{% raw %}
350 | #ifdef HWLOC_INSIDE_PLUGIN
351 |   lt_dlhandle handle;
352 |   void *sym;
353 |   handle = lt_dlopen(NULL);
354 |   if (!handle)
355 |     /* cannot check, assume things will work */
{% endraw %}

```
### src/pm/hydra/tools/topo/hwloc/hwloc/hwloc/components.c

```c

{% raw %}
96 |   }
97 | 
98 |   /* dlopen and get the component structure */
99 |   handle = lt_dlopenext(filename);
100 |   if (!handle) {
101 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### src/pm/hydra/mpl/src/gpu/mpl_gpu_cuda.c

```c

{% raw %}
298 |     void *libcuda_handle;
299 |     void *libcudart_handle;
300 | 
301 |     libcuda_handle = dlopen("libcuda.so", RTLD_LAZY | RTLD_GLOBAL);
302 |     assert(libcuda_handle);
303 |     libcudart_handle = dlopen("libcudart.so", RTLD_LAZY | RTLD_GLOBAL);
304 |     assert(libcudart_handle);
305 | 
{% endraw %}

```
### src/mpl/src/gpu/mpl_gpu_cuda.c

```c

{% raw %}
298 |     void *libcuda_handle;
299 |     void *libcudart_handle;
300 | 
301 |     libcuda_handle = dlopen("libcuda.so", RTLD_LAZY | RTLD_GLOBAL);
302 |     assert(libcuda_handle);
303 |     libcudart_handle = dlopen("libcudart.so", RTLD_LAZY | RTLD_GLOBAL);
304 |     assert(libcudart_handle);
305 | 
{% endraw %}

```
### modules/libfabric/src/fabric.c

```c

{% raw %}
564 | 		}
565 | 		FI_DBG(&core_prov, FI_LOG_CORE, "opening provider lib %s\n", lib);
566 | 
567 | 		dlhandle = dlopen(lib, RTLD_NOW);
568 | 		free(liblist[n]);
569 | 		if (dlhandle == NULL) {
570 | 			FI_WARN(&core_prov, FI_LOG_CORE,
571 | 			       "dlopen(%s): %s\n", lib, dlerror());
572 | 			free(lib);
573 | 			continue;
632 | 
633 | 	/* If dlopen fails, assume static linking and just return
634 | 	   without error */
635 | 	dlhandle = dlopen(NULL, RTLD_NOW);
636 | 	if (dlhandle == NULL) {
637 | 		goto libdl_done;
{% endraw %}

```
### modules/libfabric/prov/util/src/util_mem_hooks.c

```c

{% raw %}
84 | 	OFI_INTERCEPT_MAX
85 | };
86 | 
87 | static void *ofi_intercept_dlopen(const char *filename, int flag);
88 | static void *ofi_intercept_mmap(void *start, size_t length,
89 | 				int prot, int flags, int fd, off_t offset);
96 | static int ofi_intercept_brk(const void *brkaddr);
97 | 
98 | static struct ofi_intercept intercepts[] = {
99 | 	[OFI_INTERCEPT_DLOPEN] = { .symbol = "dlopen",
100 | 				.our_func = ofi_intercept_dlopen},
101 | 	[OFI_INTERCEPT_MMAP] = { .symbol = "mmap",
102 | 				.our_func = ofi_intercept_mmap},
115 | };
116 | 
117 | struct ofi_mem_calls {
118 | 	void *(*dlopen) (const char *, int);
119 | 	void *(*mmap)(void *, size_t, int, int, int, off_t);
120 | 	int (*munmap)(void *, size_t);
242 | 	return ret;
243 | }
244 | 
245 | static void *ofi_intercept_dlopen(const char *filename, int flag)
246 | {
247 | 	struct ofi_intercept  *intercept;
248 | 	void *handle;
249 | 
250 | 	handle = real_calls.dlopen(filename, flag);
251 | 	if (!handle)
252 | 		return NULL;
482 | 		dlist_init(&intercepts[i].dl_intercept_list);
483 | 
484 | 	ret = ofi_intercept_symbol(&intercepts[OFI_INTERCEPT_DLOPEN],
485 | 				   (void **) &real_calls.dlopen);
486 | 	if (ret) {
487 | 		FI_WARN(&core_prov, FI_LOG_MR,
488 | 		       "intercept dlopen failed %d %s\n", ret, fi_strerror(ret));
489 | 		return ret;
490 | 	}
{% endraw %}

```
### modules/hwloc/include/hwloc/plugins.h

```c

{% raw %}
350 | #ifdef HWLOC_INSIDE_PLUGIN
351 |   lt_dlhandle handle;
352 |   void *sym;
353 |   handle = lt_dlopen(NULL);
354 |   if (!handle)
355 |     /* cannot check, assume things will work */
{% endraw %}

```
### modules/hwloc/hwloc/components.c

```c

{% raw %}
96 |   }
97 | 
98 |   /* dlopen and get the component structure */
99 |   handle = lt_dlopenext(filename);
100 |   if (!handle) {
101 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### modules/ucx/src/ucm/util/sys.c

```c

{% raw %}
40 |     .enable_cuda_reloc          = 1,
41 |     .enable_dynamic_mmap_thresh = 1,
42 |     .alloc_alignment            = 16,
43 |     .dlopen_process_rpath       = 1
44 | };
45 | 
300 |      * NODELETE flag to the dynamic link map.
301 |      */
302 |     (void)dlerror();
303 |     dl = dlopen(info.dli_fname, RTLD_LOCAL|RTLD_LAZY|RTLD_NODELETE);
304 |     if (dl == NULL) {
305 |         ucm_warn("failed to load '%s': %s", info.dli_fname, dlerror());
{% endraw %}

```
### modules/ucx/src/ucm/util/reloc.c

```c

{% raw %}
33 | #include <link.h>
34 | #include <limits.h>
35 | 
36 | typedef void * (*ucm_reloc_dlopen_func_t)(const char *, int);
37 | typedef int    (*ucm_reloc_dlclose_func_t)(void *);
38 | 
64 | static pthread_mutex_t ucm_reloc_patch_list_lock = PTHREAD_MUTEX_INITIALIZER;
65 | 
66 | static khash_t(ucm_dl_info_hash) ucm_dl_info_hash;
67 | static ucm_reloc_dlopen_func_t  ucm_reloc_orig_dlopen  = NULL;
68 | static ucm_reloc_dlclose_func_t ucm_reloc_orig_dlclose = NULL;
69 | 
462 | 
463 | /* read serinfo from 'module_path', result buffer must be destroyed
464 |  * by free() call */
465 | static Dl_serinfo *ucm_dlopen_load_serinfo(const char *module_path)
466 | {
467 |     Dl_serinfo *serinfo = NULL;
469 |     void *module;
470 |     int res;
471 | 
472 |     module = ucm_reloc_orig_dlopen(module_path, RTLD_LAZY);
473 |     if (module == NULL) { /* requested module can't be loaded */
474 |         ucm_debug("failed to open %s: %s", module_path, dlerror());
502 |     return serinfo;
503 | }
504 | 
505 | void *ucm_dlopen(const char *filename, int flag)
506 | {
507 |     void *handle;
517 | 
518 |     ucm_reloc_get_orig_dl_funcs();
519 | 
520 |     if (!ucm_global_opts.dlopen_process_rpath) {
521 |         goto fallback_load_lib;
522 |     }
539 |         goto fallback_load_lib;
540 |     }
541 | 
542 |     serinfo = ucm_dlopen_load_serinfo(dl_info.dli_fname);
543 |     if (serinfo == NULL) {
544 |         /* failed to load serinfo, try just dlopen */
557 | 
558 |         free(serinfo);
559 |         /* ok, file exists, let's try to load it */
560 |         handle = ucm_reloc_orig_dlopen(file_path, flag);
561 |         if (handle == NULL) {
562 |             return NULL;
569 |     /* ok, we can't lookup module in dirs listed in caller module,
570 |      * let's fallback to legacy mode */
571 | fallback_load_lib:
572 |     handle = ucm_reloc_orig_dlopen(filename, flag);
573 |     if (handle == NULL) {
574 |         return NULL;
582 |      * loaded due to dependencies.
583 |      */
584 | 
585 |     ucm_trace("dlopen(%s) = %p", filename, handle);
586 | 
587 |     pthread_mutex_lock(&ucm_reloc_patch_list_lock);
588 |     ucs_list_for_each(patch, &ucm_reloc_patch_list, list) {
589 |         ucm_debug("in dlopen(%s), re-applying '%s' to %p", filename,
590 |                   patch->symbol, patch->value);
591 |         ucm_reloc_apply_patch(patch, 0);
628 |     return ucm_reloc_orig_dlclose(handle);
629 | }
630 | 
631 | static ucm_reloc_patch_t ucm_dlopen_reloc_patches[] = {
632 |     { .symbol = "dlopen",  .value  = ucm_dlopen  },
633 |     { .symbol = "dlclose", .value  = ucm_dlclose }
634 | };
638 |     ucm_reloc_patch_t *patch;
639 | 
640 |     /* pointer to original dlopen() */
641 |     if (ucm_reloc_orig_dlopen == NULL) {
642 |         patch                 = &ucm_dlopen_reloc_patches[0];
643 |         ucm_reloc_orig_dlopen = (ucm_reloc_dlopen_func_t)
644 |                                 ucm_reloc_get_orig(patch->symbol, patch->value);
645 |         if (ucm_reloc_orig_dlopen == NULL) {
646 |             ucm_fatal("ucm_reloc_orig_dlopen is NULL");
647 |         }
648 |     }
649 | 
650 |     /* pointer to original dlclose() */
651 |     if (ucm_reloc_orig_dlclose == NULL) {
652 |         patch                  = &ucm_dlopen_reloc_patches[1];
653 |         ucm_reloc_orig_dlclose = (ucm_reloc_dlclose_func_t)
654 |                                  ucm_reloc_get_orig(patch->symbol, patch->value);
669 |         return UCS_OK;
670 |     }
671 | 
672 |     for (i = 0; i < ucs_array_size(ucm_dlopen_reloc_patches); ++i) {
673 |         status = ucm_reloc_apply_patch(&ucm_dlopen_reloc_patches[i], 0);
674 |         if (status != UCS_OK) {
675 |             return status;
676 |         }
677 | 
678 |         ucs_list_add_tail(&ucm_reloc_patch_list, &ucm_dlopen_reloc_patches[i].list);
679 |     }
680 | 
{% endraw %}

```
### modules/ucx/src/ucm/api/ucm.h

```c

{% raw %}
193 |     int                  enable_cuda_reloc;           /* Enable installing CUDA relocations */
194 |     int                  enable_dynamic_mmap_thresh;  /* Enable adaptive mmap threshold */
195 |     size_t               alloc_alignment;             /* Alignment for memory allocations */
196 |     int                  dlopen_process_rpath;        /* Process RPATH section in dlopen hook */
197 | } ucm_global_config_t;
198 | 
459 |  * @brief Call the original implementation of @ref dlopen and all handlers
460 |  * associated with it.
461 |  */
462 | void *ucm_dlopen(const char *filename, int flag);
463 | 
464 | 
{% endraw %}

```
### modules/ucx/src/ucs/config/ucm_opts.c

```c

{% raw %}
76 | 
77 |   {"DLOPEN_PROCESS_RPATH", "yes",
78 |    "Process RPATH section of caller module during dynamic libraries opening.",
79 |    ucs_offsetof(ucm_global_config_t, dlopen_process_rpath),
80 |    UCS_CONFIG_TYPE_BOOL},
81 | 
{% endraw %}

```
### modules/ucx/src/ucs/sys/module.c

```c

{% raw %}
221 | 
222 |         /* Clear error state */
223 |         (void)dlerror();
224 |         dl = dlopen(module_path, mode);
225 |         if (dl != NULL) {
226 |             ucs_module_init(module_path, dl);
228 |         } else {
229 |             /* If a module fails to load, silently give up */
230 |             error = dlerror();
231 |             ucs_module_debug("dlopen('%s', mode=0x%x) failed: %s", module_path,
232 |                              mode, error ? error : "Unknown error");
233 |         }
{% endraw %}

```
### modules/ucx/test/mpi/test_memhooks.c

```c

{% raw %}
104 | 
105 | void* open_dyn_lib(const char *lib_path)
106 | {
107 |     void *dl = dlopen(lib_path, RTLD_LAZY);
108 |     char *error;
109 | 
{% endraw %}

```
### modules/ucx/test/gtest/ucm/malloc_hook.cc

```cpp

{% raw %}
1198 |     EXPECT_TRUE(status == UCS_OK);
1199 | }
1200 | 
1201 | class malloc_hook_dlopen : public malloc_hook {
1202 | protected:
1203 |     class library {
1267 |     }
1268 | 
1269 |     static std::string get_lib_path_do_load() {
1270 |         return get_lib_dir() + "/libdlopen_test_do_load.so";
1271 |     }
1272 | 
1273 |     static std::string get_lib_path_do_mmap() {
1274 |         return get_lib_dir() + "/libdlopen_test_do_mmap.so";
1275 |     }
1276 | 
1277 |     static std::string get_lib_path_do_load_rpath() {
1278 |         return get_lib_dir() + "/libdlopen_test_do_load_rpath.so";
1279 |     }
1280 | 
1281 |     static std::string get_lib_path_do_load_sub_rpath() {
1282 |         return "libdlopen_test_rpath.so"; // library should be located using rpath
1283 |     }
1284 | 
1285 |     /* test for mmap events are fired from non-direct load modules
1286 |      * we are trying to load lib1, from lib1 load lib2, and
1287 |      * fire mmap event from lib2 */
1288 |     void test_indirect_dlopen(loader_t loader)
1289 |     {
1290 |         typedef void (*fire_mmap_f)(void);
1321 |     }
1322 | 
1323 |     /* Test for rpath section of caller module is processes */
1324 |     void test_rpath_dlopen(loader_t loader)
1325 |     {
1326 |         typedef void* (*load_lib_f)(const char *path, void* (*func)(const char*, int));
1365 |         ASSERT_TRUE(lib2);
1366 |     }
1367 | 
1368 |     void test_dlopen_null(loader_t loader)
1369 |     {
1370 |         library lib(loader);
1374 |     }
1375 | };
1376 | 
1377 | UCS_TEST_F(malloc_hook_dlopen, indirect_dlopen) {
1378 |     test_indirect_dlopen(dlopen);
1379 | }
1380 | 
1381 | UCS_TEST_F(malloc_hook_dlopen, indirect_ucm_dlopen) {
1382 |     test_indirect_dlopen(ucm_dlopen);
1383 | }
1384 | 
1385 | UCS_TEST_F(malloc_hook_dlopen, rpath_dlopen) {
1386 |     test_rpath_dlopen(dlopen);
1387 | }
1388 | 
1389 | UCS_TEST_F(malloc_hook_dlopen, rpath_ucm_dlopen) {
1390 |     test_rpath_dlopen(ucm_dlopen);
1391 | }
1392 | 
1393 | UCS_TEST_F(malloc_hook_dlopen, ucm_dlopen_null_dlopen) {
1394 |     test_dlopen_null(dlopen);
1395 | }
1396 | 
1397 | UCS_TEST_F(malloc_hook_dlopen, ucm_dlopen_null_ucm_dlopen) {
1398 |     test_dlopen_null(ucm_dlopen);
1399 | }
1400 | 
1401 | UCS_MT_TEST_F(malloc_hook_dlopen, dlopen_mt_with_memtype, 2) {
1402 | #ifndef GTEST_UCM_HOOK_LIB_DIR
1403 | #  error "Missing build configuration"
1418 |          * iterating over loaded libraries.
1419 |          */
1420 |         if (ucs_atomic_fadd32(&count, 1) % 2) {
1421 |             void *lib1 = dlopen(get_lib_path_do_mmap().c_str(), RTLD_LAZY);
1422 |             ASSERT_TRUE(lib1 != NULL);
1423 |             dlclose(lib1);
1424 |         } else {
1425 |             void *lib2 = dlopen(get_lib_path_do_load().c_str(), RTLD_LAZY);
1426 |             ASSERT_TRUE(lib2 != NULL);
1427 |             dlclose(lib2);
{% endraw %}

```
### modules/ucx/test/gtest/ucm/test_dlopen/dlopen_test_do_load.c

```c

{% raw %}
10 | UCS_F_NOOPTIMIZE /* prevent using tail recursion unwind */
11 | void* load_lib(const char *path, void* (*load_func)(const char*, int))
12 | {
13 |     return (load_func ? load_func : dlopen)(path, RTLD_NOW);
14 | }
15 | 
{% endraw %}

```
### modules/ucx/test/apps/test_link_map.c

```c

{% raw %}
30 |      * could not be loaded due to libcuda dependency, because of a corrupted
31 |      * link_map in the program.
32 |      */
33 |     dlopen("libgcc_s.so.1", RTLD_LAZY);
34 | 
35 |     ucp_cleanup(context);
{% endraw %}

```
### modules/ucx/test/apps/test_tcmalloc.c

```c

{% raw %}
22 |         return -1;
23 |     }
24 | 
25 |     dlopen("libselinux.so", RTLD_LAZY);
26 | 
27 |     ucp_cleanup(context);
{% endraw %}

```
### modules/ucx/test/apps/test_dlopen_cfg_print.c

```c

{% raw %}
11 | #define QUOTE(x) _QUOTE(x)
12 | 
13 | 
14 | static void* do_dlopen_or_exit(const char *filename)
15 | {
16 |     void *handle;
17 | 
18 |     (void)dlerror();
19 |     printf("opening '%s'\n", filename);
20 |     handle = dlopen(filename, RTLD_LAZY);
21 |     if (handle == NULL) {
22 |         fprintf(stderr, "failed to open %s: %s\n", filename,
38 | 
39 |     /* unload and reload uct while ucs is loaded
40 |      * would fail if uct global vars are kept on global lists in ucs */
41 |     ucs_handle = do_dlopen_or_exit(ucs_filename);
42 |     for (i = 0; i < 2; ++i) {
43 |         uct_handle = do_dlopen_or_exit(uct_filename);
44 |         dlclose(uct_handle);
45 |     }
{% endraw %}

```
### modules/ucx/test/apps/test_ucs_dlopen.c

```c

{% raw %}
87 |     /* load ucm */
88 |     printf("opening '%s'\n", filename);
89 |     dlerror();
90 |     handle = dlopen(filename, RTLD_NOW);
91 |     if (handle == NULL) {
92 |         fprintf(stderr, "failed to open %s: %s\n", filename, dlerror());
93 |         ret = -1;
94 |         goto failed_dlopen;
95 |     }
96 | 
100 |     /* unload ucp */
101 |     dlclose(handle);
102 | 
103 | failed_dlopen:
104 |     /* release the memory - could break if UCM is unloaded */
105 |     munmap(ptr2, alloc_size);
{% endraw %}

```
### modules/ucx/test/apps/test_ucp_dlopen.c

```c

{% raw %}
94 | 
95 |     /* load ucp */
96 |     printf("opening '%s'\n", filename);
97 |     handle = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
98 |     if (handle == NULL) {
99 |         fprintf(stderr, "failed to open %s: %m\n", filename);
100 |         ret = -1;
101 |         goto failed_dlopen;
102 |     }
103 | 
107 |     /* unload ucp */
108 |     dlclose(handle);
109 | 
110 | failed_dlopen:
111 |     /* relase the memory - could break if UCM is unloaded */
112 |     munmap(ptr2, alloc_size);
{% endraw %}

```