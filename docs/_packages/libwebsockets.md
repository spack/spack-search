---
name: "libwebsockets"
layout: package
next_package: libx11
previous_package: libverto
languages: ['c']
---
## 2.0.3
2 / 149 files match, 2 filtered matches.

 - [lib/libuv.c](#liblibuvc)
 - [lib/lws-plat-unix.c](#liblws-plat-unixc)

### lib/libuv.c

```c

{% raw %}
484 | 			lwsl_notice("   %s\n", dent.name);
485 | 
486 | 			lws_snprintf(path, sizeof(path) - 1, "%s/%s", *d, dent.name);
487 | 			if (uv_dlopen(path, &lib)) {
488 | 				uv_dlerror(&lib);
489 | 				lwsl_err("Error loading DSO: %s\n", lib.errmsg);
{% endraw %}

```
### lib/lws-plat-unix.c

```c

{% raw %}
332 | 
333 | 			lws_snprintf(path, sizeof(path) - 1, "%s/%s", *d,
334 | 				 namelist[i]->d_name);
335 | 			l = dlopen(path, RTLD_NOW);
336 | 			if (!l) {
337 | 				lwsl_err("Error loading DSO: %s\n", dlerror());
{% endraw %}

```