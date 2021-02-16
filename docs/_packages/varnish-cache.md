---
name: "varnish-cache"
layout: package
next_package: erlang
previous_package: r-stringi
languages: ['c']
---
## 6.3.1
9 / 1480 files match, 6 filtered matches.

 - [bin/varnishd/storage/storage_umem.c](#binvarnishdstoragestorage_umemc)
 - [bin/varnishd/mgt/mgt_param_tbl.c](#binvarnishdmgtmgt_param_tblc)
 - [bin/varnishd/mgt/mgt_vcc.c](#binvarnishdmgtmgt_vccc)
 - [bin/varnishd/cache/cache_vcl.c](#binvarnishdcachecache_vclc)
 - [bin/varnishd/cache/cache_vrt_vmod.c](#binvarnishdcachecache_vrt_vmodc)
 - [lib/libvcc/vcc_vmod.c](#liblibvccvcc_vmodc)

### bin/varnishd/storage/storage_umem.c

```c

{% raw %}
270 | 	h = dlopen("libumem.so", RTLD_NOLOAD);
371 | 	libumem_hndl = dlopen("libumem.so", RTLD_LAZY);
{% endraw %}

```
### bin/varnishd/mgt/mgt_param_tbl.c

```c

{% raw %}
52 | 		"dlopen(3) loadable object.  Any occurrence of %s in "
{% endraw %}

```
### bin/varnishd/mgt/mgt_vcc.c

```c

{% raw %}
179 | run_dlopen(void *priv)
251 | 	subs = VSUB_run(sb, run_dlopen, vp, "dlopen", 10);
{% endraw %}

```
### bin/varnishd/cache/cache_vcl.c

```c

{% raw %}
374 | 	dlh = dlopen(fn, RTLD_NOW | RTLD_NOLOAD);
377 | 	dlh = dlopen(fn, RTLD_NOW | RTLD_LOCAL);
380 | 		VSB_printf(msg, "\tdlopen() = %s\n", dlerror());
{% endraw %}

```
### bin/varnishd/cache/cache_vrt_vmod.c

```c

{% raw %}
95 | 	dlhdl = dlopen(backup, RTLD_NOW | RTLD_LOCAL);
99 | 		VSB_printf(ctx->msg, "dlopen() failed: %s\n", dlerror());
{% endraw %}

```
### lib/libvcc/vcc_vmod.c

```c

{% raw %}
50 | vcc_path_dlopen(void *priv, const char *fn)
57 | 	vop->hdl = dlopen(fn, RTLD_NOW | RTLD_LOCAL);
273 | 	if (VFIL_searchpath(tl->vmod_path, vcc_path_dlopen, vop, fn, &fnpx)) {
{% endraw %}

```