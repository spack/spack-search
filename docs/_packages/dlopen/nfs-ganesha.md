---
name: "nfs-ganesha"
layout: package
next_package: grpc
previous_package: glusterfs
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.1
14 / 834 files match, 4 filtered matches.

 - [src/SAL/nfs4_recovery.c](#srcsalnfs4_recoveryc)
 - [src/include/fsal_api.h](#srcincludefsal_apih)
 - [src/config_parsing/conf_url.c](#srcconfig_parsingconf_urlc)
 - [src/FSAL/fsal_manager.c](#srcfsalfsal_managerc)

### src/SAL/nfs4_recovery.c

```c

{% raw %}
692 | 
693 | static int load_rados_recov(void)
694 | {
695 | 	rados.dl = dlopen("libganesha_rados_recov.so",
696 | #if defined(LINUX) && !defined(SANITIZE_ADDRESS)
697 | 			  RTLD_NOW | RTLD_LOCAL | RTLD_DEEPBIND);
{% endraw %}

```
### src/include/fsal_api.h

```c

{% raw %}
2776 | 	struct glist_head servers;	/*< Head of list of Data Servers */
2777 | 	char *path;		/*< Path to .so file */
2778 | 	char *name;		/*< Name set from .so and/or config */
2779 | 	void *dl_handle;	/*< Handle to the dlopen()d shared
2780 | 				   library. NULL if statically linked */
2781 | 	struct fsal_ops m_ops;	/*< FSAL module methods vector */
{% endraw %}

```
### src/config_parsing/conf_url.c

```c

{% raw %}
80 | 
81 | static void load_rados_config(void)
82 | {
83 | 	rados_urls.dl = dlopen("libganesha_rados_urls.so",
84 | #if defined(LINUX) && !defined(SANITIZE_ADDRESS)
85 | 			      RTLD_NOW | RTLD_LOCAL | RTLD_DEEPBIND);
{% endraw %}

```
### src/FSAL/fsal_manager.c

```c

{% raw %}
85 | static enum load_state {
86 | 	init,		/*< In server start state. .init sections can run */
87 | 	idle,		/*< Switch from init->idle early in main() */
88 | 	loading,	/*< In dlopen(). set by load_fsal() just prior */
89 | 	registered,	/*< signal by registration that all is well */
90 | 	error		/*< signal by registration that all is not well */
222 | 
223 | 	LogDebug(COMPONENT_INIT, "Loading FSAL %s with %s", name, path);
224 | #if defined(LINUX) && !defined(SANITIZE_ADDRESS)
225 | 	dl = dlopen(path, RTLD_NOW | RTLD_LOCAL | RTLD_DEEPBIND);
226 | #elif defined(FREEBSD) || defined(SANITIZE_ADDRESS)
227 | 	dl = dlopen(path, RTLD_NOW | RTLD_LOCAL);
228 | #endif
229 | 
231 | 	if (dl == NULL) {
232 | 		dl_error = dlerror();
233 | 		LogFatal(COMPONENT_INIT,
234 | 			 "Could not dlopen module: %s Error: %s. You might want to install the nfs-ganesha-%s package",
235 | 			 path, dl_error, name);
236 | 	}
{% endraw %}

```