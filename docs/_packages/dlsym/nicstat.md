---
name: "nicstat"
layout: package
next_package: silo
previous_package: krb5
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.95
1 / 18 files match, 1 filtered matches.

 - [nicstat.c](#nicstatc)

### nicstat.c

```c

{% raw %}
2530 | 	if ((handle = dlopen("libdladm.so.1", RTLD_LAZY)) == NULL)
2531 | 		return;
2532 | 	if ((fptr = (dladm_status_t (*)())
2533 | 	    dlsym(handle, "dladm_datalink_id2info")) == NULL) {
2534 | 		(void) dlclose(handle);
2535 | 		return;
{% endraw %}

```