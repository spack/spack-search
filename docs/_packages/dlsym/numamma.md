---
name: "numamma"
layout: package
next_package: ocaml
previous_package: nspr
library_name: dlsym
matches: ['dlsym']
languages: ['c']
---
## 1.1.1
2 / 49 files match, 2 filtered matches.

 - [src/mem_intercept.c](#srcmem_interceptc)
 - [src/mem_run.c](#srcmem_runc)

### src/mem_intercept.c

```c

{% raw %}
91 |        */								\
92 |       PROTECT_FROM_RECURSION;						\
93 |       {									\
94 | 	CALLBACK = dlsym(RTLD_NEXT, STRINGIFY(FNAME));			\
95 | 	char* error;							\
96 | 	if ((error = dlerror()) != NULL) {				\
146 | 
147 |   if (!librealloc) {
148 |     PROTECT_FROM_RECURSION;
149 |     librealloc = dlsym(RTLD_NEXT, "realloc");
150 |     UNPROTECT_FROM_RECURSION;
151 |     char* error;
243 | 
244 |   if (!libfree) {
245 |     PROTECT_FROM_RECURSION;
246 |     libfree = dlsym(RTLD_NEXT, "free");
247 |     UNPROTECT_FROM_RECURSION;
248 |     char* error;
364 |   __args->arg = arg;
365 | 
366 |   if (!libpthread_create) {
367 |     libpthread_create = dlsym(RTLD_NEXT, "pthread_create");
368 |   }
369 | 
503 | static void __memory_init(void) {
504 |   PROTECT_FROM_RECURSION;
505 | 
506 |   libmalloc = dlsym(RTLD_NEXT, "malloc");
507 |   libcalloc = dlsym(RTLD_NEXT, "calloc");
508 |   librealloc = dlsym(RTLD_NEXT, "realloc");
509 |   libfree = dlsym(RTLD_NEXT, "free");
510 |   libpthread_create = dlsym(RTLD_NEXT, "pthread_create");
511 |   libpthread_exit = dlsym(RTLD_NEXT, "pthread_exit");
512 | 
513 |   read_settings();
{% endraw %}

```
### src/mem_run.c

```c

{% raw %}
154 |      */
155 |     PROTECT_FROM_RECURSION;
156 |     {
157 |       libmalloc = dlsym(RTLD_NEXT, "malloc");
158 |       char* error;
159 |       if ((error = dlerror()) != NULL) {
208 | 
209 |   //  FUNCTION_ENTRY;
210 |   if (!librealloc) {
211 |     librealloc = dlsym(RTLD_NEXT, "realloc");
212 |     char* error;
213 |     if ((error = dlerror()) != NULL) {
299 | void free(void* ptr) {
300 |   nb_free++;
301 |   if (!libfree) {
302 |     libfree = dlsym(RTLD_NEXT, "free");
303 |     char* error;
304 |     if ((error = dlerror()) != NULL) {
420 |   __args->thread_rank= thread_rank;
421 | 
422 |   if (!libpthread_create) {
423 |     libpthread_create = dlsym(RTLD_NEXT, "pthread_create");
424 |   }
425 | 
1078 | #else
1079 |     printf("[Mem_run] malloc interception is disabled\n");
1080 | #endif
1081 |   libmalloc = dlsym(RTLD_NEXT, "malloc");
1082 |   libcalloc = dlsym(RTLD_NEXT, "calloc");
1083 |   librealloc = dlsym(RTLD_NEXT, "realloc");
1084 |   libfree = dlsym(RTLD_NEXT, "free");
1085 |   libpthread_create = dlsym(RTLD_NEXT, "pthread_create");
1086 |   libpthread_exit = dlsym(RTLD_NEXT, "pthread_exit");
1087 | 
1088 |   nb_nodes = numa_num_configured_nodes();
{% endraw %}

```