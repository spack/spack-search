---
name: "tpm2-tss"
layout: package
next_package: trilinos
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
174 |     void *dlhandle;              /**< The handle of dlopen if the tcti was
{% endraw %}

```
### test/unit/tctildr-dl.c

```c

{% raw %}
38 | __wrap_dlopen(const char *filename, int flags)
140 | test_handle_from_name_first_dlopen_success (void **state)
145 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME);
146 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
147 |     will_return(__wrap_dlopen, TEST_HANDLE);
156 | test_handle_from_name_second_dlopen_success (void **state)
161 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME);
162 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
163 |     will_return(__wrap_dlopen, NULL);
165 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME_SO_0);
166 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
167 |     will_return(__wrap_dlopen, TEST_HANDLE);
175 | test_handle_from_name_third_dlopen_success (void **state)
180 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME);
181 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
182 |     will_return(__wrap_dlopen, NULL);
184 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME_SO_0);
185 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
186 |     will_return(__wrap_dlopen, NULL);
188 |     expect_string(__wrap_dlopen, filename, TEST_TCTI_NAME_SO);
189 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
190 |     will_return(__wrap_dlopen, TEST_HANDLE);
219 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
220 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
221 |     will_return(__wrap_dlopen, NULL);
223 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so.0");
224 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
225 |     will_return(__wrap_dlopen, NULL);
227 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so");
228 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
229 |     will_return(__wrap_dlopen, NULL);
231 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-tabrmd.so.0");
232 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
233 |     will_return(__wrap_dlopen, HANDLE);
251 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
252 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
253 |     will_return(__wrap_dlopen, NULL);
255 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so.0");
256 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
257 |     will_return(__wrap_dlopen, NULL);
259 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so");
260 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
261 |     will_return(__wrap_dlopen, NULL);
263 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-tabrmd.so.0");
264 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
265 |     will_return(__wrap_dlopen, HANDLE);
288 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
289 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
290 |     will_return(__wrap_dlopen, HANDLE);
317 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
318 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
319 |     will_return(__wrap_dlopen, HANDLE);
331 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-tabrmd.so.0");
332 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
333 |     will_return(__wrap_dlopen, HANDLE);
363 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
364 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
365 |     will_return(__wrap_dlopen, HANDLE);
383 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-tabrmd.so.0");
384 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
385 |     will_return(__wrap_dlopen, HANDLE);
406 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
407 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
408 |     will_return(__wrap_dlopen, NULL);
409 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so.0");
410 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
411 |     will_return(__wrap_dlopen, NULL);
412 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-default.so.so");
413 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
414 |     will_return(__wrap_dlopen, NULL);
417 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-tabrmd.so.0");
418 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
419 |     will_return(__wrap_dlopen, NULL);
420 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-tabrmd.so.0.so.0");
421 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
422 |     will_return(__wrap_dlopen, NULL);
423 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-tabrmd.so.0.so");
424 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
425 |     will_return(__wrap_dlopen, NULL);
428 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-device.so.0");
429 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
430 |     will_return(__wrap_dlopen, NULL);
431 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-device.so.0.so.0");
432 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
433 |     will_return(__wrap_dlopen, NULL);
434 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-device.so.0.so");
435 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
436 |     will_return(__wrap_dlopen, NULL);
439 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-device.so.0");
440 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
441 |     will_return(__wrap_dlopen, NULL);
442 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-device.so.0.so.0");
443 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
444 |     will_return(__wrap_dlopen, NULL);
445 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-device.so.0.so");
446 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
447 |     will_return(__wrap_dlopen, NULL);
450 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-swtpm.so.0");
451 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
452 |     will_return(__wrap_dlopen, NULL);
453 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-swtpm.so.0.so.0");
454 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
455 |     will_return(__wrap_dlopen, NULL);
456 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-swtpm.so.0.so");
457 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
458 |     will_return(__wrap_dlopen, NULL);
461 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-mssim.so.0");
462 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
463 |     will_return(__wrap_dlopen, NULL);
464 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-mssim.so.0.so.0");
465 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
466 |     will_return(__wrap_dlopen, NULL);
467 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-libtss2-tcti-mssim.so.0.so");
468 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
469 |     will_return(__wrap_dlopen, NULL);
489 |     expect_string(__wrap_dlopen, filename, "foo");
490 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
491 |     will_return(__wrap_dlopen, NULL);
492 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-foo.so.0");
493 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
494 |     will_return(__wrap_dlopen, NULL);
495 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-foo.so");
496 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
497 |     will_return(__wrap_dlopen, NULL);
508 |     expect_string(__wrap_dlopen, filename, "foo");
509 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
510 |     will_return(__wrap_dlopen, HANDLE);
531 |     expect_string(__wrap_dlopen, filename, "foo");
532 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
533 |     will_return(__wrap_dlopen, HANDLE);
557 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
558 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
559 |     will_return(__wrap_dlopen, HANDLE);
580 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
581 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
582 |     will_return(__wrap_dlopen, HANDLE);
605 |     expect_string(__wrap_dlopen, filename, "foo");
606 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
607 |     will_return(__wrap_dlopen, NULL);
608 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-foo.so.0");
609 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
610 |     will_return(__wrap_dlopen, NULL);
611 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-foo.so");
612 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
613 |     will_return(__wrap_dlopen, NULL);
624 |     expect_string(__wrap_dlopen, filename, "libtss2-tcti-default.so");
625 |     expect_value(__wrap_dlopen, flags, RTLD_NOW);
626 |     will_return(__wrap_dlopen, HANDLE);
658 |         cmocka_unit_test(test_handle_from_name_first_dlopen_success),
659 |         cmocka_unit_test(test_handle_from_name_second_dlopen_success),
660 |         cmocka_unit_test(test_handle_from_name_third_dlopen_success),
{% endraw %}

```