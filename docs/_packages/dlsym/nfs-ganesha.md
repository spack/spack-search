---
name: "nfs-ganesha"
layout: package
next_package: grpc
previous_package: glusterfs
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.1
3 / 834 files match, 3 filtered matches.

 - [src/SAL/nfs4_recovery.c](#srcsalnfs4_recoveryc)
 - [src/config_parsing/conf_url.c](#srcconfig_parsingconf_urlc)
 - [src/FSAL/fsal_manager.c](#srcfsalfsal_managerc)

### src/SAL/nfs4_recovery.c

```c

{% raw %}
700 | #endif
701 | 
702 | 	if (rados.dl) {
703 | 		rados.kv_init = dlsym(rados.dl, "rados_kv_backend_init");
704 | 		rados.ng_init = dlsym(rados.dl, "rados_ng_backend_init");
705 | 		rados.cluster_init = dlsym(rados.dl,
706 | 					   "rados_cluster_backend_init");
707 | 		rados.load_config_from_parse = dlsym(rados.dl,
708 | 					   "rados_load_config_from_parse");
709 | 
{% endraw %}

```
### src/config_parsing/conf_url.c

```c

{% raw %}
88 | #endif
89 | 
90 | 	if (rados_urls.dl) {
91 | 		rados_urls.pkginit = dlsym(rados_urls.dl,
92 | 					   "conf_url_rados_pkginit");
93 | 		rados_urls.setup_watch = dlsym(rados_urls.dl,
94 | 					       "rados_url_setup_watch");
95 | 		rados_urls.shutdown_watch = dlsym(rados_urls.dl,
96 | 						  "rados_url_shutdown_watch");
97 | 
{% endraw %}

```
### src/FSAL/fsal_manager.c

```c

{% raw %}
244 | 		void (*module_init)(void);
245 | 		char *sym_error;
246 | 
247 | 		module_init = dlsym(dl, "fsal_init");
248 | 		sym_error = (char *)dlerror();
249 | 		if (sym_error != NULL) {
{% endraw %}

```