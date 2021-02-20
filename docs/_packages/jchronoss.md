---
name: "jchronoss"
layout: package
next_package: jimtcl
previous_package: jags
languages: ['c']
---
## 1.2
2 / 386 files match, 2 filtered matches.

 - [deps/libwebsockets/lib/libuv.c](#depslibwebsocketsliblibuvc)
 - [deps/libwebsockets/lib/lws-plat-unix.c](#depslibwebsocketsliblws-plat-unixc)

### deps/libwebsockets/lib/libuv.c

```c

{% raw %}
492 | 			lwsl_notice("   %s\n", dent.name);
493 | 
494 | 			lws_snprintf(path, sizeof(path) - 1, "%s/%s", *d, dent.name);
495 | 			if (uv_dlopen(path, &lib)) {
496 | 				uv_dlerror(&lib);
497 | 				lwsl_err("Error loading DSO: %s\n", lib.errmsg);
{% endraw %}

```
### deps/libwebsockets/lib/lws-plat-unix.c

```c

{% raw %}
338 | 
339 | 			lws_snprintf(path, sizeof(path) - 1, "%s/%s", *d,
340 | 				 namelist[i]->d_name);
341 | 			l = dlopen(path, RTLD_NOW);
342 | 			if (!l) {
343 | 				lwsl_err("Error loading DSO: %s\n", dlerror());
{% endraw %}

```