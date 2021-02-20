---
name: "bind9"
layout: package
next_package: binutils
previous_package: berkeley-db
languages: ['c']
---
## 9_14_6
57 / 3884 files match, 11 filtered matches.

 - [bin/named/main.c](#binnamedmainc)
 - [bin/named/include/dlz/dlz_dlopen_driver.h](#binnamedincludedlzdlz_dlopen_driverh)
 - [bin/named/unix/dlz_dlopen_driver.c](#binnamedunixdlz_dlopen_driverc)
 - [bin/named/win32/dlz_dlopen_driver.c](#binnamedwin32dlz_dlopen_driverc)
 - [bin/tests/system/feature-test.c](#bintestssystemfeature-testc)
 - [bin/tests/system/dlzexternal/driver.h](#bintestssystemdlzexternaldriverh)
 - [lib/ns/hooks.c](#libnshooksc)
 - [lib/isc/unix/pk11_api.c](#libiscunixpk11_apic)
 - [lib/dns/dyndb.c](#libdnsdyndbc)
 - [lib/dns/include/dns/librpz.h](#libdnsincludednslibrpzh)
 - [lib/dns/include/dns/dlz_dlopen.h](#libdnsincludednsdlz_dlopenh)

### bin/named/main.c

```c

{% raw %}
1176 | 	/*
1177 | 	 * Register the DLZ "dlopen" driver.
1178 | 	 */
1179 | 	result = dlz_dlopen_init(named_g_mctx);
1180 | 	if (result != ISC_R_SUCCESS)
1181 | 		named_main_earlyfatal("dlz_dlopen_init() failed: %s",
1182 | 				   isc_result_totext(result));
1183 | #endif
1256 | 	/*
1257 | 	 * Unregister "dlopen" DLZ driver.
1258 | 	 */
1259 | 	dlz_dlopen_clear();
1260 | #endif
1261 | 
{% endraw %}

```
### bin/named/include/dlz/dlz_dlopen_driver.h

```c

{% raw %}
13 | #define DLZ_DLOPEN_DRIVER_H
14 | 
15 | isc_result_t
16 | dlz_dlopen_init(isc_mem_t *mctx);
17 | 
18 | void
19 | dlz_dlopen_clear(void);
20 | #endif
21 | 
{% endraw %}

```
### bin/named/unix/dlz_dlopen_driver.c

```c

{% raw %}
34 | #include <dlz/dlz_dlopen_driver.h>
35 | 
36 | #ifdef ISC_DLZ_DLOPEN
37 | static dns_sdlzimplementation_t *dlz_dlopen = NULL;
38 | 
39 | 
40 | typedef struct dlopen_data {
41 | 	isc_mem_t *mctx;
42 | 	char *dl_path;
48 | 	int version;
49 | 	bool in_configure;
50 | 
51 | 	dlz_dlopen_version_t *dlz_version;
52 | 	dlz_dlopen_create_t *dlz_create;
53 | 	dlz_dlopen_findzonedb_t *dlz_findzonedb;
54 | 	dlz_dlopen_lookup_t *dlz_lookup;
55 | 	dlz_dlopen_authority_t *dlz_authority;
56 | 	dlz_dlopen_allnodes_t *dlz_allnodes;
57 | 	dlz_dlopen_allowzonexfr_t *dlz_allowzonexfr;
58 | 	dlz_dlopen_newversion_t *dlz_newversion;
59 | 	dlz_dlopen_closeversion_t *dlz_closeversion;
60 | 	dlz_dlopen_configure_t *dlz_configure;
61 | 	dlz_dlopen_ssumatch_t *dlz_ssumatch;
62 | 	dlz_dlopen_addrdataset_t *dlz_addrdataset;
63 | 	dlz_dlopen_subrdataset_t *dlz_subrdataset;
64 | 	dlz_dlopen_delrdataset_t *dlz_delrdataset;
65 | 	dlz_dlopen_destroy_t *dlz_destroy;
66 | } dlopen_data_t;
67 | 
68 | /* Modules can choose whether they are lock-safe or not. */
83 | /*
84 |  * Log a message at the given level.
85 |  */
86 | static void dlopen_log(int level, const char *fmt, ...)
87 | {
88 | 	va_list ap;
98 |  */
99 | 
100 | static isc_result_t
101 | dlopen_dlz_allnodes(const char *zone, void *driverarg, void *dbdata,
102 | 		    dns_sdlzallnodes_t *allnodes)
103 | {
104 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
105 | 	isc_result_t result;
106 | 
119 | 
120 | 
121 | static isc_result_t
122 | dlopen_dlz_allowzonexfr(void *driverarg, void *dbdata, const char *name,
123 | 			const char *client)
124 | {
125 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
126 | 	isc_result_t result;
127 | 
139 | }
140 | 
141 | static isc_result_t
142 | dlopen_dlz_authority(const char *zone, void *driverarg, void *dbdata,
143 | 		     dns_sdlzlookup_t *lookup)
144 | {
145 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
146 | 	isc_result_t result;
147 | 
158 | }
159 | 
160 | static isc_result_t
161 | dlopen_dlz_findzonedb(void *driverarg, void *dbdata, const char *name,
162 | 		      dns_clientinfomethods_t *methods,
163 | 		      dns_clientinfo_t *clientinfo)
164 | {
165 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
166 | 	isc_result_t result;
167 | 
175 | 
176 | 
177 | static isc_result_t
178 | dlopen_dlz_lookup(const char *zone, const char *name, void *driverarg,
179 | 		  void *dbdata, dns_sdlzlookup_t *lookup,
180 | 		  dns_clientinfomethods_t *methods,
181 | 		  dns_clientinfo_t *clientinfo)
182 | {
183 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
184 | 	isc_result_t result;
185 | 
196 |  * Load a symbol from the library
197 |  */
198 | static void *
199 | dl_load_symbol(dlopen_data_t *cd, const char *symbol, bool mandatory) {
200 | 	void *ptr = dlsym(cd->dl_handle, symbol);
201 | 	if (ptr == NULL && mandatory) {
202 | 		dlopen_log(ISC_LOG_ERROR,
203 | 			   "dlz_dlopen: library '%s' is missing "
204 | 			   "required symbol '%s'", cd->dl_path, symbol);
205 | 	}
210 |  * Called at startup for each dlopen zone in named.conf
211 |  */
212 | static isc_result_t
213 | dlopen_dlz_create(const char *dlzname, unsigned int argc, char *argv[],
214 | 		  void *driverarg, void **dbdata)
215 | {
216 | 	dlopen_data_t *cd;
217 | 	isc_mem_t *mctx = NULL;
218 | 	isc_result_t result = ISC_R_FAILURE;
219 | 	int dlopen_flags = 0;
220 | 
221 | 	UNUSED(driverarg);
222 | 
223 | 	if (argc < 2) {
224 | 		dlopen_log(ISC_LOG_ERROR,
225 | 			   "dlz_dlopen driver for '%s' needs a path to "
226 | 			   "the shared library", dlzname);
227 | 		return (ISC_R_FAILURE);
256 | 	isc_mutex_init(&cd->lock);
257 | 
258 | 	/* Open the library */
259 | 	dlopen_flags = RTLD_NOW|RTLD_GLOBAL;
260 | 
261 | #if defined(RTLD_DEEPBIND) && !__SANITIZE_ADDRESS__
268 | 	 * calling MIT functions, which leads to bizarre results (usually
269 | 	 * a segfault).
270 | 	 */
271 | 	dlopen_flags |= RTLD_DEEPBIND;
272 | #endif
273 | 
274 | 	cd->dl_handle = dlopen(cd->dl_path, dlopen_flags);
275 | 	if (cd->dl_handle == NULL) {
276 | 		dlopen_log(ISC_LOG_ERROR,
277 | 			   "dlz_dlopen failed to open library '%s' - %s",
278 | 			   cd->dl_path, dlerror());
279 | 		result = ISC_R_FAILURE;
281 | 	}
282 | 
283 | 	/* Find the symbols */
284 | 	cd->dlz_version = (dlz_dlopen_version_t *)
285 | 		dl_load_symbol(cd, "dlz_version", true);
286 | 	cd->dlz_create = (dlz_dlopen_create_t *)
287 | 		dl_load_symbol(cd, "dlz_create", true);
288 | 	cd->dlz_lookup = (dlz_dlopen_lookup_t *)
289 | 		dl_load_symbol(cd, "dlz_lookup", true);
290 | 	cd->dlz_findzonedb = (dlz_dlopen_findzonedb_t *)
291 | 		dl_load_symbol(cd, "dlz_findzonedb", true);
292 | 
300 | 		goto failed;
301 | 	}
302 | 
303 | 	cd->dlz_allowzonexfr = (dlz_dlopen_allowzonexfr_t *)
304 | 		dl_load_symbol(cd, "dlz_allowzonexfr", false);
305 | 	cd->dlz_allnodes = (dlz_dlopen_allnodes_t *)
306 | 		dl_load_symbol(cd, "dlz_allnodes",
307 | 			       (cd->dlz_allowzonexfr != NULL));
308 | 	cd->dlz_authority = (dlz_dlopen_authority_t *)
309 | 		dl_load_symbol(cd, "dlz_authority", false);
310 | 	cd->dlz_newversion = (dlz_dlopen_newversion_t *)
311 | 		dl_load_symbol(cd, "dlz_newversion", false);
312 | 	cd->dlz_closeversion = (dlz_dlopen_closeversion_t *)
313 | 		dl_load_symbol(cd, "dlz_closeversion",
314 | 			       (cd->dlz_newversion != NULL));
315 | 	cd->dlz_configure = (dlz_dlopen_configure_t *)
316 | 		dl_load_symbol(cd, "dlz_configure", false);
317 | 	cd->dlz_ssumatch = (dlz_dlopen_ssumatch_t *)
318 | 		dl_load_symbol(cd, "dlz_ssumatch", false);
319 | 	cd->dlz_addrdataset = (dlz_dlopen_addrdataset_t *)
320 | 		dl_load_symbol(cd, "dlz_addrdataset", false);
321 | 	cd->dlz_subrdataset = (dlz_dlopen_subrdataset_t *)
322 | 		dl_load_symbol(cd, "dlz_subrdataset", false);
323 | 	cd->dlz_delrdataset = (dlz_dlopen_delrdataset_t *)
324 | 		dl_load_symbol(cd, "dlz_delrdataset", false);
325 | 	cd->dlz_destroy = (dlz_dlopen_destroy_t *)
326 | 		dl_load_symbol(cd, "dlz_destroy", false);
327 | 
330 | 	if (cd->version < (DLZ_DLOPEN_VERSION - DLZ_DLOPEN_AGE) ||
331 | 	    cd->version > DLZ_DLOPEN_VERSION)
332 | 	{
333 | 		dlopen_log(ISC_LOG_ERROR,
334 | 			   "dlz_dlopen: %s: incorrect driver API version %d, "
335 | 			   "requires %d",
336 | 			   cd->dl_path, cd->version, DLZ_DLOPEN_VERSION);
348 | 	MAYBE_LOCK(cd);
349 | 	result = cd->dlz_create(dlzname, argc-1, argv+1,
350 | 				&cd->dbdata,
351 | 				"log", dlopen_log,
352 | 				"putrr", dns_sdlz_putrr,
353 | 				"putnamedrr", dns_sdlz_putnamedrr,
362 | 	return (ISC_R_SUCCESS);
363 | 
364 | failed:
365 | 	dlopen_log(ISC_LOG_ERROR, "dlz_dlopen of '%s' failed", dlzname);
366 | 	if (cd->dl_path != NULL) {
367 | 		isc_mem_free(mctx, cd->dl_path);
369 | 	if (cd->dlzname != NULL) {
370 | 		isc_mem_free(mctx, cd->dlzname);
371 | 	}
372 | 	if (dlopen_flags != 0) {
373 | 		isc_mutex_destroy(&cd->lock);
374 | 	}
386 |  * Called when bind is shutting down
387 |  */
388 | static void
389 | dlopen_dlz_destroy(void *driverarg, void *dbdata) {
390 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
391 | 	isc_mem_t *mctx;
392 | 
422 |  * Called to start a transaction
423 |  */
424 | static isc_result_t
425 | dlopen_dlz_newversion(const char *zone, void *driverarg, void *dbdata,
426 | 		      void **versionp)
427 | {
428 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
429 | 	isc_result_t result;
430 | 
443 |  * Called to end a transaction
444 |  */
445 | static void
446 | dlopen_dlz_closeversion(const char *zone, bool commit,
447 | 			void *driverarg, void *dbdata, void **versionp)
448 | {
449 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
450 | 
451 | 	UNUSED(driverarg);
464 |  * Called on startup to configure any writeable zones
465 |  */
466 | static isc_result_t
467 | dlopen_dlz_configure(dns_view_t *view, dns_dlzdb_t *dlzdb,
468 | 		     void *driverarg, void *dbdata)
469 | {
470 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
471 | 	isc_result_t result;
472 | 
489 |  * Check for authority to change a name.
490 |  */
491 | static bool
492 | dlopen_dlz_ssumatch(const char *signer, const char *name, const char *tcpaddr,
493 | 		    const char *type, const char *key, uint32_t keydatalen,
494 | 		    unsigned char *keydata, void *driverarg, void *dbdata)
495 | {
496 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
497 | 	bool ret;
498 | 
514 |  * Add an rdataset.
515 |  */
516 | static isc_result_t
517 | dlopen_dlz_addrdataset(const char *name, const char *rdatastr,
518 | 		       void *driverarg, void *dbdata, void *version)
519 | {
520 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
521 | 	isc_result_t result;
522 | 
536 |  * Subtract an rdataset.
537 |  */
538 | static isc_result_t
539 | dlopen_dlz_subrdataset(const char *name, const char *rdatastr,
540 | 		       void *driverarg, void *dbdata, void *version)
541 | {
542 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
543 | 	isc_result_t result;
544 | 
558 |  * Delete a rdataset.
559 |  */
560 | static isc_result_t
561 | dlopen_dlz_delrdataset(const char *name, const char *type,
562 | 		       void *driverarg, void *dbdata, void *version)
563 | {
564 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
565 | 	isc_result_t result;
566 | 
577 | }
578 | 
579 | 
580 | static dns_sdlzmethods_t dlz_dlopen_methods = {
581 | 	dlopen_dlz_create,
582 | 	dlopen_dlz_destroy,
583 | 	dlopen_dlz_findzonedb,
584 | 	dlopen_dlz_lookup,
585 | 	dlopen_dlz_authority,
586 | 	dlopen_dlz_allnodes,
587 | 	dlopen_dlz_allowzonexfr,
588 | 	dlopen_dlz_newversion,
589 | 	dlopen_dlz_closeversion,
590 | 	dlopen_dlz_configure,
591 | 	dlopen_dlz_ssumatch,
592 | 	dlopen_dlz_addrdataset,
593 | 	dlopen_dlz_subrdataset,
594 | 	dlopen_dlz_delrdataset
595 | };
596 | #endif
599 |  * Register driver with BIND
600 |  */
601 | isc_result_t
602 | dlz_dlopen_init(isc_mem_t *mctx) {
603 | #ifndef ISC_DLZ_DLOPEN
604 | 	UNUSED(mctx);
606 | #else
607 | 	isc_result_t result;
608 | 
609 | 	dlopen_log(2, "Registering DLZ_dlopen driver");
610 | 
611 | 	result = dns_sdlzregister("dlopen", &dlz_dlopen_methods, NULL,
612 | 				  DNS_SDLZFLAG_RELATIVEOWNER |
613 | 				  DNS_SDLZFLAG_RELATIVERDATA |
614 | 				  DNS_SDLZFLAG_THREADSAFE,
615 | 				  mctx, &dlz_dlopen);
616 | 
617 | 	if (result != ISC_R_SUCCESS) {
630 |  * Unregister the driver
631 |  */
632 | void
633 | dlz_dlopen_clear(void) {
634 | #ifdef ISC_DLZ_DLOPEN
635 | 	dlopen_log(2, "Unregistering DLZ_dlopen driver");
636 | 	if (dlz_dlopen != NULL)
637 | 		dns_sdlzunregister(&dlz_dlopen);
638 | #endif
639 | }
{% endraw %}

```
### bin/named/win32/dlz_dlopen_driver.c

```c

{% raw %}
33 | #include <dlz/dlz_dlopen_driver.h>
34 | 
35 | #ifdef ISC_DLZ_DLOPEN
36 | static dns_sdlzimplementation_t *dlz_dlopen = NULL;
37 | 
38 | 
39 | typedef struct dlopen_data {
40 | 	isc_mem_t *mctx;
41 | 	char *dl_path;
47 | 	int version;
48 | 	bool in_configure;
49 | 
50 | 	dlz_dlopen_version_t *dlz_version;
51 | 	dlz_dlopen_create_t *dlz_create;
52 | 	dlz_dlopen_findzonedb_t *dlz_findzonedb;
53 | 	dlz_dlopen_lookup_t *dlz_lookup;
54 | 	dlz_dlopen_authority_t *dlz_authority;
55 | 	dlz_dlopen_allnodes_t *dlz_allnodes;
56 | 	dlz_dlopen_allowzonexfr_t *dlz_allowzonexfr;
57 | 	dlz_dlopen_newversion_t *dlz_newversion;
58 | 	dlz_dlopen_closeversion_t *dlz_closeversion;
59 | 	dlz_dlopen_configure_t *dlz_configure;
60 | 	dlz_dlopen_ssumatch_t *dlz_ssumatch;
61 | 	dlz_dlopen_addrdataset_t *dlz_addrdataset;
62 | 	dlz_dlopen_subrdataset_t *dlz_subrdataset;
63 | 	dlz_dlopen_delrdataset_t *dlz_delrdataset;
64 | 	dlz_dlopen_destroy_t *dlz_destroy;
65 | } dlopen_data_t;
66 | 
67 | /* Modules can choose whether they are lock-safe or not. */
82 | /*
83 |  * Log a message at the given level.
84 |  */
85 | static void dlopen_log(int level, const char *fmt, ...)
86 | {
87 | 	va_list ap;
97 |  */
98 | 
99 | static isc_result_t
100 | dlopen_dlz_allnodes(const char *zone, void *driverarg, void *dbdata,
101 | 		    dns_sdlzallnodes_t *allnodes)
102 | {
103 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
104 | 	isc_result_t result;
105 | 
118 | 
119 | 
120 | static isc_result_t
121 | dlopen_dlz_allowzonexfr(void *driverarg, void *dbdata, const char *name,
122 | 			const char *client)
123 | {
124 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
125 | 	isc_result_t result;
126 | 
138 | }
139 | 
140 | static isc_result_t
141 | dlopen_dlz_authority(const char *zone, void *driverarg, void *dbdata,
142 | 		   dns_sdlzlookup_t *lookup)
143 | {
144 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
145 | 	isc_result_t result;
146 | 
157 | }
158 | 
159 | static isc_result_t
160 | dlopen_dlz_findzonedb(void *driverarg, void *dbdata, const char *name,
161 | 		      dns_clientinfomethods_t *methods,
162 | 		      dns_clientinfo_t *clientinfo)
163 | {
164 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
165 | 	isc_result_t result;
166 | 
174 | 
175 | 
176 | static isc_result_t
177 | dlopen_dlz_lookup(const char *zone, const char *name, void *driverarg,
178 | 		  void *dbdata, dns_sdlzlookup_t *lookup,
179 | 		  dns_clientinfomethods_t *methods,
180 | 		  dns_clientinfo_t *clientinfo)
181 | {
182 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
183 | 	isc_result_t result;
184 | 
195 |  * Load a symbol from the library
196 |  */
197 | static void *
198 | dl_load_symbol(dlopen_data_t *cd, const char *symbol, bool mandatory) {
199 | 	void *ptr = GetProcAddress(cd->dl_handle, symbol);
200 | 	if (ptr == NULL && mandatory) {
201 | 		dlopen_log(ISC_LOG_ERROR,
202 | 			   "dlz_dlopen: library '%s' is missing "
203 | 			   "required symbol '%s'", cd->dl_path, symbol);
204 | 	}
209 |  * Called at startup for each dlopen zone in named.conf
210 |  */
211 | static isc_result_t
212 | dlopen_dlz_create(const char *dlzname, unsigned int argc, char *argv[],
213 | 		  void *driverarg, void **dbdata)
214 | {
215 | 	dlopen_data_t *cd;
216 | 	isc_mem_t *mctx = NULL;
217 | 	isc_result_t result = ISC_R_FAILURE;
220 | 	UNUSED(driverarg);
221 | 
222 | 	if (argc < 2) {
223 | 		dlopen_log(ISC_LOG_ERROR,
224 | 			   "dlz_dlopen driver for '%s' needs a path to "
225 | 			   "the shared library", dlzname);
226 | 		return (ISC_R_FAILURE);
259 | 	if (cd->dl_handle == NULL) {
260 | 		unsigned int error = GetLastError();
261 | 
262 | 		dlopen_log(ISC_LOG_ERROR,
263 | 			   "dlz_dlopen failed to open library '%s' - %u",
264 | 			   cd->dl_path, error);
265 | 		result = ISC_R_FAILURE;
267 | 	}
268 | 
269 | 	/* Find the symbols */
270 | 	cd->dlz_version = (dlz_dlopen_version_t *)
271 | 		dl_load_symbol(cd, "dlz_version", true);
272 | 	cd->dlz_create = (dlz_dlopen_create_t *)
273 | 		dl_load_symbol(cd, "dlz_create", true);
274 | 	cd->dlz_lookup = (dlz_dlopen_lookup_t *)
275 | 		dl_load_symbol(cd, "dlz_lookup", true);
276 | 	cd->dlz_findzonedb = (dlz_dlopen_findzonedb_t *)
277 | 		dl_load_symbol(cd, "dlz_findzonedb", true);
278 | 
286 | 		goto cleanup_lock;
287 | 	}
288 | 
289 | 	cd->dlz_allowzonexfr = (dlz_dlopen_allowzonexfr_t *)
290 | 		dl_load_symbol(cd, "dlz_allowzonexfr", false);
291 | 	cd->dlz_allnodes = (dlz_dlopen_allnodes_t *)
292 | 		dl_load_symbol(cd, "dlz_allnodes",
293 | 			       (cd->dlz_allowzonexfr != NULL));
294 | 	cd->dlz_authority = (dlz_dlopen_authority_t *)
295 | 		dl_load_symbol(cd, "dlz_authority", false);
296 | 	cd->dlz_newversion = (dlz_dlopen_newversion_t *)
297 | 		dl_load_symbol(cd, "dlz_newversion", false);
298 | 	cd->dlz_closeversion = (dlz_dlopen_closeversion_t *)
299 | 		dl_load_symbol(cd, "dlz_closeversion",
300 | 			       (cd->dlz_newversion != NULL));
301 | 	cd->dlz_configure = (dlz_dlopen_configure_t *)
302 | 		dl_load_symbol(cd, "dlz_configure", false);
303 | 	cd->dlz_ssumatch = (dlz_dlopen_ssumatch_t *)
304 | 		dl_load_symbol(cd, "dlz_ssumatch", false);
305 | 	cd->dlz_addrdataset = (dlz_dlopen_addrdataset_t *)
306 | 		dl_load_symbol(cd, "dlz_addrdataset", false);
307 | 	cd->dlz_subrdataset = (dlz_dlopen_subrdataset_t *)
308 | 		dl_load_symbol(cd, "dlz_subrdataset", false);
309 | 	cd->dlz_delrdataset = (dlz_dlopen_delrdataset_t *)
310 | 		dl_load_symbol(cd, "dlz_delrdataset", false);
311 | 
314 | 	if (cd->version < (DLZ_DLOPEN_VERSION - DLZ_DLOPEN_AGE) ||
315 | 	    cd->version > DLZ_DLOPEN_VERSION)
316 | 	{
317 | 		dlopen_log(ISC_LOG_ERROR,
318 | 			   "dlz_dlopen: %s: incorrect driver API version %d, "
319 | 			   "requires %d",
320 | 			   cd->dl_path, cd->version, DLZ_DLOPEN_VERSION);
332 | 	MAYBE_LOCK(cd);
333 | 	result = cd->dlz_create(dlzname, argc-1, argv+1,
334 | 				&cd->dbdata,
335 | 				"log", dlopen_log,
336 | 				"putrr", dns_sdlz_putrr,
337 | 				"putnamedrr", dns_sdlz_putnamedrr,
348 | cleanup_lock:
349 | 	isc_mutex_destroy(&cd->lock);
350 | failed:
351 | 	dlopen_log(ISC_LOG_ERROR, "dlz_dlopen of '%s' failed", dlzname);
352 | 	if (cd->dl_path) {
353 | 		isc_mem_free(mctx, cd->dl_path);
371 |  * Called when bind is shutting down
372 |  */
373 | static void
374 | dlopen_dlz_destroy(void *driverarg, void *dbdata) {
375 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
376 | 	isc_mem_t *mctx;
377 | 
402 |  * Called to start a transaction
403 |  */
404 | static isc_result_t
405 | dlopen_dlz_newversion(const char *zone, void *driverarg, void *dbdata,
406 | 		      void **versionp)
407 | {
408 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
409 | 	isc_result_t result;
410 | 
423 |  * Called to end a transaction
424 |  */
425 | static void
426 | dlopen_dlz_closeversion(const char *zone, bool commit,
427 | 			void *driverarg, void *dbdata, void **versionp)
428 | {
429 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
430 | 
431 | 	UNUSED(driverarg);
444 |  * Called on startup to configure any writeable zones
445 |  */
446 | static isc_result_t
447 | dlopen_dlz_configure(dns_view_t *view, dns_dlzdb_t *dlzdb,
448 | 		     void *driverarg, void *dbdata)
449 | {
450 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
451 | 	isc_result_t result;
452 | 
469 |  * Check for authority to change a name
470 |  */
471 | static bool
472 | dlopen_dlz_ssumatch(const char *signer, const char *name, const char *tcpaddr,
473 | 		    const char *type, const char *key, uint32_t keydatalen,
474 | 		    unsigned char *keydata, void *driverarg, void *dbdata)
475 | {
476 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
477 | 	bool ret;
478 | 
494 |  * Add an rdataset
495 |  */
496 | static isc_result_t
497 | dlopen_dlz_addrdataset(const char *name, const char *rdatastr,
498 | 		       void *driverarg, void *dbdata, void *version)
499 | {
500 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
501 | 	isc_result_t result;
502 | 
516 |  * Subtract an rdataset
517 |  */
518 | static isc_result_t
519 | dlopen_dlz_subrdataset(const char *name, const char *rdatastr,
520 | 		       void *driverarg, void *dbdata, void *version)
521 | {
522 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
523 | 	isc_result_t result;
524 | 
538 |   delete a rdataset
539 |  */
540 | static isc_result_t
541 | dlopen_dlz_delrdataset(const char *name, const char *type,
542 | 		       void *driverarg, void *dbdata, void *version)
543 | {
544 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
545 | 	isc_result_t result;
546 | 
557 | }
558 | 
559 | 
560 | static dns_sdlzmethods_t dlz_dlopen_methods = {
561 | 	dlopen_dlz_create,
562 | 	dlopen_dlz_destroy,
563 | 	dlopen_dlz_findzonedb,
564 | 	dlopen_dlz_lookup,
565 | 	dlopen_dlz_authority,
566 | 	dlopen_dlz_allnodes,
567 | 	dlopen_dlz_allowzonexfr,
568 | 	dlopen_dlz_newversion,
569 | 	dlopen_dlz_closeversion,
570 | 	dlopen_dlz_configure,
571 | 	dlopen_dlz_ssumatch,
572 | 	dlopen_dlz_addrdataset,
573 | 	dlopen_dlz_subrdataset,
574 | 	dlopen_dlz_delrdataset
575 | };
576 | #endif
579 |  * Register driver with BIND
580 |  */
581 | isc_result_t
582 | dlz_dlopen_init(isc_mem_t *mctx) {
583 | #ifndef ISC_DLZ_DLOPEN
584 | 	UNUSED(mctx);
586 | #else
587 | 	isc_result_t result;
588 | 
589 | 	dlopen_log(2, "Registering DLZ_dlopen driver");
590 | 
591 | 	result = dns_sdlzregister("dlopen", &dlz_dlopen_methods, NULL,
592 | 				  DNS_SDLZFLAG_RELATIVEOWNER |
593 | 				  DNS_SDLZFLAG_RELATIVERDATA |
594 | 				  DNS_SDLZFLAG_THREADSAFE,
595 | 				  mctx, &dlz_dlopen);
596 | 
597 | 	if (result != ISC_R_SUCCESS) {
610 |  * Unregister the driver
611 |  */
612 | void
613 | dlz_dlopen_clear(void) {
614 | #ifdef ISC_DLZ_DLOPEN
615 | 	dlopen_log(2, "Unregistering DLZ_dlopen driver");
616 | 	if (dlz_dlopen != NULL)
617 | 		dns_sdlzunregister(&dlz_dlopen);
618 | #endif
619 | }
{% endraw %}

```
### bin/tests/system/feature-test.c

```c

{% raw %}
40 | 	fprintf(stderr, "	--enable-dnsrps\n");
41 | 	fprintf(stderr, "	--gethostname\n");
42 | 	fprintf(stderr, "	--gssapi\n");
43 | 	fprintf(stderr, "	--have-dlopen\n");
44 | 	fprintf(stderr, "	--have-geoip\n");
45 | 	fprintf(stderr, "	--have-geoip2\n");
111 | #endif
112 | 	}
113 | 
114 | 	if (strcmp(argv[1], "--have-dlopen") == 0) {
115 | #if defined(HAVE_DLOPEN) && defined(ISC_DLZ_DLOPEN)
116 | 		return (0);
{% endraw %}

```
### bin/tests/system/dlzexternal/driver.h

```c

{% raw %}
13 |  * This header includes the declarations of entry points.
14 |  */
15 | 
16 | dlz_dlopen_version_t dlz_version;
17 | dlz_dlopen_create_t dlz_create;
18 | dlz_dlopen_destroy_t dlz_destroy;
19 | dlz_dlopen_findzonedb_t dlz_findzonedb;
20 | dlz_dlopen_lookup_t dlz_lookup;
21 | dlz_dlopen_allowzonexfr_t dlz_allowzonexfr;
22 | dlz_dlopen_allnodes_t dlz_allnodes;
23 | dlz_dlopen_newversion_t dlz_newversion;
24 | dlz_dlopen_closeversion_t dlz_closeversion;
25 | dlz_dlopen_configure_t dlz_configure;
26 | dlz_dlopen_ssumatch_t dlz_ssumatch;
27 | dlz_dlopen_addrdataset_t dlz_addrdataset;
28 | dlz_dlopen_subrdataset_t dlz_subrdataset;
29 | dlz_dlopen_delrdataset_t dlz_delrdataset;
30 | 
{% endraw %}

```
### lib/ns/hooks.c

```c

{% raw %}
151 | 	flags |= RTLD_DEEPBIND;
152 | #endif
153 | 
154 | 	handle = dlopen(modpath, flags);
155 | 	if (handle == NULL) {
156 | 		const char *errmsg = dlerror();
159 | 		}
160 | 		isc_log_write(ns_lctx, NS_LOGCATEGORY_GENERAL,
161 | 			      NS_LOGMODULE_HOOKS, ISC_LOG_ERROR,
162 | 			      "failed to dlopen() plugin '%s': %s",
163 | 			      modpath, errmsg);
164 | 		return (ISC_R_FAILURE);
{% endraw %}

```
### lib/isc/unix/pk11_api.c

```c

{% raw %}
41 | 	if (hPK11 != NULL)
42 | 		return (CKR_LIBRARY_ALREADY_INITIALIZED);
43 | 
44 | 	hPK11 = dlopen(pk11_get_lib_name(), RTLD_NOW);
45 | 
46 | 	if (hPK11 == NULL) {
47 | 		snprintf(loaderrmsg, sizeof(loaderrmsg),
48 | 			 "dlopen(\"%s\") failed: %s\n",
49 | 			 pk11_get_lib_name(), dlerror());
50 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
141 | 	static void *pPK11 = NULL;
142 | 
143 | 	if (hPK11 == NULL)
144 | 		hPK11 = dlopen(pk11_get_lib_name(), RTLD_NOW);
145 | 	if (hPK11 == NULL) {
146 | 		snprintf(loaderrmsg, sizeof(loaderrmsg),
147 | 			 "dlopen(\"%s\") failed: %s\n",
148 | 			 pk11_get_lib_name(), dlerror());
149 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
{% endraw %}

```
### lib/dns/dyndb.c

```c

{% raw %}
136 | 	flags |= RTLD_DEEPBIND;
137 | #endif
138 | 
139 | 	handle = dlopen(filename, flags);
140 | 	if (handle == NULL)
141 | 		CHECK(ISC_R_FAILURE);
{% endraw %}

```
### lib/dns/include/dns/librpz.h

```c

{% raw %}
891 | 	if (dl_handle != NULL && *dl_handle != NULL) {
892 | 		if (dlclose(*dl_handle) != 0) {
893 | 			snprintf(emsg->c, sizeof(librpz_emsg_t),
894 | 				 "dlopen(NULL): %s", dlerror());
895 | 			return (NULL);
896 | 		}
902 | 	 * linked to librpz.
903 | 	 * Do not worry if we cannot search the main executable of the process.
904 | 	 */
905 | 	handle = dlopen(NULL, RTLD_NOW | RTLD_LOCAL);
906 | 	if (handle != NULL) {
907 | 		new_librpz = dlsym(handle, LIBRPZ_DEF_STR);
920 | 
921 | 	if (path == NULL || path[0] == '\0') {
922 | 		snprintf(emsg->c, sizeof(librpz_emsg_t),
923 | 			 "librpz not linked and no dlopen() path provided");
924 | 		return (NULL);
925 | 	}
926 | 
927 | 	handle = dlopen(path, RTLD_NOW | RTLD_LOCAL);
928 | 	if (handle == NULL) {
929 | 		snprintf(emsg->c, sizeof(librpz_emsg_t), "dlopen(%s): %s",
930 | 			 path, dlerror());
931 | 		return (NULL);
{% endraw %}

```
### lib/dns/include/dns/dlz_dlopen.h

```c

{% raw %}
33 |  * dlz_dlopen_version() is required for all DLZ external drivers. It
34 |  * should return DLZ_DLOPEN_VERSION
35 |  */
36 | typedef int dlz_dlopen_version_t(unsigned int *flags);
37 | 
38 | /*
39 |  * dlz_dlopen_create() is required for all DLZ external drivers.
40 |  */
41 | typedef isc_result_t dlz_dlopen_create_t(const char *dlzname,
42 | 					 unsigned int argc,
43 | 					 char *argv[],
48 |  * dlz_dlopen_destroy() is optional, and will be called when the
49 |  * driver is unloaded if supplied
50 |  */
51 | typedef void dlz_dlopen_destroy_t(void *dbdata);
52 | 
53 | /*
54 |  * dlz_dlopen_findzonedb() is required for all DLZ external drivers
55 |  */
56 | typedef isc_result_t dlz_dlopen_findzonedb_t(void *dbdata,
57 | 					     const char *name,
58 | 					     dns_clientinfomethods_t *methods,
61 | /*
62 |  * dlz_dlopen_lookup() is required for all DLZ external drivers
63 |  */
64 | typedef isc_result_t dlz_dlopen_lookup_t(const char *zone,
65 | 					 const char *name,
66 | 					 void *dbdata,
72 |  * dlz_dlopen_authority is optional() if dlz_dlopen_lookup()
73 |  * supplies authority information for the dns record
74 |  */
75 | typedef isc_result_t dlz_dlopen_authority_t(const char *zone,
76 | 					    void *dbdata,
77 | 					    dns_sdlzlookup_t *lookup);
80 |  * dlz_dlopen_allowzonexfr() is optional, and should be supplied if
81 |  * you want to support zone transfers
82 |  */
83 | typedef isc_result_t dlz_dlopen_allowzonexfr_t(void *dbdata,
84 | 					       const char *name,
85 | 					       const char *client);
88 |  * dlz_dlopen_allnodes() is optional, but must be supplied if supply a
89 |  * dlz_dlopen_allowzonexfr() function
90 |  */
91 | typedef isc_result_t dlz_dlopen_allnodes_t(const char *zone,
92 | 					   void *dbdata,
93 | 					   dns_sdlzallnodes_t *allnodes);
96 |  * dlz_dlopen_newversion() is optional. It should be supplied if you
97 |  * want to support dynamic updates.
98 |  */
99 | typedef isc_result_t dlz_dlopen_newversion_t(const char *zone,
100 | 					     void *dbdata,
101 | 					     void **versionp);
104 |  * dlz_closeversion() is optional, but must be supplied if you supply
105 |  * a dlz_newversion() function
106 |  */
107 | typedef void dlz_dlopen_closeversion_t(const char *zone,
108 | 				       bool commit,
109 | 				       void *dbdata,
113 |  * dlz_dlopen_configure() is optional, but must be supplied if you
114 |  * want to support dynamic updates
115 |  */
116 | typedef isc_result_t dlz_dlopen_configure_t(dns_view_t *view,
117 | 					    dns_dlzdb_t *dlzdb,
118 | 					    void *dbdata);
122 |  * want to retrieve information about the client (e.g., source address)
123 |  * before sending a replay.
124 |  */
125 | typedef isc_result_t dlz_dlopen_setclientcallback_t(dns_view_t *view,
126 | 						    void *dbdata);
127 | 
130 |  * dlz_dlopen_ssumatch() is optional, but must be supplied if you want
131 |  * to support dynamic updates
132 |  */
133 | typedef bool dlz_dlopen_ssumatch_t(const char *signer,
134 | 					    const char *name,
135 | 					    const char *tcpaddr,
143 |  * dlz_dlopen_addrdataset() is optional, but must be supplied if you
144 |  * want to support dynamic updates
145 |  */
146 | typedef isc_result_t dlz_dlopen_addrdataset_t(const char *name,
147 | 					      const char *rdatastr,
148 | 					      void *dbdata,
152 |  * dlz_dlopen_subrdataset() is optional, but must be supplied if you
153 |  * want to support dynamic updates
154 |  */
155 | typedef isc_result_t dlz_dlopen_subrdataset_t(const char *name,
156 | 					      const char *rdatastr,
157 | 					      void *dbdata,
161 |  * dlz_dlopen_delrdataset() is optional, but must be supplied if you
162 |  * want to support dynamic updates
163 |  */
164 | typedef isc_result_t dlz_dlopen_delrdataset_t(const char *name,
165 | 					      const char *type,
166 | 					      void *dbdata,
{% endraw %}

```