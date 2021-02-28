---
name: "libfabric"
layout: package
next_package: rsync
previous_package: pocl
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.6.1
4 / 638 files match, 2 filtered matches.

 - [src/fabric.c](#srcfabricc)
 - [prov/psm/src/psmx_am.c](#provpsmsrcpsmx_amc)

### src/fabric.c

```c

{% raw %}
413 | 		}
414 | 		free(lib);
415 | 
416 | 		inif = dlsym(dlhandle, "fi_prov_ini");
417 | 		if (inif == NULL) {
418 | 			FI_WARN(&core_prov, FI_LOG_CORE, "dlsym: %s\n", dlerror());
419 | 			dlclose(dlhandle);
420 | 		} else {
{% endraw %}

```
### prov/psm/src/psmx_am.c

```c

{% raw %}
137 | 			return psmx_errno(err);
138 | 
139 | 		if (psmx_am_compat_mode) {
140 | 			void *dlsym(void*, const char *);
141 | 			psmx_am_get_source = dlsym(NULL, "psm2_am_get_source");
142 | 			if (!psmx_am_get_source) {
143 | 				FI_WARN(&psmx_prov, FI_LOG_CORE,
{% endraw %}

```