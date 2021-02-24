---
name: "slurm"
layout: package
next_package: petsc
previous_package: gotcha
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 18-08-9-1
9 / 2484 files match, 5 filtered matches.

 - [src/common/plugin.c](#srccommonpluginc)
 - [src/common/plugstack.c](#srccommonplugstackc)
 - [src/plugins/switch/nrt/nrt.c](#srcpluginsswitchnrtnrtc)
 - [src/plugins/mpi/pmi2/setup.c](#srcpluginsmpipmi2setupc)
 - [src/plugins/proctrack/sgi_job/proctrack_sgi_job.c](#srcpluginsproctracksgi_jobproctrack_sgi_jobc)

### src/common/plugin.c

```c

{% raw %}
113 | 		debug3( "plugin_peek: dlopen(%s): %s", fq_path, _dlerror() );
114 | 		return SLURM_ERROR;
115 | 	}
116 | 	if ( ( type = dlsym( plug, PLUGIN_TYPE ) ) != NULL ) {
117 | 		if ( plugin_type != NULL ) {
118 | 			strlcpy(plugin_type, type, type_len);
124 | 		return SLURM_ERROR;
125 | 	}
126 | 
127 | 	version = (uint32_t *) dlsym(plug, PLUGIN_VERSION);
128 | 	if (!version) {
129 | 		verbose("%s: plugin_version symbol not defined", fq_path);
182 | 	}
183 | 
184 | 	/* Now see if our required symbols are defined. */
185 | 	if ((dlsym(plug, PLUGIN_NAME) == NULL) ||
186 | 	    ((type = dlsym(plug, PLUGIN_TYPE)) == NULL)) {
187 | 		dlclose(plug);
188 | 		return EPLUGIN_MISSING_NAME;
189 | 	}
190 | 
191 | 	version = (uint32_t *) dlsym(plug, PLUGIN_VERSION);
192 | 	if (!version) {
193 | 		verbose("%s: plugin_version symbol not defined", fq_path);
207 | 	 * Now call its init() function, if present.  If the function
208 | 	 * returns nonzero, unload the plugin and signal an error.
209 | 	 */
210 | 	if ((init = dlsym(plug, "init")) != NULL) {
211 | 		if ((*init)() != 0) {
212 | 			dlclose(plug);
300 | 	void (*fini)(void);
301 | 
302 | 	if ( plug != PLUGIN_INVALID_HANDLE ) {
303 | 		if ( ( fini = dlsym( plug, "fini" ) ) != NULL ) {
304 | 			(*fini)();
305 | 		}
323 | plugin_get_sym( plugin_handle_t plug, const char *name )
324 | {
325 | 	if ( plug != PLUGIN_INVALID_HANDLE )
326 | 		return dlsym( plug, name );
327 | 	else
328 | 		return NULL;
332 | plugin_get_name( plugin_handle_t plug )
333 | {
334 | 	if ( plug != PLUGIN_INVALID_HANDLE )
335 | 		return (const char *) dlsym( plug, PLUGIN_NAME );
336 | 	else
337 | 		return NULL;
341 | plugin_get_type( plugin_handle_t plug )
342 | {
343 | 	if ( plug != PLUGIN_INVALID_HANDLE )
344 | 		return (const char *) dlsym( plug, PLUGIN_TYPE );
345 | 	else
346 | 		return NULL;
353 | 
354 | 	if (plug == PLUGIN_INVALID_HANDLE)
355 | 		return 0;
356 | 	ptr = (uint32_t *) dlsym(plug, PLUGIN_VERSION);
357 | 	return ptr ? *ptr : 0;
358 | }
367 | 
368 | 	count = 0;
369 | 	for ( i = 0; i < n_syms; ++i ) {
370 | 		ptrs[ i ] = dlsym( plug, names[ i ] );
371 | 		if ( ptrs[ i ] )
372 | 			++count;
{% endraw %}

```
### src/common/plugstack.c

```c

{% raw %}
2316 | 	char * (*fn)(const char *n);
2317 | 	char *rc;
2318 | 
2319 | 	fn = dlsym(h, "spank_get_job_env");
2320 | 	if (fn == NULL) {
2321 | 		(void) dlclose(h);
2333 | 	int (*fn)(const char *n, const char *v, int overwrite);
2334 | 	int rc;
2335 | 
2336 | 	fn = dlsym(h, "spank_set_job_env");
2337 | 	if (fn == NULL) {
2338 | 		(void) dlclose(h);
2350 | 	int (*fn)(const char *n);
2351 | 	int rc;
2352 | 
2353 | 	fn = dlsym(h, "spank_unset_job_env");
2354 | 	if (fn == NULL) {
2355 | 		(void) dlclose(h);
{% endraw %}

```
### src/plugins/switch/nrt/nrt.c

```c

{% raw %}
95 | 
96 | 		dlerror();	/* Clear any existing error */
97 | 		for ( i = 0; nrt_sym[i]; ++i ) {
98 | 		        api_pptr[i] = dlsym(nrt_handle, nrt_sym[i]);
99 | 		        if (!api_pptr[i]) {
100 | 				fatal("Can't find %s in libnrt.so",
{% endraw %}

```
### src/plugins/mpi/pmi2/setup.c

```c

{% raw %}
621 | 		error("mpi/pmi2: failed to dlopen()");
622 | 		return SLURM_ERROR;
623 | 	}
624 | 	sym = dlsym(handle, "MPIR_proctable");
625 | 	if (sym == NULL) {
626 | 		/* if called directly in API, there may be no symbol available */
629 | 	} else {
630 | 		job_info.MPIR_proctable = *(MPIR_PROCDESC **)sym;
631 | 	}
632 | 	sym = dlsym(handle, "opt");
633 | 	if (sym == NULL) {
634 | 		verbose("mpi/pmi2: failed to find symbol 'opt'");
{% endraw %}

```
### src/plugins/proctrack/sgi_job/proctrack_sgi_job.c

```c

{% raw %}
104 | 		return SLURM_ERROR;
105 | 	}
106 | 
107 | 	job_ops.create    = dlsym (libjob_handle, "job_create");
108 | 	job_ops.getjid    = dlsym (libjob_handle, "job_getjid");
109 | 	job_ops.waitjid   = dlsym (libjob_handle, "job_waitjid");
110 | 	job_ops.killjid   = dlsym (libjob_handle, "job_killjid");
111 | 	job_ops.detachpid = dlsym (libjob_handle, "job_detachpid");
112 | 	job_ops.attachpid = dlsym (libjob_handle, "job_attachpid");
113 | 	job_ops.getpidlist= dlsym (libjob_handle, "job_getpidlist");
114 | 	job_ops.getpidcnt = dlsym (libjob_handle, "job_getpidcnt");
115 | 
116 | 	if (!job_ops.create)
{% endraw %}

```