---
name: "lvm2"
layout: package
next_package: mariadb
previous_package: lumpy-sv
languages: ['c']
---
## 2.03.02
3 / 1036 files match, 2 filtered matches.

 - [lib/mm/memlock.c](#libmmmemlockc)
 - [daemons/dmeventd/dmeventd.c](#daemonsdmeventddmeventdc)

### lib/mm/memlock.c

```c

{% raw %}
103 | 	"locale/locale-archive",
104 | 	"/LC_MESSAGES/",
105 | 	"gconv/gconv-modules.cache",
106 | 	"/ld-2.",		/* not using dlopen,dlsym during mlock */
107 | 	"/libaio.so.",		/* not using aio during mlock */
108 | 	"/libattr.so.",		/* not using during mlock (udev) */
109 | 	"/libblkid.so.",	/* not using blkid during mlock (udev) */
110 | 	"/libbz2.so.",		/* not using during mlock (udev) */
111 | 	"/libcap.so.",		/* not using during mlock (systemd) */
112 | 	"/libdl-",		/* not using dlopen,dlsym during mlock */
113 | 	"/libdw-",		/* not using during mlock (udev) */
114 | 	"/libelf-",		/* not using during mlock (udev) */
{% endraw %}

```
### daemons/dmeventd/dmeventd.c

```c

{% raw %}
156 | 
157 | 	char *dso_name;		/* DSO name (eg, "evms", "dmraid", "lvm2"). */
158 | 
159 | 	void *dso_handle;	/* Opaque handle as returned from dlopen(). */
160 | 	unsigned int ref_count;	/* Library reference count. */
161 | 
346 | 	struct dso_data *ret;
347 | 	const char *dlerr;
348 | 
349 | 	if (!(dl = dlopen(data->dso_name, RTLD_NOW))) {
350 | 		dlerr = dlerror();
351 | 		goto_bad;
380 | 
381 | 	return ret;
382 | bad:
383 | 	log_error("dmeventd %s dlopen failed: %s.", data->dso_name, dlerr);
384 | 	data->msg->size = dm_asprintf(&(data->msg->data), "%s %s dlopen failed: %s",
385 | 				      data->id, data->dso_name, dlerr);
386 | 	return NULL;
{% endraw %}

```