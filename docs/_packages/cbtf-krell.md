---
name: "cbtf-krell"
layout: package
next_package: wt
previous_package: maloc
languages: ['cpp']
---
## 1.9.3
35 / 607 files match

 - [CMakeLists.txt](#cmakeliststxt)
 - [services/configure.ac](#servicesconfigureac)
 - [services/src/offline/offline.x](#servicessrcofflineofflinex)
 - [services/src/offline/GetDLInfo.c](#servicessrcofflinegetdlinfoc)
 - [services/src/monitor/Monitor.c](#servicessrcmonitormonitorc)
 - [services/include/KrellInstitute/Services/Offline.h](#servicesincludekrellinstituteservicesofflineh)
 - [services/include/KrellInstitute/Services/Monitor.h](#servicesincludekrellinstituteservicesmonitorh)
 - [services/collector/monitor.c](#servicescollectormonitorc)
 - [services/collector/collector.c](#servicescollectorcollectorc)
 - [core/configure.ac](#coreconfigureac)
 - [core/components/LinkedObjectComponent.cpp](#corecomponentslinkedobjectcomponentcpp)
 - [core/collectors/template.xml.in](#corecollectorstemplatexmlin)
 - [core/collectors/mem/monitor.c](#corecollectorsmemmonitorc)
 - [core/collectors/mem/mem.xml.in](#corecollectorsmemmemxmlin)
 - [core/collectors/pcsamp/pcsamp.xml.in](#corecollectorspcsamppcsampxmlin)
 - [core/collectors/pcsamp/monitor.c](#corecollectorspcsampmonitorc)
 - [core/collectors/io/io.xml.in](#corecollectorsioioxmlin)
 - [core/collectors/io/iot.xml.in](#corecollectorsioiotxmlin)
 - [core/collectors/io/iop.xml.in](#corecollectorsioiopxmlin)
 - [core/collectors/hwcsamp/hwcsamp.xml.in](#corecollectorshwcsamphwcsampxmlin)
 - [core/collectors/mpi/mpit.xml.in](#corecollectorsmpimpitxmlin)
 - [core/collectors/mpi/mpip.xml.in](#corecollectorsmpimpipxmlin)
 - [core/collectors/mpi/mpi.xml.in](#corecollectorsmpimpixmlin)
 - [core/collectors/pthreads/pthreads.xml.in](#corecollectorspthreadspthreadsxmlin)
 - [core/collectors/hwctime/hwctime.xml.in](#corecollectorshwctimehwctimexmlin)
 - [core/collectors/hwc/hwc.xml.in](#corecollectorshwchwcxmlin)
 - [core/collectors/usertime/usertime.xml.in](#corecollectorsusertimeusertimexmlin)
 - [core/scripts/cbtflink.in](#corescriptscbtflinkin)
 - [test/configure.ac](#testconfigureac)
 - [examples/configure.ac](#examplesconfigureac)
 - [examples/src/python/pyExample.cpp](#examplessrcpythonpyexamplecpp)
 - [contrib/configure.ac](#contribconfigureac)
 - [messages/configure.ac](#messagesconfigureac)
 - [messages/src/events/LinkedObjectEvents.x](#messagessrceventslinkedobjecteventsx)
 - [messages/src/events/OfflineEvents.x](#messagessrceventsofflineeventsx)

### CMakeLists.txt

```

{% raw %}
77 |   #set(HAVE_DLOPEN)
78 |   add_definitions(-DHAVE_DLOPEN)
79 |   add_definitions(-DHAVE_TARGET_DLOPEN)
81 |   check_function_exists(dlopen HAVE_TARGET_DLOPEN)
82 |   if (HAVE_TARGET_DLOPEN)
83 |     add_definitions(-DHAVE_DLOPEN)
85 |   # If dlopen can be found without linking in dl then dlopen is part
{% endraw %}

```
### services/configure.ac

```

{% raw %}
52 | LT_INIT([dlopen])
285 | # Runtime Target DLOPEN Availability Specification (libmonitor callbacks)
288 | # Option: --enable-target_dlopen=yes
290 | AC_MSG_CHECKING(for target dlopen support specification)
291 | AC_ARG_ENABLE([target_dlopen],
292 |     [AS_HELP_STRING([--enable-target_dlopen],
293 |         [include support on the target architecture for dlopen [default=yes]])],
294 |     [], [enable_target_dlopen=yes])
296 | if test "x$enable_target_dlopen" = xyes ; then
297 |     AC_DEFINE([HAVE_TARGET_DLOPEN], [1],
298 |         [Enable support on the target architecture for dlopen.])
304 | AC_SUBST(HAVE_TARGET_DLOPEN)
{% endraw %}

```
### services/src/offline/offline.x

```

{% raw %}
31 |     uint8_t  is_open;     /** < flag to indicate dlopen or dlclose */
{% endraw %}

```
### services/src/offline/GetDLInfo.c

```cpp

{% raw %}
55 | extern void cbtf_offline_record_dso(const char* dsoname, uint64_t begin, uint64_t end, uint8_t is_dlopen);
56 | extern void cbtf_offline_record_dlopen(const char* dsoname, uint64_t begin, uint64_t end, uint64_t b_time, uint64_t e_time);
257 | 	cbtf_offline_record_dlopen(name, regions[0].mem_addr,
380 | 	/* the victim application has performed a dlopen. */
386 | 		fprintf(stderr,"CBTF_GetDLInfo DLOPEN RECORD: %s [%08Lx, %08Lx]\n",
390 | 	    cbtf_offline_record_dlopen(mappedpath, begin, end, b_time, e_time);
394 | 	/* Record the address range and mappedfile for non dlopened objects. */
{% endraw %}

```
### services/src/monitor/Monitor.c

```cpp

{% raw %}
40 |  * monitor_dlopen(const char *path, int flags, void *handle)  SERVICE callback.
479 | #ifdef HAVE_TARGET_DLOPEN
481 |  * callbacks for handling of DLOPEN/DLCLOSE.
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
615 | 	   /* On some systems (NASA) it appears that dlopen can be called
{% endraw %}

```
### services/include/KrellInstitute/Services/Offline.h

```cpp

{% raw %}
59 |                         uint8_t is_dlopen);
{% endraw %}

```
### services/include/KrellInstitute/Services/Monitor.h

```cpp

{% raw %}
54 |     CBTF_Monitor_pre_dlopen_event,
55 |     CBTF_Monitor_dlopen_event,
{% endraw %}

```
### services/collector/monitor.c

```cpp

{% raw %}
292 | 	case CBTF_Monitor_pre_dlopen_event:
295 | 	        fprintf(stderr,"[%d,%d] cbtf_offline_sampling_status CBTF_Monitor_pre_dlopen_event NOOP status:%s\n",
300 | 	case CBTF_Monitor_dlopen_event:
303 | 	        fprintf(stderr,"[%d,%d] cbtf_offline_sampling_status CBTF_Monitor_dlopen_event NOOP status:%s\n",
{% endraw %}

```
### services/collector/collector.c

```cpp

{% raw %}
934 |  * @param is_dlopen    Boolean "true" if this DSO was just opened,
939 | 			uint8_t is_dlopen)
950 |     if (is_dlopen) {
965 |     if (is_dlopen) {
975 |     objects.is_open = is_dlopen;
982 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
986 | 	fprintf(stderr,"cbtf_offline_record_dso fileio: dso:%s is_dlopen:%d time_begin:%ld time_end:%ld addr_begin:%lx addr_end:%lx is_exe:%d\n",
987 | 	dsoname, is_dlopen, objects.time_begin,objects.time_end,objects.addr_begin,objects.addr_end,objects.is_executable);
994 |      * and not intended for dlopen/dlclose callbacks
998 |     if (is_dlopen) {
1017 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
1021 | 	fprintf(stderr,"cbtf_offline_record_dso cbtf: dso:%s is_dlopen:%d time_begin:%ld time_end:%ld addr_begin:%lx addr_end:%lx is_exe:%d\n",
1022 | 	dsoname, is_dlopen,objects.time_begin,objects.time_end,objects.range.begin,objects.range.end,objects.is_executable);
1030 |      * intended ONLY for dlopen/dlclose callbacks
1052 |      * intended ONLY for dlopen/dlclose callbacks
1072 | //FIXME: verify that mrnet collections works for dlopen/dlclose.
1131 |     if (is_dlopen) {
1137 |  * Record a dlopened library.
1139 |  * Writes information regarding a DSO that was dlopened/dlclosed  in the thread
1148 | void cbtf_offline_record_dlopen(const char* dsoname,
1183 |      * and not intended for dlopen/dlclose callbacks
1206 |      * intended ONLY for dlopen/dlclose callbacks
1228 |      * intended ONLY for dlopen/dlclose callbacks
1256 |             fprintf(stderr,"[%d,%d] cbtf_offline_record_dlopen SENDS OBJS for %s:%lld:%lld:%d:%d\n",
{% endraw %}

```
### core/configure.ac

```

{% raw %}
52 | LT_INIT([dlopen])
{% endraw %}

```
### core/components/LinkedObjectComponent.cpp

```

{% raw %}
544 |     // Handler for dlopen events.
{% endraw %}

```
### core/collectors/template.xml.in

```

{% raw %}
40 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/mem/monitor.c

```cpp

{% raw %}
470 |  * @param is_dlopen    Boolean "true" if this DSO was just opened,
475 | 			uint8_t is_dlopen)
486 |     if (is_dlopen) {
490 |     //fprintf(stderr,"cbtf_offline_record_dso called for %s, is_dlopen = %d\n",dsoname, is_dlopen);
499 |     if (is_dlopen) {
504 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
511 |     objects.is_open = is_dlopen;
594 |     if (is_dlopen) {
{% endraw %}

```
### core/collectors/mem/mem.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/pcsamp/pcsamp.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/pcsamp/monitor.c

```cpp

{% raw %}
565 |  * @param is_dlopen    Boolean "true" if this DSO was just opened,
570 | 			uint8_t is_dlopen)
581 |     if (is_dlopen) {
585 |     //fprintf(stderr,"cbtf_offline_record_dso called for %s, is_dlopen = %d\n",dsoname, is_dlopen);
595 |     if (is_dlopen) {
600 |     objects.time_end = is_dlopen ? -1ULL : CBTF_GetTime();
607 |     objects.is_open = is_dlopen;
612 |      * and not intended for dlopen/dlclose callbacks
636 |      * intended ONLY for dlopen/dlclose callbacks
656 |      * intended ONLY for dlopen/dlclose callbacks
676 | //FIXME: verify that mrnet collections works for dlopen/dlclose.
729 |     if (is_dlopen) {
{% endraw %}

```
### core/collectors/io/io.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/io/iot.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/io/iop.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/hwcsamp/hwcsamp.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/mpi/mpit.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/mpi/mpip.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/mpi/mpi.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/pthreads/pthreads.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/hwctime/hwctime.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/hwc/hwc.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/collectors/usertime/usertime.xml.in

```

{% raw %}
47 |   in to a process or thread.  This is intended to handle dlopen
{% endraw %}

```
### core/scripts/cbtflink.in

```

{% raw %}
43 | #monitor_wrap_dlopen_names="dlopen dlclose"
44 | monitor_wrap_dlopen_names=""
282 | monitor_has_dlopen=`nm ${libmonitor} | grep -i __wrap_dlopen`
296 |   if [ -n "$monitor_has_dlopen" ] ; then
297 |     echo "DEBUG: cbtflink monitor_has_dlopen is non-null"
369 | if [ -n "$monitor_has_dlopen" ] ; then
370 |     for name in $monitor_wrap_dlopen_names ; do
378 |   echo "DEBUG: cbtflink wrap_args for monitor_wrap_dlopen_names = $wrap_args"
379 |   echo "DEBUG: cbtflink collector_service_libs for monitor_wrap_dlopen_names = $collector_service_libs"
{% endraw %}

```
### test/configure.ac

```

{% raw %}
52 | LT_INIT([dlopen])
{% endraw %}

```
### examples/configure.ac

```

{% raw %}
52 | LT_INIT([dlopen])
{% endraw %}

```
### examples/src/python/pyExample.cpp

```

{% raw %}
31 | static int dlopen_hacked = 0;
32 | int dlopen_python_hack()
34 |     if (!dlopen_hacked) {
35 |         dlopen(LIBPYTHON, RTLD_NOW|RTLD_GLOBAL);
36 |         dlopen_hacked = 1;
40 | #define dlopen_python_hack()
266 | 	dlopen_python_hack();
{% endraw %}

```
### contrib/configure.ac

```

{% raw %}
52 | LT_INIT([dlopen])
{% endraw %}

```
### messages/configure.ac

```

{% raw %}
53 | LT_INIT([dlopen])
{% endraw %}

```
### messages/src/events/LinkedObjectEvents.x

```

{% raw %}
42 |  *          when a linked object is loaded due to a dlopen().
{% endraw %}

```
### messages/src/events/OfflineEvents.x

```

{% raw %}
31 |     uint8_t  is_open;       /** < flag to indicate dlopen or dlclose */
32 |     bool  is_executable; /** < flag to indicate dlopen or dlclose */
{% endraw %}

```