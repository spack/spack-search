---
name: "jemalloc"
layout: package
next_package: sst-macro
previous_package: alsa-lib
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.2.1
2 / 200 files match, 1 filtered matches.

 - [src/mutex.c](#srcmutexc)

### src/mutex.c

```c

{% raw %}
37 | pthread_create_once(void)
38 | {
39 | 
40 | 	pthread_create_fptr = dlsym(RTLD_NEXT, "pthread_create");
41 | 	if (pthread_create_fptr == NULL) {
42 | 		malloc_write("<jemalloc>: Error in dlsym(RTLD_NEXT, "
43 | 		    "\"pthread_create\")\n");
44 | 		abort();
{% endraw %}

```