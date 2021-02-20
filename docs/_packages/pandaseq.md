---
name: "pandaseq"
layout: package
next_package: papi
previous_package: p11-kit
languages: ['c']
---
## 2.10
1 / 115 files match, 1 filtered matches.

 - [module.c](#modulec)

### module.c

```c

{% raw %}
250 | 		return NULL;
251 | 	}
252 | 
253 | 	handle = lt_dlopenext(name);
254 | 	if (handle == NULL) {
255 | 		fprintf(stderr, "Could not open module %s: %s\n", name, lt_dlerror());
404 | 	const char **version;
405 | 
406 | 	(void) data;
407 | 	handle = lt_dlopenext(filename);
408 | 	if (handle == NULL) {
409 | 		return 0;
{% endraw %}

```