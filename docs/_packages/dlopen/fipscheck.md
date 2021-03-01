---
name: "fipscheck"
layout: package
next_package: flexiblas
previous_package: fio
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.0.0.398
2 / 18 files match, 1 filtered matches.

 - [src/library.c](#srclibraryc)

### src/library.c

```c

{% raw %}
71 | 	void *dl, *sym;
72 | 	int rv = -1;
73 | 
74 |         dl = dlopen(libname, RTLD_NODELETE|RTLD_NOLOAD|RTLD_LAZY);
75 |         if (dl == NULL) {
76 | 	        return -1;
{% endraw %}

```