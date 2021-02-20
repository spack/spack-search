---
name: "libfabric"
layout: package
next_package: libfastcommon
previous_package: libevpath
languages: ['c']
---
## 1.6.1
5 / 638 files match, 1 filtered matches.

 - [src/fabric.c](#srcfabricc)

### src/fabric.c

```c

{% raw %}
403 | 		}
404 | 		FI_DBG(&core_prov, FI_LOG_CORE, "opening provider lib %s\n", lib);
405 | 
406 | 		dlhandle = dlopen(lib, RTLD_NOW);
407 | 		free(liblist[n]);
408 | 		if (dlhandle == NULL) {
409 | 			FI_WARN(&core_prov, FI_LOG_CORE,
410 | 			       "dlopen(%s): %s\n", lib, dlerror());
411 | 			free(lib);
412 | 			continue;
467 | 
468 | 	/* If dlopen fails, assume static linking and just return
469 | 	   without error */
470 | 	dlhandle = dlopen(NULL, RTLD_NOW);
471 | 	if (dlhandle == NULL) {
472 | 		goto libdl_done;
{% endraw %}

```