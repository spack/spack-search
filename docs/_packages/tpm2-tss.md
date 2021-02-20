---
name: "tpm2-tss"
layout: package
next_package: treelite
previous_package: timemory
languages: ['c']
---
## 3.0.0
7 / 739 files match, 2 filtered matches.

 - [src/tss2-esys/esys_int.h](#srctss2-esysesys_inth)
 - [test/unit/tctildr-dl.c](#testunittctildr-dlc)

### src/tss2-esys/esys_int.h

```c

{% raw %}
171 |     TSS2_TCTI_CONTEXT *tcti_app_param;/**< The TCTI context provided by the
172 |                                            application during Esys_Initialize()
173 |                                            to be returned from Esys_GetTcti().*/
174 |     void *dlhandle;              /**< The handle of dlopen if the tcti was
175 |                                       automatically loaded. */
176 |     IESYS_SESSION *enc_session;  /**< Ptr to the enc param session.
{% endraw %}

```
### test/unit/tctildr-dl.c

```c

{% raw %}
35 | }
36 | 
37 | void *
38 | __wrap_dlopen(const char *filename, int flags)
39 | {
40 |     LOG_TRACE("Called with filename %s and flags %x", filename, flags);
137 | #define TEST_TCTI_NAME "test-tcti"
138 | #define TEST_TCTI_CONF "test-conf"
139 | static void
140 | test_handle_from_name_first_dlopen_success (void **state)
141 | {
142 |     TSS2_RC rc;
143 |     void *handle = NULL;
144 | 
145 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME);
146 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
147 |     will_return(__wrap_dlopen, TEST_HANDLE);
148 | 
149 |     rc = handle_from_name (TEST_TCTI_NAME, &handle);
153 | 
154 | #define TEST_TCTI_NAME_SO_0 TCTI_PREFIX"-"TEST_TCTI_NAME""TCTI_SUFFIX_0
155 | static void
156 | test_handle_from_name_second_dlopen_success (void **state)
157 | {
158 |     TSS2_RC rc;
159 |     void *handle = NULL;
160 | 
161 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME);
162 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
163 |     will_return(__wrap_dlopen, NULL);
164 | 
165 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME_SO_0);
166 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
167 |     will_return(__wrap_dlopen, TEST_HANDLE);
168 | 
169 |     rc = handle_from_name (TEST_TCTI_NAME, &handle);
172 | }
173 | #define TEST_TCTI_NAME_SO TCTI_PREFIX"-"TEST_TCTI_NAME""TCTI_SUFFIX
174 | static void
175 | test_handle_from_name_third_dlopen_success (void **state)
176 | {
177 |     TSS2_RC rc;
178 |     void *handle = NULL;
179 | 
180 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME);
181 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
182 |     will_return(__wrap_dlopen, NULL);
183 | 
184 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME_SO_0);
185 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
186 |     will_return(__wrap_dlopen, NULL);
187 | 
188 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME_SO);
189 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
190 |     will_return(__wrap_dlopen, TEST_HANDLE);
191 | 
192 |     rc = handle_from_name (TEST_TCTI_NAME, &handle);
216 |     TSS2_TCTI_INFO *info = { 0, };
217 |     void *handle;
218 | 
219 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
220 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
221 |     will_return(__wrap_dlopen, NULL);
222 | 
223 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so.0");
224 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
225 |     will_return(__wrap_dlopen, NULL);
226 | 
227 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so");
228 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
229 |     will_return(__wrap_dlopen, NULL);
230 | 
231 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-tabrmd.so.0");
232 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
233 |     will_return(__wrap_dlopen, HANDLE);
234 | 
235 |     expect_value(__wrap_dlsym, handle, HANDLE);
248 |     TSS2_TCTI_INFO *info = { 0, };
249 |     void *handle;
250 | 
251 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
252 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
253 |     will_return(__wrap_dlopen, NULL);
254 | 
255 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so.0");
256 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
257 |     will_return(__wrap_dlopen, NULL);
258 | 
259 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so");
260 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
261 |     will_return(__wrap_dlopen, NULL);
262 | 
263 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-tabrmd.so.0");
264 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
265 |     will_return(__wrap_dlopen, HANDLE);
266 | 
267 |     expect_value(__wrap_dlsym, handle, HANDLE);
285 | {
286 |     TSS2_TCTI_CONTEXT *tcti;
287 | 
288 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
289 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
290 |     will_return(__wrap_dlopen, HANDLE);
291 | 
292 |     expect_value(__wrap_dlsym, handle, HANDLE);
314 |     TSS2_TCTI_CONTEXT *tcti;
315 | #define HANDLE (void *)123321
316 | 
317 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
318 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
319 |     will_return(__wrap_dlopen, HANDLE);
320 | 
321 |     expect_value(__wrap_dlsym, handle, HANDLE);
328 |     /** Now test
329 |      *{ "libtss2-tcti-tabrmd.so", NULL, "", "Access libtss2-tcti-tabrmd.so"},
330 |      */
331 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-tabrmd.so.0");
332 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
333 |     will_return(__wrap_dlopen, HANDLE);
334 | 
335 |     expect_value(__wrap_dlsym, handle, HANDLE);
360 |  /** Test for failure on tcti
361 |  * { "libtss2-tcti-default.so", NULL, "", "Access libtss2-tcti-default.so" }
362 |  */
363 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
364 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
365 |     will_return(__wrap_dlopen, HANDLE);
366 | 
367 |     expect_value(__wrap_dlsym, handle, HANDLE);
380 |     /** Now test
381 |      *{ "libtss2-tcti-tabrmd.so", NULL, "", "Access libtss2-tcti-tabrmd.so"},
382 |      */
383 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-tabrmd.so.0");
384 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
385 |     will_return(__wrap_dlopen, HANDLE);
386 | 
387 |     expect_value(__wrap_dlsym, handle, HANDLE);
403 | test_tcti_fail_all (void **state)
404 | {
405 |     /* skip over libtss2-tcti-default.so */
406 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
407 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
408 |     will_return(__wrap_dlopen, NULL);
409 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so.0");
410 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
411 |     will_return(__wrap_dlopen, NULL);
412 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so");
413 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
414 |     will_return(__wrap_dlopen, NULL);
415 | 
416 |     /* Skip over libtss2-tcti-tabrmd.so */
417 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-tabrmd.so.0");
418 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
419 |     will_return(__wrap_dlopen, NULL);
420 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-tabrmd.so.0.so.0");
421 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
422 |     will_return(__wrap_dlopen, NULL);
423 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-tabrmd.so.0.so");
424 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
425 |     will_return(__wrap_dlopen, NULL);
426 | 
427 |     /* Skip over libtss2-tcti-device.so, /dev/tpmrm0 */
428 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-device.so.0");
429 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
430 |     will_return(__wrap_dlopen, NULL);
431 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-device.so.0.so.0");
432 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
433 |     will_return(__wrap_dlopen, NULL);
434 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-device.so.0.so");
435 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
436 |     will_return(__wrap_dlopen, NULL);
437 | 
438 |     /* Skip over libtss2-tcti-device.so, /dev/tpm0 */
439 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-device.so.0");
440 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
441 |     will_return(__wrap_dlopen, NULL);
442 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-device.so.0.so.0");
443 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
444 |     will_return(__wrap_dlopen, NULL);
445 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-device.so.0.so");
446 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
447 |     will_return(__wrap_dlopen, NULL);
448 | 
449 |     /* Skip over libtss2-tcti-swtpm.so */
450 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-swtpm.so.0");
451 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
452 |     will_return(__wrap_dlopen, NULL);
453 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-swtpm.so.0.so.0");
454 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
455 |     will_return(__wrap_dlopen, NULL);
456 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-swtpm.so.0.so");
457 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
458 |     will_return(__wrap_dlopen, NULL);
459 | 
460 |     /* Skip over libtss2-tcti-mssim.so */
461 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-mssim.so.0");
462 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
463 |     will_return(__wrap_dlopen, NULL);
464 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-mssim.so.0.so.0");
465 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
466 |     will_return(__wrap_dlopen, NULL);
467 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-mssim.so.0.so");
468 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
469 |     will_return(__wrap_dlopen, NULL);
470 | 
471 |     TSS2_RC r;
486 |     const TSS2_TCTI_INFO *info;
487 |     void *data;
488 | 
489 |     expect_string(__wrap_dlopen, filename, "foo");
490 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
491 |     will_return(__wrap_dlopen, NULL);
492 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-foo.so.0");
493 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
494 |     will_return(__wrap_dlopen, NULL);
495 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-foo.so");
496 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
497 |     will_return(__wrap_dlopen, NULL);
498 | 
499 |     TSS2_RC rc = info_from_name ("foo", &info, &data);
505 |     const TSS2_TCTI_INFO *info = { 0, };
506 |     void *data = HANDLE;
507 | 
508 |     expect_string(__wrap_dlopen, filename, "foo");
509 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
510 |     will_return(__wrap_dlopen, HANDLE);
511 | 
512 |     expect_value(__wrap_dlsym, handle, HANDLE);
528 |     TSS2_TCTI_INFO info_instance = { 0, };
529 |     void *data;
530 | 
531 |     expect_string(__wrap_dlopen, filename, "foo");
532 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
533 |     will_return(__wrap_dlopen, HANDLE);
534 | 
535 |     expect_value(__wrap_dlsym, handle, HANDLE);
554 | {
555 |     TSS2_TCTI_CONTEXT *tcti;
556 | 
557 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
558 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
559 |     will_return(__wrap_dlopen, HANDLE);
560 | 
561 |     expect_value(__wrap_dlsym, handle, HANDLE);
577 | {
578 |     TSS2_TCTI_CONTEXT *tcti;
579 | 
580 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
581 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
582 |     will_return(__wrap_dlopen, HANDLE);
583 | 
584 |     expect_value(__wrap_dlsym, handle, HANDLE);
602 |     const TSS2_TCTI_INFO *info;
603 |     void *data;
604 | 
605 |     expect_string(__wrap_dlopen, filename, "foo");
606 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
607 |     will_return(__wrap_dlopen, NULL);
608 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-foo.so.0");
609 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
610 |     will_return(__wrap_dlopen, NULL);
611 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-foo.so");
612 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
613 |     will_return(__wrap_dlopen, NULL);
614 | 
615 |     TSS2_RC rc = tctildr_get_info ("foo", &info, &data);
621 |     const TSS2_TCTI_INFO *info;
622 |     void *data;
623 | 
624 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
625 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
626 |     will_return(__wrap_dlopen, HANDLE);
627 | 
628 |     expect_value(__wrap_dlsym, handle, HANDLE);
655 |         cmocka_unit_test(test_info_from_handle_dlsym_fail),
656 |         cmocka_unit_test(test_info_from_handle_success),
657 |         cmocka_unit_test(test_handle_from_name_null_handle),
658 |         cmocka_unit_test(test_handle_from_name_first_dlopen_success),
659 |         cmocka_unit_test(test_handle_from_name_second_dlopen_success),
660 |         cmocka_unit_test(test_handle_from_name_third_dlopen_success),
661 |         cmocka_unit_test(test_fail_null),
662 |         cmocka_unit_test(test_tcti_from_file_null_tcti),
{% endraw %}

```