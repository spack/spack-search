---
name: "ipcalc"
layout: package
next_package: ipopt
previous_package: intel-tbb
languages: ['c']
---
## 0.2.3
1 / 30 files match, 1 filtered matches.

 - [ipcalc-geoip.c](#ipcalc-geoipc)

### ipcalc-geoip.c

```c

{% raw %}
73 | 		return ret;
74 | 	}
75 | 
76 | 	ld = dlopen(LIBNAME, RTLD_LAZY);
77 | 	if (ld == NULL) {
78 | 		snprintf(err, sizeof(err), "ipcalc: could not open %s\n", LIBNAME);
{% endraw %}

```