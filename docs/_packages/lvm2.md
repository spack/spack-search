---
name: "lvm2"
layout: package
next_package: ldc-bootstrap
previous_package: graphviz
languages: ['c']
---
## 2.03.02
3 / 1036 files match, 2 filtered matches.

 - [lib/mm/memlock.c](#libmmmemlockc)
 - [daemons/dmeventd/dmeventd.c](#daemonsdmeventddmeventdc)

### lib/mm/memlock.c

```c

{% raw %}
106 | 	"/ld-2.",		/* not using dlopen,dlsym during mlock */
112 | 	"/libdl-",		/* not using dlopen,dlsym during mlock */
{% endraw %}

```
### daemons/dmeventd/dmeventd.c

```c

{% raw %}
159 | 	void *dso_handle;	/* Opaque handle as returned from dlopen(). */
349 | 	if (!(dl = dlopen(data->dso_name, RTLD_NOW))) {
383 | 	log_error("dmeventd %s dlopen failed: %s.", data->dso_name, dlerr);
384 | 	data->msg->size = dm_asprintf(&(data->msg->data), "%s %s dlopen failed: %s",
{% endraw %}

```