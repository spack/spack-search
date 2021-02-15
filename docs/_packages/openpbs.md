---
name: "openpbs"
layout: package
next_package: mbedtls
previous_package: premake-core
languages: ['cpp']
---
## 19.1.3
4 / 1254 files match

 - [configure.ac](#configureac)
 - [src/lib/Libutil/munge_supp.c](#srcliblibutilmunge_suppc)
 - [src/resmom/linux/mom_mach.c](#srcresmomlinuxmom_machc)
 - [src/resmom/linux/mom_start.c](#srcresmomlinuxmom_startc)

### configure.ac

```

{% raw %}
92 | AC_CHECK_LIB(dl, dlopen)
{% endraw %}

```
### src/lib/Libutil/munge_supp.c

```cpp

{% raw %}
91 |         munge_dlhandle = dlopen(libmunge, RTLD_LAZY);
{% endraw %}

```
### src/resmom/linux/mom_mach.c

```cpp

{% raw %}
7899 |  *	we need to use.  Instead, we use dlopen() and dlsym() to map it in
7954 | 		(handle = dlopen(memacctsoname, RTLD_LAZY)) == NULL) {
{% endraw %}

```
### src/resmom/linux/mom_start.c

```cpp

{% raw %}
134 |  *	Types of shared objects for dlopen.
1464 | 	/* multiple calls to dlopen with the same arguments do not cause multiple
1479 | 	 * If job facility is turned off, don't call dlopen for job_create.
1494 | 	handle1 = dlopen(libjob, RTLD_LAZY);
1498 | 		sprintf(log_buffer, "%s. failed to dlopen %s", dlerror(), libjob);
1504 | 	sprintf(log_buffer, "dlopen of %s successful", libjob);
1522 | 	 * don't call dlopen for CSA.
1541 | 	handle2 = dlopen(libcsa, RTLD_LAZY);
1545 | 		sprintf(log_buffer, "%s. failed to dlopen %s", dlerror(), libcsa);
1551 | 	sprintf(log_buffer, "dlopen of %s successful", libcsa);
1649 |  * 	in a shared library that has been opened by a call to dlopen.
1656 |  * @param[in]	handle	valid handle from call to dlopen
2804 |  *	then returns shared object to the caller for dlopen.
{% endraw %}

```