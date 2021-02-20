---
name: "sst-transports"
layout: package
next_package: stacks
previous_package: sst-macro
languages: ['c']
---
## master
2 / 171 files match, 2 filtered matches.

 - [libfabric/src/fabric.c](#libfabricsrcfabricc)
 - [libfabric/prov/util/src/util_mem_hooks.c](#libfabricprovutilsrcutil_mem_hooksc)

### libfabric/src/fabric.c

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
### libfabric/prov/util/src/util_mem_hooks.c

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