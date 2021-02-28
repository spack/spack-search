---
name: "keyutils"
layout: package
next_package: rdc
previous_package: wget
library_name: dlsym
matches: ['dlsym']
languages: ['c']
---
## 1.5.9
1 / 113 files match, 1 filtered matches.

 - [keyutils.c](#keyutilsc)

### keyutils.c

```c

{% raw %}
522 | 
523 | 	dlerror();
524 | 
525 | 	libc_perror = dlsym(RTLD_NEXT,"perror");
526 | 	if (!libc_perror) {
527 | 		fprintf(stderr, "Failed to look up next perror\n");
533 | 
534 | 	//fprintf(stderr, "next perror at %p\n", libc_perror);
535 | 
536 | 	libc_strerror_r = dlsym(RTLD_NEXT,"strerror_r");
537 | 	if (!libc_strerror_r) {
538 | 		fprintf(stderr, "Failed to look up next strerror_r\n");
545 | 	//fprintf(stderr, "next strerror_r at %p\n", libc_strerror_r);
546 | 
547 | #if 0
548 | 	libc_xpg_strerror_r = dlsym(RTLD_NEXT,"xpg_strerror_r");
549 | 	if (!libc_xpg_strerror_r) {
550 | 		fprintf(stderr, "Failed to look up next xpg_strerror_r\n");
{% endraw %}

```