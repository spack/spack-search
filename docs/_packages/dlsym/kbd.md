---
name: "kbd"
layout: package
next_package: wget
previous_package: petsc
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.3.0
1 / 1012 files match, 1 filtered matches.

 - [tests/libtswrap/ioctl.c](#testslibtswrapioctlc)

### tests/libtswrap/ioctl.c

```c

{% raw %}
307 | 	va_list ap;
308 | 
309 | 	if (!real_ioctl) {
310 | 		real_ioctl = dlsym(RTLD_NEXT, "ioctl");
311 | 		if (!real_ioctl) {
312 | 			fprintf(stderr, "dlsym(ioctl): %s\n", dlerror());
313 | 			exit(1);
314 | 		}
{% endraw %}

```