---
name: "tau"
layout: package
next_package: tcl
previous_package: swipl
library_name: dlsym
matches: ['dlsym', 'dlopen', 'dlmopen']
languages: ['c']
---
## 2.29.1
23 / 3452 files match, 11 filtered matches.

 - [src/wrappers/pthread/pthread_wrap.c](#srcwrapperspthreadpthread_wrapc)
 - [src/wrappers/pthread/sys_wrap.c](#srcwrapperspthreadsys_wrapc)
 - [src/wrappers/gomp/gomp_wrap.c](#srcwrappersgompgomp_wrapc)
 - [src/wrappers/mpcthread/mpcthread_wrap.c](#srcwrappersmpcthreadmpcthread_wrapc)
 - [src/wrappers/cuda/cuda_wrap.c](#srcwrapperscudacuda_wrapc)
 - [src/wrappers/shmem/tau_shmem_wrapper/wr_dynamic.c](#srcwrappersshmemtau_shmem_wrapperwr_dynamicc)
 - [src/wrappers/posixio/iowrap_shared.c](#srcwrappersposixioiowrap_sharedc)
 - [src/wrappers/taupreload/dl_auditor.c](#srcwrapperstaupreloaddl_auditorc)
 - [src/wrappers/memory/memory_wrapper_dynamic.c](#srcwrappersmemorymemory_wrapper_dynamicc)
 - [src/Profile/TauShmemSgiF.c](#srcprofiletaushmemsgifc)
 - [apex/src/wrappers/pthread_wrapper.c](#apexsrcwrapperspthread_wrapperc)

### src/wrappers/pthread/pthread_wrap.c

```c

{% raw %}
73 |   RESET_DLERROR();
74 | 
75 |   // Attempt to get the function handle
76 |   handle = dlsym(RTLD_NEXT, name);
77 | 
78 |   // Detect errors
87 |     CHECK_DLERROR();
88 |     do {
89 |       RESET_DLERROR();
90 |       handle = dlsym(syms, name);
91 |       CHECK_DLERROR();
92 |     } while (handle == caller);
{% endraw %}

```
### src/wrappers/pthread/sys_wrap.c

```c

{% raw %}
62 | 
63 |   /* Search for exit */
64 |   if (_internal_exit == NULL) {
65 |     _internal_exit = (void (*) (int status)) dlsym(RTLD_NEXT, "exit");
66 |   }
67 | 
84 | 
85 |   /* Search for exit_group */
86 |   if (_internal_exit_group == NULL) {
87 |     _internal_exit_group = (void (*) (int status)) dlsym(RTLD_NEXT, "exit_group");
88 |   }
89 | 
105 | 
106 |   /* Search for _exit */
107 |   if (_internal__exit == NULL) {
108 |     _internal__exit = (void (*) (int status)) dlsym(RTLD_NEXT, "_exit");
109 |   }
110 | 
123 | 
124 | 
125 |   if (_fork == NULL) {
126 |     _fork = (pid_t (*) (void)) dlsym(RTLD_NEXT, "fork");
127 |   }
128 | 
154 |   TAU_PROFILE_TIMER(t,"sleep inside kill timer","" ,TAU_DEFAULT);
155 |   /* Search for kill */
156 |   if (_kill == NULL) {
157 |     _kill = (int (*) (pid_t pid, int sig)) dlsym(RTLD_NEXT, "kill");
158 |   }
159 |   TAU_VERBOSE("TAU Kill Wrapper");
{% endraw %}

```
### src/wrappers/gomp/gomp_wrap.c

```c

{% raw %}
35 |     RESET_DLERROR();
36 | 
37 |     // Attempt to get the function handle
38 |     handle = dlsym(RTLD_NEXT, name);
39 | 
40 |     // Detect errors
49 |         CHECK_DLERROR();
50 |         do {
51 |             RESET_DLERROR();
52 |             handle = dlsym(syms, name);
53 |             CHECK_DLERROR();
54 |         } while (handle == caller);
{% endraw %}

```
### src/wrappers/mpcthread/mpcthread_wrap.c

```c

{% raw %}
70 | int sctk_user_thread_create (pthread_t* thread, const pthread_attr_t* attr, 
71 | 		    void *(*start_routine)(void*), void* arg) {
72 |   if (_sctk_user_thread_create == NULL) {
73 |     _sctk_user_thread_create = (int (*) (pthread_t* thread, const pthread_attr_t* attr, void *(*start_routine)(void*), void* arg)) dlsym(RTLD_NEXT, "sctk_user_thread_create");
74 |   }
75 | 	/*
84 | int sctk_thread_join (pthread_t thread, void **retval) {
85 |   int ret;
86 |   if (_sctk_thread_join == NULL) {
87 |     _sctk_thread_join = (int (*) (pthread_t, void **)) dlsym(RTLD_NEXT, "sctk_thread_join"); 
88 |   }
89 |    TAU_PROFILE_TIMER(timer, "sctk_thread_join()", "", TAU_DEFAULT);
95 | void sctk_thread_exit (void *value_ptr) {
96 | 
97 |   if (_sctk_thread_exit == NULL) {
98 |     _sctk_thread_exit = (void (*) (void *value_ptr)) dlsym(RTLD_NEXT, "sctk_thread_exit");
99 |   }
100 | 
106 | extern "C" int sctk_thread_barrier_wait(pthread_barrier_t *barrier) {
107 |   int retval;
108 |   if (_sctk_thread_barrier_wait == NULL) {
109 |     _sctk_thread_barrier_wait = (int (*) (pthread_barrier_t *barrier)) dlsym(RTLD_NEXT, "sctk_thread_barrier_wait");
110 |   }
111 |   TAU_PROFILE_TIMER(timer, "sctk_thread_barrier_wait", "", TAU_DEFAULT);
{% endraw %}

```
### src/wrappers/cuda/cuda_wrap.c

```c

{% raw %}
26 |   } 
27 |   else { 
28 |     if (cuInit_h == NULL)
29 | 	cuInit_h = (cuInit_p_h) dlsym(tau_handle,"cuInit"); 
30 |     if (cuInit_h == NULL) {
31 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
54 |   } 
55 |   else { 
56 |     if (cuDriverGetVersion_h == NULL)
57 | 	cuDriverGetVersion_h = (cuDriverGetVersion_p_h) dlsym(tau_handle,"cuDriverGetVersion"); 
58 |     if (cuDriverGetVersion_h == NULL) {
59 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
82 |   } 
83 |   else { 
84 |     if (cuDeviceGet_h == NULL)
85 | 	cuDeviceGet_h = (cuDeviceGet_p_h) dlsym(tau_handle,"cuDeviceGet"); 
86 |     if (cuDeviceGet_h == NULL) {
87 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
110 |   } 
111 |   else { 
112 |     if (cuDeviceGetCount_h == NULL)
113 | 	cuDeviceGetCount_h = (cuDeviceGetCount_p_h) dlsym(tau_handle,"cuDeviceGetCount"); 
114 |     if (cuDeviceGetCount_h == NULL) {
115 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
138 |   } 
139 |   else { 
140 |     if (cuDeviceGetName_h == NULL)
141 | 	cuDeviceGetName_h = (cuDeviceGetName_p_h) dlsym(tau_handle,"cuDeviceGetName"); 
142 |     if (cuDeviceGetName_h == NULL) {
143 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
166 |   } 
167 |   else { 
168 |     if (cuDeviceComputeCapability_h == NULL)
169 | 	cuDeviceComputeCapability_h = (cuDeviceComputeCapability_p_h) dlsym(tau_handle,"cuDeviceComputeCapability"); 
170 |     if (cuDeviceComputeCapability_h == NULL) {
171 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
194 |   } 
195 |   else { 
196 |     if (cuDeviceTotalMem_v2_h == NULL)
197 | 	cuDeviceTotalMem_v2_h = (cuDeviceTotalMem_v2_p_h) dlsym(tau_handle,"cuDeviceTotalMem_v2"); 
198 |     if (cuDeviceTotalMem_v2_h == NULL) {
199 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
222 |   } 
223 |   else { 
224 |     if (cuDeviceGetProperties_h == NULL)
225 | 	cuDeviceGetProperties_h = (cuDeviceGetProperties_p_h) dlsym(tau_handle,"cuDeviceGetProperties"); 
226 |     if (cuDeviceGetProperties_h == NULL) {
227 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
250 |   } 
251 |   else { 
252 |     if (cuDeviceGetAttribute_h == NULL)
253 | 	cuDeviceGetAttribute_h = (cuDeviceGetAttribute_p_h) dlsym(tau_handle,"cuDeviceGetAttribute"); 
254 |     if (cuDeviceGetAttribute_h == NULL) {
255 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
278 |   } 
279 |   else { 
280 |     if (cuCtxCreate_v2_h == NULL)
281 | 	cuCtxCreate_v2_h = (cuCtxCreate_v2_p_h) dlsym(tau_handle,"cuCtxCreate_v2"); 
282 |     if (cuCtxCreate_v2_h == NULL) {
283 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
306 |   } 
307 |   else { 
308 |     if (cuCtxDestroy_h == NULL)
309 | 	cuCtxDestroy_h = (cuCtxDestroy_p_h) dlsym(tau_handle,"cuCtxDestroy"); 
310 |     if (cuCtxDestroy_h == NULL) {
311 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
334 |   } 
335 |   else { 
336 |     if (cuCtxAttach_h == NULL)
337 | 	cuCtxAttach_h = (cuCtxAttach_p_h) dlsym(tau_handle,"cuCtxAttach"); 
338 |     if (cuCtxAttach_h == NULL) {
339 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
362 |   } 
363 |   else { 
364 |     if (cuCtxDetach_h == NULL)
365 | 	cuCtxDetach_h = (cuCtxDetach_p_h) dlsym(tau_handle,"cuCtxDetach"); 
366 |     if (cuCtxDetach_h == NULL) {
367 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
395 |   } 
396 |   else { 
397 |     if (cuCtxPushCurrent_h == NULL)
398 | 	cuCtxPushCurrent_h = (cuCtxPushCurrent_p_h) dlsym(tau_handle,"cuCtxPushCurrent"); 
399 |     if (cuCtxPushCurrent_h == NULL) {
400 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
423 |   } 
424 |   else { 
425 |     if (cuCtxPopCurrent_h == NULL)
426 | 	cuCtxPopCurrent_h = (cuCtxPopCurrent_p_h) dlsym(tau_handle,"cuCtxPopCurrent"); 
427 |     if (cuCtxPopCurrent_h == NULL) {
428 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
451 |   } 
452 |   else { 
453 |     if (cuCtxGetDevice_h == NULL)
454 | 	cuCtxGetDevice_h = (cuCtxGetDevice_p_h) dlsym(tau_handle,"cuCtxGetDevice"); 
455 |     if (cuCtxGetDevice_h == NULL) {
456 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
479 |   } 
480 |   else { 
481 |     if (cuCtxSynchronize_h == NULL)
482 | 	cuCtxSynchronize_h = (cuCtxSynchronize_p_h) dlsym(tau_handle,"cuCtxSynchronize"); 
483 |     if (cuCtxSynchronize_h == NULL) {
484 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
510 |   } 
511 |   else { 
512 |     if (cuCtxSetLimit_h == NULL)
513 | 	cuCtxSetLimit_h = (cuCtxSetLimit_p_h) dlsym(tau_handle,"cuCtxSetLimit"); 
514 |     if (cuCtxSetLimit_h == NULL) {
515 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
538 |   } 
539 |   else { 
540 |     if (cuCtxGetLimit_h == NULL)
541 | 	cuCtxGetLimit_h = (cuCtxGetLimit_p_h) dlsym(tau_handle,"cuCtxGetLimit"); 
542 |     if (cuCtxGetLimit_h == NULL) {
543 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
566 |   } 
567 |   else { 
568 |     if (cuCtxGetCacheConfig_h == NULL)
569 | 	cuCtxGetCacheConfig_h = (cuCtxGetCacheConfig_p_h) dlsym(tau_handle,"cuCtxGetCacheConfig"); 
570 |     if (cuCtxGetCacheConfig_h == NULL) {
571 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
594 |   } 
595 |   else { 
596 |     if (cuCtxSetCacheConfig_h == NULL)
597 | 	cuCtxSetCacheConfig_h = (cuCtxSetCacheConfig_p_h) dlsym(tau_handle,"cuCtxSetCacheConfig"); 
598 |     if (cuCtxSetCacheConfig_h == NULL) {
599 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
622 |   } 
623 |   else { 
624 |     if (cuCtxGetApiVersion_h == NULL)
625 | 	cuCtxGetApiVersion_h = (cuCtxGetApiVersion_p_h) dlsym(tau_handle,"cuCtxGetApiVersion"); 
626 |     if (cuCtxGetApiVersion_h == NULL) {
627 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
650 |   } 
651 |   else { 
652 |     if (cuModuleLoad_h == NULL)
653 | 	cuModuleLoad_h = (cuModuleLoad_p_h) dlsym(tau_handle,"cuModuleLoad"); 
654 |     if (cuModuleLoad_h == NULL) {
655 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
678 |   } 
679 |   else { 
680 |     if (cuModuleLoadData_h == NULL)
681 | 	cuModuleLoadData_h = (cuModuleLoadData_p_h) dlsym(tau_handle,"cuModuleLoadData"); 
682 |     if (cuModuleLoadData_h == NULL) {
683 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
706 |   } 
707 |   else { 
708 |     if (cuModuleLoadDataEx_h == NULL)
709 | 	cuModuleLoadDataEx_h = (cuModuleLoadDataEx_p_h) dlsym(tau_handle,"cuModuleLoadDataEx"); 
710 |     if (cuModuleLoadDataEx_h == NULL) {
711 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
734 |   } 
735 |   else { 
736 |     if (cuModuleLoadFatBinary_h == NULL)
737 | 	cuModuleLoadFatBinary_h = (cuModuleLoadFatBinary_p_h) dlsym(tau_handle,"cuModuleLoadFatBinary"); 
738 |     if (cuModuleLoadFatBinary_h == NULL) {
739 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
762 |   } 
763 |   else { 
764 |     if (cuModuleUnload_h == NULL)
765 | 	cuModuleUnload_h = (cuModuleUnload_p_h) dlsym(tau_handle,"cuModuleUnload"); 
766 |     if (cuModuleUnload_h == NULL) {
767 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
790 |   } 
791 |   else { 
792 |     if (cuModuleGetFunction_h == NULL)
793 | 	cuModuleGetFunction_h = (cuModuleGetFunction_p_h) dlsym(tau_handle,"cuModuleGetFunction"); 
794 |     if (cuModuleGetFunction_h == NULL) {
795 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
818 |   } 
819 |   else { 
820 |     if (cuModuleGetGlobal_v2_h == NULL)
821 | 	cuModuleGetGlobal_v2_h = (cuModuleGetGlobal_v2_p_h) dlsym(tau_handle,"cuModuleGetGlobal_v2"); 
822 |     if (cuModuleGetGlobal_v2_h == NULL) {
823 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
846 |   } 
847 |   else { 
848 |     if (cuModuleGetTexRef_h == NULL)
849 | 	cuModuleGetTexRef_h = (cuModuleGetTexRef_p_h) dlsym(tau_handle,"cuModuleGetTexRef"); 
850 |     if (cuModuleGetTexRef_h == NULL) {
851 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
874 |   } 
875 |   else { 
876 |     if (cuModuleGetSurfRef_h == NULL)
877 | 	cuModuleGetSurfRef_h = (cuModuleGetSurfRef_p_h) dlsym(tau_handle,"cuModuleGetSurfRef"); 
878 |     if (cuModuleGetSurfRef_h == NULL) {
879 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
902 |   } 
903 |   else { 
904 |     if (cuMemGetInfo_v2_h == NULL)
905 | 	cuMemGetInfo_v2_h = (cuMemGetInfo_v2_p_h) dlsym(tau_handle,"cuMemGetInfo_v2"); 
906 |     if (cuMemGetInfo_v2_h == NULL) {
907 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
930 |   } 
931 |   else { 
932 |     if (cuMemAllocManaged_h == NULL)
933 | 	cuMemAllocManaged_h = (cuMemAllocManaged_p_h) dlsym(tau_handle,"cuMemAllocManaged"); 
934 |     if (cuMemAllocManaged_h == NULL) {
935 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
958 |   } 
959 |   else { 
960 |     if (cuMemAlloc_v2_h == NULL)
961 | 	cuMemAlloc_v2_h = (cuMemAlloc_v2_p_h) dlsym(tau_handle,"cuMemAlloc_v2"); 
962 |     if (cuMemAlloc_v2_h == NULL) {
963 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
986 |   } 
987 |   else { 
988 |     if (cuMemAllocPitch_v2_h == NULL)
989 | 	cuMemAllocPitch_v2_h = (cuMemAllocPitch_v2_p_h) dlsym(tau_handle,"cuMemAllocPitch_v2"); 
990 |     if (cuMemAllocPitch_v2_h == NULL) {
991 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1014 |   } 
1015 |   else { 
1016 |     if (cuMemFree_v2_h == NULL)
1017 | 	cuMemFree_v2_h = (cuMemFree_v2_p_h) dlsym(tau_handle,"cuMemFree_v2"); 
1018 |     if (cuMemFree_v2_h == NULL) {
1019 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1042 |   } 
1043 |   else { 
1044 |     if (cuMemGetAddressRange_v2_h == NULL)
1045 | 	cuMemGetAddressRange_v2_h = (cuMemGetAddressRange_v2_p_h) dlsym(tau_handle,"cuMemGetAddressRange_v2"); 
1046 |     if (cuMemGetAddressRange_v2_h == NULL) {
1047 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1070 |   } 
1071 |   else { 
1072 |     if (cuMemAllocHost_v2_h == NULL)
1073 | 	cuMemAllocHost_v2_h = (cuMemAllocHost_v2_p_h) dlsym(tau_handle,"cuMemAllocHost_v2"); 
1074 |     if (cuMemAllocHost_v2_h == NULL) {
1075 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1098 |   } 
1099 |   else { 
1100 |     if (cuMemFreeHost_h == NULL)
1101 | 	cuMemFreeHost_h = (cuMemFreeHost_p_h) dlsym(tau_handle,"cuMemFreeHost"); 
1102 |     if (cuMemFreeHost_h == NULL) {
1103 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1126 |   } 
1127 |   else { 
1128 |     if (cuMemHostAlloc_h == NULL)
1129 | 	cuMemHostAlloc_h = (cuMemHostAlloc_p_h) dlsym(tau_handle,"cuMemHostAlloc"); 
1130 |     if (cuMemHostAlloc_h == NULL) {
1131 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1154 |   } 
1155 |   else { 
1156 |     if (cuMemHostGetDevicePointer_v2_h == NULL)
1157 | 	cuMemHostGetDevicePointer_v2_h = (cuMemHostGetDevicePointer_v2_p_h) dlsym(tau_handle,"cuMemHostGetDevicePointer_v2"); 
1158 |     if (cuMemHostGetDevicePointer_v2_h == NULL) {
1159 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1182 |   } 
1183 |   else { 
1184 |     if (cuMemHostGetFlags_h == NULL)
1185 | 	cuMemHostGetFlags_h = (cuMemHostGetFlags_p_h) dlsym(tau_handle,"cuMemHostGetFlags"); 
1186 |     if (cuMemHostGetFlags_h == NULL) {
1187 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1210 |   } 
1211 |   else { 
1212 |     if (cuMemcpyHtoD_v2_h == NULL)
1213 | 	cuMemcpyHtoD_v2_h = (cuMemcpyHtoD_v2_p_h) dlsym(tau_handle,"cuMemcpyHtoD_v2"); 
1214 |     if (cuMemcpyHtoD_v2_h == NULL) {
1215 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1238 |   } 
1239 |   else { 
1240 |     if (cuMemcpyDtoH_v2_h == NULL)
1241 | 	cuMemcpyDtoH_v2_h = (cuMemcpyDtoH_v2_p_h) dlsym(tau_handle,"cuMemcpyDtoH_v2"); 
1242 |     if (cuMemcpyDtoH_v2_h == NULL) {
1243 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1266 |   } 
1267 |   else { 
1268 |     if (cuMemcpyDtoD_v2_h == NULL)
1269 | 	cuMemcpyDtoD_v2_h = (cuMemcpyDtoD_v2_p_h) dlsym(tau_handle,"cuMemcpyDtoD_v2"); 
1270 |     if (cuMemcpyDtoD_v2_h == NULL) {
1271 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1294 |   } 
1295 |   else { 
1296 |     if (cuMemcpyDtoA_v2_h == NULL)
1297 | 	cuMemcpyDtoA_v2_h = (cuMemcpyDtoA_v2_p_h) dlsym(tau_handle,"cuMemcpyDtoA_v2"); 
1298 |     if (cuMemcpyDtoA_v2_h == NULL) {
1299 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1322 |   } 
1323 |   else { 
1324 |     if (cuMemcpyAtoD_v2_h == NULL)
1325 | 	cuMemcpyAtoD_v2_h = (cuMemcpyAtoD_v2_p_h) dlsym(tau_handle,"cuMemcpyAtoD_v2"); 
1326 |     if (cuMemcpyAtoD_v2_h == NULL) {
1327 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1350 |   } 
1351 |   else { 
1352 |     if (cuMemcpyHtoA_v2_h == NULL)
1353 | 	cuMemcpyHtoA_v2_h = (cuMemcpyHtoA_v2_p_h) dlsym(tau_handle,"cuMemcpyHtoA_v2"); 
1354 |     if (cuMemcpyHtoA_v2_h == NULL) {
1355 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1378 |   } 
1379 |   else { 
1380 |     if (cuMemcpyAtoH_v2_h == NULL)
1381 | 	cuMemcpyAtoH_v2_h = (cuMemcpyAtoH_v2_p_h) dlsym(tau_handle,"cuMemcpyAtoH_v2"); 
1382 |     if (cuMemcpyAtoH_v2_h == NULL) {
1383 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1406 |   } 
1407 |   else { 
1408 |     if (cuMemcpyAtoA_v2_h == NULL)
1409 | 	cuMemcpyAtoA_v2_h = (cuMemcpyAtoA_v2_p_h) dlsym(tau_handle,"cuMemcpyAtoA_v2"); 
1410 |     if (cuMemcpyAtoA_v2_h == NULL) {
1411 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1434 |   } 
1435 |   else { 
1436 |     if (cuMemcpy2D_v2_h == NULL)
1437 | 	cuMemcpy2D_v2_h = (cuMemcpy2D_v2_p_h) dlsym(tau_handle,"cuMemcpy2D_v2"); 
1438 |     if (cuMemcpy2D_v2_h == NULL) {
1439 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1462 |   } 
1463 |   else { 
1464 |     if (cuMemcpy2DUnaligned_v2_h == NULL)
1465 | 	cuMemcpy2DUnaligned_v2_h = (cuMemcpy2DUnaligned_v2_p_h) dlsym(tau_handle,"cuMemcpy2DUnaligned_v2"); 
1466 |     if (cuMemcpy2DUnaligned_v2_h == NULL) {
1467 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1490 |   } 
1491 |   else { 
1492 |     if (cuMemcpy3D_v2_h == NULL)
1493 | 	cuMemcpy3D_v2_h = (cuMemcpy3D_v2_p_h) dlsym(tau_handle,"cuMemcpy3D_v2"); 
1494 |     if (cuMemcpy3D_v2_h == NULL) {
1495 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1518 |   } 
1519 |   else { 
1520 |     if (cuMemcpyHtoDAsync_v2_h == NULL)
1521 | 	cuMemcpyHtoDAsync_v2_h = (cuMemcpyHtoDAsync_v2_p_h) dlsym(tau_handle,"cuMemcpyHtoDAsync_v2"); 
1522 |     if (cuMemcpyHtoDAsync_v2_h == NULL) {
1523 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1546 |   } 
1547 |   else { 
1548 |     if (cuMemcpyDtoHAsync_v2_h == NULL)
1549 | 	cuMemcpyDtoHAsync_v2_h = (cuMemcpyDtoHAsync_v2_p_h) dlsym(tau_handle,"cuMemcpyDtoHAsync_v2"); 
1550 |     if (cuMemcpyDtoHAsync_v2_h == NULL) {
1551 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1574 |   } 
1575 |   else { 
1576 |     if (cuMemcpyDtoDAsync_v2_h == NULL)
1577 | 	cuMemcpyDtoDAsync_v2_h = (cuMemcpyDtoDAsync_v2_p_h) dlsym(tau_handle,"cuMemcpyDtoDAsync_v2"); 
1578 |     if (cuMemcpyDtoDAsync_v2_h == NULL) {
1579 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1602 |   } 
1603 |   else { 
1604 |     if (cuMemcpyHtoAAsync_v2_h == NULL)
1605 | 	cuMemcpyHtoAAsync_v2_h = (cuMemcpyHtoAAsync_v2_p_h) dlsym(tau_handle,"cuMemcpyHtoAAsync_v2"); 
1606 |     if (cuMemcpyHtoAAsync_v2_h == NULL) {
1607 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1630 |   } 
1631 |   else { 
1632 |     if (cuMemcpyAtoHAsync_v2_h == NULL)
1633 | 	cuMemcpyAtoHAsync_v2_h = (cuMemcpyAtoHAsync_v2_p_h) dlsym(tau_handle,"cuMemcpyAtoHAsync_v2"); 
1634 |     if (cuMemcpyAtoHAsync_v2_h == NULL) {
1635 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1658 |   } 
1659 |   else { 
1660 |     if (cuMemcpy2DAsync_v2_h == NULL)
1661 | 	cuMemcpy2DAsync_v2_h = (cuMemcpy2DAsync_v2_p_h) dlsym(tau_handle,"cuMemcpy2DAsync_v2"); 
1662 |     if (cuMemcpy2DAsync_v2_h == NULL) {
1663 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1686 |   } 
1687 |   else { 
1688 |     if (cuMemcpy3DAsync_v2_h == NULL)
1689 | 	cuMemcpy3DAsync_v2_h = (cuMemcpy3DAsync_v2_p_h) dlsym(tau_handle,"cuMemcpy3DAsync_v2"); 
1690 |     if (cuMemcpy3DAsync_v2_h == NULL) {
1691 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1714 |   } 
1715 |   else { 
1716 |     if (cuMemsetD8_v2_h == NULL)
1717 | 	cuMemsetD8_v2_h = (cuMemsetD8_v2_p_h) dlsym(tau_handle,"cuMemsetD8_v2"); 
1718 |     if (cuMemsetD8_v2_h == NULL) {
1719 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1742 |   } 
1743 |   else { 
1744 |     if (cuMemsetD16_v2_h == NULL)
1745 | 	cuMemsetD16_v2_h = (cuMemsetD16_v2_p_h) dlsym(tau_handle,"cuMemsetD16_v2"); 
1746 |     if (cuMemsetD16_v2_h == NULL) {
1747 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1770 |   } 
1771 |   else { 
1772 |     if (cuMemsetD32_v2_h == NULL)
1773 | 	cuMemsetD32_v2_h = (cuMemsetD32_v2_p_h) dlsym(tau_handle,"cuMemsetD32_v2"); 
1774 |     if (cuMemsetD32_v2_h == NULL) {
1775 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1798 |   } 
1799 |   else { 
1800 |     if (cuMemsetD2D8_v2_h == NULL)
1801 | 	cuMemsetD2D8_v2_h = (cuMemsetD2D8_v2_p_h) dlsym(tau_handle,"cuMemsetD2D8_v2"); 
1802 |     if (cuMemsetD2D8_v2_h == NULL) {
1803 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1826 |   } 
1827 |   else { 
1828 |     if (cuMemsetD2D16_v2_h == NULL)
1829 | 	cuMemsetD2D16_v2_h = (cuMemsetD2D16_v2_p_h) dlsym(tau_handle,"cuMemsetD2D16_v2"); 
1830 |     if (cuMemsetD2D16_v2_h == NULL) {
1831 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1854 |   } 
1855 |   else { 
1856 |     if (cuMemsetD2D32_v2_h == NULL)
1857 | 	cuMemsetD2D32_v2_h = (cuMemsetD2D32_v2_p_h) dlsym(tau_handle,"cuMemsetD2D32_v2"); 
1858 |     if (cuMemsetD2D32_v2_h == NULL) {
1859 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1882 |   } 
1883 |   else { 
1884 |     if (cuMemsetD8Async_h == NULL)
1885 | 	cuMemsetD8Async_h = (cuMemsetD8Async_p_h) dlsym(tau_handle,"cuMemsetD8Async"); 
1886 |     if (cuMemsetD8Async_h == NULL) {
1887 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1910 |   } 
1911 |   else { 
1912 |     if (cuMemsetD16Async_h == NULL)
1913 | 	cuMemsetD16Async_h = (cuMemsetD16Async_p_h) dlsym(tau_handle,"cuMemsetD16Async"); 
1914 |     if (cuMemsetD16Async_h == NULL) {
1915 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1938 |   } 
1939 |   else { 
1940 |     if (cuMemsetD32Async_h == NULL)
1941 | 	cuMemsetD32Async_h = (cuMemsetD32Async_p_h) dlsym(tau_handle,"cuMemsetD32Async"); 
1942 |     if (cuMemsetD32Async_h == NULL) {
1943 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1966 |   } 
1967 |   else { 
1968 |     if (cuMemsetD2D8Async_h == NULL)
1969 | 	cuMemsetD2D8Async_h = (cuMemsetD2D8Async_p_h) dlsym(tau_handle,"cuMemsetD2D8Async"); 
1970 |     if (cuMemsetD2D8Async_h == NULL) {
1971 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1994 |   } 
1995 |   else { 
1996 |     if (cuMemsetD2D16Async_h == NULL)
1997 | 	cuMemsetD2D16Async_h = (cuMemsetD2D16Async_p_h) dlsym(tau_handle,"cuMemsetD2D16Async"); 
1998 |     if (cuMemsetD2D16Async_h == NULL) {
1999 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2022 |   } 
2023 |   else { 
2024 |     if (cuMemsetD2D32Async_h == NULL)
2025 | 	cuMemsetD2D32Async_h = (cuMemsetD2D32Async_p_h) dlsym(tau_handle,"cuMemsetD2D32Async"); 
2026 |     if (cuMemsetD2D32Async_h == NULL) {
2027 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2050 |   } 
2051 |   else { 
2052 |     if (cuArrayCreate_v2_h == NULL)
2053 | 	cuArrayCreate_v2_h = (cuArrayCreate_v2_p_h) dlsym(tau_handle,"cuArrayCreate_v2"); 
2054 |     if (cuArrayCreate_v2_h == NULL) {
2055 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2078 |   } 
2079 |   else { 
2080 |     if (cuArrayGetDescriptor_v2_h == NULL)
2081 | 	cuArrayGetDescriptor_v2_h = (cuArrayGetDescriptor_v2_p_h) dlsym(tau_handle,"cuArrayGetDescriptor_v2"); 
2082 |     if (cuArrayGetDescriptor_v2_h == NULL) {
2083 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2106 |   } 
2107 |   else { 
2108 |     if (cuArrayDestroy_h == NULL)
2109 | 	cuArrayDestroy_h = (cuArrayDestroy_p_h) dlsym(tau_handle,"cuArrayDestroy"); 
2110 |     if (cuArrayDestroy_h == NULL) {
2111 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2134 |   } 
2135 |   else { 
2136 |     if (cuArray3DCreate_v2_h == NULL)
2137 | 	cuArray3DCreate_v2_h = (cuArray3DCreate_v2_p_h) dlsym(tau_handle,"cuArray3DCreate_v2"); 
2138 |     if (cuArray3DCreate_v2_h == NULL) {
2139 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2162 |   } 
2163 |   else { 
2164 |     if (cuArray3DGetDescriptor_v2_h == NULL)
2165 | 	cuArray3DGetDescriptor_v2_h = (cuArray3DGetDescriptor_v2_p_h) dlsym(tau_handle,"cuArray3DGetDescriptor_v2"); 
2166 |     if (cuArray3DGetDescriptor_v2_h == NULL) {
2167 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2190 |   } 
2191 |   else { 
2192 |     if (cuStreamCreate_h == NULL)
2193 | 	cuStreamCreate_h = (cuStreamCreate_p_h) dlsym(tau_handle,"cuStreamCreate"); 
2194 |     if (cuStreamCreate_h == NULL) {
2195 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2218 |   } 
2219 |   else { 
2220 |     if (cuStreamWaitEvent_h == NULL)
2221 | 	cuStreamWaitEvent_h = (cuStreamWaitEvent_p_h) dlsym(tau_handle,"cuStreamWaitEvent"); 
2222 |     if (cuStreamWaitEvent_h == NULL) {
2223 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2246 |   } 
2247 |   else { 
2248 |     if (cuStreamQuery_h == NULL)
2249 | 	cuStreamQuery_h = (cuStreamQuery_p_h) dlsym(tau_handle,"cuStreamQuery"); 
2250 |     if (cuStreamQuery_h == NULL) {
2251 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2274 |   } 
2275 |   else { 
2276 |     if (cuStreamSynchronize_h == NULL)
2277 | 	cuStreamSynchronize_h = (cuStreamSynchronize_p_h) dlsym(tau_handle,"cuStreamSynchronize"); 
2278 |     if (cuStreamSynchronize_h == NULL) {
2279 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2305 |   } 
2306 |   else { 
2307 |     if (cuStreamDestroy_h == NULL)
2308 | 	cuStreamDestroy_h = (cuStreamDestroy_p_h) dlsym(tau_handle,"cuStreamDestroy"); 
2309 |     if (cuStreamDestroy_h == NULL) {
2310 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2333 |   } 
2334 |   else { 
2335 |     if (cuEventCreate_h == NULL)
2336 | 	cuEventCreate_h = (cuEventCreate_p_h) dlsym(tau_handle,"cuEventCreate"); 
2337 |     if (cuEventCreate_h == NULL) {
2338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2361 |   } 
2362 |   else { 
2363 |     if (cuEventRecord_h == NULL)
2364 | 	cuEventRecord_h = (cuEventRecord_p_h) dlsym(tau_handle,"cuEventRecord"); 
2365 |     if (cuEventRecord_h == NULL) {
2366 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2389 |   } 
2390 |   else { 
2391 |     if (cuEventQuery_h == NULL)
2392 | 	cuEventQuery_h = (cuEventQuery_p_h) dlsym(tau_handle,"cuEventQuery"); 
2393 |     if (cuEventQuery_h == NULL) {
2394 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2417 |   } 
2418 |   else { 
2419 |     if (cuEventSynchronize_h == NULL)
2420 | 	cuEventSynchronize_h = (cuEventSynchronize_p_h) dlsym(tau_handle,"cuEventSynchronize"); 
2421 |     if (cuEventSynchronize_h == NULL) {
2422 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2448 |   } 
2449 |   else { 
2450 |     if (cuEventDestroy_h == NULL)
2451 | 	cuEventDestroy_h = (cuEventDestroy_p_h) dlsym(tau_handle,"cuEventDestroy"); 
2452 |     if (cuEventDestroy_h == NULL) {
2453 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2476 |   } 
2477 |   else { 
2478 |     if (cuEventElapsedTime_h == NULL)
2479 | 	cuEventElapsedTime_h = (cuEventElapsedTime_p_h) dlsym(tau_handle,"cuEventElapsedTime"); 
2480 |     if (cuEventElapsedTime_h == NULL) {
2481 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2504 |   } 
2505 |   else { 
2506 |     if (cuFuncSetBlockShape_h == NULL)
2507 | 	cuFuncSetBlockShape_h = (cuFuncSetBlockShape_p_h) dlsym(tau_handle,"cuFuncSetBlockShape"); 
2508 |     if (cuFuncSetBlockShape_h == NULL) {
2509 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2532 |   } 
2533 |   else { 
2534 |     if (cuFuncSetSharedSize_h == NULL)
2535 | 	cuFuncSetSharedSize_h = (cuFuncSetSharedSize_p_h) dlsym(tau_handle,"cuFuncSetSharedSize"); 
2536 |     if (cuFuncSetSharedSize_h == NULL) {
2537 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2560 |   } 
2561 |   else { 
2562 |     if (cuFuncGetAttribute_h == NULL)
2563 | 	cuFuncGetAttribute_h = (cuFuncGetAttribute_p_h) dlsym(tau_handle,"cuFuncGetAttribute"); 
2564 |     if (cuFuncGetAttribute_h == NULL) {
2565 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2588 |   } 
2589 |   else { 
2590 |     if (cuFuncSetCacheConfig_h == NULL)
2591 | 	cuFuncSetCacheConfig_h = (cuFuncSetCacheConfig_p_h) dlsym(tau_handle,"cuFuncSetCacheConfig"); 
2592 |     if (cuFuncSetCacheConfig_h == NULL) {
2593 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2616 |   } 
2617 |   else { 
2618 |     if (cuParamSetSize_h == NULL)
2619 | 	cuParamSetSize_h = (cuParamSetSize_p_h) dlsym(tau_handle,"cuParamSetSize"); 
2620 |     if (cuParamSetSize_h == NULL) {
2621 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2644 |   } 
2645 |   else { 
2646 |     if (cuParamSeti_h == NULL)
2647 | 	cuParamSeti_h = (cuParamSeti_p_h) dlsym(tau_handle,"cuParamSeti"); 
2648 |     if (cuParamSeti_h == NULL) {
2649 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2672 |   } 
2673 |   else { 
2674 |     if (cuParamSetf_h == NULL)
2675 | 	cuParamSetf_h = (cuParamSetf_p_h) dlsym(tau_handle,"cuParamSetf"); 
2676 |     if (cuParamSetf_h == NULL) {
2677 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2700 |   } 
2701 |   else { 
2702 |     if (cuParamSetv_h == NULL)
2703 | 	cuParamSetv_h = (cuParamSetv_p_h) dlsym(tau_handle,"cuParamSetv"); 
2704 |     if (cuParamSetv_h == NULL) {
2705 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2728 |   } 
2729 |   else { 
2730 |     if (cuLaunch_h == NULL)
2731 | 	cuLaunch_h = (cuLaunch_p_h) dlsym(tau_handle,"cuLaunch"); 
2732 |     if (cuLaunch_h == NULL) {
2733 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2790 |   } 
2791 |   else { 
2792 |     if (cuLaunchKernel_h == NULL)
2793 | 	cuLaunchKernel_h = (cuLaunchKernel_p_h) dlsym(tau_handle,"cuLaunchKernel"); 
2794 |     if (cuLaunchKernel_h == NULL) {
2795 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2831 |   } 
2832 |   else { 
2833 |     if (cuLaunchGrid_h == NULL)
2834 | 	cuLaunchGrid_h = (cuLaunchGrid_p_h) dlsym(tau_handle,"cuLaunchGrid"); 
2835 |     if (cuLaunchGrid_h == NULL) {
2836 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2872 |   } 
2873 |   else { 
2874 |     if (cuLaunchGridAsync_h == NULL)
2875 | 	cuLaunchGridAsync_h = (cuLaunchGridAsync_p_h) dlsym(tau_handle,"cuLaunchGridAsync"); 
2876 |     if (cuLaunchGridAsync_h == NULL) {
2877 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2913 |   } 
2914 |   else { 
2915 |     if (cuParamSetTexRef_h == NULL)
2916 | 	cuParamSetTexRef_h = (cuParamSetTexRef_p_h) dlsym(tau_handle,"cuParamSetTexRef"); 
2917 |     if (cuParamSetTexRef_h == NULL) {
2918 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2941 |   } 
2942 |   else { 
2943 |     if (cuTexRefSetArray_h == NULL)
2944 | 	cuTexRefSetArray_h = (cuTexRefSetArray_p_h) dlsym(tau_handle,"cuTexRefSetArray"); 
2945 |     if (cuTexRefSetArray_h == NULL) {
2946 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2969 |   } 
2970 |   else { 
2971 |     if (cuTexRefSetAddress_v2_h == NULL)
2972 | 	cuTexRefSetAddress_v2_h = (cuTexRefSetAddress_v2_p_h) dlsym(tau_handle,"cuTexRefSetAddress_v2"); 
2973 |     if (cuTexRefSetAddress_v2_h == NULL) {
2974 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2997 |   } 
2998 |   else { 
2999 |     if (cuTexRefSetAddress2D_v2_h == NULL)
3000 | 	cuTexRefSetAddress2D_v2_h = (cuTexRefSetAddress2D_v2_p_h) dlsym(tau_handle,"cuTexRefSetAddress2D_v2"); 
3001 |     if (cuTexRefSetAddress2D_v2_h == NULL) {
3002 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3025 |   } 
3026 |   else { 
3027 |     if (cuTexRefSetFormat_h == NULL)
3028 | 	cuTexRefSetFormat_h = (cuTexRefSetFormat_p_h) dlsym(tau_handle,"cuTexRefSetFormat"); 
3029 |     if (cuTexRefSetFormat_h == NULL) {
3030 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3053 |   } 
3054 |   else { 
3055 |     if (cuTexRefSetAddressMode_h == NULL)
3056 | 	cuTexRefSetAddressMode_h = (cuTexRefSetAddressMode_p_h) dlsym(tau_handle,"cuTexRefSetAddressMode"); 
3057 |     if (cuTexRefSetAddressMode_h == NULL) {
3058 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3081 |   } 
3082 |   else { 
3083 |     if (cuTexRefSetFilterMode_h == NULL)
3084 | 	cuTexRefSetFilterMode_h = (cuTexRefSetFilterMode_p_h) dlsym(tau_handle,"cuTexRefSetFilterMode"); 
3085 |     if (cuTexRefSetFilterMode_h == NULL) {
3086 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3109 |   } 
3110 |   else { 
3111 |     if (cuTexRefSetFlags_h == NULL)
3112 | 	cuTexRefSetFlags_h = (cuTexRefSetFlags_p_h) dlsym(tau_handle,"cuTexRefSetFlags"); 
3113 |     if (cuTexRefSetFlags_h == NULL) {
3114 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3137 |   } 
3138 |   else { 
3139 |     if (cuTexRefGetAddress_v2_h == NULL)
3140 | 	cuTexRefGetAddress_v2_h = (cuTexRefGetAddress_v2_p_h) dlsym(tau_handle,"cuTexRefGetAddress_v2"); 
3141 |     if (cuTexRefGetAddress_v2_h == NULL) {
3142 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3165 |   } 
3166 |   else { 
3167 |     if (cuTexRefGetArray_h == NULL)
3168 | 	cuTexRefGetArray_h = (cuTexRefGetArray_p_h) dlsym(tau_handle,"cuTexRefGetArray"); 
3169 |     if (cuTexRefGetArray_h == NULL) {
3170 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3193 |   } 
3194 |   else { 
3195 |     if (cuTexRefGetAddressMode_h == NULL)
3196 | 	cuTexRefGetAddressMode_h = (cuTexRefGetAddressMode_p_h) dlsym(tau_handle,"cuTexRefGetAddressMode"); 
3197 |     if (cuTexRefGetAddressMode_h == NULL) {
3198 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3221 |   } 
3222 |   else { 
3223 |     if (cuTexRefGetFilterMode_h == NULL)
3224 | 	cuTexRefGetFilterMode_h = (cuTexRefGetFilterMode_p_h) dlsym(tau_handle,"cuTexRefGetFilterMode"); 
3225 |     if (cuTexRefGetFilterMode_h == NULL) {
3226 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3249 |   } 
3250 |   else { 
3251 |     if (cuTexRefGetFormat_h == NULL)
3252 | 	cuTexRefGetFormat_h = (cuTexRefGetFormat_p_h) dlsym(tau_handle,"cuTexRefGetFormat"); 
3253 |     if (cuTexRefGetFormat_h == NULL) {
3254 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3277 |   } 
3278 |   else { 
3279 |     if (cuTexRefGetFlags_h == NULL)
3280 | 	cuTexRefGetFlags_h = (cuTexRefGetFlags_p_h) dlsym(tau_handle,"cuTexRefGetFlags"); 
3281 |     if (cuTexRefGetFlags_h == NULL) {
3282 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3305 |   } 
3306 |   else { 
3307 |     if (cuTexRefCreate_h == NULL)
3308 | 	cuTexRefCreate_h = (cuTexRefCreate_p_h) dlsym(tau_handle,"cuTexRefCreate"); 
3309 |     if (cuTexRefCreate_h == NULL) {
3310 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3333 |   } 
3334 |   else { 
3335 |     if (cuTexRefDestroy_h == NULL)
3336 | 	cuTexRefDestroy_h = (cuTexRefDestroy_p_h) dlsym(tau_handle,"cuTexRefDestroy"); 
3337 |     if (cuTexRefDestroy_h == NULL) {
3338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3361 |   } 
3362 |   else { 
3363 |     if (cuSurfRefSetArray_h == NULL)
3364 | 	cuSurfRefSetArray_h = (cuSurfRefSetArray_p_h) dlsym(tau_handle,"cuSurfRefSetArray"); 
3365 |     if (cuSurfRefSetArray_h == NULL) {
3366 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3389 |   } 
3390 |   else { 
3391 |     if (cuSurfRefGetArray_h == NULL)
3392 | 	cuSurfRefGetArray_h = (cuSurfRefGetArray_p_h) dlsym(tau_handle,"cuSurfRefGetArray"); 
3393 |     if (cuSurfRefGetArray_h == NULL) {
3394 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3417 |   } 
3418 |   else { 
3419 |     if (cuGraphicsUnregisterResource_h == NULL)
3420 | 	cuGraphicsUnregisterResource_h = (cuGraphicsUnregisterResource_p_h) dlsym(tau_handle,"cuGraphicsUnregisterResource"); 
3421 |     if (cuGraphicsUnregisterResource_h == NULL) {
3422 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3445 |   } 
3446 |   else { 
3447 |     if (cuGraphicsSubResourceGetMappedArray_h == NULL)
3448 | 	cuGraphicsSubResourceGetMappedArray_h = (cuGraphicsSubResourceGetMappedArray_p_h) dlsym(tau_handle,"cuGraphicsSubResourceGetMappedArray"); 
3449 |     if (cuGraphicsSubResourceGetMappedArray_h == NULL) {
3450 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3473 |   } 
3474 |   else { 
3475 |     if (cuGraphicsResourceGetMappedPointer_v2_h == NULL)
3476 | 	cuGraphicsResourceGetMappedPointer_v2_h = (cuGraphicsResourceGetMappedPointer_v2_p_h) dlsym(tau_handle,"cuGraphicsResourceGetMappedPointer_v2"); 
3477 |     if (cuGraphicsResourceGetMappedPointer_v2_h == NULL) {
3478 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3501 |   } 
3502 |   else { 
3503 |     if (cuGraphicsResourceSetMapFlags_h == NULL)
3504 | 	cuGraphicsResourceSetMapFlags_h = (cuGraphicsResourceSetMapFlags_p_h) dlsym(tau_handle,"cuGraphicsResourceSetMapFlags"); 
3505 |     if (cuGraphicsResourceSetMapFlags_h == NULL) {
3506 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3529 |   } 
3530 |   else { 
3531 |     if (cuGraphicsMapResources_h == NULL)
3532 | 	cuGraphicsMapResources_h = (cuGraphicsMapResources_p_h) dlsym(tau_handle,"cuGraphicsMapResources"); 
3533 |     if (cuGraphicsMapResources_h == NULL) {
3534 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3557 |   } 
3558 |   else { 
3559 |     if (cuGraphicsUnmapResources_h == NULL)
3560 | 	cuGraphicsUnmapResources_h = (cuGraphicsUnmapResources_p_h) dlsym(tau_handle,"cuGraphicsUnmapResources"); 
3561 |     if (cuGraphicsUnmapResources_h == NULL) {
3562 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3585 |   } 
3586 |   else { 
3587 |     if (cuGetExportTable_h == NULL)
3588 | 	cuGetExportTable_h = (cuGetExportTable_p_h) dlsym(tau_handle,"cuGetExportTable"); 
3589 |     if (cuGetExportTable_h == NULL) {
3590 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
{% endraw %}

```
### src/wrappers/shmem/tau_shmem_wrapper/wr_dynamic.c

```c

{% raw %}
17 |   dlerror();
18 | 
19 |   // Attempt to get the function handle
20 |   handle = dlsym(RTLD_NEXT, name);
21 | 
22 |   // Detect errors
{% endraw %}

```
### src/wrappers/posixio/iowrap_shared.c

```c

{% raw %}
66 |   static FILE* (*_fopen)(const char *path, const char *mode) = NULL;
67 |   FILE *ret;
68 |   if (_fopen == NULL) {
69 |     _fopen = ( FILE* (*)(const char *path, const char *mode)) dlsym(RTLD_NEXT, "fopen");
70 |   }
71 | 
99 |   static FILE* (*_fopen64)(const char *path, const char *mode) = NULL;
100 |   FILE *ret;
101 |   if (_fopen64 == NULL) {
102 |     _fopen64 = ( FILE* (*)(const char *path, const char *mode)) dlsym(RTLD_NEXT, "fopen64");
103 |   }
104 | 
133 |   static FILE* (*_fdopen)(int fd, const char *mode) = NULL;
134 |   FILE *ret;
135 |   if (_fdopen == NULL) {
136 |     _fdopen = ( FILE* (*)(int fd, const char *mode)) dlsym(RTLD_NEXT, "fdopen");
137 |   }
138 | 
162 |   static FILE* (*_freopen)(const char *path, const char *mode, FILE *stream) = NULL;
163 |   FILE *ret;
164 |   if (_freopen == NULL) {
165 |     _freopen = ( FILE* (*)(const char *path, const char *mode, FILE *stream)) dlsym(RTLD_NEXT, "freopen");
166 |   }
167 | 
194 |   static int (*_fclose)(FILE *fp) = NULL;
195 |   int ret;
196 |   if (_fclose == NULL) {
197 |     _fclose = ( int (*)(FILE *fp)) dlsym(RTLD_NEXT, "fclose");
198 |   }
199 | 
226 |   static int (*_fprintf)(FILE *stream, const char *format, ...) = NULL;
227 |   int ret;
228 |   if (_fprintf == NULL) {
229 |     _fprintf = ( int (*)(FILE *stream, const char *format, ...)) dlsym(RTLD_NEXT, "fprintf");
230 |   }
231 | 
289 |   static int (*_fscanf)(FILE *stream, const char *format, ...) = NULL;
290 |   int ret;
291 |   if (_fscanf == NULL) {
292 |     _fscanf = ( int (*)(FILE *stream, const char *format, ...)) dlsym(RTLD_NEXT, "fscanf");
293 |   }
294 | 
348 |   static size_t (*_fwrite)(const void *ptr, size_t size, size_t nmemb, FILE *stream) = NULL;
349 |   size_t ret;
350 |   if (_fwrite == NULL) {
351 |     _fwrite = ( size_t (*)(const void *ptr, size_t size, size_t nmemb, FILE *stream)) dlsym(RTLD_NEXT, "fwrite");
352 |   }
353 | 
398 |   static size_t (*_fread)(void *ptr, size_t size, size_t nmemb, FILE *stream) = NULL;
399 |   int ret;
400 |   if (_fread == NULL) {
401 |     _fread = ( size_t (*)(void *ptr, size_t size, size_t nmemb, FILE *stream)) dlsym(RTLD_NEXT, "fread");
402 |   }
403 | 
449 |   static int (*_fcntl)(int fd, int cmd, ...) = NULL;
450 |   int ret;
451 |   if (_fcntl == NULL) {
452 |     _fcntl = ( int (*)(int fd, int cmd, ...)) dlsym(RTLD_NEXT, "fcntl");
453 |   }
454 | 
493 |   static off_t (*_lseek)(int fd, off_t offset, int whence) = NULL;
494 |   int ret;
495 |   if (_lseek == NULL) {
496 |     _lseek = ( off_t (*)(int fd, off_t offset, int whence)) dlsym(RTLD_NEXT, "lseek");   }
497 | 
498 |   if (Tau_iowrap_checkPassThrough()) {
520 |   static off64_t (*_lseek64)(int fd, off64_t offset, int whence) = NULL;
521 |   int ret;
522 |   if (_lseek64 == NULL) {
523 |     _lseek64 = ( off64_t (*)(int fd, off64_t offset, int whence)) dlsym(RTLD_NEXT, "lseek64");   }
524 | 
525 |   if (Tau_iowrap_checkPassThrough()) {
543 |   static int (*_fseek)(FILE *stream, long offset, int whence) = NULL;
544 |   int ret;
545 |   if (_fseek == NULL) {
546 |     _fseek = ( int (*)(FILE *stream, long offset, int whence)) dlsym(RTLD_NEXT, "fseek");
547 |   }
548 | 
567 | void rewind(FILE *stream) {
568 |   static void (*_rewind)(FILE *stream) = NULL;
569 |   if (_rewind == NULL) {
570 |     _rewind = ( void (*)(FILE *stream)) dlsym(RTLD_NEXT, "rewind");
571 |   }
572 | 
593 |   static ssize_t (*_write)(int fd, const void *buf, size_t count) = NULL;
594 |   ssize_t ret;
595 |   if (_write == NULL) {
596 |     _write = ( ssize_t (*)(int fd, const void *buf, size_t count)) dlsym(RTLD_NEXT, "write");
597 |   }
598 | 
645 |   ssize_t ret;
646 | 
647 |   if (_read == NULL) {
648 |     _read = ( ssize_t (*)(int fd, void *buf, size_t count)) dlsym(RTLD_NEXT, "read");
649 |   }
650 | 
695 |   ssize_t ret;
696 | 
697 |   if (_readv == NULL) {
698 |     _readv = ( ssize_t (*)(int fd, const struct iovec *vec, int count)) dlsym(RTLD_NEXT, "readv");
699 |   }
700 | 
753 |   double bw = 0.0;
754 | 
755 |   if (_writev == NULL) {
756 |     _writev = ( ssize_t (*)(int fd, const struct iovec *vec, int count)) dlsym(RTLD_NEXT, "writev");
757 |   }
758 | 
804 |   int ret;
805 | 
806 |   if (_mkstemp == NULL) {
807 |     _mkstemp = ( int (*)(char *templat)) dlsym(RTLD_NEXT, "mkstemp");
808 |   }
809 | 
836 |   FILE* ret;
837 | 
838 |   if (_tmpfile == NULL) {
839 |     _tmpfile = ( FILE* (*)()) dlsym(RTLD_NEXT, "tmpfile");
840 |   }
841 | 
871 |   int ret;
872 | 
873 |   if (_open == NULL) {
874 |     _open = ( int (*)(const char *pathname, int flags, ...)) dlsym(RTLD_NEXT, "open");
875 |   }
876 | 
924 |   int ret;
925 | 
926 |   if (_open64 == NULL) {
927 |      _open64 = ( int (*)(const char *pathname, int flags, ...)) dlsym(RTLD_NEXT, "open64");
928 |   }
929 | 
971 |   int ret;
972 | 
973 |   if (_creat == NULL) {
974 |      _creat = ( int (*)(const char *pathname, mode_t mode)) dlsym(RTLD_NEXT, "creat");
975 |   }
976 | 
1004 |   int ret;
1005 | 
1006 |   if (_creat64 == NULL) {
1007 |      _creat64 = ( int (*)(const char *pathname, mode_t mode)) dlsym(RTLD_NEXT, "creat64");
1008 |   }
1009 | 
1038 |   int ret;
1039 | 
1040 |   if (_close == NULL) {
1041 |     _close = (int (*) (int fd) ) dlsym(RTLD_NEXT, "close");
1042 |   }
1043 | 
1067 |   int ret;
1068 | 
1069 |   if (_pipe == NULL) {
1070 |     _pipe = (int (*) (int filedes[2]) ) dlsym(RTLD_NEXT, "pipe");
1071 |   }
1072 | 
1130 |   int ret;
1131 | 
1132 |   if (_socket == NULL) {
1133 |     _socket = (int (*) (int domain, int type, int protocol) ) dlsym(RTLD_NEXT, "socket");
1134 |   }
1135 | 
1162 |   int ret;
1163 | 
1164 |   if (_socketpair == NULL) {
1165 |     _socketpair = (int (*) (int d, int type, int protocol, int sv[2]) ) dlsym(RTLD_NEXT, "socketpair");
1166 |   }
1167 | 
1197 |   char socketname[TAU_MAX_FILENAME_LEN];
1198 | 
1199 |   if (_bind == NULL) {
1200 |     _bind = (int (*) (int socket, const struct sockaddr *address, socklen_t address_len) ) dlsym(RTLD_NEXT, "bind");
1201 |   }
1202 | 
1230 |   char socketname[TAU_MAX_FILENAME_LEN];
1231 | 
1232 |   if (_accept == NULL) {
1233 |     _accept = (int (*) (int socket, struct sockaddr *address, socklen_t* address_len) ) dlsym(RTLD_NEXT, "accept");
1234 |   }
1235 | 
1262 |   char socketname[2048];
1263 | 
1264 |   if (_connect == NULL) {
1265 |     _connect = (int (*) (int socket, const struct sockaddr *address, socklen_t address_len) ) dlsym(RTLD_NEXT, "connect");
1266 |   }
1267 | 
1292 |   ssize_t ret;
1293 | 
1294 |   if (_recv == NULL) {
1295 |     _recv = ( ssize_t (*)(int fd, void *buf, size_t count, int flags)) dlsym(RTLD_NEXT, "recv");
1296 |   }
1297 | 
1342 |   ssize_t ret;
1343 | 
1344 |   if (_send == NULL) {
1345 |     _send = ( ssize_t (*)(int fd, const void *buf, size_t count, int flags)) dlsym(RTLD_NEXT, "send");
1346 |   }
1347 | 
1393 |   ssize_t ret;
1394 | 
1395 |   if (_sendto == NULL) {
1396 |     _sendto = ( ssize_t (*)(int fd, const void *buf, size_t count, int flags, const struct sockaddr *to, socklen_t len)) dlsym(RTLD_NEXT, "sendto");
1397 |   }
1398 | 
1445 |   ssize_t ret;
1446 | 
1447 |   if (_recvfrom == NULL) {
1448 |     _recvfrom = ( ssize_t (*)(int fd, void *buf, size_t count, int flags, struct sockaddr * from, socklen_t * len)) dlsym(RTLD_NEXT, "recvfrom");
1449 |   }
1450 | 
1496 |   int fd;
1497 | 
1498 |   if (_dup == NULL) {
1499 |     _dup = ( int(*)(int fd)) dlsym(RTLD_NEXT, "dup");
1500 |   }
1501 | 
1515 |   static int (*_dup2)(int oldfd, int newfd) = NULL;
1516 | 
1517 |   if (_dup2 == NULL) {
1518 |     _dup2 = ( int(*)(int fd, int newfd)) dlsym(RTLD_NEXT, "dup2");
1519 |   }
1520 | 
1535 |   FILE* ret;
1536 | 
1537 |   if (_popen == NULL) {
1538 |     _popen = ( FILE * (*)(const char *command, const char *type)) dlsym(RTLD_NEXT, "popen");
1539 |   }
1540 | 
1564 |   int ret;
1565 | 
1566 |   if (_pclose == NULL) {
1567 |     _pclose = (int (*) (FILE * stream) ) dlsym(RTLD_NEXT, "pclose");
1568 |   }
1569 | 
1591 |   int ret;
1592 | 
1593 |   if (_aio_read == NULL) {
1594 |     _aio_read = (int (*) (struct aiocb *aiocbp) ) dlsym(RTLD_NEXT, "aio_read");
1595 |   }
1596 | 
1614 |   int ret;
1615 | 
1616 |   if (_aio_write == NULL) {
1617 |     _aio_write = (int (*) (struct aiocb *aiocbp) ) dlsym(RTLD_NEXT, "aio_write");
1618 |   }
1619 | 
1637 |   int ret;
1638 | 
1639 |   if (_aio_error == NULL) {
1640 |     _aio_error = (int (*) (const struct aiocb *aiocbp) ) dlsym(RTLD_NEXT, "aio_error");
1641 |   }
1642 | 
1675 |   ssize_t ret;
1676 | 
1677 |   if (_aio_return == NULL) {
1678 |     _aio_return = (ssize_t (*) (struct aiocb *aiocbp) ) dlsym(RTLD_NEXT, "aio_return");
1679 |   }
1680 | 
1698 |   int ret;
1699 | 
1700 |   if (_aio_suspend == NULL) {
1701 |     _aio_suspend = (int (*) (const struct aiocb * const cblist[], int n, const struct timespec *timeout) ) dlsym(RTLD_NEXT, "aio_suspend");
1702 |   }
1703 | 
1721 |   int ret;
1722 | 
1723 |   if (_aio_cancel == NULL) {
1724 |     _aio_cancel = (int (*) (int fd, struct aiocb *aiocbp) ) dlsym(RTLD_NEXT, "aio_cancel");
1725 |   }
1726 | 
1745 |   ssize_t ret;
1746 | 
1747 |   if (_lio_listio == NULL) {
1748 |     _lio_listio = (int (*) (int mode, struct aiocb * const list[], int nent, struct sigevent *sig)) dlsym(RTLD_NEXT, "lio_listio");
1749 |   }
1750 | 
1776 | 
1777 | 
1778 |   if (_internal_exit == NULL) {
1779 |     _internal_exit = (void (*) (int status)) dlsym(RTLD_NEXT, "exit");
1780 |   }
1781 | 
{% endraw %}

```
### src/wrappers/taupreload/dl_auditor.c

```c

{% raw %}
41 |     char const * err;
42 | 
43 |     dlerror(); // reset error flag
44 |     Tau_init_dl_initialized = (Tau_init_dl_initialized_t)dlsym(tau_so, "Tau_init_dl_initialized");
45 |     Tau_bfd_register_objopen_counter = (Tau_bfd_register_objopen_counter_t)dlsym(tau_so, "Tau_bfd_register_objopen_counter");
46 |     // Check for errors
47 |     if ((err = dlerror())) {
{% endraw %}

```
### src/wrappers/memory/memory_wrapper_dynamic.c

```c

{% raw %}
41 |   dlerror();
42 | 
43 |   // Attempt to get the function handle
44 |   handle = dlsym(RTLD_NEXT, name);
45 | 
46 |   // Detect errors
{% endraw %}

```
### src/Profile/TauShmemSgiF.c

```c

{% raw %}
28 |   } 
29 |   else { 
30 |     if (shmem_addr_accessible__h == NULL)
31 | 	shmem_addr_accessible__h = (shmem_addr_accessible__p_h) dlsym(tau_handle,"shmem_addr_accessible_"); 
32 |     if (shmem_addr_accessible__h == NULL) {
33 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
59 |   } 
60 |   else { 
61 |     if (shmem_barrier__h == NULL)
62 | 	shmem_barrier__h = (shmem_barrier__p_h) dlsym(tau_handle,"shmem_barrier_"); 
63 |     if (shmem_barrier__h == NULL) {
64 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
90 |   } 
91 |   else { 
92 |     if (shmem_barrier_all__h == NULL)
93 | 	shmem_barrier_all__h = (shmem_barrier_all__p_h) dlsym(tau_handle,"shmem_barrier_all_"); 
94 |     if (shmem_barrier_all__h == NULL) {
95 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
121 |   } 
122 |   else { 
123 |     if (shmem_barrier_ps__h == NULL)
124 | 	shmem_barrier_ps__h = (shmem_barrier_ps__p_h) dlsym(tau_handle,"shmem_barrier_ps_"); 
125 |     if (shmem_barrier_ps__h == NULL) {
126 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
152 |   } 
153 |   else { 
154 |     if (shmem_broadcast32__h == NULL)
155 | 	shmem_broadcast32__h = (shmem_broadcast32__p_h) dlsym(tau_handle,"shmem_broadcast32_"); 
156 |     if (shmem_broadcast32__h == NULL) {
157 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
183 |   } 
184 |   else { 
185 |     if (shmem_broadcast4__h == NULL)
186 | 	shmem_broadcast4__h = (shmem_broadcast4__p_h) dlsym(tau_handle,"shmem_broadcast4_"); 
187 |     if (shmem_broadcast4__h == NULL) {
188 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
214 |   } 
215 |   else { 
216 |     if (shmem_broadcast64__h == NULL)
217 | 	shmem_broadcast64__h = (shmem_broadcast64__p_h) dlsym(tau_handle,"shmem_broadcast64_"); 
218 |     if (shmem_broadcast64__h == NULL) {
219 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
245 |   } 
246 |   else { 
247 |     if (shmem_broadcast8__h == NULL)
248 | 	shmem_broadcast8__h = (shmem_broadcast8__p_h) dlsym(tau_handle,"shmem_broadcast8_"); 
249 |     if (shmem_broadcast8__h == NULL) {
250 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
276 |   } 
277 |   else { 
278 |     if (shmem_character_get__h == NULL)
279 | 	shmem_character_get__h = (shmem_character_get__p_h) dlsym(tau_handle,"shmem_character_get_"); 
280 |     if (shmem_character_get__h == NULL) {
281 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
309 |   } 
310 |   else { 
311 |     if (shmem_character_put__h == NULL)
312 | 	shmem_character_put__h = (shmem_character_put__p_h) dlsym(tau_handle,"shmem_character_put_"); 
313 |     if (shmem_character_put__h == NULL) {
314 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
342 |   } 
343 |   else { 
344 |     if (shmem_clear_cache_inv__h == NULL)
345 | 	shmem_clear_cache_inv__h = (shmem_clear_cache_inv__p_h) dlsym(tau_handle,"shmem_clear_cache_inv_"); 
346 |     if (shmem_clear_cache_inv__h == NULL) {
347 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
373 |   } 
374 |   else { 
375 |     if (shmem_clear_cache_line_inv__h == NULL)
376 | 	shmem_clear_cache_line_inv__h = (shmem_clear_cache_line_inv__p_h) dlsym(tau_handle,"shmem_clear_cache_line_inv_"); 
377 |     if (shmem_clear_cache_line_inv__h == NULL) {
378 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
404 |   } 
405 |   else { 
406 |     if (shmem_clear_lock__h == NULL)
407 | 	shmem_clear_lock__h = (shmem_clear_lock__p_h) dlsym(tau_handle,"shmem_clear_lock_"); 
408 |     if (shmem_clear_lock__h == NULL) {
409 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
435 |   } 
436 |   else { 
437 |     if (shmem_collect4__h == NULL)
438 | 	shmem_collect4__h = (shmem_collect4__p_h) dlsym(tau_handle,"shmem_collect4_"); 
439 |     if (shmem_collect4__h == NULL) {
440 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
466 |   } 
467 |   else { 
468 |     if (shmem_collect64__h == NULL)
469 | 	shmem_collect64__h = (shmem_collect64__p_h) dlsym(tau_handle,"shmem_collect64_"); 
470 |     if (shmem_collect64__h == NULL) {
471 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
497 |   } 
498 |   else { 
499 |     if (shmem_collect8__h == NULL)
500 | 	shmem_collect8__h = (shmem_collect8__p_h) dlsym(tau_handle,"shmem_collect8_"); 
501 |     if (shmem_collect8__h == NULL) {
502 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
528 |   } 
529 |   else { 
530 |     if (shmem_comp4_prod_to_all__h == NULL)
531 | 	shmem_comp4_prod_to_all__h = (shmem_comp4_prod_to_all__p_h) dlsym(tau_handle,"shmem_comp4_prod_to_all_"); 
532 |     if (shmem_comp4_prod_to_all__h == NULL) {
533 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
559 |   } 
560 |   else { 
561 |     if (shmem_comp4_sum_to_all__h == NULL)
562 | 	shmem_comp4_sum_to_all__h = (shmem_comp4_sum_to_all__p_h) dlsym(tau_handle,"shmem_comp4_sum_to_all_"); 
563 |     if (shmem_comp4_sum_to_all__h == NULL) {
564 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
590 |   } 
591 |   else { 
592 |     if (shmem_comp8_prod_to_all__h == NULL)
593 | 	shmem_comp8_prod_to_all__h = (shmem_comp8_prod_to_all__p_h) dlsym(tau_handle,"shmem_comp8_prod_to_all_"); 
594 |     if (shmem_comp8_prod_to_all__h == NULL) {
595 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
621 |   } 
622 |   else { 
623 |     if (shmem_comp8_sum_to_all__h == NULL)
624 | 	shmem_comp8_sum_to_all__h = (shmem_comp8_sum_to_all__p_h) dlsym(tau_handle,"shmem_comp8_sum_to_all_"); 
625 |     if (shmem_comp8_sum_to_all__h == NULL) {
626 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
652 |   } 
653 |   else { 
654 |     if (shmem_complex_get__h == NULL)
655 | 	shmem_complex_get__h = (shmem_complex_get__p_h) dlsym(tau_handle,"shmem_complex_get_"); 
656 |     if (shmem_complex_get__h == NULL) {
657 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
685 |   } 
686 |   else { 
687 |     if (shmem_complex_iget__h == NULL)
688 | 	shmem_complex_iget__h = (shmem_complex_iget__p_h) dlsym(tau_handle,"shmem_complex_iget_"); 
689 |     if (shmem_complex_iget__h == NULL) {
690 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
718 |   } 
719 |   else { 
720 |     if (shmem_complex_iput__h == NULL)
721 | 	shmem_complex_iput__h = (shmem_complex_iput__p_h) dlsym(tau_handle,"shmem_complex_iput_"); 
722 |     if (shmem_complex_iput__h == NULL) {
723 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
751 |   } 
752 |   else { 
753 |     if (shmem_complex_put__h == NULL)
754 | 	shmem_complex_put__h = (shmem_complex_put__p_h) dlsym(tau_handle,"shmem_complex_put_"); 
755 |     if (shmem_complex_put__h == NULL) {
756 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
784 |   } 
785 |   else { 
786 |     if (shmem_double_get__h == NULL)
787 | 	shmem_double_get__h = (shmem_double_get__p_h) dlsym(tau_handle,"shmem_double_get_"); 
788 |     if (shmem_double_get__h == NULL) {
789 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
817 |   } 
818 |   else { 
819 |     if (shmem_double_iget__h == NULL)
820 | 	shmem_double_iget__h = (shmem_double_iget__p_h) dlsym(tau_handle,"shmem_double_iget_"); 
821 |     if (shmem_double_iget__h == NULL) {
822 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
850 |   } 
851 |   else { 
852 |     if (shmem_double_iput__h == NULL)
853 | 	shmem_double_iput__h = (shmem_double_iput__p_h) dlsym(tau_handle,"shmem_double_iput_"); 
854 |     if (shmem_double_iput__h == NULL) {
855 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
883 |   } 
884 |   else { 
885 |     if (shmem_double_put__h == NULL)
886 | 	shmem_double_put__h = (shmem_double_put__p_h) dlsym(tau_handle,"shmem_double_put_"); 
887 |     if (shmem_double_put__h == NULL) {
888 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
916 |   } 
917 |   else { 
918 |     if (shmem_fcollect32__h == NULL)
919 | 	shmem_fcollect32__h = (shmem_fcollect32__p_h) dlsym(tau_handle,"shmem_fcollect32_"); 
920 |     if (shmem_fcollect32__h == NULL) {
921 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
947 |   } 
948 |   else { 
949 |     if (shmem_fcollect4__h == NULL)
950 | 	shmem_fcollect4__h = (shmem_fcollect4__p_h) dlsym(tau_handle,"shmem_fcollect4_"); 
951 |     if (shmem_fcollect4__h == NULL) {
952 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
978 |   } 
979 |   else { 
980 |     if (shmem_fcollect64__h == NULL)
981 | 	shmem_fcollect64__h = (shmem_fcollect64__p_h) dlsym(tau_handle,"shmem_fcollect64_"); 
982 |     if (shmem_fcollect64__h == NULL) {
983 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1009 |   } 
1010 |   else { 
1011 |     if (shmem_fcollect8__h == NULL)
1012 | 	shmem_fcollect8__h = (shmem_fcollect8__p_h) dlsym(tau_handle,"shmem_fcollect8_"); 
1013 |     if (shmem_fcollect8__h == NULL) {
1014 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1040 |   } 
1041 |   else { 
1042 |     if (shmem_fence__h == NULL)
1043 | 	shmem_fence__h = (shmem_fence__p_h) dlsym(tau_handle,"shmem_fence_"); 
1044 |     if (shmem_fence__h == NULL) {
1045 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1071 |   } 
1072 |   else { 
1073 |     if (shmem_get128__h == NULL)
1074 | 	shmem_get128__h = (shmem_get128__p_h) dlsym(tau_handle,"shmem_get128_"); 
1075 |     if (shmem_get128__h == NULL) {
1076 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1104 |   } 
1105 |   else { 
1106 |     if (shmem_get16__h == NULL)
1107 | 	shmem_get16__h = (shmem_get16__p_h) dlsym(tau_handle,"shmem_get16_"); 
1108 |     if (shmem_get16__h == NULL) {
1109 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1137 |   } 
1138 |   else { 
1139 |     if (shmem_get32__h == NULL)
1140 | 	shmem_get32__h = (shmem_get32__p_h) dlsym(tau_handle,"shmem_get32_"); 
1141 |     if (shmem_get32__h == NULL) {
1142 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1170 |   } 
1171 |   else { 
1172 |     if (shmem_get4__h == NULL)
1173 | 	shmem_get4__h = (shmem_get4__p_h) dlsym(tau_handle,"shmem_get4_"); 
1174 |     if (shmem_get4__h == NULL) {
1175 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1203 |   } 
1204 |   else { 
1205 |     if (shmem_get64__h == NULL)
1206 | 	shmem_get64__h = (shmem_get64__p_h) dlsym(tau_handle,"shmem_get64_"); 
1207 |     if (shmem_get64__h == NULL) {
1208 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1236 |   } 
1237 |   else { 
1238 |     if (shmem_get8__h == NULL)
1239 | 	shmem_get8__h = (shmem_get8__p_h) dlsym(tau_handle,"shmem_get8_"); 
1240 |     if (shmem_get8__h == NULL) {
1241 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1269 |   } 
1270 |   else { 
1271 |     if (shmem_getmem__h == NULL)
1272 | 	shmem_getmem__h = (shmem_getmem__p_h) dlsym(tau_handle,"shmem_getmem_"); 
1273 |     if (shmem_getmem__h == NULL) {
1274 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1302 |   } 
1303 |   else { 
1304 |     if (shmem_group_create_strided__h == NULL)
1305 | 	shmem_group_create_strided__h = (shmem_group_create_strided__p_h) dlsym(tau_handle,"shmem_group_create_strided_"); 
1306 |     if (shmem_group_create_strided__h == NULL) {
1307 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1333 |   } 
1334 |   else { 
1335 |     if (shmem_group_delete__h == NULL)
1336 | 	shmem_group_delete__h = (shmem_group_delete__p_h) dlsym(tau_handle,"shmem_group_delete_"); 
1337 |     if (shmem_group_delete__h == NULL) {
1338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1364 |   } 
1365 |   else { 
1366 |     if (shmem_iget128__h == NULL)
1367 | 	shmem_iget128__h = (shmem_iget128__p_h) dlsym(tau_handle,"shmem_iget128_"); 
1368 |     if (shmem_iget128__h == NULL) {
1369 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1397 |   } 
1398 |   else { 
1399 |     if (shmem_iget16__h == NULL)
1400 | 	shmem_iget16__h = (shmem_iget16__p_h) dlsym(tau_handle,"shmem_iget16_"); 
1401 |     if (shmem_iget16__h == NULL) {
1402 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1430 |   } 
1431 |   else { 
1432 |     if (shmem_iget32__h == NULL)
1433 | 	shmem_iget32__h = (shmem_iget32__p_h) dlsym(tau_handle,"shmem_iget32_"); 
1434 |     if (shmem_iget32__h == NULL) {
1435 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1463 |   } 
1464 |   else { 
1465 |     if (shmem_iget4__h == NULL)
1466 | 	shmem_iget4__h = (shmem_iget4__p_h) dlsym(tau_handle,"shmem_iget4_"); 
1467 |     if (shmem_iget4__h == NULL) {
1468 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1496 |   } 
1497 |   else { 
1498 |     if (shmem_iget64__h == NULL)
1499 | 	shmem_iget64__h = (shmem_iget64__p_h) dlsym(tau_handle,"shmem_iget64_"); 
1500 |     if (shmem_iget64__h == NULL) {
1501 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1529 |   } 
1530 |   else { 
1531 |     if (shmem_iget8__h == NULL)
1532 | 	shmem_iget8__h = (shmem_iget8__p_h) dlsym(tau_handle,"shmem_iget8_"); 
1533 |     if (shmem_iget8__h == NULL) {
1534 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1562 |   } 
1563 |   else { 
1564 |     if (shmem_int2_and_to_all__h == NULL)
1565 | 	shmem_int2_and_to_all__h = (shmem_int2_and_to_all__p_h) dlsym(tau_handle,"shmem_int2_and_to_all_"); 
1566 |     if (shmem_int2_and_to_all__h == NULL) {
1567 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1593 |   } 
1594 |   else { 
1595 |     if (shmem_int2_max_to_all__h == NULL)
1596 | 	shmem_int2_max_to_all__h = (shmem_int2_max_to_all__p_h) dlsym(tau_handle,"shmem_int2_max_to_all_"); 
1597 |     if (shmem_int2_max_to_all__h == NULL) {
1598 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1624 |   } 
1625 |   else { 
1626 |     if (shmem_int2_min_to_all__h == NULL)
1627 | 	shmem_int2_min_to_all__h = (shmem_int2_min_to_all__p_h) dlsym(tau_handle,"shmem_int2_min_to_all_"); 
1628 |     if (shmem_int2_min_to_all__h == NULL) {
1629 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1655 |   } 
1656 |   else { 
1657 |     if (shmem_int2_or_to_all__h == NULL)
1658 | 	shmem_int2_or_to_all__h = (shmem_int2_or_to_all__p_h) dlsym(tau_handle,"shmem_int2_or_to_all_"); 
1659 |     if (shmem_int2_or_to_all__h == NULL) {
1660 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1686 |   } 
1687 |   else { 
1688 |     if (shmem_int2_prod_to_all__h == NULL)
1689 | 	shmem_int2_prod_to_all__h = (shmem_int2_prod_to_all__p_h) dlsym(tau_handle,"shmem_int2_prod_to_all_"); 
1690 |     if (shmem_int2_prod_to_all__h == NULL) {
1691 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1717 |   } 
1718 |   else { 
1719 |     if (shmem_int2_sum_to_all__h == NULL)
1720 | 	shmem_int2_sum_to_all__h = (shmem_int2_sum_to_all__p_h) dlsym(tau_handle,"shmem_int2_sum_to_all_"); 
1721 |     if (shmem_int2_sum_to_all__h == NULL) {
1722 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1748 |   } 
1749 |   else { 
1750 |     if (shmem_int2_xor_to_all__h == NULL)
1751 | 	shmem_int2_xor_to_all__h = (shmem_int2_xor_to_all__p_h) dlsym(tau_handle,"shmem_int2_xor_to_all_"); 
1752 |     if (shmem_int2_xor_to_all__h == NULL) {
1753 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1779 |   } 
1780 |   else { 
1781 |     if (shmem_int4_add__h == NULL)
1782 | 	shmem_int4_add__h = (shmem_int4_add__p_h) dlsym(tau_handle,"shmem_int4_add_"); 
1783 |     if (shmem_int4_add__h == NULL) {
1784 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1810 |   } 
1811 |   else { 
1812 |     if (shmem_int4_and_to_all__h == NULL)
1813 | 	shmem_int4_and_to_all__h = (shmem_int4_and_to_all__p_h) dlsym(tau_handle,"shmem_int4_and_to_all_"); 
1814 |     if (shmem_int4_and_to_all__h == NULL) {
1815 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1842 |   } 
1843 |   else { 
1844 |     if (shmem_int4_cswap__h == NULL)
1845 | 	shmem_int4_cswap__h = (shmem_int4_cswap__p_h) dlsym(tau_handle,"shmem_int4_cswap_"); 
1846 |     if (shmem_int4_cswap__h == NULL) {
1847 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1881 |   } 
1882 |   else { 
1883 |     if (shmem_int4_fadd__h == NULL)
1884 | 	shmem_int4_fadd__h = (shmem_int4_fadd__p_h) dlsym(tau_handle,"shmem_int4_fadd_"); 
1885 |     if (shmem_int4_fadd__h == NULL) {
1886 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1918 |   } 
1919 |   else { 
1920 |     if (shmem_int4_finc__h == NULL)
1921 | 	shmem_int4_finc__h = (shmem_int4_finc__p_h) dlsym(tau_handle,"shmem_int4_finc_"); 
1922 |     if (shmem_int4_finc__h == NULL) {
1923 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1954 |   } 
1955 |   else { 
1956 |     if (shmem_int4_inc__h == NULL)
1957 | 	shmem_int4_inc__h = (shmem_int4_inc__p_h) dlsym(tau_handle,"shmem_int4_inc_"); 
1958 |     if (shmem_int4_inc__h == NULL) {
1959 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1985 |   } 
1986 |   else { 
1987 |     if (shmem_int4_max_to_all__h == NULL)
1988 | 	shmem_int4_max_to_all__h = (shmem_int4_max_to_all__p_h) dlsym(tau_handle,"shmem_int4_max_to_all_"); 
1989 |     if (shmem_int4_max_to_all__h == NULL) {
1990 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2016 |   } 
2017 |   else { 
2018 |     if (shmem_int4_min_to_all__h == NULL)
2019 | 	shmem_int4_min_to_all__h = (shmem_int4_min_to_all__p_h) dlsym(tau_handle,"shmem_int4_min_to_all_"); 
2020 |     if (shmem_int4_min_to_all__h == NULL) {
2021 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2047 |   } 
2048 |   else { 
2049 |     if (shmem_int4_or_to_all__h == NULL)
2050 | 	shmem_int4_or_to_all__h = (shmem_int4_or_to_all__p_h) dlsym(tau_handle,"shmem_int4_or_to_all_"); 
2051 |     if (shmem_int4_or_to_all__h == NULL) {
2052 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2078 |   } 
2079 |   else { 
2080 |     if (shmem_int4_prod_to_all__h == NULL)
2081 | 	shmem_int4_prod_to_all__h = (shmem_int4_prod_to_all__p_h) dlsym(tau_handle,"shmem_int4_prod_to_all_"); 
2082 |     if (shmem_int4_prod_to_all__h == NULL) {
2083 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2109 |   } 
2110 |   else { 
2111 |     if (shmem_int4_sum_to_all__h == NULL)
2112 | 	shmem_int4_sum_to_all__h = (shmem_int4_sum_to_all__p_h) dlsym(tau_handle,"shmem_int4_sum_to_all_"); 
2113 |     if (shmem_int4_sum_to_all__h == NULL) {
2114 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2141 |   } 
2142 |   else { 
2143 |     if (shmem_int4_swap__h == NULL)
2144 | 	shmem_int4_swap__h = (shmem_int4_swap__p_h) dlsym(tau_handle,"shmem_int4_swap_"); 
2145 |     if (shmem_int4_swap__h == NULL) {
2146 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2177 |   } 
2178 |   else { 
2179 |     if (shmem_int4_wait__h == NULL)
2180 | 	shmem_int4_wait__h = (shmem_int4_wait__p_h) dlsym(tau_handle,"shmem_int4_wait_"); 
2181 |     if (shmem_int4_wait__h == NULL) {
2182 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2208 |   } 
2209 |   else { 
2210 |     if (shmem_int4_wait_until__h == NULL)
2211 | 	shmem_int4_wait_until__h = (shmem_int4_wait_until__p_h) dlsym(tau_handle,"shmem_int4_wait_until_"); 
2212 |     if (shmem_int4_wait_until__h == NULL) {
2213 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2239 |   } 
2240 |   else { 
2241 |     if (shmem_int4_xor_to_all__h == NULL)
2242 | 	shmem_int4_xor_to_all__h = (shmem_int4_xor_to_all__p_h) dlsym(tau_handle,"shmem_int4_xor_to_all_"); 
2243 |     if (shmem_int4_xor_to_all__h == NULL) {
2244 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2270 |   } 
2271 |   else { 
2272 |     if (shmem_int8_add__h == NULL)
2273 | 	shmem_int8_add__h = (shmem_int8_add__p_h) dlsym(tau_handle,"shmem_int8_add_"); 
2274 |     if (shmem_int8_add__h == NULL) {
2275 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2301 |   } 
2302 |   else { 
2303 |     if (shmem_int8_and_to_all__h == NULL)
2304 | 	shmem_int8_and_to_all__h = (shmem_int8_and_to_all__p_h) dlsym(tau_handle,"shmem_int8_and_to_all_"); 
2305 |     if (shmem_int8_and_to_all__h == NULL) {
2306 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2333 |   } 
2334 |   else { 
2335 |     if (shmem_int8_cswap__h == NULL)
2336 | 	shmem_int8_cswap__h = (shmem_int8_cswap__p_h) dlsym(tau_handle,"shmem_int8_cswap_"); 
2337 |     if (shmem_int8_cswap__h == NULL) {
2338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2372 |   } 
2373 |   else { 
2374 |     if (shmem_int8_fadd__h == NULL)
2375 | 	shmem_int8_fadd__h = (shmem_int8_fadd__p_h) dlsym(tau_handle,"shmem_int8_fadd_"); 
2376 |     if (shmem_int8_fadd__h == NULL) {
2377 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2409 |   } 
2410 |   else { 
2411 |     if (shmem_int8_finc__h == NULL)
2412 | 	shmem_int8_finc__h = (shmem_int8_finc__p_h) dlsym(tau_handle,"shmem_int8_finc_"); 
2413 |     if (shmem_int8_finc__h == NULL) {
2414 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2445 |   } 
2446 |   else { 
2447 |     if (shmem_int8_inc__h == NULL)
2448 | 	shmem_int8_inc__h = (shmem_int8_inc__p_h) dlsym(tau_handle,"shmem_int8_inc_"); 
2449 |     if (shmem_int8_inc__h == NULL) {
2450 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2476 |   } 
2477 |   else { 
2478 |     if (shmem_int8_max_to_all__h == NULL)
2479 | 	shmem_int8_max_to_all__h = (shmem_int8_max_to_all__p_h) dlsym(tau_handle,"shmem_int8_max_to_all_"); 
2480 |     if (shmem_int8_max_to_all__h == NULL) {
2481 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2507 |   } 
2508 |   else { 
2509 |     if (shmem_int8_min_to_all__h == NULL)
2510 | 	shmem_int8_min_to_all__h = (shmem_int8_min_to_all__p_h) dlsym(tau_handle,"shmem_int8_min_to_all_"); 
2511 |     if (shmem_int8_min_to_all__h == NULL) {
2512 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2538 |   } 
2539 |   else { 
2540 |     if (shmem_int8_or_to_all__h == NULL)
2541 | 	shmem_int8_or_to_all__h = (shmem_int8_or_to_all__p_h) dlsym(tau_handle,"shmem_int8_or_to_all_"); 
2542 |     if (shmem_int8_or_to_all__h == NULL) {
2543 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2569 |   } 
2570 |   else { 
2571 |     if (shmem_int8_prod_to_all__h == NULL)
2572 | 	shmem_int8_prod_to_all__h = (shmem_int8_prod_to_all__p_h) dlsym(tau_handle,"shmem_int8_prod_to_all_"); 
2573 |     if (shmem_int8_prod_to_all__h == NULL) {
2574 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2600 |   } 
2601 |   else { 
2602 |     if (shmem_int8_sum_to_all__h == NULL)
2603 | 	shmem_int8_sum_to_all__h = (shmem_int8_sum_to_all__p_h) dlsym(tau_handle,"shmem_int8_sum_to_all_"); 
2604 |     if (shmem_int8_sum_to_all__h == NULL) {
2605 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2632 |   } 
2633 |   else { 
2634 |     if (shmem_int8_swap__h == NULL)
2635 | 	shmem_int8_swap__h = (shmem_int8_swap__p_h) dlsym(tau_handle,"shmem_int8_swap_"); 
2636 |     if (shmem_int8_swap__h == NULL) {
2637 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2668 |   } 
2669 |   else { 
2670 |     if (shmem_int8_wait__h == NULL)
2671 | 	shmem_int8_wait__h = (shmem_int8_wait__p_h) dlsym(tau_handle,"shmem_int8_wait_"); 
2672 |     if (shmem_int8_wait__h == NULL) {
2673 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2699 |   } 
2700 |   else { 
2701 |     if (shmem_int8_wait_until__h == NULL)
2702 | 	shmem_int8_wait_until__h = (shmem_int8_wait_until__p_h) dlsym(tau_handle,"shmem_int8_wait_until_"); 
2703 |     if (shmem_int8_wait_until__h == NULL) {
2704 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2730 |   } 
2731 |   else { 
2732 |     if (shmem_int8_xor_to_all__h == NULL)
2733 | 	shmem_int8_xor_to_all__h = (shmem_int8_xor_to_all__p_h) dlsym(tau_handle,"shmem_int8_xor_to_all_"); 
2734 |     if (shmem_int8_xor_to_all__h == NULL) {
2735 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2761 |   } 
2762 |   else { 
2763 |     if (shmem_integer_get__h == NULL)
2764 | 	shmem_integer_get__h = (shmem_integer_get__p_h) dlsym(tau_handle,"shmem_integer_get_"); 
2765 |     if (shmem_integer_get__h == NULL) {
2766 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2794 |   } 
2795 |   else { 
2796 |     if (shmem_integer_iget__h == NULL)
2797 | 	shmem_integer_iget__h = (shmem_integer_iget__p_h) dlsym(tau_handle,"shmem_integer_iget_"); 
2798 |     if (shmem_integer_iget__h == NULL) {
2799 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2827 |   } 
2828 |   else { 
2829 |     if (shmem_integer_iput__h == NULL)
2830 | 	shmem_integer_iput__h = (shmem_integer_iput__p_h) dlsym(tau_handle,"shmem_integer_iput_"); 
2831 |     if (shmem_integer_iput__h == NULL) {
2832 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2860 |   } 
2861 |   else { 
2862 |     if (shmem_integer_put__h == NULL)
2863 | 	shmem_integer_put__h = (shmem_integer_put__p_h) dlsym(tau_handle,"shmem_integer_put_"); 
2864 |     if (shmem_integer_put__h == NULL) {
2865 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2893 |   } 
2894 |   else { 
2895 |     if (shmem_iput128__h == NULL)
2896 | 	shmem_iput128__h = (shmem_iput128__p_h) dlsym(tau_handle,"shmem_iput128_"); 
2897 |     if (shmem_iput128__h == NULL) {
2898 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2926 |   } 
2927 |   else { 
2928 |     if (shmem_iput16__h == NULL)
2929 | 	shmem_iput16__h = (shmem_iput16__p_h) dlsym(tau_handle,"shmem_iput16_"); 
2930 |     if (shmem_iput16__h == NULL) {
2931 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2959 |   } 
2960 |   else { 
2961 |     if (shmem_iput32__h == NULL)
2962 | 	shmem_iput32__h = (shmem_iput32__p_h) dlsym(tau_handle,"shmem_iput32_"); 
2963 |     if (shmem_iput32__h == NULL) {
2964 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2992 |   } 
2993 |   else { 
2994 |     if (shmem_iput4__h == NULL)
2995 | 	shmem_iput4__h = (shmem_iput4__p_h) dlsym(tau_handle,"shmem_iput4_"); 
2996 |     if (shmem_iput4__h == NULL) {
2997 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3025 |   } 
3026 |   else { 
3027 |     if (shmem_iput64__h == NULL)
3028 | 	shmem_iput64__h = (shmem_iput64__p_h) dlsym(tau_handle,"shmem_iput64_"); 
3029 |     if (shmem_iput64__h == NULL) {
3030 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3058 |   } 
3059 |   else { 
3060 |     if (shmem_iput8__h == NULL)
3061 | 	shmem_iput8__h = (shmem_iput8__p_h) dlsym(tau_handle,"shmem_iput8_"); 
3062 |     if (shmem_iput8__h == NULL) {
3063 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3091 |   } 
3092 |   else { 
3093 |     if (shmem_logical_get__h == NULL)
3094 | 	shmem_logical_get__h = (shmem_logical_get__p_h) dlsym(tau_handle,"shmem_logical_get_"); 
3095 |     if (shmem_logical_get__h == NULL) {
3096 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3124 |   } 
3125 |   else { 
3126 |     if (shmem_logical_iget__h == NULL)
3127 | 	shmem_logical_iget__h = (shmem_logical_iget__p_h) dlsym(tau_handle,"shmem_logical_iget_"); 
3128 |     if (shmem_logical_iget__h == NULL) {
3129 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3157 |   } 
3158 |   else { 
3159 |     if (shmem_logical_iput__h == NULL)
3160 | 	shmem_logical_iput__h = (shmem_logical_iput__p_h) dlsym(tau_handle,"shmem_logical_iput_"); 
3161 |     if (shmem_logical_iput__h == NULL) {
3162 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3190 |   } 
3191 |   else { 
3192 |     if (shmem_logical_put__h == NULL)
3193 | 	shmem_logical_put__h = (shmem_logical_put__p_h) dlsym(tau_handle,"shmem_logical_put_"); 
3194 |     if (shmem_logical_put__h == NULL) {
3195 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3224 |   } 
3225 |   else { 
3226 |     if (shmem_my_pe__h == NULL)
3227 | 	shmem_my_pe__h = (shmem_my_pe__p_h) dlsym(tau_handle,"shmem_my_pe_"); 
3228 |     if (shmem_my_pe__h == NULL) {
3229 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3257 |   } 
3258 |   else { 
3259 |     if (shmem_n_pes__h == NULL)
3260 | 	shmem_n_pes__h = (shmem_n_pes__p_h) dlsym(tau_handle,"shmem_n_pes_"); 
3261 |     if (shmem_n_pes__h == NULL) {
3262 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3290 |   } 
3291 |   else { 
3292 |     if (shmem_pe_accessible__h == NULL)
3293 | 	shmem_pe_accessible__h = (shmem_pe_accessible__p_h) dlsym(tau_handle,"shmem_pe_accessible_"); 
3294 |     if (shmem_pe_accessible__h == NULL) {
3295 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3322 |   } 
3323 |   else { 
3324 |     if (shmem_ptr__h == NULL)
3325 | 	shmem_ptr__h = (shmem_ptr__p_h) dlsym(tau_handle,"shmem_ptr_"); 
3326 |     if (shmem_ptr__h == NULL) {
3327 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3353 |   } 
3354 |   else { 
3355 |     if (shmem_put128__h == NULL)
3356 | 	shmem_put128__h = (shmem_put128__p_h) dlsym(tau_handle,"shmem_put128_"); 
3357 |     if (shmem_put128__h == NULL) {
3358 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3386 |   } 
3387 |   else { 
3388 |     if (shmem_put16__h == NULL)
3389 | 	shmem_put16__h = (shmem_put16__p_h) dlsym(tau_handle,"shmem_put16_"); 
3390 |     if (shmem_put16__h == NULL) {
3391 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3419 |   } 
3420 |   else { 
3421 |     if (shmem_put32__h == NULL)
3422 | 	shmem_put32__h = (shmem_put32__p_h) dlsym(tau_handle,"shmem_put32_"); 
3423 |     if (shmem_put32__h == NULL) {
3424 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3452 |   } 
3453 |   else { 
3454 |     if (shmem_put4__h == NULL)
3455 | 	shmem_put4__h = (shmem_put4__p_h) dlsym(tau_handle,"shmem_put4_"); 
3456 |     if (shmem_put4__h == NULL) {
3457 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3485 |   } 
3486 |   else { 
3487 |     if (shmem_put64__h == NULL)
3488 | 	shmem_put64__h = (shmem_put64__p_h) dlsym(tau_handle,"shmem_put64_"); 
3489 |     if (shmem_put64__h == NULL) {
3490 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3518 |   } 
3519 |   else { 
3520 |     if (shmem_put8__h == NULL)
3521 | 	shmem_put8__h = (shmem_put8__p_h) dlsym(tau_handle,"shmem_put8_"); 
3522 |     if (shmem_put8__h == NULL) {
3523 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3551 |   } 
3552 |   else { 
3553 |     if (shmem_putmem__h == NULL)
3554 | 	shmem_putmem__h = (shmem_putmem__p_h) dlsym(tau_handle,"shmem_putmem_"); 
3555 |     if (shmem_putmem__h == NULL) {
3556 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3584 |   } 
3585 |   else { 
3586 |     if (shmem_quiet__h == NULL)
3587 | 	shmem_quiet__h = (shmem_quiet__p_h) dlsym(tau_handle,"shmem_quiet_"); 
3588 |     if (shmem_quiet__h == NULL) {
3589 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3615 |   } 
3616 |   else { 
3617 |     if (shmem_real16_max_to_all__h == NULL)
3618 | 	shmem_real16_max_to_all__h = (shmem_real16_max_to_all__p_h) dlsym(tau_handle,"shmem_real16_max_to_all_"); 
3619 |     if (shmem_real16_max_to_all__h == NULL) {
3620 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3646 |   } 
3647 |   else { 
3648 |     if (shmem_real16_min_to_all__h == NULL)
3649 | 	shmem_real16_min_to_all__h = (shmem_real16_min_to_all__p_h) dlsym(tau_handle,"shmem_real16_min_to_all_"); 
3650 |     if (shmem_real16_min_to_all__h == NULL) {
3651 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3677 |   } 
3678 |   else { 
3679 |     if (shmem_real16_prod_to_all__h == NULL)
3680 | 	shmem_real16_prod_to_all__h = (shmem_real16_prod_to_all__p_h) dlsym(tau_handle,"shmem_real16_prod_to_all_"); 
3681 |     if (shmem_real16_prod_to_all__h == NULL) {
3682 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3708 |   } 
3709 |   else { 
3710 |     if (shmem_real16_sum_to_all__h == NULL)
3711 | 	shmem_real16_sum_to_all__h = (shmem_real16_sum_to_all__p_h) dlsym(tau_handle,"shmem_real16_sum_to_all_"); 
3712 |     if (shmem_real16_sum_to_all__h == NULL) {
3713 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3739 |   } 
3740 |   else { 
3741 |     if (shmem_real4_max_to_all__h == NULL)
3742 | 	shmem_real4_max_to_all__h = (shmem_real4_max_to_all__p_h) dlsym(tau_handle,"shmem_real4_max_to_all_"); 
3743 |     if (shmem_real4_max_to_all__h == NULL) {
3744 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3770 |   } 
3771 |   else { 
3772 |     if (shmem_real4_min_to_all__h == NULL)
3773 | 	shmem_real4_min_to_all__h = (shmem_real4_min_to_all__p_h) dlsym(tau_handle,"shmem_real4_min_to_all_"); 
3774 |     if (shmem_real4_min_to_all__h == NULL) {
3775 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3801 |   } 
3802 |   else { 
3803 |     if (shmem_real4_prod_to_all__h == NULL)
3804 | 	shmem_real4_prod_to_all__h = (shmem_real4_prod_to_all__p_h) dlsym(tau_handle,"shmem_real4_prod_to_all_"); 
3805 |     if (shmem_real4_prod_to_all__h == NULL) {
3806 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3832 |   } 
3833 |   else { 
3834 |     if (shmem_real4_sum_to_all__h == NULL)
3835 | 	shmem_real4_sum_to_all__h = (shmem_real4_sum_to_all__p_h) dlsym(tau_handle,"shmem_real4_sum_to_all_"); 
3836 |     if (shmem_real4_sum_to_all__h == NULL) {
3837 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3864 |   } 
3865 |   else { 
3866 |     if (shmem_real4_swap__h == NULL)
3867 | 	shmem_real4_swap__h = (shmem_real4_swap__p_h) dlsym(tau_handle,"shmem_real4_swap_"); 
3868 |     if (shmem_real4_swap__h == NULL) {
3869 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3900 |   } 
3901 |   else { 
3902 |     if (shmem_real8_max_to_all__h == NULL)
3903 | 	shmem_real8_max_to_all__h = (shmem_real8_max_to_all__p_h) dlsym(tau_handle,"shmem_real8_max_to_all_"); 
3904 |     if (shmem_real8_max_to_all__h == NULL) {
3905 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3931 |   } 
3932 |   else { 
3933 |     if (shmem_real8_min_to_all__h == NULL)
3934 | 	shmem_real8_min_to_all__h = (shmem_real8_min_to_all__p_h) dlsym(tau_handle,"shmem_real8_min_to_all_"); 
3935 |     if (shmem_real8_min_to_all__h == NULL) {
3936 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3962 |   } 
3963 |   else { 
3964 |     if (shmem_real8_prod_to_all__h == NULL)
3965 | 	shmem_real8_prod_to_all__h = (shmem_real8_prod_to_all__p_h) dlsym(tau_handle,"shmem_real8_prod_to_all_"); 
3966 |     if (shmem_real8_prod_to_all__h == NULL) {
3967 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3993 |   } 
3994 |   else { 
3995 |     if (shmem_real8_sum_to_all__h == NULL)
3996 | 	shmem_real8_sum_to_all__h = (shmem_real8_sum_to_all__p_h) dlsym(tau_handle,"shmem_real8_sum_to_all_"); 
3997 |     if (shmem_real8_sum_to_all__h == NULL) {
3998 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4025 |   } 
4026 |   else { 
4027 |     if (shmem_real8_swap__h == NULL)
4028 | 	shmem_real8_swap__h = (shmem_real8_swap__p_h) dlsym(tau_handle,"shmem_real8_swap_"); 
4029 |     if (shmem_real8_swap__h == NULL) {
4030 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4061 |   } 
4062 |   else { 
4063 |     if (shmem_real_get__h == NULL)
4064 | 	shmem_real_get__h = (shmem_real_get__p_h) dlsym(tau_handle,"shmem_real_get_"); 
4065 |     if (shmem_real_get__h == NULL) {
4066 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4094 |   } 
4095 |   else { 
4096 |     if (shmem_real_iget__h == NULL)
4097 | 	shmem_real_iget__h = (shmem_real_iget__p_h) dlsym(tau_handle,"shmem_real_iget_"); 
4098 |     if (shmem_real_iget__h == NULL) {
4099 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4127 |   } 
4128 |   else { 
4129 |     if (shmem_real_iput__h == NULL)
4130 | 	shmem_real_iput__h = (shmem_real_iput__p_h) dlsym(tau_handle,"shmem_real_iput_"); 
4131 |     if (shmem_real_iput__h == NULL) {
4132 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4160 |   } 
4161 |   else { 
4162 |     if (shmem_real_put__h == NULL)
4163 | 	shmem_real_put__h = (shmem_real_put__p_h) dlsym(tau_handle,"shmem_real_put_"); 
4164 |     if (shmem_real_put__h == NULL) {
4165 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4193 |   } 
4194 |   else { 
4195 |     if (shmem_set_cache_inv__h == NULL)
4196 | 	shmem_set_cache_inv__h = (shmem_set_cache_inv__p_h) dlsym(tau_handle,"shmem_set_cache_inv_"); 
4197 |     if (shmem_set_cache_inv__h == NULL) {
4198 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4224 |   } 
4225 |   else { 
4226 |     if (shmem_set_cache_line_inv__h == NULL)
4227 | 	shmem_set_cache_line_inv__h = (shmem_set_cache_line_inv__p_h) dlsym(tau_handle,"shmem_set_cache_line_inv_"); 
4228 |     if (shmem_set_cache_line_inv__h == NULL) {
4229 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4255 |   } 
4256 |   else { 
4257 |     if (shmem_set_lock__h == NULL)
4258 | 	shmem_set_lock__h = (shmem_set_lock__p_h) dlsym(tau_handle,"shmem_set_lock_"); 
4259 |     if (shmem_set_lock__h == NULL) {
4260 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4287 |   } 
4288 |   else { 
4289 |     if (shmem_swap__h == NULL)
4290 | 	shmem_swap__h = (shmem_swap__p_h) dlsym(tau_handle,"shmem_swap_"); 
4291 |     if (shmem_swap__h == NULL) {
4292 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4324 |   } 
4325 |   else { 
4326 |     if (shmem_test_lock__h == NULL)
4327 | 	shmem_test_lock__h = (shmem_test_lock__p_h) dlsym(tau_handle,"shmem_test_lock_"); 
4328 |     if (shmem_test_lock__h == NULL) {
4329 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4356 |   } 
4357 |   else { 
4358 |     if (shmem_udcflush__h == NULL)
4359 | 	shmem_udcflush__h = (shmem_udcflush__p_h) dlsym(tau_handle,"shmem_udcflush_"); 
4360 |     if (shmem_udcflush__h == NULL) {
4361 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4387 |   } 
4388 |   else { 
4389 |     if (shmem_udcflush_line__h == NULL)
4390 | 	shmem_udcflush_line__h = (shmem_udcflush_line__p_h) dlsym(tau_handle,"shmem_udcflush_line_"); 
4391 |     if (shmem_udcflush_line__h == NULL) {
4392 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4418 |   } 
4419 |   else { 
4420 |     if (shmem_wait__h == NULL)
4421 | 	shmem_wait__h = (shmem_wait__p_h) dlsym(tau_handle,"shmem_wait_"); 
4422 |     if (shmem_wait__h == NULL) {
4423 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4449 |   } 
4450 |   else { 
4451 |     if (shmem_wait_until__h == NULL)
4452 | 	shmem_wait_until__h = (shmem_wait_until__p_h) dlsym(tau_handle,"shmem_wait_until_"); 
4453 |     if (shmem_wait_until__h == NULL) {
4454 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4480 |   } 
4481 |   else { 
4482 |     if (start_pes__h == NULL)
4483 | 	start_pes__h = (start_pes__p_h) dlsym(tau_handle,"start_pes_"); 
4484 |     if (start_pes__h == NULL) {
4485 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4520 |   } 
4521 |   else { 
4522 |     if (shmem_addr_accessible___h == NULL)
4523 | 	shmem_addr_accessible___h = (shmem_addr_accessible___p_h) dlsym(tau_handle,"shmem_addr_accessible__"); 
4524 |     if (shmem_addr_accessible___h == NULL) {
4525 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4551 |   } 
4552 |   else { 
4553 |     if (shmem_barrier___h == NULL)
4554 | 	shmem_barrier___h = (shmem_barrier___p_h) dlsym(tau_handle,"shmem_barrier__"); 
4555 |     if (shmem_barrier___h == NULL) {
4556 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4582 |   } 
4583 |   else { 
4584 |     if (shmem_barrier_all___h == NULL)
4585 | 	shmem_barrier_all___h = (shmem_barrier_all___p_h) dlsym(tau_handle,"shmem_barrier_all__"); 
4586 |     if (shmem_barrier_all___h == NULL) {
4587 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4613 |   } 
4614 |   else { 
4615 |     if (shmem_barrier_ps___h == NULL)
4616 | 	shmem_barrier_ps___h = (shmem_barrier_ps___p_h) dlsym(tau_handle,"shmem_barrier_ps__"); 
4617 |     if (shmem_barrier_ps___h == NULL) {
4618 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4644 |   } 
4645 |   else { 
4646 |     if (shmem_broadcast32___h == NULL)
4647 | 	shmem_broadcast32___h = (shmem_broadcast32___p_h) dlsym(tau_handle,"shmem_broadcast32__"); 
4648 |     if (shmem_broadcast32___h == NULL) {
4649 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4675 |   } 
4676 |   else { 
4677 |     if (shmem_broadcast4___h == NULL)
4678 | 	shmem_broadcast4___h = (shmem_broadcast4___p_h) dlsym(tau_handle,"shmem_broadcast4__"); 
4679 |     if (shmem_broadcast4___h == NULL) {
4680 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4706 |   } 
4707 |   else { 
4708 |     if (shmem_broadcast64___h == NULL)
4709 | 	shmem_broadcast64___h = (shmem_broadcast64___p_h) dlsym(tau_handle,"shmem_broadcast64__"); 
4710 |     if (shmem_broadcast64___h == NULL) {
4711 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4737 |   } 
4738 |   else { 
4739 |     if (shmem_broadcast8___h == NULL)
4740 | 	shmem_broadcast8___h = (shmem_broadcast8___p_h) dlsym(tau_handle,"shmem_broadcast8__"); 
4741 |     if (shmem_broadcast8___h == NULL) {
4742 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4768 |   } 
4769 |   else { 
4770 |     if (shmem_character_get___h == NULL)
4771 | 	shmem_character_get___h = (shmem_character_get___p_h) dlsym(tau_handle,"shmem_character_get__"); 
4772 |     if (shmem_character_get___h == NULL) {
4773 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4801 |   } 
4802 |   else { 
4803 |     if (shmem_character_put___h == NULL)
4804 | 	shmem_character_put___h = (shmem_character_put___p_h) dlsym(tau_handle,"shmem_character_put__"); 
4805 |     if (shmem_character_put___h == NULL) {
4806 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4834 |   } 
4835 |   else { 
4836 |     if (shmem_clear_cache_inv___h == NULL)
4837 | 	shmem_clear_cache_inv___h = (shmem_clear_cache_inv___p_h) dlsym(tau_handle,"shmem_clear_cache_inv__"); 
4838 |     if (shmem_clear_cache_inv___h == NULL) {
4839 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4865 |   } 
4866 |   else { 
4867 |     if (shmem_clear_cache_line_inv___h == NULL)
4868 | 	shmem_clear_cache_line_inv___h = (shmem_clear_cache_line_inv___p_h) dlsym(tau_handle,"shmem_clear_cache_line_inv__"); 
4869 |     if (shmem_clear_cache_line_inv___h == NULL) {
4870 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4896 |   } 
4897 |   else { 
4898 |     if (shmem_clear_lock___h == NULL)
4899 | 	shmem_clear_lock___h = (shmem_clear_lock___p_h) dlsym(tau_handle,"shmem_clear_lock__"); 
4900 |     if (shmem_clear_lock___h == NULL) {
4901 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4927 |   } 
4928 |   else { 
4929 |     if (shmem_collect4___h == NULL)
4930 | 	shmem_collect4___h = (shmem_collect4___p_h) dlsym(tau_handle,"shmem_collect4__"); 
4931 |     if (shmem_collect4___h == NULL) {
4932 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4958 |   } 
4959 |   else { 
4960 |     if (shmem_collect64___h == NULL)
4961 | 	shmem_collect64___h = (shmem_collect64___p_h) dlsym(tau_handle,"shmem_collect64__"); 
4962 |     if (shmem_collect64___h == NULL) {
4963 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4989 |   } 
4990 |   else { 
4991 |     if (shmem_collect8___h == NULL)
4992 | 	shmem_collect8___h = (shmem_collect8___p_h) dlsym(tau_handle,"shmem_collect8__"); 
4993 |     if (shmem_collect8___h == NULL) {
4994 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5020 |   } 
5021 |   else { 
5022 |     if (shmem_comp4_prod_to_all___h == NULL)
5023 | 	shmem_comp4_prod_to_all___h = (shmem_comp4_prod_to_all___p_h) dlsym(tau_handle,"shmem_comp4_prod_to_all__"); 
5024 |     if (shmem_comp4_prod_to_all___h == NULL) {
5025 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5051 |   } 
5052 |   else { 
5053 |     if (shmem_comp4_sum_to_all___h == NULL)
5054 | 	shmem_comp4_sum_to_all___h = (shmem_comp4_sum_to_all___p_h) dlsym(tau_handle,"shmem_comp4_sum_to_all__"); 
5055 |     if (shmem_comp4_sum_to_all___h == NULL) {
5056 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5082 |   } 
5083 |   else { 
5084 |     if (shmem_comp8_prod_to_all___h == NULL)
5085 | 	shmem_comp8_prod_to_all___h = (shmem_comp8_prod_to_all___p_h) dlsym(tau_handle,"shmem_comp8_prod_to_all__"); 
5086 |     if (shmem_comp8_prod_to_all___h == NULL) {
5087 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5113 |   } 
5114 |   else { 
5115 |     if (shmem_comp8_sum_to_all___h == NULL)
5116 | 	shmem_comp8_sum_to_all___h = (shmem_comp8_sum_to_all___p_h) dlsym(tau_handle,"shmem_comp8_sum_to_all__"); 
5117 |     if (shmem_comp8_sum_to_all___h == NULL) {
5118 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5144 |   } 
5145 |   else { 
5146 |     if (shmem_complex_get___h == NULL)
5147 | 	shmem_complex_get___h = (shmem_complex_get___p_h) dlsym(tau_handle,"shmem_complex_get__"); 
5148 |     if (shmem_complex_get___h == NULL) {
5149 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5177 |   } 
5178 |   else { 
5179 |     if (shmem_complex_iget___h == NULL)
5180 | 	shmem_complex_iget___h = (shmem_complex_iget___p_h) dlsym(tau_handle,"shmem_complex_iget__"); 
5181 |     if (shmem_complex_iget___h == NULL) {
5182 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5210 |   } 
5211 |   else { 
5212 |     if (shmem_complex_iput___h == NULL)
5213 | 	shmem_complex_iput___h = (shmem_complex_iput___p_h) dlsym(tau_handle,"shmem_complex_iput__"); 
5214 |     if (shmem_complex_iput___h == NULL) {
5215 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5243 |   } 
5244 |   else { 
5245 |     if (shmem_complex_put___h == NULL)
5246 | 	shmem_complex_put___h = (shmem_complex_put___p_h) dlsym(tau_handle,"shmem_complex_put__"); 
5247 |     if (shmem_complex_put___h == NULL) {
5248 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5276 |   } 
5277 |   else { 
5278 |     if (shmem_double_get___h == NULL)
5279 | 	shmem_double_get___h = (shmem_double_get___p_h) dlsym(tau_handle,"shmem_double_get__"); 
5280 |     if (shmem_double_get___h == NULL) {
5281 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5309 |   } 
5310 |   else { 
5311 |     if (shmem_double_iget___h == NULL)
5312 | 	shmem_double_iget___h = (shmem_double_iget___p_h) dlsym(tau_handle,"shmem_double_iget__"); 
5313 |     if (shmem_double_iget___h == NULL) {
5314 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5342 |   } 
5343 |   else { 
5344 |     if (shmem_double_iput___h == NULL)
5345 | 	shmem_double_iput___h = (shmem_double_iput___p_h) dlsym(tau_handle,"shmem_double_iput__"); 
5346 |     if (shmem_double_iput___h == NULL) {
5347 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5375 |   } 
5376 |   else { 
5377 |     if (shmem_double_put___h == NULL)
5378 | 	shmem_double_put___h = (shmem_double_put___p_h) dlsym(tau_handle,"shmem_double_put__"); 
5379 |     if (shmem_double_put___h == NULL) {
5380 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5408 |   } 
5409 |   else { 
5410 |     if (shmem_fcollect32___h == NULL)
5411 | 	shmem_fcollect32___h = (shmem_fcollect32___p_h) dlsym(tau_handle,"shmem_fcollect32__"); 
5412 |     if (shmem_fcollect32___h == NULL) {
5413 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5439 |   } 
5440 |   else { 
5441 |     if (shmem_fcollect4___h == NULL)
5442 | 	shmem_fcollect4___h = (shmem_fcollect4___p_h) dlsym(tau_handle,"shmem_fcollect4__"); 
5443 |     if (shmem_fcollect4___h == NULL) {
5444 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5470 |   } 
5471 |   else { 
5472 |     if (shmem_fcollect64___h == NULL)
5473 | 	shmem_fcollect64___h = (shmem_fcollect64___p_h) dlsym(tau_handle,"shmem_fcollect64__"); 
5474 |     if (shmem_fcollect64___h == NULL) {
5475 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5501 |   } 
5502 |   else { 
5503 |     if (shmem_fcollect8___h == NULL)
5504 | 	shmem_fcollect8___h = (shmem_fcollect8___p_h) dlsym(tau_handle,"shmem_fcollect8__"); 
5505 |     if (shmem_fcollect8___h == NULL) {
5506 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5532 |   } 
5533 |   else { 
5534 |     if (shmem_fence___h == NULL)
5535 | 	shmem_fence___h = (shmem_fence___p_h) dlsym(tau_handle,"shmem_fence__"); 
5536 |     if (shmem_fence___h == NULL) {
5537 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5563 |   } 
5564 |   else { 
5565 |     if (shmem_get128___h == NULL)
5566 | 	shmem_get128___h = (shmem_get128___p_h) dlsym(tau_handle,"shmem_get128__"); 
5567 |     if (shmem_get128___h == NULL) {
5568 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5596 |   } 
5597 |   else { 
5598 |     if (shmem_get16___h == NULL)
5599 | 	shmem_get16___h = (shmem_get16___p_h) dlsym(tau_handle,"shmem_get16__"); 
5600 |     if (shmem_get16___h == NULL) {
5601 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5629 |   } 
5630 |   else { 
5631 |     if (shmem_get32___h == NULL)
5632 | 	shmem_get32___h = (shmem_get32___p_h) dlsym(tau_handle,"shmem_get32__"); 
5633 |     if (shmem_get32___h == NULL) {
5634 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5662 |   } 
5663 |   else { 
5664 |     if (shmem_get4___h == NULL)
5665 | 	shmem_get4___h = (shmem_get4___p_h) dlsym(tau_handle,"shmem_get4__"); 
5666 |     if (shmem_get4___h == NULL) {
5667 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5695 |   } 
5696 |   else { 
5697 |     if (shmem_get64___h == NULL)
5698 | 	shmem_get64___h = (shmem_get64___p_h) dlsym(tau_handle,"shmem_get64__"); 
5699 |     if (shmem_get64___h == NULL) {
5700 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5728 |   } 
5729 |   else { 
5730 |     if (shmem_get8___h == NULL)
5731 | 	shmem_get8___h = (shmem_get8___p_h) dlsym(tau_handle,"shmem_get8__"); 
5732 |     if (shmem_get8___h == NULL) {
5733 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5761 |   } 
5762 |   else { 
5763 |     if (shmem_getmem___h == NULL)
5764 | 	shmem_getmem___h = (shmem_getmem___p_h) dlsym(tau_handle,"shmem_getmem__"); 
5765 |     if (shmem_getmem___h == NULL) {
5766 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5794 |   } 
5795 |   else { 
5796 |     if (shmem_group_create_strided___h == NULL)
5797 | 	shmem_group_create_strided___h = (shmem_group_create_strided___p_h) dlsym(tau_handle,"shmem_group_create_strided__"); 
5798 |     if (shmem_group_create_strided___h == NULL) {
5799 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5825 |   } 
5826 |   else { 
5827 |     if (shmem_group_delete___h == NULL)
5828 | 	shmem_group_delete___h = (shmem_group_delete___p_h) dlsym(tau_handle,"shmem_group_delete__"); 
5829 |     if (shmem_group_delete___h == NULL) {
5830 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5856 |   } 
5857 |   else { 
5858 |     if (shmem_iget128___h == NULL)
5859 | 	shmem_iget128___h = (shmem_iget128___p_h) dlsym(tau_handle,"shmem_iget128__"); 
5860 |     if (shmem_iget128___h == NULL) {
5861 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5889 |   } 
5890 |   else { 
5891 |     if (shmem_iget16___h == NULL)
5892 | 	shmem_iget16___h = (shmem_iget16___p_h) dlsym(tau_handle,"shmem_iget16__"); 
5893 |     if (shmem_iget16___h == NULL) {
5894 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5922 |   } 
5923 |   else { 
5924 |     if (shmem_iget32___h == NULL)
5925 | 	shmem_iget32___h = (shmem_iget32___p_h) dlsym(tau_handle,"shmem_iget32__"); 
5926 |     if (shmem_iget32___h == NULL) {
5927 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5955 |   } 
5956 |   else { 
5957 |     if (shmem_iget4___h == NULL)
5958 | 	shmem_iget4___h = (shmem_iget4___p_h) dlsym(tau_handle,"shmem_iget4__"); 
5959 |     if (shmem_iget4___h == NULL) {
5960 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5988 |   } 
5989 |   else { 
5990 |     if (shmem_iget64___h == NULL)
5991 | 	shmem_iget64___h = (shmem_iget64___p_h) dlsym(tau_handle,"shmem_iget64__"); 
5992 |     if (shmem_iget64___h == NULL) {
5993 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6021 |   } 
6022 |   else { 
6023 |     if (shmem_iget8___h == NULL)
6024 | 	shmem_iget8___h = (shmem_iget8___p_h) dlsym(tau_handle,"shmem_iget8__"); 
6025 |     if (shmem_iget8___h == NULL) {
6026 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6054 |   } 
6055 |   else { 
6056 |     if (shmem_int2_and_to_all___h == NULL)
6057 | 	shmem_int2_and_to_all___h = (shmem_int2_and_to_all___p_h) dlsym(tau_handle,"shmem_int2_and_to_all__"); 
6058 |     if (shmem_int2_and_to_all___h == NULL) {
6059 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6085 |   } 
6086 |   else { 
6087 |     if (shmem_int2_max_to_all___h == NULL)
6088 | 	shmem_int2_max_to_all___h = (shmem_int2_max_to_all___p_h) dlsym(tau_handle,"shmem_int2_max_to_all__"); 
6089 |     if (shmem_int2_max_to_all___h == NULL) {
6090 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6116 |   } 
6117 |   else { 
6118 |     if (shmem_int2_min_to_all___h == NULL)
6119 | 	shmem_int2_min_to_all___h = (shmem_int2_min_to_all___p_h) dlsym(tau_handle,"shmem_int2_min_to_all__"); 
6120 |     if (shmem_int2_min_to_all___h == NULL) {
6121 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6147 |   } 
6148 |   else { 
6149 |     if (shmem_int2_or_to_all___h == NULL)
6150 | 	shmem_int2_or_to_all___h = (shmem_int2_or_to_all___p_h) dlsym(tau_handle,"shmem_int2_or_to_all__"); 
6151 |     if (shmem_int2_or_to_all___h == NULL) {
6152 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6178 |   } 
6179 |   else { 
6180 |     if (shmem_int2_prod_to_all___h == NULL)
6181 | 	shmem_int2_prod_to_all___h = (shmem_int2_prod_to_all___p_h) dlsym(tau_handle,"shmem_int2_prod_to_all__"); 
6182 |     if (shmem_int2_prod_to_all___h == NULL) {
6183 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6209 |   } 
6210 |   else { 
6211 |     if (shmem_int2_sum_to_all___h == NULL)
6212 | 	shmem_int2_sum_to_all___h = (shmem_int2_sum_to_all___p_h) dlsym(tau_handle,"shmem_int2_sum_to_all__"); 
6213 |     if (shmem_int2_sum_to_all___h == NULL) {
6214 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6240 |   } 
6241 |   else { 
6242 |     if (shmem_int2_xor_to_all___h == NULL)
6243 | 	shmem_int2_xor_to_all___h = (shmem_int2_xor_to_all___p_h) dlsym(tau_handle,"shmem_int2_xor_to_all__"); 
6244 |     if (shmem_int2_xor_to_all___h == NULL) {
6245 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6271 |   } 
6272 |   else { 
6273 |     if (shmem_int4_add___h == NULL)
6274 | 	shmem_int4_add___h = (shmem_int4_add___p_h) dlsym(tau_handle,"shmem_int4_add__"); 
6275 |     if (shmem_int4_add___h == NULL) {
6276 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6302 |   } 
6303 |   else { 
6304 |     if (shmem_int4_and_to_all___h == NULL)
6305 | 	shmem_int4_and_to_all___h = (shmem_int4_and_to_all___p_h) dlsym(tau_handle,"shmem_int4_and_to_all__"); 
6306 |     if (shmem_int4_and_to_all___h == NULL) {
6307 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6334 |   } 
6335 |   else { 
6336 |     if (shmem_int4_cswap___h == NULL)
6337 | 	shmem_int4_cswap___h = (shmem_int4_cswap___p_h) dlsym(tau_handle,"shmem_int4_cswap__"); 
6338 |     if (shmem_int4_cswap___h == NULL) {
6339 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6373 |   } 
6374 |   else { 
6375 |     if (shmem_int4_fadd___h == NULL)
6376 | 	shmem_int4_fadd___h = (shmem_int4_fadd___p_h) dlsym(tau_handle,"shmem_int4_fadd__"); 
6377 |     if (shmem_int4_fadd___h == NULL) {
6378 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6410 |   } 
6411 |   else { 
6412 |     if (shmem_int4_finc___h == NULL)
6413 | 	shmem_int4_finc___h = (shmem_int4_finc___p_h) dlsym(tau_handle,"shmem_int4_finc__"); 
6414 |     if (shmem_int4_finc___h == NULL) {
6415 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6446 |   } 
6447 |   else { 
6448 |     if (shmem_int4_inc___h == NULL)
6449 | 	shmem_int4_inc___h = (shmem_int4_inc___p_h) dlsym(tau_handle,"shmem_int4_inc__"); 
6450 |     if (shmem_int4_inc___h == NULL) {
6451 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6477 |   } 
6478 |   else { 
6479 |     if (shmem_int4_max_to_all___h == NULL)
6480 | 	shmem_int4_max_to_all___h = (shmem_int4_max_to_all___p_h) dlsym(tau_handle,"shmem_int4_max_to_all__"); 
6481 |     if (shmem_int4_max_to_all___h == NULL) {
6482 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6508 |   } 
6509 |   else { 
6510 |     if (shmem_int4_min_to_all___h == NULL)
6511 | 	shmem_int4_min_to_all___h = (shmem_int4_min_to_all___p_h) dlsym(tau_handle,"shmem_int4_min_to_all__"); 
6512 |     if (shmem_int4_min_to_all___h == NULL) {
6513 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6539 |   } 
6540 |   else { 
6541 |     if (shmem_int4_or_to_all___h == NULL)
6542 | 	shmem_int4_or_to_all___h = (shmem_int4_or_to_all___p_h) dlsym(tau_handle,"shmem_int4_or_to_all__"); 
6543 |     if (shmem_int4_or_to_all___h == NULL) {
6544 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6570 |   } 
6571 |   else { 
6572 |     if (shmem_int4_prod_to_all___h == NULL)
6573 | 	shmem_int4_prod_to_all___h = (shmem_int4_prod_to_all___p_h) dlsym(tau_handle,"shmem_int4_prod_to_all__"); 
6574 |     if (shmem_int4_prod_to_all___h == NULL) {
6575 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6601 |   } 
6602 |   else { 
6603 |     if (shmem_int4_sum_to_all___h == NULL)
6604 | 	shmem_int4_sum_to_all___h = (shmem_int4_sum_to_all___p_h) dlsym(tau_handle,"shmem_int4_sum_to_all__"); 
6605 |     if (shmem_int4_sum_to_all___h == NULL) {
6606 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6633 |   } 
6634 |   else { 
6635 |     if (shmem_int4_swap___h == NULL)
6636 | 	shmem_int4_swap___h = (shmem_int4_swap___p_h) dlsym(tau_handle,"shmem_int4_swap__"); 
6637 |     if (shmem_int4_swap___h == NULL) {
6638 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6669 |   } 
6670 |   else { 
6671 |     if (shmem_int4_wait___h == NULL)
6672 | 	shmem_int4_wait___h = (shmem_int4_wait___p_h) dlsym(tau_handle,"shmem_int4_wait__"); 
6673 |     if (shmem_int4_wait___h == NULL) {
6674 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6700 |   } 
6701 |   else { 
6702 |     if (shmem_int4_wait_until___h == NULL)
6703 | 	shmem_int4_wait_until___h = (shmem_int4_wait_until___p_h) dlsym(tau_handle,"shmem_int4_wait_until__"); 
6704 |     if (shmem_int4_wait_until___h == NULL) {
6705 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6731 |   } 
6732 |   else { 
6733 |     if (shmem_int4_xor_to_all___h == NULL)
6734 | 	shmem_int4_xor_to_all___h = (shmem_int4_xor_to_all___p_h) dlsym(tau_handle,"shmem_int4_xor_to_all__"); 
6735 |     if (shmem_int4_xor_to_all___h == NULL) {
6736 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6762 |   } 
6763 |   else { 
6764 |     if (shmem_int8_add___h == NULL)
6765 | 	shmem_int8_add___h = (shmem_int8_add___p_h) dlsym(tau_handle,"shmem_int8_add__"); 
6766 |     if (shmem_int8_add___h == NULL) {
6767 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6793 |   } 
6794 |   else { 
6795 |     if (shmem_int8_and_to_all___h == NULL)
6796 | 	shmem_int8_and_to_all___h = (shmem_int8_and_to_all___p_h) dlsym(tau_handle,"shmem_int8_and_to_all__"); 
6797 |     if (shmem_int8_and_to_all___h == NULL) {
6798 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6825 |   } 
6826 |   else { 
6827 |     if (shmem_int8_cswap___h == NULL)
6828 | 	shmem_int8_cswap___h = (shmem_int8_cswap___p_h) dlsym(tau_handle,"shmem_int8_cswap__"); 
6829 |     if (shmem_int8_cswap___h == NULL) {
6830 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6864 |   } 
6865 |   else { 
6866 |     if (shmem_int8_fadd___h == NULL)
6867 | 	shmem_int8_fadd___h = (shmem_int8_fadd___p_h) dlsym(tau_handle,"shmem_int8_fadd__"); 
6868 |     if (shmem_int8_fadd___h == NULL) {
6869 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6901 |   } 
6902 |   else { 
6903 |     if (shmem_int8_finc___h == NULL)
6904 | 	shmem_int8_finc___h = (shmem_int8_finc___p_h) dlsym(tau_handle,"shmem_int8_finc__"); 
6905 |     if (shmem_int8_finc___h == NULL) {
6906 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6937 |   } 
6938 |   else { 
6939 |     if (shmem_int8_inc___h == NULL)
6940 | 	shmem_int8_inc___h = (shmem_int8_inc___p_h) dlsym(tau_handle,"shmem_int8_inc__"); 
6941 |     if (shmem_int8_inc___h == NULL) {
6942 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6968 |   } 
6969 |   else { 
6970 |     if (shmem_int8_max_to_all___h == NULL)
6971 | 	shmem_int8_max_to_all___h = (shmem_int8_max_to_all___p_h) dlsym(tau_handle,"shmem_int8_max_to_all__"); 
6972 |     if (shmem_int8_max_to_all___h == NULL) {
6973 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6999 |   } 
7000 |   else { 
7001 |     if (shmem_int8_min_to_all___h == NULL)
7002 | 	shmem_int8_min_to_all___h = (shmem_int8_min_to_all___p_h) dlsym(tau_handle,"shmem_int8_min_to_all__"); 
7003 |     if (shmem_int8_min_to_all___h == NULL) {
7004 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7030 |   } 
7031 |   else { 
7032 |     if (shmem_int8_or_to_all___h == NULL)
7033 | 	shmem_int8_or_to_all___h = (shmem_int8_or_to_all___p_h) dlsym(tau_handle,"shmem_int8_or_to_all__"); 
7034 |     if (shmem_int8_or_to_all___h == NULL) {
7035 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7061 |   } 
7062 |   else { 
7063 |     if (shmem_int8_prod_to_all___h == NULL)
7064 | 	shmem_int8_prod_to_all___h = (shmem_int8_prod_to_all___p_h) dlsym(tau_handle,"shmem_int8_prod_to_all__"); 
7065 |     if (shmem_int8_prod_to_all___h == NULL) {
7066 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7092 |   } 
7093 |   else { 
7094 |     if (shmem_int8_sum_to_all___h == NULL)
7095 | 	shmem_int8_sum_to_all___h = (shmem_int8_sum_to_all___p_h) dlsym(tau_handle,"shmem_int8_sum_to_all__"); 
7096 |     if (shmem_int8_sum_to_all___h == NULL) {
7097 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7124 |   } 
7125 |   else { 
7126 |     if (shmem_int8_swap___h == NULL)
7127 | 	shmem_int8_swap___h = (shmem_int8_swap___p_h) dlsym(tau_handle,"shmem_int8_swap__"); 
7128 |     if (shmem_int8_swap___h == NULL) {
7129 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7160 |   } 
7161 |   else { 
7162 |     if (shmem_int8_wait___h == NULL)
7163 | 	shmem_int8_wait___h = (shmem_int8_wait___p_h) dlsym(tau_handle,"shmem_int8_wait__"); 
7164 |     if (shmem_int8_wait___h == NULL) {
7165 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7191 |   } 
7192 |   else { 
7193 |     if (shmem_int8_wait_until___h == NULL)
7194 | 	shmem_int8_wait_until___h = (shmem_int8_wait_until___p_h) dlsym(tau_handle,"shmem_int8_wait_until__"); 
7195 |     if (shmem_int8_wait_until___h == NULL) {
7196 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7222 |   } 
7223 |   else { 
7224 |     if (shmem_int8_xor_to_all___h == NULL)
7225 | 	shmem_int8_xor_to_all___h = (shmem_int8_xor_to_all___p_h) dlsym(tau_handle,"shmem_int8_xor_to_all__"); 
7226 |     if (shmem_int8_xor_to_all___h == NULL) {
7227 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7253 |   } 
7254 |   else { 
7255 |     if (shmem_integer_get___h == NULL)
7256 | 	shmem_integer_get___h = (shmem_integer_get___p_h) dlsym(tau_handle,"shmem_integer_get__"); 
7257 |     if (shmem_integer_get___h == NULL) {
7258 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7286 |   } 
7287 |   else { 
7288 |     if (shmem_integer_iget___h == NULL)
7289 | 	shmem_integer_iget___h = (shmem_integer_iget___p_h) dlsym(tau_handle,"shmem_integer_iget__"); 
7290 |     if (shmem_integer_iget___h == NULL) {
7291 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7319 |   } 
7320 |   else { 
7321 |     if (shmem_integer_iput___h == NULL)
7322 | 	shmem_integer_iput___h = (shmem_integer_iput___p_h) dlsym(tau_handle,"shmem_integer_iput__"); 
7323 |     if (shmem_integer_iput___h == NULL) {
7324 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7352 |   } 
7353 |   else { 
7354 |     if (shmem_integer_put___h == NULL)
7355 | 	shmem_integer_put___h = (shmem_integer_put___p_h) dlsym(tau_handle,"shmem_integer_put__"); 
7356 |     if (shmem_integer_put___h == NULL) {
7357 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7385 |   } 
7386 |   else { 
7387 |     if (shmem_iput128___h == NULL)
7388 | 	shmem_iput128___h = (shmem_iput128___p_h) dlsym(tau_handle,"shmem_iput128__"); 
7389 |     if (shmem_iput128___h == NULL) {
7390 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7418 |   } 
7419 |   else { 
7420 |     if (shmem_iput16___h == NULL)
7421 | 	shmem_iput16___h = (shmem_iput16___p_h) dlsym(tau_handle,"shmem_iput16__"); 
7422 |     if (shmem_iput16___h == NULL) {
7423 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7451 |   } 
7452 |   else { 
7453 |     if (shmem_iput32___h == NULL)
7454 | 	shmem_iput32___h = (shmem_iput32___p_h) dlsym(tau_handle,"shmem_iput32__"); 
7455 |     if (shmem_iput32___h == NULL) {
7456 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7484 |   } 
7485 |   else { 
7486 |     if (shmem_iput4___h == NULL)
7487 | 	shmem_iput4___h = (shmem_iput4___p_h) dlsym(tau_handle,"shmem_iput4__"); 
7488 |     if (shmem_iput4___h == NULL) {
7489 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7517 |   } 
7518 |   else { 
7519 |     if (shmem_iput64___h == NULL)
7520 | 	shmem_iput64___h = (shmem_iput64___p_h) dlsym(tau_handle,"shmem_iput64__"); 
7521 |     if (shmem_iput64___h == NULL) {
7522 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7550 |   } 
7551 |   else { 
7552 |     if (shmem_iput8___h == NULL)
7553 | 	shmem_iput8___h = (shmem_iput8___p_h) dlsym(tau_handle,"shmem_iput8__"); 
7554 |     if (shmem_iput8___h == NULL) {
7555 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7583 |   } 
7584 |   else { 
7585 |     if (shmem_logical_get___h == NULL)
7586 | 	shmem_logical_get___h = (shmem_logical_get___p_h) dlsym(tau_handle,"shmem_logical_get__"); 
7587 |     if (shmem_logical_get___h == NULL) {
7588 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7616 |   } 
7617 |   else { 
7618 |     if (shmem_logical_iget___h == NULL)
7619 | 	shmem_logical_iget___h = (shmem_logical_iget___p_h) dlsym(tau_handle,"shmem_logical_iget__"); 
7620 |     if (shmem_logical_iget___h == NULL) {
7621 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7649 |   } 
7650 |   else { 
7651 |     if (shmem_logical_iput___h == NULL)
7652 | 	shmem_logical_iput___h = (shmem_logical_iput___p_h) dlsym(tau_handle,"shmem_logical_iput__"); 
7653 |     if (shmem_logical_iput___h == NULL) {
7654 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7682 |   } 
7683 |   else { 
7684 |     if (shmem_logical_put___h == NULL)
7685 | 	shmem_logical_put___h = (shmem_logical_put___p_h) dlsym(tau_handle,"shmem_logical_put__"); 
7686 |     if (shmem_logical_put___h == NULL) {
7687 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7716 |   } 
7717 |   else { 
7718 |     if (shmem_my_pe___h == NULL)
7719 | 	shmem_my_pe___h = (shmem_my_pe___p_h) dlsym(tau_handle,"shmem_my_pe__"); 
7720 |     if (shmem_my_pe___h == NULL) {
7721 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7749 |   } 
7750 |   else { 
7751 |     if (shmem_n_pes___h == NULL)
7752 | 	shmem_n_pes___h = (shmem_n_pes___p_h) dlsym(tau_handle,"shmem_n_pes__"); 
7753 |     if (shmem_n_pes___h == NULL) {
7754 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7782 |   } 
7783 |   else { 
7784 |     if (shmem_pe_accessible___h == NULL)
7785 | 	shmem_pe_accessible___h = (shmem_pe_accessible___p_h) dlsym(tau_handle,"shmem_pe_accessible__"); 
7786 |     if (shmem_pe_accessible___h == NULL) {
7787 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7814 |   } 
7815 |   else { 
7816 |     if (shmem_ptr___h == NULL)
7817 | 	shmem_ptr___h = (shmem_ptr___p_h) dlsym(tau_handle,"shmem_ptr__"); 
7818 |     if (shmem_ptr___h == NULL) {
7819 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7845 |   } 
7846 |   else { 
7847 |     if (shmem_put128___h == NULL)
7848 | 	shmem_put128___h = (shmem_put128___p_h) dlsym(tau_handle,"shmem_put128__"); 
7849 |     if (shmem_put128___h == NULL) {
7850 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7878 |   } 
7879 |   else { 
7880 |     if (shmem_put16___h == NULL)
7881 | 	shmem_put16___h = (shmem_put16___p_h) dlsym(tau_handle,"shmem_put16__"); 
7882 |     if (shmem_put16___h == NULL) {
7883 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7911 |   } 
7912 |   else { 
7913 |     if (shmem_put32___h == NULL)
7914 | 	shmem_put32___h = (shmem_put32___p_h) dlsym(tau_handle,"shmem_put32__"); 
7915 |     if (shmem_put32___h == NULL) {
7916 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7944 |   } 
7945 |   else { 
7946 |     if (shmem_put4___h == NULL)
7947 | 	shmem_put4___h = (shmem_put4___p_h) dlsym(tau_handle,"shmem_put4__"); 
7948 |     if (shmem_put4___h == NULL) {
7949 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7977 |   } 
7978 |   else { 
7979 |     if (shmem_put64___h == NULL)
7980 | 	shmem_put64___h = (shmem_put64___p_h) dlsym(tau_handle,"shmem_put64__"); 
7981 |     if (shmem_put64___h == NULL) {
7982 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8010 |   } 
8011 |   else { 
8012 |     if (shmem_put8___h == NULL)
8013 | 	shmem_put8___h = (shmem_put8___p_h) dlsym(tau_handle,"shmem_put8__"); 
8014 |     if (shmem_put8___h == NULL) {
8015 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8043 |   } 
8044 |   else { 
8045 |     if (shmem_putmem___h == NULL)
8046 | 	shmem_putmem___h = (shmem_putmem___p_h) dlsym(tau_handle,"shmem_putmem__"); 
8047 |     if (shmem_putmem___h == NULL) {
8048 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8076 |   } 
8077 |   else { 
8078 |     if (shmem_quiet___h == NULL)
8079 | 	shmem_quiet___h = (shmem_quiet___p_h) dlsym(tau_handle,"shmem_quiet__"); 
8080 |     if (shmem_quiet___h == NULL) {
8081 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8107 |   } 
8108 |   else { 
8109 |     if (shmem_real16_max_to_all___h == NULL)
8110 | 	shmem_real16_max_to_all___h = (shmem_real16_max_to_all___p_h) dlsym(tau_handle,"shmem_real16_max_to_all__"); 
8111 |     if (shmem_real16_max_to_all___h == NULL) {
8112 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8138 |   } 
8139 |   else { 
8140 |     if (shmem_real16_min_to_all___h == NULL)
8141 | 	shmem_real16_min_to_all___h = (shmem_real16_min_to_all___p_h) dlsym(tau_handle,"shmem_real16_min_to_all__"); 
8142 |     if (shmem_real16_min_to_all___h == NULL) {
8143 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8169 |   } 
8170 |   else { 
8171 |     if (shmem_real16_prod_to_all___h == NULL)
8172 | 	shmem_real16_prod_to_all___h = (shmem_real16_prod_to_all___p_h) dlsym(tau_handle,"shmem_real16_prod_to_all__"); 
8173 |     if (shmem_real16_prod_to_all___h == NULL) {
8174 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8200 |   } 
8201 |   else { 
8202 |     if (shmem_real16_sum_to_all___h == NULL)
8203 | 	shmem_real16_sum_to_all___h = (shmem_real16_sum_to_all___p_h) dlsym(tau_handle,"shmem_real16_sum_to_all__"); 
8204 |     if (shmem_real16_sum_to_all___h == NULL) {
8205 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8231 |   } 
8232 |   else { 
8233 |     if (shmem_real4_max_to_all___h == NULL)
8234 | 	shmem_real4_max_to_all___h = (shmem_real4_max_to_all___p_h) dlsym(tau_handle,"shmem_real4_max_to_all__"); 
8235 |     if (shmem_real4_max_to_all___h == NULL) {
8236 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8262 |   } 
8263 |   else { 
8264 |     if (shmem_real4_min_to_all___h == NULL)
8265 | 	shmem_real4_min_to_all___h = (shmem_real4_min_to_all___p_h) dlsym(tau_handle,"shmem_real4_min_to_all__"); 
8266 |     if (shmem_real4_min_to_all___h == NULL) {
8267 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8293 |   } 
8294 |   else { 
8295 |     if (shmem_real4_prod_to_all___h == NULL)
8296 | 	shmem_real4_prod_to_all___h = (shmem_real4_prod_to_all___p_h) dlsym(tau_handle,"shmem_real4_prod_to_all__"); 
8297 |     if (shmem_real4_prod_to_all___h == NULL) {
8298 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8324 |   } 
8325 |   else { 
8326 |     if (shmem_real4_sum_to_all___h == NULL)
8327 | 	shmem_real4_sum_to_all___h = (shmem_real4_sum_to_all___p_h) dlsym(tau_handle,"shmem_real4_sum_to_all__"); 
8328 |     if (shmem_real4_sum_to_all___h == NULL) {
8329 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8356 |   } 
8357 |   else { 
8358 |     if (shmem_real4_swap___h == NULL)
8359 | 	shmem_real4_swap___h = (shmem_real4_swap___p_h) dlsym(tau_handle,"shmem_real4_swap__"); 
8360 |     if (shmem_real4_swap___h == NULL) {
8361 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8392 |   } 
8393 |   else { 
8394 |     if (shmem_real8_max_to_all___h == NULL)
8395 | 	shmem_real8_max_to_all___h = (shmem_real8_max_to_all___p_h) dlsym(tau_handle,"shmem_real8_max_to_all__"); 
8396 |     if (shmem_real8_max_to_all___h == NULL) {
8397 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8423 |   } 
8424 |   else { 
8425 |     if (shmem_real8_min_to_all___h == NULL)
8426 | 	shmem_real8_min_to_all___h = (shmem_real8_min_to_all___p_h) dlsym(tau_handle,"shmem_real8_min_to_all__"); 
8427 |     if (shmem_real8_min_to_all___h == NULL) {
8428 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8454 |   } 
8455 |   else { 
8456 |     if (shmem_real8_prod_to_all___h == NULL)
8457 | 	shmem_real8_prod_to_all___h = (shmem_real8_prod_to_all___p_h) dlsym(tau_handle,"shmem_real8_prod_to_all__"); 
8458 |     if (shmem_real8_prod_to_all___h == NULL) {
8459 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8485 |   } 
8486 |   else { 
8487 |     if (shmem_real8_sum_to_all___h == NULL)
8488 | 	shmem_real8_sum_to_all___h = (shmem_real8_sum_to_all___p_h) dlsym(tau_handle,"shmem_real8_sum_to_all__"); 
8489 |     if (shmem_real8_sum_to_all___h == NULL) {
8490 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8517 |   } 
8518 |   else { 
8519 |     if (shmem_real8_swap___h == NULL)
8520 | 	shmem_real8_swap___h = (shmem_real8_swap___p_h) dlsym(tau_handle,"shmem_real8_swap__"); 
8521 |     if (shmem_real8_swap___h == NULL) {
8522 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8553 |   } 
8554 |   else { 
8555 |     if (shmem_real_get___h == NULL)
8556 | 	shmem_real_get___h = (shmem_real_get___p_h) dlsym(tau_handle,"shmem_real_get__"); 
8557 |     if (shmem_real_get___h == NULL) {
8558 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8586 |   } 
8587 |   else { 
8588 |     if (shmem_real_iget___h == NULL)
8589 | 	shmem_real_iget___h = (shmem_real_iget___p_h) dlsym(tau_handle,"shmem_real_iget__"); 
8590 |     if (shmem_real_iget___h == NULL) {
8591 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8619 |   } 
8620 |   else { 
8621 |     if (shmem_real_iput___h == NULL)
8622 | 	shmem_real_iput___h = (shmem_real_iput___p_h) dlsym(tau_handle,"shmem_real_iput__"); 
8623 |     if (shmem_real_iput___h == NULL) {
8624 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8652 |   } 
8653 |   else { 
8654 |     if (shmem_real_put___h == NULL)
8655 | 	shmem_real_put___h = (shmem_real_put___p_h) dlsym(tau_handle,"shmem_real_put__"); 
8656 |     if (shmem_real_put___h == NULL) {
8657 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8685 |   } 
8686 |   else { 
8687 |     if (shmem_set_cache_inv___h == NULL)
8688 | 	shmem_set_cache_inv___h = (shmem_set_cache_inv___p_h) dlsym(tau_handle,"shmem_set_cache_inv__"); 
8689 |     if (shmem_set_cache_inv___h == NULL) {
8690 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8716 |   } 
8717 |   else { 
8718 |     if (shmem_set_cache_line_inv___h == NULL)
8719 | 	shmem_set_cache_line_inv___h = (shmem_set_cache_line_inv___p_h) dlsym(tau_handle,"shmem_set_cache_line_inv__"); 
8720 |     if (shmem_set_cache_line_inv___h == NULL) {
8721 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8747 |   } 
8748 |   else { 
8749 |     if (shmem_set_lock___h == NULL)
8750 | 	shmem_set_lock___h = (shmem_set_lock___p_h) dlsym(tau_handle,"shmem_set_lock__"); 
8751 |     if (shmem_set_lock___h == NULL) {
8752 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8779 |   } 
8780 |   else { 
8781 |     if (shmem_swap___h == NULL)
8782 | 	shmem_swap___h = (shmem_swap___p_h) dlsym(tau_handle,"shmem_swap__"); 
8783 |     if (shmem_swap___h == NULL) {
8784 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8816 |   } 
8817 |   else { 
8818 |     if (shmem_test_lock___h == NULL)
8819 | 	shmem_test_lock___h = (shmem_test_lock___p_h) dlsym(tau_handle,"shmem_test_lock__"); 
8820 |     if (shmem_test_lock___h == NULL) {
8821 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8848 |   } 
8849 |   else { 
8850 |     if (shmem_udcflush___h == NULL)
8851 | 	shmem_udcflush___h = (shmem_udcflush___p_h) dlsym(tau_handle,"shmem_udcflush__"); 
8852 |     if (shmem_udcflush___h == NULL) {
8853 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8879 |   } 
8880 |   else { 
8881 |     if (shmem_udcflush_line___h == NULL)
8882 | 	shmem_udcflush_line___h = (shmem_udcflush_line___p_h) dlsym(tau_handle,"shmem_udcflush_line__"); 
8883 |     if (shmem_udcflush_line___h == NULL) {
8884 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8910 |   } 
8911 |   else { 
8912 |     if (shmem_wait___h == NULL)
8913 | 	shmem_wait___h = (shmem_wait___p_h) dlsym(tau_handle,"shmem_wait__"); 
8914 |     if (shmem_wait___h == NULL) {
8915 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8941 |   } 
8942 |   else { 
8943 |     if (shmem_wait_until___h == NULL)
8944 | 	shmem_wait_until___h = (shmem_wait_until___p_h) dlsym(tau_handle,"shmem_wait_until__"); 
8945 |     if (shmem_wait_until___h == NULL) {
8946 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8972 |   } 
8973 |   else { 
8974 |     if (start_pes___h == NULL)
8975 | 	start_pes___h = (start_pes___p_h) dlsym(tau_handle,"start_pes__"); 
8976 |     if (start_pes___h == NULL) {
8977 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9010 |   } 
9011 |   else { 
9012 |     if (shmem_clear_cache_inv_h == NULL)
9013 | 	shmem_clear_cache_inv_h = (shmem_clear_cache_inv_p_h) dlsym(tau_handle,"shmem_clear_cache_inv"); 
9014 |     if (shmem_clear_cache_inv_h == NULL) {
9015 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9041 |   } 
9042 |   else { 
9043 |     if (shmem_set_cache_inv_h == NULL)
9044 | 	shmem_set_cache_inv_h = (shmem_set_cache_inv_p_h) dlsym(tau_handle,"shmem_set_cache_inv"); 
9045 |     if (shmem_set_cache_inv_h == NULL) {
9046 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9072 |   } 
9073 |   else { 
9074 |     if (shmem_clear_cache_line_inv_h == NULL)
9075 | 	shmem_clear_cache_line_inv_h = (shmem_clear_cache_line_inv_p_h) dlsym(tau_handle,"shmem_clear_cache_line_inv"); 
9076 |     if (shmem_clear_cache_line_inv_h == NULL) {
9077 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9103 |   } 
9104 |   else { 
9105 |     if (shmem_set_cache_line_inv_h == NULL)
9106 | 	shmem_set_cache_line_inv_h = (shmem_set_cache_line_inv_p_h) dlsym(tau_handle,"shmem_set_cache_line_inv"); 
9107 |     if (shmem_set_cache_line_inv_h == NULL) {
9108 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9135 |   } 
9136 |   else { 
9137 |     if (my_pe__h == NULL)
9138 | 	my_pe__h = (my_pe__p_h) dlsym(tau_handle,"my_pe_"); 
9139 |     if (my_pe__h == NULL) {
9140 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9168 |   } 
9169 |   else { 
9170 |     if (my_pe___h == NULL)
9171 | 	my_pe___h = (my_pe___p_h) dlsym(tau_handle,"my_pe__"); 
9172 |     if (my_pe___h == NULL) {
9173 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
{% endraw %}

```
### apex/src/wrappers/pthread_wrapper.c

```c

{% raw %}
33 |   RESET_DLERROR();
34 | 
35 |   // Attempt to get the function handle
36 |   handle = dlsym(RTLD_NEXT, name);
37 | 
38 |   // Detect errors
47 |     CHECK_DLERROR();
48 |     do {
49 |       RESET_DLERROR();
50 |       handle = dlsym(syms, name);
51 |       CHECK_DLERROR();
52 |     } while (handle == caller);
{% endraw %}

```