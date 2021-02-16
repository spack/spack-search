---
name: "cbtf-krell"
layout: package
next_package: cctools
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
55 | extern void cbtf_offline_record_dso(const char* dsoname, uint64_t begin, uint64_t end, uint8_t is_dlopen);
56 | extern void cbtf_offline_record_dlopen(const char* dsoname, uint64_t begin, uint64_t end, uint64_t b_time, uint64_t e_time);
257 | 	cbtf_offline_record_dlopen(name, regions[0].mem_addr,
390 | 	    cbtf_offline_record_dlopen(mappedpath, begin, end, b_time, e_time);
{% endraw %}

```
### services/src/monitor/Monitor.c

```c

{% raw %}
483 | void monitor_dlopen(const char *library, int flags, void *handle)
499 | 	    fprintf(stderr,"[%d,%d] monitor_dlopen returns early due to in mpi init\n",thePid,monitor_get_thread_num());
506 | 	    fprintf(stderr,"[%d,%d] monitor_dlopen ignores null library name\n",thePid,monitor_get_thread_num());
515 | 	fprintf(stderr,"[%d,%d] monitor_dlopen called with %s\n",
529 | 	    fprintf(stderr,"[%d,%d] monitor_dlopen RESUME SAMPLING\n",
533 | 	cbtf_offline_sampling_status(CBTF_Monitor_dlopen_event,CBTF_Monitor_Resumed);
538 | monitor_pre_dlopen(const char *path, int flags)
554 | 	    fprintf(stderr,"[%d,%d] monitor_pre_dlopen returns early due to in mpi init\n",thePid,monitor_get_thread_num());
561 | 	    fprintf(stderr,"[%d,%d] monitor_pre_dlopen ignores null path\n",thePid,monitor_get_thread_num());
567 | 	fprintf(stderr,"[%d,%d] monitor_pre_dlopen %s\n",thePid,monitor_get_thread_num(),path);
573 | 	    fprintf(stderr,"[%d,%d] monitor_pre_dlopen PAUSE SAMPLING\n",
577 | 	cbtf_offline_sampling_status(CBTF_Monitor_pre_dlopen_event,CBTF_Monitor_Paused);
{% endraw %}

```
### services/include/KrellInstitute/Services/Offline.h

```c

{% raw %}
59 |                         uint8_t is_dlopen);
{% endraw %}

```
### services/include/KrellInstitute/Services/Monitor.h

```c

{% raw %}
54 |     CBTF_Monitor_pre_dlopen_event,
55 |     CBTF_Monitor_dlopen_event,
{% endraw %}

```
### services/collector/monitor.c

```c

{% raw %}
292 | 	case CBTF_Monitor_pre_dlopen_event:
295 | 	        fprintf(stderr,"[%d,%d] cbtf_offline_sampling_status CBTF_Monitor_pre_dlopen_event NOOP status:%s\n",
300 | 	case CBTF_Monitor_dlopen_event:
303 | 	        fprintf(stderr,"[%d,%d] cbtf_offline_sampling_status CBTF_Monitor_dlopen_event NOOP status:%s\n",
{% endraw %}

```
### services/collector/collector.c

```c

{% raw %}
939 | 			uint8_t is_dlopen)
950 |     if (is_dlopen) {
965 |     if (is_dlopen) {
975 |     objects.is_open = is_dlopen;
982 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
986 | 	fprintf(stderr,"cbtf_offline_record_dso fileio: dso:%s is_dlopen:%d time_begin:%ld time_end:%ld addr_begin:%lx addr_end:%lx is_exe:%d\n",
987 | 	dsoname, is_dlopen, objects.time_begin,objects.time_end,objects.addr_begin,objects.addr_end,objects.is_executable);
998 |     if (is_dlopen) {
1017 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
1021 | 	fprintf(stderr,"cbtf_offline_record_dso cbtf: dso:%s is_dlopen:%d time_begin:%ld time_end:%ld addr_begin:%lx addr_end:%lx is_exe:%d\n",
1022 | 	dsoname, is_dlopen,objects.time_begin,objects.time_end,objects.range.begin,objects.range.end,objects.is_executable);
1131 |     if (is_dlopen) {
1148 | void cbtf_offline_record_dlopen(const char* dsoname,
1256 |             fprintf(stderr,"[%d,%d] cbtf_offline_record_dlopen SENDS OBJS for %s:%lld:%lld:%d:%d\n",
{% endraw %}

```
### core/collectors/mem/monitor.c

```c

{% raw %}
475 | 			uint8_t is_dlopen)
486 |     if (is_dlopen) {
499 |     if (is_dlopen) {
504 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
511 |     objects.is_open = is_dlopen;
594 |     if (is_dlopen) {
{% endraw %}

```
### core/collectors/pcsamp/monitor.c

```c

{% raw %}
570 | 			uint8_t is_dlopen)
581 |     if (is_dlopen) {
595 |     if (is_dlopen) {
600 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
607 |     objects.is_open = is_dlopen;
729 |     if (is_dlopen) {
{% endraw %}

```