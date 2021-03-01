---
name: "tcl"
layout: package
next_package: tfel
previous_package: tau
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 8.6.6
9 / 1481 files match, 6 filtered matches.

 - [compat/dlfcn.h](#compatdlfcnh)
 - [pkgs/sqlite3.13.0/compat/sqlite3/sqlite3.c](#pkgssqlite3130compatsqlite3sqlite3c)
 - [unix/tclLoadDyld.c](#unixtclloaddyldc)
 - [unix/tclLoadDl.c](#unixtclloaddlc)
 - [unix/tclUnixInit.c](#unixtclunixinitc)
 - [unix/tclLoadAix.c](#unixtclloadaixc)

### compat/dlfcn.h

```c

{% raw %}
45 | 	void (*fini) (void);
46 | };
47 | 
48 | void *dlopen (const char *path, int mode);
49 | void *dlsym (void *handle, const char *symbol);
50 | char *dlerror (void);
{% endraw %}

```
### pkgs/sqlite3.13.0/compat/sqlite3/sqlite3.c

```c

{% raw %}
35270 | #include <dlfcn.h>
35271 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
35272 |   UNUSED_PARAMETER(NotUsed);
35273 |   return dlopen(zFilename, RTLD_NOW | RTLD_LOCAL);
35274 | }
35275 | 
{% endraw %}

```
### unix/tclLoadDyld.c

```c

{% raw %}
171 |     Tcl_DString ds;
172 |     const char *nativePath, *nativeFileName = NULL;
173 | #if TCL_DYLD_USE_DLFCN
174 |     int dlopenflags = 0;
175 | #endif /* TCL_DYLD_USE_DLFCN */
176 | 
190 |      */
191 | 
192 |     if (flags & TCL_LOAD_GLOBAL) {
193 |     	dlopenflags |= RTLD_GLOBAL;
194 |     } else {
195 |     	dlopenflags |= RTLD_LOCAL;
196 |     }
197 |     if (flags & TCL_LOAD_LAZY) {
198 |     	dlopenflags |= RTLD_LAZY;
199 |     } else {
200 |     	dlopenflags |= RTLD_NOW;
201 |     }
202 |     dlHandle = dlopen(nativePath, dlopenflags);
203 |     if (!dlHandle) {
204 | 	/*
207 | 	 * path.
208 | 	 */
209 | 
210 | 	dlHandle = dlopen(nativeFileName, dlopenflags);
211 | 	if (!dlHandle) {
212 | 	    errMsg = dlerror();
{% endraw %}

```
### unix/tclLoadDl.c

```c

{% raw %}
74 |     void *handle;
75 |     Tcl_LoadHandle newHandle;
76 |     const char *native;
77 |     int dlopenflags = 0;
78 | 
79 |     /*
87 |      * Use (RTLD_NOW|RTLD_LOCAL) as default, see [Bug #3216070]
88 |      */
89 |     if (flags & TCL_LOAD_GLOBAL) {
90 |     	dlopenflags |= RTLD_GLOBAL;
91 |     } else {
92 |     	dlopenflags |= RTLD_LOCAL;
93 |     }
94 |     if (flags & TCL_LOAD_LAZY) {
95 |     	dlopenflags |= RTLD_LAZY;
96 |     } else {
97 |     	dlopenflags |= RTLD_NOW;
98 |     }
99 |     handle = dlopen(native, dlopenflags);
100 |     if (handle == NULL) {
101 | 	/*
111 | 	/*
112 | 	 * Use (RTLD_NOW|RTLD_LOCAL) as default, see [Bug #3216070]
113 | 	 */
114 | 	handle = dlopen(native, dlopenflags);
115 | 	Tcl_DStringFree(&ds);
116 |     }
{% endraw %}

```
### unix/tclUnixInit.c

```c

{% raw %}
406 |      * Find local symbols. Don't report an error if we fail.
407 |      */
408 | 
409 |     (void) dlopen(NULL, RTLD_NOW);			/* INTL: Native. */
410 | #endif
411 | 
{% endraw %}

```
### unix/tclLoadAix.c

```c

{% raw %}
93 | static void *findMain(void);
94 | 
95 | void *
96 | dlopen(
97 |     const char *path,
98 |     int mode)
146 | 	free(mp->name);
147 | 	free(mp);
148 | 	errvalid++;
149 | 	strcpy(errbuf, "dlopen: ");
150 | 	strcat(errbuf, path);
151 | 	strcat(errbuf, ": ");
{% endraw %}

```