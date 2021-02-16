---
name: "nfs-ganesha"
layout: package
next_package: hadoop
previous_package: 3proxy
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
695 | 	rados.dl = dlopen("libganesha_rados_recov.so",
{% endraw %}

```
### src/include/fsal_api.h

```c

{% raw %}
2779 | 	void *dl_handle;	/*< Handle to the dlopen()d shared
{% endraw %}

```
### src/config_parsing/conf_url.c

```c

{% raw %}
83 | 	rados_urls.dl = dlopen("libganesha_rados_urls.so",
{% endraw %}

```
### src/FSAL/fsal_manager.c

```c

{% raw %}
88 | 	loading,	/*< In dlopen(). set by load_fsal() just prior */
225 | 	dl = dlopen(path, RTLD_NOW | RTLD_LOCAL | RTLD_DEEPBIND);
227 | 	dl = dlopen(path, RTLD_NOW | RTLD_LOCAL);
234 | 			 "Could not dlopen module: %s Error: %s. You might want to install the nfs-ganesha-%s package",
{% endraw %}

```