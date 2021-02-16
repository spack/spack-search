---
name: "bind9"
layout: package
next_package: aria2
previous_package: py-setuptools
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
1179 | 	result = dlz_dlopen_init(named_g_mctx);
1181 | 		named_main_earlyfatal("dlz_dlopen_init() failed: %s",
1259 | 	dlz_dlopen_clear();
{% endraw %}

```
### bin/named/include/dlz/dlz_dlopen_driver.h

```c

{% raw %}
16 | dlz_dlopen_init(isc_mem_t *mctx);
19 | dlz_dlopen_clear(void);
{% endraw %}

```
### bin/named/unix/dlz_dlopen_driver.c

```c

{% raw %}
37 | static dns_sdlzimplementation_t *dlz_dlopen = NULL;
40 | typedef struct dlopen_data {
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
86 | static void dlopen_log(int level, const char *fmt, ...)
101 | dlopen_dlz_allnodes(const char *zone, void *driverarg, void *dbdata,
104 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
122 | dlopen_dlz_allowzonexfr(void *driverarg, void *dbdata, const char *name,
125 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
142 | dlopen_dlz_authority(const char *zone, void *driverarg, void *dbdata,
145 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
161 | dlopen_dlz_findzonedb(void *driverarg, void *dbdata, const char *name,
165 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
178 | dlopen_dlz_lookup(const char *zone, const char *name, void *driverarg,
183 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
199 | dl_load_symbol(dlopen_data_t *cd, const char *symbol, bool mandatory) {
202 | 		dlopen_log(ISC_LOG_ERROR,
203 | 			   "dlz_dlopen: library '%s' is missing "
213 | dlopen_dlz_create(const char *dlzname, unsigned int argc, char *argv[],
216 | 	dlopen_data_t *cd;
219 | 	int dlopen_flags = 0;
224 | 		dlopen_log(ISC_LOG_ERROR,
225 | 			   "dlz_dlopen driver for '%s' needs a path to "
259 | 	dlopen_flags = RTLD_NOW|RTLD_GLOBAL;
271 | 	dlopen_flags |= RTLD_DEEPBIND;
274 | 	cd->dl_handle = dlopen(cd->dl_path, dlopen_flags);
276 | 		dlopen_log(ISC_LOG_ERROR,
277 | 			   "dlz_dlopen failed to open library '%s' - %s",
284 | 	cd->dlz_version = (dlz_dlopen_version_t *)
286 | 	cd->dlz_create = (dlz_dlopen_create_t *)
288 | 	cd->dlz_lookup = (dlz_dlopen_lookup_t *)
290 | 	cd->dlz_findzonedb = (dlz_dlopen_findzonedb_t *)
303 | 	cd->dlz_allowzonexfr = (dlz_dlopen_allowzonexfr_t *)
305 | 	cd->dlz_allnodes = (dlz_dlopen_allnodes_t *)
308 | 	cd->dlz_authority = (dlz_dlopen_authority_t *)
310 | 	cd->dlz_newversion = (dlz_dlopen_newversion_t *)
312 | 	cd->dlz_closeversion = (dlz_dlopen_closeversion_t *)
315 | 	cd->dlz_configure = (dlz_dlopen_configure_t *)
317 | 	cd->dlz_ssumatch = (dlz_dlopen_ssumatch_t *)
319 | 	cd->dlz_addrdataset = (dlz_dlopen_addrdataset_t *)
321 | 	cd->dlz_subrdataset = (dlz_dlopen_subrdataset_t *)
323 | 	cd->dlz_delrdataset = (dlz_dlopen_delrdataset_t *)
325 | 	cd->dlz_destroy = (dlz_dlopen_destroy_t *)
333 | 		dlopen_log(ISC_LOG_ERROR,
334 | 			   "dlz_dlopen: %s: incorrect driver API version %d, "
351 | 				"log", dlopen_log,
365 | 	dlopen_log(ISC_LOG_ERROR, "dlz_dlopen of '%s' failed", dlzname);
372 | 	if (dlopen_flags != 0) {
389 | dlopen_dlz_destroy(void *driverarg, void *dbdata) {
390 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
425 | dlopen_dlz_newversion(const char *zone, void *driverarg, void *dbdata,
428 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
446 | dlopen_dlz_closeversion(const char *zone, bool commit,
449 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
467 | dlopen_dlz_configure(dns_view_t *view, dns_dlzdb_t *dlzdb,
470 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
492 | dlopen_dlz_ssumatch(const char *signer, const char *name, const char *tcpaddr,
496 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
517 | dlopen_dlz_addrdataset(const char *name, const char *rdatastr,
520 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
539 | dlopen_dlz_subrdataset(const char *name, const char *rdatastr,
542 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
561 | dlopen_dlz_delrdataset(const char *name, const char *type,
564 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
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
602 | dlz_dlopen_init(isc_mem_t *mctx) {
609 | 	dlopen_log(2, "Registering DLZ_dlopen driver");
611 | 	result = dns_sdlzregister("dlopen", &dlz_dlopen_methods, NULL,
615 | 				  mctx, &dlz_dlopen);
633 | dlz_dlopen_clear(void) {
635 | 	dlopen_log(2, "Unregistering DLZ_dlopen driver");
636 | 	if (dlz_dlopen != NULL)
637 | 		dns_sdlzunregister(&dlz_dlopen);
{% endraw %}

```
### bin/named/win32/dlz_dlopen_driver.c

```c

{% raw %}
36 | static dns_sdlzimplementation_t *dlz_dlopen = NULL;
39 | typedef struct dlopen_data {
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
85 | static void dlopen_log(int level, const char *fmt, ...)
100 | dlopen_dlz_allnodes(const char *zone, void *driverarg, void *dbdata,
103 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
121 | dlopen_dlz_allowzonexfr(void *driverarg, void *dbdata, const char *name,
124 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
141 | dlopen_dlz_authority(const char *zone, void *driverarg, void *dbdata,
144 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
160 | dlopen_dlz_findzonedb(void *driverarg, void *dbdata, const char *name,
164 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
177 | dlopen_dlz_lookup(const char *zone, const char *name, void *driverarg,
182 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
198 | dl_load_symbol(dlopen_data_t *cd, const char *symbol, bool mandatory) {
201 | 		dlopen_log(ISC_LOG_ERROR,
202 | 			   "dlz_dlopen: library '%s' is missing "
212 | dlopen_dlz_create(const char *dlzname, unsigned int argc, char *argv[],
215 | 	dlopen_data_t *cd;
223 | 		dlopen_log(ISC_LOG_ERROR,
224 | 			   "dlz_dlopen driver for '%s' needs a path to "
262 | 		dlopen_log(ISC_LOG_ERROR,
263 | 			   "dlz_dlopen failed to open library '%s' - %u",
270 | 	cd->dlz_version = (dlz_dlopen_version_t *)
272 | 	cd->dlz_create = (dlz_dlopen_create_t *)
274 | 	cd->dlz_lookup = (dlz_dlopen_lookup_t *)
276 | 	cd->dlz_findzonedb = (dlz_dlopen_findzonedb_t *)
289 | 	cd->dlz_allowzonexfr = (dlz_dlopen_allowzonexfr_t *)
291 | 	cd->dlz_allnodes = (dlz_dlopen_allnodes_t *)
294 | 	cd->dlz_authority = (dlz_dlopen_authority_t *)
296 | 	cd->dlz_newversion = (dlz_dlopen_newversion_t *)
298 | 	cd->dlz_closeversion = (dlz_dlopen_closeversion_t *)
301 | 	cd->dlz_configure = (dlz_dlopen_configure_t *)
303 | 	cd->dlz_ssumatch = (dlz_dlopen_ssumatch_t *)
305 | 	cd->dlz_addrdataset = (dlz_dlopen_addrdataset_t *)
307 | 	cd->dlz_subrdataset = (dlz_dlopen_subrdataset_t *)
309 | 	cd->dlz_delrdataset = (dlz_dlopen_delrdataset_t *)
317 | 		dlopen_log(ISC_LOG_ERROR,
318 | 			   "dlz_dlopen: %s: incorrect driver API version %d, "
335 | 				"log", dlopen_log,
351 | 	dlopen_log(ISC_LOG_ERROR, "dlz_dlopen of '%s' failed", dlzname);
374 | dlopen_dlz_destroy(void *driverarg, void *dbdata) {
375 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
405 | dlopen_dlz_newversion(const char *zone, void *driverarg, void *dbdata,
408 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
426 | dlopen_dlz_closeversion(const char *zone, bool commit,
429 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
447 | dlopen_dlz_configure(dns_view_t *view, dns_dlzdb_t *dlzdb,
450 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
472 | dlopen_dlz_ssumatch(const char *signer, const char *name, const char *tcpaddr,
476 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
497 | dlopen_dlz_addrdataset(const char *name, const char *rdatastr,
500 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
519 | dlopen_dlz_subrdataset(const char *name, const char *rdatastr,
522 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
541 | dlopen_dlz_delrdataset(const char *name, const char *type,
544 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
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
582 | dlz_dlopen_init(isc_mem_t *mctx) {
589 | 	dlopen_log(2, "Registering DLZ_dlopen driver");
591 | 	result = dns_sdlzregister("dlopen", &dlz_dlopen_methods, NULL,
595 | 				  mctx, &dlz_dlopen);
613 | dlz_dlopen_clear(void) {
615 | 	dlopen_log(2, "Unregistering DLZ_dlopen driver");
616 | 	if (dlz_dlopen != NULL)
617 | 		dns_sdlzunregister(&dlz_dlopen);
{% endraw %}

```
### bin/tests/system/feature-test.c

```c

{% raw %}
43 | 	fprintf(stderr, "	--have-dlopen\n");
114 | 	if (strcmp(argv[1], "--have-dlopen") == 0) {
{% endraw %}

```
### bin/tests/system/dlzexternal/driver.h

```c

{% raw %}
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
{% endraw %}

```
### lib/ns/hooks.c

```c

{% raw %}
154 | 	handle = dlopen(modpath, flags);
162 | 			      "failed to dlopen() plugin '%s': %s",
{% endraw %}

```
### lib/isc/unix/pk11_api.c

```c

{% raw %}
44 | 	hPK11 = dlopen(pk11_get_lib_name(), RTLD_NOW);
48 | 			 "dlopen(\"%s\") failed: %s\n",
144 | 		hPK11 = dlopen(pk11_get_lib_name(), RTLD_NOW);
147 | 			 "dlopen(\"%s\") failed: %s\n",
{% endraw %}

```
### lib/dns/dyndb.c

```c

{% raw %}
139 | 	handle = dlopen(filename, flags);
{% endraw %}

```
### lib/dns/include/dns/librpz.h

```c

{% raw %}
894 | 				 "dlopen(NULL): %s", dlerror());
905 | 	handle = dlopen(NULL, RTLD_NOW | RTLD_LOCAL);
923 | 			 "librpz not linked and no dlopen() path provided");
927 | 	handle = dlopen(path, RTLD_NOW | RTLD_LOCAL);
929 | 		snprintf(emsg->c, sizeof(librpz_emsg_t), "dlopen(%s): %s",
{% endraw %}

```
### lib/dns/include/dns/dlz_dlopen.h

```c

{% raw %}
36 | typedef int dlz_dlopen_version_t(unsigned int *flags);
41 | typedef isc_result_t dlz_dlopen_create_t(const char *dlzname,
51 | typedef void dlz_dlopen_destroy_t(void *dbdata);
56 | typedef isc_result_t dlz_dlopen_findzonedb_t(void *dbdata,
64 | typedef isc_result_t dlz_dlopen_lookup_t(const char *zone,
75 | typedef isc_result_t dlz_dlopen_authority_t(const char *zone,
83 | typedef isc_result_t dlz_dlopen_allowzonexfr_t(void *dbdata,
91 | typedef isc_result_t dlz_dlopen_allnodes_t(const char *zone,
99 | typedef isc_result_t dlz_dlopen_newversion_t(const char *zone,
107 | typedef void dlz_dlopen_closeversion_t(const char *zone,
116 | typedef isc_result_t dlz_dlopen_configure_t(dns_view_t *view,
125 | typedef isc_result_t dlz_dlopen_setclientcallback_t(dns_view_t *view,
133 | typedef bool dlz_dlopen_ssumatch_t(const char *signer,
146 | typedef isc_result_t dlz_dlopen_addrdataset_t(const char *name,
155 | typedef isc_result_t dlz_dlopen_subrdataset_t(const char *name,
164 | typedef isc_result_t dlz_dlopen_delrdataset_t(const char *name,
{% endraw %}

```