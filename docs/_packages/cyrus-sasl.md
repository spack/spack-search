---
name: "cyrus-sasl"
layout: package
next_package: czmq
previous_package: curl
languages: ['c']
---
## 2.1.26
16 / 529 files match, 3 filtered matches.

 - [lib/dlopen.c](#libdlopenc)
 - [dlcompat-20010505/dlfcn.h](#dlcompat-20010505dlfcnh)
 - [dlcompat-20010505/dlopen.c](#dlcompat-20010505dlopenc)

### lib/dlopen.c

```c

{% raw %}
98 | typedef void * dll_func;
99 | 
100 | dll_handle
101 | dlopen(char *fname, int mode)
102 | {
103 |     shl_t h = shl_load(fname, BIND_DEFERRED, 0L);
371 |     newhead = sasl_ALLOC(sizeof(lib_list_t));
372 |     if(!newhead) return SASL_NOMEM;
373 | 
374 |     if (!(library = dlopen(file, flag))) {
375 | 	_sasl_log(NULL, SASL_LOG_ERR,
376 | 		  "unable to dlopen %s: %s", file, dlerror());
377 | 	sasl_FREE(newhead);
378 | 	return SASL_FAIL;
{% endraw %}

```
### dlcompat-20010505/dlfcn.h

```c

{% raw %}
30 | extern "C" {
31 | #endif
32 | 
33 | extern void * dlopen(
34 |     const char *path,
35 |     int mode);
{% endraw %}

```
### dlcompat-20010505/dlopen.c

```c

{% raw %}
57 | /*
58 |  * The structure of a dlopen() handle.
59 |  */
60 | struct dlopen_handle {
61 |     dev_t dev;		/* the path's device and inode number from stat(2) */
62 |     ino_t ino; 
63 |     int dlopen_mode;	/* current dlopen mode for this handle */
64 |     int dlopen_count;	/* number of times dlopen() called on this handle */
65 |     NSModule module;	/* the NSModule returned by NSLinkModule() */
66 |     struct dlopen_handle *prev;
67 |     struct dlopen_handle *next;
68 | };
69 | static struct dlopen_handle *dlopen_handles = NULL;
70 | static const struct dlopen_handle main_program_handle = {NULL};
71 | static char *dlerror_pointer = NULL;
72 | 
180 |  * dlopen() the MacOS X version of the FreeBSD dlopen() interface.
181 |  */
182 | void *
183 | dlopen(
184 | const char *path,
185 | int mode)
190 |     NSObjectFileImage objectFileImage;
191 |     NSObjectFileImageReturnCode ofile_result_code;
192 |     NSModule module;
193 |     struct dlopen_handle *p;
194 |     unsigned long options;
195 |     NSSymbol NSSymbol;
196 |     void (*init)(void);
197 |     char pathbuf[PATH_MAX];
198 | 
199 |         DEBUG_PRINT2("libdl: dlopen(%s,0x%x) -> ", path, (unsigned int)mode);
200 | 
201 | 	dlerror_pointer = NULL;
237 | 	 * for this path.
238 | 	 */
239 | 	if((mode & RTLD_UNSHARED) != RTLD_UNSHARED){
240 | 	    p = dlopen_handles;
241 | 	    while(p != NULL){
242 | 		if(p->dev == stat_buf.st_dev && p->ino == stat_buf.st_ino){
243 | 		    /* skip unshared handles */
244 | 		    if((p->dlopen_mode & RTLD_UNSHARED) == RTLD_UNSHARED)
245 | 			continue;
246 | 		    /*
249 | 		     * to a RTLD_GLOBAL.  Or just looking it up with
250 | 		     * RTLD_NOLOAD.
251 | 		     */
252 | 		    if((p->dlopen_mode & RTLD_LOCAL) == RTLD_LOCAL &&
253 | 		       (mode & RTLD_GLOBAL) == RTLD_GLOBAL){
254 | 			/* promote the handle */
255 | 			if(NSMakePrivateModulePublic(p->module) == TRUE){
256 | 			    p->dlopen_mode &= ~RTLD_LOCAL;
257 | 			    p->dlopen_mode |= RTLD_GLOBAL;
258 | 			    p->dlopen_count++;
259 | 			    DEBUG_PRINT1("%p\n", p);
260 | 			    return(p);
266 | 			    return(NULL);
267 | 			}
268 | 		    }
269 | 		    p->dlopen_count++;
270 | 		    DEBUG_PRINT1("%p\n", p);
271 | 		    return(p);
324 | 	module = NSLinkModule(objectFileImage, module_path, options);
325 | 	NSDestroyObjectFileImage(objectFileImage) ;
326 | 	if(module == NULL){
327 | 	    dlerror_pointer = "NSLinkModule() failed for dlopen()";
328 | 	    DEBUG_PRINT1("ERROR: %s\n", dlerror_pointer);
329 | 	    return(NULL);
342 | 	    }
343 | 	}
344 | 
345 | 	p = malloc(sizeof(struct dlopen_handle));
346 | 	if(p == NULL){
347 | 	    dlerror_pointer = "can't allocate memory for the dlopen handle";
348 | 	    DEBUG_PRINT1("ERROR: %s\n", dlerror_pointer);
349 | 	    return(NULL);
353 | 	p->dev = stat_buf.st_dev;
354 |         p->ino = stat_buf.st_ino;
355 | 	if(mode & RTLD_GLOBAL)
356 | 	    p->dlopen_mode = RTLD_GLOBAL;
357 | 	else
358 | 	    p->dlopen_mode = RTLD_LOCAL;
359 | 	p->dlopen_mode |= (mode & RTLD_UNSHARED) |
360 | 			  (mode & RTLD_NODELETE) |
361 | 			  (mode & RTLD_LAZY_UNDEF);
362 | 	p->dlopen_count = 1;
363 | 	p->module = module;
364 | 	p->prev = NULL;
365 | 	p->next = dlopen_handles;
366 | 	if(dlopen_handles != NULL)
367 | 	    dlopen_handles->prev = p;
368 | 	dlopen_handles = p;
369 | 
370 | 	/* call the init function if one exists */
386 | void * handle,
387 | const char *symbol)
388 | {
389 |     struct dlopen_handle *dlopen_handle, *p;
390 |     NSSymbol NSSymbol;
391 |     void *address;
392 | 
393 |         DEBUG_PRINT2("libdl: dlsym(%p,%s) -> ", handle, symbol);
394 | 
395 | 	dlopen_handle = (struct dlopen_handle *)handle;
396 | 
397 | 	/*
398 | 	 * If this is the handle for the main program do a global lookup.
399 | 	 */
400 | 	if(dlopen_handle == (struct dlopen_handle *)&main_program_handle){
401 | 	    if(NSIsSymbolNameDefined(symbol) == TRUE){
402 | 		NSSymbol = NSLookupAndBindSymbol(symbol);
415 | 	/*
416 | 	 * Find this handle and do a lookup in just this module.
417 | 	 */
418 | 	p = dlopen_handles;
419 | 	while(p != NULL){
420 | 	    if(dlopen_handle == p){
421 | 		NSSymbol = NSLookupSymbolInModule(p->module, symbol);
422 | 		if(NSSymbol != NULL){
460 | dlclose(
461 | void * handle)
462 | {
463 |     struct dlopen_handle *p, *q;
464 |     unsigned long options;
465 |     NSSymbol NSSymbol;
468 |         DEBUG_PRINT1("libdl: dlclose(%p) -> ", handle);
469 | 
470 | 	dlerror_pointer = NULL;
471 | 	q = (struct dlopen_handle *)handle;
472 | 	p = dlopen_handles;
473 | 	while(p != NULL){
474 | 	    if(p == q){
475 | 		/* if the dlopen() count is not zero we are done */
476 | 		p->dlopen_count--;
477 | 		if(p->dlopen_count != 0){
478 | 		    DEBUG_PRINT("OK");
479 | 		    return(0);
488 | 
489 | 		/* unlink the module for this handle */
490 | 		options = 0;
491 | 		if(p->dlopen_mode & RTLD_NODELETE)
492 | 		    options |= NSUNLINKMODULE_OPTION_KEEP_MEMORY_MAPPED;
493 | 		if(p->dlopen_mode & RTLD_LAZY_UNDEF)
494 | 		    options |= NSUNLINKMODULE_OPTION_RESET_LAZY_REFERENCES;
495 | 		if(NSUnLinkModule(p->module, options) == FALSE){
501 | 		    p->prev->next = p->next;
502 | 		if(p->next != NULL)
503 | 		    p->next->prev = p->prev;
504 | 		if(dlopen_handles == p)
505 | 		    dlopen_handles = p->next;
506 | 		free(p);
507 | 		DEBUG_PRINT("OK");
{% endraw %}

```