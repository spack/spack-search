---
name: "varnish-cache"
layout: package
next_package: erlang
previous_package: r-stringi
languages: ['cpp']
---
## 6.3.1
9 / 1480 files match

 - [configure.ac](#configureac)
 - [bin/varnishd/storage/storage_umem.c](#binvarnishdstoragestorage_umemc)
 - [bin/varnishd/mgt/mgt_param_tbl.c](#binvarnishdmgtmgt_param_tblc)
 - [bin/varnishd/mgt/mgt_vcc.c](#binvarnishdmgtmgt_vccc)
 - [bin/varnishd/cache/cache_vcl.c](#binvarnishdcachecache_vclc)
 - [bin/varnishd/cache/cache_vrt_vmod.c](#binvarnishdcachecache_vrt_vmodc)
 - [lib/libvcc/vcc_vmod.c](#liblibvccvcc_vmodc)
 - [doc/changes.rst](#docchangesrst)
 - [doc/sphinx/phk/firstdesign.rst](#docsphinxphkfirstdesignrst)

### configure.ac

```

{% raw %}
93 | _VARNISH_CHECK_LIB(dl, dlopen)
{% endraw %}

```
### bin/varnishd/storage/storage_umem.c

```cpp

{% raw %}
75 |  * use dlopen/dlsym to get the slab allocator interface into function
270 | 	h = dlopen("libumem.so", RTLD_NOLOAD);
371 | 	libumem_hndl = dlopen("libumem.so", RTLD_LAZY);
{% endraw %}

```
### bin/varnishd/mgt/mgt_param_tbl.c

```cpp

{% raw %}
52 | 		"dlopen(3) loadable object.  Any occurrence of %s in "
{% endraw %}

```
### bin/varnishd/mgt/mgt_vcc.c

```cpp

{% raw %}
179 | run_dlopen(void *priv)
251 | 	subs = VSUB_run(sb, run_dlopen, vp, "dlopen", 10);
307 | 	 * the refcounting semantics of dlopen(3).
309 | 	 * Bad implementations of dlopen(3) think the shlib you are opening
328 | 	 *	vcl.load foo /foo.vcl	// dlopen(3) says "same-same"
333 | 	 * dlopen(3) decided they were really the same thing.
{% endraw %}

```
### bin/varnishd/cache/cache_vcl.c

```cpp

{% raw %}
373 | 	/* Detect bogus caching by dlopen(3) */
374 | 	dlh = dlopen(fn, RTLD_NOW | RTLD_NOLOAD);
377 | 	dlh = dlopen(fn, RTLD_NOW | RTLD_LOCAL);
380 | 		VSB_printf(msg, "\tdlopen() = %s\n", dlerror());
{% endraw %}

```
### bin/varnishd/cache/cache_vrt_vmod.c

```cpp

{% raw %}
95 | 	dlhdl = dlopen(backup, RTLD_NOW | RTLD_LOCAL);
99 | 		VSB_printf(ctx->msg, "dlopen() failed: %s\n", dlerror());
{% endraw %}

```
### lib/libvcc/vcc_vmod.c

```cpp

{% raw %}
50 | vcc_path_dlopen(void *priv, const char *fn)
57 | 	vop->hdl = dlopen(fn, RTLD_NOW | RTLD_LOCAL);
273 | 	if (VFIL_searchpath(tl->vmod_path, vcc_path_dlopen, vop, fn, &fnpx)) {
{% endraw %}

```
### doc/changes.rst

```

{% raw %}
1571 | * 1933_ - Don't trust dlopen refcounting
{% endraw %}

```
### doc/sphinx/phk/firstdesign.rst

```

{% raw %}
330 | 	regexps, compile them into executable code and dlopen() it
489 | 	modules which are dlopen'ed by the main Varnish process.
{% endraw %}

```