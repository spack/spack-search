---
name: "nicstat"
layout: package
next_package: libfabric
previous_package: ipcalc
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.95
1 / 18 files match, 1 filtered matches.

 - [nicstat.c](#nicstatc)

### nicstat.c

```c

{% raw %}
2527 | 	dladm_status_t dlstat;
2528 | 
2529 | 	g_use_dladm = B_FALSE;
2530 | 	if ((handle = dlopen("libdladm.so.1", RTLD_LAZY)) == NULL)
2531 | 		return;
2532 | 	if ((fptr = (dladm_status_t (*)())
{% endraw %}

```