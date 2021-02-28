---
name: "dotconf"
layout: package
next_package: ngspice
previous_package: openmc
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.3
3 / 42 files match, 2 filtered matches.

 - [examples/duplicates/duplicate.c](#examplesduplicatesduplicatec)
 - [examples/modules/module.c](#examplesmodulesmodulec)

### examples/duplicates/duplicate.c

```c

{% raw %}
214 | 			if (access(filename, R_OK) == 0) {	/* if file access is permitted */
215 | 				/* load library */
216 | 				handles[handle_idx] =
217 | 				    dlopen(filename, RTLD_LAZY);
218 | 				if (!handles[handle_idx]) {
219 | 					fprintf(stderr,
{% endraw %}

```
### examples/modules/module.c

```c

{% raw %}
105 | 
106 | 	if (!access(filename, R_OK)) {	/* if file access is permitted */
107 | 		/* load library */
108 | 		handles[i] = dlopen(filename, RTLD_LAZY);
109 | 		if (!handles[i])
110 | 			printf("Error opening library: %s\n", dlerror());
{% endraw %}

```