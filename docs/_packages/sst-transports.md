---
name: "sst-transports"
layout: package
next_package: py-cairocffi
previous_package: kokkos-legacy
languages: ['c']
---
## master
2 / 171 files match

 - [libfabric/src/fabric.c](#libfabricsrcfabricc)
 - [libfabric/prov/util/src/util_mem_hooks.c](#libfabricprovutilsrcutil_mem_hooksc)

### libfabric/src/fabric.c

```c

{% raw %}
567 | 		dlhandle = dlopen(lib, RTLD_NOW);
571 | 			       "dlopen(%s): %s\n", lib, dlerror());
635 | 	dlhandle = dlopen(NULL, RTLD_NOW);
{% endraw %}

```
### libfabric/prov/util/src/util_mem_hooks.c

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