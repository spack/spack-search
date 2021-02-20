---
name: "cbtf-krell"
layout: package
next_package: cc65
previous_package: catalyst
languages: ['c']
---
## 1.9.3
35 / 607 files match, 8 filtered matches.

 - [services/src/offline/GetDLInfo.c](#servicessrcofflinegetdlinfoc)
 - [services/src/monitor/Monitor.c](#servicessrcmonitormonitorc)
 - [services/include/KrellInstitute/Services/Offline.h](#servicesincludekrellinstituteservicesofflineh)
 - [services/include/KrellInstitute/Services/Monitor.h](#servicesincludekrellinstituteservicesmonitorh)
 - [services/collector/monitor.c](#servicescollectormonitorc)
 - [services/collector/collector.c](#servicescollectorcollectorc)
 - [core/collectors/mem/monitor.c](#corecollectorsmemmonitorc)
 - [core/collectors/pcsamp/monitor.c](#corecollectorspcsampmonitorc)

### services/src/offline/GetDLInfo.c

```c

{% raw %}
52 |  */
53 | #define CBTF_USE_DL_ITERATE 1
54 | 
55 | extern void cbtf_offline_record_dso(const char* dsoname, uint64_t begin, uint64_t end, uint8_t is_dlopen);
56 | extern void cbtf_offline_record_dlopen(const char* dsoname, uint64_t begin, uint64_t end, uint64_t b_time, uint64_t e_time);
57 | 
58 | extern const char* CBTF_GetExecutablePath();
254 | #endif
255 |    
256 |     if (is_load) {
257 | 	cbtf_offline_record_dlopen(name, regions[0].mem_addr,
258 | 			      regions[0].mem_addr + regions[0].mem_size,
259 | 			      b_time, e_time);
387 | 		    mappedpath, begin, end);
388 | 	    }
389 | #endif
390 | 	    cbtf_offline_record_dlopen(mappedpath, begin, end, b_time, e_time);
391 | 	    break;
392 | 	}
{% endraw %}

```
### services/src/monitor/Monitor.c

```c

{% raw %}
480 | /*
481 |  * callbacks for handling of DLOPEN/DLCLOSE.
482 |  */
483 | void monitor_dlopen(const char *library, int flags, void *handle)
484 | {
485 |     /* Access our thread-local storage */
496 | 
497 |     if (CBTF_in_mpi_startup || tls->in_mpi_pre_init) {
498 |         if (IsMonitorDebugEnabled) {
499 | 	    fprintf(stderr,"[%d,%d] monitor_dlopen returns early due to in mpi init\n",thePid,monitor_get_thread_num());
500 | 	}
501 | 	return;
503 | 
504 |     if (library == NULL) {
505 | 	if (IsMonitorDebugEnabled) {
506 | 	    fprintf(stderr,"[%d,%d] monitor_dlopen ignores null library name\n",thePid,monitor_get_thread_num());
507 | 	}
508 | 	return;
512 |      * if CBTF_GetDLInfo does not handle errors do so here.
513 |      */
514 |     if (IsMonitorDebugEnabled) {
515 | 	fprintf(stderr,"[%d,%d] monitor_dlopen called with %s\n",
516 | 	    thePid,monitor_get_thread_num(),library);
517 |     }
526 | 
527 |     if ((tls->sampling_status == CBTF_Monitor_Paused) && !tls->in_mpi_pre_init) {
528 |         if (IsMonitorDebugEnabled) {
529 | 	    fprintf(stderr,"[%d,%d] monitor_dlopen RESUME SAMPLING\n",
530 | 		thePid,monitor_get_thread_num());
531 |         }
532 | 	tls->sampling_status = CBTF_Monitor_Resumed;
533 | 	cbtf_offline_sampling_status(CBTF_Monitor_dlopen_event,CBTF_Monitor_Resumed);
534 |     }
535 | }
536 | 
537 | void
538 | monitor_pre_dlopen(const char *path, int flags)
539 | {
540 |     /* Access our thread-local storage */
551 | 
552 |     if (tls->in_mpi_pre_init) {
553 |         if (IsMonitorDebugEnabled) {
554 | 	    fprintf(stderr,"[%d,%d] monitor_pre_dlopen returns early due to in mpi init\n",thePid,monitor_get_thread_num());
555 | 	}
556 | 	return;
558 | 
559 |     if (path == NULL) {
560 | 	if (IsMonitorDebugEnabled) {
561 | 	    fprintf(stderr,"[%d,%d] monitor_pre_dlopen ignores null path\n",thePid,monitor_get_thread_num());
562 | 	}
563 | 	return;
564 |     }
565 | 
566 |     if (IsMonitorDebugEnabled) {
567 | 	fprintf(stderr,"[%d,%d] monitor_pre_dlopen %s\n",thePid,monitor_get_thread_num(),path);
568 |     }
569 | 
570 |     if ((tls->sampling_status == CBTF_Monitor_Started ||
571 | 	 tls->sampling_status == CBTF_Monitor_Resumed) && !tls->in_mpi_pre_init) {
572 |         if (IsMonitorDebugEnabled) {
573 | 	    fprintf(stderr,"[%d,%d] monitor_pre_dlopen PAUSE SAMPLING\n",
574 | 		thePid,monitor_get_thread_num());
575 |         }
576 | 	tls->sampling_status = CBTF_Monitor_Paused;
577 | 	cbtf_offline_sampling_status(CBTF_Monitor_pre_dlopen_event,CBTF_Monitor_Paused);
578 |     }
579 | }
{% endraw %}

```
### services/include/KrellInstitute/Services/Offline.h

```c

{% raw %}
56 | void cbtf_offline_start_sampling(const char* arguments);
57 | void cbtf_offline_stop_sampling(const char* arguments, const bool finished);
58 | void cbtf_offline_record_dso(const char* dsoname, uint64_t begin, uint64_t end,
59 |                         uint8_t is_dlopen);
60 | void cbtf_offline_defer_sampling(const int flag);
61 | void cbtf_offline_sampling_status(CBTF_Monitor_Event_Type event, CBTF_Monitor_Status status);
{% endraw %}

```
### services/include/KrellInstitute/Services/Monitor.h

```c

{% raw %}
51 |     CBTF_Monitor_MPI_post_fini_event,
52 |     CBTF_Monitor_MPI_fini_event,
53 |     CBTF_Monitor_MPI_post_comm_rank_event,
54 |     CBTF_Monitor_pre_dlopen_event,
55 |     CBTF_Monitor_dlopen_event,
56 |     CBTF_Monitor_dlclose_event,
57 |     CBTF_Monitor_post_dlclose_event,
{% endraw %}

```
### services/collector/monitor.c

```c

{% raw %}
289 | 		cbtf_offline_service_sampling_control(CBTF_Monitor_Resumed);
290 | 	    }
291 | 	    break;
292 | 	case CBTF_Monitor_pre_dlopen_event:
293 | #ifndef NDEBUG
294 | 	    if (IsCollectorDebugEnabled) {
295 | 	        fprintf(stderr,"[%d,%d] cbtf_offline_sampling_status CBTF_Monitor_pre_dlopen_event NOOP status:%s\n",
296 | 		getpid(),monitor_get_thread_num(),statusstr);
297 | 	    }
298 | #endif
299 | 	    break;
300 | 	case CBTF_Monitor_dlopen_event:
301 | #ifndef NDEBUG
302 | 	    if (IsCollectorDebugEnabled) {
303 | 	        fprintf(stderr,"[%d,%d] cbtf_offline_sampling_status CBTF_Monitor_dlopen_event NOOP status:%s\n",
304 | 		getpid(),monitor_get_thread_num(),statusstr);
305 | 	    }
{% endraw %}

```
### services/collector/collector.c

```c

{% raw %}
936 |  */
937 | void cbtf_offline_record_dso(const char* dsoname,
938 | 			uint64_t begin, uint64_t end,
939 | 			uint8_t is_dlopen)
940 | {
941 |     /* Access our thread-local storage */
947 |     Assert(tls != NULL);
948 | 
949 | 
950 |     if (is_dlopen) {
951 | 	//cbtf_offline_pause_sampling(CBTF_Monitor_Default_event);
952 |     }
962 | #if defined(CBTF_SERVICE_USE_FILEIO)
963 |     CBTF_Protocol_Offline_LinkedObject objects;
964 | 
965 |     if (is_dlopen) {
966 | 	objects.time_begin = CBTF_GetTime();
967 |     } else {
972 |     objects.objname = strdup(dsoname);
973 |     objects.addr_begin = begin;
974 |     objects.addr_end = end;
975 |     objects.is_open = is_dlopen;
976 |     if (strcmp(CBTF_GetExecutablePath(),dsoname)) {
977 | 	objects.is_executable = false;
979 | 	objects.is_executable = true;
980 |     }
981 | 
982 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
983 | 
984 | #ifndef NDEBUG
985 |     if (IsCollectorDebugDsosEnabled) {
986 | 	fprintf(stderr,"cbtf_offline_record_dso fileio: dso:%s is_dlopen:%d time_begin:%ld time_end:%ld addr_begin:%lx addr_end:%lx is_exe:%d\n",
987 | 	dsoname, is_dlopen, objects.time_begin,objects.time_end,objects.addr_begin,objects.addr_end,objects.is_executable);
988 |     }
989 | #endif
995 |      */ 
996 |     CBTF_Protocol_LinkedObject objects;
997 | 
998 |     if (is_dlopen) {
999 | 	objects.time_begin = CBTF_GetTime();
1000 |     } else {
1014 | 	objects.is_executable = true;
1015 |     }
1016 | 
1017 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
1018 | 
1019 | #ifndef NDEBUG
1020 |     if (IsCollectorDebugDsosEnabled) {
1021 | 	fprintf(stderr,"cbtf_offline_record_dso cbtf: dso:%s is_dlopen:%d time_begin:%ld time_end:%ld addr_begin:%lx addr_end:%lx is_exe:%d\n",
1022 | 	dsoname, is_dlopen,objects.time_begin,objects.time_end,objects.range.begin,objects.range.end,objects.is_executable);
1023 |     }
1024 | #endif
1128 |     tls->data.linkedobjects.linkedobjects_len++;
1129 |     tls->dsoname_len += dsoname_len;
1130 | 
1131 |     if (is_dlopen) {
1132 | //	cbtf_offline_sampling_status(CBTF_Monitor_Default_event,CBTF_Monitor_Resumed);
1133 |     }
1145 |  * @param b_time       Load time
1146 |  * @param e_time       Unload time
1147 |  */
1148 | void cbtf_offline_record_dlopen(const char* dsoname,
1149 | 			uint64_t begin, uint64_t end,
1150 | 			uint64_t b_time, uint64_t e_time)
1253 |     if(newsize > CBTF_MAXLINKEDOBJECTS * sizeof(objects)) {
1254 | #ifndef NDEBUG
1255 | 	if (IsCollectorDebugEnabled) {
1256 |             fprintf(stderr,"[%d,%d] cbtf_offline_record_dlopen SENDS OBJS for %s:%lld:%lld:%d:%d\n",
1257 | 		    getpid(),monitor_get_thread_num(),
1258 |                     tls->dso_header.host, (long long)tls->dso_header.pid, 
{% endraw %}

```
### core/collectors/mem/monitor.c

```c

{% raw %}
472 |  */
473 | void cbtf_offline_record_dso(const char* dsoname,
474 | 			uint64_t begin, uint64_t end,
475 | 			uint8_t is_dlopen)
476 | {
477 |     /* Access our thread-local storage */
483 |     Assert(tls != NULL);
484 | 
485 | 
486 |     if (is_dlopen) {
487 | 	cbtf_offline_pause_sampling(0);
488 |     }
496 | 
497 |     CBTF_Protocol_Offline_LinkedObject objects;
498 | 
499 |     if (is_dlopen) {
500 | 	objects.time_begin = CBTF_GetTime();
501 |     } else {
502 | 	objects.time_begin = tls->time_started;
503 |     }
504 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
505 |     
506 | 
508 |     objects.objname = strdup(dsoname);
509 |     objects.addr_begin = begin;
510 |     objects.addr_end = end;
511 |     objects.is_open = is_dlopen;
512 | 
513 | #if defined(CBTF_SERVICE_USE_MRNET)
591 |     tls->data.linkedobjects.linkedobjects_len++;
592 |     tls->dsoname_len += dsoname_len;
593 | 
594 |     if (is_dlopen) {
595 | 	cbtf_offline_resume_sampling(0);
596 |     }
{% endraw %}

```
### core/collectors/pcsamp/monitor.c

```c

{% raw %}
567 |  */
568 | void cbtf_offline_record_dso(const char* dsoname,
569 | 			uint64_t begin, uint64_t end,
570 | 			uint8_t is_dlopen)
571 | {
572 |     /* Access our thread-local storage */
578 |     Assert(tls != NULL);
579 | 
580 | 
581 |     if (is_dlopen) {
582 | 	cbtf_offline_pause_sampling(0);
583 |     }
592 | #if defined(CBTF_SERVICE_USE_FILEIO)
593 |     CBTF_Protocol_Offline_LinkedObject objects;
594 | 
595 |     if (is_dlopen) {
596 | 	objects.time_begin = CBTF_GetTime();
597 |     } else {
598 | 	objects.time_begin = tls->time_started;
599 |     }
600 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
601 |     
602 | 
604 |     objects.objname = strdup(dsoname);
605 |     objects.addr_begin = begin;
606 |     objects.addr_end = end;
607 |     objects.is_open = is_dlopen;
608 | 
609 | #else
726 |     tls->data.linkedobjects.linkedobjects_len++;
727 |     tls->dsoname_len += dsoname_len;
728 | 
729 |     if (is_dlopen) {
730 | 	cbtf_offline_resume_sampling(0);
731 |     }
{% endraw %}

```