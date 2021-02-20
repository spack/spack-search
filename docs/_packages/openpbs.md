---
name: "openpbs"
layout: package
next_package: openresty
previous_package: openmpi
languages: ['c']
---
## 19.1.3
4 / 1254 files match, 3 filtered matches.

 - [src/lib/Libutil/munge_supp.c](#srcliblibutilmunge_suppc)
 - [src/resmom/linux/mom_mach.c](#srcresmomlinuxmom_machc)
 - [src/resmom/linux/mom_start.c](#srcresmomlinuxmom_startc)

### src/lib/Libutil/munge_supp.c

```c

{% raw %}
88 | int
89 | init_munge(char *ebuf, int ebufsz)
90 | {
91 |         munge_dlhandle = dlopen(libmunge, RTLD_LAZY);
92 |         if (munge_dlhandle == NULL) {
93 |             snprintf(ebuf, ebufsz, "%s not found", libmunge);
{% endraw %}

```
### src/resmom/linux/mom_mach.c

```c

{% raw %}
7951 | 	 *	ignore this error.
7952 | 	 */
7953 | 	if ((handle == NULL) &&
7954 | 		(handle = dlopen(memacctsoname, RTLD_LAZY)) == NULL) {
7955 | 		sprintf(log_buffer, "%s not found", memacctsoname);
7956 | 		log_event(PBSEVENT_ADMIN, PBS_EVENTCLASS_ACCT,
{% endraw %}

```
### src/resmom/linux/mom_start.c

```c

{% raw %}
1491 | 
1492 | 	sprintf(log_buffer, "using %s for job shared object", libjob);
1493 | 	log_event(PBSEVENT_ADMIN, PBS_EVENTCLASS_ACCT, LOG_DEBUG, __func__, log_buffer);
1494 | 	handle1 = dlopen(libjob, RTLD_LAZY);
1495 | 	if (handle1 == NULL) {
1496 | 		/* facility is not available */
1497 | 
1498 | 		sprintf(log_buffer, "%s. failed to dlopen %s", dlerror(), libjob);
1499 | 		log_event(PBSEVENT_ADMIN, PBS_EVENTCLASS_ACCT, LOG_DEBUG,
1500 | 			__func__, log_buffer);
1501 | 		goto err;
1502 | 	}
1503 | 
1504 | 	sprintf(log_buffer, "dlopen of %s successful", libjob);
1505 | 	log_event(PBSEVENT_ADMIN, PBS_EVENTCLASS_ACCT, LOG_DEBUG,
1506 | 			__func__, log_buffer);
1538 | 	sprintf(log_buffer, "using %s for CSA shared object", libcsa);
1539 | 	log_event(PBSEVENT_ADMIN, PBS_EVENTCLASS_ACCT, LOG_DEBUG, __func__, log_buffer);
1540 | 
1541 | 	handle2 = dlopen(libcsa, RTLD_LAZY);
1542 | 	if (handle2 == NULL) {
1543 | 		/* facility is not available */
1544 | 
1545 | 		sprintf(log_buffer, "%s. failed to dlopen %s", dlerror(), libcsa);
1546 | 		log_event(PBSEVENT_ADMIN, PBS_EVENTCLASS_ACCT, LOG_DEBUG,
1547 | 			__func__, log_buffer);
1548 | 		goto err;
1549 | 	}
1550 | 
1551 | 	sprintf(log_buffer, "dlopen of %s successful", libcsa);
1552 | 	log_event(PBSEVENT_ADMIN, PBS_EVENTCLASS_ACCT, LOG_DEBUG,
1553 | 			__func__, log_buffer);
{% endraw %}

```