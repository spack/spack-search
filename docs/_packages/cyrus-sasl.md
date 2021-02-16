---
name: "cyrus-sasl"
layout: package
next_package: googletest
previous_package: libquo
languages: ['c']
---
## 2.1.26
16 / 529 files match

 - [lib/dlopen.c](#libdlopenc)
 - [dlcompat-20010505/dlfcn.h](#dlcompat-20010505dlfcnh)
 - [dlcompat-20010505/dlopen.c](#dlcompat-20010505dlopenc)

### lib/dlopen.c

```c

{% raw %}
101 | dlopen(char *fname, int mode)
374 |     if (!(library = dlopen(file, flag))) {
376 | 		  "unable to dlopen %s: %s", file, dlerror());
{% endraw %}

```
### dlcompat-20010505/dlfcn.h

```c

{% raw %}
33 | extern void * dlopen(
{% endraw %}

```
### dlcompat-20010505/dlopen.c

```c

{% raw %}
60 | struct dlopen_handle {
63 |     int dlopen_mode;	/* current dlopen mode for this handle */
64 |     int dlopen_count;	/* number of times dlopen() called on this handle */
66 |     struct dlopen_handle *prev;
67 |     struct dlopen_handle *next;
69 | static struct dlopen_handle *dlopen_handles = NULL;
70 | static const struct dlopen_handle main_program_handle = {NULL};
183 | dlopen(
193 |     struct dlopen_handle *p;
199 |         DEBUG_PRINT2("libdl: dlopen(%s,0x%x) -> ", path, (unsigned int)mode);
240 | 	    p = dlopen_handles;
244 | 		    if((p->dlopen_mode & RTLD_UNSHARED) == RTLD_UNSHARED)
252 | 		    if((p->dlopen_mode & RTLD_LOCAL) == RTLD_LOCAL &&
256 | 			    p->dlopen_mode &= ~RTLD_LOCAL;
257 | 			    p->dlopen_mode |= RTLD_GLOBAL;
258 | 			    p->dlopen_count++;
269 | 		    p->dlopen_count++;
327 | 	    dlerror_pointer = "NSLinkModule() failed for dlopen()";
345 | 	p = malloc(sizeof(struct dlopen_handle));
347 | 	    dlerror_pointer = "can't allocate memory for the dlopen handle";
356 | 	    p->dlopen_mode = RTLD_GLOBAL;
358 | 	    p->dlopen_mode = RTLD_LOCAL;
359 | 	p->dlopen_mode |= (mode & RTLD_UNSHARED) |
362 | 	p->dlopen_count = 1;
365 | 	p->next = dlopen_handles;
366 | 	if(dlopen_handles != NULL)
367 | 	    dlopen_handles->prev = p;
368 | 	dlopen_handles = p;
389 |     struct dlopen_handle *dlopen_handle, *p;
395 | 	dlopen_handle = (struct dlopen_handle *)handle;
400 | 	if(dlopen_handle == (struct dlopen_handle *)&main_program_handle){
418 | 	p = dlopen_handles;
420 | 	    if(dlopen_handle == p){
463 |     struct dlopen_handle *p, *q;
471 | 	q = (struct dlopen_handle *)handle;
472 | 	p = dlopen_handles;
476 | 		p->dlopen_count--;
477 | 		if(p->dlopen_count != 0){
491 | 		if(p->dlopen_mode & RTLD_NODELETE)
493 | 		if(p->dlopen_mode & RTLD_LAZY_UNDEF)
504 | 		if(dlopen_handles == p)
505 | 		    dlopen_handles = p->next;
{% endraw %}

```