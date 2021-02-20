---
name: "tau"
layout: package
next_package: tcl
previous_package: taskflow
languages: ['c']
---
## 2.29.1
19 / 3452 files match, 5 filtered matches.

 - [src/wrappers/pthread/pthread_wrap.c](#srcwrapperspthreadpthread_wrapc)
 - [src/wrappers/gomp/gomp_wrap.c](#srcwrappersgompgomp_wrapc)
 - [src/wrappers/cuda/cuda_wrap.c](#srcwrapperscudacuda_wrapc)
 - [src/Profile/TauShmemSgiF.c](#srcprofiletaushmemsgifc)
 - [apex/src/wrappers/pthread_wrapper.c](#apexsrcwrapperspthread_wrapperc)

### src/wrappers/pthread/pthread_wrap.c

```c

{% raw %}
83 |   // #defines in Profiler.h, -Wl,-wrap on the link line, and LD_PRELOAD.
84 |   if (handle == caller) {
85 |     RESET_DLERROR();
86 |     void * syms = dlopen(NULL, RTLD_NOW);
87 |     CHECK_DLERROR();
88 |     do {
{% endraw %}

```
### src/wrappers/gomp/gomp_wrap.c

```c

{% raw %}
45 |     // #defines in Profiler.h, -Wl,-wrap on the link line, and LD_PRELOAD.
46 |     if (handle == caller) {
47 |         RESET_DLERROR();
48 |         void * syms = dlopen(NULL, RTLD_NOW);
49 |         CHECK_DLERROR();
50 |         do {
{% endraw %}

```
### src/wrappers/cuda/cuda_wrap.c

```c

{% raw %}
18 |   CUresult retval;
19 |   TAU_PROFILE_TIMER(t,"CUresult cuInit(unsigned int) C", "", CUDA_API);
20 |   if (tau_handle == NULL) 
21 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
22 | 
23 |   if (tau_handle == NULL) { 
24 |     perror("Error opening library in dlopen call"); 
25 |     return retval;
26 |   } 
28 |     if (cuInit_h == NULL)
29 | 	cuInit_h = (cuInit_p_h) dlsym(tau_handle,"cuInit"); 
30 |     if (cuInit_h == NULL) {
31 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
32 |       return retval;
33 |     }
46 |   CUresult retval;
47 |   TAU_PROFILE_TIMER(t,"CUresult cuDriverGetVersion(int *) C", "", CUDA_API);
48 |   if (tau_handle == NULL) 
49 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
50 | 
51 |   if (tau_handle == NULL) { 
52 |     perror("Error opening library in dlopen call"); 
53 |     return retval;
54 |   } 
56 |     if (cuDriverGetVersion_h == NULL)
57 | 	cuDriverGetVersion_h = (cuDriverGetVersion_p_h) dlsym(tau_handle,"cuDriverGetVersion"); 
58 |     if (cuDriverGetVersion_h == NULL) {
59 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
60 |       return retval;
61 |     }
74 |   CUresult retval;
75 |   TAU_PROFILE_TIMER(t,"CUresult cuDeviceGet(CUdevice *, int) C", "", CUDA_API);
76 |   if (tau_handle == NULL) 
77 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
78 | 
79 |   if (tau_handle == NULL) { 
80 |     perror("Error opening library in dlopen call"); 
81 |     return retval;
82 |   } 
84 |     if (cuDeviceGet_h == NULL)
85 | 	cuDeviceGet_h = (cuDeviceGet_p_h) dlsym(tau_handle,"cuDeviceGet"); 
86 |     if (cuDeviceGet_h == NULL) {
87 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
88 |       return retval;
89 |     }
102 |   CUresult retval;
103 |   TAU_PROFILE_TIMER(t,"CUresult cuDeviceGetCount(int *) C", "", CUDA_API);
104 |   if (tau_handle == NULL) 
105 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
106 | 
107 |   if (tau_handle == NULL) { 
108 |     perror("Error opening library in dlopen call"); 
109 |     return retval;
110 |   } 
112 |     if (cuDeviceGetCount_h == NULL)
113 | 	cuDeviceGetCount_h = (cuDeviceGetCount_p_h) dlsym(tau_handle,"cuDeviceGetCount"); 
114 |     if (cuDeviceGetCount_h == NULL) {
115 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
116 |       return retval;
117 |     }
130 |   CUresult retval;
131 |   TAU_PROFILE_TIMER(t,"CUresult cuDeviceGetName(char *, int, CUdevice) C", "", CUDA_API);
132 |   if (tau_handle == NULL) 
133 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
134 | 
135 |   if (tau_handle == NULL) { 
136 |     perror("Error opening library in dlopen call"); 
137 |     return retval;
138 |   } 
140 |     if (cuDeviceGetName_h == NULL)
141 | 	cuDeviceGetName_h = (cuDeviceGetName_p_h) dlsym(tau_handle,"cuDeviceGetName"); 
142 |     if (cuDeviceGetName_h == NULL) {
143 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
144 |       return retval;
145 |     }
158 |   CUresult retval;
159 |   TAU_PROFILE_TIMER(t,"CUresult cuDeviceComputeCapability(int *, int *, CUdevice) C", "", CUDA_API);
160 |   if (tau_handle == NULL) 
161 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
162 | 
163 |   if (tau_handle == NULL) { 
164 |     perror("Error opening library in dlopen call"); 
165 |     return retval;
166 |   } 
168 |     if (cuDeviceComputeCapability_h == NULL)
169 | 	cuDeviceComputeCapability_h = (cuDeviceComputeCapability_p_h) dlsym(tau_handle,"cuDeviceComputeCapability"); 
170 |     if (cuDeviceComputeCapability_h == NULL) {
171 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
172 |       return retval;
173 |     }
186 |   CUresult retval;
187 |   TAU_PROFILE_TIMER(t,"CUresult cuDeviceTotalMem_v2(size_t *, CUdevice) C", "", CUDA_API);
188 |   if (tau_handle == NULL) 
189 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
190 | 
191 |   if (tau_handle == NULL) { 
192 |     perror("Error opening library in dlopen call"); 
193 |     return retval;
194 |   } 
196 |     if (cuDeviceTotalMem_v2_h == NULL)
197 | 	cuDeviceTotalMem_v2_h = (cuDeviceTotalMem_v2_p_h) dlsym(tau_handle,"cuDeviceTotalMem_v2"); 
198 |     if (cuDeviceTotalMem_v2_h == NULL) {
199 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
200 |       return retval;
201 |     }
214 |   CUresult retval;
215 |   TAU_PROFILE_TIMER(t,"CUresult cuDeviceGetProperties(CUdevprop *, CUdevice) C", "", CUDA_API);
216 |   if (tau_handle == NULL) 
217 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
218 | 
219 |   if (tau_handle == NULL) { 
220 |     perror("Error opening library in dlopen call"); 
221 |     return retval;
222 |   } 
224 |     if (cuDeviceGetProperties_h == NULL)
225 | 	cuDeviceGetProperties_h = (cuDeviceGetProperties_p_h) dlsym(tau_handle,"cuDeviceGetProperties"); 
226 |     if (cuDeviceGetProperties_h == NULL) {
227 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
228 |       return retval;
229 |     }
242 |   CUresult retval;
243 |   TAU_PROFILE_TIMER(t,"CUresult cuDeviceGetAttribute(int *, CUdevice_attribute, CUdevice) C", "", CUDA_API);
244 |   if (tau_handle == NULL) 
245 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
246 | 
247 |   if (tau_handle == NULL) { 
248 |     perror("Error opening library in dlopen call"); 
249 |     return retval;
250 |   } 
252 |     if (cuDeviceGetAttribute_h == NULL)
253 | 	cuDeviceGetAttribute_h = (cuDeviceGetAttribute_p_h) dlsym(tau_handle,"cuDeviceGetAttribute"); 
254 |     if (cuDeviceGetAttribute_h == NULL) {
255 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
256 |       return retval;
257 |     }
270 |   CUresult retval;
271 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxCreate_v2(CUcontext *, unsigned int, CUdevice) C", "", CUDA_API);
272 |   if (tau_handle == NULL) 
273 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
274 | 
275 |   if (tau_handle == NULL) { 
276 |     perror("Error opening library in dlopen call"); 
277 |     return retval;
278 |   } 
280 |     if (cuCtxCreate_v2_h == NULL)
281 | 	cuCtxCreate_v2_h = (cuCtxCreate_v2_p_h) dlsym(tau_handle,"cuCtxCreate_v2"); 
282 |     if (cuCtxCreate_v2_h == NULL) {
283 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
284 |       return retval;
285 |     }
298 |   CUresult retval;
299 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxDestroy(CUcontext) C", "", CUDA_API);
300 |   if (tau_handle == NULL) 
301 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
302 | 
303 |   if (tau_handle == NULL) { 
304 |     perror("Error opening library in dlopen call"); 
305 |     return retval;
306 |   } 
308 |     if (cuCtxDestroy_h == NULL)
309 | 	cuCtxDestroy_h = (cuCtxDestroy_p_h) dlsym(tau_handle,"cuCtxDestroy"); 
310 |     if (cuCtxDestroy_h == NULL) {
311 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
312 |       return retval;
313 |     }
326 |   CUresult retval;
327 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxAttach(CUcontext *, unsigned int) C", "", CUDA_API);
328 |   if (tau_handle == NULL) 
329 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
330 | 
331 |   if (tau_handle == NULL) { 
332 |     perror("Error opening library in dlopen call"); 
333 |     return retval;
334 |   } 
336 |     if (cuCtxAttach_h == NULL)
337 | 	cuCtxAttach_h = (cuCtxAttach_p_h) dlsym(tau_handle,"cuCtxAttach"); 
338 |     if (cuCtxAttach_h == NULL) {
339 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
340 |       return retval;
341 |     }
354 |   CUresult retval;
355 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxDetach(CUcontext) C", "", CUDA_SYNC);
356 |   if (tau_handle == NULL) 
357 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
358 | 
359 |   if (tau_handle == NULL) { 
360 |     perror("Error opening library in dlopen call"); 
361 |     return retval;
362 |   } 
364 |     if (cuCtxDetach_h == NULL)
365 | 	cuCtxDetach_h = (cuCtxDetach_p_h) dlsym(tau_handle,"cuCtxDetach"); 
366 |     if (cuCtxDetach_h == NULL) {
367 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
368 |       return retval;
369 |     }
387 |   CUresult retval;
388 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxPushCurrent(CUcontext) C", "", CUDA_API);
389 |   if (tau_handle == NULL) 
390 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
391 | 
392 |   if (tau_handle == NULL) { 
393 |     perror("Error opening library in dlopen call"); 
394 |     return retval;
395 |   } 
397 |     if (cuCtxPushCurrent_h == NULL)
398 | 	cuCtxPushCurrent_h = (cuCtxPushCurrent_p_h) dlsym(tau_handle,"cuCtxPushCurrent"); 
399 |     if (cuCtxPushCurrent_h == NULL) {
400 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
401 |       return retval;
402 |     }
415 |   CUresult retval;
416 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxPopCurrent(CUcontext *) C", "", CUDA_API);
417 |   if (tau_handle == NULL) 
418 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
419 | 
420 |   if (tau_handle == NULL) { 
421 |     perror("Error opening library in dlopen call"); 
422 |     return retval;
423 |   } 
425 |     if (cuCtxPopCurrent_h == NULL)
426 | 	cuCtxPopCurrent_h = (cuCtxPopCurrent_p_h) dlsym(tau_handle,"cuCtxPopCurrent"); 
427 |     if (cuCtxPopCurrent_h == NULL) {
428 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
429 |       return retval;
430 |     }
443 |   CUresult retval;
444 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxGetDevice(CUdevice *) C", "", CUDA_API);
445 |   if (tau_handle == NULL) 
446 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
447 | 
448 |   if (tau_handle == NULL) { 
449 |     perror("Error opening library in dlopen call"); 
450 |     return retval;
451 |   } 
453 |     if (cuCtxGetDevice_h == NULL)
454 | 	cuCtxGetDevice_h = (cuCtxGetDevice_p_h) dlsym(tau_handle,"cuCtxGetDevice"); 
455 |     if (cuCtxGetDevice_h == NULL) {
456 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
457 |       return retval;
458 |     }
471 |   CUresult retval;
472 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxSynchronize(void) C", "", CUDA_SYNC);
473 |   if (tau_handle == NULL) 
474 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
475 | 
476 |   if (tau_handle == NULL) { 
477 |     perror("Error opening library in dlopen call"); 
478 |     return retval;
479 |   } 
481 |     if (cuCtxSynchronize_h == NULL)
482 | 	cuCtxSynchronize_h = (cuCtxSynchronize_p_h) dlsym(tau_handle,"cuCtxSynchronize"); 
483 |     if (cuCtxSynchronize_h == NULL) {
484 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
485 |       return retval;
486 |     }
502 |   CUresult retval;
503 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxSetLimit(CUlimit, size_t) C", "", CUDA_API);
504 |   if (tau_handle == NULL) 
505 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
506 | 
507 |   if (tau_handle == NULL) { 
508 |     perror("Error opening library in dlopen call"); 
509 |     return retval;
510 |   } 
512 |     if (cuCtxSetLimit_h == NULL)
513 | 	cuCtxSetLimit_h = (cuCtxSetLimit_p_h) dlsym(tau_handle,"cuCtxSetLimit"); 
514 |     if (cuCtxSetLimit_h == NULL) {
515 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
516 |       return retval;
517 |     }
530 |   CUresult retval;
531 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxGetLimit(size_t *, CUlimit) C", "", CUDA_API);
532 |   if (tau_handle == NULL) 
533 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
534 | 
535 |   if (tau_handle == NULL) { 
536 |     perror("Error opening library in dlopen call"); 
537 |     return retval;
538 |   } 
540 |     if (cuCtxGetLimit_h == NULL)
541 | 	cuCtxGetLimit_h = (cuCtxGetLimit_p_h) dlsym(tau_handle,"cuCtxGetLimit"); 
542 |     if (cuCtxGetLimit_h == NULL) {
543 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
544 |       return retval;
545 |     }
558 |   CUresult retval;
559 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxGetCacheConfig(CUfunc_cache *) C", "", CUDA_API);
560 |   if (tau_handle == NULL) 
561 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
562 | 
563 |   if (tau_handle == NULL) { 
564 |     perror("Error opening library in dlopen call"); 
565 |     return retval;
566 |   } 
568 |     if (cuCtxGetCacheConfig_h == NULL)
569 | 	cuCtxGetCacheConfig_h = (cuCtxGetCacheConfig_p_h) dlsym(tau_handle,"cuCtxGetCacheConfig"); 
570 |     if (cuCtxGetCacheConfig_h == NULL) {
571 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
572 |       return retval;
573 |     }
586 |   CUresult retval;
587 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxSetCacheConfig(CUfunc_cache) C", "", CUDA_API);
588 |   if (tau_handle == NULL) 
589 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
590 | 
591 |   if (tau_handle == NULL) { 
592 |     perror("Error opening library in dlopen call"); 
593 |     return retval;
594 |   } 
596 |     if (cuCtxSetCacheConfig_h == NULL)
597 | 	cuCtxSetCacheConfig_h = (cuCtxSetCacheConfig_p_h) dlsym(tau_handle,"cuCtxSetCacheConfig"); 
598 |     if (cuCtxSetCacheConfig_h == NULL) {
599 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
600 |       return retval;
601 |     }
614 |   CUresult retval;
615 |   TAU_PROFILE_TIMER(t,"CUresult cuCtxGetApiVersion(CUcontext, unsigned int *) C", "", CUDA_API);
616 |   if (tau_handle == NULL) 
617 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
618 | 
619 |   if (tau_handle == NULL) { 
620 |     perror("Error opening library in dlopen call"); 
621 |     return retval;
622 |   } 
624 |     if (cuCtxGetApiVersion_h == NULL)
625 | 	cuCtxGetApiVersion_h = (cuCtxGetApiVersion_p_h) dlsym(tau_handle,"cuCtxGetApiVersion"); 
626 |     if (cuCtxGetApiVersion_h == NULL) {
627 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
628 |       return retval;
629 |     }
642 |   CUresult retval;
643 |   TAU_PROFILE_TIMER(t,"CUresult cuModuleLoad(CUmodule *, const char *) C", "", CUDA_API);
644 |   if (tau_handle == NULL) 
645 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
646 | 
647 |   if (tau_handle == NULL) { 
648 |     perror("Error opening library in dlopen call"); 
649 |     return retval;
650 |   } 
652 |     if (cuModuleLoad_h == NULL)
653 | 	cuModuleLoad_h = (cuModuleLoad_p_h) dlsym(tau_handle,"cuModuleLoad"); 
654 |     if (cuModuleLoad_h == NULL) {
655 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
656 |       return retval;
657 |     }
670 |   CUresult retval;
671 |   TAU_PROFILE_TIMER(t,"CUresult cuModuleLoadData(CUmodule *, const void *) C", "", CUDA_API);
672 |   if (tau_handle == NULL) 
673 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
674 | 
675 |   if (tau_handle == NULL) { 
676 |     perror("Error opening library in dlopen call"); 
677 |     return retval;
678 |   } 
680 |     if (cuModuleLoadData_h == NULL)
681 | 	cuModuleLoadData_h = (cuModuleLoadData_p_h) dlsym(tau_handle,"cuModuleLoadData"); 
682 |     if (cuModuleLoadData_h == NULL) {
683 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
684 |       return retval;
685 |     }
698 |   CUresult retval;
699 |   TAU_PROFILE_TIMER(t,"CUresult cuModuleLoadDataEx(CUmodule *, const void *, unsigned int, CUjit_option *, void **) C", "", CUDA_API);
700 |   if (tau_handle == NULL) 
701 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
702 | 
703 |   if (tau_handle == NULL) { 
704 |     perror("Error opening library in dlopen call"); 
705 |     return retval;
706 |   } 
708 |     if (cuModuleLoadDataEx_h == NULL)
709 | 	cuModuleLoadDataEx_h = (cuModuleLoadDataEx_p_h) dlsym(tau_handle,"cuModuleLoadDataEx"); 
710 |     if (cuModuleLoadDataEx_h == NULL) {
711 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
712 |       return retval;
713 |     }
726 |   CUresult retval;
727 |   TAU_PROFILE_TIMER(t,"CUresult cuModuleLoadFatBinary(CUmodule *, const void *) C", "", CUDA_API);
728 |   if (tau_handle == NULL) 
729 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
730 | 
731 |   if (tau_handle == NULL) { 
732 |     perror("Error opening library in dlopen call"); 
733 |     return retval;
734 |   } 
736 |     if (cuModuleLoadFatBinary_h == NULL)
737 | 	cuModuleLoadFatBinary_h = (cuModuleLoadFatBinary_p_h) dlsym(tau_handle,"cuModuleLoadFatBinary"); 
738 |     if (cuModuleLoadFatBinary_h == NULL) {
739 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
740 |       return retval;
741 |     }
754 |   CUresult retval;
755 |   TAU_PROFILE_TIMER(t,"CUresult cuModuleUnload(CUmodule) C", "", CUDA_API);
756 |   if (tau_handle == NULL) 
757 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
758 | 
759 |   if (tau_handle == NULL) { 
760 |     perror("Error opening library in dlopen call"); 
761 |     return retval;
762 |   } 
764 |     if (cuModuleUnload_h == NULL)
765 | 	cuModuleUnload_h = (cuModuleUnload_p_h) dlsym(tau_handle,"cuModuleUnload"); 
766 |     if (cuModuleUnload_h == NULL) {
767 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
768 |       return retval;
769 |     }
782 |   CUresult retval;
783 |   TAU_PROFILE_TIMER(t,"CUresult cuModuleGetFunction(CUfunction *, CUmodule, const char *) C", "", CUDA_API);
784 |   if (tau_handle == NULL) 
785 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
786 | 
787 |   if (tau_handle == NULL) { 
788 |     perror("Error opening library in dlopen call"); 
789 |     return retval;
790 |   } 
792 |     if (cuModuleGetFunction_h == NULL)
793 | 	cuModuleGetFunction_h = (cuModuleGetFunction_p_h) dlsym(tau_handle,"cuModuleGetFunction"); 
794 |     if (cuModuleGetFunction_h == NULL) {
795 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
796 |       return retval;
797 |     }
810 |   CUresult retval;
811 |   TAU_PROFILE_TIMER(t,"CUresult cuModuleGetGlobal_v2(CUdeviceptr *, size_t *, CUmodule, const char *) C", "", CUDA_API);
812 |   if (tau_handle == NULL) 
813 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
814 | 
815 |   if (tau_handle == NULL) { 
816 |     perror("Error opening library in dlopen call"); 
817 |     return retval;
818 |   } 
820 |     if (cuModuleGetGlobal_v2_h == NULL)
821 | 	cuModuleGetGlobal_v2_h = (cuModuleGetGlobal_v2_p_h) dlsym(tau_handle,"cuModuleGetGlobal_v2"); 
822 |     if (cuModuleGetGlobal_v2_h == NULL) {
823 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
824 |       return retval;
825 |     }
838 |   CUresult retval;
839 |   TAU_PROFILE_TIMER(t,"CUresult cuModuleGetTexRef(CUtexref *, CUmodule, const char *) C", "", CUDA_API);
840 |   if (tau_handle == NULL) 
841 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
842 | 
843 |   if (tau_handle == NULL) { 
844 |     perror("Error opening library in dlopen call"); 
845 |     return retval;
846 |   } 
848 |     if (cuModuleGetTexRef_h == NULL)
849 | 	cuModuleGetTexRef_h = (cuModuleGetTexRef_p_h) dlsym(tau_handle,"cuModuleGetTexRef"); 
850 |     if (cuModuleGetTexRef_h == NULL) {
851 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
852 |       return retval;
853 |     }
866 |   CUresult retval;
867 |   TAU_PROFILE_TIMER(t,"CUresult cuModuleGetSurfRef(CUsurfref *, CUmodule, const char *) C", "", CUDA_API);
868 |   if (tau_handle == NULL) 
869 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
870 | 
871 |   if (tau_handle == NULL) { 
872 |     perror("Error opening library in dlopen call"); 
873 |     return retval;
874 |   } 
876 |     if (cuModuleGetSurfRef_h == NULL)
877 | 	cuModuleGetSurfRef_h = (cuModuleGetSurfRef_p_h) dlsym(tau_handle,"cuModuleGetSurfRef"); 
878 |     if (cuModuleGetSurfRef_h == NULL) {
879 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
880 |       return retval;
881 |     }
894 |   CUresult retval;
895 |   TAU_PROFILE_TIMER(t,"CUresult cuMemGetInfo_v2(size_t *, size_t *) C", "", CUDA_API);
896 |   if (tau_handle == NULL) 
897 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
898 | 
899 |   if (tau_handle == NULL) { 
900 |     perror("Error opening library in dlopen call"); 
901 |     return retval;
902 |   } 
904 |     if (cuMemGetInfo_v2_h == NULL)
905 | 	cuMemGetInfo_v2_h = (cuMemGetInfo_v2_p_h) dlsym(tau_handle,"cuMemGetInfo_v2"); 
906 |     if (cuMemGetInfo_v2_h == NULL) {
907 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
908 |       return retval;
909 |     }
922 |   CUresult retval;
923 |   TAU_PROFILE_TIMER(t,"CUresult cuMemAllocManaged(CUdeviceptr *, size_t, unsigned int) C", "", CUDA_API);
924 |   if (tau_handle == NULL) 
925 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
926 | 
927 |   if (tau_handle == NULL) { 
928 |     perror("Error opening library in dlopen call"); 
929 |     return retval;
930 |   } 
932 |     if (cuMemAllocManaged_h == NULL)
933 | 	cuMemAllocManaged_h = (cuMemAllocManaged_p_h) dlsym(tau_handle,"cuMemAllocManaged"); 
934 |     if (cuMemAllocManaged_h == NULL) {
935 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
936 |       return retval;
937 |     }
950 |   CUresult retval;
951 |   TAU_PROFILE_TIMER(t,"CUresult cuMemAlloc_v2(CUdeviceptr *, size_t) C", "", CUDA_API);
952 |   if (tau_handle == NULL) 
953 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
954 | 
955 |   if (tau_handle == NULL) { 
956 |     perror("Error opening library in dlopen call"); 
957 |     return retval;
958 |   } 
960 |     if (cuMemAlloc_v2_h == NULL)
961 | 	cuMemAlloc_v2_h = (cuMemAlloc_v2_p_h) dlsym(tau_handle,"cuMemAlloc_v2"); 
962 |     if (cuMemAlloc_v2_h == NULL) {
963 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
964 |       return retval;
965 |     }
978 |   CUresult retval;
979 |   TAU_PROFILE_TIMER(t,"CUresult cuMemAllocPitch_v2(CUdeviceptr *, size_t *, size_t, size_t, unsigned int) C", "", CUDA_API);
980 |   if (tau_handle == NULL) 
981 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
982 | 
983 |   if (tau_handle == NULL) { 
984 |     perror("Error opening library in dlopen call"); 
985 |     return retval;
986 |   } 
988 |     if (cuMemAllocPitch_v2_h == NULL)
989 | 	cuMemAllocPitch_v2_h = (cuMemAllocPitch_v2_p_h) dlsym(tau_handle,"cuMemAllocPitch_v2"); 
990 |     if (cuMemAllocPitch_v2_h == NULL) {
991 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
992 |       return retval;
993 |     }
1006 |   CUresult retval;
1007 |   TAU_PROFILE_TIMER(t,"CUresult cuMemFree_v2(CUdeviceptr) C", "", CUDA_API);
1008 |   if (tau_handle == NULL) 
1009 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1010 | 
1011 |   if (tau_handle == NULL) { 
1012 |     perror("Error opening library in dlopen call"); 
1013 |     return retval;
1014 |   } 
1016 |     if (cuMemFree_v2_h == NULL)
1017 | 	cuMemFree_v2_h = (cuMemFree_v2_p_h) dlsym(tau_handle,"cuMemFree_v2"); 
1018 |     if (cuMemFree_v2_h == NULL) {
1019 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1020 |       return retval;
1021 |     }
1034 |   CUresult retval;
1035 |   TAU_PROFILE_TIMER(t,"CUresult cuMemGetAddressRange_v2(CUdeviceptr *, size_t *, CUdeviceptr) C", "", CUDA_API);
1036 |   if (tau_handle == NULL) 
1037 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1038 | 
1039 |   if (tau_handle == NULL) { 
1040 |     perror("Error opening library in dlopen call"); 
1041 |     return retval;
1042 |   } 
1044 |     if (cuMemGetAddressRange_v2_h == NULL)
1045 | 	cuMemGetAddressRange_v2_h = (cuMemGetAddressRange_v2_p_h) dlsym(tau_handle,"cuMemGetAddressRange_v2"); 
1046 |     if (cuMemGetAddressRange_v2_h == NULL) {
1047 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1048 |       return retval;
1049 |     }
1062 |   CUresult retval;
1063 |   TAU_PROFILE_TIMER(t,"CUresult cuMemAllocHost_v2(void **, size_t) C", "", CUDA_API);
1064 |   if (tau_handle == NULL) 
1065 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1066 | 
1067 |   if (tau_handle == NULL) { 
1068 |     perror("Error opening library in dlopen call"); 
1069 |     return retval;
1070 |   } 
1072 |     if (cuMemAllocHost_v2_h == NULL)
1073 | 	cuMemAllocHost_v2_h = (cuMemAllocHost_v2_p_h) dlsym(tau_handle,"cuMemAllocHost_v2"); 
1074 |     if (cuMemAllocHost_v2_h == NULL) {
1075 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1076 |       return retval;
1077 |     }
1090 |   CUresult retval;
1091 |   TAU_PROFILE_TIMER(t,"CUresult cuMemFreeHost(void *) C", "", CUDA_API);
1092 |   if (tau_handle == NULL) 
1093 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1094 | 
1095 |   if (tau_handle == NULL) { 
1096 |     perror("Error opening library in dlopen call"); 
1097 |     return retval;
1098 |   } 
1100 |     if (cuMemFreeHost_h == NULL)
1101 | 	cuMemFreeHost_h = (cuMemFreeHost_p_h) dlsym(tau_handle,"cuMemFreeHost"); 
1102 |     if (cuMemFreeHost_h == NULL) {
1103 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1104 |       return retval;
1105 |     }
1118 |   CUresult retval;
1119 |   TAU_PROFILE_TIMER(t,"CUresult cuMemHostAlloc(void **, size_t, unsigned int) C", "", CUDA_API);
1120 |   if (tau_handle == NULL) 
1121 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1122 | 
1123 |   if (tau_handle == NULL) { 
1124 |     perror("Error opening library in dlopen call"); 
1125 |     return retval;
1126 |   } 
1128 |     if (cuMemHostAlloc_h == NULL)
1129 | 	cuMemHostAlloc_h = (cuMemHostAlloc_p_h) dlsym(tau_handle,"cuMemHostAlloc"); 
1130 |     if (cuMemHostAlloc_h == NULL) {
1131 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1132 |       return retval;
1133 |     }
1146 |   CUresult retval;
1147 |   TAU_PROFILE_TIMER(t,"CUresult cuMemHostGetDevicePointer_v2(CUdeviceptr *, void *, unsigned int) C", "", CUDA_API);
1148 |   if (tau_handle == NULL) 
1149 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1150 | 
1151 |   if (tau_handle == NULL) { 
1152 |     perror("Error opening library in dlopen call"); 
1153 |     return retval;
1154 |   } 
1156 |     if (cuMemHostGetDevicePointer_v2_h == NULL)
1157 | 	cuMemHostGetDevicePointer_v2_h = (cuMemHostGetDevicePointer_v2_p_h) dlsym(tau_handle,"cuMemHostGetDevicePointer_v2"); 
1158 |     if (cuMemHostGetDevicePointer_v2_h == NULL) {
1159 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1160 |       return retval;
1161 |     }
1174 |   CUresult retval;
1175 |   TAU_PROFILE_TIMER(t,"CUresult cuMemHostGetFlags(unsigned int *, void *) C", "", CUDA_API);
1176 |   if (tau_handle == NULL) 
1177 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1178 | 
1179 |   if (tau_handle == NULL) { 
1180 |     perror("Error opening library in dlopen call"); 
1181 |     return retval;
1182 |   } 
1184 |     if (cuMemHostGetFlags_h == NULL)
1185 | 	cuMemHostGetFlags_h = (cuMemHostGetFlags_p_h) dlsym(tau_handle,"cuMemHostGetFlags"); 
1186 |     if (cuMemHostGetFlags_h == NULL) {
1187 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1188 |       return retval;
1189 |     }
1202 |   CUresult retval;
1203 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyHtoD_v2(CUdeviceptr, const void *, size_t) C", "", CUDA_API);
1204 |   if (tau_handle == NULL) 
1205 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1206 | 
1207 |   if (tau_handle == NULL) { 
1208 |     perror("Error opening library in dlopen call"); 
1209 |     return retval;
1210 |   } 
1212 |     if (cuMemcpyHtoD_v2_h == NULL)
1213 | 	cuMemcpyHtoD_v2_h = (cuMemcpyHtoD_v2_p_h) dlsym(tau_handle,"cuMemcpyHtoD_v2"); 
1214 |     if (cuMemcpyHtoD_v2_h == NULL) {
1215 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1216 |       return retval;
1217 |     }
1230 |   CUresult retval;
1231 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyDtoH_v2(void *, CUdeviceptr, size_t) C", "", CUDA_API);
1232 |   if (tau_handle == NULL) 
1233 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1234 | 
1235 |   if (tau_handle == NULL) { 
1236 |     perror("Error opening library in dlopen call"); 
1237 |     return retval;
1238 |   } 
1240 |     if (cuMemcpyDtoH_v2_h == NULL)
1241 | 	cuMemcpyDtoH_v2_h = (cuMemcpyDtoH_v2_p_h) dlsym(tau_handle,"cuMemcpyDtoH_v2"); 
1242 |     if (cuMemcpyDtoH_v2_h == NULL) {
1243 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1244 |       return retval;
1245 |     }
1258 |   CUresult retval;
1259 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyDtoD_v2(CUdeviceptr, CUdeviceptr, size_t) C", "", CUDA_API);
1260 |   if (tau_handle == NULL) 
1261 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1262 | 
1263 |   if (tau_handle == NULL) { 
1264 |     perror("Error opening library in dlopen call"); 
1265 |     return retval;
1266 |   } 
1268 |     if (cuMemcpyDtoD_v2_h == NULL)
1269 | 	cuMemcpyDtoD_v2_h = (cuMemcpyDtoD_v2_p_h) dlsym(tau_handle,"cuMemcpyDtoD_v2"); 
1270 |     if (cuMemcpyDtoD_v2_h == NULL) {
1271 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1272 |       return retval;
1273 |     }
1286 |   CUresult retval;
1287 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyDtoA_v2(CUarray, size_t, CUdeviceptr, size_t) C", "", CUDA_API);
1288 |   if (tau_handle == NULL) 
1289 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1290 | 
1291 |   if (tau_handle == NULL) { 
1292 |     perror("Error opening library in dlopen call"); 
1293 |     return retval;
1294 |   } 
1296 |     if (cuMemcpyDtoA_v2_h == NULL)
1297 | 	cuMemcpyDtoA_v2_h = (cuMemcpyDtoA_v2_p_h) dlsym(tau_handle,"cuMemcpyDtoA_v2"); 
1298 |     if (cuMemcpyDtoA_v2_h == NULL) {
1299 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1300 |       return retval;
1301 |     }
1314 |   CUresult retval;
1315 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyAtoD_v2(CUdeviceptr, CUarray, size_t, size_t) C", "", CUDA_API);
1316 |   if (tau_handle == NULL) 
1317 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1318 | 
1319 |   if (tau_handle == NULL) { 
1320 |     perror("Error opening library in dlopen call"); 
1321 |     return retval;
1322 |   } 
1324 |     if (cuMemcpyAtoD_v2_h == NULL)
1325 | 	cuMemcpyAtoD_v2_h = (cuMemcpyAtoD_v2_p_h) dlsym(tau_handle,"cuMemcpyAtoD_v2"); 
1326 |     if (cuMemcpyAtoD_v2_h == NULL) {
1327 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1328 |       return retval;
1329 |     }
1342 |   CUresult retval;
1343 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyHtoA_v2(CUarray, size_t, const void *, size_t) C", "", CUDA_API);
1344 |   if (tau_handle == NULL) 
1345 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1346 | 
1347 |   if (tau_handle == NULL) { 
1348 |     perror("Error opening library in dlopen call"); 
1349 |     return retval;
1350 |   } 
1352 |     if (cuMemcpyHtoA_v2_h == NULL)
1353 | 	cuMemcpyHtoA_v2_h = (cuMemcpyHtoA_v2_p_h) dlsym(tau_handle,"cuMemcpyHtoA_v2"); 
1354 |     if (cuMemcpyHtoA_v2_h == NULL) {
1355 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1356 |       return retval;
1357 |     }
1370 |   CUresult retval;
1371 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyAtoH_v2(void *, CUarray, size_t, size_t) C", "", CUDA_API);
1372 |   if (tau_handle == NULL) 
1373 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1374 | 
1375 |   if (tau_handle == NULL) { 
1376 |     perror("Error opening library in dlopen call"); 
1377 |     return retval;
1378 |   } 
1380 |     if (cuMemcpyAtoH_v2_h == NULL)
1381 | 	cuMemcpyAtoH_v2_h = (cuMemcpyAtoH_v2_p_h) dlsym(tau_handle,"cuMemcpyAtoH_v2"); 
1382 |     if (cuMemcpyAtoH_v2_h == NULL) {
1383 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1384 |       return retval;
1385 |     }
1398 |   CUresult retval;
1399 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyAtoA_v2(CUarray, size_t, CUarray, size_t, size_t) C", "", CUDA_API);
1400 |   if (tau_handle == NULL) 
1401 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1402 | 
1403 |   if (tau_handle == NULL) { 
1404 |     perror("Error opening library in dlopen call"); 
1405 |     return retval;
1406 |   } 
1408 |     if (cuMemcpyAtoA_v2_h == NULL)
1409 | 	cuMemcpyAtoA_v2_h = (cuMemcpyAtoA_v2_p_h) dlsym(tau_handle,"cuMemcpyAtoA_v2"); 
1410 |     if (cuMemcpyAtoA_v2_h == NULL) {
1411 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1412 |       return retval;
1413 |     }
1426 |   CUresult retval;
1427 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpy2D_v2(const CUDA_MEMCPY2D *) C", "", CUDA_API);
1428 |   if (tau_handle == NULL) 
1429 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1430 | 
1431 |   if (tau_handle == NULL) { 
1432 |     perror("Error opening library in dlopen call"); 
1433 |     return retval;
1434 |   } 
1436 |     if (cuMemcpy2D_v2_h == NULL)
1437 | 	cuMemcpy2D_v2_h = (cuMemcpy2D_v2_p_h) dlsym(tau_handle,"cuMemcpy2D_v2"); 
1438 |     if (cuMemcpy2D_v2_h == NULL) {
1439 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1440 |       return retval;
1441 |     }
1454 |   CUresult retval;
1455 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpy2DUnaligned_v2(const CUDA_MEMCPY2D *) C", "", CUDA_API);
1456 |   if (tau_handle == NULL) 
1457 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1458 | 
1459 |   if (tau_handle == NULL) { 
1460 |     perror("Error opening library in dlopen call"); 
1461 |     return retval;
1462 |   } 
1464 |     if (cuMemcpy2DUnaligned_v2_h == NULL)
1465 | 	cuMemcpy2DUnaligned_v2_h = (cuMemcpy2DUnaligned_v2_p_h) dlsym(tau_handle,"cuMemcpy2DUnaligned_v2"); 
1466 |     if (cuMemcpy2DUnaligned_v2_h == NULL) {
1467 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1468 |       return retval;
1469 |     }
1482 |   CUresult retval;
1483 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpy3D_v2(const CUDA_MEMCPY3D *) C", "", CUDA_API);
1484 |   if (tau_handle == NULL) 
1485 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1486 | 
1487 |   if (tau_handle == NULL) { 
1488 |     perror("Error opening library in dlopen call"); 
1489 |     return retval;
1490 |   } 
1492 |     if (cuMemcpy3D_v2_h == NULL)
1493 | 	cuMemcpy3D_v2_h = (cuMemcpy3D_v2_p_h) dlsym(tau_handle,"cuMemcpy3D_v2"); 
1494 |     if (cuMemcpy3D_v2_h == NULL) {
1495 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1496 |       return retval;
1497 |     }
1510 |   CUresult retval;
1511 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyHtoDAsync_v2(CUdeviceptr, const void *, size_t, CUstream) C", "", CUDA_API);
1512 |   if (tau_handle == NULL) 
1513 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1514 | 
1515 |   if (tau_handle == NULL) { 
1516 |     perror("Error opening library in dlopen call"); 
1517 |     return retval;
1518 |   } 
1520 |     if (cuMemcpyHtoDAsync_v2_h == NULL)
1521 | 	cuMemcpyHtoDAsync_v2_h = (cuMemcpyHtoDAsync_v2_p_h) dlsym(tau_handle,"cuMemcpyHtoDAsync_v2"); 
1522 |     if (cuMemcpyHtoDAsync_v2_h == NULL) {
1523 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1524 |       return retval;
1525 |     }
1538 |   CUresult retval;
1539 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyDtoHAsync_v2(void *, CUdeviceptr, size_t, CUstream) C", "", CUDA_API);
1540 |   if (tau_handle == NULL) 
1541 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1542 | 
1543 |   if (tau_handle == NULL) { 
1544 |     perror("Error opening library in dlopen call"); 
1545 |     return retval;
1546 |   } 
1548 |     if (cuMemcpyDtoHAsync_v2_h == NULL)
1549 | 	cuMemcpyDtoHAsync_v2_h = (cuMemcpyDtoHAsync_v2_p_h) dlsym(tau_handle,"cuMemcpyDtoHAsync_v2"); 
1550 |     if (cuMemcpyDtoHAsync_v2_h == NULL) {
1551 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1552 |       return retval;
1553 |     }
1566 |   CUresult retval;
1567 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyDtoDAsync_v2(CUdeviceptr, CUdeviceptr, size_t, CUstream) C", "", CUDA_API);
1568 |   if (tau_handle == NULL) 
1569 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1570 | 
1571 |   if (tau_handle == NULL) { 
1572 |     perror("Error opening library in dlopen call"); 
1573 |     return retval;
1574 |   } 
1576 |     if (cuMemcpyDtoDAsync_v2_h == NULL)
1577 | 	cuMemcpyDtoDAsync_v2_h = (cuMemcpyDtoDAsync_v2_p_h) dlsym(tau_handle,"cuMemcpyDtoDAsync_v2"); 
1578 |     if (cuMemcpyDtoDAsync_v2_h == NULL) {
1579 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1580 |       return retval;
1581 |     }
1594 |   CUresult retval;
1595 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyHtoAAsync_v2(CUarray, size_t, const void *, size_t, CUstream) C", "", CUDA_API);
1596 |   if (tau_handle == NULL) 
1597 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1598 | 
1599 |   if (tau_handle == NULL) { 
1600 |     perror("Error opening library in dlopen call"); 
1601 |     return retval;
1602 |   } 
1604 |     if (cuMemcpyHtoAAsync_v2_h == NULL)
1605 | 	cuMemcpyHtoAAsync_v2_h = (cuMemcpyHtoAAsync_v2_p_h) dlsym(tau_handle,"cuMemcpyHtoAAsync_v2"); 
1606 |     if (cuMemcpyHtoAAsync_v2_h == NULL) {
1607 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1608 |       return retval;
1609 |     }
1622 |   CUresult retval;
1623 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpyAtoHAsync_v2(void *, CUarray, size_t, size_t, CUstream) C", "", CUDA_API);
1624 |   if (tau_handle == NULL) 
1625 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1626 | 
1627 |   if (tau_handle == NULL) { 
1628 |     perror("Error opening library in dlopen call"); 
1629 |     return retval;
1630 |   } 
1632 |     if (cuMemcpyAtoHAsync_v2_h == NULL)
1633 | 	cuMemcpyAtoHAsync_v2_h = (cuMemcpyAtoHAsync_v2_p_h) dlsym(tau_handle,"cuMemcpyAtoHAsync_v2"); 
1634 |     if (cuMemcpyAtoHAsync_v2_h == NULL) {
1635 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1636 |       return retval;
1637 |     }
1650 |   CUresult retval;
1651 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpy2DAsync_v2(const CUDA_MEMCPY2D *, CUstream) C", "", CUDA_API);
1652 |   if (tau_handle == NULL) 
1653 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1654 | 
1655 |   if (tau_handle == NULL) { 
1656 |     perror("Error opening library in dlopen call"); 
1657 |     return retval;
1658 |   } 
1660 |     if (cuMemcpy2DAsync_v2_h == NULL)
1661 | 	cuMemcpy2DAsync_v2_h = (cuMemcpy2DAsync_v2_p_h) dlsym(tau_handle,"cuMemcpy2DAsync_v2"); 
1662 |     if (cuMemcpy2DAsync_v2_h == NULL) {
1663 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1664 |       return retval;
1665 |     }
1678 |   CUresult retval;
1679 |   TAU_PROFILE_TIMER(t,"CUresult cuMemcpy3DAsync_v2(const CUDA_MEMCPY3D *, CUstream) C", "", CUDA_API);
1680 |   if (tau_handle == NULL) 
1681 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1682 | 
1683 |   if (tau_handle == NULL) { 
1684 |     perror("Error opening library in dlopen call"); 
1685 |     return retval;
1686 |   } 
1688 |     if (cuMemcpy3DAsync_v2_h == NULL)
1689 | 	cuMemcpy3DAsync_v2_h = (cuMemcpy3DAsync_v2_p_h) dlsym(tau_handle,"cuMemcpy3DAsync_v2"); 
1690 |     if (cuMemcpy3DAsync_v2_h == NULL) {
1691 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1692 |       return retval;
1693 |     }
1706 |   CUresult retval;
1707 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD8_v2(CUdeviceptr, unsigned char, size_t) C", "", CUDA_API);
1708 |   if (tau_handle == NULL) 
1709 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1710 | 
1711 |   if (tau_handle == NULL) { 
1712 |     perror("Error opening library in dlopen call"); 
1713 |     return retval;
1714 |   } 
1716 |     if (cuMemsetD8_v2_h == NULL)
1717 | 	cuMemsetD8_v2_h = (cuMemsetD8_v2_p_h) dlsym(tau_handle,"cuMemsetD8_v2"); 
1718 |     if (cuMemsetD8_v2_h == NULL) {
1719 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1720 |       return retval;
1721 |     }
1734 |   CUresult retval;
1735 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD16_v2(CUdeviceptr, unsigned short, size_t) C", "", CUDA_API);
1736 |   if (tau_handle == NULL) 
1737 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1738 | 
1739 |   if (tau_handle == NULL) { 
1740 |     perror("Error opening library in dlopen call"); 
1741 |     return retval;
1742 |   } 
1744 |     if (cuMemsetD16_v2_h == NULL)
1745 | 	cuMemsetD16_v2_h = (cuMemsetD16_v2_p_h) dlsym(tau_handle,"cuMemsetD16_v2"); 
1746 |     if (cuMemsetD16_v2_h == NULL) {
1747 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1748 |       return retval;
1749 |     }
1762 |   CUresult retval;
1763 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD32_v2(CUdeviceptr, unsigned int, size_t) C", "", CUDA_API);
1764 |   if (tau_handle == NULL) 
1765 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1766 | 
1767 |   if (tau_handle == NULL) { 
1768 |     perror("Error opening library in dlopen call"); 
1769 |     return retval;
1770 |   } 
1772 |     if (cuMemsetD32_v2_h == NULL)
1773 | 	cuMemsetD32_v2_h = (cuMemsetD32_v2_p_h) dlsym(tau_handle,"cuMemsetD32_v2"); 
1774 |     if (cuMemsetD32_v2_h == NULL) {
1775 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1776 |       return retval;
1777 |     }
1790 |   CUresult retval;
1791 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD2D8_v2(CUdeviceptr, size_t, unsigned char, size_t, size_t) C", "", CUDA_API);
1792 |   if (tau_handle == NULL) 
1793 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1794 | 
1795 |   if (tau_handle == NULL) { 
1796 |     perror("Error opening library in dlopen call"); 
1797 |     return retval;
1798 |   } 
1800 |     if (cuMemsetD2D8_v2_h == NULL)
1801 | 	cuMemsetD2D8_v2_h = (cuMemsetD2D8_v2_p_h) dlsym(tau_handle,"cuMemsetD2D8_v2"); 
1802 |     if (cuMemsetD2D8_v2_h == NULL) {
1803 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1804 |       return retval;
1805 |     }
1818 |   CUresult retval;
1819 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD2D16_v2(CUdeviceptr, size_t, unsigned short, size_t, size_t) C", "", CUDA_API);
1820 |   if (tau_handle == NULL) 
1821 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1822 | 
1823 |   if (tau_handle == NULL) { 
1824 |     perror("Error opening library in dlopen call"); 
1825 |     return retval;
1826 |   } 
1828 |     if (cuMemsetD2D16_v2_h == NULL)
1829 | 	cuMemsetD2D16_v2_h = (cuMemsetD2D16_v2_p_h) dlsym(tau_handle,"cuMemsetD2D16_v2"); 
1830 |     if (cuMemsetD2D16_v2_h == NULL) {
1831 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1832 |       return retval;
1833 |     }
1846 |   CUresult retval;
1847 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD2D32_v2(CUdeviceptr, size_t, unsigned int, size_t, size_t) C", "", CUDA_API);
1848 |   if (tau_handle == NULL) 
1849 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1850 | 
1851 |   if (tau_handle == NULL) { 
1852 |     perror("Error opening library in dlopen call"); 
1853 |     return retval;
1854 |   } 
1856 |     if (cuMemsetD2D32_v2_h == NULL)
1857 | 	cuMemsetD2D32_v2_h = (cuMemsetD2D32_v2_p_h) dlsym(tau_handle,"cuMemsetD2D32_v2"); 
1858 |     if (cuMemsetD2D32_v2_h == NULL) {
1859 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1860 |       return retval;
1861 |     }
1874 |   CUresult retval;
1875 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD8Async(CUdeviceptr, unsigned char, size_t, CUstream) C", "", CUDA_API);
1876 |   if (tau_handle == NULL) 
1877 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1878 | 
1879 |   if (tau_handle == NULL) { 
1880 |     perror("Error opening library in dlopen call"); 
1881 |     return retval;
1882 |   } 
1884 |     if (cuMemsetD8Async_h == NULL)
1885 | 	cuMemsetD8Async_h = (cuMemsetD8Async_p_h) dlsym(tau_handle,"cuMemsetD8Async"); 
1886 |     if (cuMemsetD8Async_h == NULL) {
1887 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1888 |       return retval;
1889 |     }
1902 |   CUresult retval;
1903 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD16Async(CUdeviceptr, unsigned short, size_t, CUstream) C", "", CUDA_API);
1904 |   if (tau_handle == NULL) 
1905 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1906 | 
1907 |   if (tau_handle == NULL) { 
1908 |     perror("Error opening library in dlopen call"); 
1909 |     return retval;
1910 |   } 
1912 |     if (cuMemsetD16Async_h == NULL)
1913 | 	cuMemsetD16Async_h = (cuMemsetD16Async_p_h) dlsym(tau_handle,"cuMemsetD16Async"); 
1914 |     if (cuMemsetD16Async_h == NULL) {
1915 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1916 |       return retval;
1917 |     }
1930 |   CUresult retval;
1931 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD32Async(CUdeviceptr, unsigned int, size_t, CUstream) C", "", CUDA_API);
1932 |   if (tau_handle == NULL) 
1933 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1934 | 
1935 |   if (tau_handle == NULL) { 
1936 |     perror("Error opening library in dlopen call"); 
1937 |     return retval;
1938 |   } 
1940 |     if (cuMemsetD32Async_h == NULL)
1941 | 	cuMemsetD32Async_h = (cuMemsetD32Async_p_h) dlsym(tau_handle,"cuMemsetD32Async"); 
1942 |     if (cuMemsetD32Async_h == NULL) {
1943 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1944 |       return retval;
1945 |     }
1958 |   CUresult retval;
1959 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD2D8Async(CUdeviceptr, size_t, unsigned char, size_t, size_t, CUstream) C", "", CUDA_API);
1960 |   if (tau_handle == NULL) 
1961 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1962 | 
1963 |   if (tau_handle == NULL) { 
1964 |     perror("Error opening library in dlopen call"); 
1965 |     return retval;
1966 |   } 
1968 |     if (cuMemsetD2D8Async_h == NULL)
1969 | 	cuMemsetD2D8Async_h = (cuMemsetD2D8Async_p_h) dlsym(tau_handle,"cuMemsetD2D8Async"); 
1970 |     if (cuMemsetD2D8Async_h == NULL) {
1971 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1972 |       return retval;
1973 |     }
1986 |   CUresult retval;
1987 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD2D16Async(CUdeviceptr, size_t, unsigned short, size_t, size_t, CUstream) C", "", CUDA_API);
1988 |   if (tau_handle == NULL) 
1989 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1990 | 
1991 |   if (tau_handle == NULL) { 
1992 |     perror("Error opening library in dlopen call"); 
1993 |     return retval;
1994 |   } 
1996 |     if (cuMemsetD2D16Async_h == NULL)
1997 | 	cuMemsetD2D16Async_h = (cuMemsetD2D16Async_p_h) dlsym(tau_handle,"cuMemsetD2D16Async"); 
1998 |     if (cuMemsetD2D16Async_h == NULL) {
1999 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2000 |       return retval;
2001 |     }
2014 |   CUresult retval;
2015 |   TAU_PROFILE_TIMER(t,"CUresult cuMemsetD2D32Async(CUdeviceptr, size_t, unsigned int, size_t, size_t, CUstream) C", "", CUDA_API);
2016 |   if (tau_handle == NULL) 
2017 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2018 | 
2019 |   if (tau_handle == NULL) { 
2020 |     perror("Error opening library in dlopen call"); 
2021 |     return retval;
2022 |   } 
2024 |     if (cuMemsetD2D32Async_h == NULL)
2025 | 	cuMemsetD2D32Async_h = (cuMemsetD2D32Async_p_h) dlsym(tau_handle,"cuMemsetD2D32Async"); 
2026 |     if (cuMemsetD2D32Async_h == NULL) {
2027 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2028 |       return retval;
2029 |     }
2042 |   CUresult retval;
2043 |   TAU_PROFILE_TIMER(t,"CUresult cuArrayCreate_v2(CUarray *, const CUDA_ARRAY_DESCRIPTOR *) C", "", CUDA_API);
2044 |   if (tau_handle == NULL) 
2045 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2046 | 
2047 |   if (tau_handle == NULL) { 
2048 |     perror("Error opening library in dlopen call"); 
2049 |     return retval;
2050 |   } 
2052 |     if (cuArrayCreate_v2_h == NULL)
2053 | 	cuArrayCreate_v2_h = (cuArrayCreate_v2_p_h) dlsym(tau_handle,"cuArrayCreate_v2"); 
2054 |     if (cuArrayCreate_v2_h == NULL) {
2055 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2056 |       return retval;
2057 |     }
2070 |   CUresult retval;
2071 |   TAU_PROFILE_TIMER(t,"CUresult cuArrayGetDescriptor_v2(CUDA_ARRAY_DESCRIPTOR *, CUarray) C", "", CUDA_API);
2072 |   if (tau_handle == NULL) 
2073 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2074 | 
2075 |   if (tau_handle == NULL) { 
2076 |     perror("Error opening library in dlopen call"); 
2077 |     return retval;
2078 |   } 
2080 |     if (cuArrayGetDescriptor_v2_h == NULL)
2081 | 	cuArrayGetDescriptor_v2_h = (cuArrayGetDescriptor_v2_p_h) dlsym(tau_handle,"cuArrayGetDescriptor_v2"); 
2082 |     if (cuArrayGetDescriptor_v2_h == NULL) {
2083 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2084 |       return retval;
2085 |     }
2098 |   CUresult retval;
2099 |   TAU_PROFILE_TIMER(t,"CUresult cuArrayDestroy(CUarray) C", "", CUDA_API);
2100 |   if (tau_handle == NULL) 
2101 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2102 | 
2103 |   if (tau_handle == NULL) { 
2104 |     perror("Error opening library in dlopen call"); 
2105 |     return retval;
2106 |   } 
2108 |     if (cuArrayDestroy_h == NULL)
2109 | 	cuArrayDestroy_h = (cuArrayDestroy_p_h) dlsym(tau_handle,"cuArrayDestroy"); 
2110 |     if (cuArrayDestroy_h == NULL) {
2111 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2112 |       return retval;
2113 |     }
2126 |   CUresult retval;
2127 |   TAU_PROFILE_TIMER(t,"CUresult cuArray3DCreate_v2(CUarray *, const CUDA_ARRAY3D_DESCRIPTOR *) C", "", CUDA_API);
2128 |   if (tau_handle == NULL) 
2129 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2130 | 
2131 |   if (tau_handle == NULL) { 
2132 |     perror("Error opening library in dlopen call"); 
2133 |     return retval;
2134 |   } 
2136 |     if (cuArray3DCreate_v2_h == NULL)
2137 | 	cuArray3DCreate_v2_h = (cuArray3DCreate_v2_p_h) dlsym(tau_handle,"cuArray3DCreate_v2"); 
2138 |     if (cuArray3DCreate_v2_h == NULL) {
2139 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2140 |       return retval;
2141 |     }
2154 |   CUresult retval;
2155 |   TAU_PROFILE_TIMER(t,"CUresult cuArray3DGetDescriptor_v2(CUDA_ARRAY3D_DESCRIPTOR *, CUarray) C", "", CUDA_API);
2156 |   if (tau_handle == NULL) 
2157 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2158 | 
2159 |   if (tau_handle == NULL) { 
2160 |     perror("Error opening library in dlopen call"); 
2161 |     return retval;
2162 |   } 
2164 |     if (cuArray3DGetDescriptor_v2_h == NULL)
2165 | 	cuArray3DGetDescriptor_v2_h = (cuArray3DGetDescriptor_v2_p_h) dlsym(tau_handle,"cuArray3DGetDescriptor_v2"); 
2166 |     if (cuArray3DGetDescriptor_v2_h == NULL) {
2167 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2168 |       return retval;
2169 |     }
2182 |   CUresult retval;
2183 |   TAU_PROFILE_TIMER(t,"CUresult cuStreamCreate(CUstream *, unsigned int) C", "", CUDA_API);
2184 |   if (tau_handle == NULL) 
2185 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2186 | 
2187 |   if (tau_handle == NULL) { 
2188 |     perror("Error opening library in dlopen call"); 
2189 |     return retval;
2190 |   } 
2192 |     if (cuStreamCreate_h == NULL)
2193 | 	cuStreamCreate_h = (cuStreamCreate_p_h) dlsym(tau_handle,"cuStreamCreate"); 
2194 |     if (cuStreamCreate_h == NULL) {
2195 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2196 |       return retval;
2197 |     }
2210 |   CUresult retval;
2211 |   TAU_PROFILE_TIMER(t,"CUresult cuStreamWaitEvent(CUstream, CUevent, unsigned int) C", "", CUDA_API);
2212 |   if (tau_handle == NULL) 
2213 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2214 | 
2215 |   if (tau_handle == NULL) { 
2216 |     perror("Error opening library in dlopen call"); 
2217 |     return retval;
2218 |   } 
2220 |     if (cuStreamWaitEvent_h == NULL)
2221 | 	cuStreamWaitEvent_h = (cuStreamWaitEvent_p_h) dlsym(tau_handle,"cuStreamWaitEvent"); 
2222 |     if (cuStreamWaitEvent_h == NULL) {
2223 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2224 |       return retval;
2225 |     }
2238 |   CUresult retval;
2239 |   TAU_PROFILE_TIMER(t,"CUresult cuStreamQuery(CUstream) C", "", CUDA_API);
2240 |   if (tau_handle == NULL) 
2241 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2242 | 
2243 |   if (tau_handle == NULL) { 
2244 |     perror("Error opening library in dlopen call"); 
2245 |     return retval;
2246 |   } 
2248 |     if (cuStreamQuery_h == NULL)
2249 | 	cuStreamQuery_h = (cuStreamQuery_p_h) dlsym(tau_handle,"cuStreamQuery"); 
2250 |     if (cuStreamQuery_h == NULL) {
2251 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2252 |       return retval;
2253 |     }
2266 |   CUresult retval;
2267 |   TAU_PROFILE_TIMER(t,"CUresult cuStreamSynchronize(CUstream) C", "", CUDA_SYNC);
2268 |   if (tau_handle == NULL) 
2269 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2270 | 
2271 |   if (tau_handle == NULL) { 
2272 |     perror("Error opening library in dlopen call"); 
2273 |     return retval;
2274 |   } 
2276 |     if (cuStreamSynchronize_h == NULL)
2277 | 	cuStreamSynchronize_h = (cuStreamSynchronize_p_h) dlsym(tau_handle,"cuStreamSynchronize"); 
2278 |     if (cuStreamSynchronize_h == NULL) {
2279 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2280 |       return retval;
2281 |     }
2297 |   CUresult retval;
2298 |   TAU_PROFILE_TIMER(t,"CUresult cuStreamDestroy(CUstream) C", "", CUDA_API);
2299 |   if (tau_handle == NULL) 
2300 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2301 | 
2302 |   if (tau_handle == NULL) { 
2303 |     perror("Error opening library in dlopen call"); 
2304 |     return retval;
2305 |   } 
2307 |     if (cuStreamDestroy_h == NULL)
2308 | 	cuStreamDestroy_h = (cuStreamDestroy_p_h) dlsym(tau_handle,"cuStreamDestroy"); 
2309 |     if (cuStreamDestroy_h == NULL) {
2310 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2311 |       return retval;
2312 |     }
2325 |   CUresult retval;
2326 |   TAU_PROFILE_TIMER(t,"CUresult cuEventCreate(CUevent *, unsigned int) C", "", CUDA_API);
2327 |   if (tau_handle == NULL) 
2328 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2329 | 
2330 |   if (tau_handle == NULL) { 
2331 |     perror("Error opening library in dlopen call"); 
2332 |     return retval;
2333 |   } 
2335 |     if (cuEventCreate_h == NULL)
2336 | 	cuEventCreate_h = (cuEventCreate_p_h) dlsym(tau_handle,"cuEventCreate"); 
2337 |     if (cuEventCreate_h == NULL) {
2338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2339 |       return retval;
2340 |     }
2353 |   CUresult retval;
2354 |   TAU_PROFILE_TIMER(t,"CUresult cuEventRecord(CUevent, CUstream) C", "", CUDA_API);
2355 |   if (tau_handle == NULL) 
2356 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2357 | 
2358 |   if (tau_handle == NULL) { 
2359 |     perror("Error opening library in dlopen call"); 
2360 |     return retval;
2361 |   } 
2363 |     if (cuEventRecord_h == NULL)
2364 | 	cuEventRecord_h = (cuEventRecord_p_h) dlsym(tau_handle,"cuEventRecord"); 
2365 |     if (cuEventRecord_h == NULL) {
2366 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2367 |       return retval;
2368 |     }
2381 |   CUresult retval;
2382 |   TAU_PROFILE_TIMER(t,"CUresult cuEventQuery(CUevent) C", "", CUDA_API);
2383 |   if (tau_handle == NULL) 
2384 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2385 | 
2386 |   if (tau_handle == NULL) { 
2387 |     perror("Error opening library in dlopen call"); 
2388 |     return retval;
2389 |   } 
2391 |     if (cuEventQuery_h == NULL)
2392 | 	cuEventQuery_h = (cuEventQuery_p_h) dlsym(tau_handle,"cuEventQuery"); 
2393 |     if (cuEventQuery_h == NULL) {
2394 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2395 |       return retval;
2396 |     }
2409 |   CUresult retval;
2410 |   TAU_PROFILE_TIMER(t,"CUresult cuEventSynchronize(CUevent) C", "", CUDA_SYNC);
2411 |   if (tau_handle == NULL) 
2412 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2413 | 
2414 |   if (tau_handle == NULL) { 
2415 |     perror("Error opening library in dlopen call"); 
2416 |     return retval;
2417 |   } 
2419 |     if (cuEventSynchronize_h == NULL)
2420 | 	cuEventSynchronize_h = (cuEventSynchronize_p_h) dlsym(tau_handle,"cuEventSynchronize"); 
2421 |     if (cuEventSynchronize_h == NULL) {
2422 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2423 |       return retval;
2424 |     }
2440 |   CUresult retval;
2441 |   TAU_PROFILE_TIMER(t,"CUresult cuEventDestroy(CUevent) C", "", CUDA_API);
2442 |   if (tau_handle == NULL) 
2443 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2444 | 
2445 |   if (tau_handle == NULL) { 
2446 |     perror("Error opening library in dlopen call"); 
2447 |     return retval;
2448 |   } 
2450 |     if (cuEventDestroy_h == NULL)
2451 | 	cuEventDestroy_h = (cuEventDestroy_p_h) dlsym(tau_handle,"cuEventDestroy"); 
2452 |     if (cuEventDestroy_h == NULL) {
2453 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2454 |       return retval;
2455 |     }
2468 |   CUresult retval;
2469 |   TAU_PROFILE_TIMER(t,"CUresult cuEventElapsedTime(float *, CUevent, CUevent) C", "", CUDA_API);
2470 |   if (tau_handle == NULL) 
2471 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2472 | 
2473 |   if (tau_handle == NULL) { 
2474 |     perror("Error opening library in dlopen call"); 
2475 |     return retval;
2476 |   } 
2478 |     if (cuEventElapsedTime_h == NULL)
2479 | 	cuEventElapsedTime_h = (cuEventElapsedTime_p_h) dlsym(tau_handle,"cuEventElapsedTime"); 
2480 |     if (cuEventElapsedTime_h == NULL) {
2481 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2482 |       return retval;
2483 |     }
2496 |   CUresult retval;
2497 |   TAU_PROFILE_TIMER(t,"CUresult cuFuncSetBlockShape(CUfunction, int, int, int) C", "", CUDA_API);
2498 |   if (tau_handle == NULL) 
2499 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2500 | 
2501 |   if (tau_handle == NULL) { 
2502 |     perror("Error opening library in dlopen call"); 
2503 |     return retval;
2504 |   } 
2506 |     if (cuFuncSetBlockShape_h == NULL)
2507 | 	cuFuncSetBlockShape_h = (cuFuncSetBlockShape_p_h) dlsym(tau_handle,"cuFuncSetBlockShape"); 
2508 |     if (cuFuncSetBlockShape_h == NULL) {
2509 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2510 |       return retval;
2511 |     }
2524 |   CUresult retval;
2525 |   TAU_PROFILE_TIMER(t,"CUresult cuFuncSetSharedSize(CUfunction, unsigned int) C", "", CUDA_API);
2526 |   if (tau_handle == NULL) 
2527 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2528 | 
2529 |   if (tau_handle == NULL) { 
2530 |     perror("Error opening library in dlopen call"); 
2531 |     return retval;
2532 |   } 
2534 |     if (cuFuncSetSharedSize_h == NULL)
2535 | 	cuFuncSetSharedSize_h = (cuFuncSetSharedSize_p_h) dlsym(tau_handle,"cuFuncSetSharedSize"); 
2536 |     if (cuFuncSetSharedSize_h == NULL) {
2537 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2538 |       return retval;
2539 |     }
2552 |   CUresult retval;
2553 |   TAU_PROFILE_TIMER(t,"CUresult cuFuncGetAttribute(int *, CUfunction_attribute, CUfunction) C", "", CUDA_API);
2554 |   if (tau_handle == NULL) 
2555 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2556 | 
2557 |   if (tau_handle == NULL) { 
2558 |     perror("Error opening library in dlopen call"); 
2559 |     return retval;
2560 |   } 
2562 |     if (cuFuncGetAttribute_h == NULL)
2563 | 	cuFuncGetAttribute_h = (cuFuncGetAttribute_p_h) dlsym(tau_handle,"cuFuncGetAttribute"); 
2564 |     if (cuFuncGetAttribute_h == NULL) {
2565 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2566 |       return retval;
2567 |     }
2580 |   CUresult retval;
2581 |   TAU_PROFILE_TIMER(t,"CUresult cuFuncSetCacheConfig(CUfunction, CUfunc_cache) C", "", CUDA_API);
2582 |   if (tau_handle == NULL) 
2583 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2584 | 
2585 |   if (tau_handle == NULL) { 
2586 |     perror("Error opening library in dlopen call"); 
2587 |     return retval;
2588 |   } 
2590 |     if (cuFuncSetCacheConfig_h == NULL)
2591 | 	cuFuncSetCacheConfig_h = (cuFuncSetCacheConfig_p_h) dlsym(tau_handle,"cuFuncSetCacheConfig"); 
2592 |     if (cuFuncSetCacheConfig_h == NULL) {
2593 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2594 |       return retval;
2595 |     }
2608 |   CUresult retval;
2609 |   TAU_PROFILE_TIMER(t,"CUresult cuParamSetSize(CUfunction, unsigned int) C", "", CUDA_API);
2610 |   if (tau_handle == NULL) 
2611 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2612 | 
2613 |   if (tau_handle == NULL) { 
2614 |     perror("Error opening library in dlopen call"); 
2615 |     return retval;
2616 |   } 
2618 |     if (cuParamSetSize_h == NULL)
2619 | 	cuParamSetSize_h = (cuParamSetSize_p_h) dlsym(tau_handle,"cuParamSetSize"); 
2620 |     if (cuParamSetSize_h == NULL) {
2621 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2622 |       return retval;
2623 |     }
2636 |   CUresult retval;
2637 |   TAU_PROFILE_TIMER(t,"CUresult cuParamSeti(CUfunction, int, unsigned int) C", "", CUDA_API);
2638 |   if (tau_handle == NULL) 
2639 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2640 | 
2641 |   if (tau_handle == NULL) { 
2642 |     perror("Error opening library in dlopen call"); 
2643 |     return retval;
2644 |   } 
2646 |     if (cuParamSeti_h == NULL)
2647 | 	cuParamSeti_h = (cuParamSeti_p_h) dlsym(tau_handle,"cuParamSeti"); 
2648 |     if (cuParamSeti_h == NULL) {
2649 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2650 |       return retval;
2651 |     }
2664 |   CUresult retval;
2665 |   TAU_PROFILE_TIMER(t,"CUresult cuParamSetf(CUfunction, int, float) C", "", CUDA_API);
2666 |   if (tau_handle == NULL) 
2667 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2668 | 
2669 |   if (tau_handle == NULL) { 
2670 |     perror("Error opening library in dlopen call"); 
2671 |     return retval;
2672 |   } 
2674 |     if (cuParamSetf_h == NULL)
2675 | 	cuParamSetf_h = (cuParamSetf_p_h) dlsym(tau_handle,"cuParamSetf"); 
2676 |     if (cuParamSetf_h == NULL) {
2677 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2678 |       return retval;
2679 |     }
2692 |   CUresult retval;
2693 |   TAU_PROFILE_TIMER(t,"CUresult cuParamSetv(CUfunction, int, void *, unsigned int) C", "", CUDA_API);
2694 |   if (tau_handle == NULL) 
2695 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2696 | 
2697 |   if (tau_handle == NULL) { 
2698 |     perror("Error opening library in dlopen call"); 
2699 |     return retval;
2700 |   } 
2702 |     if (cuParamSetv_h == NULL)
2703 | 	cuParamSetv_h = (cuParamSetv_p_h) dlsym(tau_handle,"cuParamSetv"); 
2704 |     if (cuParamSetv_h == NULL) {
2705 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2706 |       return retval;
2707 |     }
2720 |   CUresult retval;
2721 |   TAU_PROFILE_TIMER(t,"CUresult cuLaunch(CUfunction) C", "", CUDA_API);
2722 |   if (tau_handle == NULL) 
2723 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2724 | 
2725 |   if (tau_handle == NULL) { 
2726 |     perror("Error opening library in dlopen call"); 
2727 |     return retval;
2728 |   } 
2730 |     if (cuLaunch_h == NULL)
2731 | 	cuLaunch_h = (cuLaunch_p_h) dlsym(tau_handle,"cuLaunch"); 
2732 |     if (cuLaunch_h == NULL) {
2733 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2734 |       return retval;
2735 |     }
2782 |   CUresult retval;
2783 |   TAU_PROFILE_TIMER(t,"CUresult cuLaunchKernel(CUfunction, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, CUstream, void **, void **) C", "", CUDA_API);
2784 |   if (tau_handle == NULL) 
2785 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2786 | 
2787 |   if (tau_handle == NULL) { 
2788 |     perror("Error opening library in dlopen call"); 
2789 |     return retval;
2790 |   } 
2792 |     if (cuLaunchKernel_h == NULL)
2793 | 	cuLaunchKernel_h = (cuLaunchKernel_p_h) dlsym(tau_handle,"cuLaunchKernel"); 
2794 |     if (cuLaunchKernel_h == NULL) {
2795 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2796 |       return retval;
2797 |     }
2823 |   CUresult retval;
2824 |   TAU_PROFILE_TIMER(t,"CUresult cuLaunchGrid(CUfunction, int, int) C", "", CUDA_API);
2825 |   if (tau_handle == NULL) 
2826 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2827 | 
2828 |   if (tau_handle == NULL) { 
2829 |     perror("Error opening library in dlopen call"); 
2830 |     return retval;
2831 |   } 
2833 |     if (cuLaunchGrid_h == NULL)
2834 | 	cuLaunchGrid_h = (cuLaunchGrid_p_h) dlsym(tau_handle,"cuLaunchGrid"); 
2835 |     if (cuLaunchGrid_h == NULL) {
2836 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2837 |       return retval;
2838 |     }
2864 |   CUresult retval;
2865 |   TAU_PROFILE_TIMER(t,"CUresult cuLaunchGridAsync(CUfunction, int, int, CUstream) C", "", CUDA_API);
2866 |   if (tau_handle == NULL) 
2867 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2868 | 
2869 |   if (tau_handle == NULL) { 
2870 |     perror("Error opening library in dlopen call"); 
2871 |     return retval;
2872 |   } 
2874 |     if (cuLaunchGridAsync_h == NULL)
2875 | 	cuLaunchGridAsync_h = (cuLaunchGridAsync_p_h) dlsym(tau_handle,"cuLaunchGridAsync"); 
2876 |     if (cuLaunchGridAsync_h == NULL) {
2877 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2878 |       return retval;
2879 |     }
2905 |   CUresult retval;
2906 |   TAU_PROFILE_TIMER(t,"CUresult cuParamSetTexRef(CUfunction, int, CUtexref) C", "", CUDA_API);
2907 |   if (tau_handle == NULL) 
2908 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2909 | 
2910 |   if (tau_handle == NULL) { 
2911 |     perror("Error opening library in dlopen call"); 
2912 |     return retval;
2913 |   } 
2915 |     if (cuParamSetTexRef_h == NULL)
2916 | 	cuParamSetTexRef_h = (cuParamSetTexRef_p_h) dlsym(tau_handle,"cuParamSetTexRef"); 
2917 |     if (cuParamSetTexRef_h == NULL) {
2918 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2919 |       return retval;
2920 |     }
2933 |   CUresult retval;
2934 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefSetArray(CUtexref, CUarray, unsigned int) C", "", CUDA_API);
2935 |   if (tau_handle == NULL) 
2936 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2937 | 
2938 |   if (tau_handle == NULL) { 
2939 |     perror("Error opening library in dlopen call"); 
2940 |     return retval;
2941 |   } 
2943 |     if (cuTexRefSetArray_h == NULL)
2944 | 	cuTexRefSetArray_h = (cuTexRefSetArray_p_h) dlsym(tau_handle,"cuTexRefSetArray"); 
2945 |     if (cuTexRefSetArray_h == NULL) {
2946 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2947 |       return retval;
2948 |     }
2961 |   CUresult retval;
2962 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefSetAddress_v2(size_t *, CUtexref, CUdeviceptr, size_t) C", "", CUDA_API);
2963 |   if (tau_handle == NULL) 
2964 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2965 | 
2966 |   if (tau_handle == NULL) { 
2967 |     perror("Error opening library in dlopen call"); 
2968 |     return retval;
2969 |   } 
2971 |     if (cuTexRefSetAddress_v2_h == NULL)
2972 | 	cuTexRefSetAddress_v2_h = (cuTexRefSetAddress_v2_p_h) dlsym(tau_handle,"cuTexRefSetAddress_v2"); 
2973 |     if (cuTexRefSetAddress_v2_h == NULL) {
2974 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2975 |       return retval;
2976 |     }
2989 |   CUresult retval;
2990 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefSetAddress2D_v2(CUtexref, const CUDA_ARRAY_DESCRIPTOR *, CUdeviceptr, size_t) C", "", CUDA_API);
2991 |   if (tau_handle == NULL) 
2992 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2993 | 
2994 |   if (tau_handle == NULL) { 
2995 |     perror("Error opening library in dlopen call"); 
2996 |     return retval;
2997 |   } 
2999 |     if (cuTexRefSetAddress2D_v2_h == NULL)
3000 | 	cuTexRefSetAddress2D_v2_h = (cuTexRefSetAddress2D_v2_p_h) dlsym(tau_handle,"cuTexRefSetAddress2D_v2"); 
3001 |     if (cuTexRefSetAddress2D_v2_h == NULL) {
3002 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3003 |       return retval;
3004 |     }
3017 |   CUresult retval;
3018 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefSetFormat(CUtexref, CUarray_format, int) C", "", CUDA_API);
3019 |   if (tau_handle == NULL) 
3020 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3021 | 
3022 |   if (tau_handle == NULL) { 
3023 |     perror("Error opening library in dlopen call"); 
3024 |     return retval;
3025 |   } 
3027 |     if (cuTexRefSetFormat_h == NULL)
3028 | 	cuTexRefSetFormat_h = (cuTexRefSetFormat_p_h) dlsym(tau_handle,"cuTexRefSetFormat"); 
3029 |     if (cuTexRefSetFormat_h == NULL) {
3030 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3031 |       return retval;
3032 |     }
3045 |   CUresult retval;
3046 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefSetAddressMode(CUtexref, int, CUaddress_mode) C", "", CUDA_API);
3047 |   if (tau_handle == NULL) 
3048 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3049 | 
3050 |   if (tau_handle == NULL) { 
3051 |     perror("Error opening library in dlopen call"); 
3052 |     return retval;
3053 |   } 
3055 |     if (cuTexRefSetAddressMode_h == NULL)
3056 | 	cuTexRefSetAddressMode_h = (cuTexRefSetAddressMode_p_h) dlsym(tau_handle,"cuTexRefSetAddressMode"); 
3057 |     if (cuTexRefSetAddressMode_h == NULL) {
3058 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3059 |       return retval;
3060 |     }
3073 |   CUresult retval;
3074 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefSetFilterMode(CUtexref, CUfilter_mode) C", "", CUDA_API);
3075 |   if (tau_handle == NULL) 
3076 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3077 | 
3078 |   if (tau_handle == NULL) { 
3079 |     perror("Error opening library in dlopen call"); 
3080 |     return retval;
3081 |   } 
3083 |     if (cuTexRefSetFilterMode_h == NULL)
3084 | 	cuTexRefSetFilterMode_h = (cuTexRefSetFilterMode_p_h) dlsym(tau_handle,"cuTexRefSetFilterMode"); 
3085 |     if (cuTexRefSetFilterMode_h == NULL) {
3086 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3087 |       return retval;
3088 |     }
3101 |   CUresult retval;
3102 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefSetFlags(CUtexref, unsigned int) C", "", CUDA_API);
3103 |   if (tau_handle == NULL) 
3104 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3105 | 
3106 |   if (tau_handle == NULL) { 
3107 |     perror("Error opening library in dlopen call"); 
3108 |     return retval;
3109 |   } 
3111 |     if (cuTexRefSetFlags_h == NULL)
3112 | 	cuTexRefSetFlags_h = (cuTexRefSetFlags_p_h) dlsym(tau_handle,"cuTexRefSetFlags"); 
3113 |     if (cuTexRefSetFlags_h == NULL) {
3114 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3115 |       return retval;
3116 |     }
3129 |   CUresult retval;
3130 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefGetAddress_v2(CUdeviceptr *, CUtexref) C", "", CUDA_API);
3131 |   if (tau_handle == NULL) 
3132 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3133 | 
3134 |   if (tau_handle == NULL) { 
3135 |     perror("Error opening library in dlopen call"); 
3136 |     return retval;
3137 |   } 
3139 |     if (cuTexRefGetAddress_v2_h == NULL)
3140 | 	cuTexRefGetAddress_v2_h = (cuTexRefGetAddress_v2_p_h) dlsym(tau_handle,"cuTexRefGetAddress_v2"); 
3141 |     if (cuTexRefGetAddress_v2_h == NULL) {
3142 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3143 |       return retval;
3144 |     }
3157 |   CUresult retval;
3158 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefGetArray(CUarray *, CUtexref) C", "", CUDA_API);
3159 |   if (tau_handle == NULL) 
3160 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3161 | 
3162 |   if (tau_handle == NULL) { 
3163 |     perror("Error opening library in dlopen call"); 
3164 |     return retval;
3165 |   } 
3167 |     if (cuTexRefGetArray_h == NULL)
3168 | 	cuTexRefGetArray_h = (cuTexRefGetArray_p_h) dlsym(tau_handle,"cuTexRefGetArray"); 
3169 |     if (cuTexRefGetArray_h == NULL) {
3170 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3171 |       return retval;
3172 |     }
3185 |   CUresult retval;
3186 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefGetAddressMode(CUaddress_mode *, CUtexref, int) C", "", CUDA_API);
3187 |   if (tau_handle == NULL) 
3188 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3189 | 
3190 |   if (tau_handle == NULL) { 
3191 |     perror("Error opening library in dlopen call"); 
3192 |     return retval;
3193 |   } 
3195 |     if (cuTexRefGetAddressMode_h == NULL)
3196 | 	cuTexRefGetAddressMode_h = (cuTexRefGetAddressMode_p_h) dlsym(tau_handle,"cuTexRefGetAddressMode"); 
3197 |     if (cuTexRefGetAddressMode_h == NULL) {
3198 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3199 |       return retval;
3200 |     }
3213 |   CUresult retval;
3214 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefGetFilterMode(CUfilter_mode *, CUtexref) C", "", CUDA_API);
3215 |   if (tau_handle == NULL) 
3216 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3217 | 
3218 |   if (tau_handle == NULL) { 
3219 |     perror("Error opening library in dlopen call"); 
3220 |     return retval;
3221 |   } 
3223 |     if (cuTexRefGetFilterMode_h == NULL)
3224 | 	cuTexRefGetFilterMode_h = (cuTexRefGetFilterMode_p_h) dlsym(tau_handle,"cuTexRefGetFilterMode"); 
3225 |     if (cuTexRefGetFilterMode_h == NULL) {
3226 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3227 |       return retval;
3228 |     }
3241 |   CUresult retval;
3242 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefGetFormat(CUarray_format *, int *, CUtexref) C", "", CUDA_API);
3243 |   if (tau_handle == NULL) 
3244 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3245 | 
3246 |   if (tau_handle == NULL) { 
3247 |     perror("Error opening library in dlopen call"); 
3248 |     return retval;
3249 |   } 
3251 |     if (cuTexRefGetFormat_h == NULL)
3252 | 	cuTexRefGetFormat_h = (cuTexRefGetFormat_p_h) dlsym(tau_handle,"cuTexRefGetFormat"); 
3253 |     if (cuTexRefGetFormat_h == NULL) {
3254 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3255 |       return retval;
3256 |     }
3269 |   CUresult retval;
3270 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefGetFlags(unsigned int *, CUtexref) C", "", CUDA_API);
3271 |   if (tau_handle == NULL) 
3272 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3273 | 
3274 |   if (tau_handle == NULL) { 
3275 |     perror("Error opening library in dlopen call"); 
3276 |     return retval;
3277 |   } 
3279 |     if (cuTexRefGetFlags_h == NULL)
3280 | 	cuTexRefGetFlags_h = (cuTexRefGetFlags_p_h) dlsym(tau_handle,"cuTexRefGetFlags"); 
3281 |     if (cuTexRefGetFlags_h == NULL) {
3282 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3283 |       return retval;
3284 |     }
3297 |   CUresult retval;
3298 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefCreate(CUtexref *) C", "", CUDA_API);
3299 |   if (tau_handle == NULL) 
3300 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3301 | 
3302 |   if (tau_handle == NULL) { 
3303 |     perror("Error opening library in dlopen call"); 
3304 |     return retval;
3305 |   } 
3307 |     if (cuTexRefCreate_h == NULL)
3308 | 	cuTexRefCreate_h = (cuTexRefCreate_p_h) dlsym(tau_handle,"cuTexRefCreate"); 
3309 |     if (cuTexRefCreate_h == NULL) {
3310 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3311 |       return retval;
3312 |     }
3325 |   CUresult retval;
3326 |   TAU_PROFILE_TIMER(t,"CUresult cuTexRefDestroy(CUtexref) C", "", CUDA_API);
3327 |   if (tau_handle == NULL) 
3328 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3329 | 
3330 |   if (tau_handle == NULL) { 
3331 |     perror("Error opening library in dlopen call"); 
3332 |     return retval;
3333 |   } 
3335 |     if (cuTexRefDestroy_h == NULL)
3336 | 	cuTexRefDestroy_h = (cuTexRefDestroy_p_h) dlsym(tau_handle,"cuTexRefDestroy"); 
3337 |     if (cuTexRefDestroy_h == NULL) {
3338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3339 |       return retval;
3340 |     }
3353 |   CUresult retval;
3354 |   TAU_PROFILE_TIMER(t,"CUresult cuSurfRefSetArray(CUsurfref, CUarray, unsigned int) C", "", CUDA_API);
3355 |   if (tau_handle == NULL) 
3356 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3357 | 
3358 |   if (tau_handle == NULL) { 
3359 |     perror("Error opening library in dlopen call"); 
3360 |     return retval;
3361 |   } 
3363 |     if (cuSurfRefSetArray_h == NULL)
3364 | 	cuSurfRefSetArray_h = (cuSurfRefSetArray_p_h) dlsym(tau_handle,"cuSurfRefSetArray"); 
3365 |     if (cuSurfRefSetArray_h == NULL) {
3366 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3367 |       return retval;
3368 |     }
3381 |   CUresult retval;
3382 |   TAU_PROFILE_TIMER(t,"CUresult cuSurfRefGetArray(CUarray *, CUsurfref) C", "", CUDA_API);
3383 |   if (tau_handle == NULL) 
3384 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3385 | 
3386 |   if (tau_handle == NULL) { 
3387 |     perror("Error opening library in dlopen call"); 
3388 |     return retval;
3389 |   } 
3391 |     if (cuSurfRefGetArray_h == NULL)
3392 | 	cuSurfRefGetArray_h = (cuSurfRefGetArray_p_h) dlsym(tau_handle,"cuSurfRefGetArray"); 
3393 |     if (cuSurfRefGetArray_h == NULL) {
3394 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3395 |       return retval;
3396 |     }
3409 |   CUresult retval;
3410 |   TAU_PROFILE_TIMER(t,"CUresult cuGraphicsUnregisterResource(CUgraphicsResource) C", "", CUDA_API);
3411 |   if (tau_handle == NULL) 
3412 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3413 | 
3414 |   if (tau_handle == NULL) { 
3415 |     perror("Error opening library in dlopen call"); 
3416 |     return retval;
3417 |   } 
3419 |     if (cuGraphicsUnregisterResource_h == NULL)
3420 | 	cuGraphicsUnregisterResource_h = (cuGraphicsUnregisterResource_p_h) dlsym(tau_handle,"cuGraphicsUnregisterResource"); 
3421 |     if (cuGraphicsUnregisterResource_h == NULL) {
3422 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3423 |       return retval;
3424 |     }
3437 |   CUresult retval;
3438 |   TAU_PROFILE_TIMER(t,"CUresult cuGraphicsSubResourceGetMappedArray(CUarray *, CUgraphicsResource, unsigned int, unsigned int) C", "", CUDA_API);
3439 |   if (tau_handle == NULL) 
3440 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3441 | 
3442 |   if (tau_handle == NULL) { 
3443 |     perror("Error opening library in dlopen call"); 
3444 |     return retval;
3445 |   } 
3447 |     if (cuGraphicsSubResourceGetMappedArray_h == NULL)
3448 | 	cuGraphicsSubResourceGetMappedArray_h = (cuGraphicsSubResourceGetMappedArray_p_h) dlsym(tau_handle,"cuGraphicsSubResourceGetMappedArray"); 
3449 |     if (cuGraphicsSubResourceGetMappedArray_h == NULL) {
3450 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3451 |       return retval;
3452 |     }
3465 |   CUresult retval;
3466 |   TAU_PROFILE_TIMER(t,"CUresult cuGraphicsResourceGetMappedPointer_v2(CUdeviceptr *, size_t *, CUgraphicsResource) C", "", CUDA_API);
3467 |   if (tau_handle == NULL) 
3468 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3469 | 
3470 |   if (tau_handle == NULL) { 
3471 |     perror("Error opening library in dlopen call"); 
3472 |     return retval;
3473 |   } 
3475 |     if (cuGraphicsResourceGetMappedPointer_v2_h == NULL)
3476 | 	cuGraphicsResourceGetMappedPointer_v2_h = (cuGraphicsResourceGetMappedPointer_v2_p_h) dlsym(tau_handle,"cuGraphicsResourceGetMappedPointer_v2"); 
3477 |     if (cuGraphicsResourceGetMappedPointer_v2_h == NULL) {
3478 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3479 |       return retval;
3480 |     }
3493 |   CUresult retval;
3494 |   TAU_PROFILE_TIMER(t,"CUresult cuGraphicsResourceSetMapFlags(CUgraphicsResource, unsigned int) C", "", CUDA_API);
3495 |   if (tau_handle == NULL) 
3496 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3497 | 
3498 |   if (tau_handle == NULL) { 
3499 |     perror("Error opening library in dlopen call"); 
3500 |     return retval;
3501 |   } 
3503 |     if (cuGraphicsResourceSetMapFlags_h == NULL)
3504 | 	cuGraphicsResourceSetMapFlags_h = (cuGraphicsResourceSetMapFlags_p_h) dlsym(tau_handle,"cuGraphicsResourceSetMapFlags"); 
3505 |     if (cuGraphicsResourceSetMapFlags_h == NULL) {
3506 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3507 |       return retval;
3508 |     }
3521 |   CUresult retval;
3522 |   TAU_PROFILE_TIMER(t,"CUresult cuGraphicsMapResources(unsigned int, CUgraphicsResource *, CUstream) C", "", CUDA_API);
3523 |   if (tau_handle == NULL) 
3524 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3525 | 
3526 |   if (tau_handle == NULL) { 
3527 |     perror("Error opening library in dlopen call"); 
3528 |     return retval;
3529 |   } 
3531 |     if (cuGraphicsMapResources_h == NULL)
3532 | 	cuGraphicsMapResources_h = (cuGraphicsMapResources_p_h) dlsym(tau_handle,"cuGraphicsMapResources"); 
3533 |     if (cuGraphicsMapResources_h == NULL) {
3534 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3535 |       return retval;
3536 |     }
3549 |   CUresult retval;
3550 |   TAU_PROFILE_TIMER(t,"CUresult cuGraphicsUnmapResources(unsigned int, CUgraphicsResource *, CUstream) C", "", CUDA_API);
3551 |   if (tau_handle == NULL) 
3552 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3553 | 
3554 |   if (tau_handle == NULL) { 
3555 |     perror("Error opening library in dlopen call"); 
3556 |     return retval;
3557 |   } 
3559 |     if (cuGraphicsUnmapResources_h == NULL)
3560 | 	cuGraphicsUnmapResources_h = (cuGraphicsUnmapResources_p_h) dlsym(tau_handle,"cuGraphicsUnmapResources"); 
3561 |     if (cuGraphicsUnmapResources_h == NULL) {
3562 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3563 |       return retval;
3564 |     }
3577 |   CUresult retval;
3578 |   TAU_PROFILE_TIMER(t,"CUresult cuGetExportTable(const void **, const CUuuid *) C", "", CUDA_API);
3579 |   if (tau_handle == NULL) 
3580 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3581 | 
3582 |   if (tau_handle == NULL) { 
3583 |     perror("Error opening library in dlopen call"); 
3584 |     return retval;
3585 |   } 
3587 |     if (cuGetExportTable_h == NULL)
3588 | 	cuGetExportTable_h = (cuGetExportTable_p_h) dlsym(tau_handle,"cuGetExportTable"); 
3589 |     if (cuGetExportTable_h == NULL) {
3590 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3591 |       return retval;
3592 |     }
{% endraw %}

```
### src/Profile/TauShmemSgiF.c

```c

{% raw %}
20 |   static shmem_addr_accessible__p_h shmem_addr_accessible__h = NULL;
21 |   TAU_PROFILE_TIMER(t,"void shmem_addr_accessible_(void *, int *)", "", TAU_USER);
22 |   if (tau_handle == NULL) 
23 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
24 | 
25 |   if (tau_handle == NULL) { 
26 |     perror("Error opening library in dlopen call"); 
27 |     return;
28 |   } 
30 |     if (shmem_addr_accessible__h == NULL)
31 | 	shmem_addr_accessible__h = (shmem_addr_accessible__p_h) dlsym(tau_handle,"shmem_addr_accessible_"); 
32 |     if (shmem_addr_accessible__h == NULL) {
33 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
34 |       return;
35 |     }
51 |   static shmem_barrier__p_h shmem_barrier__h = NULL;
52 |   TAU_PROFILE_TIMER(t,"void shmem_barrier_(int *, int *, int *, long *)", "", TAU_USER);
53 |   if (tau_handle == NULL) 
54 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
55 | 
56 |   if (tau_handle == NULL) { 
57 |     perror("Error opening library in dlopen call"); 
58 |     return;
59 |   } 
61 |     if (shmem_barrier__h == NULL)
62 | 	shmem_barrier__h = (shmem_barrier__p_h) dlsym(tau_handle,"shmem_barrier_"); 
63 |     if (shmem_barrier__h == NULL) {
64 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
65 |       return;
66 |     }
82 |   static shmem_barrier_all__p_h shmem_barrier_all__h = NULL;
83 |   TAU_PROFILE_TIMER(t,"void shmem_barrier_all_()", "", TAU_USER);
84 |   if (tau_handle == NULL) 
85 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
86 | 
87 |   if (tau_handle == NULL) { 
88 |     perror("Error opening library in dlopen call"); 
89 |     return;
90 |   } 
92 |     if (shmem_barrier_all__h == NULL)
93 | 	shmem_barrier_all__h = (shmem_barrier_all__p_h) dlsym(tau_handle,"shmem_barrier_all_"); 
94 |     if (shmem_barrier_all__h == NULL) {
95 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
96 |       return;
97 |     }
113 |   static shmem_barrier_ps__p_h shmem_barrier_ps__h = NULL;
114 |   TAU_PROFILE_TIMER(t,"void shmem_barrier_ps_(int *, int *, int *, long *)", "", TAU_USER);
115 |   if (tau_handle == NULL) 
116 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
117 | 
118 |   if (tau_handle == NULL) { 
119 |     perror("Error opening library in dlopen call"); 
120 |     return;
121 |   } 
123 |     if (shmem_barrier_ps__h == NULL)
124 | 	shmem_barrier_ps__h = (shmem_barrier_ps__p_h) dlsym(tau_handle,"shmem_barrier_ps_"); 
125 |     if (shmem_barrier_ps__h == NULL) {
126 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
127 |       return;
128 |     }
144 |   static shmem_broadcast32__p_h shmem_broadcast32__h = NULL;
145 |   TAU_PROFILE_TIMER(t,"void shmem_broadcast32_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
146 |   if (tau_handle == NULL) 
147 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
148 | 
149 |   if (tau_handle == NULL) { 
150 |     perror("Error opening library in dlopen call"); 
151 |     return;
152 |   } 
154 |     if (shmem_broadcast32__h == NULL)
155 | 	shmem_broadcast32__h = (shmem_broadcast32__p_h) dlsym(tau_handle,"shmem_broadcast32_"); 
156 |     if (shmem_broadcast32__h == NULL) {
157 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
158 |       return;
159 |     }
175 |   static shmem_broadcast4__p_h shmem_broadcast4__h = NULL;
176 |   TAU_PROFILE_TIMER(t,"void shmem_broadcast4_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
177 |   if (tau_handle == NULL) 
178 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
179 | 
180 |   if (tau_handle == NULL) { 
181 |     perror("Error opening library in dlopen call"); 
182 |     return;
183 |   } 
185 |     if (shmem_broadcast4__h == NULL)
186 | 	shmem_broadcast4__h = (shmem_broadcast4__p_h) dlsym(tau_handle,"shmem_broadcast4_"); 
187 |     if (shmem_broadcast4__h == NULL) {
188 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
189 |       return;
190 |     }
206 |   static shmem_broadcast64__p_h shmem_broadcast64__h = NULL;
207 |   TAU_PROFILE_TIMER(t,"void shmem_broadcast64_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
208 |   if (tau_handle == NULL) 
209 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
210 | 
211 |   if (tau_handle == NULL) { 
212 |     perror("Error opening library in dlopen call"); 
213 |     return;
214 |   } 
216 |     if (shmem_broadcast64__h == NULL)
217 | 	shmem_broadcast64__h = (shmem_broadcast64__p_h) dlsym(tau_handle,"shmem_broadcast64_"); 
218 |     if (shmem_broadcast64__h == NULL) {
219 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
220 |       return;
221 |     }
237 |   static shmem_broadcast8__p_h shmem_broadcast8__h = NULL;
238 |   TAU_PROFILE_TIMER(t,"void shmem_broadcast8_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
239 |   if (tau_handle == NULL) 
240 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
241 | 
242 |   if (tau_handle == NULL) { 
243 |     perror("Error opening library in dlopen call"); 
244 |     return;
245 |   } 
247 |     if (shmem_broadcast8__h == NULL)
248 | 	shmem_broadcast8__h = (shmem_broadcast8__p_h) dlsym(tau_handle,"shmem_broadcast8_"); 
249 |     if (shmem_broadcast8__h == NULL) {
250 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
251 |       return;
252 |     }
268 |   static shmem_character_get__p_h shmem_character_get__h = NULL;
269 |   TAU_PROFILE_TIMER(t,"void shmem_character_get_(void *, void *, int *, int *)", "", TAU_USER);
270 |   if (tau_handle == NULL) 
271 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
272 | 
273 |   if (tau_handle == NULL) { 
274 |     perror("Error opening library in dlopen call"); 
275 |     return;
276 |   } 
278 |     if (shmem_character_get__h == NULL)
279 | 	shmem_character_get__h = (shmem_character_get__p_h) dlsym(tau_handle,"shmem_character_get_"); 
280 |     if (shmem_character_get__h == NULL) {
281 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
282 |       return;
283 |     }
301 |   static shmem_character_put__p_h shmem_character_put__h = NULL;
302 |   TAU_PROFILE_TIMER(t,"void shmem_character_put_(void *, void *, int *, int *)", "", TAU_USER);
303 |   if (tau_handle == NULL) 
304 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
305 | 
306 |   if (tau_handle == NULL) { 
307 |     perror("Error opening library in dlopen call"); 
308 |     return;
309 |   } 
311 |     if (shmem_character_put__h == NULL)
312 | 	shmem_character_put__h = (shmem_character_put__p_h) dlsym(tau_handle,"shmem_character_put_"); 
313 |     if (shmem_character_put__h == NULL) {
314 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
315 |       return;
316 |     }
334 |   static shmem_clear_cache_inv__p_h shmem_clear_cache_inv__h = NULL;
335 |   TAU_PROFILE_TIMER(t,"void shmem_clear_cache_inv_()", "", TAU_USER);
336 |   if (tau_handle == NULL) 
337 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
338 | 
339 |   if (tau_handle == NULL) { 
340 |     perror("Error opening library in dlopen call"); 
341 |     return;
342 |   } 
344 |     if (shmem_clear_cache_inv__h == NULL)
345 | 	shmem_clear_cache_inv__h = (shmem_clear_cache_inv__p_h) dlsym(tau_handle,"shmem_clear_cache_inv_"); 
346 |     if (shmem_clear_cache_inv__h == NULL) {
347 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
348 |       return;
349 |     }
365 |   static shmem_clear_cache_line_inv__p_h shmem_clear_cache_line_inv__h = NULL;
366 |   TAU_PROFILE_TIMER(t,"void shmem_clear_cache_line_inv_(void *)", "", TAU_USER);
367 |   if (tau_handle == NULL) 
368 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
369 | 
370 |   if (tau_handle == NULL) { 
371 |     perror("Error opening library in dlopen call"); 
372 |     return;
373 |   } 
375 |     if (shmem_clear_cache_line_inv__h == NULL)
376 | 	shmem_clear_cache_line_inv__h = (shmem_clear_cache_line_inv__p_h) dlsym(tau_handle,"shmem_clear_cache_line_inv_"); 
377 |     if (shmem_clear_cache_line_inv__h == NULL) {
378 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
379 |       return;
380 |     }
396 |   static shmem_clear_lock__p_h shmem_clear_lock__h = NULL;
397 |   TAU_PROFILE_TIMER(t,"void shmem_clear_lock_(long *)", "", TAU_USER);
398 |   if (tau_handle == NULL) 
399 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
400 | 
401 |   if (tau_handle == NULL) { 
402 |     perror("Error opening library in dlopen call"); 
403 |     return;
404 |   } 
406 |     if (shmem_clear_lock__h == NULL)
407 | 	shmem_clear_lock__h = (shmem_clear_lock__p_h) dlsym(tau_handle,"shmem_clear_lock_"); 
408 |     if (shmem_clear_lock__h == NULL) {
409 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
410 |       return;
411 |     }
427 |   static shmem_collect4__p_h shmem_collect4__h = NULL;
428 |   TAU_PROFILE_TIMER(t,"void shmem_collect4_(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
429 |   if (tau_handle == NULL) 
430 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
431 | 
432 |   if (tau_handle == NULL) { 
433 |     perror("Error opening library in dlopen call"); 
434 |     return;
435 |   } 
437 |     if (shmem_collect4__h == NULL)
438 | 	shmem_collect4__h = (shmem_collect4__p_h) dlsym(tau_handle,"shmem_collect4_"); 
439 |     if (shmem_collect4__h == NULL) {
440 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
441 |       return;
442 |     }
458 |   static shmem_collect64__p_h shmem_collect64__h = NULL;
459 |   TAU_PROFILE_TIMER(t,"void shmem_collect64_(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
460 |   if (tau_handle == NULL) 
461 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
462 | 
463 |   if (tau_handle == NULL) { 
464 |     perror("Error opening library in dlopen call"); 
465 |     return;
466 |   } 
468 |     if (shmem_collect64__h == NULL)
469 | 	shmem_collect64__h = (shmem_collect64__p_h) dlsym(tau_handle,"shmem_collect64_"); 
470 |     if (shmem_collect64__h == NULL) {
471 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
472 |       return;
473 |     }
489 |   static shmem_collect8__p_h shmem_collect8__h = NULL;
490 |   TAU_PROFILE_TIMER(t,"void shmem_collect8_(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
491 |   if (tau_handle == NULL) 
492 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
493 | 
494 |   if (tau_handle == NULL) { 
495 |     perror("Error opening library in dlopen call"); 
496 |     return;
497 |   } 
499 |     if (shmem_collect8__h == NULL)
500 | 	shmem_collect8__h = (shmem_collect8__p_h) dlsym(tau_handle,"shmem_collect8_"); 
501 |     if (shmem_collect8__h == NULL) {
502 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
503 |       return;
504 |     }
520 |   static shmem_comp4_prod_to_all__p_h shmem_comp4_prod_to_all__h = NULL;
521 |   TAU_PROFILE_TIMER(t,"void shmem_comp4_prod_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
522 |   if (tau_handle == NULL) 
523 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
524 | 
525 |   if (tau_handle == NULL) { 
526 |     perror("Error opening library in dlopen call"); 
527 |     return;
528 |   } 
530 |     if (shmem_comp4_prod_to_all__h == NULL)
531 | 	shmem_comp4_prod_to_all__h = (shmem_comp4_prod_to_all__p_h) dlsym(tau_handle,"shmem_comp4_prod_to_all_"); 
532 |     if (shmem_comp4_prod_to_all__h == NULL) {
533 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
534 |       return;
535 |     }
551 |   static shmem_comp4_sum_to_all__p_h shmem_comp4_sum_to_all__h = NULL;
552 |   TAU_PROFILE_TIMER(t,"void shmem_comp4_sum_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
553 |   if (tau_handle == NULL) 
554 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
555 | 
556 |   if (tau_handle == NULL) { 
557 |     perror("Error opening library in dlopen call"); 
558 |     return;
559 |   } 
561 |     if (shmem_comp4_sum_to_all__h == NULL)
562 | 	shmem_comp4_sum_to_all__h = (shmem_comp4_sum_to_all__p_h) dlsym(tau_handle,"shmem_comp4_sum_to_all_"); 
563 |     if (shmem_comp4_sum_to_all__h == NULL) {
564 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
565 |       return;
566 |     }
582 |   static shmem_comp8_prod_to_all__p_h shmem_comp8_prod_to_all__h = NULL;
583 |   TAU_PROFILE_TIMER(t,"void shmem_comp8_prod_to_all_(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
584 |   if (tau_handle == NULL) 
585 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
586 | 
587 |   if (tau_handle == NULL) { 
588 |     perror("Error opening library in dlopen call"); 
589 |     return;
590 |   } 
592 |     if (shmem_comp8_prod_to_all__h == NULL)
593 | 	shmem_comp8_prod_to_all__h = (shmem_comp8_prod_to_all__p_h) dlsym(tau_handle,"shmem_comp8_prod_to_all_"); 
594 |     if (shmem_comp8_prod_to_all__h == NULL) {
595 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
596 |       return;
597 |     }
613 |   static shmem_comp8_sum_to_all__p_h shmem_comp8_sum_to_all__h = NULL;
614 |   TAU_PROFILE_TIMER(t,"void shmem_comp8_sum_to_all_(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
615 |   if (tau_handle == NULL) 
616 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
617 | 
618 |   if (tau_handle == NULL) { 
619 |     perror("Error opening library in dlopen call"); 
620 |     return;
621 |   } 
623 |     if (shmem_comp8_sum_to_all__h == NULL)
624 | 	shmem_comp8_sum_to_all__h = (shmem_comp8_sum_to_all__p_h) dlsym(tau_handle,"shmem_comp8_sum_to_all_"); 
625 |     if (shmem_comp8_sum_to_all__h == NULL) {
626 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
627 |       return;
628 |     }
644 |   static shmem_complex_get__p_h shmem_complex_get__h = NULL;
645 |   TAU_PROFILE_TIMER(t,"void shmem_complex_get_(void *, void *, int *, int *)", "", TAU_USER);
646 |   if (tau_handle == NULL) 
647 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
648 | 
649 |   if (tau_handle == NULL) { 
650 |     perror("Error opening library in dlopen call"); 
651 |     return;
652 |   } 
654 |     if (shmem_complex_get__h == NULL)
655 | 	shmem_complex_get__h = (shmem_complex_get__p_h) dlsym(tau_handle,"shmem_complex_get_"); 
656 |     if (shmem_complex_get__h == NULL) {
657 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
658 |       return;
659 |     }
677 |   static shmem_complex_iget__p_h shmem_complex_iget__h = NULL;
678 |   TAU_PROFILE_TIMER(t,"void shmem_complex_iget_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
679 |   if (tau_handle == NULL) 
680 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
681 | 
682 |   if (tau_handle == NULL) { 
683 |     perror("Error opening library in dlopen call"); 
684 |     return;
685 |   } 
687 |     if (shmem_complex_iget__h == NULL)
688 | 	shmem_complex_iget__h = (shmem_complex_iget__p_h) dlsym(tau_handle,"shmem_complex_iget_"); 
689 |     if (shmem_complex_iget__h == NULL) {
690 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
691 |       return;
692 |     }
710 |   static shmem_complex_iput__p_h shmem_complex_iput__h = NULL;
711 |   TAU_PROFILE_TIMER(t,"void shmem_complex_iput_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
712 |   if (tau_handle == NULL) 
713 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
714 | 
715 |   if (tau_handle == NULL) { 
716 |     perror("Error opening library in dlopen call"); 
717 |     return;
718 |   } 
720 |     if (shmem_complex_iput__h == NULL)
721 | 	shmem_complex_iput__h = (shmem_complex_iput__p_h) dlsym(tau_handle,"shmem_complex_iput_"); 
722 |     if (shmem_complex_iput__h == NULL) {
723 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
724 |       return;
725 |     }
743 |   static shmem_complex_put__p_h shmem_complex_put__h = NULL;
744 |   TAU_PROFILE_TIMER(t,"void shmem_complex_put_(void *, void *, int *, int *)", "", TAU_USER);
745 |   if (tau_handle == NULL) 
746 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
747 | 
748 |   if (tau_handle == NULL) { 
749 |     perror("Error opening library in dlopen call"); 
750 |     return;
751 |   } 
753 |     if (shmem_complex_put__h == NULL)
754 | 	shmem_complex_put__h = (shmem_complex_put__p_h) dlsym(tau_handle,"shmem_complex_put_"); 
755 |     if (shmem_complex_put__h == NULL) {
756 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
757 |       return;
758 |     }
776 |   static shmem_double_get__p_h shmem_double_get__h = NULL;
777 |   TAU_PROFILE_TIMER(t,"void shmem_double_get_(void *, void *, int *, int *)", "", TAU_USER);
778 |   if (tau_handle == NULL) 
779 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
780 | 
781 |   if (tau_handle == NULL) { 
782 |     perror("Error opening library in dlopen call"); 
783 |     return;
784 |   } 
786 |     if (shmem_double_get__h == NULL)
787 | 	shmem_double_get__h = (shmem_double_get__p_h) dlsym(tau_handle,"shmem_double_get_"); 
788 |     if (shmem_double_get__h == NULL) {
789 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
790 |       return;
791 |     }
809 |   static shmem_double_iget__p_h shmem_double_iget__h = NULL;
810 |   TAU_PROFILE_TIMER(t,"void shmem_double_iget_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
811 |   if (tau_handle == NULL) 
812 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
813 | 
814 |   if (tau_handle == NULL) { 
815 |     perror("Error opening library in dlopen call"); 
816 |     return;
817 |   } 
819 |     if (shmem_double_iget__h == NULL)
820 | 	shmem_double_iget__h = (shmem_double_iget__p_h) dlsym(tau_handle,"shmem_double_iget_"); 
821 |     if (shmem_double_iget__h == NULL) {
822 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
823 |       return;
824 |     }
842 |   static shmem_double_iput__p_h shmem_double_iput__h = NULL;
843 |   TAU_PROFILE_TIMER(t,"void shmem_double_iput_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
844 |   if (tau_handle == NULL) 
845 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
846 | 
847 |   if (tau_handle == NULL) { 
848 |     perror("Error opening library in dlopen call"); 
849 |     return;
850 |   } 
852 |     if (shmem_double_iput__h == NULL)
853 | 	shmem_double_iput__h = (shmem_double_iput__p_h) dlsym(tau_handle,"shmem_double_iput_"); 
854 |     if (shmem_double_iput__h == NULL) {
855 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
856 |       return;
857 |     }
875 |   static shmem_double_put__p_h shmem_double_put__h = NULL;
876 |   TAU_PROFILE_TIMER(t,"void shmem_double_put_(void *, void *, int *, int *)", "", TAU_USER);
877 |   if (tau_handle == NULL) 
878 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
879 | 
880 |   if (tau_handle == NULL) { 
881 |     perror("Error opening library in dlopen call"); 
882 |     return;
883 |   } 
885 |     if (shmem_double_put__h == NULL)
886 | 	shmem_double_put__h = (shmem_double_put__p_h) dlsym(tau_handle,"shmem_double_put_"); 
887 |     if (shmem_double_put__h == NULL) {
888 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
889 |       return;
890 |     }
908 |   static shmem_fcollect32__p_h shmem_fcollect32__h = NULL;
909 |   TAU_PROFILE_TIMER(t,"void shmem_fcollect32_(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
910 |   if (tau_handle == NULL) 
911 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
912 | 
913 |   if (tau_handle == NULL) { 
914 |     perror("Error opening library in dlopen call"); 
915 |     return;
916 |   } 
918 |     if (shmem_fcollect32__h == NULL)
919 | 	shmem_fcollect32__h = (shmem_fcollect32__p_h) dlsym(tau_handle,"shmem_fcollect32_"); 
920 |     if (shmem_fcollect32__h == NULL) {
921 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
922 |       return;
923 |     }
939 |   static shmem_fcollect4__p_h shmem_fcollect4__h = NULL;
940 |   TAU_PROFILE_TIMER(t,"void shmem_fcollect4_(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
941 |   if (tau_handle == NULL) 
942 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
943 | 
944 |   if (tau_handle == NULL) { 
945 |     perror("Error opening library in dlopen call"); 
946 |     return;
947 |   } 
949 |     if (shmem_fcollect4__h == NULL)
950 | 	shmem_fcollect4__h = (shmem_fcollect4__p_h) dlsym(tau_handle,"shmem_fcollect4_"); 
951 |     if (shmem_fcollect4__h == NULL) {
952 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
953 |       return;
954 |     }
970 |   static shmem_fcollect64__p_h shmem_fcollect64__h = NULL;
971 |   TAU_PROFILE_TIMER(t,"void shmem_fcollect64_(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
972 |   if (tau_handle == NULL) 
973 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
974 | 
975 |   if (tau_handle == NULL) { 
976 |     perror("Error opening library in dlopen call"); 
977 |     return;
978 |   } 
980 |     if (shmem_fcollect64__h == NULL)
981 | 	shmem_fcollect64__h = (shmem_fcollect64__p_h) dlsym(tau_handle,"shmem_fcollect64_"); 
982 |     if (shmem_fcollect64__h == NULL) {
983 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
984 |       return;
985 |     }
1001 |   static shmem_fcollect8__p_h shmem_fcollect8__h = NULL;
1002 |   TAU_PROFILE_TIMER(t,"void shmem_fcollect8_(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
1003 |   if (tau_handle == NULL) 
1004 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1005 | 
1006 |   if (tau_handle == NULL) { 
1007 |     perror("Error opening library in dlopen call"); 
1008 |     return;
1009 |   } 
1011 |     if (shmem_fcollect8__h == NULL)
1012 | 	shmem_fcollect8__h = (shmem_fcollect8__p_h) dlsym(tau_handle,"shmem_fcollect8_"); 
1013 |     if (shmem_fcollect8__h == NULL) {
1014 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1015 |       return;
1016 |     }
1032 |   static shmem_fence__p_h shmem_fence__h = NULL;
1033 |   TAU_PROFILE_TIMER(t,"void shmem_fence_()", "", TAU_USER);
1034 |   if (tau_handle == NULL) 
1035 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1036 | 
1037 |   if (tau_handle == NULL) { 
1038 |     perror("Error opening library in dlopen call"); 
1039 |     return;
1040 |   } 
1042 |     if (shmem_fence__h == NULL)
1043 | 	shmem_fence__h = (shmem_fence__p_h) dlsym(tau_handle,"shmem_fence_"); 
1044 |     if (shmem_fence__h == NULL) {
1045 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1046 |       return;
1047 |     }
1063 |   static shmem_get128__p_h shmem_get128__h = NULL;
1064 |   TAU_PROFILE_TIMER(t,"void shmem_get128_(void *, void *, int *, int *)", "", TAU_USER);
1065 |   if (tau_handle == NULL) 
1066 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1067 | 
1068 |   if (tau_handle == NULL) { 
1069 |     perror("Error opening library in dlopen call"); 
1070 |     return;
1071 |   } 
1073 |     if (shmem_get128__h == NULL)
1074 | 	shmem_get128__h = (shmem_get128__p_h) dlsym(tau_handle,"shmem_get128_"); 
1075 |     if (shmem_get128__h == NULL) {
1076 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1077 |       return;
1078 |     }
1096 |   static shmem_get16__p_h shmem_get16__h = NULL;
1097 |   TAU_PROFILE_TIMER(t,"void shmem_get16_(void *, void *, int *, int *)", "", TAU_USER);
1098 |   if (tau_handle == NULL) 
1099 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1100 | 
1101 |   if (tau_handle == NULL) { 
1102 |     perror("Error opening library in dlopen call"); 
1103 |     return;
1104 |   } 
1106 |     if (shmem_get16__h == NULL)
1107 | 	shmem_get16__h = (shmem_get16__p_h) dlsym(tau_handle,"shmem_get16_"); 
1108 |     if (shmem_get16__h == NULL) {
1109 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1110 |       return;
1111 |     }
1129 |   static shmem_get32__p_h shmem_get32__h = NULL;
1130 |   TAU_PROFILE_TIMER(t,"void shmem_get32_(void *, void *, int *, int *)", "", TAU_USER);
1131 |   if (tau_handle == NULL) 
1132 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1133 | 
1134 |   if (tau_handle == NULL) { 
1135 |     perror("Error opening library in dlopen call"); 
1136 |     return;
1137 |   } 
1139 |     if (shmem_get32__h == NULL)
1140 | 	shmem_get32__h = (shmem_get32__p_h) dlsym(tau_handle,"shmem_get32_"); 
1141 |     if (shmem_get32__h == NULL) {
1142 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1143 |       return;
1144 |     }
1162 |   static shmem_get4__p_h shmem_get4__h = NULL;
1163 |   TAU_PROFILE_TIMER(t,"void shmem_get4_(void *, void *, int *, int *)", "", TAU_USER);
1164 |   if (tau_handle == NULL) 
1165 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1166 | 
1167 |   if (tau_handle == NULL) { 
1168 |     perror("Error opening library in dlopen call"); 
1169 |     return;
1170 |   } 
1172 |     if (shmem_get4__h == NULL)
1173 | 	shmem_get4__h = (shmem_get4__p_h) dlsym(tau_handle,"shmem_get4_"); 
1174 |     if (shmem_get4__h == NULL) {
1175 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1176 |       return;
1177 |     }
1195 |   static shmem_get64__p_h shmem_get64__h = NULL;
1196 |   TAU_PROFILE_TIMER(t,"void shmem_get64_(void *, void *, int *, int *)", "", TAU_USER);
1197 |   if (tau_handle == NULL) 
1198 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1199 | 
1200 |   if (tau_handle == NULL) { 
1201 |     perror("Error opening library in dlopen call"); 
1202 |     return;
1203 |   } 
1205 |     if (shmem_get64__h == NULL)
1206 | 	shmem_get64__h = (shmem_get64__p_h) dlsym(tau_handle,"shmem_get64_"); 
1207 |     if (shmem_get64__h == NULL) {
1208 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1209 |       return;
1210 |     }
1228 |   static shmem_get8__p_h shmem_get8__h = NULL;
1229 |   TAU_PROFILE_TIMER(t,"void shmem_get8_(void *, void *, int *, int *)", "", TAU_USER);
1230 |   if (tau_handle == NULL) 
1231 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1232 | 
1233 |   if (tau_handle == NULL) { 
1234 |     perror("Error opening library in dlopen call"); 
1235 |     return;
1236 |   } 
1238 |     if (shmem_get8__h == NULL)
1239 | 	shmem_get8__h = (shmem_get8__p_h) dlsym(tau_handle,"shmem_get8_"); 
1240 |     if (shmem_get8__h == NULL) {
1241 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1242 |       return;
1243 |     }
1261 |   static shmem_getmem__p_h shmem_getmem__h = NULL;
1262 |   TAU_PROFILE_TIMER(t,"void shmem_getmem_(void *, void *, int *, int *)", "", TAU_USER);
1263 |   if (tau_handle == NULL) 
1264 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1265 | 
1266 |   if (tau_handle == NULL) { 
1267 |     perror("Error opening library in dlopen call"); 
1268 |     return;
1269 |   } 
1271 |     if (shmem_getmem__h == NULL)
1272 | 	shmem_getmem__h = (shmem_getmem__p_h) dlsym(tau_handle,"shmem_getmem_"); 
1273 |     if (shmem_getmem__h == NULL) {
1274 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1275 |       return;
1276 |     }
1294 |   static shmem_group_create_strided__p_h shmem_group_create_strided__h = NULL;
1295 |   TAU_PROFILE_TIMER(t,"void shmem_group_create_strided_(int *, int *, int *, int *, int *, int *)", "", TAU_USER);
1296 |   if (tau_handle == NULL) 
1297 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1298 | 
1299 |   if (tau_handle == NULL) { 
1300 |     perror("Error opening library in dlopen call"); 
1301 |     return;
1302 |   } 
1304 |     if (shmem_group_create_strided__h == NULL)
1305 | 	shmem_group_create_strided__h = (shmem_group_create_strided__p_h) dlsym(tau_handle,"shmem_group_create_strided_"); 
1306 |     if (shmem_group_create_strided__h == NULL) {
1307 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1308 |       return;
1309 |     }
1325 |   static shmem_group_delete__p_h shmem_group_delete__h = NULL;
1326 |   TAU_PROFILE_TIMER(t,"void shmem_group_delete_(int *)", "", TAU_USER);
1327 |   if (tau_handle == NULL) 
1328 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1329 | 
1330 |   if (tau_handle == NULL) { 
1331 |     perror("Error opening library in dlopen call"); 
1332 |     return;
1333 |   } 
1335 |     if (shmem_group_delete__h == NULL)
1336 | 	shmem_group_delete__h = (shmem_group_delete__p_h) dlsym(tau_handle,"shmem_group_delete_"); 
1337 |     if (shmem_group_delete__h == NULL) {
1338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1339 |       return;
1340 |     }
1356 |   static shmem_iget128__p_h shmem_iget128__h = NULL;
1357 |   TAU_PROFILE_TIMER(t,"void shmem_iget128_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
1358 |   if (tau_handle == NULL) 
1359 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1360 | 
1361 |   if (tau_handle == NULL) { 
1362 |     perror("Error opening library in dlopen call"); 
1363 |     return;
1364 |   } 
1366 |     if (shmem_iget128__h == NULL)
1367 | 	shmem_iget128__h = (shmem_iget128__p_h) dlsym(tau_handle,"shmem_iget128_"); 
1368 |     if (shmem_iget128__h == NULL) {
1369 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1370 |       return;
1371 |     }
1389 |   static shmem_iget16__p_h shmem_iget16__h = NULL;
1390 |   TAU_PROFILE_TIMER(t,"void shmem_iget16_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
1391 |   if (tau_handle == NULL) 
1392 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1393 | 
1394 |   if (tau_handle == NULL) { 
1395 |     perror("Error opening library in dlopen call"); 
1396 |     return;
1397 |   } 
1399 |     if (shmem_iget16__h == NULL)
1400 | 	shmem_iget16__h = (shmem_iget16__p_h) dlsym(tau_handle,"shmem_iget16_"); 
1401 |     if (shmem_iget16__h == NULL) {
1402 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1403 |       return;
1404 |     }
1422 |   static shmem_iget32__p_h shmem_iget32__h = NULL;
1423 |   TAU_PROFILE_TIMER(t,"void shmem_iget32_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
1424 |   if (tau_handle == NULL) 
1425 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1426 | 
1427 |   if (tau_handle == NULL) { 
1428 |     perror("Error opening library in dlopen call"); 
1429 |     return;
1430 |   } 
1432 |     if (shmem_iget32__h == NULL)
1433 | 	shmem_iget32__h = (shmem_iget32__p_h) dlsym(tau_handle,"shmem_iget32_"); 
1434 |     if (shmem_iget32__h == NULL) {
1435 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1436 |       return;
1437 |     }
1455 |   static shmem_iget4__p_h shmem_iget4__h = NULL;
1456 |   TAU_PROFILE_TIMER(t,"void shmem_iget4_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
1457 |   if (tau_handle == NULL) 
1458 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1459 | 
1460 |   if (tau_handle == NULL) { 
1461 |     perror("Error opening library in dlopen call"); 
1462 |     return;
1463 |   } 
1465 |     if (shmem_iget4__h == NULL)
1466 | 	shmem_iget4__h = (shmem_iget4__p_h) dlsym(tau_handle,"shmem_iget4_"); 
1467 |     if (shmem_iget4__h == NULL) {
1468 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1469 |       return;
1470 |     }
1488 |   static shmem_iget64__p_h shmem_iget64__h = NULL;
1489 |   TAU_PROFILE_TIMER(t,"void shmem_iget64_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
1490 |   if (tau_handle == NULL) 
1491 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1492 | 
1493 |   if (tau_handle == NULL) { 
1494 |     perror("Error opening library in dlopen call"); 
1495 |     return;
1496 |   } 
1498 |     if (shmem_iget64__h == NULL)
1499 | 	shmem_iget64__h = (shmem_iget64__p_h) dlsym(tau_handle,"shmem_iget64_"); 
1500 |     if (shmem_iget64__h == NULL) {
1501 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1502 |       return;
1503 |     }
1521 |   static shmem_iget8__p_h shmem_iget8__h = NULL;
1522 |   TAU_PROFILE_TIMER(t,"void shmem_iget8_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
1523 |   if (tau_handle == NULL) 
1524 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1525 | 
1526 |   if (tau_handle == NULL) { 
1527 |     perror("Error opening library in dlopen call"); 
1528 |     return;
1529 |   } 
1531 |     if (shmem_iget8__h == NULL)
1532 | 	shmem_iget8__h = (shmem_iget8__p_h) dlsym(tau_handle,"shmem_iget8_"); 
1533 |     if (shmem_iget8__h == NULL) {
1534 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1535 |       return;
1536 |     }
1554 |   static shmem_int2_and_to_all__p_h shmem_int2_and_to_all__h = NULL;
1555 |   TAU_PROFILE_TIMER(t,"void shmem_int2_and_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
1556 |   if (tau_handle == NULL) 
1557 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1558 | 
1559 |   if (tau_handle == NULL) { 
1560 |     perror("Error opening library in dlopen call"); 
1561 |     return;
1562 |   } 
1564 |     if (shmem_int2_and_to_all__h == NULL)
1565 | 	shmem_int2_and_to_all__h = (shmem_int2_and_to_all__p_h) dlsym(tau_handle,"shmem_int2_and_to_all_"); 
1566 |     if (shmem_int2_and_to_all__h == NULL) {
1567 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1568 |       return;
1569 |     }
1585 |   static shmem_int2_max_to_all__p_h shmem_int2_max_to_all__h = NULL;
1586 |   TAU_PROFILE_TIMER(t,"void shmem_int2_max_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
1587 |   if (tau_handle == NULL) 
1588 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1589 | 
1590 |   if (tau_handle == NULL) { 
1591 |     perror("Error opening library in dlopen call"); 
1592 |     return;
1593 |   } 
1595 |     if (shmem_int2_max_to_all__h == NULL)
1596 | 	shmem_int2_max_to_all__h = (shmem_int2_max_to_all__p_h) dlsym(tau_handle,"shmem_int2_max_to_all_"); 
1597 |     if (shmem_int2_max_to_all__h == NULL) {
1598 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1599 |       return;
1600 |     }
1616 |   static shmem_int2_min_to_all__p_h shmem_int2_min_to_all__h = NULL;
1617 |   TAU_PROFILE_TIMER(t,"void shmem_int2_min_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
1618 |   if (tau_handle == NULL) 
1619 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1620 | 
1621 |   if (tau_handle == NULL) { 
1622 |     perror("Error opening library in dlopen call"); 
1623 |     return;
1624 |   } 
1626 |     if (shmem_int2_min_to_all__h == NULL)
1627 | 	shmem_int2_min_to_all__h = (shmem_int2_min_to_all__p_h) dlsym(tau_handle,"shmem_int2_min_to_all_"); 
1628 |     if (shmem_int2_min_to_all__h == NULL) {
1629 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1630 |       return;
1631 |     }
1647 |   static shmem_int2_or_to_all__p_h shmem_int2_or_to_all__h = NULL;
1648 |   TAU_PROFILE_TIMER(t,"void shmem_int2_or_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
1649 |   if (tau_handle == NULL) 
1650 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1651 | 
1652 |   if (tau_handle == NULL) { 
1653 |     perror("Error opening library in dlopen call"); 
1654 |     return;
1655 |   } 
1657 |     if (shmem_int2_or_to_all__h == NULL)
1658 | 	shmem_int2_or_to_all__h = (shmem_int2_or_to_all__p_h) dlsym(tau_handle,"shmem_int2_or_to_all_"); 
1659 |     if (shmem_int2_or_to_all__h == NULL) {
1660 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1661 |       return;
1662 |     }
1678 |   static shmem_int2_prod_to_all__p_h shmem_int2_prod_to_all__h = NULL;
1679 |   TAU_PROFILE_TIMER(t,"void shmem_int2_prod_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
1680 |   if (tau_handle == NULL) 
1681 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1682 | 
1683 |   if (tau_handle == NULL) { 
1684 |     perror("Error opening library in dlopen call"); 
1685 |     return;
1686 |   } 
1688 |     if (shmem_int2_prod_to_all__h == NULL)
1689 | 	shmem_int2_prod_to_all__h = (shmem_int2_prod_to_all__p_h) dlsym(tau_handle,"shmem_int2_prod_to_all_"); 
1690 |     if (shmem_int2_prod_to_all__h == NULL) {
1691 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1692 |       return;
1693 |     }
1709 |   static shmem_int2_sum_to_all__p_h shmem_int2_sum_to_all__h = NULL;
1710 |   TAU_PROFILE_TIMER(t,"void shmem_int2_sum_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
1711 |   if (tau_handle == NULL) 
1712 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1713 | 
1714 |   if (tau_handle == NULL) { 
1715 |     perror("Error opening library in dlopen call"); 
1716 |     return;
1717 |   } 
1719 |     if (shmem_int2_sum_to_all__h == NULL)
1720 | 	shmem_int2_sum_to_all__h = (shmem_int2_sum_to_all__p_h) dlsym(tau_handle,"shmem_int2_sum_to_all_"); 
1721 |     if (shmem_int2_sum_to_all__h == NULL) {
1722 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1723 |       return;
1724 |     }
1740 |   static shmem_int2_xor_to_all__p_h shmem_int2_xor_to_all__h = NULL;
1741 |   TAU_PROFILE_TIMER(t,"void shmem_int2_xor_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
1742 |   if (tau_handle == NULL) 
1743 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1744 | 
1745 |   if (tau_handle == NULL) { 
1746 |     perror("Error opening library in dlopen call"); 
1747 |     return;
1748 |   } 
1750 |     if (shmem_int2_xor_to_all__h == NULL)
1751 | 	shmem_int2_xor_to_all__h = (shmem_int2_xor_to_all__p_h) dlsym(tau_handle,"shmem_int2_xor_to_all_"); 
1752 |     if (shmem_int2_xor_to_all__h == NULL) {
1753 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1754 |       return;
1755 |     }
1771 |   static shmem_int4_add__p_h shmem_int4_add__h = NULL;
1772 |   TAU_PROFILE_TIMER(t,"void shmem_int4_add_(void *, int *, int *)", "", TAU_USER);
1773 |   if (tau_handle == NULL) 
1774 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1775 | 
1776 |   if (tau_handle == NULL) { 
1777 |     perror("Error opening library in dlopen call"); 
1778 |     return;
1779 |   } 
1781 |     if (shmem_int4_add__h == NULL)
1782 | 	shmem_int4_add__h = (shmem_int4_add__p_h) dlsym(tau_handle,"shmem_int4_add_"); 
1783 |     if (shmem_int4_add__h == NULL) {
1784 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1785 |       return;
1786 |     }
1802 |   static shmem_int4_and_to_all__p_h shmem_int4_and_to_all__h = NULL;
1803 |   TAU_PROFILE_TIMER(t,"void shmem_int4_and_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
1804 |   if (tau_handle == NULL) 
1805 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1806 | 
1807 |   if (tau_handle == NULL) { 
1808 |     perror("Error opening library in dlopen call"); 
1809 |     return;
1810 |   } 
1812 |     if (shmem_int4_and_to_all__h == NULL)
1813 | 	shmem_int4_and_to_all__h = (shmem_int4_and_to_all__p_h) dlsym(tau_handle,"shmem_int4_and_to_all_"); 
1814 |     if (shmem_int4_and_to_all__h == NULL) {
1815 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1816 |       return;
1817 |     }
1834 |   int retval = 0;
1835 |   TAU_PROFILE_TIMER(t,"int shmem_int4_cswap_(int *, int *, int *, int *)", "", TAU_USER);
1836 |   if (tau_handle == NULL) 
1837 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1838 | 
1839 |   if (tau_handle == NULL) { 
1840 |     perror("Error opening library in dlopen call"); 
1841 |     return retval;
1842 |   } 
1844 |     if (shmem_int4_cswap__h == NULL)
1845 | 	shmem_int4_cswap__h = (shmem_int4_cswap__p_h) dlsym(tau_handle,"shmem_int4_cswap_"); 
1846 |     if (shmem_int4_cswap__h == NULL) {
1847 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1848 |       return retval;
1849 |     }
1873 |   int retval = 0;
1874 |   TAU_PROFILE_TIMER(t,"int shmem_int4_fadd_(void *, int *, int *)", "", TAU_USER);
1875 |   if (tau_handle == NULL) 
1876 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1877 | 
1878 |   if (tau_handle == NULL) { 
1879 |     perror("Error opening library in dlopen call"); 
1880 |     return retval;
1881 |   } 
1883 |     if (shmem_int4_fadd__h == NULL)
1884 | 	shmem_int4_fadd__h = (shmem_int4_fadd__p_h) dlsym(tau_handle,"shmem_int4_fadd_"); 
1885 |     if (shmem_int4_fadd__h == NULL) {
1886 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1887 |       return retval;
1888 |     }
1910 |   int retval = 0;
1911 |   TAU_PROFILE_TIMER(t,"int shmem_int4_finc_(void *, int *)", "", TAU_USER);
1912 |   if (tau_handle == NULL) 
1913 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1914 | 
1915 |   if (tau_handle == NULL) { 
1916 |     perror("Error opening library in dlopen call"); 
1917 |     return retval;
1918 |   } 
1920 |     if (shmem_int4_finc__h == NULL)
1921 | 	shmem_int4_finc__h = (shmem_int4_finc__p_h) dlsym(tau_handle,"shmem_int4_finc_"); 
1922 |     if (shmem_int4_finc__h == NULL) {
1923 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1924 |       return retval;
1925 |     }
1946 |   static shmem_int4_inc__p_h shmem_int4_inc__h = NULL;
1947 |   TAU_PROFILE_TIMER(t,"void shmem_int4_inc_(void *, int *)", "", TAU_USER);
1948 |   if (tau_handle == NULL) 
1949 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1950 | 
1951 |   if (tau_handle == NULL) { 
1952 |     perror("Error opening library in dlopen call"); 
1953 |     return;
1954 |   } 
1956 |     if (shmem_int4_inc__h == NULL)
1957 | 	shmem_int4_inc__h = (shmem_int4_inc__p_h) dlsym(tau_handle,"shmem_int4_inc_"); 
1958 |     if (shmem_int4_inc__h == NULL) {
1959 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1960 |       return;
1961 |     }
1977 |   static shmem_int4_max_to_all__p_h shmem_int4_max_to_all__h = NULL;
1978 |   TAU_PROFILE_TIMER(t,"void shmem_int4_max_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
1979 |   if (tau_handle == NULL) 
1980 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1981 | 
1982 |   if (tau_handle == NULL) { 
1983 |     perror("Error opening library in dlopen call"); 
1984 |     return;
1985 |   } 
1987 |     if (shmem_int4_max_to_all__h == NULL)
1988 | 	shmem_int4_max_to_all__h = (shmem_int4_max_to_all__p_h) dlsym(tau_handle,"shmem_int4_max_to_all_"); 
1989 |     if (shmem_int4_max_to_all__h == NULL) {
1990 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1991 |       return;
1992 |     }
2008 |   static shmem_int4_min_to_all__p_h shmem_int4_min_to_all__h = NULL;
2009 |   TAU_PROFILE_TIMER(t,"void shmem_int4_min_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
2010 |   if (tau_handle == NULL) 
2011 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2012 | 
2013 |   if (tau_handle == NULL) { 
2014 |     perror("Error opening library in dlopen call"); 
2015 |     return;
2016 |   } 
2018 |     if (shmem_int4_min_to_all__h == NULL)
2019 | 	shmem_int4_min_to_all__h = (shmem_int4_min_to_all__p_h) dlsym(tau_handle,"shmem_int4_min_to_all_"); 
2020 |     if (shmem_int4_min_to_all__h == NULL) {
2021 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2022 |       return;
2023 |     }
2039 |   static shmem_int4_or_to_all__p_h shmem_int4_or_to_all__h = NULL;
2040 |   TAU_PROFILE_TIMER(t,"void shmem_int4_or_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
2041 |   if (tau_handle == NULL) 
2042 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2043 | 
2044 |   if (tau_handle == NULL) { 
2045 |     perror("Error opening library in dlopen call"); 
2046 |     return;
2047 |   } 
2049 |     if (shmem_int4_or_to_all__h == NULL)
2050 | 	shmem_int4_or_to_all__h = (shmem_int4_or_to_all__p_h) dlsym(tau_handle,"shmem_int4_or_to_all_"); 
2051 |     if (shmem_int4_or_to_all__h == NULL) {
2052 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2053 |       return;
2054 |     }
2070 |   static shmem_int4_prod_to_all__p_h shmem_int4_prod_to_all__h = NULL;
2071 |   TAU_PROFILE_TIMER(t,"void shmem_int4_prod_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
2072 |   if (tau_handle == NULL) 
2073 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2074 | 
2075 |   if (tau_handle == NULL) { 
2076 |     perror("Error opening library in dlopen call"); 
2077 |     return;
2078 |   } 
2080 |     if (shmem_int4_prod_to_all__h == NULL)
2081 | 	shmem_int4_prod_to_all__h = (shmem_int4_prod_to_all__p_h) dlsym(tau_handle,"shmem_int4_prod_to_all_"); 
2082 |     if (shmem_int4_prod_to_all__h == NULL) {
2083 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2084 |       return;
2085 |     }
2101 |   static shmem_int4_sum_to_all__p_h shmem_int4_sum_to_all__h = NULL;
2102 |   TAU_PROFILE_TIMER(t,"void shmem_int4_sum_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
2103 |   if (tau_handle == NULL) 
2104 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2105 | 
2106 |   if (tau_handle == NULL) { 
2107 |     perror("Error opening library in dlopen call"); 
2108 |     return;
2109 |   } 
2111 |     if (shmem_int4_sum_to_all__h == NULL)
2112 | 	shmem_int4_sum_to_all__h = (shmem_int4_sum_to_all__p_h) dlsym(tau_handle,"shmem_int4_sum_to_all_"); 
2113 |     if (shmem_int4_sum_to_all__h == NULL) {
2114 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2115 |       return;
2116 |     }
2133 |   int retval = 0;
2134 |   TAU_PROFILE_TIMER(t,"int shmem_int4_swap_(void *, int *, int *)", "", TAU_USER);
2135 |   if (tau_handle == NULL) 
2136 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2137 | 
2138 |   if (tau_handle == NULL) { 
2139 |     perror("Error opening library in dlopen call"); 
2140 |     return retval;
2141 |   } 
2143 |     if (shmem_int4_swap__h == NULL)
2144 | 	shmem_int4_swap__h = (shmem_int4_swap__p_h) dlsym(tau_handle,"shmem_int4_swap_"); 
2145 |     if (shmem_int4_swap__h == NULL) {
2146 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2147 |       return retval;
2148 |     }
2169 |   static shmem_int4_wait__p_h shmem_int4_wait__h = NULL;
2170 |   TAU_PROFILE_TIMER(t,"void shmem_int4_wait_(int *, int *)", "", TAU_USER);
2171 |   if (tau_handle == NULL) 
2172 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2173 | 
2174 |   if (tau_handle == NULL) { 
2175 |     perror("Error opening library in dlopen call"); 
2176 |     return;
2177 |   } 
2179 |     if (shmem_int4_wait__h == NULL)
2180 | 	shmem_int4_wait__h = (shmem_int4_wait__p_h) dlsym(tau_handle,"shmem_int4_wait_"); 
2181 |     if (shmem_int4_wait__h == NULL) {
2182 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2183 |       return;
2184 |     }
2200 |   static shmem_int4_wait_until__p_h shmem_int4_wait_until__h = NULL;
2201 |   TAU_PROFILE_TIMER(t,"void shmem_int4_wait_until_(int *, int *, int *)", "", TAU_USER);
2202 |   if (tau_handle == NULL) 
2203 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2204 | 
2205 |   if (tau_handle == NULL) { 
2206 |     perror("Error opening library in dlopen call"); 
2207 |     return;
2208 |   } 
2210 |     if (shmem_int4_wait_until__h == NULL)
2211 | 	shmem_int4_wait_until__h = (shmem_int4_wait_until__p_h) dlsym(tau_handle,"shmem_int4_wait_until_"); 
2212 |     if (shmem_int4_wait_until__h == NULL) {
2213 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2214 |       return;
2215 |     }
2231 |   static shmem_int4_xor_to_all__p_h shmem_int4_xor_to_all__h = NULL;
2232 |   TAU_PROFILE_TIMER(t,"void shmem_int4_xor_to_all_(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
2233 |   if (tau_handle == NULL) 
2234 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2235 | 
2236 |   if (tau_handle == NULL) { 
2237 |     perror("Error opening library in dlopen call"); 
2238 |     return;
2239 |   } 
2241 |     if (shmem_int4_xor_to_all__h == NULL)
2242 | 	shmem_int4_xor_to_all__h = (shmem_int4_xor_to_all__p_h) dlsym(tau_handle,"shmem_int4_xor_to_all_"); 
2243 |     if (shmem_int4_xor_to_all__h == NULL) {
2244 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2245 |       return;
2246 |     }
2262 |   static shmem_int8_add__p_h shmem_int8_add__h = NULL;
2263 |   TAU_PROFILE_TIMER(t,"void shmem_int8_add_(void *, long *, int *)", "", TAU_USER);
2264 |   if (tau_handle == NULL) 
2265 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2266 | 
2267 |   if (tau_handle == NULL) { 
2268 |     perror("Error opening library in dlopen call"); 
2269 |     return;
2270 |   } 
2272 |     if (shmem_int8_add__h == NULL)
2273 | 	shmem_int8_add__h = (shmem_int8_add__p_h) dlsym(tau_handle,"shmem_int8_add_"); 
2274 |     if (shmem_int8_add__h == NULL) {
2275 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2276 |       return;
2277 |     }
2293 |   static shmem_int8_and_to_all__p_h shmem_int8_and_to_all__h = NULL;
2294 |   TAU_PROFILE_TIMER(t,"void shmem_int8_and_to_all_(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
2295 |   if (tau_handle == NULL) 
2296 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2297 | 
2298 |   if (tau_handle == NULL) { 
2299 |     perror("Error opening library in dlopen call"); 
2300 |     return;
2301 |   } 
2303 |     if (shmem_int8_and_to_all__h == NULL)
2304 | 	shmem_int8_and_to_all__h = (shmem_int8_and_to_all__p_h) dlsym(tau_handle,"shmem_int8_and_to_all_"); 
2305 |     if (shmem_int8_and_to_all__h == NULL) {
2306 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2307 |       return;
2308 |     }
2325 |   long retval = 0;
2326 |   TAU_PROFILE_TIMER(t,"long shmem_int8_cswap_(long *, long *, long *, int *)", "", TAU_USER);
2327 |   if (tau_handle == NULL) 
2328 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2329 | 
2330 |   if (tau_handle == NULL) { 
2331 |     perror("Error opening library in dlopen call"); 
2332 |     return retval;
2333 |   } 
2335 |     if (shmem_int8_cswap__h == NULL)
2336 | 	shmem_int8_cswap__h = (shmem_int8_cswap__p_h) dlsym(tau_handle,"shmem_int8_cswap_"); 
2337 |     if (shmem_int8_cswap__h == NULL) {
2338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2339 |       return retval;
2340 |     }
2364 |   long retval = 0;
2365 |   TAU_PROFILE_TIMER(t,"long shmem_int8_fadd_(void *, int *, int *)", "", TAU_USER);
2366 |   if (tau_handle == NULL) 
2367 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2368 | 
2369 |   if (tau_handle == NULL) { 
2370 |     perror("Error opening library in dlopen call"); 
2371 |     return retval;
2372 |   } 
2374 |     if (shmem_int8_fadd__h == NULL)
2375 | 	shmem_int8_fadd__h = (shmem_int8_fadd__p_h) dlsym(tau_handle,"shmem_int8_fadd_"); 
2376 |     if (shmem_int8_fadd__h == NULL) {
2377 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2378 |       return retval;
2379 |     }
2401 |   long retval = 0;
2402 |   TAU_PROFILE_TIMER(t,"long shmem_int8_finc_(void *, int *)", "", TAU_USER);
2403 |   if (tau_handle == NULL) 
2404 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2405 | 
2406 |   if (tau_handle == NULL) { 
2407 |     perror("Error opening library in dlopen call"); 
2408 |     return retval;
2409 |   } 
2411 |     if (shmem_int8_finc__h == NULL)
2412 | 	shmem_int8_finc__h = (shmem_int8_finc__p_h) dlsym(tau_handle,"shmem_int8_finc_"); 
2413 |     if (shmem_int8_finc__h == NULL) {
2414 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2415 |       return retval;
2416 |     }
2437 |   static shmem_int8_inc__p_h shmem_int8_inc__h = NULL;
2438 |   TAU_PROFILE_TIMER(t,"void shmem_int8_inc_(void *, int *)", "", TAU_USER);
2439 |   if (tau_handle == NULL) 
2440 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2441 | 
2442 |   if (tau_handle == NULL) { 
2443 |     perror("Error opening library in dlopen call"); 
2444 |     return;
2445 |   } 
2447 |     if (shmem_int8_inc__h == NULL)
2448 | 	shmem_int8_inc__h = (shmem_int8_inc__p_h) dlsym(tau_handle,"shmem_int8_inc_"); 
2449 |     if (shmem_int8_inc__h == NULL) {
2450 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2451 |       return;
2452 |     }
2468 |   static shmem_int8_max_to_all__p_h shmem_int8_max_to_all__h = NULL;
2469 |   TAU_PROFILE_TIMER(t,"void shmem_int8_max_to_all_(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
2470 |   if (tau_handle == NULL) 
2471 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2472 | 
2473 |   if (tau_handle == NULL) { 
2474 |     perror("Error opening library in dlopen call"); 
2475 |     return;
2476 |   } 
2478 |     if (shmem_int8_max_to_all__h == NULL)
2479 | 	shmem_int8_max_to_all__h = (shmem_int8_max_to_all__p_h) dlsym(tau_handle,"shmem_int8_max_to_all_"); 
2480 |     if (shmem_int8_max_to_all__h == NULL) {
2481 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2482 |       return;
2483 |     }
2499 |   static shmem_int8_min_to_all__p_h shmem_int8_min_to_all__h = NULL;
2500 |   TAU_PROFILE_TIMER(t,"void shmem_int8_min_to_all_(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
2501 |   if (tau_handle == NULL) 
2502 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2503 | 
2504 |   if (tau_handle == NULL) { 
2505 |     perror("Error opening library in dlopen call"); 
2506 |     return;
2507 |   } 
2509 |     if (shmem_int8_min_to_all__h == NULL)
2510 | 	shmem_int8_min_to_all__h = (shmem_int8_min_to_all__p_h) dlsym(tau_handle,"shmem_int8_min_to_all_"); 
2511 |     if (shmem_int8_min_to_all__h == NULL) {
2512 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2513 |       return;
2514 |     }
2530 |   static shmem_int8_or_to_all__p_h shmem_int8_or_to_all__h = NULL;
2531 |   TAU_PROFILE_TIMER(t,"void shmem_int8_or_to_all_(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
2532 |   if (tau_handle == NULL) 
2533 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2534 | 
2535 |   if (tau_handle == NULL) { 
2536 |     perror("Error opening library in dlopen call"); 
2537 |     return;
2538 |   } 
2540 |     if (shmem_int8_or_to_all__h == NULL)
2541 | 	shmem_int8_or_to_all__h = (shmem_int8_or_to_all__p_h) dlsym(tau_handle,"shmem_int8_or_to_all_"); 
2542 |     if (shmem_int8_or_to_all__h == NULL) {
2543 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2544 |       return;
2545 |     }
2561 |   static shmem_int8_prod_to_all__p_h shmem_int8_prod_to_all__h = NULL;
2562 |   TAU_PROFILE_TIMER(t,"void shmem_int8_prod_to_all_(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
2563 |   if (tau_handle == NULL) 
2564 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2565 | 
2566 |   if (tau_handle == NULL) { 
2567 |     perror("Error opening library in dlopen call"); 
2568 |     return;
2569 |   } 
2571 |     if (shmem_int8_prod_to_all__h == NULL)
2572 | 	shmem_int8_prod_to_all__h = (shmem_int8_prod_to_all__p_h) dlsym(tau_handle,"shmem_int8_prod_to_all_"); 
2573 |     if (shmem_int8_prod_to_all__h == NULL) {
2574 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2575 |       return;
2576 |     }
2592 |   static shmem_int8_sum_to_all__p_h shmem_int8_sum_to_all__h = NULL;
2593 |   TAU_PROFILE_TIMER(t,"void shmem_int8_sum_to_all_(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
2594 |   if (tau_handle == NULL) 
2595 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2596 | 
2597 |   if (tau_handle == NULL) { 
2598 |     perror("Error opening library in dlopen call"); 
2599 |     return;
2600 |   } 
2602 |     if (shmem_int8_sum_to_all__h == NULL)
2603 | 	shmem_int8_sum_to_all__h = (shmem_int8_sum_to_all__p_h) dlsym(tau_handle,"shmem_int8_sum_to_all_"); 
2604 |     if (shmem_int8_sum_to_all__h == NULL) {
2605 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2606 |       return;
2607 |     }
2624 |   long retval = 0;
2625 |   TAU_PROFILE_TIMER(t,"long shmem_int8_swap_(void *, long *, int *)", "", TAU_USER);
2626 |   if (tau_handle == NULL) 
2627 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2628 | 
2629 |   if (tau_handle == NULL) { 
2630 |     perror("Error opening library in dlopen call"); 
2631 |     return retval;
2632 |   } 
2634 |     if (shmem_int8_swap__h == NULL)
2635 | 	shmem_int8_swap__h = (shmem_int8_swap__p_h) dlsym(tau_handle,"shmem_int8_swap_"); 
2636 |     if (shmem_int8_swap__h == NULL) {
2637 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2638 |       return retval;
2639 |     }
2660 |   static shmem_int8_wait__p_h shmem_int8_wait__h = NULL;
2661 |   TAU_PROFILE_TIMER(t,"void shmem_int8_wait_(long *, long *)", "", TAU_USER);
2662 |   if (tau_handle == NULL) 
2663 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2664 | 
2665 |   if (tau_handle == NULL) { 
2666 |     perror("Error opening library in dlopen call"); 
2667 |     return;
2668 |   } 
2670 |     if (shmem_int8_wait__h == NULL)
2671 | 	shmem_int8_wait__h = (shmem_int8_wait__p_h) dlsym(tau_handle,"shmem_int8_wait_"); 
2672 |     if (shmem_int8_wait__h == NULL) {
2673 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2674 |       return;
2675 |     }
2691 |   static shmem_int8_wait_until__p_h shmem_int8_wait_until__h = NULL;
2692 |   TAU_PROFILE_TIMER(t,"void shmem_int8_wait_until_(long *, int *, long *)", "", TAU_USER);
2693 |   if (tau_handle == NULL) 
2694 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2695 | 
2696 |   if (tau_handle == NULL) { 
2697 |     perror("Error opening library in dlopen call"); 
2698 |     return;
2699 |   } 
2701 |     if (shmem_int8_wait_until__h == NULL)
2702 | 	shmem_int8_wait_until__h = (shmem_int8_wait_until__p_h) dlsym(tau_handle,"shmem_int8_wait_until_"); 
2703 |     if (shmem_int8_wait_until__h == NULL) {
2704 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2705 |       return;
2706 |     }
2722 |   static shmem_int8_xor_to_all__p_h shmem_int8_xor_to_all__h = NULL;
2723 |   TAU_PROFILE_TIMER(t,"void shmem_int8_xor_to_all_(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
2724 |   if (tau_handle == NULL) 
2725 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2726 | 
2727 |   if (tau_handle == NULL) { 
2728 |     perror("Error opening library in dlopen call"); 
2729 |     return;
2730 |   } 
2732 |     if (shmem_int8_xor_to_all__h == NULL)
2733 | 	shmem_int8_xor_to_all__h = (shmem_int8_xor_to_all__p_h) dlsym(tau_handle,"shmem_int8_xor_to_all_"); 
2734 |     if (shmem_int8_xor_to_all__h == NULL) {
2735 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2736 |       return;
2737 |     }
2753 |   static shmem_integer_get__p_h shmem_integer_get__h = NULL;
2754 |   TAU_PROFILE_TIMER(t,"void shmem_integer_get_(void *, void *, int *, int *)", "", TAU_USER);
2755 |   if (tau_handle == NULL) 
2756 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2757 | 
2758 |   if (tau_handle == NULL) { 
2759 |     perror("Error opening library in dlopen call"); 
2760 |     return;
2761 |   } 
2763 |     if (shmem_integer_get__h == NULL)
2764 | 	shmem_integer_get__h = (shmem_integer_get__p_h) dlsym(tau_handle,"shmem_integer_get_"); 
2765 |     if (shmem_integer_get__h == NULL) {
2766 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2767 |       return;
2768 |     }
2786 |   static shmem_integer_iget__p_h shmem_integer_iget__h = NULL;
2787 |   TAU_PROFILE_TIMER(t,"void shmem_integer_iget_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
2788 |   if (tau_handle == NULL) 
2789 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2790 | 
2791 |   if (tau_handle == NULL) { 
2792 |     perror("Error opening library in dlopen call"); 
2793 |     return;
2794 |   } 
2796 |     if (shmem_integer_iget__h == NULL)
2797 | 	shmem_integer_iget__h = (shmem_integer_iget__p_h) dlsym(tau_handle,"shmem_integer_iget_"); 
2798 |     if (shmem_integer_iget__h == NULL) {
2799 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2800 |       return;
2801 |     }
2819 |   static shmem_integer_iput__p_h shmem_integer_iput__h = NULL;
2820 |   TAU_PROFILE_TIMER(t,"void shmem_integer_iput_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
2821 |   if (tau_handle == NULL) 
2822 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2823 | 
2824 |   if (tau_handle == NULL) { 
2825 |     perror("Error opening library in dlopen call"); 
2826 |     return;
2827 |   } 
2829 |     if (shmem_integer_iput__h == NULL)
2830 | 	shmem_integer_iput__h = (shmem_integer_iput__p_h) dlsym(tau_handle,"shmem_integer_iput_"); 
2831 |     if (shmem_integer_iput__h == NULL) {
2832 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2833 |       return;
2834 |     }
2852 |   static shmem_integer_put__p_h shmem_integer_put__h = NULL;
2853 |   TAU_PROFILE_TIMER(t,"void shmem_integer_put_(void *, void *, int *, int *)", "", TAU_USER);
2854 |   if (tau_handle == NULL) 
2855 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2856 | 
2857 |   if (tau_handle == NULL) { 
2858 |     perror("Error opening library in dlopen call"); 
2859 |     return;
2860 |   } 
2862 |     if (shmem_integer_put__h == NULL)
2863 | 	shmem_integer_put__h = (shmem_integer_put__p_h) dlsym(tau_handle,"shmem_integer_put_"); 
2864 |     if (shmem_integer_put__h == NULL) {
2865 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2866 |       return;
2867 |     }
2885 |   static shmem_iput128__p_h shmem_iput128__h = NULL;
2886 |   TAU_PROFILE_TIMER(t,"void shmem_iput128_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
2887 |   if (tau_handle == NULL) 
2888 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2889 | 
2890 |   if (tau_handle == NULL) { 
2891 |     perror("Error opening library in dlopen call"); 
2892 |     return;
2893 |   } 
2895 |     if (shmem_iput128__h == NULL)
2896 | 	shmem_iput128__h = (shmem_iput128__p_h) dlsym(tau_handle,"shmem_iput128_"); 
2897 |     if (shmem_iput128__h == NULL) {
2898 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2899 |       return;
2900 |     }
2918 |   static shmem_iput16__p_h shmem_iput16__h = NULL;
2919 |   TAU_PROFILE_TIMER(t,"void shmem_iput16_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
2920 |   if (tau_handle == NULL) 
2921 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2922 | 
2923 |   if (tau_handle == NULL) { 
2924 |     perror("Error opening library in dlopen call"); 
2925 |     return;
2926 |   } 
2928 |     if (shmem_iput16__h == NULL)
2929 | 	shmem_iput16__h = (shmem_iput16__p_h) dlsym(tau_handle,"shmem_iput16_"); 
2930 |     if (shmem_iput16__h == NULL) {
2931 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2932 |       return;
2933 |     }
2951 |   static shmem_iput32__p_h shmem_iput32__h = NULL;
2952 |   TAU_PROFILE_TIMER(t,"void shmem_iput32_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
2953 |   if (tau_handle == NULL) 
2954 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2955 | 
2956 |   if (tau_handle == NULL) { 
2957 |     perror("Error opening library in dlopen call"); 
2958 |     return;
2959 |   } 
2961 |     if (shmem_iput32__h == NULL)
2962 | 	shmem_iput32__h = (shmem_iput32__p_h) dlsym(tau_handle,"shmem_iput32_"); 
2963 |     if (shmem_iput32__h == NULL) {
2964 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2965 |       return;
2966 |     }
2984 |   static shmem_iput4__p_h shmem_iput4__h = NULL;
2985 |   TAU_PROFILE_TIMER(t,"void shmem_iput4_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
2986 |   if (tau_handle == NULL) 
2987 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2988 | 
2989 |   if (tau_handle == NULL) { 
2990 |     perror("Error opening library in dlopen call"); 
2991 |     return;
2992 |   } 
2994 |     if (shmem_iput4__h == NULL)
2995 | 	shmem_iput4__h = (shmem_iput4__p_h) dlsym(tau_handle,"shmem_iput4_"); 
2996 |     if (shmem_iput4__h == NULL) {
2997 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2998 |       return;
2999 |     }
3017 |   static shmem_iput64__p_h shmem_iput64__h = NULL;
3018 |   TAU_PROFILE_TIMER(t,"void shmem_iput64_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
3019 |   if (tau_handle == NULL) 
3020 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3021 | 
3022 |   if (tau_handle == NULL) { 
3023 |     perror("Error opening library in dlopen call"); 
3024 |     return;
3025 |   } 
3027 |     if (shmem_iput64__h == NULL)
3028 | 	shmem_iput64__h = (shmem_iput64__p_h) dlsym(tau_handle,"shmem_iput64_"); 
3029 |     if (shmem_iput64__h == NULL) {
3030 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3031 |       return;
3032 |     }
3050 |   static shmem_iput8__p_h shmem_iput8__h = NULL;
3051 |   TAU_PROFILE_TIMER(t,"void shmem_iput8_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
3052 |   if (tau_handle == NULL) 
3053 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3054 | 
3055 |   if (tau_handle == NULL) { 
3056 |     perror("Error opening library in dlopen call"); 
3057 |     return;
3058 |   } 
3060 |     if (shmem_iput8__h == NULL)
3061 | 	shmem_iput8__h = (shmem_iput8__p_h) dlsym(tau_handle,"shmem_iput8_"); 
3062 |     if (shmem_iput8__h == NULL) {
3063 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3064 |       return;
3065 |     }
3083 |   static shmem_logical_get__p_h shmem_logical_get__h = NULL;
3084 |   TAU_PROFILE_TIMER(t,"void shmem_logical_get_(void *, void *, int *, int *)", "", TAU_USER);
3085 |   if (tau_handle == NULL) 
3086 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3087 | 
3088 |   if (tau_handle == NULL) { 
3089 |     perror("Error opening library in dlopen call"); 
3090 |     return;
3091 |   } 
3093 |     if (shmem_logical_get__h == NULL)
3094 | 	shmem_logical_get__h = (shmem_logical_get__p_h) dlsym(tau_handle,"shmem_logical_get_"); 
3095 |     if (shmem_logical_get__h == NULL) {
3096 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3097 |       return;
3098 |     }
3116 |   static shmem_logical_iget__p_h shmem_logical_iget__h = NULL;
3117 |   TAU_PROFILE_TIMER(t,"void shmem_logical_iget_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
3118 |   if (tau_handle == NULL) 
3119 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3120 | 
3121 |   if (tau_handle == NULL) { 
3122 |     perror("Error opening library in dlopen call"); 
3123 |     return;
3124 |   } 
3126 |     if (shmem_logical_iget__h == NULL)
3127 | 	shmem_logical_iget__h = (shmem_logical_iget__p_h) dlsym(tau_handle,"shmem_logical_iget_"); 
3128 |     if (shmem_logical_iget__h == NULL) {
3129 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3130 |       return;
3131 |     }
3149 |   static shmem_logical_iput__p_h shmem_logical_iput__h = NULL;
3150 |   TAU_PROFILE_TIMER(t,"void shmem_logical_iput_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
3151 |   if (tau_handle == NULL) 
3152 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3153 | 
3154 |   if (tau_handle == NULL) { 
3155 |     perror("Error opening library in dlopen call"); 
3156 |     return;
3157 |   } 
3159 |     if (shmem_logical_iput__h == NULL)
3160 | 	shmem_logical_iput__h = (shmem_logical_iput__p_h) dlsym(tau_handle,"shmem_logical_iput_"); 
3161 |     if (shmem_logical_iput__h == NULL) {
3162 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3163 |       return;
3164 |     }
3182 |   static shmem_logical_put__p_h shmem_logical_put__h = NULL;
3183 |   TAU_PROFILE_TIMER(t,"void shmem_logical_put_(void *, void *, int *, int *)", "", TAU_USER);
3184 |   if (tau_handle == NULL) 
3185 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3186 | 
3187 |   if (tau_handle == NULL) { 
3188 |     perror("Error opening library in dlopen call"); 
3189 |     return;
3190 |   } 
3192 |     if (shmem_logical_put__h == NULL)
3193 | 	shmem_logical_put__h = (shmem_logical_put__p_h) dlsym(tau_handle,"shmem_logical_put_"); 
3194 |     if (shmem_logical_put__h == NULL) {
3195 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3196 |       return;
3197 |     }
3216 |   int retval = 0;
3217 |   TAU_PROFILE_TIMER(t,"int shmem_my_pe_()", "", TAU_USER);
3218 |   if (tau_handle == NULL) 
3219 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3220 | 
3221 |   if (tau_handle == NULL) { 
3222 |     perror("Error opening library in dlopen call"); 
3223 |     return retval;
3224 |   } 
3226 |     if (shmem_my_pe__h == NULL)
3227 | 	shmem_my_pe__h = (shmem_my_pe__p_h) dlsym(tau_handle,"shmem_my_pe_"); 
3228 |     if (shmem_my_pe__h == NULL) {
3229 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3230 |       return retval;
3231 |     }
3249 |   int retval = 0;
3250 |   TAU_PROFILE_TIMER(t,"int shmem_n_pes_()", "", TAU_USER);
3251 |   if (tau_handle == NULL) 
3252 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3253 | 
3254 |   if (tau_handle == NULL) { 
3255 |     perror("Error opening library in dlopen call"); 
3256 |     return retval;
3257 |   } 
3259 |     if (shmem_n_pes__h == NULL)
3260 | 	shmem_n_pes__h = (shmem_n_pes__p_h) dlsym(tau_handle,"shmem_n_pes_"); 
3261 |     if (shmem_n_pes__h == NULL) {
3262 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3263 |       return retval;
3264 |     }
3282 |   int retval = 0;
3283 |   TAU_PROFILE_TIMER(t,"int shmem_pe_accessible_(int *)", "", TAU_USER);
3284 |   if (tau_handle == NULL) 
3285 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3286 | 
3287 |   if (tau_handle == NULL) { 
3288 |     perror("Error opening library in dlopen call"); 
3289 |     return retval;
3290 |   } 
3292 |     if (shmem_pe_accessible__h == NULL)
3293 | 	shmem_pe_accessible__h = (shmem_pe_accessible__p_h) dlsym(tau_handle,"shmem_pe_accessible_"); 
3294 |     if (shmem_pe_accessible__h == NULL) {
3295 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3296 |       return retval;
3297 |     }
3314 |   static shmem_ptr__p_h shmem_ptr__h = NULL;
3315 |   TAU_PROFILE_TIMER(t,"void shmem_ptr_(void *, int *)", "", TAU_USER);
3316 |   if (tau_handle == NULL) 
3317 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3318 | 
3319 |   if (tau_handle == NULL) { 
3320 |     perror("Error opening library in dlopen call"); 
3321 |     return;
3322 |   } 
3324 |     if (shmem_ptr__h == NULL)
3325 | 	shmem_ptr__h = (shmem_ptr__p_h) dlsym(tau_handle,"shmem_ptr_"); 
3326 |     if (shmem_ptr__h == NULL) {
3327 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3328 |       return;
3329 |     }
3345 |   static shmem_put128__p_h shmem_put128__h = NULL;
3346 |   TAU_PROFILE_TIMER(t,"void shmem_put128_(void *, void *, int *, int *)", "", TAU_USER);
3347 |   if (tau_handle == NULL) 
3348 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3349 | 
3350 |   if (tau_handle == NULL) { 
3351 |     perror("Error opening library in dlopen call"); 
3352 |     return;
3353 |   } 
3355 |     if (shmem_put128__h == NULL)
3356 | 	shmem_put128__h = (shmem_put128__p_h) dlsym(tau_handle,"shmem_put128_"); 
3357 |     if (shmem_put128__h == NULL) {
3358 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3359 |       return;
3360 |     }
3378 |   static shmem_put16__p_h shmem_put16__h = NULL;
3379 |   TAU_PROFILE_TIMER(t,"void shmem_put16_(void *, void *, int *, int *)", "", TAU_USER);
3380 |   if (tau_handle == NULL) 
3381 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3382 | 
3383 |   if (tau_handle == NULL) { 
3384 |     perror("Error opening library in dlopen call"); 
3385 |     return;
3386 |   } 
3388 |     if (shmem_put16__h == NULL)
3389 | 	shmem_put16__h = (shmem_put16__p_h) dlsym(tau_handle,"shmem_put16_"); 
3390 |     if (shmem_put16__h == NULL) {
3391 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3392 |       return;
3393 |     }
3411 |   static shmem_put32__p_h shmem_put32__h = NULL;
3412 |   TAU_PROFILE_TIMER(t,"void shmem_put32_(void *, void *, int *, int *)", "", TAU_USER);
3413 |   if (tau_handle == NULL) 
3414 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3415 | 
3416 |   if (tau_handle == NULL) { 
3417 |     perror("Error opening library in dlopen call"); 
3418 |     return;
3419 |   } 
3421 |     if (shmem_put32__h == NULL)
3422 | 	shmem_put32__h = (shmem_put32__p_h) dlsym(tau_handle,"shmem_put32_"); 
3423 |     if (shmem_put32__h == NULL) {
3424 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3425 |       return;
3426 |     }
3444 |   static shmem_put4__p_h shmem_put4__h = NULL;
3445 |   TAU_PROFILE_TIMER(t,"void shmem_put4_(void *, void *, int *, int *)", "", TAU_USER);
3446 |   if (tau_handle == NULL) 
3447 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3448 | 
3449 |   if (tau_handle == NULL) { 
3450 |     perror("Error opening library in dlopen call"); 
3451 |     return;
3452 |   } 
3454 |     if (shmem_put4__h == NULL)
3455 | 	shmem_put4__h = (shmem_put4__p_h) dlsym(tau_handle,"shmem_put4_"); 
3456 |     if (shmem_put4__h == NULL) {
3457 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3458 |       return;
3459 |     }
3477 |   static shmem_put64__p_h shmem_put64__h = NULL;
3478 |   TAU_PROFILE_TIMER(t,"void shmem_put64_(void *, void *, int *, int *)", "", TAU_USER);
3479 |   if (tau_handle == NULL) 
3480 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3481 | 
3482 |   if (tau_handle == NULL) { 
3483 |     perror("Error opening library in dlopen call"); 
3484 |     return;
3485 |   } 
3487 |     if (shmem_put64__h == NULL)
3488 | 	shmem_put64__h = (shmem_put64__p_h) dlsym(tau_handle,"shmem_put64_"); 
3489 |     if (shmem_put64__h == NULL) {
3490 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3491 |       return;
3492 |     }
3510 |   static shmem_put8__p_h shmem_put8__h = NULL;
3511 |   TAU_PROFILE_TIMER(t,"void shmem_put8_(void *, void *, int *, int *)", "", TAU_USER);
3512 |   if (tau_handle == NULL) 
3513 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3514 | 
3515 |   if (tau_handle == NULL) { 
3516 |     perror("Error opening library in dlopen call"); 
3517 |     return;
3518 |   } 
3520 |     if (shmem_put8__h == NULL)
3521 | 	shmem_put8__h = (shmem_put8__p_h) dlsym(tau_handle,"shmem_put8_"); 
3522 |     if (shmem_put8__h == NULL) {
3523 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3524 |       return;
3525 |     }
3543 |   static shmem_putmem__p_h shmem_putmem__h = NULL;
3544 |   TAU_PROFILE_TIMER(t,"void shmem_putmem_(void *, void *, int *, int *)", "", TAU_USER);
3545 |   if (tau_handle == NULL) 
3546 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3547 | 
3548 |   if (tau_handle == NULL) { 
3549 |     perror("Error opening library in dlopen call"); 
3550 |     return;
3551 |   } 
3553 |     if (shmem_putmem__h == NULL)
3554 | 	shmem_putmem__h = (shmem_putmem__p_h) dlsym(tau_handle,"shmem_putmem_"); 
3555 |     if (shmem_putmem__h == NULL) {
3556 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3557 |       return;
3558 |     }
3576 |   static shmem_quiet__p_h shmem_quiet__h = NULL;
3577 |   TAU_PROFILE_TIMER(t,"void shmem_quiet_()", "", TAU_USER);
3578 |   if (tau_handle == NULL) 
3579 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3580 | 
3581 |   if (tau_handle == NULL) { 
3582 |     perror("Error opening library in dlopen call"); 
3583 |     return;
3584 |   } 
3586 |     if (shmem_quiet__h == NULL)
3587 | 	shmem_quiet__h = (shmem_quiet__p_h) dlsym(tau_handle,"shmem_quiet_"); 
3588 |     if (shmem_quiet__h == NULL) {
3589 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3590 |       return;
3591 |     }
3607 |   static shmem_real16_max_to_all__p_h shmem_real16_max_to_all__h = NULL;
3608 |   TAU_PROFILE_TIMER(t,"void shmem_real16_max_to_all_(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
3609 |   if (tau_handle == NULL) 
3610 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3611 | 
3612 |   if (tau_handle == NULL) { 
3613 |     perror("Error opening library in dlopen call"); 
3614 |     return;
3615 |   } 
3617 |     if (shmem_real16_max_to_all__h == NULL)
3618 | 	shmem_real16_max_to_all__h = (shmem_real16_max_to_all__p_h) dlsym(tau_handle,"shmem_real16_max_to_all_"); 
3619 |     if (shmem_real16_max_to_all__h == NULL) {
3620 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3621 |       return;
3622 |     }
3638 |   static shmem_real16_min_to_all__p_h shmem_real16_min_to_all__h = NULL;
3639 |   TAU_PROFILE_TIMER(t,"void shmem_real16_min_to_all_(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
3640 |   if (tau_handle == NULL) 
3641 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3642 | 
3643 |   if (tau_handle == NULL) { 
3644 |     perror("Error opening library in dlopen call"); 
3645 |     return;
3646 |   } 
3648 |     if (shmem_real16_min_to_all__h == NULL)
3649 | 	shmem_real16_min_to_all__h = (shmem_real16_min_to_all__p_h) dlsym(tau_handle,"shmem_real16_min_to_all_"); 
3650 |     if (shmem_real16_min_to_all__h == NULL) {
3651 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3652 |       return;
3653 |     }
3669 |   static shmem_real16_prod_to_all__p_h shmem_real16_prod_to_all__h = NULL;
3670 |   TAU_PROFILE_TIMER(t,"void shmem_real16_prod_to_all_(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
3671 |   if (tau_handle == NULL) 
3672 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3673 | 
3674 |   if (tau_handle == NULL) { 
3675 |     perror("Error opening library in dlopen call"); 
3676 |     return;
3677 |   } 
3679 |     if (shmem_real16_prod_to_all__h == NULL)
3680 | 	shmem_real16_prod_to_all__h = (shmem_real16_prod_to_all__p_h) dlsym(tau_handle,"shmem_real16_prod_to_all_"); 
3681 |     if (shmem_real16_prod_to_all__h == NULL) {
3682 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3683 |       return;
3684 |     }
3700 |   static shmem_real16_sum_to_all__p_h shmem_real16_sum_to_all__h = NULL;
3701 |   TAU_PROFILE_TIMER(t,"void shmem_real16_sum_to_all_(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
3702 |   if (tau_handle == NULL) 
3703 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3704 | 
3705 |   if (tau_handle == NULL) { 
3706 |     perror("Error opening library in dlopen call"); 
3707 |     return;
3708 |   } 
3710 |     if (shmem_real16_sum_to_all__h == NULL)
3711 | 	shmem_real16_sum_to_all__h = (shmem_real16_sum_to_all__p_h) dlsym(tau_handle,"shmem_real16_sum_to_all_"); 
3712 |     if (shmem_real16_sum_to_all__h == NULL) {
3713 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3714 |       return;
3715 |     }
3731 |   static shmem_real4_max_to_all__p_h shmem_real4_max_to_all__h = NULL;
3732 |   TAU_PROFILE_TIMER(t,"void shmem_real4_max_to_all_(void *, void *, int *, int *, int *, int *, float *, long *)", "", TAU_USER);
3733 |   if (tau_handle == NULL) 
3734 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3735 | 
3736 |   if (tau_handle == NULL) { 
3737 |     perror("Error opening library in dlopen call"); 
3738 |     return;
3739 |   } 
3741 |     if (shmem_real4_max_to_all__h == NULL)
3742 | 	shmem_real4_max_to_all__h = (shmem_real4_max_to_all__p_h) dlsym(tau_handle,"shmem_real4_max_to_all_"); 
3743 |     if (shmem_real4_max_to_all__h == NULL) {
3744 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3745 |       return;
3746 |     }
3762 |   static shmem_real4_min_to_all__p_h shmem_real4_min_to_all__h = NULL;
3763 |   TAU_PROFILE_TIMER(t,"void shmem_real4_min_to_all_(void *, void *, int *, int *, int *, int *, float *, long *)", "", TAU_USER);
3764 |   if (tau_handle == NULL) 
3765 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3766 | 
3767 |   if (tau_handle == NULL) { 
3768 |     perror("Error opening library in dlopen call"); 
3769 |     return;
3770 |   } 
3772 |     if (shmem_real4_min_to_all__h == NULL)
3773 | 	shmem_real4_min_to_all__h = (shmem_real4_min_to_all__p_h) dlsym(tau_handle,"shmem_real4_min_to_all_"); 
3774 |     if (shmem_real4_min_to_all__h == NULL) {
3775 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3776 |       return;
3777 |     }
3793 |   static shmem_real4_prod_to_all__p_h shmem_real4_prod_to_all__h = NULL;
3794 |   TAU_PROFILE_TIMER(t,"void shmem_real4_prod_to_all_(void *, void *, int *, int *, int *, int *, float *, long *)", "", TAU_USER);
3795 |   if (tau_handle == NULL) 
3796 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3797 | 
3798 |   if (tau_handle == NULL) { 
3799 |     perror("Error opening library in dlopen call"); 
3800 |     return;
3801 |   } 
3803 |     if (shmem_real4_prod_to_all__h == NULL)
3804 | 	shmem_real4_prod_to_all__h = (shmem_real4_prod_to_all__p_h) dlsym(tau_handle,"shmem_real4_prod_to_all_"); 
3805 |     if (shmem_real4_prod_to_all__h == NULL) {
3806 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3807 |       return;
3808 |     }
3824 |   static shmem_real4_sum_to_all__p_h shmem_real4_sum_to_all__h = NULL;
3825 |   TAU_PROFILE_TIMER(t,"void shmem_real4_sum_to_all_(void *, void *, int *, int *, int *, int *, float *, long *)", "", TAU_USER);
3826 |   if (tau_handle == NULL) 
3827 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3828 | 
3829 |   if (tau_handle == NULL) { 
3830 |     perror("Error opening library in dlopen call"); 
3831 |     return;
3832 |   } 
3834 |     if (shmem_real4_sum_to_all__h == NULL)
3835 | 	shmem_real4_sum_to_all__h = (shmem_real4_sum_to_all__p_h) dlsym(tau_handle,"shmem_real4_sum_to_all_"); 
3836 |     if (shmem_real4_sum_to_all__h == NULL) {
3837 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3838 |       return;
3839 |     }
3856 |   float retval = 0;
3857 |   TAU_PROFILE_TIMER(t,"float shmem_real4_swap_(void *, float *, int *)", "", TAU_USER);
3858 |   if (tau_handle == NULL) 
3859 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3860 | 
3861 |   if (tau_handle == NULL) { 
3862 |     perror("Error opening library in dlopen call"); 
3863 |     return retval;
3864 |   } 
3866 |     if (shmem_real4_swap__h == NULL)
3867 | 	shmem_real4_swap__h = (shmem_real4_swap__p_h) dlsym(tau_handle,"shmem_real4_swap_"); 
3868 |     if (shmem_real4_swap__h == NULL) {
3869 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3870 |       return retval;
3871 |     }
3892 |   static shmem_real8_max_to_all__p_h shmem_real8_max_to_all__h = NULL;
3893 |   TAU_PROFILE_TIMER(t,"void shmem_real8_max_to_all_(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
3894 |   if (tau_handle == NULL) 
3895 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3896 | 
3897 |   if (tau_handle == NULL) { 
3898 |     perror("Error opening library in dlopen call"); 
3899 |     return;
3900 |   } 
3902 |     if (shmem_real8_max_to_all__h == NULL)
3903 | 	shmem_real8_max_to_all__h = (shmem_real8_max_to_all__p_h) dlsym(tau_handle,"shmem_real8_max_to_all_"); 
3904 |     if (shmem_real8_max_to_all__h == NULL) {
3905 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3906 |       return;
3907 |     }
3923 |   static shmem_real8_min_to_all__p_h shmem_real8_min_to_all__h = NULL;
3924 |   TAU_PROFILE_TIMER(t,"void shmem_real8_min_to_all_(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
3925 |   if (tau_handle == NULL) 
3926 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3927 | 
3928 |   if (tau_handle == NULL) { 
3929 |     perror("Error opening library in dlopen call"); 
3930 |     return;
3931 |   } 
3933 |     if (shmem_real8_min_to_all__h == NULL)
3934 | 	shmem_real8_min_to_all__h = (shmem_real8_min_to_all__p_h) dlsym(tau_handle,"shmem_real8_min_to_all_"); 
3935 |     if (shmem_real8_min_to_all__h == NULL) {
3936 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3937 |       return;
3938 |     }
3954 |   static shmem_real8_prod_to_all__p_h shmem_real8_prod_to_all__h = NULL;
3955 |   TAU_PROFILE_TIMER(t,"void shmem_real8_prod_to_all_(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
3956 |   if (tau_handle == NULL) 
3957 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3958 | 
3959 |   if (tau_handle == NULL) { 
3960 |     perror("Error opening library in dlopen call"); 
3961 |     return;
3962 |   } 
3964 |     if (shmem_real8_prod_to_all__h == NULL)
3965 | 	shmem_real8_prod_to_all__h = (shmem_real8_prod_to_all__p_h) dlsym(tau_handle,"shmem_real8_prod_to_all_"); 
3966 |     if (shmem_real8_prod_to_all__h == NULL) {
3967 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3968 |       return;
3969 |     }
3985 |   static shmem_real8_sum_to_all__p_h shmem_real8_sum_to_all__h = NULL;
3986 |   TAU_PROFILE_TIMER(t,"void shmem_real8_sum_to_all_(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
3987 |   if (tau_handle == NULL) 
3988 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3989 | 
3990 |   if (tau_handle == NULL) { 
3991 |     perror("Error opening library in dlopen call"); 
3992 |     return;
3993 |   } 
3995 |     if (shmem_real8_sum_to_all__h == NULL)
3996 | 	shmem_real8_sum_to_all__h = (shmem_real8_sum_to_all__p_h) dlsym(tau_handle,"shmem_real8_sum_to_all_"); 
3997 |     if (shmem_real8_sum_to_all__h == NULL) {
3998 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3999 |       return;
4000 |     }
4017 |   double retval = 0;
4018 |   TAU_PROFILE_TIMER(t,"double shmem_real8_swap_(void *, double *, int *)", "", TAU_USER);
4019 |   if (tau_handle == NULL) 
4020 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4021 | 
4022 |   if (tau_handle == NULL) { 
4023 |     perror("Error opening library in dlopen call"); 
4024 |     return retval;
4025 |   } 
4027 |     if (shmem_real8_swap__h == NULL)
4028 | 	shmem_real8_swap__h = (shmem_real8_swap__p_h) dlsym(tau_handle,"shmem_real8_swap_"); 
4029 |     if (shmem_real8_swap__h == NULL) {
4030 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4031 |       return retval;
4032 |     }
4053 |   static shmem_real_get__p_h shmem_real_get__h = NULL;
4054 |   TAU_PROFILE_TIMER(t,"void shmem_real_get_(void *, void *, int *, int *)", "", TAU_USER);
4055 |   if (tau_handle == NULL) 
4056 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4057 | 
4058 |   if (tau_handle == NULL) { 
4059 |     perror("Error opening library in dlopen call"); 
4060 |     return;
4061 |   } 
4063 |     if (shmem_real_get__h == NULL)
4064 | 	shmem_real_get__h = (shmem_real_get__p_h) dlsym(tau_handle,"shmem_real_get_"); 
4065 |     if (shmem_real_get__h == NULL) {
4066 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4067 |       return;
4068 |     }
4086 |   static shmem_real_iget__p_h shmem_real_iget__h = NULL;
4087 |   TAU_PROFILE_TIMER(t,"void shmem_real_iget_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
4088 |   if (tau_handle == NULL) 
4089 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4090 | 
4091 |   if (tau_handle == NULL) { 
4092 |     perror("Error opening library in dlopen call"); 
4093 |     return;
4094 |   } 
4096 |     if (shmem_real_iget__h == NULL)
4097 | 	shmem_real_iget__h = (shmem_real_iget__p_h) dlsym(tau_handle,"shmem_real_iget_"); 
4098 |     if (shmem_real_iget__h == NULL) {
4099 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4100 |       return;
4101 |     }
4119 |   static shmem_real_iput__p_h shmem_real_iput__h = NULL;
4120 |   TAU_PROFILE_TIMER(t,"void shmem_real_iput_(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
4121 |   if (tau_handle == NULL) 
4122 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4123 | 
4124 |   if (tau_handle == NULL) { 
4125 |     perror("Error opening library in dlopen call"); 
4126 |     return;
4127 |   } 
4129 |     if (shmem_real_iput__h == NULL)
4130 | 	shmem_real_iput__h = (shmem_real_iput__p_h) dlsym(tau_handle,"shmem_real_iput_"); 
4131 |     if (shmem_real_iput__h == NULL) {
4132 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4133 |       return;
4134 |     }
4152 |   static shmem_real_put__p_h shmem_real_put__h = NULL;
4153 |   TAU_PROFILE_TIMER(t,"void shmem_real_put_(void *, void *, int *, int *)", "", TAU_USER);
4154 |   if (tau_handle == NULL) 
4155 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4156 | 
4157 |   if (tau_handle == NULL) { 
4158 |     perror("Error opening library in dlopen call"); 
4159 |     return;
4160 |   } 
4162 |     if (shmem_real_put__h == NULL)
4163 | 	shmem_real_put__h = (shmem_real_put__p_h) dlsym(tau_handle,"shmem_real_put_"); 
4164 |     if (shmem_real_put__h == NULL) {
4165 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4166 |       return;
4167 |     }
4185 |   static shmem_set_cache_inv__p_h shmem_set_cache_inv__h = NULL;
4186 |   TAU_PROFILE_TIMER(t,"void shmem_set_cache_inv_()", "", TAU_USER);
4187 |   if (tau_handle == NULL) 
4188 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4189 | 
4190 |   if (tau_handle == NULL) { 
4191 |     perror("Error opening library in dlopen call"); 
4192 |     return;
4193 |   } 
4195 |     if (shmem_set_cache_inv__h == NULL)
4196 | 	shmem_set_cache_inv__h = (shmem_set_cache_inv__p_h) dlsym(tau_handle,"shmem_set_cache_inv_"); 
4197 |     if (shmem_set_cache_inv__h == NULL) {
4198 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4199 |       return;
4200 |     }
4216 |   static shmem_set_cache_line_inv__p_h shmem_set_cache_line_inv__h = NULL;
4217 |   TAU_PROFILE_TIMER(t,"void shmem_set_cache_line_inv_(void *)", "", TAU_USER);
4218 |   if (tau_handle == NULL) 
4219 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4220 | 
4221 |   if (tau_handle == NULL) { 
4222 |     perror("Error opening library in dlopen call"); 
4223 |     return;
4224 |   } 
4226 |     if (shmem_set_cache_line_inv__h == NULL)
4227 | 	shmem_set_cache_line_inv__h = (shmem_set_cache_line_inv__p_h) dlsym(tau_handle,"shmem_set_cache_line_inv_"); 
4228 |     if (shmem_set_cache_line_inv__h == NULL) {
4229 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4230 |       return;
4231 |     }
4247 |   static shmem_set_lock__p_h shmem_set_lock__h = NULL;
4248 |   TAU_PROFILE_TIMER(t,"void shmem_set_lock_(long *)", "", TAU_USER);
4249 |   if (tau_handle == NULL) 
4250 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4251 | 
4252 |   if (tau_handle == NULL) { 
4253 |     perror("Error opening library in dlopen call"); 
4254 |     return;
4255 |   } 
4257 |     if (shmem_set_lock__h == NULL)
4258 | 	shmem_set_lock__h = (shmem_set_lock__p_h) dlsym(tau_handle,"shmem_set_lock_"); 
4259 |     if (shmem_set_lock__h == NULL) {
4260 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4261 |       return;
4262 |     }
4279 |   int retval = 0;
4280 |   TAU_PROFILE_TIMER(t,"int shmem_swap_(void *, int *, int *)", "", TAU_USER);
4281 |   if (tau_handle == NULL) 
4282 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4283 | 
4284 |   if (tau_handle == NULL) { 
4285 |     perror("Error opening library in dlopen call"); 
4286 |     return retval;
4287 |   } 
4289 |     if (shmem_swap__h == NULL)
4290 | 	shmem_swap__h = (shmem_swap__p_h) dlsym(tau_handle,"shmem_swap_"); 
4291 |     if (shmem_swap__h == NULL) {
4292 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4293 |       return retval;
4294 |     }
4316 |   int retval = 0;
4317 |   TAU_PROFILE_TIMER(t,"int shmem_test_lock_(long *)", "", TAU_USER);
4318 |   if (tau_handle == NULL) 
4319 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4320 | 
4321 |   if (tau_handle == NULL) { 
4322 |     perror("Error opening library in dlopen call"); 
4323 |     return retval;
4324 |   } 
4326 |     if (shmem_test_lock__h == NULL)
4327 | 	shmem_test_lock__h = (shmem_test_lock__p_h) dlsym(tau_handle,"shmem_test_lock_"); 
4328 |     if (shmem_test_lock__h == NULL) {
4329 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4330 |       return retval;
4331 |     }
4348 |   static shmem_udcflush__p_h shmem_udcflush__h = NULL;
4349 |   TAU_PROFILE_TIMER(t,"void shmem_udcflush_()", "", TAU_USER);
4350 |   if (tau_handle == NULL) 
4351 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4352 | 
4353 |   if (tau_handle == NULL) { 
4354 |     perror("Error opening library in dlopen call"); 
4355 |     return;
4356 |   } 
4358 |     if (shmem_udcflush__h == NULL)
4359 | 	shmem_udcflush__h = (shmem_udcflush__p_h) dlsym(tau_handle,"shmem_udcflush_"); 
4360 |     if (shmem_udcflush__h == NULL) {
4361 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4362 |       return;
4363 |     }
4379 |   static shmem_udcflush_line__p_h shmem_udcflush_line__h = NULL;
4380 |   TAU_PROFILE_TIMER(t,"void shmem_udcflush_line_(void *)", "", TAU_USER);
4381 |   if (tau_handle == NULL) 
4382 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4383 | 
4384 |   if (tau_handle == NULL) { 
4385 |     perror("Error opening library in dlopen call"); 
4386 |     return;
4387 |   } 
4389 |     if (shmem_udcflush_line__h == NULL)
4390 | 	shmem_udcflush_line__h = (shmem_udcflush_line__p_h) dlsym(tau_handle,"shmem_udcflush_line_"); 
4391 |     if (shmem_udcflush_line__h == NULL) {
4392 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4393 |       return;
4394 |     }
4410 |   static shmem_wait__p_h shmem_wait__h = NULL;
4411 |   TAU_PROFILE_TIMER(t,"void shmem_wait_(long *, long *)", "", TAU_USER);
4412 |   if (tau_handle == NULL) 
4413 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4414 | 
4415 |   if (tau_handle == NULL) { 
4416 |     perror("Error opening library in dlopen call"); 
4417 |     return;
4418 |   } 
4420 |     if (shmem_wait__h == NULL)
4421 | 	shmem_wait__h = (shmem_wait__p_h) dlsym(tau_handle,"shmem_wait_"); 
4422 |     if (shmem_wait__h == NULL) {
4423 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4424 |       return;
4425 |     }
4441 |   static shmem_wait_until__p_h shmem_wait_until__h = NULL;
4442 |   TAU_PROFILE_TIMER(t,"void shmem_wait_until_(int *, int *, int *)", "", TAU_USER);
4443 |   if (tau_handle == NULL) 
4444 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4445 | 
4446 |   if (tau_handle == NULL) { 
4447 |     perror("Error opening library in dlopen call"); 
4448 |     return;
4449 |   } 
4451 |     if (shmem_wait_until__h == NULL)
4452 | 	shmem_wait_until__h = (shmem_wait_until__p_h) dlsym(tau_handle,"shmem_wait_until_"); 
4453 |     if (shmem_wait_until__h == NULL) {
4454 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4455 |       return;
4456 |     }
4472 |   static start_pes__p_h start_pes__h = NULL;
4473 |   TAU_PROFILE_TIMER(t,"void start_pes_(int *)", "", TAU_USER);
4474 |   if (tau_handle == NULL) 
4475 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4476 | 
4477 |   if (tau_handle == NULL) { 
4478 |     perror("Error opening library in dlopen call"); 
4479 |     return;
4480 |   } 
4482 |     if (start_pes__h == NULL)
4483 | 	start_pes__h = (start_pes__p_h) dlsym(tau_handle,"start_pes_"); 
4484 |     if (start_pes__h == NULL) {
4485 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4486 |       return;
4487 |     }
4512 |   static shmem_addr_accessible___p_h shmem_addr_accessible___h = NULL;
4513 |   TAU_PROFILE_TIMER(t,"void shmem_addr_accessible__(void *, int *)", "", TAU_USER);
4514 |   if (tau_handle == NULL) 
4515 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4516 | 
4517 |   if (tau_handle == NULL) { 
4518 |     perror("Error opening library in dlopen call"); 
4519 |     return;
4520 |   } 
4522 |     if (shmem_addr_accessible___h == NULL)
4523 | 	shmem_addr_accessible___h = (shmem_addr_accessible___p_h) dlsym(tau_handle,"shmem_addr_accessible__"); 
4524 |     if (shmem_addr_accessible___h == NULL) {
4525 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4526 |       return;
4527 |     }
4543 |   static shmem_barrier___p_h shmem_barrier___h = NULL;
4544 |   TAU_PROFILE_TIMER(t,"void shmem_barrier__(int *, int *, int *, long *)", "", TAU_USER);
4545 |   if (tau_handle == NULL) 
4546 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4547 | 
4548 |   if (tau_handle == NULL) { 
4549 |     perror("Error opening library in dlopen call"); 
4550 |     return;
4551 |   } 
4553 |     if (shmem_barrier___h == NULL)
4554 | 	shmem_barrier___h = (shmem_barrier___p_h) dlsym(tau_handle,"shmem_barrier__"); 
4555 |     if (shmem_barrier___h == NULL) {
4556 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4557 |       return;
4558 |     }
4574 |   static shmem_barrier_all___p_h shmem_barrier_all___h = NULL;
4575 |   TAU_PROFILE_TIMER(t,"void shmem_barrier_all__()", "", TAU_USER);
4576 |   if (tau_handle == NULL) 
4577 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4578 | 
4579 |   if (tau_handle == NULL) { 
4580 |     perror("Error opening library in dlopen call"); 
4581 |     return;
4582 |   } 
4584 |     if (shmem_barrier_all___h == NULL)
4585 | 	shmem_barrier_all___h = (shmem_barrier_all___p_h) dlsym(tau_handle,"shmem_barrier_all__"); 
4586 |     if (shmem_barrier_all___h == NULL) {
4587 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4588 |       return;
4589 |     }
4605 |   static shmem_barrier_ps___p_h shmem_barrier_ps___h = NULL;
4606 |   TAU_PROFILE_TIMER(t,"void shmem_barrier_ps__(int *, int *, int *, long *)", "", TAU_USER);
4607 |   if (tau_handle == NULL) 
4608 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4609 | 
4610 |   if (tau_handle == NULL) { 
4611 |     perror("Error opening library in dlopen call"); 
4612 |     return;
4613 |   } 
4615 |     if (shmem_barrier_ps___h == NULL)
4616 | 	shmem_barrier_ps___h = (shmem_barrier_ps___p_h) dlsym(tau_handle,"shmem_barrier_ps__"); 
4617 |     if (shmem_barrier_ps___h == NULL) {
4618 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4619 |       return;
4620 |     }
4636 |   static shmem_broadcast32___p_h shmem_broadcast32___h = NULL;
4637 |   TAU_PROFILE_TIMER(t,"void shmem_broadcast32__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
4638 |   if (tau_handle == NULL) 
4639 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4640 | 
4641 |   if (tau_handle == NULL) { 
4642 |     perror("Error opening library in dlopen call"); 
4643 |     return;
4644 |   } 
4646 |     if (shmem_broadcast32___h == NULL)
4647 | 	shmem_broadcast32___h = (shmem_broadcast32___p_h) dlsym(tau_handle,"shmem_broadcast32__"); 
4648 |     if (shmem_broadcast32___h == NULL) {
4649 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4650 |       return;
4651 |     }
4667 |   static shmem_broadcast4___p_h shmem_broadcast4___h = NULL;
4668 |   TAU_PROFILE_TIMER(t,"void shmem_broadcast4__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
4669 |   if (tau_handle == NULL) 
4670 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4671 | 
4672 |   if (tau_handle == NULL) { 
4673 |     perror("Error opening library in dlopen call"); 
4674 |     return;
4675 |   } 
4677 |     if (shmem_broadcast4___h == NULL)
4678 | 	shmem_broadcast4___h = (shmem_broadcast4___p_h) dlsym(tau_handle,"shmem_broadcast4__"); 
4679 |     if (shmem_broadcast4___h == NULL) {
4680 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4681 |       return;
4682 |     }
4698 |   static shmem_broadcast64___p_h shmem_broadcast64___h = NULL;
4699 |   TAU_PROFILE_TIMER(t,"void shmem_broadcast64__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
4700 |   if (tau_handle == NULL) 
4701 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4702 | 
4703 |   if (tau_handle == NULL) { 
4704 |     perror("Error opening library in dlopen call"); 
4705 |     return;
4706 |   } 
4708 |     if (shmem_broadcast64___h == NULL)
4709 | 	shmem_broadcast64___h = (shmem_broadcast64___p_h) dlsym(tau_handle,"shmem_broadcast64__"); 
4710 |     if (shmem_broadcast64___h == NULL) {
4711 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4712 |       return;
4713 |     }
4729 |   static shmem_broadcast8___p_h shmem_broadcast8___h = NULL;
4730 |   TAU_PROFILE_TIMER(t,"void shmem_broadcast8__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
4731 |   if (tau_handle == NULL) 
4732 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4733 | 
4734 |   if (tau_handle == NULL) { 
4735 |     perror("Error opening library in dlopen call"); 
4736 |     return;
4737 |   } 
4739 |     if (shmem_broadcast8___h == NULL)
4740 | 	shmem_broadcast8___h = (shmem_broadcast8___p_h) dlsym(tau_handle,"shmem_broadcast8__"); 
4741 |     if (shmem_broadcast8___h == NULL) {
4742 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4743 |       return;
4744 |     }
4760 |   static shmem_character_get___p_h shmem_character_get___h = NULL;
4761 |   TAU_PROFILE_TIMER(t,"void shmem_character_get__(void *, void *, int *, int *)", "", TAU_USER);
4762 |   if (tau_handle == NULL) 
4763 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4764 | 
4765 |   if (tau_handle == NULL) { 
4766 |     perror("Error opening library in dlopen call"); 
4767 |     return;
4768 |   } 
4770 |     if (shmem_character_get___h == NULL)
4771 | 	shmem_character_get___h = (shmem_character_get___p_h) dlsym(tau_handle,"shmem_character_get__"); 
4772 |     if (shmem_character_get___h == NULL) {
4773 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4774 |       return;
4775 |     }
4793 |   static shmem_character_put___p_h shmem_character_put___h = NULL;
4794 |   TAU_PROFILE_TIMER(t,"void shmem_character_put__(void *, void *, int *, int *)", "", TAU_USER);
4795 |   if (tau_handle == NULL) 
4796 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4797 | 
4798 |   if (tau_handle == NULL) { 
4799 |     perror("Error opening library in dlopen call"); 
4800 |     return;
4801 |   } 
4803 |     if (shmem_character_put___h == NULL)
4804 | 	shmem_character_put___h = (shmem_character_put___p_h) dlsym(tau_handle,"shmem_character_put__"); 
4805 |     if (shmem_character_put___h == NULL) {
4806 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4807 |       return;
4808 |     }
4826 |   static shmem_clear_cache_inv___p_h shmem_clear_cache_inv___h = NULL;
4827 |   TAU_PROFILE_TIMER(t,"void shmem_clear_cache_inv__()", "", TAU_USER);
4828 |   if (tau_handle == NULL) 
4829 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4830 | 
4831 |   if (tau_handle == NULL) { 
4832 |     perror("Error opening library in dlopen call"); 
4833 |     return;
4834 |   } 
4836 |     if (shmem_clear_cache_inv___h == NULL)
4837 | 	shmem_clear_cache_inv___h = (shmem_clear_cache_inv___p_h) dlsym(tau_handle,"shmem_clear_cache_inv__"); 
4838 |     if (shmem_clear_cache_inv___h == NULL) {
4839 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4840 |       return;
4841 |     }
4857 |   static shmem_clear_cache_line_inv___p_h shmem_clear_cache_line_inv___h = NULL;
4858 |   TAU_PROFILE_TIMER(t,"void shmem_clear_cache_line_inv__(void *)", "", TAU_USER);
4859 |   if (tau_handle == NULL) 
4860 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4861 | 
4862 |   if (tau_handle == NULL) { 
4863 |     perror("Error opening library in dlopen call"); 
4864 |     return;
4865 |   } 
4867 |     if (shmem_clear_cache_line_inv___h == NULL)
4868 | 	shmem_clear_cache_line_inv___h = (shmem_clear_cache_line_inv___p_h) dlsym(tau_handle,"shmem_clear_cache_line_inv__"); 
4869 |     if (shmem_clear_cache_line_inv___h == NULL) {
4870 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4871 |       return;
4872 |     }
4888 |   static shmem_clear_lock___p_h shmem_clear_lock___h = NULL;
4889 |   TAU_PROFILE_TIMER(t,"void shmem_clear_lock__(long *)", "", TAU_USER);
4890 |   if (tau_handle == NULL) 
4891 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4892 | 
4893 |   if (tau_handle == NULL) { 
4894 |     perror("Error opening library in dlopen call"); 
4895 |     return;
4896 |   } 
4898 |     if (shmem_clear_lock___h == NULL)
4899 | 	shmem_clear_lock___h = (shmem_clear_lock___p_h) dlsym(tau_handle,"shmem_clear_lock__"); 
4900 |     if (shmem_clear_lock___h == NULL) {
4901 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4902 |       return;
4903 |     }
4919 |   static shmem_collect4___p_h shmem_collect4___h = NULL;
4920 |   TAU_PROFILE_TIMER(t,"void shmem_collect4__(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
4921 |   if (tau_handle == NULL) 
4922 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4923 | 
4924 |   if (tau_handle == NULL) { 
4925 |     perror("Error opening library in dlopen call"); 
4926 |     return;
4927 |   } 
4929 |     if (shmem_collect4___h == NULL)
4930 | 	shmem_collect4___h = (shmem_collect4___p_h) dlsym(tau_handle,"shmem_collect4__"); 
4931 |     if (shmem_collect4___h == NULL) {
4932 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4933 |       return;
4934 |     }
4950 |   static shmem_collect64___p_h shmem_collect64___h = NULL;
4951 |   TAU_PROFILE_TIMER(t,"void shmem_collect64__(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
4952 |   if (tau_handle == NULL) 
4953 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4954 | 
4955 |   if (tau_handle == NULL) { 
4956 |     perror("Error opening library in dlopen call"); 
4957 |     return;
4958 |   } 
4960 |     if (shmem_collect64___h == NULL)
4961 | 	shmem_collect64___h = (shmem_collect64___p_h) dlsym(tau_handle,"shmem_collect64__"); 
4962 |     if (shmem_collect64___h == NULL) {
4963 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4964 |       return;
4965 |     }
4981 |   static shmem_collect8___p_h shmem_collect8___h = NULL;
4982 |   TAU_PROFILE_TIMER(t,"void shmem_collect8__(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
4983 |   if (tau_handle == NULL) 
4984 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4985 | 
4986 |   if (tau_handle == NULL) { 
4987 |     perror("Error opening library in dlopen call"); 
4988 |     return;
4989 |   } 
4991 |     if (shmem_collect8___h == NULL)
4992 | 	shmem_collect8___h = (shmem_collect8___p_h) dlsym(tau_handle,"shmem_collect8__"); 
4993 |     if (shmem_collect8___h == NULL) {
4994 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4995 |       return;
4996 |     }
5012 |   static shmem_comp4_prod_to_all___p_h shmem_comp4_prod_to_all___h = NULL;
5013 |   TAU_PROFILE_TIMER(t,"void shmem_comp4_prod_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
5014 |   if (tau_handle == NULL) 
5015 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5016 | 
5017 |   if (tau_handle == NULL) { 
5018 |     perror("Error opening library in dlopen call"); 
5019 |     return;
5020 |   } 
5022 |     if (shmem_comp4_prod_to_all___h == NULL)
5023 | 	shmem_comp4_prod_to_all___h = (shmem_comp4_prod_to_all___p_h) dlsym(tau_handle,"shmem_comp4_prod_to_all__"); 
5024 |     if (shmem_comp4_prod_to_all___h == NULL) {
5025 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5026 |       return;
5027 |     }
5043 |   static shmem_comp4_sum_to_all___p_h shmem_comp4_sum_to_all___h = NULL;
5044 |   TAU_PROFILE_TIMER(t,"void shmem_comp4_sum_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
5045 |   if (tau_handle == NULL) 
5046 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5047 | 
5048 |   if (tau_handle == NULL) { 
5049 |     perror("Error opening library in dlopen call"); 
5050 |     return;
5051 |   } 
5053 |     if (shmem_comp4_sum_to_all___h == NULL)
5054 | 	shmem_comp4_sum_to_all___h = (shmem_comp4_sum_to_all___p_h) dlsym(tau_handle,"shmem_comp4_sum_to_all__"); 
5055 |     if (shmem_comp4_sum_to_all___h == NULL) {
5056 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5057 |       return;
5058 |     }
5074 |   static shmem_comp8_prod_to_all___p_h shmem_comp8_prod_to_all___h = NULL;
5075 |   TAU_PROFILE_TIMER(t,"void shmem_comp8_prod_to_all__(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
5076 |   if (tau_handle == NULL) 
5077 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5078 | 
5079 |   if (tau_handle == NULL) { 
5080 |     perror("Error opening library in dlopen call"); 
5081 |     return;
5082 |   } 
5084 |     if (shmem_comp8_prod_to_all___h == NULL)
5085 | 	shmem_comp8_prod_to_all___h = (shmem_comp8_prod_to_all___p_h) dlsym(tau_handle,"shmem_comp8_prod_to_all__"); 
5086 |     if (shmem_comp8_prod_to_all___h == NULL) {
5087 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5088 |       return;
5089 |     }
5105 |   static shmem_comp8_sum_to_all___p_h shmem_comp8_sum_to_all___h = NULL;
5106 |   TAU_PROFILE_TIMER(t,"void shmem_comp8_sum_to_all__(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
5107 |   if (tau_handle == NULL) 
5108 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5109 | 
5110 |   if (tau_handle == NULL) { 
5111 |     perror("Error opening library in dlopen call"); 
5112 |     return;
5113 |   } 
5115 |     if (shmem_comp8_sum_to_all___h == NULL)
5116 | 	shmem_comp8_sum_to_all___h = (shmem_comp8_sum_to_all___p_h) dlsym(tau_handle,"shmem_comp8_sum_to_all__"); 
5117 |     if (shmem_comp8_sum_to_all___h == NULL) {
5118 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5119 |       return;
5120 |     }
5136 |   static shmem_complex_get___p_h shmem_complex_get___h = NULL;
5137 |   TAU_PROFILE_TIMER(t,"void shmem_complex_get__(void *, void *, int *, int *)", "", TAU_USER);
5138 |   if (tau_handle == NULL) 
5139 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5140 | 
5141 |   if (tau_handle == NULL) { 
5142 |     perror("Error opening library in dlopen call"); 
5143 |     return;
5144 |   } 
5146 |     if (shmem_complex_get___h == NULL)
5147 | 	shmem_complex_get___h = (shmem_complex_get___p_h) dlsym(tau_handle,"shmem_complex_get__"); 
5148 |     if (shmem_complex_get___h == NULL) {
5149 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5150 |       return;
5151 |     }
5169 |   static shmem_complex_iget___p_h shmem_complex_iget___h = NULL;
5170 |   TAU_PROFILE_TIMER(t,"void shmem_complex_iget__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
5171 |   if (tau_handle == NULL) 
5172 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5173 | 
5174 |   if (tau_handle == NULL) { 
5175 |     perror("Error opening library in dlopen call"); 
5176 |     return;
5177 |   } 
5179 |     if (shmem_complex_iget___h == NULL)
5180 | 	shmem_complex_iget___h = (shmem_complex_iget___p_h) dlsym(tau_handle,"shmem_complex_iget__"); 
5181 |     if (shmem_complex_iget___h == NULL) {
5182 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5183 |       return;
5184 |     }
5202 |   static shmem_complex_iput___p_h shmem_complex_iput___h = NULL;
5203 |   TAU_PROFILE_TIMER(t,"void shmem_complex_iput__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
5204 |   if (tau_handle == NULL) 
5205 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5206 | 
5207 |   if (tau_handle == NULL) { 
5208 |     perror("Error opening library in dlopen call"); 
5209 |     return;
5210 |   } 
5212 |     if (shmem_complex_iput___h == NULL)
5213 | 	shmem_complex_iput___h = (shmem_complex_iput___p_h) dlsym(tau_handle,"shmem_complex_iput__"); 
5214 |     if (shmem_complex_iput___h == NULL) {
5215 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5216 |       return;
5217 |     }
5235 |   static shmem_complex_put___p_h shmem_complex_put___h = NULL;
5236 |   TAU_PROFILE_TIMER(t,"void shmem_complex_put__(void *, void *, int *, int *)", "", TAU_USER);
5237 |   if (tau_handle == NULL) 
5238 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5239 | 
5240 |   if (tau_handle == NULL) { 
5241 |     perror("Error opening library in dlopen call"); 
5242 |     return;
5243 |   } 
5245 |     if (shmem_complex_put___h == NULL)
5246 | 	shmem_complex_put___h = (shmem_complex_put___p_h) dlsym(tau_handle,"shmem_complex_put__"); 
5247 |     if (shmem_complex_put___h == NULL) {
5248 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5249 |       return;
5250 |     }
5268 |   static shmem_double_get___p_h shmem_double_get___h = NULL;
5269 |   TAU_PROFILE_TIMER(t,"void shmem_double_get__(void *, void *, int *, int *)", "", TAU_USER);
5270 |   if (tau_handle == NULL) 
5271 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5272 | 
5273 |   if (tau_handle == NULL) { 
5274 |     perror("Error opening library in dlopen call"); 
5275 |     return;
5276 |   } 
5278 |     if (shmem_double_get___h == NULL)
5279 | 	shmem_double_get___h = (shmem_double_get___p_h) dlsym(tau_handle,"shmem_double_get__"); 
5280 |     if (shmem_double_get___h == NULL) {
5281 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5282 |       return;
5283 |     }
5301 |   static shmem_double_iget___p_h shmem_double_iget___h = NULL;
5302 |   TAU_PROFILE_TIMER(t,"void shmem_double_iget__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
5303 |   if (tau_handle == NULL) 
5304 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5305 | 
5306 |   if (tau_handle == NULL) { 
5307 |     perror("Error opening library in dlopen call"); 
5308 |     return;
5309 |   } 
5311 |     if (shmem_double_iget___h == NULL)
5312 | 	shmem_double_iget___h = (shmem_double_iget___p_h) dlsym(tau_handle,"shmem_double_iget__"); 
5313 |     if (shmem_double_iget___h == NULL) {
5314 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5315 |       return;
5316 |     }
5334 |   static shmem_double_iput___p_h shmem_double_iput___h = NULL;
5335 |   TAU_PROFILE_TIMER(t,"void shmem_double_iput__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
5336 |   if (tau_handle == NULL) 
5337 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5338 | 
5339 |   if (tau_handle == NULL) { 
5340 |     perror("Error opening library in dlopen call"); 
5341 |     return;
5342 |   } 
5344 |     if (shmem_double_iput___h == NULL)
5345 | 	shmem_double_iput___h = (shmem_double_iput___p_h) dlsym(tau_handle,"shmem_double_iput__"); 
5346 |     if (shmem_double_iput___h == NULL) {
5347 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5348 |       return;
5349 |     }
5367 |   static shmem_double_put___p_h shmem_double_put___h = NULL;
5368 |   TAU_PROFILE_TIMER(t,"void shmem_double_put__(void *, void *, int *, int *)", "", TAU_USER);
5369 |   if (tau_handle == NULL) 
5370 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5371 | 
5372 |   if (tau_handle == NULL) { 
5373 |     perror("Error opening library in dlopen call"); 
5374 |     return;
5375 |   } 
5377 |     if (shmem_double_put___h == NULL)
5378 | 	shmem_double_put___h = (shmem_double_put___p_h) dlsym(tau_handle,"shmem_double_put__"); 
5379 |     if (shmem_double_put___h == NULL) {
5380 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5381 |       return;
5382 |     }
5400 |   static shmem_fcollect32___p_h shmem_fcollect32___h = NULL;
5401 |   TAU_PROFILE_TIMER(t,"void shmem_fcollect32__(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
5402 |   if (tau_handle == NULL) 
5403 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5404 | 
5405 |   if (tau_handle == NULL) { 
5406 |     perror("Error opening library in dlopen call"); 
5407 |     return;
5408 |   } 
5410 |     if (shmem_fcollect32___h == NULL)
5411 | 	shmem_fcollect32___h = (shmem_fcollect32___p_h) dlsym(tau_handle,"shmem_fcollect32__"); 
5412 |     if (shmem_fcollect32___h == NULL) {
5413 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5414 |       return;
5415 |     }
5431 |   static shmem_fcollect4___p_h shmem_fcollect4___h = NULL;
5432 |   TAU_PROFILE_TIMER(t,"void shmem_fcollect4__(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
5433 |   if (tau_handle == NULL) 
5434 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5435 | 
5436 |   if (tau_handle == NULL) { 
5437 |     perror("Error opening library in dlopen call"); 
5438 |     return;
5439 |   } 
5441 |     if (shmem_fcollect4___h == NULL)
5442 | 	shmem_fcollect4___h = (shmem_fcollect4___p_h) dlsym(tau_handle,"shmem_fcollect4__"); 
5443 |     if (shmem_fcollect4___h == NULL) {
5444 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5445 |       return;
5446 |     }
5462 |   static shmem_fcollect64___p_h shmem_fcollect64___h = NULL;
5463 |   TAU_PROFILE_TIMER(t,"void shmem_fcollect64__(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
5464 |   if (tau_handle == NULL) 
5465 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5466 | 
5467 |   if (tau_handle == NULL) { 
5468 |     perror("Error opening library in dlopen call"); 
5469 |     return;
5470 |   } 
5472 |     if (shmem_fcollect64___h == NULL)
5473 | 	shmem_fcollect64___h = (shmem_fcollect64___p_h) dlsym(tau_handle,"shmem_fcollect64__"); 
5474 |     if (shmem_fcollect64___h == NULL) {
5475 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5476 |       return;
5477 |     }
5493 |   static shmem_fcollect8___p_h shmem_fcollect8___h = NULL;
5494 |   TAU_PROFILE_TIMER(t,"void shmem_fcollect8__(void *, void *, int *, int *, int *, int *, long *)", "", TAU_USER);
5495 |   if (tau_handle == NULL) 
5496 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5497 | 
5498 |   if (tau_handle == NULL) { 
5499 |     perror("Error opening library in dlopen call"); 
5500 |     return;
5501 |   } 
5503 |     if (shmem_fcollect8___h == NULL)
5504 | 	shmem_fcollect8___h = (shmem_fcollect8___p_h) dlsym(tau_handle,"shmem_fcollect8__"); 
5505 |     if (shmem_fcollect8___h == NULL) {
5506 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5507 |       return;
5508 |     }
5524 |   static shmem_fence___p_h shmem_fence___h = NULL;
5525 |   TAU_PROFILE_TIMER(t,"void shmem_fence__()", "", TAU_USER);
5526 |   if (tau_handle == NULL) 
5527 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5528 | 
5529 |   if (tau_handle == NULL) { 
5530 |     perror("Error opening library in dlopen call"); 
5531 |     return;
5532 |   } 
5534 |     if (shmem_fence___h == NULL)
5535 | 	shmem_fence___h = (shmem_fence___p_h) dlsym(tau_handle,"shmem_fence__"); 
5536 |     if (shmem_fence___h == NULL) {
5537 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5538 |       return;
5539 |     }
5555 |   static shmem_get128___p_h shmem_get128___h = NULL;
5556 |   TAU_PROFILE_TIMER(t,"void shmem_get128__(void *, void *, int *, int *)", "", TAU_USER);
5557 |   if (tau_handle == NULL) 
5558 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5559 | 
5560 |   if (tau_handle == NULL) { 
5561 |     perror("Error opening library in dlopen call"); 
5562 |     return;
5563 |   } 
5565 |     if (shmem_get128___h == NULL)
5566 | 	shmem_get128___h = (shmem_get128___p_h) dlsym(tau_handle,"shmem_get128__"); 
5567 |     if (shmem_get128___h == NULL) {
5568 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5569 |       return;
5570 |     }
5588 |   static shmem_get16___p_h shmem_get16___h = NULL;
5589 |   TAU_PROFILE_TIMER(t,"void shmem_get16__(void *, void *, int *, int *)", "", TAU_USER);
5590 |   if (tau_handle == NULL) 
5591 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5592 | 
5593 |   if (tau_handle == NULL) { 
5594 |     perror("Error opening library in dlopen call"); 
5595 |     return;
5596 |   } 
5598 |     if (shmem_get16___h == NULL)
5599 | 	shmem_get16___h = (shmem_get16___p_h) dlsym(tau_handle,"shmem_get16__"); 
5600 |     if (shmem_get16___h == NULL) {
5601 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5602 |       return;
5603 |     }
5621 |   static shmem_get32___p_h shmem_get32___h = NULL;
5622 |   TAU_PROFILE_TIMER(t,"void shmem_get32__(void *, void *, int *, int *)", "", TAU_USER);
5623 |   if (tau_handle == NULL) 
5624 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5625 | 
5626 |   if (tau_handle == NULL) { 
5627 |     perror("Error opening library in dlopen call"); 
5628 |     return;
5629 |   } 
5631 |     if (shmem_get32___h == NULL)
5632 | 	shmem_get32___h = (shmem_get32___p_h) dlsym(tau_handle,"shmem_get32__"); 
5633 |     if (shmem_get32___h == NULL) {
5634 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5635 |       return;
5636 |     }
5654 |   static shmem_get4___p_h shmem_get4___h = NULL;
5655 |   TAU_PROFILE_TIMER(t,"void shmem_get4__(void *, void *, int *, int *)", "", TAU_USER);
5656 |   if (tau_handle == NULL) 
5657 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5658 | 
5659 |   if (tau_handle == NULL) { 
5660 |     perror("Error opening library in dlopen call"); 
5661 |     return;
5662 |   } 
5664 |     if (shmem_get4___h == NULL)
5665 | 	shmem_get4___h = (shmem_get4___p_h) dlsym(tau_handle,"shmem_get4__"); 
5666 |     if (shmem_get4___h == NULL) {
5667 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5668 |       return;
5669 |     }
5687 |   static shmem_get64___p_h shmem_get64___h = NULL;
5688 |   TAU_PROFILE_TIMER(t,"void shmem_get64__(void *, void *, int *, int *)", "", TAU_USER);
5689 |   if (tau_handle == NULL) 
5690 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5691 | 
5692 |   if (tau_handle == NULL) { 
5693 |     perror("Error opening library in dlopen call"); 
5694 |     return;
5695 |   } 
5697 |     if (shmem_get64___h == NULL)
5698 | 	shmem_get64___h = (shmem_get64___p_h) dlsym(tau_handle,"shmem_get64__"); 
5699 |     if (shmem_get64___h == NULL) {
5700 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5701 |       return;
5702 |     }
5720 |   static shmem_get8___p_h shmem_get8___h = NULL;
5721 |   TAU_PROFILE_TIMER(t,"void shmem_get8__(void *, void *, int *, int *)", "", TAU_USER);
5722 |   if (tau_handle == NULL) 
5723 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5724 | 
5725 |   if (tau_handle == NULL) { 
5726 |     perror("Error opening library in dlopen call"); 
5727 |     return;
5728 |   } 
5730 |     if (shmem_get8___h == NULL)
5731 | 	shmem_get8___h = (shmem_get8___p_h) dlsym(tau_handle,"shmem_get8__"); 
5732 |     if (shmem_get8___h == NULL) {
5733 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5734 |       return;
5735 |     }
5753 |   static shmem_getmem___p_h shmem_getmem___h = NULL;
5754 |   TAU_PROFILE_TIMER(t,"void shmem_getmem__(void *, void *, int *, int *)", "", TAU_USER);
5755 |   if (tau_handle == NULL) 
5756 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5757 | 
5758 |   if (tau_handle == NULL) { 
5759 |     perror("Error opening library in dlopen call"); 
5760 |     return;
5761 |   } 
5763 |     if (shmem_getmem___h == NULL)
5764 | 	shmem_getmem___h = (shmem_getmem___p_h) dlsym(tau_handle,"shmem_getmem__"); 
5765 |     if (shmem_getmem___h == NULL) {
5766 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5767 |       return;
5768 |     }
5786 |   static shmem_group_create_strided___p_h shmem_group_create_strided___h = NULL;
5787 |   TAU_PROFILE_TIMER(t,"void shmem_group_create_strided__(int *, int *, int *, int *, int *, int *)", "", TAU_USER);
5788 |   if (tau_handle == NULL) 
5789 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5790 | 
5791 |   if (tau_handle == NULL) { 
5792 |     perror("Error opening library in dlopen call"); 
5793 |     return;
5794 |   } 
5796 |     if (shmem_group_create_strided___h == NULL)
5797 | 	shmem_group_create_strided___h = (shmem_group_create_strided___p_h) dlsym(tau_handle,"shmem_group_create_strided__"); 
5798 |     if (shmem_group_create_strided___h == NULL) {
5799 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5800 |       return;
5801 |     }
5817 |   static shmem_group_delete___p_h shmem_group_delete___h = NULL;
5818 |   TAU_PROFILE_TIMER(t,"void shmem_group_delete__(int *)", "", TAU_USER);
5819 |   if (tau_handle == NULL) 
5820 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5821 | 
5822 |   if (tau_handle == NULL) { 
5823 |     perror("Error opening library in dlopen call"); 
5824 |     return;
5825 |   } 
5827 |     if (shmem_group_delete___h == NULL)
5828 | 	shmem_group_delete___h = (shmem_group_delete___p_h) dlsym(tau_handle,"shmem_group_delete__"); 
5829 |     if (shmem_group_delete___h == NULL) {
5830 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5831 |       return;
5832 |     }
5848 |   static shmem_iget128___p_h shmem_iget128___h = NULL;
5849 |   TAU_PROFILE_TIMER(t,"void shmem_iget128__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
5850 |   if (tau_handle == NULL) 
5851 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5852 | 
5853 |   if (tau_handle == NULL) { 
5854 |     perror("Error opening library in dlopen call"); 
5855 |     return;
5856 |   } 
5858 |     if (shmem_iget128___h == NULL)
5859 | 	shmem_iget128___h = (shmem_iget128___p_h) dlsym(tau_handle,"shmem_iget128__"); 
5860 |     if (shmem_iget128___h == NULL) {
5861 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5862 |       return;
5863 |     }
5881 |   static shmem_iget16___p_h shmem_iget16___h = NULL;
5882 |   TAU_PROFILE_TIMER(t,"void shmem_iget16__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
5883 |   if (tau_handle == NULL) 
5884 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5885 | 
5886 |   if (tau_handle == NULL) { 
5887 |     perror("Error opening library in dlopen call"); 
5888 |     return;
5889 |   } 
5891 |     if (shmem_iget16___h == NULL)
5892 | 	shmem_iget16___h = (shmem_iget16___p_h) dlsym(tau_handle,"shmem_iget16__"); 
5893 |     if (shmem_iget16___h == NULL) {
5894 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5895 |       return;
5896 |     }
5914 |   static shmem_iget32___p_h shmem_iget32___h = NULL;
5915 |   TAU_PROFILE_TIMER(t,"void shmem_iget32__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
5916 |   if (tau_handle == NULL) 
5917 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5918 | 
5919 |   if (tau_handle == NULL) { 
5920 |     perror("Error opening library in dlopen call"); 
5921 |     return;
5922 |   } 
5924 |     if (shmem_iget32___h == NULL)
5925 | 	shmem_iget32___h = (shmem_iget32___p_h) dlsym(tau_handle,"shmem_iget32__"); 
5926 |     if (shmem_iget32___h == NULL) {
5927 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5928 |       return;
5929 |     }
5947 |   static shmem_iget4___p_h shmem_iget4___h = NULL;
5948 |   TAU_PROFILE_TIMER(t,"void shmem_iget4__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
5949 |   if (tau_handle == NULL) 
5950 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5951 | 
5952 |   if (tau_handle == NULL) { 
5953 |     perror("Error opening library in dlopen call"); 
5954 |     return;
5955 |   } 
5957 |     if (shmem_iget4___h == NULL)
5958 | 	shmem_iget4___h = (shmem_iget4___p_h) dlsym(tau_handle,"shmem_iget4__"); 
5959 |     if (shmem_iget4___h == NULL) {
5960 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5961 |       return;
5962 |     }
5980 |   static shmem_iget64___p_h shmem_iget64___h = NULL;
5981 |   TAU_PROFILE_TIMER(t,"void shmem_iget64__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
5982 |   if (tau_handle == NULL) 
5983 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5984 | 
5985 |   if (tau_handle == NULL) { 
5986 |     perror("Error opening library in dlopen call"); 
5987 |     return;
5988 |   } 
5990 |     if (shmem_iget64___h == NULL)
5991 | 	shmem_iget64___h = (shmem_iget64___p_h) dlsym(tau_handle,"shmem_iget64__"); 
5992 |     if (shmem_iget64___h == NULL) {
5993 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5994 |       return;
5995 |     }
6013 |   static shmem_iget8___p_h shmem_iget8___h = NULL;
6014 |   TAU_PROFILE_TIMER(t,"void shmem_iget8__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
6015 |   if (tau_handle == NULL) 
6016 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6017 | 
6018 |   if (tau_handle == NULL) { 
6019 |     perror("Error opening library in dlopen call"); 
6020 |     return;
6021 |   } 
6023 |     if (shmem_iget8___h == NULL)
6024 | 	shmem_iget8___h = (shmem_iget8___p_h) dlsym(tau_handle,"shmem_iget8__"); 
6025 |     if (shmem_iget8___h == NULL) {
6026 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6027 |       return;
6028 |     }
6046 |   static shmem_int2_and_to_all___p_h shmem_int2_and_to_all___h = NULL;
6047 |   TAU_PROFILE_TIMER(t,"void shmem_int2_and_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6048 |   if (tau_handle == NULL) 
6049 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6050 | 
6051 |   if (tau_handle == NULL) { 
6052 |     perror("Error opening library in dlopen call"); 
6053 |     return;
6054 |   } 
6056 |     if (shmem_int2_and_to_all___h == NULL)
6057 | 	shmem_int2_and_to_all___h = (shmem_int2_and_to_all___p_h) dlsym(tau_handle,"shmem_int2_and_to_all__"); 
6058 |     if (shmem_int2_and_to_all___h == NULL) {
6059 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6060 |       return;
6061 |     }
6077 |   static shmem_int2_max_to_all___p_h shmem_int2_max_to_all___h = NULL;
6078 |   TAU_PROFILE_TIMER(t,"void shmem_int2_max_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6079 |   if (tau_handle == NULL) 
6080 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6081 | 
6082 |   if (tau_handle == NULL) { 
6083 |     perror("Error opening library in dlopen call"); 
6084 |     return;
6085 |   } 
6087 |     if (shmem_int2_max_to_all___h == NULL)
6088 | 	shmem_int2_max_to_all___h = (shmem_int2_max_to_all___p_h) dlsym(tau_handle,"shmem_int2_max_to_all__"); 
6089 |     if (shmem_int2_max_to_all___h == NULL) {
6090 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6091 |       return;
6092 |     }
6108 |   static shmem_int2_min_to_all___p_h shmem_int2_min_to_all___h = NULL;
6109 |   TAU_PROFILE_TIMER(t,"void shmem_int2_min_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6110 |   if (tau_handle == NULL) 
6111 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6112 | 
6113 |   if (tau_handle == NULL) { 
6114 |     perror("Error opening library in dlopen call"); 
6115 |     return;
6116 |   } 
6118 |     if (shmem_int2_min_to_all___h == NULL)
6119 | 	shmem_int2_min_to_all___h = (shmem_int2_min_to_all___p_h) dlsym(tau_handle,"shmem_int2_min_to_all__"); 
6120 |     if (shmem_int2_min_to_all___h == NULL) {
6121 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6122 |       return;
6123 |     }
6139 |   static shmem_int2_or_to_all___p_h shmem_int2_or_to_all___h = NULL;
6140 |   TAU_PROFILE_TIMER(t,"void shmem_int2_or_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6141 |   if (tau_handle == NULL) 
6142 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6143 | 
6144 |   if (tau_handle == NULL) { 
6145 |     perror("Error opening library in dlopen call"); 
6146 |     return;
6147 |   } 
6149 |     if (shmem_int2_or_to_all___h == NULL)
6150 | 	shmem_int2_or_to_all___h = (shmem_int2_or_to_all___p_h) dlsym(tau_handle,"shmem_int2_or_to_all__"); 
6151 |     if (shmem_int2_or_to_all___h == NULL) {
6152 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6153 |       return;
6154 |     }
6170 |   static shmem_int2_prod_to_all___p_h shmem_int2_prod_to_all___h = NULL;
6171 |   TAU_PROFILE_TIMER(t,"void shmem_int2_prod_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6172 |   if (tau_handle == NULL) 
6173 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6174 | 
6175 |   if (tau_handle == NULL) { 
6176 |     perror("Error opening library in dlopen call"); 
6177 |     return;
6178 |   } 
6180 |     if (shmem_int2_prod_to_all___h == NULL)
6181 | 	shmem_int2_prod_to_all___h = (shmem_int2_prod_to_all___p_h) dlsym(tau_handle,"shmem_int2_prod_to_all__"); 
6182 |     if (shmem_int2_prod_to_all___h == NULL) {
6183 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6184 |       return;
6185 |     }
6201 |   static shmem_int2_sum_to_all___p_h shmem_int2_sum_to_all___h = NULL;
6202 |   TAU_PROFILE_TIMER(t,"void shmem_int2_sum_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6203 |   if (tau_handle == NULL) 
6204 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6205 | 
6206 |   if (tau_handle == NULL) { 
6207 |     perror("Error opening library in dlopen call"); 
6208 |     return;
6209 |   } 
6211 |     if (shmem_int2_sum_to_all___h == NULL)
6212 | 	shmem_int2_sum_to_all___h = (shmem_int2_sum_to_all___p_h) dlsym(tau_handle,"shmem_int2_sum_to_all__"); 
6213 |     if (shmem_int2_sum_to_all___h == NULL) {
6214 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6215 |       return;
6216 |     }
6232 |   static shmem_int2_xor_to_all___p_h shmem_int2_xor_to_all___h = NULL;
6233 |   TAU_PROFILE_TIMER(t,"void shmem_int2_xor_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6234 |   if (tau_handle == NULL) 
6235 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6236 | 
6237 |   if (tau_handle == NULL) { 
6238 |     perror("Error opening library in dlopen call"); 
6239 |     return;
6240 |   } 
6242 |     if (shmem_int2_xor_to_all___h == NULL)
6243 | 	shmem_int2_xor_to_all___h = (shmem_int2_xor_to_all___p_h) dlsym(tau_handle,"shmem_int2_xor_to_all__"); 
6244 |     if (shmem_int2_xor_to_all___h == NULL) {
6245 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6246 |       return;
6247 |     }
6263 |   static shmem_int4_add___p_h shmem_int4_add___h = NULL;
6264 |   TAU_PROFILE_TIMER(t,"void shmem_int4_add__(void *, int *, int *)", "", TAU_USER);
6265 |   if (tau_handle == NULL) 
6266 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6267 | 
6268 |   if (tau_handle == NULL) { 
6269 |     perror("Error opening library in dlopen call"); 
6270 |     return;
6271 |   } 
6273 |     if (shmem_int4_add___h == NULL)
6274 | 	shmem_int4_add___h = (shmem_int4_add___p_h) dlsym(tau_handle,"shmem_int4_add__"); 
6275 |     if (shmem_int4_add___h == NULL) {
6276 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6277 |       return;
6278 |     }
6294 |   static shmem_int4_and_to_all___p_h shmem_int4_and_to_all___h = NULL;
6295 |   TAU_PROFILE_TIMER(t,"void shmem_int4_and_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6296 |   if (tau_handle == NULL) 
6297 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6298 | 
6299 |   if (tau_handle == NULL) { 
6300 |     perror("Error opening library in dlopen call"); 
6301 |     return;
6302 |   } 
6304 |     if (shmem_int4_and_to_all___h == NULL)
6305 | 	shmem_int4_and_to_all___h = (shmem_int4_and_to_all___p_h) dlsym(tau_handle,"shmem_int4_and_to_all__"); 
6306 |     if (shmem_int4_and_to_all___h == NULL) {
6307 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6308 |       return;
6309 |     }
6326 |   int retval = 0;
6327 |   TAU_PROFILE_TIMER(t,"int shmem_int4_cswap__(int *, int *, int *, int *)", "", TAU_USER);
6328 |   if (tau_handle == NULL) 
6329 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6330 | 
6331 |   if (tau_handle == NULL) { 
6332 |     perror("Error opening library in dlopen call"); 
6333 |     return retval;
6334 |   } 
6336 |     if (shmem_int4_cswap___h == NULL)
6337 | 	shmem_int4_cswap___h = (shmem_int4_cswap___p_h) dlsym(tau_handle,"shmem_int4_cswap__"); 
6338 |     if (shmem_int4_cswap___h == NULL) {
6339 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6340 |       return retval;
6341 |     }
6365 |   int retval = 0;
6366 |   TAU_PROFILE_TIMER(t,"int shmem_int4_fadd__(void *, int *, int *)", "", TAU_USER);
6367 |   if (tau_handle == NULL) 
6368 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6369 | 
6370 |   if (tau_handle == NULL) { 
6371 |     perror("Error opening library in dlopen call"); 
6372 |     return retval;
6373 |   } 
6375 |     if (shmem_int4_fadd___h == NULL)
6376 | 	shmem_int4_fadd___h = (shmem_int4_fadd___p_h) dlsym(tau_handle,"shmem_int4_fadd__"); 
6377 |     if (shmem_int4_fadd___h == NULL) {
6378 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6379 |       return retval;
6380 |     }
6402 |   int retval = 0;
6403 |   TAU_PROFILE_TIMER(t,"int shmem_int4_finc__(void *, int *)", "", TAU_USER);
6404 |   if (tau_handle == NULL) 
6405 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6406 | 
6407 |   if (tau_handle == NULL) { 
6408 |     perror("Error opening library in dlopen call"); 
6409 |     return retval;
6410 |   } 
6412 |     if (shmem_int4_finc___h == NULL)
6413 | 	shmem_int4_finc___h = (shmem_int4_finc___p_h) dlsym(tau_handle,"shmem_int4_finc__"); 
6414 |     if (shmem_int4_finc___h == NULL) {
6415 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6416 |       return retval;
6417 |     }
6438 |   static shmem_int4_inc___p_h shmem_int4_inc___h = NULL;
6439 |   TAU_PROFILE_TIMER(t,"void shmem_int4_inc__(void *, int *)", "", TAU_USER);
6440 |   if (tau_handle == NULL) 
6441 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6442 | 
6443 |   if (tau_handle == NULL) { 
6444 |     perror("Error opening library in dlopen call"); 
6445 |     return;
6446 |   } 
6448 |     if (shmem_int4_inc___h == NULL)
6449 | 	shmem_int4_inc___h = (shmem_int4_inc___p_h) dlsym(tau_handle,"shmem_int4_inc__"); 
6450 |     if (shmem_int4_inc___h == NULL) {
6451 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6452 |       return;
6453 |     }
6469 |   static shmem_int4_max_to_all___p_h shmem_int4_max_to_all___h = NULL;
6470 |   TAU_PROFILE_TIMER(t,"void shmem_int4_max_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6471 |   if (tau_handle == NULL) 
6472 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6473 | 
6474 |   if (tau_handle == NULL) { 
6475 |     perror("Error opening library in dlopen call"); 
6476 |     return;
6477 |   } 
6479 |     if (shmem_int4_max_to_all___h == NULL)
6480 | 	shmem_int4_max_to_all___h = (shmem_int4_max_to_all___p_h) dlsym(tau_handle,"shmem_int4_max_to_all__"); 
6481 |     if (shmem_int4_max_to_all___h == NULL) {
6482 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6483 |       return;
6484 |     }
6500 |   static shmem_int4_min_to_all___p_h shmem_int4_min_to_all___h = NULL;
6501 |   TAU_PROFILE_TIMER(t,"void shmem_int4_min_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6502 |   if (tau_handle == NULL) 
6503 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6504 | 
6505 |   if (tau_handle == NULL) { 
6506 |     perror("Error opening library in dlopen call"); 
6507 |     return;
6508 |   } 
6510 |     if (shmem_int4_min_to_all___h == NULL)
6511 | 	shmem_int4_min_to_all___h = (shmem_int4_min_to_all___p_h) dlsym(tau_handle,"shmem_int4_min_to_all__"); 
6512 |     if (shmem_int4_min_to_all___h == NULL) {
6513 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6514 |       return;
6515 |     }
6531 |   static shmem_int4_or_to_all___p_h shmem_int4_or_to_all___h = NULL;
6532 |   TAU_PROFILE_TIMER(t,"void shmem_int4_or_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6533 |   if (tau_handle == NULL) 
6534 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6535 | 
6536 |   if (tau_handle == NULL) { 
6537 |     perror("Error opening library in dlopen call"); 
6538 |     return;
6539 |   } 
6541 |     if (shmem_int4_or_to_all___h == NULL)
6542 | 	shmem_int4_or_to_all___h = (shmem_int4_or_to_all___p_h) dlsym(tau_handle,"shmem_int4_or_to_all__"); 
6543 |     if (shmem_int4_or_to_all___h == NULL) {
6544 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6545 |       return;
6546 |     }
6562 |   static shmem_int4_prod_to_all___p_h shmem_int4_prod_to_all___h = NULL;
6563 |   TAU_PROFILE_TIMER(t,"void shmem_int4_prod_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6564 |   if (tau_handle == NULL) 
6565 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6566 | 
6567 |   if (tau_handle == NULL) { 
6568 |     perror("Error opening library in dlopen call"); 
6569 |     return;
6570 |   } 
6572 |     if (shmem_int4_prod_to_all___h == NULL)
6573 | 	shmem_int4_prod_to_all___h = (shmem_int4_prod_to_all___p_h) dlsym(tau_handle,"shmem_int4_prod_to_all__"); 
6574 |     if (shmem_int4_prod_to_all___h == NULL) {
6575 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6576 |       return;
6577 |     }
6593 |   static shmem_int4_sum_to_all___p_h shmem_int4_sum_to_all___h = NULL;
6594 |   TAU_PROFILE_TIMER(t,"void shmem_int4_sum_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6595 |   if (tau_handle == NULL) 
6596 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6597 | 
6598 |   if (tau_handle == NULL) { 
6599 |     perror("Error opening library in dlopen call"); 
6600 |     return;
6601 |   } 
6603 |     if (shmem_int4_sum_to_all___h == NULL)
6604 | 	shmem_int4_sum_to_all___h = (shmem_int4_sum_to_all___p_h) dlsym(tau_handle,"shmem_int4_sum_to_all__"); 
6605 |     if (shmem_int4_sum_to_all___h == NULL) {
6606 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6607 |       return;
6608 |     }
6625 |   int retval = 0;
6626 |   TAU_PROFILE_TIMER(t,"int shmem_int4_swap__(void *, int *, int *)", "", TAU_USER);
6627 |   if (tau_handle == NULL) 
6628 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6629 | 
6630 |   if (tau_handle == NULL) { 
6631 |     perror("Error opening library in dlopen call"); 
6632 |     return retval;
6633 |   } 
6635 |     if (shmem_int4_swap___h == NULL)
6636 | 	shmem_int4_swap___h = (shmem_int4_swap___p_h) dlsym(tau_handle,"shmem_int4_swap__"); 
6637 |     if (shmem_int4_swap___h == NULL) {
6638 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6639 |       return retval;
6640 |     }
6661 |   static shmem_int4_wait___p_h shmem_int4_wait___h = NULL;
6662 |   TAU_PROFILE_TIMER(t,"void shmem_int4_wait__(int *, int *)", "", TAU_USER);
6663 |   if (tau_handle == NULL) 
6664 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6665 | 
6666 |   if (tau_handle == NULL) { 
6667 |     perror("Error opening library in dlopen call"); 
6668 |     return;
6669 |   } 
6671 |     if (shmem_int4_wait___h == NULL)
6672 | 	shmem_int4_wait___h = (shmem_int4_wait___p_h) dlsym(tau_handle,"shmem_int4_wait__"); 
6673 |     if (shmem_int4_wait___h == NULL) {
6674 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6675 |       return;
6676 |     }
6692 |   static shmem_int4_wait_until___p_h shmem_int4_wait_until___h = NULL;
6693 |   TAU_PROFILE_TIMER(t,"void shmem_int4_wait_until__(int *, int *, int *)", "", TAU_USER);
6694 |   if (tau_handle == NULL) 
6695 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6696 | 
6697 |   if (tau_handle == NULL) { 
6698 |     perror("Error opening library in dlopen call"); 
6699 |     return;
6700 |   } 
6702 |     if (shmem_int4_wait_until___h == NULL)
6703 | 	shmem_int4_wait_until___h = (shmem_int4_wait_until___p_h) dlsym(tau_handle,"shmem_int4_wait_until__"); 
6704 |     if (shmem_int4_wait_until___h == NULL) {
6705 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6706 |       return;
6707 |     }
6723 |   static shmem_int4_xor_to_all___p_h shmem_int4_xor_to_all___h = NULL;
6724 |   TAU_PROFILE_TIMER(t,"void shmem_int4_xor_to_all__(void *, void *, int *, int *, int *, int *, int *, long *)", "", TAU_USER);
6725 |   if (tau_handle == NULL) 
6726 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6727 | 
6728 |   if (tau_handle == NULL) { 
6729 |     perror("Error opening library in dlopen call"); 
6730 |     return;
6731 |   } 
6733 |     if (shmem_int4_xor_to_all___h == NULL)
6734 | 	shmem_int4_xor_to_all___h = (shmem_int4_xor_to_all___p_h) dlsym(tau_handle,"shmem_int4_xor_to_all__"); 
6735 |     if (shmem_int4_xor_to_all___h == NULL) {
6736 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6737 |       return;
6738 |     }
6754 |   static shmem_int8_add___p_h shmem_int8_add___h = NULL;
6755 |   TAU_PROFILE_TIMER(t,"void shmem_int8_add__(void *, long *, int *)", "", TAU_USER);
6756 |   if (tau_handle == NULL) 
6757 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6758 | 
6759 |   if (tau_handle == NULL) { 
6760 |     perror("Error opening library in dlopen call"); 
6761 |     return;
6762 |   } 
6764 |     if (shmem_int8_add___h == NULL)
6765 | 	shmem_int8_add___h = (shmem_int8_add___p_h) dlsym(tau_handle,"shmem_int8_add__"); 
6766 |     if (shmem_int8_add___h == NULL) {
6767 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6768 |       return;
6769 |     }
6785 |   static shmem_int8_and_to_all___p_h shmem_int8_and_to_all___h = NULL;
6786 |   TAU_PROFILE_TIMER(t,"void shmem_int8_and_to_all__(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
6787 |   if (tau_handle == NULL) 
6788 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6789 | 
6790 |   if (tau_handle == NULL) { 
6791 |     perror("Error opening library in dlopen call"); 
6792 |     return;
6793 |   } 
6795 |     if (shmem_int8_and_to_all___h == NULL)
6796 | 	shmem_int8_and_to_all___h = (shmem_int8_and_to_all___p_h) dlsym(tau_handle,"shmem_int8_and_to_all__"); 
6797 |     if (shmem_int8_and_to_all___h == NULL) {
6798 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6799 |       return;
6800 |     }
6817 |   long retval = 0;
6818 |   TAU_PROFILE_TIMER(t,"long shmem_int8_cswap__(long *, long *, long *, int *)", "", TAU_USER);
6819 |   if (tau_handle == NULL) 
6820 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6821 | 
6822 |   if (tau_handle == NULL) { 
6823 |     perror("Error opening library in dlopen call"); 
6824 |     return retval;
6825 |   } 
6827 |     if (shmem_int8_cswap___h == NULL)
6828 | 	shmem_int8_cswap___h = (shmem_int8_cswap___p_h) dlsym(tau_handle,"shmem_int8_cswap__"); 
6829 |     if (shmem_int8_cswap___h == NULL) {
6830 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6831 |       return retval;
6832 |     }
6856 |   long retval = 0;
6857 |   TAU_PROFILE_TIMER(t,"long shmem_int8_fadd__(void *, int *, int *)", "", TAU_USER);
6858 |   if (tau_handle == NULL) 
6859 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6860 | 
6861 |   if (tau_handle == NULL) { 
6862 |     perror("Error opening library in dlopen call"); 
6863 |     return retval;
6864 |   } 
6866 |     if (shmem_int8_fadd___h == NULL)
6867 | 	shmem_int8_fadd___h = (shmem_int8_fadd___p_h) dlsym(tau_handle,"shmem_int8_fadd__"); 
6868 |     if (shmem_int8_fadd___h == NULL) {
6869 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6870 |       return retval;
6871 |     }
6893 |   long retval = 0;
6894 |   TAU_PROFILE_TIMER(t,"long shmem_int8_finc__(void *, int *)", "", TAU_USER);
6895 |   if (tau_handle == NULL) 
6896 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6897 | 
6898 |   if (tau_handle == NULL) { 
6899 |     perror("Error opening library in dlopen call"); 
6900 |     return retval;
6901 |   } 
6903 |     if (shmem_int8_finc___h == NULL)
6904 | 	shmem_int8_finc___h = (shmem_int8_finc___p_h) dlsym(tau_handle,"shmem_int8_finc__"); 
6905 |     if (shmem_int8_finc___h == NULL) {
6906 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6907 |       return retval;
6908 |     }
6929 |   static shmem_int8_inc___p_h shmem_int8_inc___h = NULL;
6930 |   TAU_PROFILE_TIMER(t,"void shmem_int8_inc__(void *, int *)", "", TAU_USER);
6931 |   if (tau_handle == NULL) 
6932 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6933 | 
6934 |   if (tau_handle == NULL) { 
6935 |     perror("Error opening library in dlopen call"); 
6936 |     return;
6937 |   } 
6939 |     if (shmem_int8_inc___h == NULL)
6940 | 	shmem_int8_inc___h = (shmem_int8_inc___p_h) dlsym(tau_handle,"shmem_int8_inc__"); 
6941 |     if (shmem_int8_inc___h == NULL) {
6942 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6943 |       return;
6944 |     }
6960 |   static shmem_int8_max_to_all___p_h shmem_int8_max_to_all___h = NULL;
6961 |   TAU_PROFILE_TIMER(t,"void shmem_int8_max_to_all__(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
6962 |   if (tau_handle == NULL) 
6963 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6964 | 
6965 |   if (tau_handle == NULL) { 
6966 |     perror("Error opening library in dlopen call"); 
6967 |     return;
6968 |   } 
6970 |     if (shmem_int8_max_to_all___h == NULL)
6971 | 	shmem_int8_max_to_all___h = (shmem_int8_max_to_all___p_h) dlsym(tau_handle,"shmem_int8_max_to_all__"); 
6972 |     if (shmem_int8_max_to_all___h == NULL) {
6973 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6974 |       return;
6975 |     }
6991 |   static shmem_int8_min_to_all___p_h shmem_int8_min_to_all___h = NULL;
6992 |   TAU_PROFILE_TIMER(t,"void shmem_int8_min_to_all__(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
6993 |   if (tau_handle == NULL) 
6994 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6995 | 
6996 |   if (tau_handle == NULL) { 
6997 |     perror("Error opening library in dlopen call"); 
6998 |     return;
6999 |   } 
7001 |     if (shmem_int8_min_to_all___h == NULL)
7002 | 	shmem_int8_min_to_all___h = (shmem_int8_min_to_all___p_h) dlsym(tau_handle,"shmem_int8_min_to_all__"); 
7003 |     if (shmem_int8_min_to_all___h == NULL) {
7004 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7005 |       return;
7006 |     }
7022 |   static shmem_int8_or_to_all___p_h shmem_int8_or_to_all___h = NULL;
7023 |   TAU_PROFILE_TIMER(t,"void shmem_int8_or_to_all__(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
7024 |   if (tau_handle == NULL) 
7025 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7026 | 
7027 |   if (tau_handle == NULL) { 
7028 |     perror("Error opening library in dlopen call"); 
7029 |     return;
7030 |   } 
7032 |     if (shmem_int8_or_to_all___h == NULL)
7033 | 	shmem_int8_or_to_all___h = (shmem_int8_or_to_all___p_h) dlsym(tau_handle,"shmem_int8_or_to_all__"); 
7034 |     if (shmem_int8_or_to_all___h == NULL) {
7035 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7036 |       return;
7037 |     }
7053 |   static shmem_int8_prod_to_all___p_h shmem_int8_prod_to_all___h = NULL;
7054 |   TAU_PROFILE_TIMER(t,"void shmem_int8_prod_to_all__(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
7055 |   if (tau_handle == NULL) 
7056 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7057 | 
7058 |   if (tau_handle == NULL) { 
7059 |     perror("Error opening library in dlopen call"); 
7060 |     return;
7061 |   } 
7063 |     if (shmem_int8_prod_to_all___h == NULL)
7064 | 	shmem_int8_prod_to_all___h = (shmem_int8_prod_to_all___p_h) dlsym(tau_handle,"shmem_int8_prod_to_all__"); 
7065 |     if (shmem_int8_prod_to_all___h == NULL) {
7066 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7067 |       return;
7068 |     }
7084 |   static shmem_int8_sum_to_all___p_h shmem_int8_sum_to_all___h = NULL;
7085 |   TAU_PROFILE_TIMER(t,"void shmem_int8_sum_to_all__(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
7086 |   if (tau_handle == NULL) 
7087 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7088 | 
7089 |   if (tau_handle == NULL) { 
7090 |     perror("Error opening library in dlopen call"); 
7091 |     return;
7092 |   } 
7094 |     if (shmem_int8_sum_to_all___h == NULL)
7095 | 	shmem_int8_sum_to_all___h = (shmem_int8_sum_to_all___p_h) dlsym(tau_handle,"shmem_int8_sum_to_all__"); 
7096 |     if (shmem_int8_sum_to_all___h == NULL) {
7097 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7098 |       return;
7099 |     }
7116 |   long retval = 0;
7117 |   TAU_PROFILE_TIMER(t,"long shmem_int8_swap__(void *, long *, int *)", "", TAU_USER);
7118 |   if (tau_handle == NULL) 
7119 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7120 | 
7121 |   if (tau_handle == NULL) { 
7122 |     perror("Error opening library in dlopen call"); 
7123 |     return retval;
7124 |   } 
7126 |     if (shmem_int8_swap___h == NULL)
7127 | 	shmem_int8_swap___h = (shmem_int8_swap___p_h) dlsym(tau_handle,"shmem_int8_swap__"); 
7128 |     if (shmem_int8_swap___h == NULL) {
7129 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7130 |       return retval;
7131 |     }
7152 |   static shmem_int8_wait___p_h shmem_int8_wait___h = NULL;
7153 |   TAU_PROFILE_TIMER(t,"void shmem_int8_wait__(long *, long *)", "", TAU_USER);
7154 |   if (tau_handle == NULL) 
7155 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7156 | 
7157 |   if (tau_handle == NULL) { 
7158 |     perror("Error opening library in dlopen call"); 
7159 |     return;
7160 |   } 
7162 |     if (shmem_int8_wait___h == NULL)
7163 | 	shmem_int8_wait___h = (shmem_int8_wait___p_h) dlsym(tau_handle,"shmem_int8_wait__"); 
7164 |     if (shmem_int8_wait___h == NULL) {
7165 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7166 |       return;
7167 |     }
7183 |   static shmem_int8_wait_until___p_h shmem_int8_wait_until___h = NULL;
7184 |   TAU_PROFILE_TIMER(t,"void shmem_int8_wait_until__(long *, int *, long *)", "", TAU_USER);
7185 |   if (tau_handle == NULL) 
7186 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7187 | 
7188 |   if (tau_handle == NULL) { 
7189 |     perror("Error opening library in dlopen call"); 
7190 |     return;
7191 |   } 
7193 |     if (shmem_int8_wait_until___h == NULL)
7194 | 	shmem_int8_wait_until___h = (shmem_int8_wait_until___p_h) dlsym(tau_handle,"shmem_int8_wait_until__"); 
7195 |     if (shmem_int8_wait_until___h == NULL) {
7196 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7197 |       return;
7198 |     }
7214 |   static shmem_int8_xor_to_all___p_h shmem_int8_xor_to_all___h = NULL;
7215 |   TAU_PROFILE_TIMER(t,"void shmem_int8_xor_to_all__(void *, void *, int *, int *, int *, int *, long *, long *)", "", TAU_USER);
7216 |   if (tau_handle == NULL) 
7217 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7218 | 
7219 |   if (tau_handle == NULL) { 
7220 |     perror("Error opening library in dlopen call"); 
7221 |     return;
7222 |   } 
7224 |     if (shmem_int8_xor_to_all___h == NULL)
7225 | 	shmem_int8_xor_to_all___h = (shmem_int8_xor_to_all___p_h) dlsym(tau_handle,"shmem_int8_xor_to_all__"); 
7226 |     if (shmem_int8_xor_to_all___h == NULL) {
7227 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7228 |       return;
7229 |     }
7245 |   static shmem_integer_get___p_h shmem_integer_get___h = NULL;
7246 |   TAU_PROFILE_TIMER(t,"void shmem_integer_get__(void *, void *, int *, int *)", "", TAU_USER);
7247 |   if (tau_handle == NULL) 
7248 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7249 | 
7250 |   if (tau_handle == NULL) { 
7251 |     perror("Error opening library in dlopen call"); 
7252 |     return;
7253 |   } 
7255 |     if (shmem_integer_get___h == NULL)
7256 | 	shmem_integer_get___h = (shmem_integer_get___p_h) dlsym(tau_handle,"shmem_integer_get__"); 
7257 |     if (shmem_integer_get___h == NULL) {
7258 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7259 |       return;
7260 |     }
7278 |   static shmem_integer_iget___p_h shmem_integer_iget___h = NULL;
7279 |   TAU_PROFILE_TIMER(t,"void shmem_integer_iget__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
7280 |   if (tau_handle == NULL) 
7281 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7282 | 
7283 |   if (tau_handle == NULL) { 
7284 |     perror("Error opening library in dlopen call"); 
7285 |     return;
7286 |   } 
7288 |     if (shmem_integer_iget___h == NULL)
7289 | 	shmem_integer_iget___h = (shmem_integer_iget___p_h) dlsym(tau_handle,"shmem_integer_iget__"); 
7290 |     if (shmem_integer_iget___h == NULL) {
7291 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7292 |       return;
7293 |     }
7311 |   static shmem_integer_iput___p_h shmem_integer_iput___h = NULL;
7312 |   TAU_PROFILE_TIMER(t,"void shmem_integer_iput__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
7313 |   if (tau_handle == NULL) 
7314 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7315 | 
7316 |   if (tau_handle == NULL) { 
7317 |     perror("Error opening library in dlopen call"); 
7318 |     return;
7319 |   } 
7321 |     if (shmem_integer_iput___h == NULL)
7322 | 	shmem_integer_iput___h = (shmem_integer_iput___p_h) dlsym(tau_handle,"shmem_integer_iput__"); 
7323 |     if (shmem_integer_iput___h == NULL) {
7324 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7325 |       return;
7326 |     }
7344 |   static shmem_integer_put___p_h shmem_integer_put___h = NULL;
7345 |   TAU_PROFILE_TIMER(t,"void shmem_integer_put__(void *, void *, int *, int *)", "", TAU_USER);
7346 |   if (tau_handle == NULL) 
7347 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7348 | 
7349 |   if (tau_handle == NULL) { 
7350 |     perror("Error opening library in dlopen call"); 
7351 |     return;
7352 |   } 
7354 |     if (shmem_integer_put___h == NULL)
7355 | 	shmem_integer_put___h = (shmem_integer_put___p_h) dlsym(tau_handle,"shmem_integer_put__"); 
7356 |     if (shmem_integer_put___h == NULL) {
7357 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7358 |       return;
7359 |     }
7377 |   static shmem_iput128___p_h shmem_iput128___h = NULL;
7378 |   TAU_PROFILE_TIMER(t,"void shmem_iput128__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
7379 |   if (tau_handle == NULL) 
7380 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7381 | 
7382 |   if (tau_handle == NULL) { 
7383 |     perror("Error opening library in dlopen call"); 
7384 |     return;
7385 |   } 
7387 |     if (shmem_iput128___h == NULL)
7388 | 	shmem_iput128___h = (shmem_iput128___p_h) dlsym(tau_handle,"shmem_iput128__"); 
7389 |     if (shmem_iput128___h == NULL) {
7390 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7391 |       return;
7392 |     }
7410 |   static shmem_iput16___p_h shmem_iput16___h = NULL;
7411 |   TAU_PROFILE_TIMER(t,"void shmem_iput16__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
7412 |   if (tau_handle == NULL) 
7413 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7414 | 
7415 |   if (tau_handle == NULL) { 
7416 |     perror("Error opening library in dlopen call"); 
7417 |     return;
7418 |   } 
7420 |     if (shmem_iput16___h == NULL)
7421 | 	shmem_iput16___h = (shmem_iput16___p_h) dlsym(tau_handle,"shmem_iput16__"); 
7422 |     if (shmem_iput16___h == NULL) {
7423 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7424 |       return;
7425 |     }
7443 |   static shmem_iput32___p_h shmem_iput32___h = NULL;
7444 |   TAU_PROFILE_TIMER(t,"void shmem_iput32__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
7445 |   if (tau_handle == NULL) 
7446 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7447 | 
7448 |   if (tau_handle == NULL) { 
7449 |     perror("Error opening library in dlopen call"); 
7450 |     return;
7451 |   } 
7453 |     if (shmem_iput32___h == NULL)
7454 | 	shmem_iput32___h = (shmem_iput32___p_h) dlsym(tau_handle,"shmem_iput32__"); 
7455 |     if (shmem_iput32___h == NULL) {
7456 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7457 |       return;
7458 |     }
7476 |   static shmem_iput4___p_h shmem_iput4___h = NULL;
7477 |   TAU_PROFILE_TIMER(t,"void shmem_iput4__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
7478 |   if (tau_handle == NULL) 
7479 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7480 | 
7481 |   if (tau_handle == NULL) { 
7482 |     perror("Error opening library in dlopen call"); 
7483 |     return;
7484 |   } 
7486 |     if (shmem_iput4___h == NULL)
7487 | 	shmem_iput4___h = (shmem_iput4___p_h) dlsym(tau_handle,"shmem_iput4__"); 
7488 |     if (shmem_iput4___h == NULL) {
7489 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7490 |       return;
7491 |     }
7509 |   static shmem_iput64___p_h shmem_iput64___h = NULL;
7510 |   TAU_PROFILE_TIMER(t,"void shmem_iput64__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
7511 |   if (tau_handle == NULL) 
7512 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7513 | 
7514 |   if (tau_handle == NULL) { 
7515 |     perror("Error opening library in dlopen call"); 
7516 |     return;
7517 |   } 
7519 |     if (shmem_iput64___h == NULL)
7520 | 	shmem_iput64___h = (shmem_iput64___p_h) dlsym(tau_handle,"shmem_iput64__"); 
7521 |     if (shmem_iput64___h == NULL) {
7522 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7523 |       return;
7524 |     }
7542 |   static shmem_iput8___p_h shmem_iput8___h = NULL;
7543 |   TAU_PROFILE_TIMER(t,"void shmem_iput8__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
7544 |   if (tau_handle == NULL) 
7545 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7546 | 
7547 |   if (tau_handle == NULL) { 
7548 |     perror("Error opening library in dlopen call"); 
7549 |     return;
7550 |   } 
7552 |     if (shmem_iput8___h == NULL)
7553 | 	shmem_iput8___h = (shmem_iput8___p_h) dlsym(tau_handle,"shmem_iput8__"); 
7554 |     if (shmem_iput8___h == NULL) {
7555 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7556 |       return;
7557 |     }
7575 |   static shmem_logical_get___p_h shmem_logical_get___h = NULL;
7576 |   TAU_PROFILE_TIMER(t,"void shmem_logical_get__(void *, void *, int *, int *)", "", TAU_USER);
7577 |   if (tau_handle == NULL) 
7578 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7579 | 
7580 |   if (tau_handle == NULL) { 
7581 |     perror("Error opening library in dlopen call"); 
7582 |     return;
7583 |   } 
7585 |     if (shmem_logical_get___h == NULL)
7586 | 	shmem_logical_get___h = (shmem_logical_get___p_h) dlsym(tau_handle,"shmem_logical_get__"); 
7587 |     if (shmem_logical_get___h == NULL) {
7588 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7589 |       return;
7590 |     }
7608 |   static shmem_logical_iget___p_h shmem_logical_iget___h = NULL;
7609 |   TAU_PROFILE_TIMER(t,"void shmem_logical_iget__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
7610 |   if (tau_handle == NULL) 
7611 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7612 | 
7613 |   if (tau_handle == NULL) { 
7614 |     perror("Error opening library in dlopen call"); 
7615 |     return;
7616 |   } 
7618 |     if (shmem_logical_iget___h == NULL)
7619 | 	shmem_logical_iget___h = (shmem_logical_iget___p_h) dlsym(tau_handle,"shmem_logical_iget__"); 
7620 |     if (shmem_logical_iget___h == NULL) {
7621 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7622 |       return;
7623 |     }
7641 |   static shmem_logical_iput___p_h shmem_logical_iput___h = NULL;
7642 |   TAU_PROFILE_TIMER(t,"void shmem_logical_iput__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
7643 |   if (tau_handle == NULL) 
7644 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7645 | 
7646 |   if (tau_handle == NULL) { 
7647 |     perror("Error opening library in dlopen call"); 
7648 |     return;
7649 |   } 
7651 |     if (shmem_logical_iput___h == NULL)
7652 | 	shmem_logical_iput___h = (shmem_logical_iput___p_h) dlsym(tau_handle,"shmem_logical_iput__"); 
7653 |     if (shmem_logical_iput___h == NULL) {
7654 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7655 |       return;
7656 |     }
7674 |   static shmem_logical_put___p_h shmem_logical_put___h = NULL;
7675 |   TAU_PROFILE_TIMER(t,"void shmem_logical_put__(void *, void *, int *, int *)", "", TAU_USER);
7676 |   if (tau_handle == NULL) 
7677 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7678 | 
7679 |   if (tau_handle == NULL) { 
7680 |     perror("Error opening library in dlopen call"); 
7681 |     return;
7682 |   } 
7684 |     if (shmem_logical_put___h == NULL)
7685 | 	shmem_logical_put___h = (shmem_logical_put___p_h) dlsym(tau_handle,"shmem_logical_put__"); 
7686 |     if (shmem_logical_put___h == NULL) {
7687 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7688 |       return;
7689 |     }
7708 |   int retval = 0;
7709 |   TAU_PROFILE_TIMER(t,"int shmem_my_pe__()", "", TAU_USER);
7710 |   if (tau_handle == NULL) 
7711 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7712 | 
7713 |   if (tau_handle == NULL) { 
7714 |     perror("Error opening library in dlopen call"); 
7715 |     return retval;
7716 |   } 
7718 |     if (shmem_my_pe___h == NULL)
7719 | 	shmem_my_pe___h = (shmem_my_pe___p_h) dlsym(tau_handle,"shmem_my_pe__"); 
7720 |     if (shmem_my_pe___h == NULL) {
7721 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7722 |       return retval;
7723 |     }
7741 |   int retval = 0;
7742 |   TAU_PROFILE_TIMER(t,"int shmem_n_pes__()", "", TAU_USER);
7743 |   if (tau_handle == NULL) 
7744 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7745 | 
7746 |   if (tau_handle == NULL) { 
7747 |     perror("Error opening library in dlopen call"); 
7748 |     return retval;
7749 |   } 
7751 |     if (shmem_n_pes___h == NULL)
7752 | 	shmem_n_pes___h = (shmem_n_pes___p_h) dlsym(tau_handle,"shmem_n_pes__"); 
7753 |     if (shmem_n_pes___h == NULL) {
7754 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7755 |       return retval;
7756 |     }
7774 |   int retval = 0;
7775 |   TAU_PROFILE_TIMER(t,"int shmem_pe_accessible__(int *)", "", TAU_USER);
7776 |   if (tau_handle == NULL) 
7777 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7778 | 
7779 |   if (tau_handle == NULL) { 
7780 |     perror("Error opening library in dlopen call"); 
7781 |     return retval;
7782 |   } 
7784 |     if (shmem_pe_accessible___h == NULL)
7785 | 	shmem_pe_accessible___h = (shmem_pe_accessible___p_h) dlsym(tau_handle,"shmem_pe_accessible__"); 
7786 |     if (shmem_pe_accessible___h == NULL) {
7787 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7788 |       return retval;
7789 |     }
7806 |   static shmem_ptr___p_h shmem_ptr___h = NULL;
7807 |   TAU_PROFILE_TIMER(t,"void shmem_ptr__(void *, int *)", "", TAU_USER);
7808 |   if (tau_handle == NULL) 
7809 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7810 | 
7811 |   if (tau_handle == NULL) { 
7812 |     perror("Error opening library in dlopen call"); 
7813 |     return;
7814 |   } 
7816 |     if (shmem_ptr___h == NULL)
7817 | 	shmem_ptr___h = (shmem_ptr___p_h) dlsym(tau_handle,"shmem_ptr__"); 
7818 |     if (shmem_ptr___h == NULL) {
7819 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7820 |       return;
7821 |     }
7837 |   static shmem_put128___p_h shmem_put128___h = NULL;
7838 |   TAU_PROFILE_TIMER(t,"void shmem_put128__(void *, void *, int *, int *)", "", TAU_USER);
7839 |   if (tau_handle == NULL) 
7840 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7841 | 
7842 |   if (tau_handle == NULL) { 
7843 |     perror("Error opening library in dlopen call"); 
7844 |     return;
7845 |   } 
7847 |     if (shmem_put128___h == NULL)
7848 | 	shmem_put128___h = (shmem_put128___p_h) dlsym(tau_handle,"shmem_put128__"); 
7849 |     if (shmem_put128___h == NULL) {
7850 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7851 |       return;
7852 |     }
7870 |   static shmem_put16___p_h shmem_put16___h = NULL;
7871 |   TAU_PROFILE_TIMER(t,"void shmem_put16__(void *, void *, int *, int *)", "", TAU_USER);
7872 |   if (tau_handle == NULL) 
7873 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7874 | 
7875 |   if (tau_handle == NULL) { 
7876 |     perror("Error opening library in dlopen call"); 
7877 |     return;
7878 |   } 
7880 |     if (shmem_put16___h == NULL)
7881 | 	shmem_put16___h = (shmem_put16___p_h) dlsym(tau_handle,"shmem_put16__"); 
7882 |     if (shmem_put16___h == NULL) {
7883 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7884 |       return;
7885 |     }
7903 |   static shmem_put32___p_h shmem_put32___h = NULL;
7904 |   TAU_PROFILE_TIMER(t,"void shmem_put32__(void *, void *, int *, int *)", "", TAU_USER);
7905 |   if (tau_handle == NULL) 
7906 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7907 | 
7908 |   if (tau_handle == NULL) { 
7909 |     perror("Error opening library in dlopen call"); 
7910 |     return;
7911 |   } 
7913 |     if (shmem_put32___h == NULL)
7914 | 	shmem_put32___h = (shmem_put32___p_h) dlsym(tau_handle,"shmem_put32__"); 
7915 |     if (shmem_put32___h == NULL) {
7916 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7917 |       return;
7918 |     }
7936 |   static shmem_put4___p_h shmem_put4___h = NULL;
7937 |   TAU_PROFILE_TIMER(t,"void shmem_put4__(void *, void *, int *, int *)", "", TAU_USER);
7938 |   if (tau_handle == NULL) 
7939 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7940 | 
7941 |   if (tau_handle == NULL) { 
7942 |     perror("Error opening library in dlopen call"); 
7943 |     return;
7944 |   } 
7946 |     if (shmem_put4___h == NULL)
7947 | 	shmem_put4___h = (shmem_put4___p_h) dlsym(tau_handle,"shmem_put4__"); 
7948 |     if (shmem_put4___h == NULL) {
7949 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7950 |       return;
7951 |     }
7969 |   static shmem_put64___p_h shmem_put64___h = NULL;
7970 |   TAU_PROFILE_TIMER(t,"void shmem_put64__(void *, void *, int *, int *)", "", TAU_USER);
7971 |   if (tau_handle == NULL) 
7972 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7973 | 
7974 |   if (tau_handle == NULL) { 
7975 |     perror("Error opening library in dlopen call"); 
7976 |     return;
7977 |   } 
7979 |     if (shmem_put64___h == NULL)
7980 | 	shmem_put64___h = (shmem_put64___p_h) dlsym(tau_handle,"shmem_put64__"); 
7981 |     if (shmem_put64___h == NULL) {
7982 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7983 |       return;
7984 |     }
8002 |   static shmem_put8___p_h shmem_put8___h = NULL;
8003 |   TAU_PROFILE_TIMER(t,"void shmem_put8__(void *, void *, int *, int *)", "", TAU_USER);
8004 |   if (tau_handle == NULL) 
8005 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8006 | 
8007 |   if (tau_handle == NULL) { 
8008 |     perror("Error opening library in dlopen call"); 
8009 |     return;
8010 |   } 
8012 |     if (shmem_put8___h == NULL)
8013 | 	shmem_put8___h = (shmem_put8___p_h) dlsym(tau_handle,"shmem_put8__"); 
8014 |     if (shmem_put8___h == NULL) {
8015 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8016 |       return;
8017 |     }
8035 |   static shmem_putmem___p_h shmem_putmem___h = NULL;
8036 |   TAU_PROFILE_TIMER(t,"void shmem_putmem__(void *, void *, int *, int *)", "", TAU_USER);
8037 |   if (tau_handle == NULL) 
8038 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8039 | 
8040 |   if (tau_handle == NULL) { 
8041 |     perror("Error opening library in dlopen call"); 
8042 |     return;
8043 |   } 
8045 |     if (shmem_putmem___h == NULL)
8046 | 	shmem_putmem___h = (shmem_putmem___p_h) dlsym(tau_handle,"shmem_putmem__"); 
8047 |     if (shmem_putmem___h == NULL) {
8048 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8049 |       return;
8050 |     }
8068 |   static shmem_quiet___p_h shmem_quiet___h = NULL;
8069 |   TAU_PROFILE_TIMER(t,"void shmem_quiet__()", "", TAU_USER);
8070 |   if (tau_handle == NULL) 
8071 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8072 | 
8073 |   if (tau_handle == NULL) { 
8074 |     perror("Error opening library in dlopen call"); 
8075 |     return;
8076 |   } 
8078 |     if (shmem_quiet___h == NULL)
8079 | 	shmem_quiet___h = (shmem_quiet___p_h) dlsym(tau_handle,"shmem_quiet__"); 
8080 |     if (shmem_quiet___h == NULL) {
8081 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8082 |       return;
8083 |     }
8099 |   static shmem_real16_max_to_all___p_h shmem_real16_max_to_all___h = NULL;
8100 |   TAU_PROFILE_TIMER(t,"void shmem_real16_max_to_all__(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
8101 |   if (tau_handle == NULL) 
8102 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8103 | 
8104 |   if (tau_handle == NULL) { 
8105 |     perror("Error opening library in dlopen call"); 
8106 |     return;
8107 |   } 
8109 |     if (shmem_real16_max_to_all___h == NULL)
8110 | 	shmem_real16_max_to_all___h = (shmem_real16_max_to_all___p_h) dlsym(tau_handle,"shmem_real16_max_to_all__"); 
8111 |     if (shmem_real16_max_to_all___h == NULL) {
8112 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8113 |       return;
8114 |     }
8130 |   static shmem_real16_min_to_all___p_h shmem_real16_min_to_all___h = NULL;
8131 |   TAU_PROFILE_TIMER(t,"void shmem_real16_min_to_all__(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
8132 |   if (tau_handle == NULL) 
8133 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8134 | 
8135 |   if (tau_handle == NULL) { 
8136 |     perror("Error opening library in dlopen call"); 
8137 |     return;
8138 |   } 
8140 |     if (shmem_real16_min_to_all___h == NULL)
8141 | 	shmem_real16_min_to_all___h = (shmem_real16_min_to_all___p_h) dlsym(tau_handle,"shmem_real16_min_to_all__"); 
8142 |     if (shmem_real16_min_to_all___h == NULL) {
8143 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8144 |       return;
8145 |     }
8161 |   static shmem_real16_prod_to_all___p_h shmem_real16_prod_to_all___h = NULL;
8162 |   TAU_PROFILE_TIMER(t,"void shmem_real16_prod_to_all__(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
8163 |   if (tau_handle == NULL) 
8164 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8165 | 
8166 |   if (tau_handle == NULL) { 
8167 |     perror("Error opening library in dlopen call"); 
8168 |     return;
8169 |   } 
8171 |     if (shmem_real16_prod_to_all___h == NULL)
8172 | 	shmem_real16_prod_to_all___h = (shmem_real16_prod_to_all___p_h) dlsym(tau_handle,"shmem_real16_prod_to_all__"); 
8173 |     if (shmem_real16_prod_to_all___h == NULL) {
8174 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8175 |       return;
8176 |     }
8192 |   static shmem_real16_sum_to_all___p_h shmem_real16_sum_to_all___h = NULL;
8193 |   TAU_PROFILE_TIMER(t,"void shmem_real16_sum_to_all__(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
8194 |   if (tau_handle == NULL) 
8195 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8196 | 
8197 |   if (tau_handle == NULL) { 
8198 |     perror("Error opening library in dlopen call"); 
8199 |     return;
8200 |   } 
8202 |     if (shmem_real16_sum_to_all___h == NULL)
8203 | 	shmem_real16_sum_to_all___h = (shmem_real16_sum_to_all___p_h) dlsym(tau_handle,"shmem_real16_sum_to_all__"); 
8204 |     if (shmem_real16_sum_to_all___h == NULL) {
8205 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8206 |       return;
8207 |     }
8223 |   static shmem_real4_max_to_all___p_h shmem_real4_max_to_all___h = NULL;
8224 |   TAU_PROFILE_TIMER(t,"void shmem_real4_max_to_all__(void *, void *, int *, int *, int *, int *, float *, long *)", "", TAU_USER);
8225 |   if (tau_handle == NULL) 
8226 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8227 | 
8228 |   if (tau_handle == NULL) { 
8229 |     perror("Error opening library in dlopen call"); 
8230 |     return;
8231 |   } 
8233 |     if (shmem_real4_max_to_all___h == NULL)
8234 | 	shmem_real4_max_to_all___h = (shmem_real4_max_to_all___p_h) dlsym(tau_handle,"shmem_real4_max_to_all__"); 
8235 |     if (shmem_real4_max_to_all___h == NULL) {
8236 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8237 |       return;
8238 |     }
8254 |   static shmem_real4_min_to_all___p_h shmem_real4_min_to_all___h = NULL;
8255 |   TAU_PROFILE_TIMER(t,"void shmem_real4_min_to_all__(void *, void *, int *, int *, int *, int *, float *, long *)", "", TAU_USER);
8256 |   if (tau_handle == NULL) 
8257 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8258 | 
8259 |   if (tau_handle == NULL) { 
8260 |     perror("Error opening library in dlopen call"); 
8261 |     return;
8262 |   } 
8264 |     if (shmem_real4_min_to_all___h == NULL)
8265 | 	shmem_real4_min_to_all___h = (shmem_real4_min_to_all___p_h) dlsym(tau_handle,"shmem_real4_min_to_all__"); 
8266 |     if (shmem_real4_min_to_all___h == NULL) {
8267 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8268 |       return;
8269 |     }
8285 |   static shmem_real4_prod_to_all___p_h shmem_real4_prod_to_all___h = NULL;
8286 |   TAU_PROFILE_TIMER(t,"void shmem_real4_prod_to_all__(void *, void *, int *, int *, int *, int *, float *, long *)", "", TAU_USER);
8287 |   if (tau_handle == NULL) 
8288 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8289 | 
8290 |   if (tau_handle == NULL) { 
8291 |     perror("Error opening library in dlopen call"); 
8292 |     return;
8293 |   } 
8295 |     if (shmem_real4_prod_to_all___h == NULL)
8296 | 	shmem_real4_prod_to_all___h = (shmem_real4_prod_to_all___p_h) dlsym(tau_handle,"shmem_real4_prod_to_all__"); 
8297 |     if (shmem_real4_prod_to_all___h == NULL) {
8298 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8299 |       return;
8300 |     }
8316 |   static shmem_real4_sum_to_all___p_h shmem_real4_sum_to_all___h = NULL;
8317 |   TAU_PROFILE_TIMER(t,"void shmem_real4_sum_to_all__(void *, void *, int *, int *, int *, int *, float *, long *)", "", TAU_USER);
8318 |   if (tau_handle == NULL) 
8319 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8320 | 
8321 |   if (tau_handle == NULL) { 
8322 |     perror("Error opening library in dlopen call"); 
8323 |     return;
8324 |   } 
8326 |     if (shmem_real4_sum_to_all___h == NULL)
8327 | 	shmem_real4_sum_to_all___h = (shmem_real4_sum_to_all___p_h) dlsym(tau_handle,"shmem_real4_sum_to_all__"); 
8328 |     if (shmem_real4_sum_to_all___h == NULL) {
8329 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8330 |       return;
8331 |     }
8348 |   float retval = 0;
8349 |   TAU_PROFILE_TIMER(t,"float shmem_real4_swap__(void *, float *, int *)", "", TAU_USER);
8350 |   if (tau_handle == NULL) 
8351 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8352 | 
8353 |   if (tau_handle == NULL) { 
8354 |     perror("Error opening library in dlopen call"); 
8355 |     return retval;
8356 |   } 
8358 |     if (shmem_real4_swap___h == NULL)
8359 | 	shmem_real4_swap___h = (shmem_real4_swap___p_h) dlsym(tau_handle,"shmem_real4_swap__"); 
8360 |     if (shmem_real4_swap___h == NULL) {
8361 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8362 |       return retval;
8363 |     }
8384 |   static shmem_real8_max_to_all___p_h shmem_real8_max_to_all___h = NULL;
8385 |   TAU_PROFILE_TIMER(t,"void shmem_real8_max_to_all__(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
8386 |   if (tau_handle == NULL) 
8387 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8388 | 
8389 |   if (tau_handle == NULL) { 
8390 |     perror("Error opening library in dlopen call"); 
8391 |     return;
8392 |   } 
8394 |     if (shmem_real8_max_to_all___h == NULL)
8395 | 	shmem_real8_max_to_all___h = (shmem_real8_max_to_all___p_h) dlsym(tau_handle,"shmem_real8_max_to_all__"); 
8396 |     if (shmem_real8_max_to_all___h == NULL) {
8397 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8398 |       return;
8399 |     }
8415 |   static shmem_real8_min_to_all___p_h shmem_real8_min_to_all___h = NULL;
8416 |   TAU_PROFILE_TIMER(t,"void shmem_real8_min_to_all__(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
8417 |   if (tau_handle == NULL) 
8418 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8419 | 
8420 |   if (tau_handle == NULL) { 
8421 |     perror("Error opening library in dlopen call"); 
8422 |     return;
8423 |   } 
8425 |     if (shmem_real8_min_to_all___h == NULL)
8426 | 	shmem_real8_min_to_all___h = (shmem_real8_min_to_all___p_h) dlsym(tau_handle,"shmem_real8_min_to_all__"); 
8427 |     if (shmem_real8_min_to_all___h == NULL) {
8428 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8429 |       return;
8430 |     }
8446 |   static shmem_real8_prod_to_all___p_h shmem_real8_prod_to_all___h = NULL;
8447 |   TAU_PROFILE_TIMER(t,"void shmem_real8_prod_to_all__(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
8448 |   if (tau_handle == NULL) 
8449 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8450 | 
8451 |   if (tau_handle == NULL) { 
8452 |     perror("Error opening library in dlopen call"); 
8453 |     return;
8454 |   } 
8456 |     if (shmem_real8_prod_to_all___h == NULL)
8457 | 	shmem_real8_prod_to_all___h = (shmem_real8_prod_to_all___p_h) dlsym(tau_handle,"shmem_real8_prod_to_all__"); 
8458 |     if (shmem_real8_prod_to_all___h == NULL) {
8459 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8460 |       return;
8461 |     }
8477 |   static shmem_real8_sum_to_all___p_h shmem_real8_sum_to_all___h = NULL;
8478 |   TAU_PROFILE_TIMER(t,"void shmem_real8_sum_to_all__(void *, void *, int *, int *, int *, int *, double *, long *)", "", TAU_USER);
8479 |   if (tau_handle == NULL) 
8480 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8481 | 
8482 |   if (tau_handle == NULL) { 
8483 |     perror("Error opening library in dlopen call"); 
8484 |     return;
8485 |   } 
8487 |     if (shmem_real8_sum_to_all___h == NULL)
8488 | 	shmem_real8_sum_to_all___h = (shmem_real8_sum_to_all___p_h) dlsym(tau_handle,"shmem_real8_sum_to_all__"); 
8489 |     if (shmem_real8_sum_to_all___h == NULL) {
8490 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8491 |       return;
8492 |     }
8509 |   double retval = 0;
8510 |   TAU_PROFILE_TIMER(t,"double shmem_real8_swap__(void *, double *, int *)", "", TAU_USER);
8511 |   if (tau_handle == NULL) 
8512 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8513 | 
8514 |   if (tau_handle == NULL) { 
8515 |     perror("Error opening library in dlopen call"); 
8516 |     return retval;
8517 |   } 
8519 |     if (shmem_real8_swap___h == NULL)
8520 | 	shmem_real8_swap___h = (shmem_real8_swap___p_h) dlsym(tau_handle,"shmem_real8_swap__"); 
8521 |     if (shmem_real8_swap___h == NULL) {
8522 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8523 |       return retval;
8524 |     }
8545 |   static shmem_real_get___p_h shmem_real_get___h = NULL;
8546 |   TAU_PROFILE_TIMER(t,"void shmem_real_get__(void *, void *, int *, int *)", "", TAU_USER);
8547 |   if (tau_handle == NULL) 
8548 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8549 | 
8550 |   if (tau_handle == NULL) { 
8551 |     perror("Error opening library in dlopen call"); 
8552 |     return;
8553 |   } 
8555 |     if (shmem_real_get___h == NULL)
8556 | 	shmem_real_get___h = (shmem_real_get___p_h) dlsym(tau_handle,"shmem_real_get__"); 
8557 |     if (shmem_real_get___h == NULL) {
8558 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8559 |       return;
8560 |     }
8578 |   static shmem_real_iget___p_h shmem_real_iget___h = NULL;
8579 |   TAU_PROFILE_TIMER(t,"void shmem_real_iget__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
8580 |   if (tau_handle == NULL) 
8581 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8582 | 
8583 |   if (tau_handle == NULL) { 
8584 |     perror("Error opening library in dlopen call"); 
8585 |     return;
8586 |   } 
8588 |     if (shmem_real_iget___h == NULL)
8589 | 	shmem_real_iget___h = (shmem_real_iget___p_h) dlsym(tau_handle,"shmem_real_iget__"); 
8590 |     if (shmem_real_iget___h == NULL) {
8591 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8592 |       return;
8593 |     }
8611 |   static shmem_real_iput___p_h shmem_real_iput___h = NULL;
8612 |   TAU_PROFILE_TIMER(t,"void shmem_real_iput__(void *, void *, int *, int *, int *, int *)", "", TAU_USER);
8613 |   if (tau_handle == NULL) 
8614 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8615 | 
8616 |   if (tau_handle == NULL) { 
8617 |     perror("Error opening library in dlopen call"); 
8618 |     return;
8619 |   } 
8621 |     if (shmem_real_iput___h == NULL)
8622 | 	shmem_real_iput___h = (shmem_real_iput___p_h) dlsym(tau_handle,"shmem_real_iput__"); 
8623 |     if (shmem_real_iput___h == NULL) {
8624 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8625 |       return;
8626 |     }
8644 |   static shmem_real_put___p_h shmem_real_put___h = NULL;
8645 |   TAU_PROFILE_TIMER(t,"void shmem_real_put__(void *, void *, int *, int *)", "", TAU_USER);
8646 |   if (tau_handle == NULL) 
8647 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8648 | 
8649 |   if (tau_handle == NULL) { 
8650 |     perror("Error opening library in dlopen call"); 
8651 |     return;
8652 |   } 
8654 |     if (shmem_real_put___h == NULL)
8655 | 	shmem_real_put___h = (shmem_real_put___p_h) dlsym(tau_handle,"shmem_real_put__"); 
8656 |     if (shmem_real_put___h == NULL) {
8657 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8658 |       return;
8659 |     }
8677 |   static shmem_set_cache_inv___p_h shmem_set_cache_inv___h = NULL;
8678 |   TAU_PROFILE_TIMER(t,"void shmem_set_cache_inv__()", "", TAU_USER);
8679 |   if (tau_handle == NULL) 
8680 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8681 | 
8682 |   if (tau_handle == NULL) { 
8683 |     perror("Error opening library in dlopen call"); 
8684 |     return;
8685 |   } 
8687 |     if (shmem_set_cache_inv___h == NULL)
8688 | 	shmem_set_cache_inv___h = (shmem_set_cache_inv___p_h) dlsym(tau_handle,"shmem_set_cache_inv__"); 
8689 |     if (shmem_set_cache_inv___h == NULL) {
8690 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8691 |       return;
8692 |     }
8708 |   static shmem_set_cache_line_inv___p_h shmem_set_cache_line_inv___h = NULL;
8709 |   TAU_PROFILE_TIMER(t,"void shmem_set_cache_line_inv__(void *)", "", TAU_USER);
8710 |   if (tau_handle == NULL) 
8711 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8712 | 
8713 |   if (tau_handle == NULL) { 
8714 |     perror("Error opening library in dlopen call"); 
8715 |     return;
8716 |   } 
8718 |     if (shmem_set_cache_line_inv___h == NULL)
8719 | 	shmem_set_cache_line_inv___h = (shmem_set_cache_line_inv___p_h) dlsym(tau_handle,"shmem_set_cache_line_inv__"); 
8720 |     if (shmem_set_cache_line_inv___h == NULL) {
8721 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8722 |       return;
8723 |     }
8739 |   static shmem_set_lock___p_h shmem_set_lock___h = NULL;
8740 |   TAU_PROFILE_TIMER(t,"void shmem_set_lock__(long *)", "", TAU_USER);
8741 |   if (tau_handle == NULL) 
8742 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8743 | 
8744 |   if (tau_handle == NULL) { 
8745 |     perror("Error opening library in dlopen call"); 
8746 |     return;
8747 |   } 
8749 |     if (shmem_set_lock___h == NULL)
8750 | 	shmem_set_lock___h = (shmem_set_lock___p_h) dlsym(tau_handle,"shmem_set_lock__"); 
8751 |     if (shmem_set_lock___h == NULL) {
8752 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8753 |       return;
8754 |     }
8771 |   int retval = 0;
8772 |   TAU_PROFILE_TIMER(t,"int shmem_swap__(void *, int *, int *)", "", TAU_USER);
8773 |   if (tau_handle == NULL) 
8774 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8775 | 
8776 |   if (tau_handle == NULL) { 
8777 |     perror("Error opening library in dlopen call"); 
8778 |     return retval;
8779 |   } 
8781 |     if (shmem_swap___h == NULL)
8782 | 	shmem_swap___h = (shmem_swap___p_h) dlsym(tau_handle,"shmem_swap__"); 
8783 |     if (shmem_swap___h == NULL) {
8784 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8785 |       return retval;
8786 |     }
8808 |   int retval = 0;
8809 |   TAU_PROFILE_TIMER(t,"int shmem_test_lock__(long *)", "", TAU_USER);
8810 |   if (tau_handle == NULL) 
8811 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8812 | 
8813 |   if (tau_handle == NULL) { 
8814 |     perror("Error opening library in dlopen call"); 
8815 |     return retval;
8816 |   } 
8818 |     if (shmem_test_lock___h == NULL)
8819 | 	shmem_test_lock___h = (shmem_test_lock___p_h) dlsym(tau_handle,"shmem_test_lock__"); 
8820 |     if (shmem_test_lock___h == NULL) {
8821 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8822 |       return retval;
8823 |     }
8840 |   static shmem_udcflush___p_h shmem_udcflush___h = NULL;
8841 |   TAU_PROFILE_TIMER(t,"void shmem_udcflush__()", "", TAU_USER);
8842 |   if (tau_handle == NULL) 
8843 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8844 | 
8845 |   if (tau_handle == NULL) { 
8846 |     perror("Error opening library in dlopen call"); 
8847 |     return;
8848 |   } 
8850 |     if (shmem_udcflush___h == NULL)
8851 | 	shmem_udcflush___h = (shmem_udcflush___p_h) dlsym(tau_handle,"shmem_udcflush__"); 
8852 |     if (shmem_udcflush___h == NULL) {
8853 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8854 |       return;
8855 |     }
8871 |   static shmem_udcflush_line___p_h shmem_udcflush_line___h = NULL;
8872 |   TAU_PROFILE_TIMER(t,"void shmem_udcflush_line__(void *)", "", TAU_USER);
8873 |   if (tau_handle == NULL) 
8874 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8875 | 
8876 |   if (tau_handle == NULL) { 
8877 |     perror("Error opening library in dlopen call"); 
8878 |     return;
8879 |   } 
8881 |     if (shmem_udcflush_line___h == NULL)
8882 | 	shmem_udcflush_line___h = (shmem_udcflush_line___p_h) dlsym(tau_handle,"shmem_udcflush_line__"); 
8883 |     if (shmem_udcflush_line___h == NULL) {
8884 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8885 |       return;
8886 |     }
8902 |   static shmem_wait___p_h shmem_wait___h = NULL;
8903 |   TAU_PROFILE_TIMER(t,"void shmem_wait__(long *, long *)", "", TAU_USER);
8904 |   if (tau_handle == NULL) 
8905 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8906 | 
8907 |   if (tau_handle == NULL) { 
8908 |     perror("Error opening library in dlopen call"); 
8909 |     return;
8910 |   } 
8912 |     if (shmem_wait___h == NULL)
8913 | 	shmem_wait___h = (shmem_wait___p_h) dlsym(tau_handle,"shmem_wait__"); 
8914 |     if (shmem_wait___h == NULL) {
8915 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8916 |       return;
8917 |     }
8933 |   static shmem_wait_until___p_h shmem_wait_until___h = NULL;
8934 |   TAU_PROFILE_TIMER(t,"void shmem_wait_until__(int *, int *, int *)", "", TAU_USER);
8935 |   if (tau_handle == NULL) 
8936 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8937 | 
8938 |   if (tau_handle == NULL) { 
8939 |     perror("Error opening library in dlopen call"); 
8940 |     return;
8941 |   } 
8943 |     if (shmem_wait_until___h == NULL)
8944 | 	shmem_wait_until___h = (shmem_wait_until___p_h) dlsym(tau_handle,"shmem_wait_until__"); 
8945 |     if (shmem_wait_until___h == NULL) {
8946 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8947 |       return;
8948 |     }
8964 |   static start_pes___p_h start_pes___h = NULL;
8965 |   TAU_PROFILE_TIMER(t,"void start_pes__(int *)", "", TAU_USER);
8966 |   if (tau_handle == NULL) 
8967 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8968 | 
8969 |   if (tau_handle == NULL) { 
8970 |     perror("Error opening library in dlopen call"); 
8971 |     return;
8972 |   } 
8974 |     if (start_pes___h == NULL)
8975 | 	start_pes___h = (start_pes___p_h) dlsym(tau_handle,"start_pes__"); 
8976 |     if (start_pes___h == NULL) {
8977 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8978 |       return;
8979 |     }
9002 |   static shmem_clear_cache_inv_p_h shmem_clear_cache_inv_h = NULL;
9003 |   TAU_PROFILE_TIMER(t,"void shmem_clear_cache_inv()", "", TAU_USER);
9004 |   if (tau_handle == NULL) 
9005 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9006 | 
9007 |   if (tau_handle == NULL) { 
9008 |     perror("Error opening library in dlopen call"); 
9009 |     return;
9010 |   } 
9012 |     if (shmem_clear_cache_inv_h == NULL)
9013 | 	shmem_clear_cache_inv_h = (shmem_clear_cache_inv_p_h) dlsym(tau_handle,"shmem_clear_cache_inv"); 
9014 |     if (shmem_clear_cache_inv_h == NULL) {
9015 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9016 |       return;
9017 |     }
9033 |   static shmem_set_cache_inv_p_h shmem_set_cache_inv_h = NULL;
9034 |   TAU_PROFILE_TIMER(t,"void shmem_set_cache_inv()", "", TAU_USER);
9035 |   if (tau_handle == NULL) 
9036 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9037 | 
9038 |   if (tau_handle == NULL) { 
9039 |     perror("Error opening library in dlopen call"); 
9040 |     return;
9041 |   } 
9043 |     if (shmem_set_cache_inv_h == NULL)
9044 | 	shmem_set_cache_inv_h = (shmem_set_cache_inv_p_h) dlsym(tau_handle,"shmem_set_cache_inv"); 
9045 |     if (shmem_set_cache_inv_h == NULL) {
9046 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9047 |       return;
9048 |     }
9064 |   static shmem_clear_cache_line_inv_p_h shmem_clear_cache_line_inv_h = NULL;
9065 |   TAU_PROFILE_TIMER(t,"void shmem_clear_cache_line_inv(void *)", "", TAU_USER);
9066 |   if (tau_handle == NULL) 
9067 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9068 | 
9069 |   if (tau_handle == NULL) { 
9070 |     perror("Error opening library in dlopen call"); 
9071 |     return;
9072 |   } 
9074 |     if (shmem_clear_cache_line_inv_h == NULL)
9075 | 	shmem_clear_cache_line_inv_h = (shmem_clear_cache_line_inv_p_h) dlsym(tau_handle,"shmem_clear_cache_line_inv"); 
9076 |     if (shmem_clear_cache_line_inv_h == NULL) {
9077 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9078 |       return;
9079 |     }
9095 |   static shmem_set_cache_line_inv_p_h shmem_set_cache_line_inv_h = NULL;
9096 |   TAU_PROFILE_TIMER(t,"void shmem_set_cache_line_inv(void *)", "", TAU_USER);
9097 |   if (tau_handle == NULL) 
9098 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9099 | 
9100 |   if (tau_handle == NULL) { 
9101 |     perror("Error opening library in dlopen call"); 
9102 |     return;
9103 |   } 
9105 |     if (shmem_set_cache_line_inv_h == NULL)
9106 | 	shmem_set_cache_line_inv_h = (shmem_set_cache_line_inv_p_h) dlsym(tau_handle,"shmem_set_cache_line_inv"); 
9107 |     if (shmem_set_cache_line_inv_h == NULL) {
9108 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9109 |       return;
9110 |     }
9127 |   int retval = 0;
9128 |   TAU_PROFILE_TIMER(t,"int my_pe_()", "", TAU_USER);
9129 |   if (tau_handle == NULL) 
9130 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9131 | 
9132 |   if (tau_handle == NULL) { 
9133 |     perror("Error opening library in dlopen call"); 
9134 |     return retval;
9135 |   } 
9137 |     if (my_pe__h == NULL)
9138 | 	my_pe__h = (my_pe__p_h) dlsym(tau_handle,"my_pe_"); 
9139 |     if (my_pe__h == NULL) {
9140 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9141 |       return retval;
9142 |     }
9160 |   int retval = 0;
9161 |   TAU_PROFILE_TIMER(t,"int my_pe__()", "", TAU_USER);
9162 |   if (tau_handle == NULL) 
9163 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9164 | 
9165 |   if (tau_handle == NULL) { 
9166 |     perror("Error opening library in dlopen call"); 
9167 |     return retval;
9168 |   } 
9170 |     if (my_pe___h == NULL)
9171 | 	my_pe___h = (my_pe___p_h) dlsym(tau_handle,"my_pe__"); 
9172 |     if (my_pe___h == NULL) {
9173 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9174 |       return retval;
9175 |     }
{% endraw %}

```
### apex/src/wrappers/pthread_wrapper.c

```c

{% raw %}
43 |   // #defines in Profiler.h, -Wl,-wrap on the link line, and LD_PRELOAD.
44 |   if (handle == caller) {
45 |     RESET_DLERROR();
46 |     void * syms = dlopen(NULL, RTLD_NOW);
47 |     CHECK_DLERROR();
48 |     do {
{% endraw %}

```