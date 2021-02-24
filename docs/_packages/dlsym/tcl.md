---
name: "tcl"
layout: package
next_package: dimemas
previous_package: libpam
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 8.6.6
6 / 1481 files match, 6 filtered matches.

 - [compat/dlfcn.h](#compatdlfcnh)
 - [pkgs/sqlite3.13.0/compat/sqlite3/sqlite3.c](#pkgssqlite3130compatsqlite3sqlite3c)
 - [unix/tclLoadDyld.c](#unixtclloaddyldc)
 - [unix/tclLoadDl.c](#unixtclloaddlc)
 - [unix/tclLoadAix.c](#unixtclloadaixc)
 - [macosx/tclMacOSXBundle.c](#macosxtclmacosxbundlec)

### compat/dlfcn.h

```c

{% raw %}
46 | };
47 | 
48 | void *dlopen (const char *path, int mode);
49 | void *dlsym (void *handle, const char *symbol);
50 | char *dlerror (void);
51 | int dlclose (void *handle);
{% endraw %}

```
### pkgs/sqlite3.13.0/compat/sqlite3/sqlite3.c

```c

{% raw %}
35310 |   */
35311 |   void (*(*x)(void*,const char*))(void);
35312 |   UNUSED_PARAMETER(NotUsed);
35313 |   x = (void(*(*)(void*,const char*))(void))dlsym;
35314 |   return (*x)(p, zSym);
35315 | }
{% endraw %}

```
### unix/tclLoadDyld.c

```c

{% raw %}
340 |     native = Tcl_UtfToExternalDString(NULL, symbol, -1, &ds);
341 |     if (dyldLoadHandle->dlHandle) {
342 | #if TCL_DYLD_USE_DLFCN
343 | 	proc = dlsym(dyldLoadHandle->dlHandle, native);
344 | 	if (!proc) {
345 | 	    errMsg = dlerror();
{% endraw %}

```
### unix/tclLoadDl.c

```c

{% raw %}
179 |      */
180 | 
181 |     native = Tcl_UtfToExternalDString(NULL, symbol, -1, &ds);
182 |     proc = dlsym(handle, native);	/* INTL: Native. */
183 |     if (proc == NULL) {
184 | 	Tcl_DStringInit(&newName);
185 | 	TclDStringAppendLiteral(&newName, "_");
186 | 	native = Tcl_DStringAppend(&newName, native, -1);
187 | 	proc = dlsym(handle, native);	/* INTL: Native. */
188 | 	Tcl_DStringFree(&newName);
189 |     }
{% endraw %}

```
### unix/tclLoadAix.c

```c

{% raw %}
208 |      * If there is a dl_info structure, call the init function.
209 |      */
210 | 
211 |     if (mp->info = (struct dl_info *)dlsym(mp, "dl_info")) {
212 | 	if (mp->info->init) {
213 | 	    mp->info->init();
221 |      * constructors (and later on dlclose destructors).
222 |      */
223 | 
224 |     if (mp->cdtors = (CdtorPtr) dlsym(mp, "__cdtors")) {
225 | 	while (mp->cdtors->init) {
226 | 	    mp->cdtors->init();
277 | }
278 | 
279 | void *
280 | dlsym(
281 |     void *handle,
282 |     const char *symbol)
297 |     }
298 | 
299 |     errvalid++;
300 |     strcpy(errbuf, "dlsym: undefined symbol ");
301 |     strcat(errbuf, symbol);
302 |     return NULL;
{% endraw %}

```
### macosx/tclMacOSXBundle.c

```c

{% raw %}
43 | /*
44 |  * Support for weakly importing dlfcn API.
45 |  */
46 | extern void *		dlsym(void *handle, const char *symbol)
47 | 			    WEAK_IMPORT_ATTRIBUTE;
48 | extern char *		dlerror(void) WEAK_IMPORT_ATTRIBUTE;
105 | 	if (tclMacOSXDarwinRelease >= 8)
106 | #endif
107 | 	{
108 | 	    openresourcemap = dlsym(RTLD_NEXT,
109 | 		    "CFBundleOpenBundleResourceMap");
110 | #ifdef TCL_DEBUG_LOAD
111 | 	    if (!openresourcemap) {
112 | 		const char *errMsg = dlerror();
113 | 
114 | 		TclLoadDbgMsg("dlsym() failed: %s", errMsg);
115 | 	    }
116 | #endif /* TCL_DEBUG_LOAD */
{% endraw %}

```