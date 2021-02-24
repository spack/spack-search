---
name: "cpuinfo"
layout: package
next_package: iproute2
previous_package: php
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## master
2 / 547 files match, 2 filtered matches.

 - [src/arm/linux/hwcap.c](#srcarmlinuxhwcapc)
 - [tools/auxv-dump.c](#toolsauxv-dumpc)

### src/arm/linux/hwcap.c

```c

{% raw %}
58 | 				goto cleanup;
59 | 			}
60 | 
61 | 			getauxval = (getauxval_function_t) dlsym(libc, "getauxval");
62 | 			if (getauxval == NULL) {
63 | 				cpuinfo_log_info("failed to locate getauxval in libc.so: %s", dlerror());
{% endraw %}

```
### tools/auxv-dump.c

```c

{% raw %}
16 | 		exit(EXIT_FAILURE);
17 | 	}
18 | 
19 | 	getauxval_function_t getauxval = (getauxval_function_t) dlsym(libc, "getauxval");
20 | 	if (getauxval == NULL) {
21 | 		fprintf(stderr, "Error: failed to locate getauxval in libc.so: %s", dlerror());
{% endraw %}

```