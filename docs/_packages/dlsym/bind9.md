---
name: "bind9"
layout: package
next_package: libbsd
previous_package: libuv
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 9_14_6
9 / 3884 files match, 5 filtered matches.

 - [bin/named/unix/dlz_dlopen_driver.c](#binnamedunixdlz_dlopen_driverc)
 - [lib/ns/hooks.c](#libnshooksc)
 - [lib/isc/unix/pk11_api.c](#libiscunixpk11_apic)
 - [lib/dns/dyndb.c](#libdnsdyndbc)
 - [lib/dns/include/dns/librpz.h](#libdnsincludednslibrpzh)

### bin/named/unix/dlz_dlopen_driver.c

```c

{% raw %}
197 |  */
198 | static void *
199 | dl_load_symbol(dlopen_data_t *cd, const char *symbol, bool mandatory) {
200 | 	void *ptr = dlsym(cd->dl_handle, symbol);
201 | 	if (ptr == NULL && mandatory) {
202 | 		dlopen_log(ISC_LOG_ERROR,
{% endraw %}

```
### lib/ns/hooks.c

```c

{% raw %}
114 | 	 * if there is one.)
115 | 	 */
116 | 	dlerror();
117 | 	symbol = dlsym(handle, symbol_name);
118 | 	if (symbol == NULL) {
119 | 		const char *errmsg = dlerror();
{% endraw %}

```
### lib/isc/unix/pk11_api.c

```c

{% raw %}
49 | 			 pk11_get_lib_name(), dlerror());
50 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
51 | 	}
52 | 	sym = (CK_C_Initialize)dlsym(hPK11, "C_Initialize");
53 | 	if (sym == NULL)
54 | 		return (CKR_SYMBOL_RESOLUTION_FAILED);
66 | 
67 | 	if (hPK11 == NULL)
68 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
69 | 	sym = (CK_C_Finalize)dlsym(hPK11, "C_Finalize");
70 | 	if (sym == NULL)
71 | 		return (CKR_SYMBOL_RESOLUTION_FAILED);
87 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
88 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
89 | 		pPK11 = hPK11;
90 | 		sym = (CK_C_GetSlotList)dlsym(hPK11, "C_GetSlotList");
91 | 	}
92 | 	if (sym == NULL)
103 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
104 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
105 | 		pPK11 = hPK11;
106 | 		sym = (CK_C_GetTokenInfo)dlsym(hPK11, "C_GetTokenInfo");
107 | 	}
108 | 	if (sym == NULL)
121 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
122 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
123 | 		pPK11 = hPK11;
124 | 		sym = (CK_C_GetMechanismInfo)dlsym(hPK11,
125 | 						   "C_GetMechanismInfo");
126 | 	}
150 | 	}
151 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
152 | 		pPK11 = hPK11;
153 | 		sym = (CK_C_OpenSession)dlsym(hPK11, "C_OpenSession");
154 | 	}
155 | 	if (sym == NULL)
166 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
167 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
168 | 		pPK11 = hPK11;
169 | 		sym = (CK_C_CloseSession)dlsym(hPK11, "C_CloseSession");
170 | 	}
171 | 	if (sym == NULL)
184 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
185 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
186 | 		pPK11 = hPK11;
187 | 		sym = (CK_C_Login)dlsym(hPK11, "C_Login");
188 | 	}
189 | 	if (sym == NULL)
200 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
201 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
202 | 		pPK11 = hPK11;
203 | 		sym = (CK_C_Logout)dlsym(hPK11, "C_Logout");
204 | 	}
205 | 	if (sym == NULL)
218 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
219 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
220 | 		pPK11 = hPK11;
221 | 		sym = (CK_C_CreateObject)dlsym(hPK11, "C_CreateObject");
222 | 	}
223 | 	if (sym == NULL)
234 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
235 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
236 | 		pPK11 = hPK11;
237 | 		sym = (CK_C_DestroyObject)dlsym(hPK11, "C_DestroyObject");
238 | 	}
239 | 	if (sym == NULL)
252 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
253 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
254 | 		pPK11 = hPK11;
255 | 		sym = (CK_C_GetAttributeValue)dlsym(hPK11,
256 | 						    "C_GetAttributeValue");
257 | 	}
271 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
272 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
273 | 		pPK11 = hPK11;
274 | 		sym = (CK_C_SetAttributeValue)dlsym(hPK11,
275 | 						    "C_SetAttributeValue");
276 | 	}
290 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
291 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
292 | 		pPK11 = hPK11;
293 | 		sym = (CK_C_FindObjectsInit)dlsym(hPK11, "C_FindObjectsInit");
294 | 	}
295 | 	if (sym == NULL)
308 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
309 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
310 | 		pPK11 = hPK11;
311 | 		sym = (CK_C_FindObjects)dlsym(hPK11, "C_FindObjects");
312 | 	}
313 | 	if (sym == NULL)
325 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
326 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
327 | 		pPK11 = hPK11;
328 | 		sym = (CK_C_FindObjectsFinal)dlsym(hPK11,
329 | 						   "C_FindObjectsFinal");
330 | 	}
344 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
345 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
346 | 		pPK11 = hPK11;
347 | 		sym = (CK_C_EncryptInit)dlsym(hPK11, "C_EncryptInit");
348 | 	}
349 | 	if (sym == NULL)
363 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
364 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
365 | 		pPK11 = hPK11;
366 | 		sym = (CK_C_Encrypt)dlsym(hPK11, "C_Encrypt");
367 | 	}
368 | 	if (sym == NULL)
380 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
381 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
382 | 		pPK11 = hPK11;
383 | 		sym = (CK_C_DigestInit)dlsym(hPK11, "C_DigestInit");
384 | 	}
385 | 	if (sym == NULL)
398 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
399 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
400 | 		pPK11 = hPK11;
401 | 		sym = (CK_C_DigestUpdate)dlsym(hPK11, "C_DigestUpdate");
402 | 	}
403 | 	if (sym == NULL)
416 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
417 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
418 | 		pPK11 = hPK11;
419 | 		sym = (CK_C_DigestFinal)dlsym(hPK11, "C_DigestFinal");
420 | 	}
421 | 	if (sym == NULL)
434 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
435 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
436 | 		pPK11 = hPK11;
437 | 		sym = (CK_C_SignInit)dlsym(hPK11, "C_SignInit");
438 | 	}
439 | 	if (sym == NULL)
453 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
454 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
455 | 		pPK11 = hPK11;
456 | 		sym = (CK_C_Sign)dlsym(hPK11, "C_Sign");
457 | 	}
458 | 	if (sym == NULL)
471 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
472 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
473 | 		pPK11 = hPK11;
474 | 		sym = (CK_C_SignUpdate)dlsym(hPK11, "C_SignUpdate");
475 | 	}
476 | 	if (sym == NULL)
489 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
490 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
491 | 		pPK11 = hPK11;
492 | 		sym = (CK_C_SignFinal)dlsym(hPK11, "C_SignFinal");
493 | 	}
494 | 	if (sym == NULL)
507 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
508 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
509 | 		pPK11 = hPK11;
510 | 		sym = (CK_C_VerifyInit)dlsym(hPK11, "C_VerifyInit");
511 | 	}
512 | 	if (sym == NULL)
526 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
527 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
528 | 		pPK11 = hPK11;
529 | 		sym = (CK_C_Verify)dlsym(hPK11, "C_Verify");
530 | 	}
531 | 	if (sym == NULL)
544 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
545 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
546 | 		pPK11 = hPK11;
547 | 		sym = (CK_C_VerifyUpdate)dlsym(hPK11, "C_VerifyUpdate");
548 | 	}
549 | 	if (sym == NULL)
562 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
563 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
564 | 		pPK11 = hPK11;
565 | 		sym = (CK_C_VerifyFinal)dlsym(hPK11, "C_VerifyFinal");
566 | 	}
567 | 	if (sym == NULL)
581 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
582 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
583 | 		pPK11 = hPK11;
584 | 		sym = (CK_C_GenerateKey)dlsym(hPK11, "C_GenerateKey");
585 | 	}
586 | 	if (sym == NULL)
605 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
606 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
607 | 		pPK11 = hPK11;
608 | 		sym = (CK_C_GenerateKeyPair)dlsym(hPK11, "C_GenerateKeyPair");
609 | 	}
610 | 	if (sym == NULL)
631 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
632 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
633 | 		pPK11 = hPK11;
634 | 		sym = (CK_C_DeriveKey)dlsym(hPK11, "C_DeriveKey");
635 | 	}
636 | 	if (sym == NULL)
654 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
655 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
656 | 		pPK11 = hPK11;
657 | 		sym = (CK_C_SeedRandom)dlsym(hPK11, "C_SeedRandom");
658 | 	}
659 | 	if (sym == NULL)
672 | 		return (CKR_LIBRARY_FAILED_TO_LOAD);
673 | 	if ((sym == NULL) || (hPK11 != pPK11)) {
674 | 		pPK11 = hPK11;
675 | 		sym = (CK_C_GenerateRandom)dlsym(hPK11, "C_GenerateRandom");
676 | 	}
677 | 	if (sym == NULL)
{% endraw %}

```
### lib/dns/dyndb.c

```c

{% raw %}
93 | 	REQUIRE(handle != NULL);
94 | 	REQUIRE(symbolp != NULL && *symbolp == NULL);
95 | 
96 | 	symbol = dlsym(handle, symbol_name);
97 | 	if (symbol == NULL) {
98 | 		errmsg = dlerror();
{% endraw %}

```
### lib/dns/include/dns/librpz.h

```c

{% raw %}
904 | 	 */
905 | 	handle = dlopen(NULL, RTLD_NOW | RTLD_LOCAL);
906 | 	if (handle != NULL) {
907 | 		new_librpz = dlsym(handle, LIBRPZ_DEF_STR);
908 | 		if (new_librpz != NULL) {
909 | 			if (dl_handle != NULL)
912 | 		}
913 | 		if (dlclose(handle) != 0) {
914 | 			snprintf(emsg->c, sizeof(librpz_emsg_t),
915 | 				 "dlsym(NULL, "LIBRPZ_DEF_STR"): %s",
916 | 				 dlerror());
917 | 			return (NULL);
930 | 			 path, dlerror());
931 | 		return (NULL);
932 | 	}
933 | 	new_librpz = dlsym(handle, LIBRPZ_DEF_STR);
934 | 	if (new_librpz != NULL) {
935 | 		if (dl_handle != NULL)
937 | 		return (new_librpz);
938 | 	}
939 | 	snprintf(emsg->c, sizeof(librpz_emsg_t),
940 | 		 "dlsym(%s, "LIBRPZ_DEF_STR"): %s",
941 | 		 path, dlerror());
942 | 	dlclose(handle);
{% endraw %}

```