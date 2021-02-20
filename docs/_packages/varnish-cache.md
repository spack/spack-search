---
name: "varnish-cache"
layout: package
next_package: veclibfort
previous_package: vampirtrace
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
267 | {
268 | 	void *h = NULL;
269 | 
270 | 	h = dlopen("libumem.so", RTLD_NOLOAD);
271 | 	if (h) {
272 | 		AZ(dlclose(h));
368 | 		AN(getenv(env_umem_options));
369 | 
370 | 	AZ(libumem_hndl);
371 | 	libumem_hndl = dlopen("libumem.so", RTLD_LAZY);
372 | 	AN(libumem_hndl);
373 | 
{% endraw %}

```
### bin/varnishd/mgt/mgt_param_tbl.c

```c

{% raw %}
49 | 	{ "cc_command", tweak_string, &mgt_cc_cmd,
50 | 		NULL, NULL,
51 | 		"Command used for compiling the C source code to a "
52 | 		"dlopen(3) loadable object.  Any occurrence of %s in "
53 | 		"the string will be replaced with the source file name, "
54 | 		"and %o will be replaced with the output file name.",
{% endraw %}

```
### bin/varnishd/mgt/mgt_vcc.c

```c

{% raw %}
176 |  */
177 | 
178 | static void v_matchproto_(vsub_func_f)
179 | run_dlopen(void *priv)
180 | {
181 | 	struct vcc_priv *vp;
248 | 	if (subs)
249 | 		return (subs);
250 | 
251 | 	subs = VSUB_run(sb, run_dlopen, vp, "dlopen", 10);
252 | 	return (subs);
253 | }
{% endraw %}

```
### bin/varnishd/cache/cache_vcl.c

```c

{% raw %}
371 | 
372 | #ifdef RTLD_NOLOAD
373 | 	/* Detect bogus caching by dlopen(3) */
374 | 	dlh = dlopen(fn, RTLD_NOW | RTLD_NOLOAD);
375 | 	AZ(dlh);
376 | #endif
377 | 	dlh = dlopen(fn, RTLD_NOW | RTLD_LOCAL);
378 | 	if (dlh == NULL) {
379 | 		VSB_printf(msg, "Could not load compiled VCL.\n");
380 | 		VSB_printf(msg, "\tdlopen() = %s\n", dlerror());
381 | 		return (NULL);
382 | 	}
{% endraw %}

```
### bin/varnishd/cache/cache_vrt_vmod.c

```c

{% raw %}
92 | 	AN(hdl);
93 | 	AZ(*hdl);
94 | 
95 | 	dlhdl = dlopen(backup, RTLD_NOW | RTLD_LOCAL);
96 | 	if (dlhdl == NULL) {
97 | 		VSB_printf(ctx->msg, "Loading vmod %s from %s (%s):\n",
98 | 		    nm, backup, path);
99 | 		VSB_printf(ctx->msg, "dlopen() failed: %s\n", dlerror());
100 | 		return (1);
101 | 	}
{% endraw %}

```
### lib/libvcc/vcc_vmod.c

```c

{% raw %}
47 | };
48 | 
49 | static int
50 | vcc_path_dlopen(void *priv, const char *fn)
51 | {
52 | 	struct vmod_open *vop;
54 | 	CAST_OBJ_NOTNULL(vop, priv, VMOD_OPEN_MAGIC);
55 | 	AN(fn);
56 | 
57 | 	vop->hdl = dlopen(fn, RTLD_NOW | RTLD_LOCAL);
58 | 	if (vop->hdl == NULL) {
59 | 		vop->err = dlerror();
270 | 
271 | 	SkipToken(tl, ';');
272 | 
273 | 	if (VFIL_searchpath(tl->vmod_path, vcc_path_dlopen, vop, fn, &fnpx)) {
274 | 		if (vop->err == NULL) {
275 | 			VSB_printf(tl->sb,
{% endraw %}

```