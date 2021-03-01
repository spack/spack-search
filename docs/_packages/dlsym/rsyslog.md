---
name: "rsyslog"
layout: package
next_package: ruby
previous_package: rsync
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 8.2006.0
3 / 1621 files match, 3 filtered matches.

 - [tests/override_getaddrinfo.c](#testsoverride_getaddrinfoc)
 - [tests/override_gethostname.c](#testsoverride_gethostnamec)
 - [runtime/modules.c](#runtimemodulesc)

### tests/override_getaddrinfo.c

```c

{% raw %}
22 | 	printf("loaded\n");
23 | 	 * or - more importantly - obtain a pointer to the overriden
24 | 	 * API:
25 | 	orig_etry = dlsym(RTLD_NEXT, "original_entry_point");
26 | 	*/
27 | }
{% endraw %}

```
### tests/override_gethostname.c

```c

{% raw %}
16 | 	printf("loaded\n");
17 | 	 * or - more importantly - obtain a pointer to the overriden
18 | 	 * API:
19 | 	orig_etry = dlsym(RTLD_NEXT, "original_entry_point");
20 | 	*/
21 | }
{% endraw %}

```
### runtime/modules.c

```c

{% raw %}
1261 | 			(load_err_msg == NULL) ? "NONE SEEN???" : (const char*) cstrGetSzStrNoNULL(load_err_msg));
1262 | 		ABORT_FINALIZE(RS_RET_MODULE_LOAD_ERR_DLOPEN);
1263 | 	}
1264 | 	if(!(pModInit = (pModInit_t)dlsym(pModHdlr, "modInit"))) {
1265 | 		LogError(0, RS_RET_MODULE_LOAD_ERR_NO_INIT,
1266 | 			 	"could not load module '%s', dlsym: %s\n", pPathBuf, dlerror());
1267 | 		dlclose(pModHdlr);
1268 | 		ABORT_FINALIZE(RS_RET_MODULE_LOAD_ERR_NO_INIT);
{% endraw %}

```