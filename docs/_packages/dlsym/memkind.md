---
name: "memkind"
layout: package
next_package: nettle
previous_package: dpdk
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.9.0
7 / 482 files match, 4 filtered matches.

 - [src/tbb_wrapper.c](#srctbb_wrapperc)
 - [test/load_tbbmalloc_symbols.c](#testload_tbbmalloc_symbolsc)
 - [jemalloc/src/background_thread.c](#jemallocsrcbackground_threadc)
 - [jemalloc/src/ctl.c](#jemallocsrcctlc)

### src/tbb_wrapper.c

```c

{% raw %}
57 |         abort();
58 |     }
59 | 
60 |     pool_malloc = dlsym(tbb_handle, "_ZN3rml11pool_mallocEPNS_10MemoryPoolEm");
61 |     pool_realloc = dlsym(tbb_handle, "_ZN3rml12pool_reallocEPNS_10MemoryPoolEPvm");
62 |     pool_aligned_malloc = dlsym(tbb_handle,
63 |                                 "_ZN3rml19pool_aligned_mallocEPNS_10MemoryPoolEmm");
64 |     pool_free = dlsym(tbb_handle, "_ZN3rml9pool_freeEPNS_10MemoryPoolEPv");
65 |     pool_create_v1 = dlsym(tbb_handle,
66 |                            "_ZN3rml14pool_create_v1ElPKNS_13MemPoolPolicyEPPNS_10MemoryPoolE");
67 |     pool_destroy = dlsym(tbb_handle, "_ZN3rml12pool_destroyEPNS_10MemoryPoolE");
68 |     pool_identify = dlsym(tbb_handle, "_ZN3rml13pool_identifyEPv");
69 |     pool_msize = dlsym(tbb_handle, "_ZN3rml10pool_msizeEPNS_10MemoryPoolEPv");
70 | 
71 |     if(!pool_malloc ||
{% endraw %}

```
### test/load_tbbmalloc_symbols.c

```c

{% raw %}
32 |         return -1;
33 |     }
34 | 
35 |     scalable_malloc = dlsym(tbb_handle, "scalable_malloc");
36 |     if(!scalable_malloc) {
37 |         printf("Cannot load scalable_malloc symbol from %s\n", so_name);
38 |         return -1;
39 |     }
40 | 
41 |     scalable_realloc = dlsym(tbb_handle, "scalable_realloc");
42 |     if(!scalable_realloc) {
43 |         printf("Cannot load scalable_realloc symbol from %s\n", so_name);
44 |         return -1;
45 |     }
46 | 
47 |     scalable_calloc = dlsym(tbb_handle, "scalable_calloc");
48 |     if(!scalable_calloc) {
49 |         printf("Cannot load scalable_calloc symbol from %s\n", so_name);
50 |         return -1;
51 |     }
52 | 
53 |     scalable_free = dlsym(tbb_handle, "scalable_free");
54 |     if(!scalable_free) {
55 |         printf("Cannot load scalable_free symbol from %s\n", so_name);
{% endraw %}

```
### jemalloc/src/background_thread.c

```c

{% raw %}
817 | 	}
818 | 
819 | #ifdef JEMALLOC_PTHREAD_CREATE_WRAPPER
820 | 	pthread_create_fptr = dlsym(RTLD_NEXT, "pthread_create");
821 | 	if (pthread_create_fptr == NULL) {
822 | 		can_enable_background_thread = false;
823 | 		if (config_lazy_lock || opt_background_thread) {
824 | 			malloc_write("<jemalloc>: Error in dlsym(RTLD_NEXT, "
825 | 			    "\"pthread_create\")\n");
826 | 			abort();
{% endraw %}

```
### jemalloc/src/ctl.c

```c

{% raw %}
1524 | 		background_thread_enabled_set(tsd_tsdn(tsd), newval);
1525 | 		if (newval) {
1526 | 			if (!can_enable_background_thread) {
1527 | 				malloc_printf("<jemalloc>: Error in dlsym("
1528 | 			            "RTLD_NEXT, \"pthread_create\"). Cannot "
1529 | 				    "enable background_thread\n");
{% endraw %}

```