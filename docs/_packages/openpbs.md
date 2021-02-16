---
name: "openpbs"
layout: package
next_package: mbedtls
previous_package: premake-core
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
91 |         munge_dlhandle = dlopen(libmunge, RTLD_LAZY);
{% endraw %}

```
### src/resmom/linux/mom_mach.c

```c

{% raw %}
7954 | 		(handle = dlopen(memacctsoname, RTLD_LAZY)) == NULL) {
{% endraw %}

```
### src/resmom/linux/mom_start.c

```c

{% raw %}
1494 | 	handle1 = dlopen(libjob, RTLD_LAZY);
1498 | 		sprintf(log_buffer, "%s. failed to dlopen %s", dlerror(), libjob);
1504 | 	sprintf(log_buffer, "dlopen of %s successful", libjob);
1541 | 	handle2 = dlopen(libcsa, RTLD_LAZY);
1545 | 		sprintf(log_buffer, "%s. failed to dlopen %s", dlerror(), libcsa);
1551 | 	sprintf(log_buffer, "dlopen of %s successful", libcsa);
{% endraw %}

```