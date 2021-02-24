---
name: "apr"
layout: package
next_package: likwid
previous_package: ngspice
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.7.0
7 / 467 files match, 4 filtered matches.

 - [include/arch/aix/apr_arch_dso.h](#includearchaixapr_arch_dsoh)
 - [dso/unix/dso.c](#dsounixdsoc)
 - [dso/aix/dso.c](#dsoaixdsoc)
 - [dso/netware/dso.c](#dsonetwaredsoc)

### include/arch/aix/apr_arch_dso.h

```c

{% raw %}
25 | #if APR_HAS_DSO
26 | 
27 | void *dlopen(const char *path, int mode);
28 | void *dlsym(void *handle, const char *symbol);
29 | const char *dlerror(void);
30 | int dlclose(void *handle);
{% endraw %}

```
### dso/unix/dso.c

```c

{% raw %}
218 |     void *retval;
219 |     char *symbol = (char*)malloc(sizeof(char)*(strlen(symname)+2));
220 |     sprintf(symbol, "_%s", symname);
221 |     retval = dlsym(handle->handle, symbol);
222 |     free(symbol);
223 | #elif defined(SEQUENT) || defined(SNI)
224 |     void *retval = dlsym(handle->handle, (char *)symname);
225 | #else
226 |     void *retval = dlsym(handle->handle, symname);
227 | #endif /* DLSYM_NEEDS_UNDERSCORE */
228 | 
{% endraw %}

```
### dso/aix/dso.c

```c

{% raw %}
154 |                                       apr_dso_handle_t *handle, 
155 |                                       const char *symname)
156 | {
157 |     void *retval = dlsym(handle->handle, symname);
158 | 
159 |     if (retval == NULL) {
336 |     /*
337 |      * If there is a dl_info structure, call the init function.
338 |      */
339 |     if (mp->info = (struct dl_info *) dlsym(mp, "dl_info")) {
340 | 	if (mp->info->init)
341 | 	    (*mp->info->init) ();
346 |      * If the shared object was compiled using xlC we will need
347 |      * to call static constructors (and later on dlclose destructors).
348 |      */
349 |     if (mp->cdtors = (CdtorPtr) dlsym(mp, "__cdtors")) {
350 | 	CdtorPtr cp = mp->cdtors;
351 | 	while (cp->init || cp->term) {
360 | 	 * funciton.  --jwe
361 | 	 */
362 |     }
363 |     else if (mp->gcc_ctor = (GccCDtorPtr) dlsym(mp, "_GLOBAL__DI")) {
364 | 	(*mp->gcc_ctor) ();
365 | 	mp->gcc_dtor = (GccCDtorPtr) dlsym(mp, "_GLOBAL__DD");
366 |     }
367 |     else
408 |     }
409 | }
410 | 
411 | void *dlsym(void *handle, const char *symbol)
412 | {
413 |     register ModulePtr mp = (ModulePtr) handle;
422 | 	if (strcmp(ep->name, symbol) == 0)
423 | 	    return ep->addr;
424 |     errvalid++;
425 |     strcpy(errbuf, "dlsym: undefined symbol ");
426 |     strcat(errbuf, symbol);
427 |     return NULL;
{% endraw %}

```
### dso/netware/dso.c

```c

{% raw %}
107 |                                       const char *symname)
108 | {
109 |     sym_list *symbol = NULL;
110 |     void *retval = dlsym(handle->handle, symname);
111 | 
112 |     if (retval == NULL) {
{% endraw %}

```